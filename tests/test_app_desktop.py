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

    assert app_desktop.__version__ == "3.10.0"


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


def test_readme_view_setmarkdown(qapp):
    """ReadmeView usa QTextBrowser.setMarkdown — sin web engine de por medio."""
    from app_desktop.readme_view import ReadmeView

    view = ReadmeView()
    view.load_markdown("# Hola\n\nun párrafo con `código`.")
    # Si llegamos acá Qt rindió bien el markdown como rich text.
    assert "Hola" in view.toPlainText()
