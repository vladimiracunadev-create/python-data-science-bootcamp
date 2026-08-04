"""Verifica que no queden enlaces rotos en el sitio ni en la app.

Qué resuelve:
    Los enlaces del producto se construyen en tres lugares distintos y se
    rompen en silencio: el sitio estático de GitHub Pages (rutas relativas
    entre 3 niveles de carpetas), los README de clase (que enlazan su PDF y su
    PPTX por nombre de archivo) y la app de escritorio (que arma URLs raw de
    GitHub a partir del slug). Un nombre de archivo que cambia deja un 404 que
    nadie nota hasta que un alumno hace clic.

    Este script revisa las tres capas contra el filesystem, sin red:

      [sitio]   cada href/src relativo de site/**/*.html existe en disco
      [clases]  cada enlace relativo de classes/**/README.md existe
      [app]     las URLs que arma app_desktop.curriculum apuntan a archivos
                que EXISTEN en el repo (se valida la ruta local equivalente)

Uso:
    python scripts/check_links.py            # revisa todo
    python scripts/check_links.py --site     # solo el sitio
    python scripts/check_links.py --app      # solo las URLs de la app

Salida: código 0 si no hay enlaces rotos, 1 si hay al menos uno.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

# La consola de Windows usa cp1252 y revienta con las flechas del reporte.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SITE = ROOT / "site"
CLASSES = ROOT / "classes"

#: Prefijos que este verificador no resuelve (son externos o del navegador).
SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "data:", "#", "javascript:")

_RE_HTML_LINK = re.compile(r'(?:href|src)="([^"]+)"')
_RE_MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def _is_external(target: str) -> bool:
    return target.startswith(SKIP_PREFIXES) or not target.strip()


def _resolve(base_file: Path, target: str) -> Path:
    """Resuelve un enlace relativo respecto del archivo que lo contiene."""
    path = unquote(urlparse(target).path)
    if path.startswith("/"):
        # Ruta absoluta del sitio: se cuelga de site/.
        return SITE / path.lstrip("/")
    return (base_file.parent / path).resolve()


def _exists(candidate: Path) -> bool:
    if candidate.exists():
        return True
    # Un enlace a una carpeta sirve si esa carpeta tiene index.html.
    return (candidate / "index.html").exists()


def check_site() -> list[str]:
    """Enlaces y assets relativos de las páginas generadas del portal."""
    problems: list[str] = []
    pages = sorted(SITE.rglob("*.html"))
    if not pages:
        return ["[sitio] no hay HTML en site/ — ¿corriste generate_site_curriculum.py?"]

    for page in pages:
        html_text = page.read_text(encoding="utf-8", errors="replace")
        for target in _RE_HTML_LINK.findall(html_text):
            if _is_external(target):
                continue
            if not _exists(_resolve(page, target)):
                problems.append(
                    f"[sitio] {page.relative_to(ROOT)} → {target} (no existe)"
                )
    print(f"[sitio] {len(pages)} páginas revisadas")
    return problems


def check_class_readmes() -> list[str]:
    """Enlaces relativos dentro de los README de clase (PDF, PPTX, notebook)."""
    problems: list[str] = []
    readmes = sorted(CLASSES.rglob("README.md"))
    for readme in readmes:
        text = readme.read_text(encoding="utf-8", errors="replace")
        for target in _RE_MD_LINK.findall(text):
            if _is_external(target):
                continue
            if not _exists(_resolve(readme, target)):
                problems.append(
                    f"[clases] {readme.relative_to(ROOT)} → {target} (no existe)"
                )
    print(f"[clases] {len(readmes)} README revisados")
    return problems


def check_app_urls() -> list[str]:
    """Las URLs que arma la app deben corresponder a archivos reales del repo.

    No se hace red: cada URL raw de GitHub se traduce a su ruta local y se
    comprueba que exista. Si el nombre del PDF de una clase cambia, acá salta.
    """
    from app_desktop import curriculum

    problems: list[str] = []
    tree = curriculum.list_curriculum()
    n_classes = 0

    for part in tree:
        for cls in part["classes"]:
            slug = cls["slug"]
            n_classes += 1

            for label, url in (
                ("PDF", curriculum.class_pdf_url(slug)),
                ("PPTX", curriculum.class_pptx_url(slug)),
            ):
                rel = url.split("/raw/main/", 1)[-1]
                if not (ROOT / rel).exists():
                    problems.append(f"[app] {slug}: URL de {label} apunta a {rel} (no existe)")

            # La carpeta de la clase en el repo y su página en Pages.
            repo_rel = curriculum.class_repo_url(slug).split("/tree/main/", 1)[-1]
            if not (ROOT / repo_rel).exists():
                problems.append(f"[app] {slug}: carpeta {repo_rel} no existe")

            page_rel = curriculum.class_page_url(slug).split("/python-data-science-program/", 1)[-1]
            if not (SITE / page_rel / "index.html").exists():
                problems.append(
                    f"[app] {slug}: página de Pages site/{page_rel}index.html no existe"
                )

    icon = curriculum.app_icon_path()
    if icon is None:
        problems.append("[app] no hay icono de producto — corré scripts/generate_product_icon.py")

    print(f"[app] {n_classes} clases × 4 enlaces revisados")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", action="store_true", help="solo el sitio")
    parser.add_argument("--clases", action="store_true", help="solo los README")
    parser.add_argument("--app", action="store_true", help="solo las URLs de la app")
    args = parser.parse_args()

    run_all = not (args.site or args.clases or args.app)
    problems: list[str] = []

    if run_all or args.site:
        problems += check_site()
    if run_all or args.clases:
        problems += check_class_readmes()
    if run_all or args.app:
        problems += check_app_urls()

    if problems:
        print(f"\n[FALLO] {len(problems)} enlaces rotos:\n")
        for line in problems[:200]:
            print(f"  {line}")
        if len(problems) > 200:
            print(f"  … y {len(problems) - 200} más")
        return 1

    print("\n[OK] no hay enlaces rotos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
