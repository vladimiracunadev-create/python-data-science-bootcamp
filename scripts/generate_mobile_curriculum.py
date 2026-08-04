"""Generate the embedded curriculum data for the React Native app.

Walks ``classes/parte-*/NNN-*/README.md`` — the single source of truth for the
232 classes — and emits ``mobile/src/data/classes.js`` with three exports:

    PARTS             — the 9 parts, with their class ranges and progress totals
    CLASSES           — the 232 classes, flat and ordered by number
    CLASSES_BY_PART   — the same classes indexed by part slug

The app embeds this file in the JS bundle so the curriculum works offline; the
only thing that needs a network is the Colab link.

Section parsing is anchored on the heading *emoji* rather than its wording: the
titles drift across parts (``🗺️ Temas`` vs ``🗺️ Fases del capstone``,
``📂 Dataset / recursos`` vs ``📂 Recursos``) but the emoji is stable in all 232
files. Re-run after any curriculum edit; ``tests/test_mobile_curriculum.py``
fails if the generated file drifts from the markdown.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CLASSES_DIR = ROOT / "classes"
OUT_FILE = ROOT / "mobile" / "src" / "data" / "classes.js"


def _project_version() -> str:
    """Versión canónica del proyecto, leída de ``pyproject.toml``.

    Estaba hardcodeada en la plantilla de abajo, así que cada bump dejaba el
    bundle móvil anunciando la versión anterior hasta que alguien se acordaba
    de editarla a mano.
    """
    text = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    return match.group(1) if match else "0.0.0"


PROJECT_VERSION = _project_version()

# Colab resolves notebooks straight from GitHub, so the branch has to be the
# one that actually exists on the remote (``main``) — see mobile/src/utils/colab.js.
GITHUB_USER = "vladimiracunadev-create"
GITHUB_REPO = "python-data-science-program"
GITHUB_BRANCH = "main"

# Part metadata mirrors scripts/generate_site_curriculum.py so the app, the web
# portal and the desktop app describe the curriculum identically.
PART_META: dict[str, tuple[str, str, str]] = {
    "parte-0-prerrequisitos": (
        "Prerrequisitos",
        "Python, NumPy, pandas, viz, SQL, NoSQL, APIs",
        "Basico",
    ),
    "parte-1-machine-learning-clasico": (
        "ML clásico",
        "Regresión, clasificación, ensembles, no supervisado",
        "Intermedio",
    ),
    "parte-2-deep-learning": (
        "Deep Learning",
        "Keras, TF, CNN, RNN, Transformers, RL, despliegue",
        "Avanzado",
    ),
    "parte-3-estadistica-inferencial": (
        "Estadística inferencial",
        "Hipótesis, A/B testing, inferencia causal, Bayes",
        "Intermedio-Avanzado",
    ),
    "parte-4-mlops": (
        "MLOps",
        "Docker, CI/CD, MLflow, monitoreo, interpretabilidad",
        "Avanzado",
    ),
    "parte-5-ingenieria-de-datos": (
        "Ingeniería de datos",
        "Spark, Airflow, lakehouses, streaming",
        "Avanzado",
    ),
    "parte-6-sistemas-de-recomendacion": (
        "Recomendadores",
        "Filtrado colaborativo, factorización, secuenciales",
        "Intermedio-Avanzado",
    ),
    "parte-7-etica-fairness-privacidad": (
        "Ética, fairness, privacidad",
        "Sesgo, explicabilidad, marcos normativos",
        "Intermedio",
    ),
    "parte-8-capstones": (
        "Capstones",
        "Proyectos integradores end-to-end",
        "Integrador",
    ),
}

# ── Regexes ──────────────────────────────────────────────────────────────────

TITLE_RE = re.compile(r"^#\s+Clase\s+(\d{1,3})\s*[—–-]\s*(.+)$", re.MULTILINE)
DURATION_RE = re.compile(r"Duración estimada:\s*\*\*(.+?)\*\*")
PART_DIR_RE = re.compile(r"^parte-(\d+)")
CLASS_DIR_RE = re.compile(r"^(\d{1,3})-(.+)$")

# Inline markdown we strip so the app renders plain text in <Text> nodes.
LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\)")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
ITALIC_RE = re.compile(r"(?<!\*)\*([^*]+)\*(?!\*)")
CODE_RE = re.compile(r"`([^`]+)`")
FENCE_RE = re.compile(r"^```(\w*)\n(.*?)^```", re.MULTILINE | re.DOTALL)

BULLET_RE = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+(.*)$")
# Part 0 numbers its exercises as bold text (``**1.** **Atajos...**``) rather
# than as a markdown list, so it needs its own pattern.
BOLD_NUM_RE = re.compile(r"^\s*\*\*(\d+)[.)]\*\*\s*(.*)$")


def strip_inline(text: str) -> str:
    """Flatten inline markdown to plain text.

    Qué resuelve:
        React Native ``<Text>`` renders literally, so leftover ``**`` or link
        syntax would show up as visible noise in the app.
    """
    text = LINK_RE.sub(r"\1", text)
    text = BOLD_RE.sub(r"\1", text)
    text = ITALIC_RE.sub(r"\1", text)
    text = CODE_RE.sub(r"\1", text)
    return re.sub(r"\s+", " ", text).strip()


def section(body: str, emoji: str) -> str:
    """Return the raw body of the ``## <emoji> ...`` section, or ``""``.

    Anchors on the emoji because the heading wording varies across parts while
    the emoji does not.
    """
    pattern = re.compile(
        rf"^##\s+{re.escape(emoji)}[^\n]*\n(.*?)(?=^##\s|\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(body)
    return match.group(1).strip() if match else ""


def list_items(block: str, limit: int | None = None) -> list[str]:
    """Extract bullet or numbered list items from a markdown block.

    Handles both shapes the curriculum uses (``1. **Verificar** ...`` in the
    early parts, ``- Estructurar ...`` in the capstones) and drops nested
    continuation lines, which are prose rather than separate items.
    """
    items: list[str] = []
    for line in block.splitlines():
        if line.startswith(("  ", "\t")):
            continue  # nested continuation, belongs to the previous item
        bold_num = BOLD_NUM_RE.match(line)
        if bold_num:
            cleaned = strip_inline(bold_num.group(2))
            if cleaned:
                items.append(cleaned)
            continue

        match = BULLET_RE.match(line)
        if not match:
            continue
        cleaned = strip_inline(match.group(1))
        if cleaned:
            items.append(cleaned)
    return items[:limit] if limit else items


def table_column(block: str, index: int = 1) -> list[str]:
    """Extract one column from a markdown table, skipping header and separator.

    The ``🗺️`` section is a ``| # | Tema | Por qué importa |`` table in every
    class; column 1 holds the topic name.
    """
    rows: list[str] = []
    for line in block.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) <= index:
            continue
        if set(cells[0]) <= set("-: "):
            continue  # separator row
        if cells[0] in {"#", "Fase", "Componente"}:
            continue  # header row
        value = strip_inline(cells[index])
        if value:
            rows.append(value)
    return rows


def first_sentence(text: str, max_len: int = 220) -> str:
    """Trim a paragraph down to a card-sized description."""
    text = strip_inline(text)
    match = re.search(r"^(.+?[.!?])(?:\s|$)", text)
    candidate = match.group(1) if match else text
    if len(candidate) > max_len:
        candidate = candidate[: max_len - 1].rstrip() + "…"
    return candidate


def paragraphs(block: str) -> str:
    """Collapse a section body into plain prose, dropping list syntax."""
    lines = [ln for ln in block.splitlines() if ln.strip()]
    return strip_inline(" ".join(lines))


def code_examples(body: str, class_id: str) -> list[dict[str, str]]:
    """Extract fenced code blocks as documented examples.

    Only a handful of classes embed code in the README (the practice lives in
    the notebook), so this is usually empty — ``ClassScreen`` renders a fallback
    card in that case and the Práctica tab falls back to ``exercises``.
    """
    examples: list[dict[str, str]] = []
    for i, match in enumerate(FENCE_RE.finditer(body), start=1):
        language = match.group(1) or "python"
        code = match.group(2).rstrip()
        if not code.strip():
            continue
        examples.append(
            {
                "id": f"{class_id}-code-{i}",
                "title": f"Bloque {i}",
                "explanation": "Código incluido en el material de la clase.",
                "schema": f"{language} · {len(code.splitlines())} líneas",
                "language": language,
                "code": code,
            }
        )
    return examples


def parse_class(readme: Path, part_slug: str) -> dict[str, Any]:
    """Build one class record from its README."""
    body = readme.read_text(encoding="utf-8")
    folder = readme.parent.name

    dir_match = CLASS_DIR_RE.match(folder)
    if not dir_match:
        raise ValueError(f"Carpeta de clase con formato inesperado: {folder}")
    number = int(dir_match.group(1))

    title_match = TITLE_RE.search(body)
    if not title_match:
        raise ValueError(f"README sin encabezado '# Clase NNN — ...': {readme}")
    title = strip_inline(title_match.group(2))

    duration_match = DURATION_RE.search(body)
    duration = strip_inline(duration_match.group(1)) if duration_match else "90 min"

    objetivo = section(body, "🎯")
    outcomes = list_items(section(body, "📚"))
    topics = table_column(section(body, "🗺️")) or list_items(section(body, "🗺️"))
    materials = list_items(section(body, "📂"), limit=12)
    exercises = list_items(section(body, "🧪"))

    class_id = f"{part_slug}/{folder}"
    notebook_path = f"classes/{part_slug}/{folder}/notebook.ipynb"
    has_notebook = (readme.parent / "notebook.ipynb").exists()

    return {
        "id": class_id,
        "number": number,
        "slug": folder,
        "partSlug": part_slug,
        "title": title,
        "description": first_sentence(objetivo),
        "level": PART_META[part_slug][2],
        "duration": duration,
        "theory": paragraphs(objetivo),
        "outcomes": outcomes,
        "topics": topics,
        "materials": materials or ["Material de la clase en el repositorio"],
        "exercises": exercises,
        "codeExamples": code_examples(body, class_id),
        "colabUrl": (
            f"https://colab.research.google.com/github/{GITHUB_USER}/{GITHUB_REPO}"
            f"/blob/{GITHUB_BRANCH}/{notebook_path}"
            if has_notebook
            else None
        ),
    }


def collect() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Walk the curriculum and return ``(parts, classes)`` ordered by number."""
    parts: list[dict[str, Any]] = []
    classes: list[dict[str, Any]] = []

    part_dirs = sorted(
        (d for d in CLASSES_DIR.iterdir() if d.is_dir() and PART_DIR_RE.match(d.name)),
        key=lambda d: int(PART_DIR_RE.match(d.name).group(1)),  # type: ignore[union-attr]
    )

    for part_dir in part_dirs:
        slug = part_dir.name
        if slug not in PART_META:
            raise ValueError(f"Parte sin metadata declarada en PART_META: {slug}")

        readmes = sorted(
            (p / "README.md" for p in part_dir.iterdir() if p.is_dir()),
            key=lambda p: p.parent.name,
        )
        readmes = [r for r in readmes if r.exists()]

        part_classes = [parse_class(r, slug) for r in readmes]
        part_classes.sort(key=lambda c: c["number"])
        classes.extend(part_classes)

        title, subtitle, level = PART_META[slug]
        parts.append(
            {
                "id": slug,
                "number": int(PART_DIR_RE.match(slug).group(1)),  # type: ignore[union-attr]
                "title": title,
                "subtitle": subtitle,
                "level": level,
                "classCount": len(part_classes),
                "firstClass": part_classes[0]["number"] if part_classes else None,
                "lastClass": part_classes[-1]["number"] if part_classes else None,
            }
        )

    classes.sort(key=lambda c: c["number"])
    return parts, classes


