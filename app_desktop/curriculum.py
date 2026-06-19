"""Adapter del currículo para la app desktop.

Qué resuelve:
    Reusa ``app.notebook_loader`` (single source of truth del currículo)
    asegurando que el import funcione tanto desde el repo en modo dev como
    desde un bundle PyInstaller (``sys._MEIPASS``). Suma helpers para
    localizar PDF/PPTX/carpeta de cada clase y abrirlos con el sistema.
"""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices

log = logging.getLogger(__name__)


def _project_root() -> Path:
    """Raíz del proyecto en dev o del bundle congelado.

    Resuelve ``sys._MEIPASS`` cuando se corre desde PyInstaller; cae al
    directorio padre del paquete en dev.
    """
    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parents[1]


ROOT = _project_root()
CLASSES_DIR = ROOT / "classes"

# Asegura que `app.notebook_loader` sea importable tanto en dev como en bundle.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    from app.notebook_loader import list_curriculum, load_notebook  # noqa: E402
except Exception as exc:  # pragma: no cover - entorno sin app/
    log.warning("No se pudo importar app.notebook_loader: %s", exc)

    def list_curriculum() -> list[dict[str, Any]]:  # type: ignore[no-redef]
        return []

    def load_notebook(slug: str) -> dict[str, Any]:  # type: ignore[no-redef]
        raise FileNotFoundError(slug)


def resolve_resource_path(rel: str) -> str | None:
    """Resuelve una ruta relativa contra la raíz del proyecto / bundle.

    Devuelve la ruta absoluta como str si existe, ``None`` si no.
    """
    candidate = ROOT / rel
    if candidate.exists():
        return str(candidate)
    return None


def class_dir(slug: str) -> Path:
    """Devuelve la carpeta de una clase dada su slug ``parte-X/NNN-tema``."""
    return CLASSES_DIR / slug


def class_readme(slug: str) -> Path | None:
    """Ruta al README.md de la clase, o None si no existe."""
    path = class_dir(slug) / "README.md"
    return path if path.exists() else None


def class_pdf(slug: str) -> Path | None:
    """Ruta al PDF ``clase-NNN-...-guia-explicativa.pdf`` o None."""
    folder = class_dir(slug)
    if not folder.exists():
        return None
    matches = sorted(folder.glob("clase-*-guia-explicativa.pdf"))
    if matches:
        return matches[0]
    # Fallback: cualquier PDF en la carpeta.
    any_pdf = sorted(folder.glob("*.pdf"))
    return any_pdf[0] if any_pdf else None


def class_pptx(slug: str) -> Path | None:
    """Ruta al PPTX ``clase-NNN-...-presentacion.pptx`` o None."""
    folder = class_dir(slug)
    if not folder.exists():
        return None
    matches = sorted(folder.glob("clase-*-presentacion.pptx"))
    if matches:
        return matches[0]
    any_pptx = sorted(folder.glob("*.pptx"))
    return any_pptx[0] if any_pptx else None


def class_notebook(slug: str) -> Path | None:
    """Ruta al notebook.ipynb de la clase o None."""
    path = class_dir(slug) / "notebook.ipynb"
    return path if path.exists() else None


def open_with_system(path: Path | str) -> bool:
    """Abre un archivo o carpeta con la aplicación por defecto del sistema."""
    p = Path(path)
    if not p.exists():
        log.warning("No se puede abrir, no existe: %s", p)
        return False
    return QDesktopServices.openUrl(QUrl.fromLocalFile(str(p)))


__all__ = [
    "ROOT",
    "CLASSES_DIR",
    "list_curriculum",
    "load_notebook",
    "resolve_resource_path",
    "class_dir",
    "class_readme",
    "class_pdf",
    "class_pptx",
    "class_notebook",
    "open_with_system",
]
