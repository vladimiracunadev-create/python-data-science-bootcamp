"""Genera el icono del producto en todos los formatos que consume el proyecto.

Qué resuelve:
    Hasta v3.10.0 el ejecutable salía con el icono genérico de PyInstaller
    (``program.spec`` buscaba ``installer/icon.ico`` y ese archivo no existía),
    el instalador Inno Setup tenía ``SetupIconFile`` comentado y la ventana Qt
    no declaraba icono. Este script parte del SVG maestro
    ``installer/icon.svg`` y produce:

        installer/icon.ico   — multi-resolución (16…256), para el .exe,
                               el instalador y la ventana de la app
        installer/icon.png   — 512 px, respaldo para Qt y para la documentación
        site/assets/icon.svg — el mismo SVG, para el favicon de GitHub Pages
        site/assets/icon.png — 512 px, para las tarjetas Open Graph del portal

Uso:
    python scripts/generate_product_icon.py

Dependencias: ``pillow`` y ``cairosvg`` (ambos en requirements.txt). Si
``cairosvg`` no está disponible se usa un rasterizador de respaldo mínimo
basado en QtSvg (PySide6), que ya es dependencia de la app.
"""

from __future__ import annotations

import io
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SVG = ROOT / "installer" / "icon.svg"
ICO = ROOT / "installer" / "icon.ico"
PNG = ROOT / "installer" / "icon.png"
SITE_ASSETS = ROOT / "site" / "assets"

#: Tamaños que Windows espera dentro de un .ico de aplicación.
ICO_SIZES = [16, 24, 32, 48, 64, 128, 256]
MASTER_PX = 512


def _rasterize_cairosvg(svg_bytes: bytes, px: int) -> bytes | None:
    try:
        import cairosvg  # type: ignore
    except Exception:
        return None
    return cairosvg.svg2png(bytestring=svg_bytes, output_width=px, output_height=px)


#: La QGuiApplication de Qt debe vivir durante todo el proceso: crearla y
#: destruirla por cada rasterizado hace que Qt caiga con segfault.
_QT_APP = None


def _rasterize_qt(svg_path: Path, px: int) -> bytes | None:
    """Respaldo con QtSvg — PySide6 ya es dependencia de la app desktop."""
    global _QT_APP
    try:
        from PySide6.QtCore import QBuffer, QByteArray, Qt
        from PySide6.QtGui import QGuiApplication, QImage, QPainter
        from PySide6.QtSvg import QSvgRenderer
    except Exception:
        return None

    import os

    os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
    if _QT_APP is None:
        _QT_APP = QGuiApplication.instance() or QGuiApplication([])

    renderer = QSvgRenderer(str(svg_path))
    image = QImage(px, px, QImage.Format.Format_ARGB32)
    image.fill(Qt.GlobalColor.transparent)
    painter = QPainter(image)
    renderer.render(painter)
    painter.end()

    # El QByteArray debe tener nombre: si se pasa como temporal, Python lo
    # libera y QBuffer queda con un puntero colgante (segfault al escribir).
    payload = QByteArray()
    buffer = QBuffer(payload)
    buffer.open(QBuffer.OpenModeFlag.WriteOnly)
    image.save(buffer, "PNG")
    buffer.close()
    return bytes(payload)


def rasterize(px: int) -> bytes:
    svg_bytes = SVG.read_bytes()
    data = _rasterize_cairosvg(svg_bytes, px)
    if data is None:
        data = _rasterize_qt(SVG, px)
    if data is None:
        raise RuntimeError(
            "No hay rasterizador disponible: instalá cairosvg o PySide6 "
            "(pip install cairosvg)"
        )
    return data


def main() -> int:
    if not SVG.exists():
        print(f"[ERROR] falta el SVG maestro: {SVG}")
        return 1

    from PIL import Image  # pillow ya está en requirements.txt

    master = Image.open(io.BytesIO(rasterize(MASTER_PX))).convert("RGBA")

    # PNG maestro.
    PNG.parent.mkdir(parents=True, exist_ok=True)
    master.save(PNG, format="PNG")
    print(f"[ok] {PNG.relative_to(ROOT)}  ({MASTER_PX}x{MASTER_PX})")

    # ICO multi-resolución: cada tamaño se rasteriza aparte para que los
    # iconos chicos no salgan de un downscale borroso del de 512.
    frames = [
        Image.open(io.BytesIO(rasterize(px))).convert("RGBA") for px in ICO_SIZES
    ]
    frames[-1].save(
        ICO,
        format="ICO",
        sizes=[(px, px) for px in ICO_SIZES],
        append_images=frames[:-1],
    )
    print(f"[ok] {ICO.relative_to(ROOT)}  ({', '.join(str(s) for s in ICO_SIZES)})")

    # Assets del portal.
    SITE_ASSETS.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SVG, SITE_ASSETS / "icon.svg")
    master.save(SITE_ASSETS / "icon.png", format="PNG")
    master.resize((180, 180), Image.LANCZOS).save(
        SITE_ASSETS / "apple-touch-icon.png", format="PNG"
    )
    print(f"[ok] {(SITE_ASSETS / 'icon.svg').relative_to(ROOT)}")
    print(f"[ok] {(SITE_ASSETS / 'icon.png').relative_to(ROOT)}")
    print(f"[ok] {(SITE_ASSETS / 'apple-touch-icon.png').relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
