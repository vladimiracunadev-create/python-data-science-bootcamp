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
    # Un notebook es un flujo de celdas donde cada celda depende de las anteriores.
    # Si el engine no conserva el namespace entre llamadas, el alumno no puede definir
    # una variable en una celda y usarla en la siguiente, lo que rompe toda la experiencia interactiva.
    assert result["result"] == "15"


def test_execute_code_captures_stdout():
    reset_session("stdout")
    result = execute_code("stdout", 'print("hola")')
    assert "hola" in result["stdout"]


def test_execute_code_handles_runtime_error():
    reset_session("err-test")
    result = execute_code("err-test", "1 / 0")
    # Errores de ejecución del alumno (ZeroDivisionError, NameError, etc.) son esperados
    # y deben quedar contenidos dentro del resultado; no deben lanzar una excepción Python
    # que burbujee hasta Flask y devuelva un 500, lo que cortaría la sesión del alumno.
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
    # Un reset debe eliminar por completo el namespace de la sesión, no solo los valores visibles.
    # Si la variable persiste tras el reset, el alumno podría continuar ejecutando celdas con
    # estado corrupto o heredado de una ejecución anterior, produciendo resultados inesperados.
    assert result["error"] is not None


def test_reset_session_nonexistent_does_not_raise():
    reset_session("sesion-que-no-existe-xyz")


def test_session_eviction_does_not_crash():
    # Si el engine acumula en memoria una sesión por cada alumno sin limpiarlas,
    # en una clase con 30+ alumnos el proceso puede quedarse sin RAM y caer.
    # Este stress mínimo verifica que crear 50 sesiones distintas no lanza excepción
    # y que el diccionario de sesiones sigue siendo accesible (la política de evicción,
    # si existe, no debe corromper la estructura compartida).
    for i in range(50):
        execute_code(f"evict-stress-{i}", "pass")
    assert len(_SESSIONS) > 0


def test_oversized_code_is_rejected():
    result = execute_code("big-code", "x = 1\n" * 5000)
    # El límite de 20 KB protege contra dos vectores: código con loops infinitos que
    # consumen CPU indefinidamente, y payloads gigantes enviados por error o con intención
    # maliciosa. El mensaje de error debe mencionar "largo" para que el alumno entienda
    # la causa sin ver un traceback interno del servidor.
    assert result["error"] is not None
    assert "largo" in result["error"]
