"""Punto de entrada mínimo para levantar la app Flask del bootcamp.

Este script resuelve el caso simple de ejecución desde el repositorio: toma
host y puerto desde variables de entorno y arranca la aplicación sin pasar por
el launcher de Windows o por PyInstaller.
"""

from __future__ import annotations

import os

from app.app import app


def main() -> None:
    """Lee la configuración básica del entorno y arranca Flask."""
    host = os.getenv("BOOTCAMP_HOST", "127.0.0.1")
    port = int(os.getenv("BOOTCAMP_PORT", "8000"))
    app.run(host=host, port=port, debug=False)


if __name__ == "__main__":
    main()
