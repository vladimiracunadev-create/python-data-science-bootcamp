"""
launcher.py — Punto de entrada del instalador Windows del Bootcamp Python DS.

Responsabilidades:
  1. Detectar si ya hay una instancia corriendo en el puerto configurado.
  2. Arrancar el servidor Flask en un hilo separado.
  3. Esperar que el servidor responda /health antes de abrir el navegador.
  4. Mantener el proceso vivo mostrando un menu de consola minimo.
  5. Apagar correctamente el servidor al salir.

Uso:
  python launcher.py               # Arranca en 127.0.0.1:8000
  BOOTCAMP_PORT=9000 python launcher.py
"""

import os
import sys
import time
import signal
import socket
import webbrowser
import threading
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# CONFIGURACION
# ---------------------------------------------------------------------------

# Direccion de escucha — siempre 127.0.0.1 para uso local
HOST = os.environ.get("BOOTCAMP_HOST", "127.0.0.1")

# Puerto — configurable por variable de entorno
PORT = int(os.environ.get("BOOTCAMP_PORT", "8000"))

# Tiempo maximo de espera para que Flask arranque (segundos)
STARTUP_TIMEOUT = 30

# Intervalo de polling mientras espera que el servidor responda
POLL_INTERVAL = 0.5

# URL base de la aplicacion
BASE_URL = f"http://{HOST}:{PORT}"

# ---------------------------------------------------------------------------
# UTILIDADES
# ---------------------------------------------------------------------------

def puerto_en_uso(host: str, port: int) -> bool:
    """
    Verifica si ya hay algo escuchando en host:port.

    Usa un socket TCP de prueba con timeout corto.
    Si la conexion es exitosa, el puerto esta ocupado.

    Returns:
        True  si el puerto ya esta en uso.
        False si el puerto esta libre.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # SO_REUSEADDR evita falsos positivos en TIME_WAIT
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(1)
        try:
            sock.connect((host, port))
            return True          # Conexion exitosa → puerto ocupado
        except (ConnectionRefusedError, socket.timeout, OSError):
            return False         # No hay nadie escuchando → puerto libre


def esperar_servidor(url: str, timeout: int) -> bool:
    """
    Hace polling al endpoint /health hasta que el servidor responde 200.

    Parametros:
        url     URL completa del endpoint health.
        timeout Tiempo maximo de espera en segundos.

    Returns:
        True  si el servidor respondio antes del timeout.
        False si se agoto el tiempo.
    """
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as resp:
                if resp.status == 200:
                    return True     # Servidor listo
        except Exception:
            pass                    # Todavia no responde, seguir esperando
        time.sleep(POLL_INTERVAL)
    return False                    # Timeout agotado


def imprimir_banner():
    """
    Muestra el banner inicial del bootcamp en consola.
    """
    print()
    print("=" * 60)
    print("  BOOTCAMP PYTHON PARA DATA SCIENCE")
    print("  Entorno local de aprendizaje interactivo")
    print("=" * 60)
    print(f"  URL: {BASE_URL}")
    print("=" * 60)
    print()


def imprimir_menu():
    """
    Muestra las opciones disponibles en consola.
    """
    print()
    print("  Opciones:")
    print("  [Enter]  Reabrir el navegador")
    print("  [q]      Apagar el servidor y salir")
    print()


# ---------------------------------------------------------------------------
# ARRANQUE DEL SERVIDOR
# ---------------------------------------------------------------------------

def arrancar_flask():
    """
    Importa y arranca la aplicacion Flask.

    Se ejecuta en un hilo daemon para que muera junto con el proceso principal.
    El import se hace aqui (no al nivel del modulo) para que PyInstaller pueda
    detectar las dependencias correctamente.
    """
    # Ajustar el path para que el import funcione tanto desde el repo
    # como desde el directorio de instalacion de PyInstaller.
    base_dir = os.path.dirname(os.path.abspath(__file__))
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    # Configurar variables de entorno antes de importar Flask
    os.environ.setdefault("BOOTCAMP_HOST", HOST)
    os.environ.setdefault("BOOTCAMP_PORT", str(PORT))

    # Importar y ejecutar la app
    # El import de app.app carga Flask, configura rutas y seguridad.
    from app.app import app  # noqa: F401 — importacion necesaria para PyInstaller
    app.run(host=HOST, port=PORT, debug=False, use_reloader=False)


# ---------------------------------------------------------------------------
# PUNTO DE ENTRADA PRINCIPAL
# ---------------------------------------------------------------------------

def main():
    """
    Flujo principal del launcher:

    1. Mostrar banner
    2. Verificar si el puerto ya esta en uso (instancia duplicada)
    3. Arrancar Flask en hilo daemon
    4. Esperar que /health responda
    5. Abrir el navegador
    6. Mantener el proceso vivo con menu de consola
    7. Apagar limpiamente al recibir Ctrl+C o comando 'q'
    """
    imprimir_banner()

    # ---- Paso 1: Verificar instancia duplicada ----
    if puerto_en_uso(HOST, PORT):
        print(f"  Ya hay una instancia corriendo en {BASE_URL}")
        print("  Abriendo el navegador...")
        webbrowser.open(BASE_URL)
        return

    # ---- Paso 2: Arrancar Flask en hilo daemon ----
    print("  Iniciando el servidor Flask...")
    hilo_flask = threading.Thread(target=arrancar_flask, daemon=True, name="flask-server")
    hilo_flask.start()

    # ---- Paso 3: Esperar que el servidor este listo ----
    health_url = f"{BASE_URL}/health"
    print(f"  Esperando que el servidor responda en {health_url} ...")
    listo = esperar_servidor(health_url, STARTUP_TIMEOUT)

    if not listo:
        print()
        print("  ERROR: El servidor no respondio en el tiempo esperado.")
        print("  Revisa que el puerto no este bloqueado por el firewall.")
        print(f"  Intenta abrir manualmente: {BASE_URL}")
        sys.exit(1)

    print("  Servidor listo.")

    # ---- Paso 4: Abrir el navegador ----
    print(f"  Abriendo {BASE_URL} en el navegador...")
    webbrowser.open(BASE_URL)

    # ---- Paso 5: Menu de consola ----
    imprimir_menu()

    # Capturar Ctrl+C para apagar limpiamente
    def manejador_sigint(sig, frame):
        print("\n\n  Apagando el servidor...")
        sys.exit(0)

    signal.signal(signal.SIGINT, manejador_sigint)

    # Bucle principal: espera comandos del usuario
    while True:
        try:
            entrada = input("  > ").strip().lower()
        except EOFError:
            # stdin cerrado (por ejemplo, lanzado sin consola)
            # Mantener el servidor vivo esperando en el hilo
            hilo_flask.join()
            break

        if entrada in ("q", "quit", "exit", "salir"):
            print("  Apagando el servidor...")
            break
        elif entrada == "":
            # Enter → reabrir el navegador
            print(f"  Reabriendo {BASE_URL}...")
            webbrowser.open(BASE_URL)
        else:
            print("  Comando no reconocido. Usa [Enter] o [q].")

    sys.exit(0)


if __name__ == "__main__":
    main()
