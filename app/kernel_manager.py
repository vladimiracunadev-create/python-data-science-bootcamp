"""Gestor de kernels IPython para el laboratorio Flask del programa.

Qué resuelve:
    Reemplaza el `execution_engine` basado en `exec()` por kernels Jupyter reales
    (jupyter_client + ipykernel). Esto habilita salidas ricas (HTML, imágenes,
    widgets), aislamiento por proceso y la semántica Out[n] nativa de Jupyter.

    Cada kernel vive en su propio proceso. La app Flask interactúa con él vía
    `BlockingKernelClient` sobre sockets ZMQ. El estado se mantiene en un dict
    protegido por un RLock; las operaciones bloqueantes (drenar iopub) se hacen
    fuera del lock para no serializar todas las ejecuciones del lab.
"""

from __future__ import annotations

import atexit
import logging
import queue
import threading
import time
import uuid
from typing import Any

from jupyter_client import KernelManager
from jupyter_client.blocking.client import BlockingKernelClient

logger = logging.getLogger(__name__)

# Límites del gestor — cada valor responde a una restricción concreta:
#   MAX_KERNELS=50              : techo de procesos kernel simultáneos. Cada uno
#                                 consume ~80-150 MB RAM, así que 50 = ~5-7 GB en
#                                 el peor caso, suficiente para una clase entera.
#   KERNEL_TTL_SECONDS=3600     : cubre el tiempo de una clase típica; kernels más
#                                 viejos se apagan automáticamente para liberar RAM.
#   DEFAULT_EXECUTION_TIMEOUT   : 60s es 2× el del exec engine porque celdas reales
#                                 con pandas/sklearn pueden tardar más.
#   MAX_CODE_LENGTH=200_000     : 10× el exec engine ya que notebooks reales tienen
#                                 celdas más grandes (datos pegados, código generado).
MAX_KERNELS = 50
KERNEL_TTL_SECONDS = 3600
DEFAULT_EXECUTION_TIMEOUT = 60
MAX_CODE_LENGTH = 200_000


_KERNELS: dict[str, dict[str, Any]] = {}
_LOCK = threading.RLock()


def _evict_stale() -> None:
    """Apaga kernels vencidos y aplica el techo MAX_KERNELS.

    Qué resuelve:
        Evita que el lab acumule procesos kernel indefinidamente cuando varios
        alumnos abren pestañas y las abandonan sin cerrar la sesión.
    """
    now = time.time()
    to_kill: list[str] = []
    with _LOCK:
        stale = [kid for kid, entry in _KERNELS.items() if now - entry["last_used"] > KERNEL_TTL_SECONDS]
        to_kill.extend(stale)
        remaining = [kid for kid in _KERNELS if kid not in stale]
        if len(remaining) > MAX_KERNELS:
            sorted_ids = sorted(remaining, key=lambda k: _KERNELS[k]["last_used"])
            overflow = len(remaining) - MAX_KERNELS
            to_kill.extend(sorted_ids[:overflow])

    for kid in to_kill:
        try:
            shutdown(kid)
        except Exception:  # noqa: BLE001
            logger.exception("Error apagando kernel %s en evicción", kid)


def start_kernel() -> str:
    """Arranca un kernel IPython nuevo y devuelve su identificador.

    Qué resuelve:
        Encapsula el ciclo de vida de jupyter_client (start_kernel + cliente
        bloqueante + canales) para que el resto de la app trabaje con un id opaco.
    """
    _evict_stale()
    km = KernelManager()
    km.start_kernel()
    kc: BlockingKernelClient = km.client()
    kc.start_channels()
    try:
        kc.wait_for_ready(timeout=30)
    except RuntimeError:
        kc.stop_channels()
        km.shutdown_kernel(now=True)
        raise

    kernel_id = uuid.uuid4().hex
    now = time.time()
    with _LOCK:
        _KERNELS[kernel_id] = {
            "km": km,
            "kc": kc,
            "started_at": now,
            "last_used": now,
            "executions": 0,
            "exec_lock": threading.Lock(),
        }
    logger.info("Kernel iniciado %s", kernel_id)
    return kernel_id


