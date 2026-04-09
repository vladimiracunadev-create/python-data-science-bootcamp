"""Punto de entrada para ejecutar el bootcamp en modo desarrollo (localhost).

Uso:
    python run_bootcamp.py

Esto levanta Flask en http://127.0.0.1:8000 y abre el navegador
automáticamente cuando el servidor esté listo.
Para la app de escritorio (sin navegador), ejecuta BootcampPythonDS.exe.
"""

from __future__ import annotations

import os
import socket
import sys
import threading
import time
import urllib.request
import webbrowser

HOST = os.getenv("BOOTCAMP_HOST", "127.0.0.1")
PORT = int(os.getenv("BOOTCAMP_PORT", "8000"))
STARTUP_TIMEOUT = 30


def _port_in_use(host: str, port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        try:
            s.connect((host, port))
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False


def _wait_for_server(url: str, timeout: int) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as r:  # nosec B310 — URL is always http://127.0.0.1
                if r.status == 200:
                    return True
        except Exception:  # nosec B110 — intentional: server not ready yet, keep polling
            pass
        time.sleep(0.4)
    return False


def main() -> None:
    url = f"http://{HOST}:{PORT}"

    print()
    print("=" * 58)
    print("  BOOTCAMP PYTHON DS — Modo desarrollo (localhost)")
    print("=" * 58)
    print(f"  URL: {url}")
    print()

    if _port_in_use(HOST, PORT):
        print(f"  Ya hay un servidor en {url}. Abriendo navegador...")
        webbrowser.open(url)
        return

    # Importar la app aquí para detectar errores antes de iniciar el hilo
    try:
        from app.app import app
    except ImportError as exc:
        print(f"  ERROR: No se pudo importar la app Flask: {exc}")
        print("  Asegúrate de tener instaladas las dependencias:")
        print("    pip install -r requirements.txt")
        sys.exit(1)

    print("  Iniciando Flask en segundo plano...")

    flask_thread = threading.Thread(
        target=lambda: app.run(host=HOST, port=PORT, debug=False, use_reloader=False),
        daemon=True,
        name="flask-dev",
    )
    flask_thread.start()

    print(f"  Esperando que el servidor responda en {url}/health ...")
    ready = _wait_for_server(f"{url}/health", STARTUP_TIMEOUT)

    if not ready:
        print()
        print("  ERROR: El servidor no respondió en el tiempo esperado.")
        print("  Posibles causas:")
        print(f"    - Puerto {PORT} bloqueado por firewall")
        print("    - Error en la importación de dependencias (revisa arriba)")
        print(f"  Intenta abrir manualmente: {url}")
        sys.exit(1)

    print("  Servidor listo. Abriendo navegador...")
    webbrowser.open(url)

    print()
    print("  Presiona Ctrl+C para detener el servidor.")
    print()

    try:
        flask_thread.join()
    except KeyboardInterrupt:
        print("\n  Servidor detenido.")


if __name__ == "__main__":
    main()
