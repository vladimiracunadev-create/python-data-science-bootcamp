"""Generate static HTML pages for the curriculum under site/clases/.

Walks classes/parte-*/ and renders each README.md to HTML, producing:

    site/clases/index.html                        — overview of the 9 parts
    site/clases/<parte>/index.html                — part landing (its classes)
    site/clases/<parte>/<class>/index.html        — class detail (README rendered)

Reuses the portal palette (../styles.css from each page) and the curriculum
markdown as the single source of truth. Re-run any time content changes; the
CI workflow runs this before the Pages artifact upload.
"""
from __future__ import annotations

import html
import re
import shutil
import sys
from pathlib import Path

import markdown  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ROOT / "classes"
OUT = ROOT / "site" / "clases"

MD = markdown.Markdown(
    extensions=["extra", "toc", "sane_lists", "tables", "fenced_code"],
    output_format="html5",
)

PART_TITLES = {
    "parte-0-prerrequisitos": ("Parte 0", "Prerrequisitos", "Python, NumPy, pandas, viz, SQL, NoSQL, APIs"),
    "parte-1-machine-learning-clasico": ("Parte 1", "ML clásico", "Regresión, clasificación, ensembles, no supervisado"),
    "parte-2-deep-learning": ("Parte 2", "Deep Learning", "Keras, TF, CNN, RNN, Transformers, RL, despliegue"),
    "parte-3-estadistica-inferencial": ("Parte 3", "Estadística inferencial", "Hipótesis, A/B testing, inferencia causal, Bayes"),
    "parte-4-mlops": ("Parte 4", "MLOps", "Docker, CI/CD, MLflow, monitoreo, interpretabilidad"),
    "parte-5-ingenieria-de-datos": ("Parte 5", "Ingeniería de datos", "Spark, Airflow, lakehouses, streaming"),
    "parte-6-sistemas-de-recomendacion": ("Parte 6", "Recomendadores", "Filtrado colaborativo, factorización, secuenciales"),
    "parte-7-etica-fairness-privacidad": ("Parte 7", "Ética, fairness, privacidad", "Sesgo, explicabilidad, marcos normativos"),
    "parte-8-capstones": ("Parte 8", "Capstones", "Proyectos integradores end-to-end"),
}

PART_EMOJIS = {
    "parte-0-prerrequisitos": "0️⃣",
    "parte-1-machine-learning-clasico": "1️⃣",
    "parte-2-deep-learning": "2️⃣",
    "parte-3-estadistica-inferencial": "3️⃣",
    "parte-4-mlops": "4️⃣",
    "parte-5-ingenieria-de-datos": "5️⃣",
    "parte-6-sistemas-de-recomendacion": "6️⃣",
    "parte-7-etica-fairness-privacidad": "7️⃣",
    "parte-8-capstones": "8️⃣",
}


# ──────────────────────────────────────────────────────────────────────────────
# HTML shell
# ──────────────────────────────────────────────────────────────────────────────

PAGE = """<!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} | Python Data Science Program</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#0f3d3e">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="icon" href="{root}assets/icon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{root}styles.css">
  <link rel="stylesheet" href="{root}clases/curriculum.css">
</head>
<body class="curriculum-body">
  <header class="cur-topbar">
    <a class="brand" href="{root}index.html">
      <span aria-hidden="true">🐍</span> Python Data Science Program
    </a>
    <nav class="cur-breadcrumbs">
      {breadcrumbs}
    </nav>
  </header>
  <main class="cur-main">
    {body}
  </main>
  <footer class="cur-footer">
    <p>
      Fuente única del currículo: <a href="https://github.com/vladimiracunadev-create/python-data-science-program/tree/main/{repo_path}"><code>{repo_path}</code></a>
      · <a href="{root}index.html">← Volver al portal del alumno</a>
    </p>
  </footer>
</body>
</html>
"""

