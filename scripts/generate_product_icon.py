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
        mobile/assets/*.png  — icono, adaptive-icon, favicon y splash de la app
                               Android (venían con el robot genérico de Expo)

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
MOBILE_ASSETS = ROOT / "mobile" / "assets"

#: Fondo de la placa del icono. Se usa para el splash y para el relleno del
#: adaptive-icon de Android, que recorta la imagen a la forma del launcher.
BRAND_BG = (10, 32, 41)  # #0a2029, el mismo del SVG

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

    write_mobile_assets(master, Image)
    return 0


def write_mobile_assets(master, Image) -> None:
    """Assets de la app Android (Expo). Traían el robot genérico del template.

    Android recorta el ``adaptive-icon`` a la forma del launcher (círculo,
    squircle…), así que el motivo va con margen dentro de un lienzo de 1024 px
    sobre el color de marca: sin ese margen el recorte se come los lazos.
    """
    if not MOBILE_ASSETS.exists():
        print("[skip] mobile/assets no existe — se omiten los assets Android")
        return

    icon_1024 = Image.open(io.BytesIO(rasterize(1024))).convert("RGBA")
    icon_1024.save(MOBILE_ASSETS / "icon.png", format="PNG")

    # Adaptive icon: 66% de zona segura centrada sobre el color de marca.
    adaptive = Image.new("RGBA", (1024, 1024), (*BRAND_BG, 255))
    inner = icon_1024.resize((676, 676), Image.LANCZOS)
    adaptive.paste(inner, (174, 174), inner)
    adaptive.save(MOBILE_ASSETS / "adaptive-icon.png", format="PNG")

    master.resize((196, 196), Image.LANCZOS).save(
        MOBILE_ASSETS / "favicon.png", format="PNG"
    )

    # Splash: el icono centrado sobre el color de marca, en 1284x2778 (retrato).
    splash = Image.new("RGBA", (1284, 2778), (*BRAND_BG, 255))
    mark = icon_1024.resize((420, 420), Image.LANCZOS)
    splash.paste(mark, ((1284 - 420) // 2, (2778 - 420) // 2), mark)
    splash.save(MOBILE_ASSETS / "splash.png", format="PNG")

    for name in ("icon.png", "adaptive-icon.png", "favicon.png", "splash.png"):
        print(f"[ok] {(MOBILE_ASSETS / name).relative_to(ROOT)}")

    write_android_launcher_icons(icon_1024, Image)


#: Densidades del launcher de Android y el lado del icono en px para cada una.
#: `ic_launcher` es el icono legacy (cuadrado), `ic_launcher_round` el redondo y
#: `ic_launcher_foreground` la capa recortable del adaptive icon (API 26+).
ANDROID_DENSITIES = {
    "mdpi": 48,
    "hdpi": 72,
    "xhdpi": 96,
    "xxhdpi": 144,
    "xxxhdpi": 192,
}


def write_android_launcher_icons(icon_1024, Image) -> None:
    """Regenera los ``mipmap-*`` nativos del proyecto Android.

    El proyecto vive prebuildeado (``mobile/android/`` está commiteado), así que
    los iconos del launcher NO se derivan de ``app.json`` en cada build: son
    PNGs versionados. Sin este paso el APK seguiría saliendo con el robot verde
    del template aunque ``mobile/assets/icon.png`` ya tenga el del producto.
    """
    res_dir = ROOT / "mobile" / "android" / "app" / "src" / "main" / "res"
    if not res_dir.exists():
        print("[skip] no hay proyecto Android prebuildeado")
        return

    from PIL import ImageDraw

    for density, size in ANDROID_DENSITIES.items():
        target = res_dir / f"mipmap-{density}"
        if not target.exists():
            continue

        square = icon_1024.resize((size, size), Image.LANCZOS)
        square.save(target / "ic_launcher.png", format="PNG")

        # Variante redonda: el mismo icono recortado a círculo.
        round_icon = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        mask = Image.new("L", (size * 4, size * 4), 0)
        ImageDraw.Draw(mask).ellipse((0, 0, size * 4 - 1, size * 4 - 1), fill=255)
        round_icon.paste(square, (0, 0), mask.resize((size, size), Image.LANCZOS))
        round_icon.save(target / "ic_launcher_round.png", format="PNG")

        # Capa foreground del adaptive icon: el sistema recorta hasta un 33%,
        # así que el motivo va al 66% centrado sobre lienzo transparente.
        fg = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        inner = max(1, int(size * 0.66))
        fg.paste(
            icon_1024.resize((inner, inner), Image.LANCZOS),
            ((size - inner) // 2, (size - inner) // 2),
            icon_1024.resize((inner, inner), Image.LANCZOS),
        )
        fg.save(target / "ic_launcher_foreground.png", format="PNG")

        print(f"[ok] mobile/android/.../mipmap-{density}/  ({size}px x3)")


if __name__ == "__main__":
    raise SystemExit(main())
