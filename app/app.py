from __future__ import annotations

from pathlib import Path

from flask import Flask, jsonify, render_template, request
import markdown

from .content_loader import list_classes, list_notebook_templates, load_notebook_template, read_class_markdown, save_notebook
from .execution_engine import execute_code, reset_session

BASE_DIR = Path(__file__).resolve().parents[1]
app = Flask(__name__, template_folder=str(BASE_DIR / "app" / "templates"), static_folder=str(BASE_DIR / "app" / "static"))


@app.get("/")
def index():
    return render_template("index.html", classes=list_classes(), templates=list_notebook_templates())


@app.get("/api/classes")
def api_classes():
    return jsonify(list_classes())


@app.get("/api/class/<slug>")
def api_class_detail(slug: str):
    data = read_class_markdown(slug)
    html = {name: markdown.markdown(text, extensions=["fenced_code", "tables"]) for name, text in data.items()}
    return jsonify({"slug": slug, "html": html, "raw": data})


@app.get("/api/notebooks")
def api_notebooks():
    return jsonify(list_notebook_templates())


@app.get("/api/notebook/<template_id>")
def api_notebook_detail(template_id: str):
    return jsonify(load_notebook_template(template_id))


@app.post("/api/notebook/save")
def api_notebook_save():
    payload = request.get_json(force=True)
    name = payload.get("name", "mi_notebook")
    path = save_notebook(name, payload)
    return jsonify({"ok": True, "saved_to": str(path.relative_to(BASE_DIR))})


@app.post("/api/execute")
def api_execute():
    payload = request.get_json(force=True)
    notebook_id = payload.get("notebook_id", "default")
    code = payload.get("code", "")
    return jsonify(execute_code(notebook_id, code))


@app.post("/api/reset")
def api_reset():
    payload = request.get_json(force=True)
    notebook_id = payload.get("notebook_id", "default")
    reset_session(notebook_id)
    return jsonify({"ok": True, "message": f"Sesión {notebook_id} reiniciada"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
