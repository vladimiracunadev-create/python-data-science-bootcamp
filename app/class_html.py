"""Renderizador compartido Markdown → HTML de las clases.

Qué resuelve:
    Hasta v3.10.0 había DOS caminos distintos para mostrar una clase:
    GitHub Pages convertía el ``README.md`` a HTML con python-markdown,
    y la app Windows lo pasaba crudo a ``QTextBrowser.setMarkdown()`` —
    que ignora tablas complejas, no colorea código y no permite estilar
    nada. Resultado: la misma clase se veía bien en la web y mal en la app.

    Este módulo es la fuente única de la conversión. Ambos consumidores
    llaman a :func:`render_markdown`; la app además pasa el fragmento por
    :func:`to_qt_html`, que lo adapta al subset de HTML/CSS que entiende el
    motor de rich text de Qt (sin flexbox, sin border-radius, sin
    ``max-width``), y por :func:`qt_page` para envolverlo con el tema.

Nota sobre Qt:
    ``QTextBrowser`` NO pinta el fondo de un ``<pre>`` a todo el ancho del
    bloque: solo pinta detrás de los glifos. El truco estándar es meter el
    ``<pre>`` en una celda de tabla con ``bgcolor`` — eso sí ocupa el ancho
    completo. Lo mismo aplica a los ``<blockquote>`` con barra lateral.
"""

from __future__ import annotations

import re
from typing import Any

try:  # pragma: no cover - entorno mínimo sin markdown
    import markdown as _markdown
except Exception:  # pragma: no cover
    _markdown = None  # type: ignore[assignment]

# ──────────────────────────────────────────────────────────────────────────────
# Conversión markdown → HTML (compartida app + Pages)
# ──────────────────────────────────────────────────────────────────────────────

#: Extensiones de python-markdown. ``codehilite`` con Pygments colorea los
#: bloques de código; ``noclasses`` mete los estilos inline para que el HTML
#: sirva tal cual en Qt (que no carga hojas de estilo externas).
MD_EXTENSIONS: list[str] = [
    "extra",
    "toc",
    "sane_lists",
    "tables",
    "fenced_code",
    "codehilite",
]

#: Tema Pygments. Se usa el mismo en claro y oscuro: los bloques de código
#: quedan siempre oscuros (igual que en la web y que en un notebook real).
PYGMENTS_STYLE = "github-dark"

#: Fondo del bloque de código por tema. En claro va el oscuro clásico; en
#: oscuro se usa el MÁS oscuro de los dos, para que el bloque se despegue del
#: fondo de la página (que en modo oscuro ya es #161b22).
CODE_BG = {"light": "#0d1117", "dark": "#010409"}

#: Color base del texto dentro del bloque. Pygments solo colorea los tokens que
#: reconoce: en un bloque ```bash casi todo es token genérico y sin este color
#: explícito hereda el del documento — texto gris oscuro sobre fondo oscuro.
CODE_INK = "#e6edf3"

MD_EXTENSION_CONFIGS: dict[str, dict[str, Any]] = {
    "codehilite": {
        "noclasses": True,
        "pygments_style": PYGMENTS_STYLE,
        "guess_lang": False,
    },
}

_MD_INSTANCE = None


def _md():
    """Instancia perezosa y reutilizada de ``markdown.Markdown``."""
    global _MD_INSTANCE
    if _MD_INSTANCE is None:
        if _markdown is None:  # pragma: no cover
            raise RuntimeError("python-markdown no está instalado")
        _MD_INSTANCE = _markdown.Markdown(
            extensions=MD_EXTENSIONS,
            extension_configs=MD_EXTENSION_CONFIGS,
            output_format="html5",
        )
    return _MD_INSTANCE


def markdown_available() -> bool:
    """True si python-markdown se puede importar (la app cae a texto si no)."""
    return _markdown is not None


_RE_LIST_ITEM = re.compile(r"^\s{0,3}([-*+]|\d+[.)])\s+\S")
_RE_FENCE = re.compile(r"^\s*(```|~~~)")


