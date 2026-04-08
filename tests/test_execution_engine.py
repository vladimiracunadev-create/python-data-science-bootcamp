"""Pruebas del motor de ejecución interactiva del bootcamp.

Validan que el backend conserve estado por sesión, capture stdout, reporte
errores y soporte la carga previa de utilidades comunes para el laboratorio.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.execution_engine import _SESSIONS, execute_code, reset_session


def test_execute_code_keeps_state_between_cells():
    reset_session("demo")
    execute_code("demo", "x = 10")
    result = execute_code("demo", "x + 5")
    assert result["result"] == "15"


def test_execute_code_captures_stdout():
    reset_session("stdout")
    result = execute_code("stdout", 'print("hola")')
    assert "hola" in result["stdout"]


def test_execute_code_handles_runtime_error():
    reset_session("err-test")
    result = execute_code("err-test", "1 / 0")
    assert result["error"] is not None
    assert "ZeroDivisionError" in result["error"]


def test_execute_code_captures_expression_result():
    reset_session("expr")
    result = execute_code("expr", "[i**2 for i in range(5)]")
    assert result["result"] is not None
    assert "16" in result["result"]


def test_execute_code_preloads_pandas():
    reset_session("pandas-preload")
    result = execute_code("pandas-preload", "import pandas as pd; type(pd.DataFrame()).__name__")
    assert result["result"] == "'DataFrame'"


def test_reset_session_removes_state():
    reset_session("state-test")
    execute_code("state-test", "secret = 42")
    reset_session("state-test")
    result = execute_code("state-test", "secret")
    assert result["error"] is not None


def test_reset_session_nonexistent_does_not_raise():
    reset_session("sesion-que-no-existe-xyz")


def test_session_eviction_does_not_crash():
    # Este stress mínimo asegura que crear muchas sesiones no rompe el runner.
    for i in range(50):
        execute_code(f"evict-stress-{i}", "pass")
    assert len(_SESSIONS) > 0


def test_oversized_code_is_rejected():
    result = execute_code("big-code", "x = 1\n" * 5000)
    assert result["error"] is not None
    assert "largo" in result["error"]
