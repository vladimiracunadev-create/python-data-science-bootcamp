"""Demo rápida del flujo de análisis del bootcamp.

Este ejemplo resuelve una necesidad concreta de onboarding: mostrar, en pocos
pasos, cómo cargar datos, calcular métricas útiles y producir una visualización
lista para compartir.
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.utils import add_total_column, load_csv, tasa_perdida_clientes


def main() -> None:
    """Ejecuta una demostración corta de análisis comercial y retención."""
    # Cargamos ventas y calculamos métricas derivadas para resumir el negocio.
    ventas = load_csv("ventas_tienda.csv")
    ventas = add_total_column(ventas)
    resumen = ventas.groupby("categoria", as_index=False)["total_neto"].sum()
    print("Resumen de ventas por categoría")
    print(resumen.to_string(index=False))

    # Luego calculamos una tasa de pérdida para mostrar otro caso de uso.
    clientes = load_csv("retencion_clientes.csv")
    clientes = tasa_perdida_clientes(clientes)
    print("\nTasa de pérdida mensual")
    print(clientes[["mes", "tasa_perdida"]].to_string(index=False))

    # Finalmente guardamos un gráfico para evidenciar el resultado visual.
    plt.figure(figsize=(7, 4))
    plt.bar(resumen["categoria"], resumen["total_neto"])
    plt.title("Ventas netas por categoría")
    plt.tight_layout()
    output = BASE_DIR / "examples" / "demo_chart.png"
    plt.savefig(output)
    print(f"\nGráfico guardado en: {output}")


if __name__ == "__main__":
    main()
