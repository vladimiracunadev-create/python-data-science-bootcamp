"""Genera los PDFs de apoyo para entrevista y estudio del repositorio.

Responsabilidades:
    1. Convertir los documentos clave de `docs/entrevista/` a PDF.
    2. Mantener nombres de salida estables para compartir e imprimir.
    3. Evitar que los binarios queden desalineados con sus Markdown fuente.
"""

from __future__ import annotations

from pathlib import Path

from generar_pdf_documento import render_markdown

BASE_DIR = Path(__file__).resolve().parents[1]
INTERVIEW_DIR = BASE_DIR / "docs" / "entrevista"
PDF_DIR = BASE_DIR / "docs" / "pdfs"

DOCUMENTS = [
    {
        "input": INTERVIEW_DIR / "muestra-producto-para-skillnest.md",
        "output": PDF_DIR / "muestra-producto-para-skillnest.pdf",
        "title": "Muestra del portal y del producto",
        "subtitle": "Documento breve para reunión, demo o conversación de valor.",
    },
    {
        "input": INTERVIEW_DIR / "preguntas-para-hacer-en-entrevista.md",
        "output": PDF_DIR / "preguntas-para-hacer-en-entrevista.pdf",
        "title": "Preguntas para hacer en la entrevista",
        "subtitle": "Guía personal para aclarar alcance, pago, propiedad y contexto.",
    },
    {
        "input": INTERVIEW_DIR / "guia-estudio-repositorio.md",
        "output": PDF_DIR / "guia-estudio-repositorio.pdf",
        "title": "Guía de estudio del repositorio",
        "subtitle": "Resumen de comandos, temas y práctica para preparar la entrevista.",
    },
    {
        "input": INTERVIEW_DIR / "preparacion-entrevista-imprimible.md",
        "output": PDF_DIR / "preparacion-entrevista-imprimible.pdf",
        "title": "Preparación de entrevista imprimible",
        "subtitle": "Versión corta y clara para leer antes de entrar a la reunión.",
    },
    {
        "input": INTERVIEW_DIR / "entrevista-skillnest-presentacion-v2.md",
        "output": PDF_DIR / "entrevista-skillnest-presentacion-v2.pdf",
        "title": "Presentación breve para entrevista",
        "subtitle": "Resumen de valor, enfoque y ruta propuesta para la conversación.",
    },
]


def main() -> None:
    """Genera todos los PDFs de la carpeta de entrevista."""
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    for doc in DOCUMENTS:
        render_markdown(
            input_path=doc["input"],
            output_path=doc["output"],
            title=doc["title"],
            subtitle=doc["subtitle"],
        )
        print(f"[OK] {doc['output'].relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
