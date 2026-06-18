"""Carga notebooks reales del currículo para el laboratorio Flask.

Este módulo complementa a ``content_loader``: mientras aquel sirve READMEs y
plantillas de notebooks de la app, este lee los ``notebook.ipynb`` originales
de cada clase del programa (232 clases en 9 partes) y los entrega como una
estructura JSON-friendly lista para renderizar en el frontend.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import markdown as _markdown

try:  # nbformat es el parser canónico de .ipynb; el fallback a json es defensivo.
    import nbformat as _nbformat
except Exception:  # pragma: no cover - entorno sin nbformat
    _nbformat = None


def _resolve_base_dir() -> Path:
    """Resuelve la raíz del proyecto en desarrollo y en PyInstaller.

    Qué resuelve:
        Garantiza que el módulo encuentre ``classes/`` tanto al correr desde
        código fuente como desde un ejecutable empaquetado con ``_MEIPASS``.
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parents[1]


BASE_DIR = _resolve_base_dir()
CLASS_DIR = BASE_DIR / "classes"

SAFE_NAME_RE = re.compile(r"^[\w\-/]{1,160}$")
_PART_NUM_RE = re.compile(r"^parte-(\d+)")
_CLASS_NUM_RE = re.compile(r"^(\d{1,3})")


def _safe_resolve(base: Path, name: str) -> Path:
    """Resuelve una ruta y verifica que permanezca dentro del directorio base.

    Qué resuelve:
        Bloquea intentos de path traversal (``../``) en slugs recibidos desde
        la capa HTTP antes de tocar el filesystem.
    """
    resolved = (base / name).resolve()
    if not str(resolved).startswith(str(base.resolve())):
        raise PermissionError(f"Acceso fuera del directorio permitido: {name}")
    return resolved


def _read_first_h1(readme: Path) -> str | None:
    """Devuelve el primer ``# H1`` del README, o ``None`` si no existe."""
    if not readme.exists():
        return None
    for line in readme.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped.lstrip("# ").strip()
    return None


def _part_number(folder_name: str) -> int:
    """Extrae el número de parte desde ``parte-N-...``; ``-1`` si no matchea."""
    m = _PART_NUM_RE.match(folder_name)
    return int(m.group(1)) if m else -1


def _class_number(folder_name: str) -> int:
    """Extrae el número de clase desde ``NNN-...``; ``-1`` si no matchea."""
    m = _CLASS_NUM_RE.match(folder_name)
    return int(m.group(1)) if m else -1


def _derive_title_from_folder(folder_name: str) -> str:
    """Genera un título legible a partir del nombre de carpeta."""
    return folder_name.replace("-", " ").strip().capitalize()


def list_curriculum() -> list[dict[str, Any]]:
    """Devuelve el árbol completo del currículo agrupado por parte.

    Qué resuelve:
        Permite a la UI del laboratorio mostrar el menú jerárquico
        Parte → Clase sin recorrer el filesystem en cada request del frontend.
    """
    parts_map: dict[int, dict[str, Any]] = {}

    # Iteramos por carpetas de clase, NO por notebooks: el currículo cuenta
    # README.md (232 clases en v3.5.0) — el notebook.ipynb es un artefacto
    # opcional que existe en 197/232 (las 35 sin notebook son las clases
    # dedicadas modernas: Polars, Optuna, Ray Tune, Lightning, etc., cuyo
    # README es completo pero el .ipynb está pendiente de generar).
    # Marcamos `has_notebook` para que la UI deshabilite "Ejecutar" cuando falta.
    for part_dir in CLASS_DIR.glob("parte-*"):
        if not part_dir.is_dir():
            continue
        part_num = _part_number(part_dir.name)
        if part_num < 0:
            continue

        for class_dir in part_dir.iterdir():
            if not class_dir.is_dir():
                continue
            class_num = _class_number(class_dir.name)
            if class_num < 0:
                continue
            if not (class_dir / "README.md").exists():
                continue  # carpeta huérfana sin README — se ignora.

            if part_num not in parts_map:
                part_title = _read_first_h1(part_dir / "README.md") or _derive_title_from_folder(part_dir.name)
                parts_map[part_num] = {
                    "part_slug": part_dir.name,
                    "part_title": part_title,
                    "part_number": part_num,
                    "classes": [],
                }

            class_title = _read_first_h1(class_dir / "README.md") or _derive_title_from_folder(class_dir.name)
            rel_slug = class_dir.relative_to(CLASS_DIR).as_posix()
            parts_map[part_num]["classes"].append(
                {
                    "slug": rel_slug,
                    "number": class_num,
                    "title": class_title,
                    "has_notebook": (class_dir / "notebook.ipynb").exists(),
                }
            )

    result = sorted(parts_map.values(), key=lambda p: p["part_number"])
    for part in result:
        part["classes"].sort(key=lambda c: c["number"])
    return result


