"""Launcher local para la app del bootcamp en Windows.

Responsabilidades:
    1. Detectar si ya existe una instancia corriendo en el puerto configurado.
    2. Arrancar el servidor Flask en un hilo separado.
    3. Esperar el endpoint `/health` antes de abrir el navegador.
    4. Mantener el proceso vivo con un menú mínimo de consola.
    5. Cerrar la aplicación de forma limpia al salir.

Este archivo resuelve la experiencia de uso más amigable para docentes o
estudiantes que quieren abrir el sistema local sin pelear con comandos largos.
"""

from __future__ import annotations

import os
import signal
import socket
import sys
import threading
import time
import urllib.request
import webbrowser

# Dirección de escucha: siempre local para que la app no quede expuesta en red.
HOST = os.environ.get("BOOTCAMP_HOST", "127.0.0.1")
# Puerto configurable para evitar conflictos con otros servicios locales.
PORT = int(os.environ.get("BOOTCAMP_PORT", "8000"))
STARTUP_TIMEOUT = 30
POLL_INTERVAL = 0.5
BASE_URL = f"http://{HOST}:{PORT}"


def puerto_en_uso(host: str, port: int) -> bool:
    """Comprueba si ya existe un proceso escuchando en `host:port`.

    Qué resuelve:
        Evita abrir una segunda instancia de la app y permite reutilizar la ya
        existente en lugar de fallar con un error de puerto ocupado.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1)
        try:
            sock.connect((host, port))
            return True
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False


def esperar_servidor(url: str, timeout: int) -> bool:
    """Hace polling a `/health` hasta que el servidor responde correctamente.

    Qué resuelve:
        Sin esta espera, el navegador podría abrirse antes de que Flask esté
        listo y el usuario vería una página caída al iniciar el sistema.
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                if response.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(POLL_INTERVAL)
    return False


def imprimir_banner() -> None:
    """Muestra en consola el contexto básico de la sesión actual."""
    print()
    print("=" * 60)
    print("  BOOTCAMP PYTHON PARA DATA SCIENCE")
    print("  Entorno local de aprendizaje interactivo")
    print("=" * 60)
    print(f"  URL: {BASE_URL}")
    print("=" * 60)
    print()


def imprimir_menu() -> None:
    """Presenta los comandos mínimos disponibles para el usuario."""
    print()
    print("  Opciones:")
    print("  [Enter]  Reabrir el navegador")
    print("  [q]      Apagar el servidor y salir")
    print()


def arrancar_flask() -> None:
    """Importa y levanta la app Flask dentro de un hilo daemon.

    Qué resuelve:
        Mantiene libre el hilo principal para mostrar estado, esperar `/health`
        y responder a comandos del usuario mientras el servidor sigue vivo.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    os.environ.setdefault("BOOTCAMP_HOST", HOST)
    os.environ.setdefault("BOOTCAMP_PORT", str(PORT))

    # El import ocurre aquí para que PyInstaller detecte dependencias y para no
    # cargar Flask si el launcher descubre una instancia ya corriendo.
    from app.app import app

    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)


def main() -> None:
    """Coordina arranque, apertura de navegador y cierre limpio del sistema."""
    imprimir_banner()

    if puerto_en_uso(HOST, PORT):
        print(f"  Ya hay una instancia corriendo en {BASE_URL}")
        print("  Abriendo el navegador...")
        webbrowser.open(BASE_URL)
        return

    print("  Iniciando el servidor Flask...")
    hilo_flask = threading.Thread(target=arrancar_flask, daemon=True, name="flask-server")
    hilo_flask.start()

    health_url = f"{BASE_URL}/health"
    print(f"  Esperando que el servidor responda en {health_url} ...")
    listo = esperar_servidor(health_url, STARTUP_TIMEOUT)
    if not listo:
        print()
        print("  ERROR: El servidor no respondió en el tiempo esperado.")
        print("  Revisa que el puerto no esté bloqueado por el firewall.")
        print(f"  Intenta abrir manualmente: {BASE_URL}")
        sys.exit(1)

    print("  Servidor listo.")
    print(f"  Abriendo {BASE_URL} en el navegador...")
    webbrowser.open(BASE_URL)
    imprimir_menu()

    def manejador_sigint(sig: int, frame: object) -> None:
        """Cierra el proceso cuando el usuario presiona Ctrl+C."""
        del sig, frame
        print("\n\n  Apagando el servidor...")
        sys.exit(0)

    signal.signal(signal.SIGINT, manejador_sigint)

    while True:
        try:
            entrada = input("  > ").strip().lower()
        except EOFError:
            # Si la consola se cierra pero el proceso sigue vivo, esperamos al
            # hilo para no matar abruptamente el servidor.
            hilo_flask.join()
            break

        if entrada in ("q", "quit", "exit", "salir"):
            print("  Apagando el servidor...")
            break
        if entrada == "":
            print(f"  Reabriendo {BASE_URL}...")
            webbrowser.open(BASE_URL)
            continue

        print("  Comando no reconocido. Usa [Enter] o [q].")

    sys.exit(0)


if __name__ == "__main__":
    main()
