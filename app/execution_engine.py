from __future__ import annotations

import ast
import base64
from contextlib import redirect_stdout
from dataclasses import dataclass, field
from io import BytesIO, StringIO
from typing import Any
import traceback

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


@dataclass
class RuntimeSession:
    namespace: dict[str, Any] = field(default_factory=dict)


_SESSIONS: dict[str, RuntimeSession] = {}


def get_session(session_id: str) -> RuntimeSession:
    session = _SESSIONS.get(session_id)
    if session is None:
        session = RuntimeSession(namespace={"__name__": "__main__"})
        _SESSIONS[session_id] = session
    return session


def reset_session(session_id: str) -> None:
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


def execute_code(session_id: str, code: str) -> dict[str, Any]:
    session = get_session(session_id)
    stdout_buffer = StringIO()
    plt.close("all")

    if not session.namespace.get("_bootcamp_preloaded"):
        exec(COMMON_PRELOAD, session.namespace)
        session.namespace["_bootcamp_preloaded"] = True

    response = {"stdout": "", "result": None, "error": None, "images": []}

    try:
        tree = ast.parse(code, mode="exec")
        body = tree.body
        last_expr = None
        if body and isinstance(body[-1], ast.Expr):
            last_expr = ast.Expression(body.pop().value)

        with redirect_stdout(stdout_buffer):
            if body:
                module = ast.Module(body=body, type_ignores=[])
                exec(compile(module, "<bootcamp-cell>", "exec"), session.namespace)
            if last_expr is not None:
                result = eval(compile(last_expr, "<bootcamp-cell>", "eval"), session.namespace)
                if result is not None:
                    response["result"] = repr(result)

        response["stdout"] = stdout_buffer.getvalue()
        response["images"] = _capture_figures()
        return response
    except Exception:
        response["stdout"] = stdout_buffer.getvalue()
        response["error"] = traceback.format_exc()
        response["images"] = _capture_figures()
        return response