def _normalize_source(source: Any) -> str:
    """nbformat puede devolver la fuente como lista de líneas; la unifica."""
    if isinstance(source, list):
        return "".join(source)
    if source is None:
        return ""
    return str(source)


def _json_safe_outputs(outputs: Any) -> list[dict[str, Any]]:
    """Filtra outputs de celdas de código para que sean JSON-serializables."""
    if not outputs:
        return []
    safe: list[dict[str, Any]] = []
    for out in outputs:
        try:
            json.dumps(out, default=str)
            safe.append(dict(out))
        except (TypeError, ValueError):
            continue
    return safe


def _parse_notebook(path: Path) -> dict[str, Any]:
    """Lee un .ipynb usando nbformat si está disponible, con fallback a json."""
    if _nbformat is not None:
        nb = _nbformat.read(str(path), as_version=4)
        return dict(nb)
    return json.loads(path.read_text(encoding="utf-8"))


def load_notebook(class_slug: str) -> dict[str, Any]:
    """Carga el ``notebook.ipynb`` de una clase y lo entrega listo para la UI.

    Qué resuelve:
        Convierte el notebook de la clase a una estructura JSON estable, con
        markdown ya renderizado a HTML, para que el frontend del laboratorio
        no tenga que parsear nbformat ni convertir markdown en el cliente.
    """
    if not SAFE_NAME_RE.match(class_slug):
        raise ValueError(f"Slug inválido: {class_slug}")

    class_dir = _safe_resolve(CLASS_DIR, class_slug)
    if not class_dir.exists() or not class_dir.is_dir():
        raise FileNotFoundError(class_slug)

    notebook_path = class_dir / "notebook.ipynb"
    if not notebook_path.exists():
        raise FileNotFoundError(f"{class_slug}/notebook.ipynb")

    nb = _parse_notebook(notebook_path)
    title = _read_first_h1(class_dir / "README.md") or _derive_title_from_folder(class_dir.name)

    raw_cells = nb.get("cells", []) or []
    cells: list[dict[str, Any]] = []
    for idx, cell in enumerate(raw_cells):
        cell_type = cell.get("cell_type", "raw")
        source = _normalize_source(cell.get("source"))
        entry: dict[str, Any] = {
            "id": f"cell-{idx}",
            "type": cell_type,
            "source": source,
        }
        if cell_type == "markdown":
            entry["rendered_html"] = _markdown.markdown(
                source, extensions=["fenced_code", "tables"]
            )
        elif cell_type == "code":
            entry["outputs"] = _json_safe_outputs(cell.get("outputs"))
        cells.append(entry)

    kernel_name = (
        nb.get("metadata", {})
        .get("kernelspec", {})
        .get("name", "python3")
    )

    return {
        "slug": class_slug,
        "title": title,
        "cells": cells,
        "metadata": {
            "kernel": kernel_name,
            "n_cells": len(cells),
        },
    }
