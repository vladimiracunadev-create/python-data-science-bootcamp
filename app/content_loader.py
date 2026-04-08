from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


def _resolve_base_dir() -> Path:
    """
    Resuelve el directorio raiz del proyecto de forma compatible con
    ejecucion normal (python launcher.py) y con bundles de PyInstaller.

    PyInstaller congela el codigo en un directorio temporal (sys._MEIPASS)
    donde coloca las DLLs y los archivos .pyc. Los datas (clases, notebooks,
    templates) se copian al mismo nivel que sys._MEIPASS en modo onedir.

    Modo normal:
        BASE_DIR = raiz del repositorio (parents[1] de este archivo)

    Modo PyInstaller (sys.frozen = True):
        BASE_DIR = sys._MEIPASS  (donde PyInstaller extrae todos los datas)
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        # Bundle de PyInstaller: los archivos de datos estan en _MEIPASS
        return Path(sys._MEIPASS)
    # Ejecucion normal: subir dos niveles desde app/content_loader.py → raiz
    return Path(__file__).resolve().parents[1]


def _resolve_saved_notebooks_dir() -> Path:
    """
    Directorio para los notebooks guardados por alumnos.

    En modo PyInstaller el directorio _MEIPASS es de solo lectura,
    por lo que los notebooks se guardan junto al ejecutable real.
    En modo normal se usa la carpeta del repositorio.
    """
    if getattr(sys, "frozen", False):
        # Junto al .exe instalado — es escribible por el usuario
        return Path(sys.executable).parent / "saved_notebooks"
    return Path(__file__).resolve().parents[1] / "app" / "saved_notebooks"


BASE_DIR = _resolve_base_dir()
CLASS_DIR = BASE_DIR / "classes"
NOTEBOOK_TEMPLATES_DIR = BASE_DIR / "app" / "notebooks"
SAVED_NOTEBOOKS_DIR = _resolve_saved_notebooks_dir()

SAFE_NAME_RE = re.compile(r"^[\w\-]{1,80}$")


def _safe_resolve(base: Path, name: str) -> Path:
    """Resuelve una ruta dentro de base y valida que no salga del directorio."""
    resolved = (base / name).resolve()
    if not str(resolved).startswith(str(base.resolve())):
        raise PermissionError(f"Acceso fuera del directorio permitido: {name}")
    return resolved


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
    if not SAFE_NAME_RE.match(slug):
        raise ValueError(f"Slug inválido: {slug}")
    class_dir = _safe_resolve(CLASS_DIR, slug)
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
    if not SAFE_NAME_RE.match(template_id):
        raise ValueError(f"ID inválido: {template_id}")
    path = _safe_resolve(NOTEBOOK_TEMPLATES_DIR, f"{template_id}.json")
    if not path.exists():
        raise FileNotFoundError(template_id)
    return json.loads(path.read_text(encoding="utf-8"))


def save_notebook(name: str, payload: dict[str, Any]) -> Path:
    safe_name = re.sub(r"[^a-z0-9_\-]", "_", name[:80])
    SAVED_NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
    target = _safe_resolve(SAVED_NOTEBOOKS_DIR, f"{safe_name}.json")
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return target
