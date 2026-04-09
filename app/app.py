"""Aplicación Flask del bootcamp Python para Data Science.

Este módulo resuelve la capa HTTP del sistema local: publica la interfaz web,
expone APIs para clases y notebooks, y conecta la ejecución de código con el
contenido docente almacenado en disco.
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

import markdown
from flask import Flask, jsonify, render_template, request, send_file, url_for

from .content_loader import (
    get_class_assets,
    list_classes,
    list_notebook_templates,
    load_class_quiz,
    load_notebook_template,
    read_class_markdown,
    resolve_class_asset_path,
    save_notebook,
)
from .execution_engine import MAX_CODE_LENGTH, execute_code, reset_session


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

MAX_PAYLOAD_BYTES = 1_000_000  # 1 MB
SLUG_RE = re.compile(r"^[\w\-]{1,80}$")
DEFAULT_HOST = os.getenv("BOOTCAMP_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.getenv("BOOTCAMP_PORT", "8000"))


def _valid_slug(slug: str) -> bool:
    """Valida identificadores de clases y notebooks expuestos por la API."""
    return bool(SLUG_RE.match(slug))


@app.after_request
def add_security_headers(response):
    """Añade cabeceras básicas para endurecer la app local en navegador.

    Qué resuelve:
        Reduce riesgos comunes de contenido embebido, sniffing y políticas de
        origen al servir una aplicación que ejecuta código local del alumno.
    """
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    response.headers.setdefault("Referrer-Policy", "no-referrer")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
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


@app.get("/")
def index():
    """Renderiza la vista principal con catálogo de clases y laboratorios."""
    return render_template("index.html", classes=list_classes(), templates=list_notebook_templates())


@app.get("/health")
def health():
    """Expone un healthcheck liviano para launcher, tests y monitoreo local."""
    return jsonify({"status": "ok", "service": "python-data-science-bootcamp"})


@app.get("/ready")
def ready():
    """Confirma que la app puede listar clases y notebooks antes de usarse."""
    classes = list_classes()
    templates = list_notebook_templates()
    return jsonify(
        {
            "status": "ready",
            "service": "python-data-science-bootcamp",
            "classes": len(classes),
            "notebooks": len(templates),
        }
    )


@app.get("/api/classes")
def api_classes():
    """Devuelve el catálogo de clases para la web y la app de escritorio."""
    return jsonify(list_classes())


@app.get("/api/class/<slug>")
def api_class_detail(slug: str):
    """Entrega markdown y quiz de una clase en formato consumible por la UI.

    Qué resuelve:
        Convierte el contenido docente almacenado en disco en un payload JSON con
        HTML y texto crudo, listo para renderizar y reutilizar en la aplicación.
    """
    if not _valid_slug(slug):
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
        kind: {
            **meta,
            "url": url_for("download_class_asset", slug=slug, asset_kind=kind),
        }
        for kind, meta in assets.items()
    }
    return jsonify({"slug": slug, "html": html, "raw": data, "quiz": quiz, "assets": asset_payload})


@app.get("/downloads/class/<slug>/<asset_kind>")
def download_class_asset(slug: str, asset_kind: str):
    """Sirve guías PDF y presentaciones PPTX derivadas de una clase.

    Qué resuelve:
        Permite abrir o descargar desde la interfaz los materiales listos para
        compartir, sin obligar al usuario a buscar los archivos dentro del repo.
    """
    if not _valid_slug(slug):
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


@app.get("/api/notebooks")
def api_notebooks():
    """Lista plantillas de laboratorio disponibles en la app."""
    return jsonify(list_notebook_templates())


@app.get("/api/notebook/<template_id>")
def api_notebook_detail(template_id: str):
    """Entrega el contenido de una plantilla de notebook por identificador."""
    if not _valid_slug(template_id):
        return jsonify({"error": "id inválido"}), 400
    try:
        return jsonify(load_notebook_template(template_id))
    except FileNotFoundError:
        return jsonify({"error": "notebook no encontrado"}), 404


@app.post("/api/notebook/save")
def api_notebook_save():
    """Guarda un notebook editado por el alumno dentro del directorio seguro."""
    if request.content_length and request.content_length > MAX_PAYLOAD_BYTES:
        return jsonify({"error": "payload demasiado grande"}), 413

    payload = request.get_json(force=True, silent=True) or {}
    name = re.sub(r"[^a-z0-9_\-]", "_", str(payload.get("name", "mi_notebook"))[:80])
    path = save_notebook(name, payload)
    return jsonify({"ok": True, "saved_to": str(path.relative_to(BASE_DIR))})


@app.post("/api/execute")
def api_execute():
    """Ejecuta una celda del notebook interactivo y devuelve su resultado."""
    if request.content_length and request.content_length > MAX_PAYLOAD_BYTES:
        return jsonify({"error": "payload demasiado grande"}), 413

    payload = request.get_json(force=True, silent=True) or {}
    notebook_id = str(payload.get("notebook_id", "default"))[:80]
    code = str(payload.get("code", ""))
    if len(code) > MAX_CODE_LENGTH:
        return jsonify({"error": f"Código demasiado largo (máx {MAX_CODE_LENGTH} caracteres)."}), 400
    return jsonify(execute_code(notebook_id, code))


@app.post("/api/reset")
def api_reset():
    """Reinicia el estado persistente de una sesión de notebook."""
    payload = request.get_json(force=True, silent=True) or {}
    notebook_id = str(payload.get("notebook_id", "default"))[:80]
    reset_session(notebook_id)
    return jsonify({"ok": True, "message": f"Sesión {notebook_id} reiniciada"})


if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=False)
