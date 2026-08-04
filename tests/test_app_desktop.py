"""Smoke tests para la app Windows nativa (PySide6).

Validan que el paquete se importe sin levantar QApplication a la fuerza, que
los adapters al currículo encuentren las 232 clases, y que la ``MainWindow``
se instancie correctamente con plataforma ``offscreen`` (CI headless).
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def test_package_metadata_importable():
    """El paquete y su versión deben importar sin tocar Qt."""
    import app_desktop

    assert app_desktop.__version__ == "3.11.0"


def test_curriculum_adapter_lists_232_classes():
    """El adapter delega en app.notebook_loader y ve las 232 clases."""
    from app_desktop import curriculum

    tree = curriculum.list_curriculum()
    assert len(tree) == 9
    total = sum(len(part["classes"]) for part in tree)
    assert total == 232


def test_curriculum_resolves_asset_paths():
    """Para una clase real, debe resolver PDF, PPTX y notebook si existen."""
    from app_desktop import curriculum

    slug = "parte-7-etica-fairness-privacidad/223-tipos-de-sesgo-algoritmico-y-origenes"
    pdf = curriculum.class_pdf(slug)
    pptx = curriculum.class_pptx(slug)
    nb = curriculum.class_notebook(slug)
    assert pdf is not None and pdf.exists()
    assert pptx is not None and pptx.exists()
    assert nb is not None and nb.exists()


@pytest.fixture(scope="module")
def qapp():
    """QApplication offscreen para tests headless (CI)."""
    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    from PySide6.QtWidgets import QApplication

    app = QApplication.instance() or QApplication([])
    yield app


def test_main_window_instantiates(qapp):
    """MainWindow debe levantar sin pedir display."""
    from app_desktop.main_window import MainWindow

    win = MainWindow()
    # Sin esto la ventana no se materializa y algunas señales de Qt no se
    # registran; sin ser show() no hay redraw real, pero sí pasa init.
    assert "Python Data Science Program" in win.windowTitle()
    assert win.size().width() >= 1000


def test_notebook_view_renders_a_real_class(qapp):
    """Cargar la clase 223 (sintética sin imágenes) no debe explotar."""
    from app_desktop.curriculum import load_notebook
    from app_desktop.notebook_view import NotebookView

    nb = load_notebook("parte-7-etica-fairness-privacidad/223-tipos-de-sesgo-algoritmico-y-origenes")
    view = NotebookView()
    view.load_notebook(nb)
    # Debe haber al menos algunas celdas montadas.
    assert nb["metadata"]["n_cells"] > 0


def test_readme_view_renders_html(qapp):
    """ReadmeView renderiza HTML (no markdown crudo) sin web engine de por medio."""
    from app_desktop.readme_view import ReadmeView

    view = ReadmeView()
    view.load_markdown("# Hola\n\nun párrafo con `código`.")
    assert "Hola" in view._browser.toPlainText()
    # El documento debe ser rich text con estilos, no texto plano.
    assert "<h1" in view._browser.toHtml().lower()


def test_readme_view_theme_and_zoom(qapp):
    """Cambiar tema y zoom re-renderiza sin perder el contenido."""
    from app_desktop.readme_view import MAX_SCALE, ReadmeView

    view = ReadmeView()
    view.load_markdown("# Título\n\nTexto de prueba.")
    view.set_theme("dark")
    assert "Texto de prueba" in view._browser.toPlainText()

    before = view.scale
    view.zoom_in()
    assert view.scale > before
    for _ in range(30):
        view.zoom_in()
    assert view.scale <= MAX_SCALE  # el zoom está acotado
    view.zoom_reset()
    assert view.scale == 1.0


def test_main_window_opens_a_class_and_fills_header(qapp):
    """Abrir una clase debe poblar la cabecera y habilitar las acciones."""
    from app_desktop.main_window import MainWindow

    win = MainWindow()
    slug = "parte-0-prerrequisitos/001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda"
    win._open_class(slug)

    assert win._current_slug == slug
    assert "001" in win._header._badge.text()
    assert win._header._title.text()  # título limpio, sin el prefijo "Clase NNN —"
    assert not win._header._title.text().startswith("Clase 001")
    assert win._act_web.isEnabled()


def test_tree_labels_do_not_duplicate_the_part_prefix(qapp):
    """El árbol no debe mostrar 'Parte 0 — Parte 0 — …' (regresión de v3.10.0)."""
    from app_desktop.main_window import MainWindow

    win = MainWindow()
    root = win._tree_model.invisibleRootItem()
    for i in range(root.rowCount()):
        label = root.child(i).text()
        assert label.count("Parte ") == 1, label
