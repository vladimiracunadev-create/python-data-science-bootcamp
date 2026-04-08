from __future__ import annotations

import json
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[1]
CLASS_DIR = BASE_DIR / "classes"
NOTEBOOK_TEMPLATES_DIR = BASE_DIR / "app" / "notebooks"
SAVED_NOTEBOOKS_DIR = BASE_DIR / "app" / "saved_notebooks"


def list_classes() -> list[dict[str, str]]:
    items = []
    for class_dir in sorted(CLASS_DIR.iterdir()):
        if not class_dir.is_dir():
            continue
        readme = class_dir / "README.md"
        title = class_dir.name
        if readme.exists():
            first = readme.read_text(encoding="utf-8").splitlines()[0].strip()
            title = first.lstrip("# ")
        items.append({"slug": class_dir.name, "title": title, "path": str(class_dir.relative_to(BASE_DIR))})
    return items


def read_class_markdown(slug: str) -> dict[str, str]:
    class_dir = CLASS_DIR / slug
    if not class_dir.exists():
        raise FileNotFoundError(slug)
    result = {}
    for name in ["README.md", "slides.md", "ejercicios.md", "homework.md"]:
        path = class_dir / name
        result[name] = path.read_text(encoding="utf-8") if path.exists() else ""
    return result


def list_notebook_templates() -> list[dict[str, str]]:
    items = []
    for path in sorted(NOTEBOOK_TEMPLATES_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        items.append({"id": path.stem, "title": data.get("title", path.stem), "description": data.get("description", "Notebook interactivo")})
    return items


def load_notebook_template(template_id: str) -> dict[str, Any]:
    path = NOTEBOOK_TEMPLATES_DIR / f"{template_id}.json"
    if not path.exists():
        raise FileNotFoundError(template_id)
    return json.loads(path.read_text(encoding="utf-8"))


def save_notebook(name: str, payload: dict[str, Any]) -> Path:
    SAVED_NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
    target = SAVED_NOTEBOOKS_DIR / f"{name}.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return target
