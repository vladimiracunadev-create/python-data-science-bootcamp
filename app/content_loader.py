"""Carga y guarda contenidos locales del bootcamp.

Este módulo resuelve la capa de acceso a archivos de la aplicación Flask.
Centraliza lectura de clases, quizzes y plantillas de notebooks, y aplica
validaciones para que la app solo opere dentro de directorios permitidos.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


def _resolve_base_dir() -> Path:
    """Resuelve la raíz del proyecto tanto en desarrollo como en PyInstaller.

    Qué resuelve:
        Evita que la app pierda ubicación de clases, templates y notebooks al
        ejecutarse como código fuente o como ejecutable empaquetado.
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parents[1]


def _resolve_saved_notebooks_dir() -> Path:
    """Devuelve el directorio escribible donde se guardan notebooks del alumno.

    Qué resuelve:
        En modo PyInstaller el bundle es de solo lectura, así que los archivos
        del usuario deben vivir junto al ejecutable y no dentro de `_MEIPASS`.
    """
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent / "saved_notebooks"
    return Path(__file__).resolve().parents[1] / "app" / "saved_notebooks"


BASE_DIR = _resolve_base_dir()
CLASS_DIR = BASE_DIR / "classes"
NOTEBOOK_TEMPLATES_DIR = BASE_DIR / "app" / "notebooks"
SAVED_NOTEBOOKS_DIR = _resolve_saved_notebooks_dir()

SAFE_NAME_RE = re.compile(r"^[\w\-]{1,80}$")


def _safe_resolve(base: Path, name: str) -> Path:
    """Resuelve una ruta y verifica que permanezca dentro del directorio base.

    Qué resuelve:
        Bloquea intentos de path traversal al leer clases, quizzes o plantillas
        solicitadas desde la interfaz o desde la API.
    """
    resolved = (base / name).resolve()
    if not str(resolved).startswith(str(base.resolve())):
        raise PermissionError(f"Acceso fuera del directorio permitido: {name}")
    return resolved


def list_classes() -> list[dict[str, str]]:
    """Construye el catálogo de clases visibles para la app.

    Qué resuelve:
        Permite poblar menús y listados sin hardcodear títulos. Si existe un
        `README.md`, usa su primer encabezado como nombre legible.
    """
    items: list[dict[str, str]] = []
    for class_dir in sorted(CLASS_DIR.iterdir()):
        if not class_dir.is_dir():
            continue
        readme = class_dir / "README.md"
        title = class_dir.name
        if readme.exists():
            title = readme.read_text(encoding="utf-8").splitlines()[0].strip().lstrip("# ")
        items.append(
            {
                "slug": class_dir.name,
                "title": title,
                "path": str(class_dir.relative_to(BASE_DIR)),
            }
        )
    return items


def read_class_markdown(slug: str) -> dict[str, str]:
    """Carga el paquete de markdown asociado a una clase.

    Qué resuelve:
        Entrega en una sola llamada los documentos base de la clase para que la
        UI pueda mostrar teoría, slides, ejercicios y tarea sin lógica duplicada.
    """
    if not SAFE_NAME_RE.match(slug):
        raise ValueError(f"Slug inválido: {slug}")
    class_dir = _safe_resolve(CLASS_DIR, slug)
    if not class_dir.exists():
        raise FileNotFoundError(slug)

    result: dict[str, str] = {}
    for name in ["README.md", "teoria.md", "slides.md", "ejercicios.md", "homework.md"]:
        path = class_dir / name
        result[name] = path.read_text(encoding="utf-8") if path.exists() else ""
    return result


def load_class_quiz(slug: str) -> dict[str, Any] | None:
    """Carga el quiz JSON de una clase si existe.

    Qué resuelve:
        Separa el contenido opcional de evaluación del contenido textual para
        que la clase 0 y futuras evaluaciones puedan activarse sin romper otras clases.
    """
    if not SAFE_NAME_RE.match(slug):
        raise ValueError(f"Slug inválido: {slug}")
    class_dir = _safe_resolve(CLASS_DIR, slug)
    quiz_path = class_dir / "quiz.json"
    if not quiz_path.exists():
        return None
    return json.loads(quiz_path.read_text(encoding="utf-8"))


def list_notebook_templates() -> list[dict[str, str]]:
    """Lista las plantillas de notebooks disponibles en la app.

    Qué resuelve:
        Permite ofrecer laboratorios guiados desde metadatos simples sin abrir
        cada notebook completo hasta que el usuario realmente lo solicite.
    """
    items: list[dict[str, str]] = []
    for path in sorted(NOTEBOOK_TEMPLATES_DIR.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        items.append(
            {
                "id": path.stem,
                "title": data.get("title", path.stem),
                "description": data.get("description", "Notebook interactivo"),
            }
        )
    return items


def load_notebook_template(template_id: str) -> dict[str, Any]:
    """Abre una plantilla de notebook por identificador seguro.

    Qué resuelve:
        Da acceso controlado al contenido del laboratorio que la interfaz debe
        cargar en pantalla cuando el estudiante elige una plantilla.
    """
    if not SAFE_NAME_RE.match(template_id):
        raise ValueError(f"ID inválido: {template_id}")
    path = _safe_resolve(NOTEBOOK_TEMPLATES_DIR, f"{template_id}.json")
    if not path.exists():
        raise FileNotFoundError(template_id)
    return json.loads(path.read_text(encoding="utf-8"))


def save_notebook(name: str, payload: dict[str, Any]) -> Path:
    """Guarda el notebook del usuario con un nombre saneado.

    Qué resuelve:
        Evita que nombres arbitrarios rompan la estructura del disco y mantiene
        una ubicación estable para recuperar trabajos guardados desde la app.
    """
    safe_name = re.sub(r"[^a-z0-9_\-]", "_", name[:80])
    SAVED_NOTEBOOKS_DIR.mkdir(parents=True, exist_ok=True)
    target = _safe_resolve(SAVED_NOTEBOOKS_DIR, f"{safe_name}.json")
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return target
