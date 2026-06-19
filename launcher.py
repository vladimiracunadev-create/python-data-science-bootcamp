"""Launcher de escritorio para el Python Data Science Program.

Qué resuelve:
    Arranca la app Windows **nativa** del programa — ventana Qt con widgets
    reales (PySide6), SIN levantar servidor HTTP, SIN navegador embebido,
    SIN localhost. Es el entry point que ejecuta el instalador (Inno Setup)
    y el bundle PyInstaller (``program.spec``).

Si el alumno quiere ejecutar código Python sobre los notebooks, lo hace
desde el laboratorio Flask + kernel Jupyter (módulo ``app``), que es una
superficie separada que se levanta con ``python -m app.app``. Esta app
desktop es solo para revisión del contenido (README, celdas, links a
PDF/PPTX/notebook).
"""

from __future__ import annotations

import sys


def main() -> int:
    """Entry point del .exe / del comando ``python launcher.py``."""
    # Import tardío: PyInstaller detecta dependencias por análisis estático,
    # pero queremos que un error de import de PySide6 produzca un mensaje
    # claro y no un traceback antes de tener consola.
    try:
        from app_desktop.main import main as run
    except ImportError as exc:  # pragma: no cover - solo afecta a usuarios sin deps
        sys.stderr.write(
            "ERROR: No se pudo importar app_desktop. "
            "Instalá PySide6 con `pip install PySide6`.\n"
            f"Detalle: {exc}\n"
        )
        return 1

    return run()


if __name__ == "__main__":
    raise SystemExit(main())
