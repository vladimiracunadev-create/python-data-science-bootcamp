"""Aplicación Flask del Python Data Science Program — capa HTTP del laboratorio.

Qué resuelve:
    Publica la interfaz web del laboratorio local: navegación del currículo,
    lectura de notebooks ``.ipynb`` reales y ejecución de código sobre kernels
    IPython gestionados en proceso. Conserva las rutas históricas para clases
    y descargas de assets (PDF/PPTX) para no romper otros consumidores.
"""

# Arquitectura: app Flask local-first. No expone internet.
# El laboratorio de ejecución (Jupyter kernel real vía jupyter_client),
# el portal del alumno y la presentación institucional conviven en el mismo
# proceso para simplificar el instalador Windows (launcher.py + Edge WebView2).

from __future__ import annotations

import logging
import os
import re
import sys
from pathlib import Path

import markdown
from flask import Flask, jsonify, render_template, request, send_file, url_for

from .content_loader import (
    get_class_assets,
    list_classes,
    load_class_quiz,
    read_class_markdown,
    resolve_class_asset_path,
)
from .kernel_manager import (
    MAX_CODE_LENGTH,
    execute as kernel_execute,
    interrupt as kernel_interrupt,
    list_kernels as kernel_list,
    restart as kernel_restart,
    shutdown as kernel_shutdown,
    start_kernel,
)
from .notebook_loader import list_curriculum, load_notebook

logger = logging.getLogger(__name__)


def _get_base_dir() -> Path:
    """Devuelve la raíz del proyecto tanto en desarrollo como en bundle PyInstaller."""
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parents[1]


BASE_DIR = _get_base_dir()
app = Flask(
    __name__,
    template_folder=str(BASE_DIR / "app" / "templates"),
    static_folder=str(BASE_DIR / "app" / "static"),
)

