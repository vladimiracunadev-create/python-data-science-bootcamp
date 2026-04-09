"""Launcher de escritorio para el Bootcamp Python DS — Windows.

Abre una ventana nativa de Windows usando pywebview + Edge WebView2.
Flask corre internamente en un puerto libre elegido automáticamente.
El usuario nunca ve localhost, no se abre ningún navegador externo.

Requisitos:
    pip install pywebview
    Windows 10 (1803+) o Windows 11 con Edge WebView2 Runtime instalado.
    (Edge WebView2 viene preinstalado en Windows 10 20H2+ y en todo Windows 11.)
"""

from __future__ import annotations

import os
import socket
import sys
import threading
import time
import urllib.request
from pathlib import Path

APP_TITLE = "Bootcamp Python — Data Science"
WIN_W, WIN_H = 1280, 800
MIN_W, MIN_H = 960, 620
STARTUP_TIMEOUT = 45  # segundos esperando que Flask responda


# ---------------------------------------------------------------------------
# Utilidades de red
# ---------------------------------------------------------------------------

def _find_free_port() -> int:
    """Pide al sistema operativo un puerto libre en loopback."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _wait_for_server(url: str, timeout: int) -> bool:
    """Hace polling en /health hasta que Flask responde 200 o se acaba el tiempo."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as r:
                if r.status == 200:
                    return True
        except Exception:
            pass
        time.sleep(0.3)
    return False


# ---------------------------------------------------------------------------
# Inicio de Flask
# ---------------------------------------------------------------------------

def _start_flask(host: str, port: int) -> None:
    """Arranca la app Flask en un hilo daemon.

    Qué resuelve:
        El servidor corre en segundo plano. La ventana de pywebview se crea
        en el hilo principal, que es el requisito de la mayoría de los
        toolkits gráficos de Windows.
    """
    base_dir = str(Path(__file__).resolve().parent)
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    # Inyectamos las variables de entorno antes del import de Flask para que
    # app.py las lea correctamente al construir la instancia.
    os.environ["BOOTCAMP_HOST"] = host
    os.environ["BOOTCAMP_PORT"] = str(port)

    from app.app import app as flask_app  # noqa: PLC0415
    flask_app.run(
        host=host,
        port=port,
        debug=False,
        use_reloader=False,
        threaded=True,
    )


# ---------------------------------------------------------------------------
# HTML de estados internos (carga y error)
# ---------------------------------------------------------------------------

_LOADING_HTML = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Iniciando…</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #0f172a; color: #94a3b8;
      font-family: 'Segoe UI', system-ui, Arial, sans-serif;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      height: 100vh; text-align: center; padding: 32px;
    }
    .spinner {
      width: 52px; height: 52px;
      border: 3px solid #1e293b;
      border-top-color: #22c55e;
      border-radius: 50%;
      animation: spin 0.9s linear infinite;
      margin-bottom: 28px;
    }
    @keyframes spin { to { transform: rotate(360deg); } }
    h2 { color: #f1f5f9; font-size: 1.35rem; margin-bottom: 10px; font-weight: 600; }
    p  { font-size: 0.9rem; line-height: 1.6; }
  </style>
</head>
<body>
  <div class="spinner"></div>
  <h2>Iniciando Bootcamp Python DS</h2>
  <p>Preparando el entorno de aprendizaje…</p>
</body>
</html>"""


def _error_html(detail: str) -> str:
    return f"""<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <title>Error — Bootcamp Python DS</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #0f172a; color: #f1f5f9;
      font-family: 'Segoe UI', system-ui, Arial, sans-serif;
      display: flex; flex-direction: column;
      align-items: center; justify-content: center;
      height: 100vh; text-align: center; padding: 40px;
    }}
    .icon {{ font-size: 3rem; margin-bottom: 20px; }}
    h2 {{ color: #ef4444; font-size: 1.4rem; margin-bottom: 12px; font-weight: 600; }}
    p  {{ color: #94a3b8; max-width: 500px; line-height: 1.7; font-size: 0.95rem; }}
    .detail {{
      margin-top: 20px; background: #1e293b;
      border: 1px solid #334155; border-radius: 10px;
      padding: 14px 18px; color: #fca5a5;
      font-size: 0.85rem; max-width: 540px; text-align: left;
    }}
  </style>
</head>
<body>
  <div class="icon">⚠️</div>
  <h2>No se pudo iniciar el Bootcamp</h2>
  <p>El servidor interno no respondió a tiempo. Cierra esta ventana y vuelve a abrir la aplicación.</p>
  <div class="detail">{detail}</div>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Punto de entrada principal
# ---------------------------------------------------------------------------

def main() -> None:
    host = "127.0.0.1"
    port = _find_free_port()
    url = f"http://{host}:{port}"

    # Inicia Flask antes de crear la ventana para aprovechar el tiempo de
    # inicialización del runtime de WebView2.
    flask_thread = threading.Thread(
        target=_start_flask,
        args=(host, port),
        daemon=True,
        name="flask-server",
    )
    flask_thread.start()

    import webview  # noqa: PLC0415  — import tardío para que PyInstaller lo detecte

    window = webview.create_window(
        title=APP_TITLE,
        html=_LOADING_HTML,
        width=WIN_W,
        height=WIN_H,
        min_size=(MIN_W, MIN_H),
        resizable=True,
        text_select=True,
        zoomable=True,
    )

    def _load_when_ready() -> None:
        """Callback que corre en hilo separado mientras webview.start() espera."""
        ok = _wait_for_server(f"{url}/health", STARTUP_TIMEOUT)
        if ok:
            window.load_url(url)
        else:
            window.load_html(
                _error_html(
                    f"Timeout: el servidor en {url} no respondió en "
                    f"{STARTUP_TIMEOUT} segundos."
                )
            )

    # debug=False oculta DevTools en producción.
    # El callback se ejecuta en un hilo de pywebview, no en el principal.
    webview.start(_load_when_ready, debug=False)


if __name__ == "__main__":
    main()