def normalize_markdown(text: str) -> str:
    """Inserta la línea en blanco que ``sane_lists`` exige antes de una lista.

    Qué resuelve:
        Varios READMEs escriben ``Recursos externos:`` y en la línea siguiente
        arrancan con ``- item``. CommonMark lo acepta, pero python-markdown con
        ``sane_lists`` NO: sin línea en blanco de por medio pega los ítems al
        párrafo y la lista se ve como un renglón corrido con guiones sueltos.
        Se veía roto igual en la app y en GitHub Pages; normalizar acá lo
        arregla en los dos sin tocar los 232 README.
    """
    lines = (text or "").split("\n")
    out: list[str] = []
    in_fence = False
    for i, line in enumerate(lines):
        if _RE_FENCE.match(line):
            in_fence = not in_fence
        if not in_fence and i > 0 and _RE_LIST_ITEM.match(line):
            prev = lines[i - 1]
            prev_is_open_paragraph = (
                prev.strip()
                and not _RE_LIST_ITEM.match(prev)
                and not prev.lstrip().startswith(("#", ">", "|"))
                and not _RE_FENCE.match(prev)
            )
            if prev_is_open_paragraph:
                out.append("")
        out.append(line)
    return "\n".join(out)


def render_markdown(text: str) -> str:
    """Convierte markdown a un fragmento HTML. Fuente única app + Pages."""
    md = _md()
    md.reset()
    return md.convert(normalize_markdown(text))


# ──────────────────────────────────────────────────────────────────────────────
# Temas para la app (QTextBrowser)
# ──────────────────────────────────────────────────────────────────────────────

QT_THEMES: dict[str, dict[str, str]] = {
    "light": {
        "bg": "#ffffff",
        "ink": "#1f2328",
        "ink_soft": "#57606a",
        "accent": "#0f766e",
        "accent_soft": "#0d9488",
        "link": "#0969da",
        "line": "#d0d7de",
        "quote_bg": "#f6f8fa",
        "quote_bar": "#d9a441",
        "inline_code_bg": "#eef2f7",
        "inline_code_ink": "#4c1d95",
        "th_bg": "#0f766e",
        "th_ink": "#ffffff",
        "td_bg": "#ffffff",
        "td_bg_alt": "#f6f8fa",
        "callout_bg": "#fff8e6",
    },
    "dark": {
        # La "página" en modo oscuro es #161b22 (el mismo tono de tarjeta que
        # usa el QSS de la ventana), NO el #0d1117 del fondo de la app: así el
        # bloque de código y la cita se distinguen del papel.
        "bg": "#161b22",
        "ink": "#e6edf3",
        "ink_soft": "#9198a1",
        "accent": "#2dd4bf",
        "accent_soft": "#5eead4",
        "link": "#58a6ff",
        "line": "#30363d",
        "quote_bg": "#0d1117",
        "quote_bar": "#d9a441",
        "inline_code_bg": "#262c36",
        "inline_code_ink": "#d2a8ff",
        "th_bg": "#164e63",
        "th_ink": "#ffffff",
        "td_bg": "#1c2128",
        "td_bg_alt": "#20262e",
        "callout_bg": "#1c1a12",
    },
}