def render(parts: list[dict[str, Any]], classes: list[dict[str, Any]]) -> str:
    """Render the generated ES module."""
    by_part = {
        part["id"]: [c["id"] for c in classes if c["partSlug"] == part["id"]]
        for part in parts
    }

    def dump(value: Any) -> str:
        return json.dumps(value, ensure_ascii=False, indent=2)

    return f"""// GENERADO AUTOMÁTICAMENTE — no editar a mano.
//
// Fuente: classes/parte-*/NNN-*/README.md (las 232 clases del currículo v3).
// Regenerar con:  python scripts/generate_mobile_curriculum.py
//
// El contenido va embebido en el bundle JS para que el programa se pueda leer
// sin conexión; solo los enlaces a Colab requieren internet.

export const CURRICULUM_VERSION = "v{PROJECT_VERSION}";

export const PARTS = {dump(parts)};

export const CLASSES = {dump(classes)};

export const CLASS_IDS_BY_PART = {dump(by_part)};

/** Devuelve las clases de una parte, en orden de numeración. */
export const classesForPart = (partId) =>
  CLASSES.filter((item) => item.partSlug === partId);

/** Busca una clase por su id (`parte-N-slug/NNN-slug`). */
export const classById = (id) => CLASSES.find((item) => item.id === id);

export const TOTAL_CLASSES = {len(classes)};
export const TOTAL_PARTS = {len(parts)};
"""


def main() -> int:
    if not CLASSES_DIR.exists():
        print(f"No existe el directorio del currículo: {CLASSES_DIR}", file=sys.stderr)
        return 1

    parts, classes = collect()

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(render(parts, classes), encoding="utf-8")

    size_kb = OUT_FILE.stat().st_size / 1024
    print(f"{OUT_FILE.relative_to(ROOT)} — {len(classes)} clases en {len(parts)} partes ({size_kb:.0f} KB)")
    for part in parts:
        print(f"  {part['id']}: {part['classCount']} clases ({part['firstClass']}–{part['lastClass']})")

    missing_colab = [c["id"] for c in classes if not c["colabUrl"]]
    if missing_colab:
        print(f"  aviso: {len(missing_colab)} clases sin notebook.ipynb")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