MAX_PAYLOAD_BYTES = 2_000_000  # 2 MB — notebooks reales con código generado pueden ser grandes.
SLUG_RE = re.compile(r"^[\w\-]{1,80}$")
CLASS_SLUG_RE = re.compile(r"^[\w\-/]{1,160}$")
KERNEL_ID_RE = re.compile(r"^[a-f0-9]{32}$")  # uuid4().hex
DEFAULT_HOST = os.getenv("PROGRAM_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.getenv("PROGRAM_PORT", "8000"))


def _valid_class_slug(slug: str) -> bool:
    return bool(CLASS_SLUG_RE.match(slug))


def _valid_kernel_id(kid: str) -> bool:
    return bool(KERNEL_ID_RE.match(kid))


@app.after_request
def add_security_headers(response):
    """Endurecimiento básico para la app local en navegador / WebView2.

    Qué resuelve:
        Reduce riesgos de contenido embebido, sniffing y políticas de origen
        al servir una app que ejecuta código local del alumno.
    """
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    response.headers.setdefault("Referrer-Policy", "no-referrer")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
    # CSP sin fuentes externas: la app funciona offline, todo asset debe servirse local.
    # Ampliarlo a CDNs rompería el modo sin red del instalador Windows.
    response.headers.setdefault(
        "Content-Security-Policy",
        (
            "default-src 'self'; "
            "style-src 'self' 'unsafe-inline'; "
            "font-src 'self' data:; "
            "img-src 'self' data:; "
            "script-src 'self'; "
            "connect-src 'self'; "
            "frame-ancestors 'self'; "
            "base-uri 'self'; "
            "form-action 'self'"
        ),
    )
    return response


# ---------------------------------------------------------------------------
# Vistas y health
# ---------------------------------------------------------------------------

@app.get("/")
def index():
    """Renderiza la SPA del laboratorio (el currículo y los kernels se cargan vía API)."""
    return render_template("index.html")


@app.get("/health")
def health():
    """Healthcheck liviano para launcher.py, tests y Docker HEALTHCHECK."""
    return jsonify({"status": "ok", "service": "python-data-science-program"})


@app.get("/ready")
def ready():
    """Confirma que el currículo se puede listar antes de servir tráfico."""
    curriculum = list_curriculum()
    n_classes = sum(len(part["classes"]) for part in curriculum)
    return jsonify(
        {
            "status": "ready",
            "service": "python-data-science-program",
            "parts": len(curriculum),
            "classes": n_classes,
        }
    )


# ---------------------------------------------------------------------------
# Currículo: listado y detalle (clases + notebook)
# ---------------------------------------------------------------------------

@app.get("/api/curriculum")
def api_curriculum():
    """Árbol completo del currículo agrupado por parte (9 partes · 232 clases).

    Qué resuelve:
        El frontend necesita una sola llamada al cargar la app para poblar el
        sidebar navegable; evitamos N+1 requests.
    """
    return jsonify(list_curriculum())


@app.get("/api/notebook/<path:class_slug>")
def api_notebook(class_slug: str):
    """Devuelve las celdas del ``notebook.ipynb`` real de una clase.

    Qué resuelve:
        Permite que el lab cargue el contenido ejecutable de cualquier clase del
        currículo sin convertirlo manualmente — el .ipynb es la fuente de verdad.
    """
    if not _valid_class_slug(class_slug):
        return jsonify({"error": "slug inválido"}), 400
    try:
        return jsonify(load_notebook(class_slug))
    except FileNotFoundError:
        return jsonify({"error": "notebook no encontrado"}), 404
    except (ValueError, PermissionError) as exc:
        return jsonify({"error": str(exc)}), 400


@app.get("/api/classes")
def api_classes():
    """Listado plano de clases (compat con consumidores históricos)."""
    return jsonify(list_classes())


@app.get("/api/class/<path:slug>")
def api_class_detail(slug: str):
    """Markdown renderizado + quiz + assets de una clase.

    Qué resuelve:
        El panel "Ver README completo" del lab y consumidores externos (mobile,
        portal del alumno) consumen este endpoint para presentar la ficha de clase.
    """
    if not _valid_class_slug(slug):
        return jsonify({"error": "slug inválido"}), 400
    try:
        data = read_class_markdown(slug)
        quiz = load_class_quiz(slug)
        assets = get_class_assets(slug)
    except FileNotFoundError:
        return jsonify({"error": "clase no encontrada"}), 404

    html = {
        name: markdown.markdown(text, extensions=["fenced_code", "tables"])
        for name, text in data.items()
    }
    asset_payload = {
        kind: {**meta, "url": url_for("download_class_asset", slug=slug, asset_kind=kind)}
        for kind, meta in assets.items()
    }
    return jsonify({"slug": slug, "html": html, "raw": data, "quiz": quiz, "assets": asset_payload})


@app.get("/downloads/class/<path:slug>/<asset_kind>")
def download_class_asset(slug: str, asset_kind: str):
    """Sirve PDFs y PPTX derivados por clase (mantenido por compatibilidad)."""
    if not _valid_class_slug(slug):
        return jsonify({"error": "slug inválido"}), 400
    if asset_kind not in {"pdf", "pptx"}:
        return jsonify({"error": "tipo de archivo inválido"}), 400

    try:
        path = resolve_class_asset_path(slug, asset_kind)
    except FileNotFoundError:
        return jsonify({"error": "archivo no encontrado"}), 404

    mimetype = {
        "pdf": "application/pdf",
        "pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    }[asset_kind]
    return send_file(path, mimetype=mimetype, as_attachment=False, download_name=path.name)


# ---------------------------------------------------------------------------
# Kernels: lifecycle + ejecución de celdas
# ---------------------------------------------------------------------------

@app.post("/api/kernel/start")
def api_kernel_start():
    """Inicia un kernel IPython fresco y devuelve su identificador."""
    try:
        kid = start_kernel()
    except Exception:  # pragma: no cover - falla rara al lanzar el subproceso
        logger.exception("No se pudo iniciar el kernel")
        return jsonify({"error": "no se pudo iniciar el kernel"}), 500
    return jsonify({"kernel_id": kid})


@app.get("/api/kernels")
def api_kernel_list():
    """Lista de kernels activos (debugging / panel admin)."""
    return jsonify(kernel_list())


@app.post("/api/kernel/<kid>/execute")
def api_kernel_execute(kid: str):
    """Ejecuta una celda en el kernel ``kid`` y devuelve los outputs del iopub.

    Qué resuelve:
        Es el endpoint caliente del lab. Bloquea hasta idle (o timeout); el
        frontend muestra el estado "busy" mientras tanto.
    """
    if not _valid_kernel_id(kid):
        return jsonify({"error": "kernel_id inválido"}), 400
    if request.content_length and request.content_length > MAX_PAYLOAD_BYTES:
        return jsonify({"error": "payload demasiado grande"}), 413

    payload = request.get_json(force=True, silent=True) or {}
    code = str(payload.get("code", ""))
    if len(code) > MAX_CODE_LENGTH:
        return (
            jsonify({"error": f"Código demasiado largo (máx {MAX_CODE_LENGTH} caracteres)."}),
            400,
        )

    try:
        result = kernel_execute(kid, code)
    except KeyError:
        return jsonify({"error": "kernel no encontrado"}), 404
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400
    return jsonify(result)


@app.post("/api/kernel/<kid>/interrupt")
def api_kernel_interrupt(kid: str):
    """Envía SIGINT a la ejecución actual del kernel."""
    if not _valid_kernel_id(kid):
        return jsonify({"error": "kernel_id inválido"}), 400
    try:
        kernel_interrupt(kid)
    except KeyError:
        return jsonify({"error": "kernel no encontrado"}), 404
    return ("", 204)


@app.post("/api/kernel/<kid>/restart")
def api_kernel_restart(kid: str):
    """Reinicia el kernel (limpia variables; mismo kernel_id)."""
    if not _valid_kernel_id(kid):
        return jsonify({"error": "kernel_id inválido"}), 400
    try:
        kernel_restart(kid)
    except KeyError:
        return jsonify({"error": "kernel no encontrado"}), 404
    return ("", 204)


@app.delete("/api/kernel/<kid>")
def api_kernel_shutdown(kid: str):
    """Termina el proceso del kernel y libera recursos."""
    if not _valid_kernel_id(kid):
        return jsonify({"error": "kernel_id inválido"}), 400
    try:
        kernel_shutdown(kid)
    except KeyError:
        return jsonify({"error": "kernel no encontrado"}), 404
    return ("", 204)


if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=False)
