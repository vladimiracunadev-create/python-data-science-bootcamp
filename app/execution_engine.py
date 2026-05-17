"""Motor de ejecución para el laboratorio local del bootcamp.

Este módulo resuelve la experiencia tipo notebook dentro de la app Flask:
conserva estado por sesión, precarga herramientas frecuentes, captura salida de
texto e imágenes de matplotlib y corta ejecuciones largas para recuperar el lab.
"""

from __future__ import annotations

import ast
import base64
import threading
import time
import traceback
from contextlib import redirect_stdout
from dataclasses import dataclass, field
from io import BytesIO, StringIO
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Límites del motor de ejecución — cada valor responde a una restricción concreta:
#   MAX_SESSIONS=100      : techo para evitar OOM si muchas pestañas crean sesiones
#                           y las abandonan; 100 namespaces en RAM es razonable.
#   SESSION_TTL_SECONDS   : 1 hora cubre el tiempo de una clase; las sesiones más
#                           antiguas se expulsan automáticamente en el siguiente ciclo.
#   EXECUTION_TIMEOUT     : 30 s es suficiente para ejercicios docentes; corta loops
#                           infinitos del alumno sin bloquear el lab indefinidamente.
#   MAX_CODE_LENGTH=20 KB : límite razonable para el contenido de una celda de clase;
#                           rechaza payloads anómalos antes de llegar al exec().
MAX_SESSIONS = 100
SESSION_TTL_SECONDS = 3600  # 1 hora
EXECUTION_TIMEOUT_SECONDS = 30
MAX_CODE_LENGTH = 20_000  # 20 KB


@dataclass
class RuntimeSession:
    """Estado persistente de una sesión de ejecución del laboratorio.

    Qué resuelve:
        Permite que varias celdas compartan variables como en un notebook real,
        manteniendo además la última vez de uso para poder expulsar sesiones viejas.
    """

    namespace: dict[str, Any] = field(default_factory=dict)
    last_used: float = field(default_factory=time.time)


_SESSIONS: dict[str, RuntimeSession] = {}
_SESSIONS_LOCK = threading.Lock()


# Se precargan las librerías más usadas en el bootcamp para dos fines:
#   1. Reducir el tiempo de primera ejecución: importar pandas y matplotlib
#      en frío puede tardar varios segundos, lo que genera confusión en clase.
#   2. Evitar que el alumno tenga que escribir los imports en cada celda,
#      replicando la experiencia de un entorno Jupyter ya inicializado.
COMMON_PRELOAD = """
import math
import statistics
import pandas as pd
import matplotlib.pyplot as plt
"""


def _evict_stale_sessions() -> None:
    """Limpia sesiones vencidas y limita el total de sesiones activas.

    Qué resuelve:
        Evita que el laboratorio local acumule memoria indefinidamente cuando
        varios alumnos o pruebas crean sesiones y luego las abandonan.
    """
    now = time.time()
    with _SESSIONS_LOCK:
        stale = [sid for sid, session in _SESSIONS.items() if now - session.last_used > SESSION_TTL_SECONDS]
        for sid in stale:
            _SESSIONS.pop(sid, None)

        if len(_SESSIONS) > MAX_SESSIONS:
            sorted_ids = sorted(_SESSIONS, key=lambda key: _SESSIONS[key].last_used)
            overflow = len(_SESSIONS) - MAX_SESSIONS
            for sid in sorted_ids[:overflow]:
                _SESSIONS.pop(sid, None)


def get_session(session_id: str) -> RuntimeSession:
    """Obtiene o crea una sesión de ejecución identificada por notebook.

    Qué resuelve:
        Da continuidad entre celdas para que el usuario pueda definir variables,
        reutilizarlas y seguir trabajando como en un entorno de clase interactivo.
    """
    _evict_stale_sessions()
    with _SESSIONS_LOCK:
        session = _SESSIONS.get(session_id)
        if session is None:
            session = RuntimeSession(namespace={"__name__": "__main__"})
            _SESSIONS[session_id] = session
        session.last_used = time.time()
        return session


def reset_session(session_id: str) -> None:
    """Elimina una sesión para devolver el laboratorio a un estado limpio."""
    with _SESSIONS_LOCK:
        _SESSIONS.pop(session_id, None)


