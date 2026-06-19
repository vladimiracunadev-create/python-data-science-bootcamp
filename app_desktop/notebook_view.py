"""Visor de notebooks ``.ipynb`` en widgets Qt nativos.

Qué resuelve:
    Renderiza celdas markdown (QTextBrowser) y code (QTextEdit con fondo
    oscuro fijo + outputs) en un QScrollArea vertical. Cero WebView.
    No ejecuta código — solo visualiza.
"""

from __future__ import annotations

import base64
import logging
from typing import Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTextBrowser,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

log = logging.getLogger(__name__)

_CODE_FONT: QFont | None = None


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

_CODE_STYLE = (
    "background-color: #1a1a1a; color: #e6edf3; border: 1px solid #30363d;"
    " border-radius: 6px; padding: 10px;"
)
_OUTPUT_STYLE = (
    "background-color: #0d1117; color: #c9d1d9; border: 1px solid #30363d;"
    " border-radius: 6px; padding: 8px;"
)
_ERROR_STYLE = (
    "background-color: #2d1418; color: #ffa198; border: 1px solid #f85149;"
    " border-radius: 6px; padding: 8px;"
)


class _CellSeparator(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)


class NotebookView(QWidget):
    """Widget que renderiza un notebook completo dentro de un QScrollArea."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(6)

        # Header: título + n celdas + botón "Abrir en Jupyter" (placeholder).
        header = QHBoxLayout()
        self._title_label = QLabel("—")
        title_font = QFont()
        title_font.setPointSize(13)
        title_font.setBold(True)
        self._title_label.setFont(title_font)
        self._meta_label = QLabel("")
        self._meta_label.setStyleSheet("color: #57606a;")
        self._open_jupyter_btn = QPushButton("Abrir en Jupyter")
        self._open_jupyter_btn.setEnabled(False)
        self._open_jupyter_btn.setToolTip("Pendiente — placeholder UI")
        header.addWidget(self._title_label)
        header.addSpacing(12)
        header.addWidget(self._meta_label)
        header.addStretch(1)
        header.addWidget(self._open_jupyter_btn)
        root.addLayout(header)

        self._scroll = QScrollArea(self)
        self._scroll.setWidgetResizable(True)
        self._scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        root.addWidget(self._scroll, 1)

        self._container = QWidget()
        self._cells_layout = QVBoxLayout(self._container)
        self._cells_layout.setContentsMargins(8, 8, 8, 8)
        self._cells_layout.setSpacing(10)
        self._cells_layout.addStretch(1)
        self._scroll.setWidget(self._container)

    # ------------------------------------------------------------------
    def _clear_cells(self) -> None:
        while self._cells_layout.count() > 0:
            item = self._cells_layout.takeAt(0)
            w = item.widget()
            if w is not None:
                w.setParent(None)
                w.deleteLater()
        self._cells_layout.addStretch(1)

    def load_empty(self, message: str) -> None:
        """Muestra un mensaje (clase sin notebook, error, etc.)."""
        self._clear_cells()
        self._title_label.setText("—")
        self._meta_label.setText("")
        label = QLabel(message)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: #8c959f; padding: 40px; font-size: 12pt;")
        self._cells_layout.insertWidget(0, label)

    def load_notebook(self, notebook: dict[str, Any]) -> None:
        """Renderiza un notebook recibido de ``notebook_loader.load_notebook``."""
        self._clear_cells()
        title = notebook.get("title", "")
        cells = notebook.get("cells", []) or []
        self._title_label.setText(title)
        self._meta_label.setText(f"{len(cells)} celdas")

        insert_at = 0
        for cell in cells:
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
            sep = _CellSeparator()
            self._cells_layout.insertWidget(insert_at, sep)
            insert_at += 1

    # ------------------------------------------------------------------
    def _build_markdown_cell(self, source: str) -> QWidget:
        browser = QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.setMarkdown(source or "")
        browser.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        browser.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        browser.document().setTextWidth(browser.viewport().width())
        # Sizing fijo: altura = sizeHint del documento, sin scroll interno.
        doc_height = int(browser.document().size().height()) + 24
        browser.setFixedHeight(max(40, doc_height))
        browser.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return browser

    def _build_code_cell(
        self,
        source: str,
        outputs: list[dict[str, Any]] | None,
        execution_count: int | None,
    ) -> QWidget:
        wrapper = QWidget()
        layout = QVBoxLayout(wrapper)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        row = QHBoxLayout()
        row.setSpacing(8)
        exec_label = QLabel(f"[{execution_count}]:" if execution_count else "[ ]:")
        exec_label.setStyleSheet("color: #1f6feb; font-family: monospace;")
        exec_label.setFixedWidth(48)
        exec_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
        row.addWidget(exec_label)

        editor = QTextEdit()
        editor.setReadOnly(True)
        editor.setFont(_code_font())
        editor.setStyleSheet(_CODE_STYLE)
        editor.setPlainText(source or "")
        editor.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        editor.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        editor.document().setTextWidth(editor.viewport().width())
        n_lines = max(1, (source or "").count("\n") + 1)
        editor.setFixedHeight(min(600, n_lines * 18 + 28))
        row.addWidget(editor, 1)
        layout.addLayout(row)

        if outputs:
            for out in outputs:
                out_widget = self._build_output(out)
                if out_widget is not None:
                    indent = QHBoxLayout()
                    indent.setContentsMargins(56, 0, 0, 0)
                    indent.addWidget(out_widget, 1)
                    layout.addLayout(indent)

        return wrapper

    def _build_output(self, out: dict[str, Any]) -> QWidget | None:
        otype = out.get("output_type", "")
        if otype == "stream":
            text = out.get("text", "")
            if isinstance(text, list):
                text = "".join(text)
            return self._make_pre(text, style=_OUTPUT_STYLE)
        if otype in ("execute_result", "display_data"):
            data = out.get("data", {}) or {}
            # Imagen PNG embebida en base64.
            if "image/png" in data:
                return self._make_image(data["image/png"])
            if "text/plain" in data:
                text = data["text/plain"]
                if isinstance(text, list):
                    text = "".join(text)
                return self._make_pre(text, style=_OUTPUT_STYLE)
            return None
        if otype == "error":
            traceback = out.get("traceback") or []
            text = "\n".join(traceback) if isinstance(traceback, list) else str(traceback)
            # Quitar códigos ANSI básicos.
            import re as _re

            text = _re.sub(r"\x1b\[[0-9;]*m", "", text)
            return self._make_pre(text, style=_ERROR_STYLE)
        return None

    def _make_pre(self, text: str, style: str) -> QWidget:
        edit = QTextEdit()
        edit.setReadOnly(True)
        edit.setFont(_code_font())
        edit.setStyleSheet(style)
        edit.setPlainText(text or "")
        edit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        n_lines = max(1, (text or "").count("\n") + 1)
        edit.setFixedHeight(min(400, n_lines * 16 + 24))
        return edit

    def _make_image(self, b64_data: str) -> QWidget:
        label = QLabel()
        try:
            raw = base64.b64decode(b64_data)
            pix = QPixmap()
            pix.loadFromData(raw)
            if not pix.isNull():
                # Limita ancho a 800px conservando aspect ratio.
                if pix.width() > 800:
                    pix = pix.scaledToWidth(
                        800, Qt.TransformationMode.SmoothTransformation
                    )
                label.setPixmap(pix)
                label.setStyleSheet("background-color: #ffffff; padding: 8px; border-radius: 6px;")
                return label
        except Exception as exc:
            log.warning("No se pudo decodificar imagen de output: %s", exc)
        label.setText("[imagen no decodificable]")
        label.setStyleSheet(_OUTPUT_STYLE)
        return label

    def _build_raw_cell(self, source: str) -> QWidget:
        return self._make_pre(source, style=_OUTPUT_STYLE)
