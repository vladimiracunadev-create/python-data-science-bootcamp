"""
Genera un PDF simple y presentable a partir de un archivo Markdown.

Uso:
    .venv\\Scripts\\python scripts/generar_pdf_documento.py ^
        --input docs\\entrevista-skillnest-presentacion-v2.md ^
        --output docs\\pdfs\\entrevista-skillnest-presentacion-v2.pdf ^
        --title "Bootcamp Python para Data Science" ^
        --subtitle "Demo de mi sistema de capacitacion"

Requiere: fpdf2
"""

from __future__ import annotations

import argparse
from pathlib import Path

from fpdf import FPDF


COLOR_BG = (15, 23, 42)
COLOR_PANEL = (17, 24, 39)
COLOR_ACCENT = (34, 197, 94)
COLOR_TEXT = (203, 213, 225)
COLOR_MUTED = (148, 163, 184)
COLOR_WHITE = (248, 250, 252)


def parse_line(line: str) -> tuple[str, str]:
    stripped = line.strip()
    if stripped.startswith("# "):
        return "h1", stripped[2:]
    if stripped.startswith("## "):
        return "h2", stripped[3:]
    if stripped.startswith("### "):
        return "h3", stripped[4:]
    if stripped.startswith("- "):
        return "bullet", stripped[2:]
    if stripped == "---":
        return "hr", ""
    if stripped == "":
        return "blank", ""
    return "text", stripped


class DocumentPDF(FPDF):
    def __init__(self, header_title: str):
        super().__init__()
        self.header_title = header_title
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(left=18, top=18, right=18)

    def header(self):
        self.set_fill_color(*COLOR_PANEL)
        self.rect(0, 0, 210, 14, "F")
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*COLOR_ACCENT)
        self.set_y(4)
        self.cell(0, 6, "BOOTCAMP PYTHON - DATA SCIENCE", align="L")
        self.set_text_color(*COLOR_MUTED)
        self.cell(0, 6, self.header_title, align="R")
        self.ln(8)

    def footer(self):
        self.set_y(-14)
        self.set_fill_color(*COLOR_PANEL)
        self.rect(0, 283, 210, 14, "F")
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*COLOR_MUTED)
        self.cell(0, 6, f"Pagina {self.page_no()}", align="C")

    def cover(self, title: str, subtitle: str):
        self.add_page()
        self.set_fill_color(*COLOR_BG)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*COLOR_ACCENT)
        self.rect(0, 80, 210, 4, "F")

        self.set_font("Helvetica", "B", 24)
        self.set_text_color(*COLOR_WHITE)
        self.set_xy(18, 92)
        self.multi_cell(174, 10, title)

        if subtitle:
            self.set_font("Helvetica", "", 12)
            self.set_text_color(*COLOR_MUTED)
            self.set_x(18)
            self.multi_cell(174, 7, subtitle)

    def start_body(self):
        self.add_page()
        self.set_fill_color(*COLOR_BG)
        self.rect(0, 0, 210, 297, "F")

    def h1(self, text: str):
        self.ln(8)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*COLOR_WHITE)
        self.multi_cell(self.epw, 8, text)
        y = self.get_y()
        self.set_draw_color(*COLOR_ACCENT)
        self.set_line_width(0.5)
        self.line(self.l_margin, y, self.l_margin + self.epw, y)
        self.ln(4)

    def h2(self, text: str):
        self.ln(6)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*COLOR_ACCENT)
        self.multi_cell(self.epw, 7, text)
        self.ln(2)

    def h3(self, text: str):
        self.ln(4)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*COLOR_WHITE)
        self.multi_cell(self.epw, 6, text)
        self.ln(1)

    def text(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*COLOR_TEXT)
        self.multi_cell(self.epw, 5.5, text)
        self.ln(1)

    def bullet(self, text: str):
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*COLOR_TEXT)
        self.set_x(self.l_margin + 4)
        self.cell(6, 5.5, "-", align="C")
        self.multi_cell(self.epw - 10, 5.5, text)

    def hr(self):
        self.ln(4)
        self.set_draw_color(*COLOR_PANEL)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), self.l_margin + self.epw, self.get_y())
        self.ln(4)


def extract_title(markdown: str, fallback: str) -> str:
    for line in markdown.splitlines():
        kind, value = parse_line(line)
        if kind == "h1":
            return value
    return fallback


def render_markdown(input_path: Path, output_path: Path, title: str, subtitle: str):
    markdown = input_path.read_text(encoding="utf-8")
    header_title = extract_title(markdown, title)

    pdf = DocumentPDF(header_title=header_title)
    pdf.cover(title=title, subtitle=subtitle)
    pdf.start_body()

    for line in markdown.splitlines():
        kind, value = parse_line(line)
        if kind == "h1":
            pdf.h1(value)
        elif kind == "h2":
            pdf.h2(value)
        elif kind == "h3":
            pdf.h3(value)
        elif kind == "bullet":
            pdf.bullet(value)
        elif kind == "text":
            pdf.text(value)
        elif kind == "hr":
            pdf.hr()
        elif kind == "blank":
            pdf.ln(2)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(output_path))


def main():
    parser = argparse.ArgumentParser(description="Genera un PDF a partir de un archivo Markdown.")
    parser.add_argument("--input", required=True, help="Ruta del archivo Markdown de entrada.")
    parser.add_argument("--output", required=True, help="Ruta del PDF de salida.")
    parser.add_argument("--title", required=True, help="Titulo de portada.")
    parser.add_argument("--subtitle", default="", help="Subtitulo de portada.")
    args = parser.parse_args()

    render_markdown(
        input_path=Path(args.input),
        output_path=Path(args.output),
        title=args.title,
        subtitle=args.subtitle,
    )
    print(f"PDF generado: {args.output}")


if __name__ == "__main__":
    main()
