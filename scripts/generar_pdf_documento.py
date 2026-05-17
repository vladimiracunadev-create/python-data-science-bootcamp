"""Renderiza documentos Markdown del bootcamp a PDF con una plantilla uniforme.

Responsabilidades:
    1. Convertir Markdown simple a un PDF legible y visualmente consistente.
    2. Soportar títulos, listas, tablas, citas y bloques de código.
    3. Usar tipografías Unicode del sistema para no romper acentos en español.

Qué resuelve:
    Permite generar PDFs presentables para clases, entrevistas y material de
    estudio sin depender de exportes manuales desde otras herramientas.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

from fpdf import FPDF

COLOR_BG = (15, 23, 42)
COLOR_PANEL = (17, 24, 39)
COLOR_ACCENT = (34, 197, 94)
COLOR_TEXT = (203, 213, 225)
COLOR_MUTED = (148, 163, 184)
COLOR_WHITE = (248, 250, 252)
COLOR_HEADER_BG = (31, 41, 55)
COLOR_ROW_ALT = (21, 29, 44)
COLOR_CODE_BG = (2, 6, 23)

PRINT_BG = (255, 255, 255)
PRINT_PANEL = (245, 247, 250)
PRINT_ACCENT = (30, 64, 175)
PRINT_TEXT = (17, 24, 39)
PRINT_MUTED = (75, 85, 99)
PRINT_HEADER_BG = (229, 231, 235)
PRINT_ROW_ALT = (249, 250, 251)
PRINT_CODE_BG = (243, 244, 246)

FONT_DIR = Path(r"C:\Windows\Fonts")
FONT_FAMILY = "BootcampSans"
FONT_REGULAR = FONT_DIR / "arial.ttf"
FONT_BOLD = FONT_DIR / "arialbd.ttf"
FONT_ITALIC = FONT_DIR / "ariali.ttf"
FONT_MONO = "Courier"

ICON_MAP = {
    "🧭": "",
    "📝": "",
    "🤝": "",
    "🗺️": "",
    "🎯": "",
    "🛠️": "",
    "🔐": "",
    "📦": "",
    "📱": "",
    "🏗️": "",
    "🪟": "",
    "🧪": "",
    "🧠": "",
    "🖥️": "",
    "📚": "",
    "🎤": "",
    "💡": "",
    "⚙️": "",
    "🧩": "",
    "🧱": "",
    "📌": "",
    "🏁": "",
    "🚪": "",
    "❓": "",
    "⚠️": "",
    "🔗": "",
    "👩‍🏫": "",
    "🎬": "",
    "📍": "",
    "✅": "",
    "💻": "",
    "🧰": "",
    "📖": "",
    "🔍": "",
    "🌐": "",
    "💼": "",
    "🧾": "",
    "🏫": "",
    "🐍": "",
    "📊": "",
    "📐": "",
    "🎨": "",
    "🗓️": "",
    "🤖": "",
    "📏": "",
    "⏱️": "",
}

EMOJI_PATTERN = re.compile(r"[\U0001F300-\U0001FAFF\u2600-\u27BF\u2300-\u23FF]")


@dataclass
class Block:
    """Representa una pieza de contenido ya clasificada para el render PDF."""

    kind: str
    value: str


def _strip_md_inline(text: str) -> str:
    """Limpia formato inline para dejar el texto visible listo para PDF."""
    clean = text
    clean = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", clean)
    clean = re.sub(r"`(.+?)`", r"\1", clean)
    clean = re.sub(r"\*\*(.+?)\*\*", r"\1", clean)
    clean = re.sub(r"\*(.+?)\*", r"\1", clean)
    for icon, replacement in ICON_MAP.items():
        clean = clean.replace(icon, replacement)
    clean = EMOJI_PATTERN.sub("", clean)
    clean = clean.replace("\u200d", "")
    clean = clean.replace("\ufe0f", "")
    return clean.strip()


def _parse_line(line: str) -> tuple[str, str]:
    """Clasifica una línea markdown simple en una categoría de render."""
    stripped = line.strip()
    if stripped.startswith("# "):
        return "h1", stripped[2:]
    if stripped.startswith("## "):
        return "h2", stripped[3:]
    if stripped.startswith("### "):
        return "h3", stripped[4:]
    if stripped.startswith("```"):
        return "code_fence", stripped
    if stripped.startswith("|"):
        return "table_row", stripped
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


def _parse_table_row(line: str) -> list[str]:
    """Divide una fila markdown en celdas limpias."""
    line = line.strip().strip("|")
    return [_strip_md_inline(cell.strip()) for cell in line.split("|")]


def parse_markdown(markdown_text: str) -> list[Block]:
    """Convierte el markdown en bloques lineales fáciles de renderizar."""
    blocks: list[Block] = []
    in_code = False
    code_lines: list[str] = []
    table_rows: list[list[str]] = []

    for line in markdown_text.splitlines():
        kind, value = _parse_line(line)

        if kind == "code_fence":
            if not in_code:
                in_code = True
                code_lines = []
            else:
                blocks.append(Block("code", "\n".join(code_lines).rstrip()))
                code_lines = []
                in_code = False
            continue

        if in_code:
            code_lines.append(line.rstrip())
            continue

        if kind == "table_row":
            table_rows.append(_parse_table_row(value))
            continue

        if table_rows:
            blocks.append(Block("table", json.dumps(table_rows, ensure_ascii=False)))
            table_rows = []

        if kind == "blank":
            blocks.append(Block("blank", ""))
        else:
            blocks.append(Block(kind, value))

    if table_rows:
        blocks.append(Block("table", json.dumps(table_rows, ensure_ascii=False)))
    if code_lines:
        blocks.append(Block("code", "\n".join(code_lines).rstrip()))

    return blocks


class DocumentPDF(FPDF):
    """Plantilla PDF visual del bootcamp con soporte Unicode."""

    def __init__(self, header_title: str):
        super().__init__()
        self.header_title = _strip_md_inline(header_title)
        self.set_auto_page_break(auto=True, margin=18)
        self.set_margins(left=18, top=18, right=18)
        self._using_unicode_fonts = False
        self._register_fonts()

    def _register_fonts(self) -> None:
        """Configura las fuentes disponibles para acentos y texto largo."""
        if FONT_REGULAR.exists() and FONT_BOLD.exists() and FONT_ITALIC.exists():
            self.add_font(FONT_FAMILY, "", str(FONT_REGULAR))
            self.add_font(FONT_FAMILY, "B", str(FONT_BOLD))
            self.add_font(FONT_FAMILY, "I", str(FONT_ITALIC))
            self._using_unicode_fonts = True

    @property
    def family(self) -> str:
        """Devuelve la familia tipográfica activa."""
        return FONT_FAMILY if self._using_unicode_fonts else "Helvetica"

    def header(self) -> None:
        """Dibuja fondo y cabecera en cada página del PDF.

        Qué resuelve:
            Cuando FPDF agrega páginas automáticas por salto de contenido,
            esta rutina vuelve a pintar el fondo completo. Así evitamos que
            solo la portada o la primera página del cuerpo tengan identidad
            visual y el resto quede en blanco.
        """
        self.set_fill_color(*COLOR_BG)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*COLOR_PANEL)
        self.rect(0, 0, 210, 14, "F")
        self.set_font(self.family, "B", 8)
        self.set_text_color(*COLOR_ACCENT)
        self.set_y(4)
        self.cell(0, 6, "BOOTCAMP PYTHON - DATA SCIENCE", align="L")
        self.set_text_color(*COLOR_MUTED)
        self.cell(0, 6, self.header_title, align="R")
        self.ln(8)

    def footer(self) -> None:
        """Dibuja pie de página con paginación."""
        self.set_y(-14)
        self.set_fill_color(*COLOR_PANEL)
        self.rect(0, 283, 210, 14, "F")
        self.set_font(self.family, "", 8)
        self.set_text_color(*COLOR_MUTED)
        self.cell(0, 6, f"Página {self.page_no()}", align="C")

    def cover(self, title: str, subtitle: str) -> None:
        """Crea una portada simple con identidad visual consistente."""
        self.add_page()
        self.set_fill_color(*COLOR_BG)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*COLOR_ACCENT)
        self.rect(0, 80, 210, 4, "F")

        self.set_font(self.family, "B", 24)
        self.set_text_color(*COLOR_WHITE)
        self.set_xy(18, 92)
        self.multi_cell(174, 10, _strip_md_inline(title))

        if subtitle:
            self.set_font(self.family, "", 12)
            self.set_text_color(*COLOR_MUTED)
            self.set_x(18)
            self.multi_cell(174, 7, _strip_md_inline(subtitle))

    def start_body(self) -> None:
        """Inicia el cuerpo del PDF.

        Qué resuelve:
            La plantilla ya pinta el fondo desde `header()`, así que aquí solo
            abrimos la primera página del cuerpo para mantener consistencia con
            las páginas agregadas automáticamente después.
        """
        self.add_page()

    def h1(self, text: str) -> None:
        """Renderiza un título principal de sección."""
        self.ln(8)
        self.set_font(self.family, "B", 16)
        self.set_text_color(*COLOR_WHITE)
        self.multi_cell(self.epw, 8, _strip_md_inline(text))
        y = self.get_y()
        self.set_draw_color(*COLOR_ACCENT)
        self.set_line_width(0.5)
        self.line(self.l_margin, y, self.l_margin + self.epw, y)
        self.ln(4)

    def h2(self, text: str) -> None:
        """Renderiza un subtítulo con color de acento."""
        self.ln(6)
        self.set_font(self.family, "B", 13)
        self.set_text_color(*COLOR_ACCENT)
        self.multi_cell(self.epw, 7, _strip_md_inline(text))
        self.ln(2)

    def h3(self, text: str) -> None:
        """Renderiza un subtítulo menor para bloques internos."""
        self.ln(4)
        self.set_font(self.family, "B", 11)
        self.set_text_color(*COLOR_WHITE)
        self.multi_cell(self.epw, 6, _strip_md_inline(text))
        self.ln(1)

    def text(self, text: str) -> None:
        """Renderiza un párrafo corrido."""
        self.set_font(self.family, "", 10)
        self.set_text_color(*COLOR_TEXT)
        self.multi_cell(self.epw, 5.5, _strip_md_inline(text))
        self.ln(1)

    def bullet(self, text: str) -> None:
        """Renderiza un bullet simple."""
        self.set_font(self.family, "", 10)
        self.set_text_color(*COLOR_TEXT)
        self.set_x(self.l_margin + 4)
        self.cell(6, 5.5, "-", align="C")
        self.multi_cell(self.epw - 10, 5.5, _strip_md_inline(text))

    def numbered(self, text: str, number: int) -> None:
        """Renderiza listas numeradas manteniendo jerarquía visual."""
        self.set_font(self.family, "", 10)
        self.set_x(self.l_margin + 4)
        self.set_text_color(*COLOR_ACCENT)
        self.cell(8, 5.5, f"{number}.", align="L")
        self.set_text_color(*COLOR_TEXT)
        self.multi_cell(self.epw - 12, 5.5, _strip_md_inline(text))

    def quote(self, text: str) -> None:
        """Resalta una cita o nota importante."""
        clean = _strip_md_inline(text)
        self.set_fill_color(*COLOR_PANEL)
        self.set_draw_color(*COLOR_ACCENT)
        self.set_line_width(0.8)
        y = self.get_y()
        self.set_x(self.l_margin + 4)
        self.set_font(self.family, "I", 10)
        self.set_text_color(*COLOR_MUTED)
        self.multi_cell(self.epw - 8, 5.5, clean, fill=True)
        self.line(self.l_margin, y, self.l_margin, self.get_y())
        self.ln(2)

    def hr(self) -> None:
        """Dibuja una separación horizontal suave."""
        self.ln(4)
        self.set_draw_color(*COLOR_PANEL)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), self.l_margin + self.epw, self.get_y())
        self.ln(4)

    def code(self, code_text: str) -> None:
        """Renderiza un bloque de código con fuente monoespaciada."""
        self.ln(3)
        self.set_fill_color(*COLOR_CODE_BG)
        self.set_draw_color(*COLOR_PANEL)
        self.set_line_width(0.3)
        self.set_font(self.family, "", 8)
        self.set_text_color(*COLOR_TEXT)
        self.multi_cell(self.epw, 4.5, _strip_md_inline(code_text), fill=True, border=1)
        self.ln(3)

    def table(self, rows: list[list[str]]) -> None:
        """Renderiza tablas markdown simples con cabecera y bandas alternas."""
        if not rows:
            return

        visible_rows = [row for row in rows if not all(set(cell.strip()) <= set("-: ") for cell in row)]
        if not visible_rows:
            return

        col_count = max(len(row) for row in visible_rows)
        col_width = self.epw / col_count
        row_height = 6
        self.ln(3)

        for row_index, row in enumerate(visible_rows):
            values = row + [""] * (col_count - len(row))
            if row_index == 0:
                self.set_fill_color(*COLOR_HEADER_BG)
                self.set_text_color(*COLOR_ACCENT)
                self.set_font(self.family, "B", 8)
            else:
                self.set_fill_color(*(COLOR_ROW_ALT if row_index % 2 == 0 else COLOR_PANEL))
                self.set_text_color(*COLOR_TEXT)
                self.set_font(self.family, "", 8)

            for cell in values:
                text = _strip_md_inline(cell)
                self.cell(col_width, row_height, text[:42], border=1, fill=True)
            self.ln()

        self.ln(3)


class PrintDocumentPDF(DocumentPDF):
    """Plantilla PDF clara y sobria para documentos de entrevista/imprenta."""

    def header(self) -> None:
        self.set_fill_color(*PRINT_BG)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*PRINT_HEADER_BG)
        self.rect(0, 0, 210, 12, "F")
        self.set_font(self.family, "B", 8)
        self.set_text_color(*PRINT_ACCENT)
        self.set_y(3.5)
        self.cell(0, 5, "BOOTCAMP PYTHON - DOSSIER", align="L")
        self.set_text_color(*PRINT_MUTED)
        self.cell(0, 5, self.header_title, align="R")
        self.ln(9)

    def footer(self) -> None:
        self.set_y(-12)
        self.set_draw_color(*PRINT_HEADER_BG)
        self.set_line_width(0.2)
        self.line(self.l_margin, self.get_y(), self.l_margin + self.epw, self.get_y())
        self.ln(2)
        self.set_font(self.family, "", 8)
        self.set_text_color(*PRINT_MUTED)
        self.cell(0, 4, f"Página {self.page_no()}", align="C")

    def cover(self, title: str, subtitle: str) -> None:
        self.add_page()
        self.set_fill_color(*PRINT_BG)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*PRINT_ACCENT)
        self.rect(18, 42, 174, 2.4, "F")
        self.set_fill_color(*PRINT_PANEL)
        self.rect(18, 54, 174, 36, "F")

        self.set_font(self.family, "B", 22)
        self.set_text_color(*PRINT_TEXT)
        self.set_xy(24, 60)
        self.multi_cell(162, 9, _strip_md_inline(title))

        if subtitle:
            self.set_font(self.family, "", 11)
            self.set_text_color(*PRINT_MUTED)
            self.set_x(24)
            self.multi_cell(162, 6.5, _strip_md_inline(subtitle))

    def h1(self, text: str) -> None:
        self.ln(7)
        self.set_font(self.family, "B", 16)
        self.set_text_color(*PRINT_TEXT)
        self.multi_cell(self.epw, 8, _strip_md_inline(text))
        y = self.get_y()
        self.set_draw_color(*PRINT_ACCENT)
        self.set_line_width(0.45)
        self.line(self.l_margin, y, self.l_margin + 48, y)
        self.ln(3)

    def h2(self, text: str) -> None:
        self.ln(5)
        self.set_font(self.family, "B", 12)
        self.set_text_color(*PRINT_ACCENT)
        self.multi_cell(self.epw, 6.5, _strip_md_inline(text))
        self.ln(1.5)

    def h3(self, text: str) -> None:
        self.ln(3)
        self.set_font(self.family, "B", 10.5)
        self.set_text_color(*PRINT_TEXT)
        self.multi_cell(self.epw, 5.5, _strip_md_inline(text))
        self.ln(0.8)

    def text(self, text: str) -> None:
        self.set_font(self.family, "", 10)
        self.set_text_color(*PRINT_TEXT)
        self.multi_cell(self.epw, 5.5, _strip_md_inline(text))
        self.ln(0.8)

    def bullet(self, text: str) -> None:
        self.set_font(self.family, "", 10)
        self.set_text_color(*PRINT_TEXT)
        self.set_x(self.l_margin + 3)
        self.cell(5.5, 5.5, "-", align="C")
        self.multi_cell(self.epw - 9, 5.5, _strip_md_inline(text))

    def numbered(self, text: str, number: int) -> None:
        self.set_font(self.family, "", 10)
        self.set_x(self.l_margin + 3)
        self.set_text_color(*PRINT_ACCENT)
        self.cell(8, 5.5, f"{number}.", align="L")
        self.set_text_color(*PRINT_TEXT)
        self.multi_cell(self.epw - 12, 5.5, _strip_md_inline(text))

    def quote(self, text: str) -> None:
        clean = _strip_md_inline(text)
        self.set_fill_color(*PRINT_PANEL)
        self.set_draw_color(*PRINT_ACCENT)
        self.set_line_width(0.7)
        y = self.get_y()
        self.set_x(self.l_margin + 4)
        self.set_font(self.family, "I", 10)
        self.set_text_color(*PRINT_MUTED)
        self.multi_cell(self.epw - 8, 5.5, clean, fill=True)
        self.line(self.l_margin, y, self.l_margin, self.get_y())
        self.ln(1.5)

    def hr(self) -> None:
        self.ln(3)
        self.set_draw_color(*PRINT_HEADER_BG)
        self.set_line_width(0.25)
        self.line(self.l_margin, self.get_y(), self.l_margin + self.epw, self.get_y())
        self.ln(3)

    def code(self, code_text: str) -> None:
        self.ln(2)
        self.set_fill_color(*PRINT_CODE_BG)
        self.set_draw_color(*PRINT_HEADER_BG)
        self.set_line_width(0.25)
        self.set_font(self.family, "", 8.5)
        self.set_text_color(*PRINT_TEXT)
        self.multi_cell(self.epw, 4.5, _strip_md_inline(code_text), fill=True, border=1)
        self.ln(2)

    def table(self, rows: list[list[str]]) -> None:
        if not rows:
            return

        visible_rows = [row for row in rows if not all(set(cell.strip()) <= set("-: ") for cell in row)]
        if not visible_rows:
            return

        col_count = max(len(row) for row in visible_rows)
        col_width = self.epw / col_count
        row_height = 6
        self.ln(2)

        for row_index, row in enumerate(visible_rows):
            values = row + [""] * (col_count - len(row))
            if row_index == 0:
                self.set_fill_color(*PRINT_HEADER_BG)
                self.set_text_color(*PRINT_TEXT)
                self.set_font(self.family, "B", 8)
            else:
                self.set_fill_color(*(PRINT_ROW_ALT if row_index % 2 == 0 else PRINT_BG))
                self.set_text_color(*PRINT_TEXT)
                self.set_font(self.family, "", 8)

            for cell in values:
                text = _strip_md_inline(cell)
                self.cell(col_width, row_height, text[:42], border=1, fill=True)
            self.ln()

        self.ln(2)


def extract_title(markdown_text: str, fallback: str) -> str:
    """Obtiene el primer H1 del markdown para reutilizarlo como cabecera."""
    for block in parse_markdown(markdown_text):
        if block.kind == "h1":
            return _strip_md_inline(block.value)
    return _strip_md_inline(fallback)


def render_markdown_text(
    markdown_text: str,
    output_path: Path,
    title: str,
    subtitle: str = "",
    style: str = "dark",
) -> None:
    """Convierte un string Markdown a PDF usando la plantilla visual del repo."""
    pdf_class = PrintDocumentPDF if style == "print" else DocumentPDF
    pdf = pdf_class(header_title=extract_title(markdown_text, title))
    pdf.cover(title=title, subtitle=subtitle)
    pdf.start_body()

    numbered_counter = 0
    for block in parse_markdown(markdown_text):
        if block.kind == "h1":
            numbered_counter = 0
            pdf.h1(block.value)
        elif block.kind == "h2":
            numbered_counter = 0
            pdf.h2(block.value)
        elif block.kind == "h3":
            numbered_counter = 0
            pdf.h3(block.value)
        elif block.kind == "text":
            numbered_counter = 0
            pdf.text(block.value)
        elif block.kind == "bullet":
            numbered_counter = 0
            pdf.bullet(block.value)
        elif block.kind == "numbered":
            numbered_counter += 1
            pdf.numbered(block.value, numbered_counter)
        elif block.kind == "blockquote":
            numbered_counter = 0
            pdf.quote(block.value)
        elif block.kind == "hr":
            numbered_counter = 0
            pdf.hr()
        elif block.kind == "code":
            numbered_counter = 0
            pdf.code(block.value)
        elif block.kind == "table":
            numbered_counter = 0
            pdf.table(json.loads(block.value))
        elif block.kind == "blank":
            numbered_counter = 0
            pdf.ln(2)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(output_path))


def render_markdown(
    input_path: Path,
    output_path: Path,
    title: str,
    subtitle: str = "",
    style: str = "dark",
) -> None:
    """Lee un Markdown desde disco y lo renderiza a PDF."""
    render_markdown_text(
        markdown_text=input_path.read_text(encoding="utf-8"),
        output_path=output_path,
        title=title,
        subtitle=subtitle,
        style=style,
    )


def main() -> None:
    """Permite usar el renderer desde la línea de comandos."""
    parser = argparse.ArgumentParser(description="Genera un PDF a partir de un archivo Markdown.")
    parser.add_argument("--input", required=True, help="Ruta del archivo Markdown de entrada.")
    parser.add_argument("--output", required=True, help="Ruta del PDF de salida.")
    parser.add_argument("--title", required=True, help="Título de portada.")
    parser.add_argument("--subtitle", default="", help="Subtítulo de portada.")
    parser.add_argument("--style", default="dark", choices=["dark", "print"], help="Estilo visual del PDF.")
    args = parser.parse_args()

    render_markdown(
        input_path=Path(args.input),
        output_path=Path(args.output),
        title=args.title,
        subtitle=args.subtitle,
        style=args.style,
    )
    print(f"PDF generado: {args.output}")


if __name__ == "__main__":
    main()
