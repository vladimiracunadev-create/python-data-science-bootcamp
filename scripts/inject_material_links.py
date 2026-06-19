"""Inyecta una sección de Material descargable en cada README de clase.

Qué resuelve:
    Las 232 clases del currículo tienen PDF + PPTX generados (v3.7.0+), pero
    ningún README las enlaza. Este script agrega una sección
    ``## 📥 Material descargable`` justo antes de ``## ➡️ Siguiente clase``
    con links relativos al PDF y al PPTX que viven en la misma carpeta.

    Idempotente: si la sección ya existe la reemplaza. Si no hay
    ``## ➡️ Siguiente clase`` (última clase, 232), la agrega al final.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES_DIR = ROOT / "classes"

MARKER = "## 📥 Material descargable"
NEXT_HEADING_RE = re.compile(r"^## ➡️ Siguiente clase", re.MULTILINE)
EXISTING_BLOCK_RE = re.compile(
    r"## 📥 Material descargable\n.*?(?=^## |\Z)",
    flags=re.MULTILINE | re.DOTALL,
)


def class_basename(class_dir: Path) -> str:
    """Devuelve el nombre de la carpeta de clase (ej. ``223-tipos-...``)."""
    return class_dir.name


def material_section(class_dir: Path) -> str:
    """Construye la sección a inyectar para una clase concreta."""
    base = class_basename(class_dir)
    pdf = f"clase-{base}-guia-explicativa.pdf"
    pptx = f"clase-{base}-presentacion.pptx"
    return (
        f"{MARKER}\n\n"
        f"- 📄 [Guía explicativa (PDF)](./{pdf}) — versión imprimible con todo "
        f"el contenido de la clase.\n"
        f"- 🎞️ [Presentación (PPTX)](./{pptx}) — deck PowerPoint listo para "
        f"proyectar en clase.\n"
        f"- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde "
        f"el laboratorio del programa o desde Jupyter.\n\n"
    )


def discover_class_readmes() -> list[Path]:
    """Lista los README.md de cada clase v3 ordenados por (parte, número)."""
    readmes: list[Path] = []
    for part in sorted(CLASSES_DIR.glob("parte-*")):
        if not part.is_dir():
            continue
        for class_dir in sorted(d for d in part.iterdir() if d.is_dir() and d.name[0].isdigit()):
            readme = class_dir / "README.md"
            if readme.exists():
                readmes.append(readme)
    return readmes


def inject(readme: Path, dry_run: bool = False) -> str:
    """Inserta o reemplaza la sección de material. Devuelve estado."""
    text = readme.read_text(encoding="utf-8")
    section = material_section(readme.parent)

    # Caso 1: la sección ya existe → reemplazar.
    if MARKER in text:
        new_text = EXISTING_BLOCK_RE.sub(section, text, count=1)
        status = "replaced"
    else:
        match = NEXT_HEADING_RE.search(text)
        if match:
            # Caso 2: insertar antes de "➡️ Siguiente clase".
            new_text = text[: match.start()] + section + text[match.start():]
            status = "inserted"
        else:
            # Caso 3: última clase (sin Siguiente) → agregar al final.
            new_text = text.rstrip() + "\n\n" + section.rstrip() + "\n"
            status = "appended"

    if not dry_run and new_text != text:
        readme.write_text(new_text, encoding="utf-8")
    return status


def main() -> None:
    parser = argparse.ArgumentParser(description="Inyecta sección Material en READMEs de clase.")
    parser.add_argument("--dry-run", action="store_true", help="Sin escribir cambios.")
    args = parser.parse_args()

    readmes = discover_class_readmes()
    print(f"Procesando {len(readmes)} READMEs...")

    counters = {"replaced": 0, "inserted": 0, "appended": 0}
    for readme in readmes:
        status = inject(readme, dry_run=args.dry_run)
        counters[status] += 1

    print(
        f"OK · inserted={counters['inserted']} · "
        f"replaced={counters['replaced']} · appended={counters['appended']}"
        + ("  [DRY-RUN]" if args.dry_run else "")
    )


if __name__ == "__main__":
    main()
