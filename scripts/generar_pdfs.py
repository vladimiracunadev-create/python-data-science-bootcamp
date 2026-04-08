"""
Generador de PDFs para cada clase del bootcamp.

Convierte teoria.md de cada clase en un PDF profesional con formato.

Uso:
    python scripts/generar_pdfs.py               # genera todos los PDFs
    python scripts/generar_pdfs.py --clase 01    # solo clase 01
    python scripts/generar_pdfs.py --listar      # muestra clases disponibles

Requiere: fpdf2 (pip install fpdf2)
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
CLASS_DIR = BASE_DIR / "classes"
OUTPUT_DIR = BASE_DIR / "docs" / "pdfs"

# Paleta de colores del bootcamp
COLOR_BG         = (15, 23, 42)      # #0f172a  fondo oscuro
COLOR_PANEL      = (17, 24, 39)      # #111827  panel
COLOR_ACCENT     = (34, 197, 94)     # #22c55e  verde
COLOR_TEXT       = (203, 213, 225)   # #cbd5e1  texto principal
COLOR_MUTED      = (148, 163, 184)   # #94a3b8  texto secundario
COLOR_WHITE      = (248, 250, 252)   # #f8fafc  blanco
COLOR_HEADER_BG  = (31, 41, 55)      # #1f2937  header de tabla
COLOR_ROW_ALT    = (17, 24, 39)      # fila alternada

try:
    from fpdf import FPDF
except ImportError:
    print("ERROR: fpdf2 no está instalado. Ejecuta: pip install fpdf2")
    sys.exit(1)


def _parse_markdown_line(line: str) -> tuple[str, str]:
    """Devuelve (tipo, contenido) de una línea markdown."""
    stripped = line.strip()
    if stripped.startswith("# "):
        return "h1", stripped[2:]
    if stripped.startswith("## "):
        return "h2", stripped[3:]
    if stripped.startswith("### "):
        return "h3", stripped[4:]
    if stripped.startswith("| "):
        return "table_row", stripped
    if stripped.startswith("```"):
        return "code_fence", stripped
    if stripped.startswith("- ") or stripped.startswith("* "):
        return "bullet", stripped[2:]
    if re.match(r"^\d+\. ", stripped):
        return "numbered", re.sub(r"^\d+\. ", "", stripped)
    if stripped.startswith("> "):
        return "blockquote", stripped[2:]
    if stripped == "---":
        return "hr", ""
    if stripped == "":
        return "blank", ""
    return "text", stripped


def _strip_md_inline(text: str) -> str:
    """Elimina formateo inline de markdown (**bold**, `code`, etc.)."""
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", text)
    return text


class BootcampPDF(FPDF):
    """PDF con estilo visual del bootcamp."""

    def __init__(self, clase_titulo: str):
        super().__init__()
        self.clase_titulo = clase_titulo
        self.set_auto_page_break(auto=True, margin=20)
        self.set_margins(left=18, top=18, right=18)

    def header(self):
        self.set_fill_color(*COLOR_PANEL)
        self.rect(0, 0, 210, 14, "F")
        self.set_font("Helvetica", "B", 8)
        self.set_text_color(*COLOR_ACCENT)
        self.set_y(4)
        self.cell(0, 6, "BOOTCAMP PYTHON — DATA SCIENCE", align="L")
        self.set_text_color(*COLOR_MUTED)
        self.cell(0, 6, self.clase_titulo, align="R")
        self.ln(8)

    def footer(self):
        self.set_y(-14)
        self.set_fill_color(*COLOR_PANEL)
        self.rect(0, 283, 210, 14, "F")
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*COLOR_MUTED)
        self.cell(0, 6, f"Página {self.page_no()}", align="C")

    def add_cover(self, numero: str, titulo: str, subtitulo: str = ""):
        self.add_page()
        # Fondo oscuro
        self.set_fill_color(*COLOR_BG)
        self.rect(0, 0, 210, 297, "F")

        # Banda de color acento
        self.set_fill_color(*COLOR_ACCENT)
        self.rect(0, 80, 210, 4, "F")

        # Número de clase
        self.set_font("Helvetica", "B", 48)
        self.set_text_color(*COLOR_ACCENT)
        self.set_xy(18, 40)
        self.cell(0, 30, f"Clase {numero}", align="L")

        # Título
        self.set_font("Helvetica", "B", 22)
        self.set_text_color(*COLOR_WHITE)
        self.set_xy(18, 92)
        self.multi_cell(174, 10, titulo, align="L")

        # Subtítulo
        if subtitulo:
            self.set_font("Helvetica", "", 12)
            self.set_text_color(*COLOR_MUTED)
            self.set_xy(18, self.get_y() + 6)
            self.multi_cell(174, 7, subtitulo, align="L")

        # Footer de portada
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*COLOR_MUTED)
        self.set_xy(18, 260)
        self.cell(0, 6, "Material de capacitación — Uso docente", align="L")

    def add_h1(self, text: str):
        text = _strip_md_inline(text)
        self.ln(8)
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(*COLOR_WHITE)
        self.set_fill_color(*COLOR_PANEL)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 8, text, fill=False)
        self.set_draw_color(*COLOR_ACCENT)
        self.set_line_width(0.5)
        x = self.l_margin
        y = self.get_y()
        self.line(x, y, x + self.epw, y)
        self.ln(4)

    def add_h2(self, text: str):
        text = _strip_md_inline(text)
        self.ln(6)
        self.set_font("Helvetica", "B", 13)
        self.set_text_color(*COLOR_ACCENT)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 7, text)
        self.ln(2)

    def add_h3(self, text: str):
        text = _strip_md_inline(text)
        self.ln(4)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*COLOR_WHITE)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 6, text)
        self.ln(1)

    def add_text(self, text: str):
        text = _strip_md_inline(text)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*COLOR_TEXT)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 5.5, text)
        self.ln(1)

    def add_bullet(self, text: str):
        text = _strip_md_inline(text)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*COLOR_TEXT)
        self.set_x(self.l_margin + 4)
        self.cell(6, 5.5, "•", align="C")
        self.multi_cell(self.epw - 10, 5.5, text)

    def add_numbered(self, text: str, num: int):
        text = _strip_md_inline(text)
        self.set_font("Helvetica", "", 10)
        self.set_text_color(*COLOR_TEXT)
        self.set_x(self.l_margin + 4)
        self.set_text_color(*COLOR_ACCENT)
        self.cell(6, 5.5, f"{num}.", align="L")
        self.set_text_color(*COLOR_TEXT)
        self.multi_cell(self.epw - 10, 5.5, text)

    def add_blockquote(self, text: str):
        text = _strip_md_inline(text)
        self.set_fill_color(*COLOR_PANEL)
        self.set_draw_color(*COLOR_ACCENT)
        self.set_line_width(0.8)
        x = self.l_margin + 4
        y = self.get_y()
        self.set_x(x)
        self.set_font("Helvetica", "I", 10)
        self.set_text_color(*COLOR_MUTED)
        self.multi_cell(self.epw - 8, 5.5, text, fill=True)
        h = self.get_y() - y
        self.line(self.l_margin, y, self.l_margin, y + h)
        self.ln(2)

    def add_hr(self):
        self.ln(4)
        self.set_draw_color(*COLOR_PANEL)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), self.l_margin + self.epw, self.get_y())
        self.ln(4)

    def add_code_block(self, lines: list[str]):
        code = "\n".join(lines)
        self.ln(3)
        self.set_fill_color(2, 6, 23)
        self.set_draw_color(*COLOR_PANEL)
        self.set_line_width(0.3)
        self.set_font("Courier", "", 8)
        self.set_text_color(*COLOR_TEXT)
        self.set_x(self.l_margin)
        self.multi_cell(self.epw, 4.5, code, fill=True, border=1)
        self.ln(3)

    def add_table(self, rows: list[list[str]]):
        if not rows:
            return
        self.ln(3)
        n_cols = len(rows[0])
        col_w  = self.epw / n_cols
        row_h  = 6

        for row_i, row in enumerate(rows):
            if row_i == 0 or (row_i == 1 and all(set(c.strip()) <= set("-: ") for c in row)):
                # Header de tabla
                self.set_fill_color(*COLOR_HEADER_BG)
                self.set_text_color(*COLOR_ACCENT)
                self.set_font("Helvetica", "B", 8)
            else:
                # Fila alternada
                if row_i % 2 == 0:
                    self.set_fill_color(*COLOR_ROW_ALT)
                else:
                    self.set_fill_color(*COLOR_PANEL)
                self.set_text_color(*COLOR_TEXT)
                self.set_font("Helvetica", "", 8)

            # Saltar fila separadora de markdown (---|---|---)
            if all(set(c.strip()) <= set("-: ") for c in row):
                continue

            for cell in row:
                cell_text = _strip_md_inline(cell.strip())
                self.cell(col_w, row_h, cell_text[:45], border=1, fill=True)
            self.ln()

        self.ln(3)


def _parse_table_row(line: str) -> list[str]:
    line = line.strip().strip("|")
    return [c.strip() for c in line.split("|")]


def generate_pdf(class_dir: Path) -> Path:
    teoria_path = class_dir / "teoria.md"
    if not teoria_path.exists():
        raise FileNotFoundError(f"No existe teoria.md en {class_dir}")

    # Extraer número y título
    match = re.match(r"(\d+)-(.+)", class_dir.name)
    numero = match.group(1) if match else "??"
    nombre_dir = match.group(2).replace("-", " ").title() if match else class_dir.name

    content = teoria_path.read_text(encoding="utf-8")
    lines = content.splitlines()

    # Extraer título del H1
    h1_title = nombre_dir
    for line in lines:
        kind, val = _parse_markdown_line(line)
        if kind == "h1":
            h1_title = re.sub(r"Documento Teórico — Clase \d+: ", "", val)
            break

    pdf = BootcampPDF(clase_titulo=f"Clase {numero}")
    pdf.add_cover(numero, h1_title, "Documento teórico completo con ejemplos y tablas")

    pdf.add_page()
    pdf.set_fill_color(*COLOR_BG)
    pdf.rect(0, 0, 210, 297, "F")

    in_code = False
    code_lines: list[str] = []
    table_rows: list[list[str]] = []
    in_table = False
    numbered_counter = 0

    for line in lines:
        kind, val = _parse_markdown_line(line)

        # Manejo de bloques de código
        if kind == "code_fence":
            if not in_code:
                in_code = True
                code_lines = []
            else:
                in_code = False
                pdf.add_code_block(code_lines)
                code_lines = []
            continue

        if in_code:
            code_lines.append(line.rstrip())
            continue

        # Manejo de tablas
        if kind == "table_row":
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append(_parse_table_row(val))
            continue
        else:
            if in_table:
                pdf.add_table(table_rows)
                table_rows = []
                in_table = False

        # Renderizar
        if kind == "h1":
            pdf.add_h1(val)
        elif kind == "h2":
            pdf.add_h2(val)
        elif kind == "h3":
            pdf.add_h3(val)
        elif kind == "bullet":
            numbered_counter = 0
            pdf.add_bullet(val)
        elif kind == "numbered":
            numbered_counter += 1
            pdf.add_numbered(val, numbered_counter)
        elif kind == "blockquote":
            pdf.add_blockquote(val)
        elif kind == "hr":
            pdf.add_hr()
        elif kind == "text":
            numbered_counter = 0
            pdf.add_text(val)
        elif kind == "blank":
            numbered_counter = 0
            pdf.ln(2)

    # Cerrar tabla si quedó abierta
    if in_table:
        pdf.add_table(table_rows)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / f"clase-{numero}-{class_dir.name.split('-', 1)[1]}.pdf"
    pdf.output(str(output_path))
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Generador de PDFs del bootcamp")
    parser.add_argument("--clase", help="Número de clase (ej: 01, 09)")
    parser.add_argument("--listar", action="store_true", help="Listar clases disponibles")
    args = parser.parse_args()

    class_dirs = sorted([d for d in CLASS_DIR.iterdir() if d.is_dir()])

    if args.listar:
        print("Clases disponibles:")
        for d in class_dirs:
            tiene_teoria = "✅" if (d / "teoria.md").exists() else "❌"
            print(f"  {tiene_teoria} {d.name}")
        return

    if args.clase:
        matches = [d for d in class_dirs if d.name.startswith(args.clase)]
        if not matches:
            print(f"No se encontró la clase '{args.clase}'")
            sys.exit(1)
        class_dirs = matches

    print(f"Generando PDFs en: {OUTPUT_DIR}")
    errores = []
    for class_dir in class_dirs:
        if not (class_dir / "teoria.md").exists():
            print(f"  ⚠ Sin teoria.md: {class_dir.name}")
            continue
        try:
            output = generate_pdf(class_dir)
            print(f"  ✅ {output.name}")
        except Exception as e:
            print(f"  ❌ Error en {class_dir.name}: {e}")
            errores.append(class_dir.name)

    if errores:
        print(f"\n{len(errores)} errores. Revisar clases: {', '.join(errores)}")
    else:
        print(f"\n✅ Todos los PDFs generados en {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