CSS = """/* Curriculum pages — extiende styles.css del portal */
.curriculum-body { background: var(--bg); color: var(--ink); font-family: 'IBM Plex Sans', sans-serif; margin: 0; line-height: 1.6; }
.cur-topbar { display: flex; align-items: center; justify-content: space-between; padding: 14px 28px; background: var(--bg-soft); border-bottom: 1px solid var(--line); position: sticky; top: 0; z-index: 50; backdrop-filter: blur(8px); }
.cur-topbar .brand { font-family: 'Space Grotesk', sans-serif; font-weight: 700; color: var(--teal-dark); text-decoration: none; font-size: 1.05rem; }
.cur-breadcrumbs { font-size: 0.92rem; color: var(--ink-soft); }
.cur-breadcrumbs a { color: var(--teal-dark); text-decoration: none; }
.cur-breadcrumbs a:hover { text-decoration: underline; }
.cur-breadcrumbs .sep { margin: 0 8px; opacity: 0.4; }
.cur-main { max-width: 880px; margin: 0 auto; padding: 40px 28px 80px; }
.cur-main h1 { font-family: 'Space Grotesk', sans-serif; font-size: 2.1rem; line-height: 1.2; margin: 0 0 0.4em; color: var(--teal-dark); }
.cur-main h2 { font-family: 'Space Grotesk', sans-serif; font-size: 1.45rem; margin: 2em 0 0.5em; color: var(--ink); border-bottom: 1px solid var(--line); padding-bottom: 6px; }
.cur-main h3 { font-size: 1.15rem; margin: 1.6em 0 0.4em; color: var(--ink); }
.cur-main p, .cur-main ul, .cur-main ol { color: var(--ink-soft); }
.cur-main a { color: var(--teal); text-decoration: underline; text-decoration-color: var(--gold-light); text-underline-offset: 3px; }
.cur-main a:hover { color: var(--teal-dark); text-decoration-color: var(--gold); }
.cur-main code { font-family: 'JetBrains Mono', monospace; background: var(--purple-light); padding: 1px 6px; border-radius: 4px; font-size: 0.9em; color: #4c1d95; }
.cur-main pre { background: #0f172a; color: #e2e8f0; padding: 16px 20px; border-radius: var(--radius-sm); overflow-x: auto; box-shadow: var(--shadow); }
.cur-main pre code { background: transparent; color: inherit; padding: 0; }
.cur-main blockquote { border-left: 4px solid var(--gold); background: var(--bg-soft); padding: 14px 18px; margin: 1.4em 0; border-radius: 0 var(--radius-sm) var(--radius-sm) 0; color: var(--ink); }
.cur-main table { border-collapse: collapse; width: 100%; margin: 1.4em 0; background: var(--card); border-radius: var(--radius-sm); overflow: hidden; box-shadow: var(--shadow); }
.cur-main th, .cur-main td { padding: 10px 14px; text-align: left; border-bottom: 1px solid var(--line); }
.cur-main th { background: var(--teal-dark); color: #fff; font-weight: 600; }
.cur-main tr:last-child td { border-bottom: none; }
.cur-main hr { border: none; border-top: 1px solid var(--line); margin: 2.4em 0; }
.cur-footer { max-width: 880px; margin: 0 auto; padding: 24px 28px 40px; font-size: 0.88rem; color: var(--ink-soft); border-top: 1px solid var(--line); }
.cur-footer code { font-family: 'JetBrains Mono', monospace; font-size: 0.85em; }

/* Index/part grids */
.parts-grid, .classes-list { display: grid; gap: 18px; margin: 24px 0 40px; }
.parts-grid { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.part-card { display: block; padding: 22px 24px; background: var(--card); border: 1px solid var(--line); border-radius: var(--radius); text-decoration: none; transition: transform 0.15s, box-shadow 0.15s; box-shadow: var(--shadow); }
.part-card:hover { transform: translateY(-3px); box-shadow: var(--shadow-hover); }
.part-card .badge { font-family: 'Space Grotesk', sans-serif; font-size: 0.82rem; color: var(--teal-dark); font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase; }
.part-card h3 { margin: 6px 0 8px; color: var(--ink); font-size: 1.25rem; }
.part-card p { margin: 0; color: var(--ink-soft); font-size: 0.95rem; }
.part-card .count { display: inline-block; margin-top: 12px; padding: 3px 10px; background: var(--gold-light); color: #78350f; border-radius: 999px; font-weight: 600; font-size: 0.82rem; }

.classes-list a { display: block; padding: 14px 18px; background: var(--card); border: 1px solid var(--line); border-radius: var(--radius-sm); text-decoration: none; color: var(--ink); transition: border-color 0.15s, transform 0.15s; }
.classes-list a:hover { border-color: var(--teal); transform: translateX(3px); }
.classes-list .num { display: inline-block; min-width: 48px; font-family: 'JetBrains Mono', monospace; color: var(--teal-dark); font-weight: 600; }
.classes-list .title { color: var(--ink); }

.notebook-link { display: inline-flex; align-items: center; gap: 6px; margin: 8px 0 18px; padding: 6px 14px; background: var(--purple-light); color: #4c1d95; border-radius: 999px; font-size: 0.9rem; text-decoration: none; font-weight: 500; }
.notebook-link:hover { background: var(--purple); color: #fff; }
"""


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def slugify_part(name: str) -> str:
    return name  # already slug form on disk


