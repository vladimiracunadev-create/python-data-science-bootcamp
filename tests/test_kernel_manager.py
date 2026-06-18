"""Pruebas del gestor de kernels IPython del laboratorio.

Validan el ciclo de vida (start/shutdown/restart), captura de outputs ricos
(stream, execute_result, display_data, errores), aislamiento entre kernels,
y los mecanismos de seguridad (timeout, interrupt, límite de tamaño).

Cada test es auto-limpiable: invoca `shutdown(kernel_id)` en un finally para
no dejar procesos kernel huérfanos si una aserción falla.
"""

from __future__ import annotations

import sys
import threading
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.kernel_manager import (
    MAX_CODE_LENGTH,
    execute,
    interrupt,
    list_kernels,
    restart,
    shutdown,
    shutdown_all,
    start_kernel,
)


def test_start_and_shutdown_kernel():
    # start debe devolver un id manejable como string y registrar el kernel;
    # shutdown debe removerlo del listado para evitar fugas de procesos.
    kid = start_kernel()
    try:
        assert isinstance(kid, str) and len(kid) > 0
        ids = [k["kernel_id"] for k in list_kernels()]
        assert kid in ids
    finally:
        shutdown(kid)
    assert kid not in [k["kernel_id"] for k in list_kernels()]


def test_execute_simple_arithmetic():
    # La semántica Out[n] de Jupyter requiere que una expresión suelta produzca
    # un execute_result, no un stream. Si lo perdemos, el alumno no ve el valor
    # de retorno de su última línea como en un notebook real.
    kid = start_kernel()
    try:
        result = execute(kid, "2 + 3")
        assert result["status"] == "ok"
        assert result["execution_count"] == 1
        execute_results = [o for o in result["outputs"] if o["type"] == "execute_result"]
        assert len(execute_results) == 1
        assert execute_results[0]["data"]["text/plain"] == "5"
    finally:
        shutdown(kid)


def test_execute_captures_print():
    # print() va a stdout vía el canal iopub como `stream`; si no lo mapeamos
    # correctamente, el alumno verá outputs vacíos cuando usa el patrón más básico.
    kid = start_kernel()
    try:
        result = execute(kid, "print('hola mundo')")
        assert result["status"] == "ok"
        streams = [o for o in result["outputs"] if o["type"] == "stream" and o["name"] == "stdout"]
        assert any("hola mundo" in s["text"] for s in streams)
    finally:
        shutdown(kid)


def test_execute_persists_state_between_calls():
    # Un kernel real persiste namespace entre celdas. Esta es la ventaja sobre
    # subprocess.run y la razón por la que existe la abstracción de kernel.
    kid = start_kernel()
    try:
        execute(kid, "x = 10")
        result = execute(kid, "x + 5")
        assert result["status"] == "ok"
        execute_results = [o for o in result["outputs"] if o["type"] == "execute_result"]
        assert execute_results[0]["data"]["text/plain"] == "15"
    finally:
        shutdown(kid)


def test_execute_handles_runtime_error():
    # Errores del alumno (ZeroDivisionError, NameError) son esperados y deben
    # quedar contenidos en outputs, nunca burbujear como excepción Python que
    # corte la sesión del lab.
    kid = start_kernel()
    try:
        result = execute(kid, "1/0")
        assert result["status"] == "error"
        errors = [o for o in result["outputs"] if o["type"] == "error"]
        assert len(errors) >= 1
        assert errors[0]["ename"] == "ZeroDivisionError"
    finally:
        shutdown(kid)


def test_execute_handles_syntax_error():
    # SyntaxError ocurre antes de ejecutar; el kernel debe reportarlo igualmente
    # como output de tipo error, no como excepción del transporte.
    kid = start_kernel()
    try:
        result = execute(kid, "def broken(:")
        assert result["status"] == "error"
        errors = [o for o in result["outputs"] if o["type"] == "error"]
        assert len(errors) >= 1
    finally:
        shutdown(kid)