def list_kernels() -> list[dict[str, Any]]:
    """Lista metadatos de los kernels vivos.

    Qué resuelve:
        Da a la UI de admin del lab visibilidad de los procesos kernel activos
        sin exponer los objetos internos KernelManager/Client.
    """
    with _LOCK:
        return [
            {
                "kernel_id": kid,
                "started_at": entry["started_at"],
                "last_used": entry["last_used"],
                "code_executions": entry["executions"],
            }
            for kid, entry in _KERNELS.items()
        ]


def _get_entry(kernel_id: str) -> dict[str, Any]:
    """Devuelve el entry interno o lanza KeyError. Pensado para uso bajo lock."""
    entry = _KERNELS.get(kernel_id)
    if entry is None:
        raise KeyError(f"kernel desconocido: {kernel_id}")
    return entry


def execute(kernel_id: str, code: str, timeout: float = DEFAULT_EXECUTION_TIMEOUT) -> dict[str, Any]:
    """Ejecuta código sobre el kernel y devuelve un payload estructurado.

    Qué resuelve:
        Traduce el protocolo de mensajería de Jupyter (iopub/shell) al formato
        de outputs estilo notebook que la UI sabe renderizar, aplicando timeout
        con interrupción cooperativa al kernel.
    """
    if len(code) > MAX_CODE_LENGTH:
        raise ValueError(f"Código demasiado largo (máx {MAX_CODE_LENGTH} caracteres).")

    _evict_stale()

    # Tomamos el lock SOLO para sacar referencias y bumpear contadores; nunca lo
    # mantenemos durante el drenado bloqueante de iopub, porque eso serializaría
    # todas las ejecuciones del lab a través de un único mutex global.
    with _LOCK:
        entry = _get_entry(kernel_id)
        km: KernelManager = entry["km"]
        kc: BlockingKernelClient = entry["kc"]
        exec_lock: threading.Lock = entry["exec_lock"]
        entry["last_used"] = time.time()
        entry["executions"] += 1

    outputs: list[dict[str, Any]] = []
    status = "ok"
    execution_count: int | None = None

    # Un mismo kernel no soporta dos `execute_request` simultáneos sobre el
    # mismo cliente: las respuestas iopub se mezclarían. Serializamos por
    # kernel, no globalmente.
    with exec_lock:
        msg_id = kc.execute(code)
        deadline = time.time() + timeout
        idle_received = False
        reply_received = False
        timed_out = False

        while not (idle_received and reply_received):
            remaining = deadline - time.time()
            if remaining <= 0:
                timed_out = True
                break
            try:
                msg = kc.get_iopub_msg(timeout=min(remaining, 1.0))
            except queue.Empty:
                continue
            if msg.get("parent_header", {}).get("msg_id") != msg_id:
                continue

            msg_type = msg["msg_type"]
            content = msg["content"]

            if msg_type == "status":
                if content.get("execution_state") == "idle":
                    idle_received = True
            elif msg_type == "stream":
                outputs.append({"type": "stream", "name": content.get("name", "stdout"), "text": content.get("text", "")})
            elif msg_type == "execute_result":
                execution_count = content.get("execution_count", execution_count)
                outputs.append({"type": "execute_result", "data": content.get("data", {})})
            elif msg_type == "display_data":
                outputs.append({"type": "display_data", "data": content.get("data", {})})
            elif msg_type == "error":
                outputs.append(
                    {
                        "type": "error",
                        "ename": content.get("ename", ""),
                        "evalue": content.get("evalue", ""),
                        "traceback": content.get("traceback", []),
                    }
                )
                status = "error"
            elif msg_type == "execute_input":
                execution_count = content.get("execution_count", execution_count)

            # Drenamos shell oportunísticamente para capturar el execute_reply.
            if not reply_received:
                try:
                    reply = kc.get_shell_msg(timeout=0.01)
                    if reply.get("parent_header", {}).get("msg_id") == msg_id:
                        reply_received = True
                        reply_content = reply["content"]
                        reply_status = reply_content.get("status")
                        execution_count = reply_content.get("execution_count", execution_count)
                        if reply_status == "error" and status != "error":
                            status = "error"
                except queue.Empty:
                    pass

        if timed_out:
            logger.warning("Timeout de %ss en kernel %s; interrumpiendo", timeout, kernel_id)
            try:
                km.interrupt_kernel()
            except Exception:  # noqa: BLE001
                logger.exception("Falló interrupt_kernel sobre %s", kernel_id)
            # Gracia de 2s para drenar mensajes pendientes generados antes/después de la interrupción.
            grace_deadline = time.time() + 2.0
            while time.time() < grace_deadline:
                try:
                    msg = kc.get_iopub_msg(timeout=0.2)
                except queue.Empty:
                    continue
                if msg.get("parent_header", {}).get("msg_id") != msg_id:
                    continue
                msg_type = msg["msg_type"]
                content = msg["content"]
                if msg_type == "stream":
                    outputs.append({"type": "stream", "name": content.get("name", "stdout"), "text": content.get("text", "")})
                elif msg_type == "error":
                    outputs.append(
                        {
                            "type": "error",
                            "ename": content.get("ename", ""),
                            "evalue": content.get("evalue", ""),
                            "traceback": content.get("traceback", []),
                        }
                    )
                elif msg_type == "status" and content.get("execution_state") == "idle":
                    break
            # Distinguimos timeout (vencimos el reloj) de interrupted (interrupción
            # externa entregada antes del deadline): si vimos un KeyboardInterrupt
            # en outputs lo marcamos como interrupted, si no, como timeout.
            interrupted = any(
                out.get("type") == "error" and out.get("ename") == "KeyboardInterrupt" for out in outputs
            )
            status = "interrupted" if interrupted else "timeout"

    # Si hubo KeyboardInterrupt sin haber vencido el reloj (interrupción manual
    # vía `interrupt()`), reportamos status="interrupted" en lugar de "error".
    if status == "error" and any(
        out.get("type") == "error" and out.get("ename") == "KeyboardInterrupt" for out in outputs
    ):
        status = "interrupted"

    return {"outputs": outputs, "status": status, "execution_count": execution_count}