def qt_stylesheet(theme: str = "light", *, scale: float = 1.0) -> str:
    """Hoja de estilo para ``QTextDocument.setDefaultStyleSheet``.

    ``scale`` permite el zoom de texto (Ctrl +/-) sin recargar el contenido:
    todos los tamaños se derivan de él.
    """
    c = QT_THEMES.get(theme, QT_THEMES["light"])

    def pt(base: float) -> str:
        return f"{base * scale:.1f}pt"

    return f"""
    body {{ color: {c['ink']}; background-color: {c['bg']};
            font-family: 'Segoe UI', 'Inter', Arial, sans-serif; font-size: {pt(11)}; }}
    p, li, td, th {{ font-size: {pt(11)}; }}
    h1 {{ color: {c['accent']}; font-size: {pt(20)}; font-weight: 700;
          margin-top: 4px; margin-bottom: 10px; }}
    h2 {{ color: {c['ink']}; font-size: {pt(15.5)}; font-weight: 700;
          margin-top: 26px; margin-bottom: 8px;
          border-bottom: 1px solid {c['line']}; padding-bottom: 4px; }}
    h3 {{ color: {c['ink']}; font-size: {pt(13)}; font-weight: 700;
          margin-top: 20px; margin-bottom: 6px; }}
    h4, h5, h6 {{ color: {c['ink_soft']}; font-size: {pt(11.5)}; font-weight: 700;
                  margin-top: 16px; margin-bottom: 4px; }}
    p {{ margin-top: 6px; margin-bottom: 10px; line-height: 152%; }}
    li {{ margin-bottom: 5px; line-height: 150%; }}
    a {{ color: {c['link']}; text-decoration: none; }}
    code {{ background-color: {c['inline_code_bg']}; color: {c['inline_code_ink']};
            font-family: 'Cascadia Code', 'JetBrains Mono', Consolas, monospace;
            font-size: {pt(10)}; }}
    pre {{ font-family: 'Cascadia Code', 'JetBrains Mono', Consolas, monospace;
           font-size: {pt(10)}; margin: 0; }}
    pre code {{ background-color: transparent; color: inherit; }}
    table.cls-code {{ margin-top: 10px; margin-bottom: 14px; }}
    table.cls-quote {{ margin-top: 12px; margin-bottom: 14px; }}
    table.cls-data {{ margin-top: 12px; margin-bottom: 16px;
                      border: 1px solid {c['line']}; }}
    table.cls-data th {{ background-color: {c['th_bg']}; color: {c['th_ink']};
                         font-weight: 700; }}
    table.cls-data td {{ background-color: {c['td_bg']}; color: {c['ink']}; }}
    .cls-lead {{ color: {c['ink_soft']}; }}
    hr {{ color: {c['line']}; }}
    """


# ──────────────────────────────────────────────────────────────────────────────
# Adaptación del fragmento al motor de rich text de Qt
# ──────────────────────────────────────────────────────────────────────────────

_RE_CODEHILITE = re.compile(
    r'<div class="codehilite"[^>]*>(?P<inner>.*?)</div>', re.DOTALL
)
_RE_BARE_PRE = re.compile(r"(?P<pre><pre\b.*?</pre>)", re.DOTALL)
_RE_BLOCKQUOTE = re.compile(r"<blockquote>(?P<inner>.*?)</blockquote>", re.DOTALL)
_RE_TABLE_OPEN = re.compile(r"<table>")
_RE_HEADING_ID = re.compile(r'<(?P<tag>h[1-6])\b[^>]*\bid="(?P<id>[^"]+)"')


_RE_PRE_OPEN = re.compile(r"<pre(?P<attrs>[^>]*)>")


_RE_INNER_CODE = re.compile(r"</?code>")


def _force_code_ink(inner_html: str) -> str:
    """Fija el color base del texto en el ``<pre>`` del bloque de código.

    También quita el ``<code>`` que Pygments anida dentro del ``<pre>``: el
    motor de Qt no aplica el selector descendente ``pre code``, así que ese
    ``<code>`` se lleva el estilo del código *inline* (fondo claro, tinta
    violeta) y deja ilegible todo lo que Pygments no coloreó — por ejemplo un
    bloque ```bash entero.
    """
    inner_html = _RE_INNER_CODE.sub("", inner_html)

    def repl(match: re.Match[str]) -> str:
        attrs = match.group("attrs")
        if "style=" in attrs:
            return re.sub(
                r'style="', f'style="color:{CODE_INK};', f"<pre{attrs}>", count=1
            )
        return f'<pre{attrs} style="color:{CODE_INK};">'

    return _RE_PRE_OPEN.sub(repl, inner_html, count=1)


