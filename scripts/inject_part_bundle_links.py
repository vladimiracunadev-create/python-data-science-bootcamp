"""Inyecta una sección de Material descargable en cada README de Parte.

Qué resuelve:
    Cada `classes/parte-N-slug/README.md` ahora debe linkear al bundle PDF +
    PPTX consolidado de esa parte (generado por
    ``scripts/generate_part_bundles.py``). Esta sección se inserta antes del
    footer ``> [⬅️ Volver al programa]…`` para no romper la navegación.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES_DIR = ROOT / "classes"

MARKER = "## 📥 Material descargable — parte completa"
EXISTING_BLOCK_RE = re.compile(
    r"## 📥 Material descargable — parte completa\n.*?(?=^---|\Z)",
    flags=re.MULTILINE | re.DOTALL,
)
FOOTER_DIVIDER_RE = re.compile(r"^---\n\n> \[⬅️ Volver al programa\]", re.MULTILINE)


def section(part_slug: str) -> str:
    """Construye la sección a inyectar para una parte concreta."""
    pdf = f"../../docs/pdfs/parts/{part_slug}-completa.pdf"
    pptx = f"../../docs/presentaciones/parts/{part_slug}-completa.pptx"
    return (
        f"{MARKER}\n\n"
        f"Materiales consolidados con TODAS las clases de esta parte "
        f"(útiles para revisar offline o imprimir el bloque entero):\n\n"
        f"- 📄 [Guía PDF — parte completa]({pdf}) — todas las clases concatenadas con headings demoteados.\n"
        f"- 🎞️ [Presentación PPTX — parte completa]({pptx}) — portada + TOC + slides de cada clase.\n\n"
    )


def inject(readme: Path, part_slug: str, dry_run: bool = False) -> str:
    text = readme.read_text(encoding="utf-8")
    block = section(part_slug)

    if MARKER in text:
        new_text = EXISTING_BLOCK_RE.sub(block, text, count=1)
        status = "replaced"
    else:
        match = FOOTER_DIVIDER_RE.search(text)
        if match:
            new_text = text[: match.start()] + block + text[match.start():]
            status = "inserted"
        else:
            new_text = text.rstrip() + "\n\n" + block.rstrip() + "\n"
            status = "appended"

    if not dry_run and new_text != text:
        readme.write_text(new_text, encoding="utf-8")
    return status


def main() -> None:
    parser = argparse.ArgumentParser(description="Inyecta sección bundle en READMEs de Parte.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    parts = sorted(d for d in CLASSES_DIR.glob("parte-*") if d.is_dir())
    print(f"Procesando {len(parts)} READMEs de Parte...")
    counters = {"replaced": 0, "inserted": 0, "appended": 0}
    for part in parts:
        readme = part / "README.md"
        if not readme.exists():
            continue
        status = inject(readme, part.name, dry_run=args.dry_run)
        counters[status] += 1
    print(
        f"OK · inserted={counters['inserted']} · replaced={counters['replaced']} · "
        f"appended={counters['appended']}"
        + ("  [DRY-RUN]" if args.dry_run else "")
    )


if __name__ == "__main__":
    main()