def _capture_figures() -> list[str]:
    """Convierte figuras activas de matplotlib en PNG base64.

    Qué resuelve:
        Permite que la interfaz web muestre gráficos generados en el backend sin
        escribir archivos temporales ni depender de un entorno gráfico local.
    """
    images: list[str] = []
    for fig_num in plt.get_fignums():
        fig = plt.figure(fig_num)
        buffer = BytesIO()
        fig.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)
        images.append(base64.b64encode(buffer.read()).decode("utf-8"))
        plt.close(fig)
    return images


def _execute_with_timeout(
    code: str,
    session_namespace: dict[str, Any],
    stdout_buffer: StringIO,
    response: dict[str, Any],
) -> None:
    """Ejecuta una celda, capturando stdout, resultado final y errores.

    Qué resuelve:
        Separa la lógica de ejecución del hilo principal para que `execute_code`
        pueda aplicar timeout y devolver una respuesta estructurada a la UI.
    """
    try:
        tree = ast.parse(code, mode="exec")
        body = tree.body
        last_expr = None
        # Truco AST para emular el comportamiento Out[n] de Jupyter:
        # si la última sentencia es una expresión (no una asignación ni un
        # statement), se extrae del árbol y se evalúa con `eval` en lugar de
        # `exec`, lo que permite capturar su valor de retorno y mostrarlo
        # como resultado de celda sin necesidad de un `print()` explícito.
        if body and isinstance(body[-1], ast.Expr):
            last_expr = ast.Expression(body.pop().value)

        with redirect_stdout(stdout_buffer):
            if body:
                module = ast.Module(body=body, type_ignores=[])
                # Riesgo aceptado y documentado: esta app es local-only; no existe
                # un atacante remoto que pueda enviar código. El alumno ejecuta
                # su propio código en su propia máquina, igual que con Jupyter.
                exec(compile(module, "<bootcamp-cell>", "exec"), session_namespace)  # nosec
            if last_expr is not None:
                # `eval` sobre la última expresión captura el valor de retorno
                # sin imprimirlo, replicando la salida Out[n] de los notebooks.
                result = eval(compile(last_expr, "<bootcamp-cell>", "eval"), session_namespace)  # nosec
                if result is not None:
                    response["result"] = repr(result)

        response["stdout"] = stdout_buffer.getvalue()
        response["images"] = _capture_figures()
    except Exception:
        response["stdout"] = stdout_buffer.getvalue()
        response["error"] = traceback.format_exc()
        response["images"] = _capture_figures()


def execute_code(session_id: str, code: str) -> dict[str, Any]:
    """Ejecuta código del alumno dentro de una sesión persistente.

    Qué resuelve:
        Entrega una única interfaz para la app web: valida el tamaño del código,
        prepara dependencias frecuentes, aplica timeout y devuelve stdout,
        resultado, errores e imágenes en un mismo payload.
    """
    if len(code) > MAX_CODE_LENGTH:
        return {
            "stdout": "",
            "result": None,
            "error": f"Código demasiado largo (máx {MAX_CODE_LENGTH} caracteres).",
            "images": [],
        }

    session = get_session(session_id)
    stdout_buffer = StringIO()
    plt.close("all")

    if not session.namespace.get("_bootcamp_preloaded"):
        # Precargamos utilidades comunes para reducir fricción en la práctica.
        exec(COMMON_PRELOAD, session.namespace)  # nosec
        session.namespace["_bootcamp_preloaded"] = True

    response: dict[str, Any] = {"stdout": "", "result": None, "error": None, "images": []}

    thread = threading.Thread(
        target=_execute_with_timeout,
        args=(code, session.namespace, stdout_buffer, response),
        daemon=True,
    )
    thread.start()
    thread.join(timeout=EXECUTION_TIMEOUT_SECONDS)

    if thread.is_alive():
        # Si una celda se cuelga, reiniciamos la sesión para recuperar el entorno.
        reset_session(session_id)
        response["error"] = (
            f"Tiempo de ejecución excedido ({EXECUTION_TIMEOUT_SECONDS}s). "
            "La sesión fue reiniciada."
        )

    return response