def render_md(text: str) -> str:
    MD.reset()
    return MD.convert(text)


def rewrite_links(html_body: str, part_dir: str, class_dir: str | None) -> str:
    """Adjust relative links inside rendered markdown so they work from the generated path."""
    # Inside a class page: links like ../002-foo/README.md → ../002-foo/index.html
    # Links like ../../README.md (back to parte index) → ../../index.html (curriculum overview)
    # Links to classes/README.md don't apply here
    def fix(match: re.Match) -> str:
        target = match.group(1)
        # Skip absolute and anchors
        if target.startswith(("http://", "https://", "#", "mailto:")):
            return match.group(0)
        # README.md → index.html
        new = target.replace("README.md", "index.html")
        # Notebooks: link to GitHub blob (Pages can't serve .ipynb nicely)
        if new.endswith(".ipynb"):
            if class_dir is not None:
                gh_base = f"https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/classes/{part_dir}/{class_dir}/"
            else:
                gh_base = f"https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/classes/{part_dir}/"
            # If link is just `notebook.ipynb` (no path), point to GitHub
            if "/" not in new:
                new = gh_base + new
        return f'href="{new}"'

    return re.sub(r'href="([^"]+)"', fix, html_body)


def build_breadcrumbs(items: list[tuple[str, str | None]]) -> str:
    """items: [(label, href_or_None)] — last one usually href=None."""
    pieces = []
    for i, (label, href) in enumerate(items):
        if i > 0:
            pieces.append('<span class="sep">›</span>')
        if href:
            pieces.append(f'<a href="{href}">{html.escape(label)}</a>')
        else:
            pieces.append(f'<span>{html.escape(label)}</span>')
    return "".join(pieces)


