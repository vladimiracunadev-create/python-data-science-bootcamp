"""Bootstrap de la app desktop PySide6.

Qué resuelve:
    Configura QApplication (nombre, versión, ícono si existe), instancia la
    MainWindow y arranca el event loop con manejo de KeyboardInterrupt.
"""

from __future__ import annotations

import logging
import signal
import sys
from pathlib import Path

from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from app_desktop import __version__
from app_desktop.curriculum import app_icon_path
from app_desktop.main_window import MainWindow


def _setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def main() -> int:
    """Punto de entrada del binario / `python -m app_desktop`."""
    _setup_logging()
    log = logging.getLogger("app_desktop")

    QCoreApplication.setOrganizationName("PythonDataScienceProgram")
    QCoreApplication.setApplicationName("Python Data Science Program")
    QCoreApplication.setApplicationVersion(__version__)

    app = QApplication(sys.argv)

    # Permitir Ctrl+C en consola desde el event loop de Qt.
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Ícono del producto — el mismo .ico que lleva el .exe y el instalador.
    icon_path = app_icon_path()
    if icon_path and Path(icon_path).exists():
        app.setWindowIcon(QIcon(str(icon_path)))
    else:
        log.debug("Sin icono de producto: corré scripts/generate_product_icon.py")

    try:
        window = MainWindow()
        window.show()
        log.info("App desktop v%s iniciada", __version__)
        return app.exec()
    except KeyboardInterrupt:
        log.info("Interrumpido por usuario")
        return 0


if __name__ == "__main__":
    sys.exit(main())