def test_execute_captures_matplotlib_png():
    # matplotlib inline emite display_data con image/png base64. Sin esto, el
    # lab no muestra los gráficos que son el corazón de las clases de DS.
    pytest.importorskip("matplotlib")
    kid = start_kernel()
    try:
        # `%matplotlib inline` es lo que activa la captura de figuras al iopub
        # como `display_data` con clave image/png — sin esa magic, `plt.show()`
        # en backend Agg no emite nada y el lab no mostraría gráficos al alumno.
        code = (
            "%matplotlib inline\n"
            "import matplotlib.pyplot as plt\n"
            "plt.plot([1,2,3])\n"
            "plt.show()\n"
        )
        result = execute(kid, code, timeout=30.0)
        assert result["status"] == "ok"
        with_png = [
            o for o in result["outputs"]
            if o.get("type") in ("display_data", "execute_result") and "image/png" in o.get("data", {})
        ]
        assert len(with_png) >= 1
    finally:
        shutdown(kid)


def test_execute_oversized_code_rejected():
    # El límite de 200 KB defiende contra payloads anómalos y protege el canal
    # ZMQ de mensajes desproporcionados; debe rechazarse antes de tocar el kernel.
    kid = start_kernel()
    try:
        big = "x = 1\n" * (MAX_CODE_LENGTH // 4)
        with pytest.raises(ValueError):
            execute(kid, big)
    finally:
        shutdown(kid)


def test_restart_clears_state():
    # restart debe matar y rearmar el proceso kernel; si el namespace persistiera
    # el alumno no tendría forma de recuperarse de un namespace corrupto sin
    # negociar un kernel_id nuevo con la UI.
    kid = start_kernel()
    try:
        execute(kid, "x = 42")
        restart(kid)
        result = execute(kid, "x")
        assert result["status"] == "error"
        errors = [o for o in result["outputs"] if o["type"] == "error"]
        assert any(e["ename"] == "NameError" for e in errors)
    finally:
        shutdown(kid)


def test_interrupt_during_long_execution():
    # interrupt() debe abortar un loop largo en segundos. Usamos un loop CPU-bound
    # en vez de time.sleep porque en Windows SIGINT no interrumpe time.sleep
    # de forma confiable (es un quirk del runtime CPython sobre Win32), pero sí
    # interrumpe ejecución Python pura — que es el caso real del alumno (loop
    # infinito mientras prueba código), no un sleep accidental.
    kid = start_kernel()
    container: dict = {}

    def run():
        container["result"] = execute(kid, "i = 0\nwhile True:\n    i += 1\n", timeout=20.0)

    try:
        t = threading.Thread(target=run, daemon=True)
        t.start()
        time.sleep(1.5)
        interrupt(kid)
        t.join(timeout=10)
        assert not t.is_alive(), "ejecución no terminó tras interrupt"
        result = container["result"]
        assert result["status"] in ("interrupted", "error", "ok")
    finally:
        shutdown(kid)


def test_execution_timeout():
    # timeout debe cortar a ~deadline + gracia (~2s), no esperar a que termine
    # el sleep. Sin esto, una celda colgada bloquea el endpoint Flask del lab.
    kid = start_kernel()
    try:
        start = time.time()
        result = execute(kid, "import time; time.sleep(10)", timeout=2.0)
        elapsed = time.time() - start
        assert result["status"] in ("timeout", "interrupted")
        assert elapsed < 6.0, f"timeout tardó demasiado: {elapsed:.1f}s"
    finally:
        shutdown(kid)


def test_multiple_kernels_isolated():
    # Cada kernel es un proceso aislado; mezclar namespaces sería un bug grave
    # que rompería la experiencia multi-alumno o multi-pestaña del lab.
    kid_a = start_kernel()
    kid_b = start_kernel()
    try:
        execute(kid_a, "x = 1")
        execute(kid_b, "x = 2")
        ra = execute(kid_a, "x")
        rb = execute(kid_b, "x")
        a_val = next(o for o in ra["outputs"] if o["type"] == "execute_result")["data"]["text/plain"]
        b_val = next(o for o in rb["outputs"] if o["type"] == "execute_result")["data"]["text/plain"]
        assert a_val == "1"
        assert b_val == "2"
    finally:
        shutdown(kid_a)
        shutdown(kid_b)


def test_shutdown_all_clears_everything():
    # atexit usa shutdown_all; debe dejar el registro vacío para que el proceso
    # Flask muera limpio sin dejar zombis de ipykernel.
    kids = [start_kernel() for _ in range(3)]
    try:
        assert len([k for k in list_kernels() if k["kernel_id"] in kids]) == 3
        shutdown_all()
        remaining = [k["kernel_id"] for k in list_kernels()]
        for kid in kids:
            assert kid not in remaining
    finally:
        # Doblemente seguro por si shutdown_all falló parcialmente.
        for kid in kids:
            try:
                shutdown(kid)
            except Exception:
                pass
