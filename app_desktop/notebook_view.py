"""Visor de notebooks ``.ipynb`` en widgets Qt nativos.

Qué resuelve:
    Renderiza celdas markdown (HTML vía ``app.class_html``) y celdas de código
    (con resaltado de sintaxis Pygments + outputs) en un ``QScrollArea``
    vertical. Cero WebView. No ejecuta código — solo visualiza.

    Desde v3.11.0 las celdas siguen el tema activo (claro/oscuro), el markdown
    usa el mismo renderizador que GitHub Pages, el código va resaltado y todo
    vive dentro de una columna de lectura acotada en vez de estirarse a lo
    ancho de la ventana.
"""

from __future__ import annotations

import base64
import logging
import re
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QSizePolicy,
    QTextBrowser,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

try:
    from app.class_html import QT_THEMES, markdown_available, qt_page
except Exception as exc:  # pragma: no cover - entorno sin markdown
    logging.getLogger(__name__).warning("class_html no disponible: %s", exc)
    QT_THEMES = {  # type: ignore[assignment]
        "light": {"bg": "#ffffff", "ink": "#1f2328", "ink_soft": "#57606a", "line": "#d0d7de"},
        "dark": {"bg": "#0d1117", "ink": "#e6edf3", "ink_soft": "#9198a1", "line": "#30363d"},
    }
    markdown_available = lambda: False  # noqa: E731
    qt_page = None  # type: ignore[assignment]

try:  # Resaltado de las celdas de código.
    from pygments import highlight as _pyg_highlight
    from pygments.formatters import HtmlFormatter as _PygHtmlFormatter
    from pygments.lexers import get_lexer_by_name as _pyg_lexer
except Exception:  # pragma: no cover - entorno sin pygments
    _pyg_highlight = None  # type: ignore[assignment]

log = logging.getLogger(__name__)

#: Mismo ancho de columna que la vista de README.
READING_WIDTH = 940

_CODE_FONT: QFont | None = None

_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")


def _code_font() -> QFont:
    """Construye la fuente monoespaciada lazy: requiere QApplication viva."""
    global _CODE_FONT
    if _CODE_FONT is None:
        font = QFont("Cascadia Code", 10)
        if not font.exactMatch():
            font = QFont("Consolas", 10)
        font.setStyleHint(QFont.StyleHint.Monospace)
        _CODE_FONT = font
    return _CODE_FONT


# Paleta de las celdas — fija y oscura para el código (como un notebook real),
# variable para el chrome (títulos, separadores) según el tema de la app.
_CELL_COLORS = {
    "code_bg": "#0d1117",
    "code_ink": "#e6edf3",
    "code_border": "#30363d",
    "out_bg_light": "#f6f8fa",
    "out_ink_light": "#1f2328",
    "out_bg_dark": "#161b22",
    "out_ink_dark": "#c9d1d9",
    "err_bg": "#2d1418",
    "err_ink": "#ffa198",
    "err_border": "#f85149",
}


def _style(bg: str, ink: str, border: str) -> str:
    return (
        f"background-color: {bg}; color: {ink}; border: 1px solid {border};"
        " border-radius: 6px; padding: 10px;"
    )


class _CellSeparator(QFrame):
    def __init__(self, color: str) -> None:
        super().__init__()
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFixedHeight(1)
        self.setStyleSheet(f"background-color: {color}; border: none;")


