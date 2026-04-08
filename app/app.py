from __future__ import annotations

import os
import re
from pathlib import Path

from flask import Flask, jsonify, render_template, request
import markdown

from .content_loader import list_classes, list_notebook_templates, load_notebook_template, read_class_markdown, save_notebook
from .execution_engine import execute_code, reset_session, MAX_CODE_LENGTH

BASE_DIR = Path(__file__).resolve().parents[1]
app = Flask(__name__, template_folder=str(BASE_DIR / "app" / "templates"), static_folder=str(BASE_DIR / "app" / "static"))

MAX_PAYLOAD_BYTES = 1_000_000  # 1 MB
SLUG_RE = re.compile(r"^[\w\-]{1,80}$")
DEFAULT_HOST = os.getenv("BOOTCAMP_HOST", "127.0.0.1")
DEFAULT_PORT = int(os.getenv("BOOTCAMP_PORT", "8000"))


def _valid_slug(slug: str) -> bool:
    return bool(SLUG_RE.match(slug))


@app.after_request
def add_security_headers(response):
    response.headers.setdefault("X-Content-Type-Options", "nosniff")
    response.headers.setdefault("X-Frame-Options", "SAMEORIGIN")
    response.headers.setdefault("Referrer-Policy", "no-referrer")
    response.headers.setdefault("Permissions-Policy", "camera=(), microphone=(), geolocation=()")
    return response


@app.get("/")
def index():
    return render_template("index.html", classes=list_classes(), templates=list_notebook_templates())


@app.get("/api/classes")
def api_classes():
    return jsonify(list_classes())


@app.get("/api/class/<slug>")
def api_class_detail(slug: str):
    if not _valid_slug(slug):
        return jsonify({"error": "slug inválido"}), 400
    try:
        data = read_class_markdown(slug)
    except FileNotFoundError:
        return jsonify({"error": "clase no encontrada"}), 404
    html = {name: markdown.markdown(text, extensions=["fenced_code", "tables"]) for name, text in data.items()}
    return jsonify({"slug": slug, "html": html, "raw": data})


@app.get("/api/notebooks")
def api_notebooks():
    return jsonify(list_notebook_templates())


@app.get("/api/notebook/<template_id>")
def api_notebook_detail(template_id: str):
    if not _valid_slug(template_id):
        return jsonify({"error": "id inválido"}), 400
    try:
        return jsonify(load_notebook_template(template_id))
    except FileNotFoundError:
        return jsonify({"error": "notebook no encontrado"}), 404


@app.post("/api/notebook/save")
def api_notebook_save():
    if request.content_length and request.content_length > MAX_PAYLOAD_BYTES:
        return jsonify({"error": "payload demasiado grande"}), 413
    payload = request.get_json(force=True, silent=True) or {}
    name = re.sub(r"[^a-z0-9_\-]", "_", str(payload.get("name", "mi_notebook"))[:80])
    path = save_notebook(name, payload)
    return jsonify({"ok": True, "saved_to": str(path.relative_to(BASE_DIR))})


@app.post("/api/execute")
def api_execute():
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
    payload = request.get_json(force=True, silent=True) or {}
    notebook_id = str(payload.get("notebook_id", "default"))[:80]
    reset_session(notebook_id)
    return jsonify({"ok": True, "message": f"Sesión {notebook_id} reiniciada"})


if __name__ == "__main__":
    app.run(host=DEFAULT_HOST, port=DEFAULT_PORT, debug=False)
