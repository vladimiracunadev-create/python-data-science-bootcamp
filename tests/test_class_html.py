"""Tests del renderizador compartido de clases (``app.class_html``).

Cubre lo que se rompió históricamente: listas pegadas al párrafo anterior,
bloques de código sin fondo o con el texto ilegible en Qt, y tablas que
llegaban sin atributos y se dibujaban como texto corrido.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.class_html import (  # noqa: E402
    CODE_INK,
    QT_THEMES,
    normalize_markdown,
    qt_page,
    qt_stylesheet,
    render_markdown,
    to_qt_html,
)


def test_list_glued_to_paragraph_becomes_a_real_list():
    """``Recursos:`` + ``- item`` sin línea en blanco debe dar un <ul>."""
    md = "Recursos externos:\n- [uv](https://docs.astral.sh/uv/) — gestor.\n- Otro.\n"
    html_out = render_markdown(md)
    assert "<ul>" in html_out
    assert html_out.count("<li>") == 2


def test_normalize_markdown_respects_fenced_code():
    """Dentro de un bloque ``` no se toca nada — un '- x' ahí es código."""
    md = "Texto:\n```bash\nls -la\n- no soy una lista\n```\n"
    out = normalize_markdown(md)
    assert "- no soy una lista" in out
    # Solo se insertó (como mucho) la línea previa al fence, no dentro.
    assert out.count("- no soy una lista") == 1


def test_code_block_is_wrapped_in_a_solid_table_for_qt():
    """Qt no pinta el fondo de un <pre>; el bloque debe ir en una celda."""
    html_out = to_qt_html(render_markdown("```python\nx = 1\n```\n"), "light")
    assert 'class="cls-code"' in html_out
    assert "bgcolor=" in html_out


def test_code_block_forces_a_readable_ink():
    """Un bloque ```bash casi no tiene tokens: necesita color base explícito."""
    html_out = to_qt_html(render_markdown("```bash\npip install -r req.txt\n```\n"), "dark")
    assert CODE_INK in html_out
    # El <code> anidado de Pygments se quita: en Qt se lleva el estilo inline.
    assert "<code>" not in html_out


def test_tables_get_explicit_attributes():
    md = "| a | b |\n| --- | --- |\n| 1 | 2 |\n"
    html_out = to_qt_html(render_markdown(md), "light")
    assert 'class="cls-data"' in html_out
    assert 'border="1"' in html_out


def test_headings_get_navigable_anchors():
    """El índice interno de la clase necesita <a name> además del id."""
    html_out = to_qt_html(render_markdown("## 🎯 Objetivo\n"), "light")
    assert "<a name=" in html_out


def test_blockquote_becomes_a_bar_plus_content():
    html_out = to_qt_html(render_markdown("> una cita\n"), "light")
    assert 'class="cls-quote"' in html_out
    assert QT_THEMES["light"]["quote_bar"] in html_out


def test_qt_page_is_a_full_document_per_theme():
    for theme in ("light", "dark"):
        page = qt_page("# Hola\n", theme=theme)
        assert page.startswith("<html>")
        assert QT_THEMES[theme]["bg"] in page


def test_stylesheet_scales_with_zoom():
    small = qt_stylesheet("light", scale=1.0)
    big = qt_stylesheet("light", scale=1.5)
    assert small != big
    assert "pt;" in big


def test_renders_a_real_class_readme():
    """Extremo a extremo sobre una clase real del currículo."""
    readme = (
        Path(__file__).resolve().parents[1]
        / "classes"
        / "parte-0-prerrequisitos"
        / "001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda"
        / "README.md"
    )
    page = qt_page(readme.read_text(encoding="utf-8"), theme="light")
    assert "Objetivo" in page
    assert 'class="cls-data"' in page  # la tabla de temas
