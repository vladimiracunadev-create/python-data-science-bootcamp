"""Validador rápido de datasets y artefactos clave del bootcamp.

Este script resuelve una verificación operacional simple: comprobar que los
archivos base existen y que el proyecto tiene los componentes mínimos para usar
las demos y la app interactiva.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.utils import load_csv


def main() -> None:
    """Construye un reporte JSON con estado de datasets y archivos clave."""
    expected = [
        "ventas_tienda.csv",
        "estudiantes.csv",
        "transporte.csv",
        "soporte_tickets.csv",
        "retencion_clientes.csv",
    ]
    report = {"datasets": {}, "checks": {}}

    for filename in expected:
        try:
            df = load_csv(filename)
            report["datasets"][filename] = {
                "ok": True,
                "rows": int(df.shape[0]),
                "columns": int(df.shape[1]),
            }
        except Exception as exc:  # pragma: no cover - reporte operativo simple
            report["datasets"][filename] = {"ok": False, "error": str(exc)}

    # Estos checks dejan visible si el proyecto está completo para la demo local.
    report["checks"]["interactive_app_exists"] = (BASE_DIR / "app" / "app.py").exists()
    report["checks"]["docker_exists"] = (BASE_DIR / "Dockerfile").exists()

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