def _code_block(inner_html: str, theme: str) -> str:
    """Envuelve un bloque de código en una tabla de una celda con fondo sólido.

    Qt no pinta el fondo de un ``<pre>`` a todo el ancho; una celda de tabla sí.
    """
    bg = CODE_BG.get(theme, CODE_BG["light"])
    return (
        '<table class="cls-code" width="100%" cellpadding="12" cellspacing="0" '
        f'border="0"><tr><td bgcolor="{bg}">{_force_code_ink(inner_html)}</td>'
        "</tr></table>"
    )


def _quote_block(inner_html: str, bar_color: str, bg_color: str) -> str:
    """Blockquote como tabla: celda estrecha de color + celda de contenido."""
    return (
        '<table class="cls-quote" width="100%" cellpadding="0" cellspacing="0" '
        'border="0"><tr>'
        f'<td width="4" bgcolor="{bar_color}"></td>'
        f'<td bgcolor="{bg_color}" style="padding-left:14px;padding-right:14px;">'
        f"{inner_html}</td>"
        "</tr></table>"
    )


def to_qt_html(fragment: str, theme: str = "light") -> str:
    """Adapta un fragmento HTML al subset que soporta ``QTextBrowser``.

    Transformaciones:
        1. Bloques de código (``codehilite`` o ``<pre>`` pelado) → tabla con
           fondo sólido a todo el ancho.
        2. ``<blockquote>`` → tabla con barra lateral de color.
        3. ``<table>`` → atributos ``border``/``cellpadding`` explícitos, que
           Qt respeta mejor que el CSS de bordes.
        4. Encabezados con ``id`` → se les antepone ``<a name="…">`` para que
           los enlaces internos del índice funcionen.
    """
    c = QT_THEMES.get(theme, QT_THEMES["light"])
    html_out = fragment

    # 1a. Bloques con resaltado de Pygments.
    html_out = _RE_CODEHILITE.sub(
        lambda m: _code_block(m.group("inner"), theme), html_out
    )

    # 1b. Bloques de código sin resaltar (```sin lenguaje) que quedaron sueltos.
    def _wrap_bare(match: re.Match[str]) -> str:
        return _code_block(match.group("pre"), theme)

    # Solo los <pre> que NO están ya dentro de una celda cls-code.
    parts = re.split(r'(<table class="cls-code".*?</table>)', html_out, flags=re.DOTALL)
    html_out = "".join(
        part if part.startswith('<table class="cls-code"') else _RE_BARE_PRE.sub(_wrap_bare, part)
        for part in parts
    )

    # 2. Citas.
    html_out = _RE_BLOCKQUOTE.sub(
        lambda m: _quote_block(m.group("inner"), c["quote_bar"], c["quote_bg"]),
        html_out,
    )

    # 3. Tablas de datos del markdown.
    html_out = _RE_TABLE_OPEN.sub(
        '<table class="cls-data" width="100%" border="1" cellpadding="7" cellspacing="0">',
        html_out,
    )

    # 4. Anclas navegables.
    html_out = _RE_HEADING_ID.sub(
        lambda m: f'<a name="{m.group("id")}"></a><{m.group("tag")}', html_out
    )

    return html_out


def qt_page(
    markdown_text: str,
    *,
    theme: str = "light",
    scale: float = 1.0,
    header_html: str = "",
) -> str:
    """Documento HTML completo listo para ``QTextBrowser.setHtml``."""
    fragment = to_qt_html(render_markdown(markdown_text), theme)
    c = QT_THEMES.get(theme, QT_THEMES["light"])
    return (
        "<html><head><meta charset='utf-8'>"
        f"<style>{qt_stylesheet(theme, scale=scale)}</style></head>"
        f"<body bgcolor='{c['bg']}'>{header_html}{fragment}</body></html>"
    )


__all__ = [
    "MD_EXTENSIONS",
    "MD_EXTENSION_CONFIGS",
    "PYGMENTS_STYLE",
    "QT_THEMES",
    "markdown_available",
    "normalize_markdown",
    "render_markdown",
    "qt_stylesheet",
    "to_qt_html",
    "qt_page",
]