class NotebookView(QWidget):
    """Widget que renderiza un notebook completo dentro de un QScrollArea."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._theme = "light"
        self._scale = 1.0
        self._notebook: dict[str, Any] | None = None
        self._empty_message: str | None = "Seleccioná una clase."

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Barra de contexto: título de la clase + nº de celdas.
        self._bar = QWidget()
        bar_layout = QHBoxLayout(self._bar)
        bar_layout.setContentsMargins(18, 10, 18, 10)
        bar_layout.setSpacing(12)
        self._title_label = QLabel("—")
        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)
        self._title_label.setFont(title_font)
        self._title_label.setWordWrap(False)
        self._meta_label = QLabel("")
        bar_layout.addWidget(self._title_label, 1)
        bar_layout.addWidget(self._meta_label, 0)
        root.addWidget(self._bar)

        self._scroll = QScrollArea(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setFrameShape(QScrollArea.Shape.NoFrame)
        self._scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        root.addWidget(self._scroll, 1)

        # Columna de lectura centrada.
        outer = QWidget()
        outer_layout = QHBoxLayout(outer)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.addStretch(1)
        self._container = QWidget()
        self._container.setMaximumWidth(READING_WIDTH)
        # Stretch alto + maximumWidth = columna centrada de ancho acotado.
        outer_layout.addWidget(self._container, 20)
        outer_layout.addStretch(1)

        self._cells_layout = QVBoxLayout(self._container)
        self._cells_layout.setContentsMargins(16, 18, 16, 40)
        self._cells_layout.setSpacing(14)
        self._cells_layout.addStretch(1)
        self._scroll.setWidget(outer)

        self._apply_chrome()

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------
    def set_theme(self, theme: str) -> None:
        if theme == self._theme:
            return
        self._theme = theme
        self._apply_chrome()
        self._rerender()

    def set_scale(self, scale: float) -> None:
        if abs(scale - self._scale) < 0.001:
            return
        self._scale = scale
        self._rerender()

    def load_notebook(self, notebook: dict[str, Any]) -> None:
        """Renderiza un notebook devuelto por ``app.notebook_loader``."""
        self._notebook = notebook
        self._empty_message = None
        self._rerender()

    def load_empty(self, message: str) -> None:
        """Muestra un mensaje (clase sin notebook, error, etc.)."""
        self._notebook = None
        self._empty_message = message
        self._rerender()

    # ------------------------------------------------------------------
    # Interno
    # ------------------------------------------------------------------
    def _colors(self) -> dict[str, str]:
        return QT_THEMES.get(self._theme, QT_THEMES["light"])

    def _apply_chrome(self) -> None:
        c = self._colors()
        self._bar.setStyleSheet(
            f"background-color: {c['bg']}; border-bottom: 1px solid {c['line']};"
        )
        self._title_label.setStyleSheet(f"color: {c['ink']}; border: none;")
        self._meta_label.setStyleSheet(f"color: {c['ink_soft']}; border: none;")
        self._scroll.setStyleSheet(f"background-color: {c['bg']};")
        self._container.setStyleSheet(f"background-color: {c['bg']};")

    def _clear_cells(self) -> None:
        while self._cells_layout.count() > 0:
            item = self._cells_layout.takeAt(0)
            w = item.widget()
            if w is not None:
                w.setParent(None)
                w.deleteLater()
        self._cells_layout.addStretch(1)

    def _rerender(self) -> None:
        self._clear_cells()
        c = self._colors()

        if self._notebook is None:
            self._title_label.setText("—")
            self._meta_label.setText("")
            label = QLabel(self._empty_message or "")
            label.setWordWrap(True)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet(
                f"color: {c['ink_soft']}; padding: 60px 20px; font-size: 12pt; border: none;"
            )
            self._cells_layout.insertWidget(0, label)
            return

        title = self._notebook.get("title", "")
        cells = self._notebook.get("cells", []) or []
        self._title_label.setText(title)
        self._meta_label.setText(f"{len(cells)} celdas · solo lectura")

        insert_at = 0
        for i, cell in enumerate(cells):
            ctype = cell.get("type", "raw")
            source = cell.get("source", "")
            if ctype == "markdown":
                widget = self._build_markdown_cell(source)
            elif ctype == "code":
                widget = self._build_code_cell(
                    source,
                    outputs=cell.get("outputs", []),
                    execution_count=cell.get("execution_count"),
                )
            else:
                widget = self._build_raw_cell(source)
            self._cells_layout.insertWidget(insert_at, widget)
            insert_at += 1
            if i < len(cells) - 1:
                self._cells_layout.insertWidget(insert_at, _CellSeparator(c["line"]))
                insert_at += 1

    # ------------------------------------------------------------------
    def _sized_browser(self, html_doc: str) -> QTextBrowser:
        browser = QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.setFrameShape(QTextBrowser.Shape.NoFrame)
        browser.setStyleSheet("background: transparent; border: none;")
        browser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        browser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        browser.document().setDocumentMargin(6)
        browser.setHtml(html_doc)
        browser.document().setTextWidth(READING_WIDTH - 44)
        doc_height = int(browser.document().size().height()) + 16
        browser.setFixedHeight(max(32, doc_height))
        browser.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return browser

    def _build_markdown_cell(self, source: str) -> QWidget:
        if markdown_available() and qt_page is not None:
            try:
                return self._sized_browser(
                    qt_page(source or "", theme=self._theme, scale=self._scale)
                )
            except Exception as exc:  # pragma: no cover - defensivo
                log.warning("Fallo el render de una celda markdown: %s", exc)
        browser = QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.setFrameShape(QTextBrowser.Shape.NoFrame)
        browser.setMarkdown(source or "")
        browser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        browser.document().setTextWidth(READING_WIDTH - 44)
        browser.setFixedHeight(max(32, int(browser.document().size().height()) + 16))
        browser.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return browser

    def _highlight_code(self, source: str) -> str | None:
        """Devuelve el código como HTML resaltado, o ``None`` sin Pygments."""
        if _pyg_highlight is None:
            return None
        try:
            lexer = _pyg_lexer("python", stripnl=False)
            formatter = _PygHtmlFormatter(
                noclasses=True, style="github-dark", nowrap=True
            )
            body = _pyg_highlight(source or "", lexer, formatter)
        except Exception as exc:  # pragma: no cover - defensivo
            log.debug("Pygments falló, uso texto plano: %s", exc)
            return None
        font_size = 10 * self._scale
        return (
            "<html><body style='margin:0'>"
            f"<pre style=\"font-family:'Cascadia Code','JetBrains Mono',Consolas,monospace;"
            f"font-size:{font_size:.1f}pt;color:{_CELL_COLORS['code_ink']};margin:0;\">"
            f"{body}</pre></body></html>"
        )

    def _build_code_cell(
        self,
        source: str,
        outputs: list[dict[str, Any]] | None,
        execution_count: int | None,
    ) -> QWidget:
        wrapper = QWidget()
        wrapper.setStyleSheet("background: transparent;")
        layout = QVBoxLayout(wrapper)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        row = QHBoxLayout()
        row.setSpacing(8)
        exec_label = QLabel(f"[{execution_count}]:" if execution_count else "[ ]:")
        exec_label.setStyleSheet(
            "color: #1f6feb; font-family: 'Cascadia Code', Consolas, monospace;"
            " border: none; background: transparent;"
        )
        exec_label.setFixedWidth(42)
        exec_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        row.addWidget(exec_label)

        n_lines = max(1, (source or "").count("\n") + 1)
        line_h = int(18 * self._scale)
        highlighted = self._highlight_code(source)
        if highlighted is not None:
            editor: QWidget = QTextBrowser()
            editor.setFrameShape(QTextBrowser.Shape.NoFrame)
            editor.setStyleSheet(
                _style(
                    _CELL_COLORS["code_bg"],
                    _CELL_COLORS["code_ink"],
                    _CELL_COLORS["code_border"],
                )
            )
            editor.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            editor.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            editor.setHtml(highlighted)
        else:
            editor = QTextEdit()
            editor.setReadOnly(True)
            editor.setFont(_code_font())
            editor.setStyleSheet(
                _style(
                    _CELL_COLORS["code_bg"],
                    _CELL_COLORS["code_ink"],
                    _CELL_COLORS["code_border"],
                )
            )
            editor.setPlainText(source or "")
            editor.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
            editor.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        editor.setFixedHeight(min(700, n_lines * line_h + 30))
        row.addWidget(editor, 1)
        layout.addLayout(row)

        if outputs:
            for out in outputs:
                out_widget = self._build_output(out)
                if out_widget is not None:
                    indent = QHBoxLayout()
                    indent.setContentsMargins(50, 0, 0, 0)
                    indent.addWidget(out_widget, 1)
                    layout.addLayout(indent)

        return wrapper

    def _build_output(self, out: dict[str, Any]) -> QWidget | None:
        otype = out.get("output_type", "")
        if otype == "stream":
            return self._make_pre(_join(out.get("text", "")), kind="out")
        if otype in ("execute_result", "display_data"):
            data = out.get("data", {}) or {}
            if "image/png" in data:
                return self._make_image(data["image/png"])
            if "text/plain" in data:
                return self._make_pre(_join(data["text/plain"]), kind="out")
            return None
        if otype == "error":
            traceback = out.get("traceback") or []
            text = "\n".join(traceback) if isinstance(traceback, list) else str(traceback)
            return self._make_pre(_ANSI_RE.sub("", text), kind="err")
        return None

    def _make_pre(self, text: str, kind: str) -> QWidget:
        if kind == "err":
            bg, ink, border = (
                _CELL_COLORS["err_bg"],
                _CELL_COLORS["err_ink"],
                _CELL_COLORS["err_border"],
            )
        elif self._theme == "dark":
            bg, ink, border = (
                _CELL_COLORS["out_bg_dark"],
                _CELL_COLORS["out_ink_dark"],
                self._colors()["line"],
            )
        else:
            bg, ink, border = (
                _CELL_COLORS["out_bg_light"],
                _CELL_COLORS["out_ink_light"],
                self._colors()["line"],
            )
        edit = QTextEdit()
        edit.setReadOnly(True)
        edit.setFont(_code_font())
        edit.setFrameShape(QTextEdit.Shape.NoFrame)
        edit.setStyleSheet(_style(bg, ink, border))
        edit.setPlainText(text or "")
        edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        n_lines = max(1, (text or "").count("\n") + 1)
        edit.setFixedHeight(min(420, n_lines * int(16 * self._scale) + 26))
        return edit

    def _make_image(self, b64_data: str) -> QWidget:
        label = QLabel()
        try:
            raw = base64.b64decode(b64_data)
            pix = QPixmap()
            pix.loadFromData(raw)
            if not pix.isNull():
                max_w = READING_WIDTH - 110
                if pix.width() > max_w:
                    pix = pix.scaledToWidth(
                        max_w, Qt.TransformationMode.SmoothTransformation
                    )
                label.setPixmap(pix)
                label.setStyleSheet(
                    "background-color: #ffffff; padding: 10px; border-radius: 6px;"
                    f" border: 1px solid {self._colors()['line']};"
                )
                return label
        except Exception as exc:
            log.warning("No se pudo decodificar imagen de output: %s", exc)
        label.setText("[imagen no decodificable]")
        label.setStyleSheet(
            _style(
                _CELL_COLORS["out_bg_dark"], _CELL_COLORS["out_ink_dark"], self._colors()["line"]
            )
        )
        return label

    def _build_raw_cell(self, source: str) -> QWidget:
        return self._make_pre(source, kind="out")


def _join(value: Any) -> str:
    """nbformat entrega texto como lista de líneas o como string."""
    if isinstance(value, list):
        return "".join(value)
    return str(value or "")


__all__ = ["NotebookView", "READING_WIDTH"]
