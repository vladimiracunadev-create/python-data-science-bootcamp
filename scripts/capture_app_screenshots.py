"""Captura screenshots reales de la app Windows y los deja en docs/screenshots/.

Qué resuelve:
    Dos necesidades distintas con una sola fuente:

    1. **Verificación** — mirar la ventana de verdad después de tocar la UI, en
       vez de confiar en que "compila, luego se ve bien". Se capturan las
       vistas críticas en los dos temas.
    2. **Documentación** — las mismas imágenes alimentan el README, la guía del
       producto y la página de capturas de GitHub Pages.

    Las capturas se toman de la ``MainWindow`` real cargando clases reales del
    currículo, no de un mock: si el render se rompe, la captura lo muestra.

Uso:
    python scripts/capture_app_screenshots.py            # todas
    python scripts/capture_app_screenshots.py --list     # ver qué genera

Requiere sesión gráfica de Windows (usa el backend ``windows`` de Qt; el
backend ``offscreen`` no tiene fuentes instaladas y sale todo en cajitas).
"""

from __future__ import annotations

import argparse
import os
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

OUT_DIR = ROOT / "docs" / "screenshots"
SITE_DIR = ROOT / "site" / "assets" / "screenshots"

WINDOW_W, WINDOW_H = 1500, 950


@dataclass(frozen=True)
class Shot:
    """Una captura: qué clase abrir, en qué tema, qué pestaña y cuánto bajar."""

    name: str
    slug_index: int
    theme: str
    tab: int  # 0 = Clase (README), 1 = Notebook
    scroll: int
    caption: str


SHOTS: list[Shot] = [
    Shot(
        "01-clase-readme-claro",
        0,
        "light",
        0,
        0,
        "Vista de clase: cabecera fija, columna de lectura y README en HTML.",
    ),
    Shot(
        "02-clase-tabla-claro",
        0,
        "light",
        0,
        700,
        "Tablas del temario renderizadas como tabla real, no como texto corrido.",
    ),
    Shot(
        "03-notebook-claro",
        0,
        "light",
        1,
        600,
        "Pestaña Notebook: celdas de código con resaltado de sintaxis y outputs.",
    ),
    Shot(
        "04-clase-readme-oscuro",
        25,
        "dark",
        0,
        900,
        "Tema oscuro: la paleta se aplica también al contenido de la clase.",
    ),
    Shot(
        "05-notebook-oscuro",
        61,
        "dark",
        1,
        400,
        "Notebook en tema oscuro con la misma columna de lectura.",
    ),
    Shot(
        "06-buscador",
        0,
        "light",
        0,
        0,
        "Buscador incremental sobre las 232 clases del árbol.",
    ),
]


def capture(shots: list[Shot], out_dir: Path, mirror_to_site: bool = True) -> int:
    os.environ.setdefault("QT_QPA_PLATFORM", "windows")

    from PySide6.QtWidgets import QApplication

    from app_desktop.main_window import MainWindow

    app = QApplication.instance() or QApplication([])
    out_dir.mkdir(parents=True, exist_ok=True)

    window = MainWindow()
    window.resize(WINDOW_W, WINDOW_H)
    window.show()
    _pump(app)

    total = len(window._flat_class_slugs)
    if total == 0:
        print("[ERROR] el currículo vino vacío — no hay nada que capturar")
        return 1

    written = 0
    for shot in shots:
        window._set_theme(shot.theme)
        _pump(app)
        window._open_class(window._flat_class_slugs[min(shot.slug_index, total - 1)])
        window._tabs.setCurrentIndex(shot.tab)
        _pump(app)

        if shot.name.endswith("buscador"):
            window._search.setText("pandas")
            _pump(app)
        else:
            window._search.setText("")

        if shot.scroll:
            if shot.tab == 0:
                window._readme_view._browser.verticalScrollBar().setValue(shot.scroll)
            else:
                window._notebook_view._scroll.verticalScrollBar().setValue(shot.scroll)
            _pump(app)

        target = out_dir / f"{shot.name}.png"
        if not window.grab().save(str(target)):
            print(f"[ERROR] no se pudo guardar {target}")
            return 1
        size_kb = target.stat().st_size // 1024
        print(f"[ok] {target.relative_to(ROOT)}  ({size_kb} KB) — {shot.caption}")
        written += 1

    if mirror_to_site:
        SITE_DIR.mkdir(parents=True, exist_ok=True)
        import shutil

        for png in sorted(out_dir.glob("*.png")):
            shutil.copy2(png, SITE_DIR / png.name)
        print(f"[ok] copiadas {written} capturas a {SITE_DIR.relative_to(ROOT)}")

    return 0


def _pump(app, rounds: int = 8) -> None:
    """Deja que Qt procese layout, render y scroll antes de capturar."""
    for _ in range(rounds):
        app.processEvents()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--list", action="store_true", help="solo listar las capturas")
    parser.add_argument(
        "--out", type=Path, default=OUT_DIR, help="directorio de salida"
    )
    parser.add_argument(
        "--no-site", action="store_true", help="no copiar a site/assets/screenshots"
    )
    args = parser.parse_args()

    if args.list:
        for shot in SHOTS:
            print(f"{shot.name}.png  [{shot.theme}/tab {shot.tab}]  — {shot.caption}")
        return 0

    return capture(SHOTS, args.out, mirror_to_site=not args.no_site)


if __name__ == "__main__":
    raise SystemExit(main())
