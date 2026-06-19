"""Vista de README en markdown usando QTextBrowser nativo.

Qué resuelve:
    Renderiza markdown sin WebView ni QWebEngineView — usa la API nativa
    ``QTextBrowser.setMarkdown()`` (Qt 5.14+), que entrega rich text Qt.
    Las imágenes relativas se resuelven con ``setSearchPaths``.
"""

from __future__ import annotations

from pathlib import Path

from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTextBrowser


class ReadmeView(QTextBrowser):
    """QTextBrowser configurado para renderizar el README de una clase."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setOpenExternalLinks(True)
        self.setOpenLinks(True)
        # Fuente legible base; QTextBrowser usa monospace para <pre><code>.
        font = QFont("Segoe UI", 11)
        self.setFont(font)
        self.document().setDefaultStyleSheet(
            """
            h1 { color: #0969da; margin-top: 16px; margin-bottom: 8px; }
            h2 { color: #1f2328; margin-top: 14px; margin-bottom: 6px; }
            h3 { color: #1f2328; margin-top: 12px; margin-bottom: 4px; }
            code { background-color: #eaeef2; padding: 2px 4px; border-radius: 3px;
                   font-family: "Cascadia Code", "Consolas", monospace; }
            pre { background-color: #f6f8fa; padding: 12px; border-radius: 6px;
                  font-family: "Cascadia Code", "Consolas", monospace; }
            a { color: #0969da; text-decoration: none; }
            blockquote { border-left: 4px solid #d0d7de; padding-left: 12px;
                         color: #57606a; margin-left: 0; }
            table { border-collapse: collapse; }
            th, td { border: 1px solid #d0d7de; padding: 6px 10px; }
            th { background-color: #eaeef2; }
            """
        )

    def load_markdown(self, text: str, base_dir: Path | None = None) -> None:
        """Carga texto markdown; ``base_dir`` para resolver imágenes relativas."""
        if base_dir is not None:
            # Permite que ![](./img.png) y similares resuelvan al filesystem.
            self.setSearchPaths([str(base_dir)])
            self.document().setBaseUrl(
                # QUrl import lazy para no pesar el módulo si no se usa.
                __import__("PySide6.QtCore", fromlist=["QUrl"]).QUrl.fromLocalFile(
                    str(base_dir) + "/"
                )
            )
        self.setMarkdown(text or "")
        # Scrollear al inicio cuando se carga una clase nueva.
        self.verticalScrollBar().setValue(0)

    def load_empty_state(self, message: str) -> None:
        """Muestra un mensaje cuando no hay clase seleccionada o hay error."""
        self.setMarkdown(f"# {message}\n")
