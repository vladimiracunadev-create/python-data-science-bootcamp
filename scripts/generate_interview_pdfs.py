"""Genera los tres PDFs canónicos de entrevista y estudio del repositorio.

Responsabilidades:
    1. Convertir las tres piezas principales de `docs/entrevista/` a PDF.
    2. Mantener nombres de salida estables y fáciles de ubicar.
    3. Separar estos dossieres de otras notas personales del proceso.
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
        "title": "Muestra del producto y enfoque docente",
        "subtitle": "Dossier breve para explicar el repositorio, la propuesta y la manera de enseñar.",
    },
    {
        "input": INTERVIEW_DIR / "preguntas-para-hacer-en-entrevista.md",
        "output": PDF_DIR / "preguntas-para-hacer-en-entrevista.pdf",
        "title": "Preguntas para hacer en la entrevista",
        "subtitle": "Guía personal para aclarar alcance, condiciones, contexto y riesgos antes de comprometer trabajo.",
    },
    {
        "input": INTERVIEW_DIR / "guia-estudio-repositorio.md",
        "output": PDF_DIR / "guia-estudio-repositorio.pdf",
        "title": "Guía maestra de estudio del repositorio",
        "subtitle": "Documento principal para estudiar producto, pedagogía, arquitectura y contenidos a profundidad.",
    },
]


def main() -> None:
    """Genera todos los PDFs principales de la carpeta de entrevista."""
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    for doc in DOCUMENTS:
        render_markdown(
            input_path=doc["input"],
            output_path=doc["output"],
            title=doc["title"],
            subtitle=doc["subtitle"],
            style="print",
        )
        print(f"[OK] {doc['output'].relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
