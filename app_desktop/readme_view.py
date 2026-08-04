"""Vista de la clase: README renderizado como HTML en widgets Qt nativos.

Qué resuelve:
    Antes el README se pasaba crudo a ``QTextBrowser.setMarkdown()``: sin
    color en el código, sin control de tipografía, con el texto ocupando
    todo el ancho de la ventana (líneas de 200 caracteres, ilegibles) y con
    los colores fijos del tema claro incluso en modo oscuro.

    Ahora el markdown pasa por ``app.class_html`` — el MISMO renderizador que
    genera las páginas de GitHub Pages — y se muestra con ``setHtml()`` sobre
    una columna de lectura centrada y de ancho acotado, con tema claro/oscuro
    y zoom de texto. Sigue sin haber WebView: es rich text de Qt.
"""

from __future__ import annotations

import logging
from pathlib import Path

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QHBoxLayout, QTextBrowser, QWidget

try:
    from app.class_html import markdown_available, qt_page, qt_stylesheet
except Exception as exc:  # pragma: no cover - entorno sin markdown
    logging.getLogger(__name__).warning("class_html no disponible: %s", exc)
    markdown_available = lambda: False  # noqa: E731
    qt_page = None  # type: ignore[assignment]
    qt_stylesheet = None  # type: ignore[assignment]

log = logging.getLogger(__name__)

#: Ancho máximo de la columna de lectura, en píxeles. Por encima de ~95
#: caracteres por línea la lectura se degrada; 940 px con la tipografía base
#: deja unas 90.
READING_WIDTH = 940

#: Límites del zoom de texto (Ctrl + / Ctrl -).
MIN_SCALE = 0.8
MAX_SCALE = 1.8


class ReadmeView(QWidget):
    """Columna de lectura centrada con el README de la clase en HTML."""

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self._theme = "light"
        self._scale = 1.0
        self._markdown_text = ""
        self._header_html = ""
        self._base_dir: Path | None = None

        self._browser = QTextBrowser()
        self._browser.setOpenExternalLinks(False)
        self._browser.setOpenLinks(False)
        self._browser.anchorClicked.connect(self._on_anchor_clicked)
        self._browser.setFrameShape(QTextBrowser.Shape.NoFrame)
        self._browser.setMaximumWidth(READING_WIDTH)
        self._browser.document().setDocumentMargin(30)

        # Columna centrada: el navegador se lleva casi todo el estiramiento y
        # su `maximumWidth` lo frena en READING_WIDTH; el sobrante se reparte
        # entre los dos espaciadores, que es lo que centra la columna.
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch(1)
        layout.addWidget(self._browser, 20)
        layout.addStretch(1)

    # ------------------------------------------------------------------
    # API pública
    # ------------------------------------------------------------------
    def load_markdown(
        self,
        text: str,
        base_dir: Path | None = None,
        header_html: str = "",
    ) -> None:
        """Carga el markdown de una clase; ``base_dir`` resuelve imágenes."""
        self._markdown_text = text or ""
        self._header_html = header_html
        self._base_dir = base_dir
        if base_dir is not None:
            self._browser.setSearchPaths([str(base_dir)])
            self._browser.document().setBaseUrl(
                QUrl.fromLocalFile(str(base_dir) + "/")
            )
        self._rerender()
        self._browser.verticalScrollBar().setValue(0)

    def load_empty_state(self, message: str) -> None:
        """Mensaje cuando no hay clase seleccionada o falló la lectura."""
        self.load_markdown(f"# {message}\n")

    def set_theme(self, theme: str) -> None:
        """Aplica tema ``light``/``dark`` re-renderizando el documento."""
        if theme == self._theme:
            return
        self._theme = theme
        self._rerender(keep_scroll=True)

    def zoom_in(self) -> None:
        self._set_scale(self._scale + 0.1)

    def zoom_out(self) -> None:
        self._set_scale(self._scale - 0.1)

    def zoom_reset(self) -> None:
        self._set_scale(1.0)

    def set_scale(self, scale: float) -> None:
        """Fija el zoom de texto (usado al restaurar la preferencia guardada)."""
        self._set_scale(scale)

    @property
    def scale(self) -> float:
        return self._scale

    # ------------------------------------------------------------------
    # Interno
    # ------------------------------------------------------------------
    def _set_scale(self, value: float) -> None:
        value = max(MIN_SCALE, min(MAX_SCALE, round(value, 2)))
        if abs(value - self._scale) < 0.001:
            return
        self._scale = value
        self._rerender(keep_scroll=True)

    def _rerender(self, keep_scroll: bool = False) -> None:
        pos = self._browser.verticalScrollBar().value() if keep_scroll else 0
        if markdown_available() and qt_page is not None:
            try:
                self._browser.setHtml(
                    qt_page(
                        self._markdown_text,
                        theme=self._theme,
                        scale=self._scale,
                        header_html=self._header_html,
                    )
                )
            except Exception as exc:  # pragma: no cover - defensivo
                log.warning("Fallo el render HTML, uso markdown plano: %s", exc)
                self._fallback_markdown()
        else:
            self._fallback_markdown()
        self._browser.verticalScrollBar().setValue(pos)

    def _fallback_markdown(self) -> None:
        """Sin python-markdown: render nativo, peor pero funcional."""
        if qt_stylesheet is not None:
            self._browser.document().setDefaultStyleSheet(
                qt_stylesheet(self._theme, scale=self._scale)
            )
        self._browser.setMarkdown(self._markdown_text)

    def _on_anchor_clicked(self, url: QUrl) -> None:
        """Anclas internas hacen scroll; el resto abre en el navegador/sistema."""
        if url.scheme() in ("http", "https", "mailto"):
            QDesktopServices.openUrl(url)
            return
        fragment = url.fragment()
        if not url.path() and fragment:
            self._browser.scrollToAnchor(fragment)
            return
        # Enlace relativo a un archivo de la clase (PDF, PPTX, notebook…).
        if self._base_dir is not None:
            target = (self._base_dir / url.path()).resolve()
            if target.exists():
                QDesktopServices.openUrl(QUrl.fromLocalFile(str(target)))
                return
        if fragment:
            self._browser.scrollToAnchor(fragment)

    # Delegación cómoda para el resto de la app.
    def scroll_to_top(self) -> None:
        self._browser.verticalScrollBar().setValue(0)

    def setFocus(self) -> None:  # noqa: N802 (Qt API)
        self._browser.setFocus(Qt.FocusReason.OtherFocusReason)
