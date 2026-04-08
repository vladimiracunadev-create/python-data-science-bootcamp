from __future__ import annotations

from pathlib import Path
import sys
import json

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.utils import load_csv


def main() -> None:
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
            report["datasets"][filename] = {"ok": True, "rows": int(df.shape[0]), "columns": int(df.shape[1])}
        except Exception as exc:
            report["datasets"][filename] = {"ok": False, "error": str(exc)}

    report["checks"]["interactive_app_exists"] = (BASE_DIR / "app" / "app.py").exists()
    report["checks"]["docker_exists"] = (BASE_DIR / "Dockerfile").exists()

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