def interrupt(kernel_id: str) -> None:
    """Envía SIGINT al kernel para abortar la ejecución actual.

    Qué resuelve:
        Permite al alumno cancelar un loop largo sin perder el namespace,
        a diferencia de `restart` que sí lo borra todo.
    """
    with _LOCK:
        entry = _get_entry(kernel_id)
        km: KernelManager = entry["km"]
    km.interrupt_kernel()


def restart(kernel_id: str) -> None:
    """Reinicia el kernel preservando el mismo id pero borrando todo el estado.

    Qué resuelve:
        Cubre el caso en que el alumno corrompió el namespace (monkey-patched
        builtins, fugas de memoria, etc.) y necesita un entorno limpio sin
        renegociar un id nuevo con la UI.
    """
    with _LOCK:
        entry = _get_entry(kernel_id)
        km: KernelManager = entry["km"]
        kc: BlockingKernelClient = entry["kc"]

    kc.stop_channels()
    km.restart_kernel(now=True)
    new_kc = km.client()
    new_kc.start_channels()
    new_kc.wait_for_ready(timeout=30)

    with _LOCK:
        entry = _KERNELS.get(kernel_id)
        if entry is not None:
            entry["kc"] = new_kc
            entry["last_used"] = time.time()
            entry["executions"] = 0
            entry["exec_lock"] = threading.Lock()
    logger.info("Kernel reiniciado %s", kernel_id)


def shutdown(kernel_id: str) -> None:
    """Apaga un kernel y libera sus recursos.

    Qué resuelve:
        Cierra el proceso kernel y los canales ZMQ asociados; sin esto los
        procesos kernel quedarían huérfanos hasta que muera el proceso Flask.
    """
    with _LOCK:
        entry = _KERNELS.pop(kernel_id, None)
    if entry is None:
        return
    kc: BlockingKernelClient = entry["kc"]
    km: KernelManager = entry["km"]
    try:
        kc.stop_channels()
    except Exception:  # noqa: BLE001
        logger.exception("Error parando canales de %s", kernel_id)
    try:
        km.shutdown_kernel(now=True)
    except Exception:  # noqa: BLE001
        logger.exception("Error apagando kernel %s", kernel_id)
    logger.info("Kernel apagado %s", kernel_id)


def shutdown_all() -> None:
    """Apaga todos los kernels. Best-effort, usado al cierre de Flask."""
    with _LOCK:
        kernel_ids = list(_KERNELS.keys())
    for kid in kernel_ids:
        try:
            shutdown(kid)
        except Exception:  # noqa: BLE001
            logger.exception("Error en shutdown_all para %s", kid)


atexit.register(shutdown_all)
