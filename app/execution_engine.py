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

MAX_SESSIONS = 100
SESSION_TTL_SECONDS = 3600  # 1 hora
EXECUTION_TIMEOUT_SECONDS = 30
MAX_CODE_LENGTH = 20_000  # 20 KB


@dataclass
class RuntimeSession:
    namespace: dict[str, Any] = field(default_factory=dict)
    last_used: float = field(default_factory=time.time)


_SESSIONS: dict[str, RuntimeSession] = {}
_SESSIONS_LOCK = threading.Lock()


def _evict_stale_sessions() -> None:
    now = time.time()
    with _SESSIONS_LOCK:
        stale = [sid for sid, s in _SESSIONS.items() if now - s.last_used > SESSION_TTL_SECONDS]
        for sid in stale:
            _SESSIONS.pop(sid, None)
        # Si aún hay demasiadas, eliminar las más antiguas
        if len(_SESSIONS) > MAX_SESSIONS:
            sorted_ids = sorted(_SESSIONS, key=lambda k: _SESSIONS[k].last_used)
            for sid in sorted_ids[:len(_SESSIONS) - MAX_SESSIONS]:
                _SESSIONS.pop(sid, None)


def get_session(session_id: str) -> RuntimeSession:
    _evict_stale_sessions()
    with _SESSIONS_LOCK:
        session = _SESSIONS.get(session_id)
        if session is None:
            session = RuntimeSession(namespace={"__name__": "__main__"})
            _SESSIONS[session_id] = session
        session.last_used = time.time()
        return session


def reset_session(session_id: str) -> None:
    with _SESSIONS_LOCK:
        _SESSIONS.pop(session_id, None)


def _capture_figures() -> list[str]:
    images: list[str] = []
    for fig_num in plt.get_fignums():
        fig = plt.figure(fig_num)
        buffer = BytesIO()
        fig.savefig(buffer, format="png", bbox_inches="tight")
        buffer.seek(0)
        images.append(base64.b64encode(buffer.read()).decode("utf-8"))
        plt.close(fig)
    return images


COMMON_PRELOAD = """
import math
import statistics
import pandas as pd
import matplotlib.pyplot as plt
"""


def _execute_with_timeout(code: str, session_namespace: dict, stdout_buffer: StringIO, response: dict) -> None:
    try:
        tree = ast.parse(code, mode="exec")
        body = tree.body
        last_expr = None
        if body and isinstance(body[-1], ast.Expr):
            last_expr = ast.Expression(body.pop().value)

        with redirect_stdout(stdout_buffer):
            if body:
                module = ast.Module(body=body, type_ignores=[])
                # El runner de laboratorio necesita ejecutar codigo arbitrario del alumno.
                # Esta excepcion de Bandit es intencional y esta documentada en SECURITY.md.
                exec(compile(module, "<bootcamp-cell>", "exec"), session_namespace)  # nosec
            if last_expr is not None:
                # Se evalua solo la ultima expresion para emular un notebook local de aula.
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
    if len(code) > MAX_CODE_LENGTH:
        return {"stdout": "", "result": None, "error": f"Código demasiado largo (máx {MAX_CODE_LENGTH} caracteres).", "images": []}

    session = get_session(session_id)
    stdout_buffer = StringIO()
    plt.close("all")

    if not session.namespace.get("_bootcamp_preloaded"):
        # Precarga controlada de ayudas comunes para el laboratorio local. Ver SECURITY.md.
        exec(COMMON_PRELOAD, session.namespace)  # nosec
        session.namespace["_bootcamp_preloaded"] = True

    response: dict[str, Any] = {"stdout": "", "result": None, "error": None, "images": []}

    thread = threading.Thread(target=_execute_with_timeout, args=(code, session.namespace, stdout_buffer, response), daemon=True)
    thread.start()
    thread.join(timeout=EXECUTION_TIMEOUT_SECONDS)

    if thread.is_alive():
        reset_session(session_id)
        response["error"] = f"Tiempo de ejecución excedido ({EXECUTION_TIMEOUT_SECONDS}s). La sesión fue reiniciada."

    return response