def class_title_from_readme(text: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    return m.group(1).strip() if m else fallback


def list_parts() -> list[Path]:
    return sorted(p for p in CLASSES.glob("parte-*") if p.is_dir())


def list_classes(part_dir: Path) -> list[Path]:
    return sorted(c for c in part_dir.iterdir() if c.is_dir() and re.match(r"^\d{3}-", c.name))


# ──────────────────────────────────────────────────────────────────────────────
# Page builders
# ──────────────────────────────────────────────────────────────────────────────

def write_page(out_path: Path, *, title: str, description: str, body: str, breadcrumbs: str, repo_path: str, depth: int) -> None:
    root = "../" * depth
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(
        PAGE.format(
            title=html.escape(title),
            description=html.escape(description),
            body=body,
            breadcrumbs=breadcrumbs,
            root=root,
            repo_path=repo_path,
        ),
        encoding="utf-8",
    )


def build_curriculum_index() -> None:
    parts = list_parts()
    cards = []
    total_classes = 0
    for part in parts:
        n_classes = len(list_classes(part))
        total_classes += n_classes
        emoji = PART_EMOJIS.get(part.name, "•")
        meta = PART_TITLES.get(part.name)
        if meta:
            badge, title, desc = meta
        else:
            badge, title, desc = part.name, part.name, ""
        cards.append(
            f'<a class="part-card" href="{part.name}/index.html">'
            f'<span class="badge">{emoji} {html.escape(badge)}</span>'
            f'<h3>{html.escape(title)}</h3>'
            f'<p>{html.escape(desc)}</p>'
            f'<span class="count">{n_classes} clases</span>'
            f'</a>'
        )

    body = f"""
    <h1>Currículo completo</h1>
    <p><strong>{total_classes} clases en {len(parts)} partes.</strong> Esta es la fuente de referencia
    para alumnos, docentes y evaluadores: cada clase tiene su ficha pedagógica (objetivo, resultados,
    temas, ejercicios, homework) y enlace al notebook.</p>
    <p>El contenido se genera automáticamente desde los <code>README.md</code> del repositorio
    en cada deploy de Pages — no edites el HTML, edita el markdown.</p>
    <div class="parts-grid">{''.join(cards)}</div>
    """
    breadcrumbs = build_breadcrumbs([("🏠 Portal", "../index.html"), ("Currículo", None)])
    write_page(
        OUT / "index.html",
        title="Currículo completo",
        description=f"Las {total_classes} clases del Python Data Science Program organizadas en {len(parts)} partes.",
        body=body,
        breadcrumbs=breadcrumbs,
        repo_path="classes/",
        depth=1,
    )


def build_part_page(part: Path) -> None:
    classes = list_classes(part)
    readme = (part / "README.md").read_text(encoding="utf-8")
    # Strip the top nav blockquote (breadcrumbs already cover it)
    readme = re.sub(r"^>\s*\[⬅️.*?Parte siguiente\].*?\n", "", readme, flags=re.MULTILINE)
    # Strip the redundant "Índice de clases" section — we render a richer one below
    readme = re.sub(
        r"##\s*📚\s*Índice de clases.*?(?=\n##|\n>\s*\[⬅️|\Z)",
        "",
        readme,
        flags=re.DOTALL,
    )
    # Strip the trailing nav blockquote
    readme = re.sub(r"\n>\s*\[⬅️.*?Parte siguiente\].*?$", "", readme, flags=re.DOTALL)
    rendered = render_md(readme)
    rendered = rewrite_links(rendered, part.name, None)
    meta = PART_TITLES.get(part.name)
    title = meta[1] if meta else part.name
    badge = meta[0] if meta else ""

    # Replace the class index links with our own list (more visual)
    classes_list = ['<div class="classes-list">']
    for c in classes:
        num = c.name[:3]
        c_readme = (c / "README.md").read_text(encoding="utf-8")
        c_title = class_title_from_readme(c_readme, c.name)
        # Strip leading "Clase NNN — " if present to avoid repetition
        c_title = re.sub(r"^Clase\s+\d+\s+[—-]\s+", "", c_title)
        classes_list.append(
            f'<a href="{c.name}/index.html">'
            f'<span class="num">{num}</span> '
            f'<span class="title">{html.escape(c_title)}</span>'
            f'</a>'
        )
    classes_list.append("</div>")

    body = f"""
    {rendered}
    <hr>
    <h2>📚 Ficha por clase</h2>
    {''.join(classes_list)}
    """
    breadcrumbs = build_breadcrumbs([
        ("🏠 Portal", "../../index.html"),
        ("Currículo", "../index.html"),
        (f"{badge} — {title}", None),
    ])
    write_page(
        OUT / part.name / "index.html",
        title=f"{badge} · {title}",
        description=(meta[2] if meta else title),
        body=body,
        breadcrumbs=breadcrumbs,
        repo_path=f"classes/{part.name}/",
        depth=2,
    )


def build_class_page(part: Path, klass: Path) -> None:
    readme = (klass / "README.md").read_text(encoding="utf-8")
    title = class_title_from_readme(readme, klass.name)
    rendered = render_md(readme)
    rendered = rewrite_links(rendered, part.name, klass.name)

    notebook_link = (
        f'<a class="notebook-link" '
        f'href="https://github.com/vladimiracunadev-create/python-data-science-program/blob/main/classes/{part.name}/{klass.name}/notebook.ipynb">'
        f'📓 Abrir notebook en GitHub'
        f'</a>'
    )
    body = f"{notebook_link}\n{rendered}"

    part_meta = PART_TITLES.get(part.name)
    part_label = f"{part_meta[0]} — {part_meta[1]}" if part_meta else part.name
    breadcrumbs = build_breadcrumbs([
        ("🏠 Portal", "../../../index.html"),
        ("Currículo", "../../index.html"),
        (part_label, "../index.html"),
        (klass.name[:3], None),
    ])
    write_page(
        OUT / part.name / klass.name / "index.html",
        title=title,
        description=f"Clase {klass.name[:3]} del Python Data Science Program",
        body=body,
        breadcrumbs=breadcrumbs,
        repo_path=f"classes/{part.name}/{klass.name}/",
        depth=3,
    )


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "curriculum.css").write_text(CSS, encoding="utf-8")

    build_curriculum_index()

    parts = list_parts()
    n_classes_total = 0
    for part in parts:
        build_part_page(part)
        for klass in list_classes(part):
            build_class_page(part, klass)
            n_classes_total += 1

    print(f"[OK] Generated {len(parts)} parts and {n_classes_total} classes under {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
