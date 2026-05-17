"""Genera la guía ampliada de estudio de Python con Data Science.

Responsabilidades:
    1. Convertir la guía extensa investigada desde `docs/entrevista/` a PDF.
    2. Mantener un nombre de salida estable para estudio e impresión.
    3. Separar esta pieza grande del set canónico de entrevista.

Qué resuelve:
    Permite regenerar un documento de estudio profundo, casi tipo manual,
    sin mezclarlo con los tres PDFs principales de entrevista.
"""

from __future__ import annotations

from pathlib import Path

from generar_pdf_documento import render_markdown

BASE_DIR = Path(__file__).resolve().parents[1]
SOURCE_PATH = BASE_DIR / "docs" / "entrevista" / "guia-total-python-data-science.md"
OUTPUT_PATH = BASE_DIR / "docs" / "pdfs" / "guia-total-python-data-science.pdf"


def main() -> None:
    """Genera el PDF ampliado de estudio de Python con Data Science."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    render_markdown(
        input_path=SOURCE_PATH,
        output_path=OUTPUT_PATH,
        title="Guía total de estudio: Python con Data Science",
        subtitle=(
            "Manual ampliado para estudiar fundamentos, herramientas, estadística, "
            "machine learning, buenas prácticas y rutas de dominio del área."
        ),
        style="print",
    )
    print(f"[OK] {OUTPUT_PATH.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
