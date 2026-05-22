"""Generate README.md + notebook.ipynb for Parte 0 classes (002-046).

Each class has structured content (objetivo, resultados, temas, dataset, ejercicios,
homework, referencias) and a notebook with executable cells. Content draws on
VanderPlas (Python Data Science Handbook) and official docs.

Idempotent: re-run to refresh content. Single source of truth for class material
lives here until the corpus is mature enough to split per-file.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLASSES = ROOT / "classes" / "parte-0-prerrequisitos"


@dataclass
class Cell:
    kind: str  # "md" | "code"
    src: str


@dataclass
class ClassSpec:
    folder: str
    number: str
    title: str
    duration: str
    source: str
    objetivo: str
    resultados: list[str]
    temas: list[tuple[str, str]]  # (subtema, por qué importa)
    dataset: str
    ejercicios: list[str]
    homework: str
    homework_criterio: str
    referencias: list[str]
    siguiente: tuple[str, str]  # (folder, title)
    cells: list[Cell] = field(default_factory=list)


# ──────────────────────────────────────────────────────────────────────────────
# README + notebook writers
# ──────────────────────────────────────────────────────────────────────────────

def render_readme(s: ClassSpec) -> str:
    temas_md = "\n".join(f"| {i+1} | {t} | {w} |" for i, (t, w) in enumerate(s.temas))
    resultados_md = "\n".join(f"{i+1}. {r}" for i, r in enumerate(s.resultados))
    ejercicios_md = "\n\n".join(f"**{i+1}.** {e}" for i, e in enumerate(s.ejercicios))
    refs_md = "\n".join(f"- {r}" for r in s.referencias)
    return f"""# Clase {s.number} — {s.title}

> Parte: **0 — Prerrequisitos** · Fuente: {s.source}
> ⏱️ Duración estimada: **{s.duration}**.

---

## 🎯 Objetivo

{s.objetivo}

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

{resultados_md}

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
{temas_md}

## 📂 Dataset / recursos

{s.dataset}

## 🧪 Ejercicios

{ejercicios_md}

## 📝 Homework verificable

{s.homework}

**Criterio de aceptación:** {s.homework_criterio}

## 🔗 Referencias

{refs_md}

## ➡️ Siguiente clase

[Clase {s.siguiente[0][:3]} — {s.siguiente[1]}](../{s.siguiente[0]}/README.md)
"""


def render_notebook(s: ClassSpec) -> dict:
    cells = []
    for c in s.cells:
        src_lines = c.src.split("\n")
        src = [l + "\n" for l in src_lines[:-1]] + [src_lines[-1]]
        if c.kind == "md":
            cells.append({"cell_type": "markdown", "metadata": {}, "source": src})
        else:
            cells.append({"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": src})
    return {
        "cells": cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def write_class(s: ClassSpec) -> None:
    folder = CLASSES / s.folder
    if not folder.exists():
        print(f"  SKIP (folder missing): {s.folder}")
        return
    (folder / "README.md").write_text(render_readme(s), encoding="utf-8")
    (folder / "notebook.ipynb").write_text(
        json.dumps(render_notebook(s), indent=1, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"  [OK] {s.number} — {s.title[:60]}")


# ──────────────────────────────────────────────────────────────────────────────
# Class specs
# ──────────────────────────────────────────────────────────────────────────────

SPECS: list[ClassSpec] = []


def add(s: ClassSpec) -> None:
    SPECS.append(s)


# Bloque Setup (002-005) ─────────────────────────────────────────────────────

add(ClassSpec(
    folder="002-jupyter-y-jupyterlab-kernels-magics-debugging-profiling",
    number="002",
    title="Jupyter y JupyterLab — kernels, magics, debugging, profiling",
    duration="90 min",
    source="VanderPlas, *Python Data Science Handbook*, **cap. 1** — IPython: Beyond Normal Python.",
    objetivo=(
        "Que el alumno deje de usar Jupyter como un editor de texto con botón \"play\" y empiece a "
        "usarlo como un entorno exploratorio profesional: con magics que ahorran horas, debugger "
        "interactivo (`%debug`), y profiling real (`%timeit`, `%prun`). Al final debe poder "
        "diagnosticar por qué un notebook es lento sin adivinar."
    ),
    resultados=[
        "**Diferenciar** kernel, frontend (Notebook vs JupyterLab vs VS Code) y servidor — y saber qué pasa cuando uno se cuelga.",
        "**Usar magics esenciales:** `%timeit`, `%%time`, `%run`, `%load`, `%matplotlib inline`, `%debug`, `%who`, `%xmode`.",
        "**Conectar un kernel específico** a un notebook (`ipykernel install --user --name <env>`) sin pelearse con el venv equivocado.",
        "**Debuggear** una excepción con `%debug` y `pdb` (n, s, c, q, p, l).",
        "**Profilar** código lento con `%timeit` (microbenchmark) y `%prun` (line profiler) para decidir dónde optimizar.",
    ],
    temas=[
        ("Kernel ↔ frontend ↔ servidor", "Saber cuál murió cuando el notebook se cuelga."),
        ("Modo comando vs modo edición + atajos", "Velocidad real: A/B/X/M/Y/Esc/Enter."),
        ("Magics line (`%`) vs cell (`%%`)", "El 80% del valor de Jupyter está en las magics."),
        ("`%timeit` y `%%time`", "Microbenchmark riguroso (varias corridas, descarta outliers)."),
        ("`%debug` + pdb", "Inspección post-mortem sin re-correr todo el notebook."),
        ("`%prun` y `%lprun`", "Saber qué función pesa antes de optimizar."),
        ("Registro de kernels por venv", "Cada proyecto, su propio kernel — evita el bug `import` falla."),
    ],
    dataset=(
        "No requiere dataset externo. Usamos arreglos sintéticos con `numpy.random` para "
        "benchmarks. Para el ejercicio de debug, generamos un `ValueError` intencional."
    ),
    ejercicios=[
        "**Atajos sin mouse.** Crea 5 celdas, navega solo con teclado: convierte 2 a markdown, ejecuta todo en orden, borra una, deshaz. Cronométrate.",
        "**Registra tu kernel.** Desde un venv recién creado: `python -m ipykernel install --user --name ds-lab-001 --display-name 'DS Lab 001'`. Abre Jupyter, selecciona ese kernel, verifica con `import sys; sys.executable`.",
        "**Benchmark vectorización.** Con `%timeit`, compara sumar `range(10_000)` con un `for` vs `np.arange(10_000).sum()`. Anota cuántas veces más rápido es NumPy.",
        "**Post-mortem.** Provoca un `ZeroDivisionError`, luego ejecuta `%debug` en la siguiente celda y navega el stack con `u`/`d`, inspecciona variables con `p`.",
        "**Profila una función.** Escribe una función que ordene una lista 1000 veces con sort burbuja. Ejecuta `%prun -s cumulative tu_func()`. Identifica la línea más cara.",
    ],
    homework=(
        "Entrega un notebook `homework.ipynb` con: (a) celda que muestra `sys.executable` confirmando "
        "que usas un kernel registrado por ti; (b) benchmark `%timeit` comparando `sum(range(N))` "
        "vs `np.arange(N).sum()` para N=10k, 100k, 1M; (c) tabla markdown con los resultados; "
        "(d) gráfico simple del speedup."
    ),
    homework_criterio=(
        "El notebook abre con kernel propio (no el global), las 3 mediciones corren sin errores, y "
        "la conclusión incluye un número concreto (\"NumPy es ~50× más rápido para N=1M\")."
    ),
    referencias=[
        "VanderPlas, **cap. 1** — *IPython: Beyond Normal Python*.",
        "[IPython magics reference](https://ipython.readthedocs.io/en/stable/interactive/magics.html)",
        "[JupyterLab user guide](https://jupyterlab.readthedocs.io/)",
    ],
    siguiente=("003-git-y-github-para-data-scientists", "Git y GitHub para data scientists"),
    cells=[
        Cell("md", "# Clase 002 — Jupyter y JupyterLab\n\n**Parte 0 — Prerrequisitos** · VanderPlas cap. 1.\n\n> 🎯 Dejar de usar Jupyter como editor de texto y empezar a usarlo como entorno exploratorio: magics, debug interactivo, profiling.\n\n> ⏱️ ~90 min"),
        Cell("md", "## 🗺️ Agenda\n\n1. Kernel vs frontend vs servidor\n2. Magics esenciales (`%timeit`, `%debug`, `%prun`)\n3. Registrar un kernel propio\n4. Ejercicio de profiling\n5. Checklist + homework"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import sys, time\nimport numpy as np\nprint('python:', sys.version.split()[0])\nprint('exec  :', sys.executable)\nprint('numpy :', np.__version__)"),
        Cell("md", "## 1️⃣ Magics esenciales\n\n**Line magic** (`%`) afecta a la línea. **Cell magic** (`%%`) afecta a toda la celda.\n\n- `%timeit expr` → microbenchmark con varias corridas (descarta outliers).\n- `%%time` → tiempo total de la celda (una sola corrida).\n- `%who` → lista variables del namespace.\n- `%matplotlib inline` → gráficos dentro del notebook.\n- `%load_ext autoreload` + `%autoreload 2` → recarga módulos sin reiniciar kernel."),
        Cell("code", "# Microbenchmark riguroso: sum nativo vs numpy\nN = 100_000\nl = list(range(N))\na = np.arange(N)\n\nt0 = time.perf_counter(); s1 = sum(l); t1 = time.perf_counter()\nt2 = time.perf_counter(); s2 = a.sum(); t3 = time.perf_counter()\n\nprint(f'sum(range): {(t1-t0)*1000:.3f} ms')\nprint(f'np.sum   : {(t3-t2)*1000:.3f} ms')\nprint(f'speedup  : {(t1-t0)/(t3-t2):.1f}x')\nprint('(En Jupyter, prefiere %timeit que repite la medición.)')"),
        Cell("md", "## 2️⃣ Debugging interactivo\n\nCuando una celda explota, NO la re-ejecutas a ciegas — usa `%debug` en la siguiente celda y entras al stack en el punto exacto del error.\n\nComandos pdb:\n- `n` (next), `s` (step into), `c` (continue), `q` (quit)\n- `p var` (print), `pp var` (pretty print)\n- `u` / `d` (sube/baja en el stack)\n- `l` (lista código alrededor)"),
        Cell("code", "# Simulamos un bug típico — comenta la línea raise para evitar romper la ejecución del notebook\ndef divide_safe(a, b):\n    return a / b  # bug: no valida b == 0\n\ntry:\n    divide_safe(10, 0)\nexcept ZeroDivisionError as e:\n    print(f'ERROR: {e}')\n    print('En Jupyter, ahora ejecutarías %debug en la siguiente celda para entrar al pdb post-mortem.')"),
        Cell("md", "## 3️⃣ Profiling — saber qué optimizar\n\nReglas:\n1. **Mide antes de optimizar.** No adivines.\n2. `%timeit` para microbenchmarks de una expresión.\n3. `%prun` para perfil de función completa (tiempo por llamada).\n4. `%lprun` (requiere `pip install line_profiler`) para perfil línea por línea.\n5. `%memit` (requiere `memory_profiler`) para memoria."),
        Cell("code", "# Función deliberadamente ineficiente para profilar\ndef ordena_lento(xs):\n    # Bubble sort O(n^2) — no hagan esto en prod\n    xs = list(xs)\n    n = len(xs)\n    for i in range(n):\n        for j in range(n - i - 1):\n            if xs[j] > xs[j+1]:\n                xs[j], xs[j+1] = xs[j+1], xs[j]\n    return xs\n\nimport random\ndata = [random.random() for _ in range(500)]\n\nt0 = time.perf_counter(); ordena_lento(data); t1 = time.perf_counter()\nt2 = time.perf_counter(); sorted(data); t3 = time.perf_counter()\nprint(f'bubble : {(t1-t0)*1000:.2f} ms')\nprint(f'sorted : {(t3-t2)*1000:.2f} ms')\nprint(f'ratio  : {(t1-t0)/(t3-t2):.0f}x más lento')\nprint()\nprint('En Jupyter: %prun -s cumulative ordena_lento(data)')\nprint('te muestra dónde se gasta el tiempo, no solo cuánto.')"),
        Cell("md", "## 4️⃣ Registrar tu propio kernel\n\nEvita el bug clásico de la clase 001 (\"pip install funcionó pero import falla\"):\n\n```bash\n# Desde tu venv activo:\npython -m pip install ipykernel\npython -m ipykernel install --user --name ds-lab --display-name 'DS Lab (mi venv)'\n```\n\nLuego en Jupyter: **Kernel → Change Kernel → DS Lab**. Verifica con `import sys; sys.executable` que apunta a tu `.venv`."),
        Cell("code", "# Verifica el kernel activo\nimport sys\nfrom pathlib import Path\n\nprint('Kernel ejecutando este notebook:')\nprint(f'  {sys.executable}')\nprint()\nin_venv = sys.prefix != sys.base_prefix\nprint(f'¿Es un venv?: {in_venv}')\nif not in_venv:\n    print('⚠️  Estás en el Python global. Registra un kernel propio antes de instalar paquetes.')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé navegar Jupyter sin mouse (modo comando vs edición)\n- [ ] Uso `%timeit` en vez de cronometrar a ojo\n- [ ] Sé entrar a `%debug` cuando algo explota\n- [ ] Mi notebook usa un kernel propio del venv del proyecto\n- [ ] Sé qué función pesa más en mi código (con `%prun`)"),
        Cell("md", "## 📝 Homework\n\nVer `README.md` — entrega un notebook con benchmark `%timeit` comparando `sum(range(N))` vs `np.arange(N).sum()` para N=10k/100k/1M, tabla y gráfico."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas, **cap. 1** — *IPython: Beyond Normal Python*\n- [IPython magics](https://ipython.readthedocs.io/en/stable/interactive/magics.html)\n\n➡️ **Siguiente:** [003 — Git y GitHub para data scientists](../003-git-y-github-para-data-scientists/README.md)"),
    ],
))

add(ClassSpec(
    folder="003-git-y-github-para-data-scientists",
    number="003",
    title="Git y GitHub para data scientists",
    duration="120 min",
    source="Pro Git (Chacon & Straub) — caps. 2 y 3 · GitHub docs.",
    objetivo=(
        "Que el alumno use git no como \"botón save\" sino como un sistema serio de versionado: "
        "commits atómicos con mensajes útiles, branches por feature, PRs con review, y "
        "resolución de conflictos sin pánico. Adicionalmente: ignorar correctamente los archivos "
        "típicos de DS (datos pesados, notebooks con output, secrets)."
    ),
    resultados=[
        "**Inicializar** un repo, hacer commits atómicos con mensajes en formato convencional.",
        "**Trabajar con branches**: crear, cambiar, mergear y resolver un conflicto sin perder código.",
        "**Configurar `.gitignore`** para un proyecto de DS (datos, `.venv`, secrets, outputs de notebooks).",
        "**Abrir y revisar un PR en GitHub** desde la línea de comandos con `gh`.",
        "**Recuperar** trabajo perdido con `git reflog` (la red de seguridad invisible).",
    ],
    temas=[
        ("Modelo de git: working tree → staging → repo → remote", "Sin este modelo mental, todo parece magia."),
        ("Commits atómicos + mensajes convencionales", "Un commit = un cambio lógico revertible."),
        ("Branches y merge vs rebase", "Cuándo usar cada uno; por qué no rebasear ramas públicas."),
        ("`.gitignore` para data science", "Datos, modelos, notebooks con output, `.env` no van al repo."),
        ("Conflictos: anatomía y resolución", "`<<<<<<<`, `=======`, `>>>>>>>` y cómo no entrar en pánico."),
        ("Pull Requests + review en GitHub", "El review es donde se transfiere conocimiento."),
        ("`git reflog` — la red de seguridad", "Aunque borres una rama, los commits viven 90 días."),
    ],
    dataset=(
        "No requiere dataset. El \"dataset\" son los propios cambios que el alumno hace en archivos "
        "de prueba. Para el ejercicio del `.gitignore`, simulamos archivos típicos de DS (csv pesado, "
        "`.env`, `.ipynb_checkpoints/`)."
    ),
    ejercicios=[
        "**Repo desde cero.** `git init`, crea 3 archivos (`README.md`, `data.csv`, `notebook.ipynb`), haz 3 commits con mensajes en formato `tipo: descripción` (feat/fix/docs/chore).",
        "**Branch + conflicto.** Crea rama `feature/x`, modifica una línea en `README.md`. Vuelve a `main`, modifica la **misma línea** distinto. Mergea, resuelve el conflicto a mano.",
        "**`.gitignore` profesional.** Genera uno que ignore: `.venv/`, `__pycache__/`, `.ipynb_checkpoints/`, `*.csv` en `data/raw/`, `.env`, `models/*.pkl`. Verifica con `git status` que no aparecen.",
        "**PR desde la CLI.** Crea repo en GitHub (con `gh repo create`), push, crea PR con `gh pr create` y descripción no trivial.",
        "**Recuperación.** Borra una rama con commits. Recupera el HEAD con `git reflog` + `git checkout <sha>` + `git switch -c rescate`.",
    ],
    homework=(
        "Repo público en GitHub con: 5+ commits en formato convencional, al menos 1 branch mergeada, "
        "un `.gitignore` de DS completo, README con badges (build status si aplica) y un PR cerrado."
    ),
    homework_criterio=(
        "El historial (`git log --oneline`) se lee como cambios atómicos coherentes. `git status` "
        "limpio después de un experimento. PR mergeado con descripción legible."
    ),
    referencias=[
        "[Pro Git book](https://git-scm.com/book) — cap. 2 *Git Basics*, cap. 3 *Branching*.",
        "[Conventional Commits](https://www.conventionalcommits.org/)",
        "[GitHub CLI manual](https://cli.github.com/manual/)",
    ],
    siguiente=("004-estructura-reproducible-de-proyecto-cookiecutter-data-science", "Estructura reproducible de proyecto"),
    cells=[
        Cell("md", "# Clase 003 — Git y GitHub para data scientists\n\n**Parte 0 — Prerrequisitos** · Pro Git caps. 2-3.\n\n> 🎯 Usar git como sistema serio de versionado: commits atómicos, branches, PRs, conflictos sin pánico, `.gitignore` para DS.\n\n> ⏱️ ~120 min"),
        Cell("md", "## ⚙️ Setup\n\nLa mayoría de los ejercicios se hacen en terminal. Este notebook documenta los comandos y verifica el estado del repo desde Python."),
        Cell("code", "import subprocess\nfrom pathlib import Path\n\ndef run(cmd):\n    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)\n    return r.stdout.strip() or r.stderr.strip()\n\nprint('git version:', run('git --version'))\nprint('cwd        :', Path.cwd())"),
        Cell("md", "## 1️⃣ Modelo mental de git\n\n```\n[working tree]  ──git add──▶  [staging area]  ──git commit──▶  [local repo]  ──git push──▶  [remote]\n     editas                    preparas                       guardas                    publicas\n```\n\nCada commit es **un nodo en un DAG** identificado por su SHA-1. Las ramas son **punteros móviles** a commits. `HEAD` es el puntero al commit actual."),
        Cell("code", "# Inspecciona el estado del repo donde corre este notebook\nprint('--- branch actual ---')\nprint(run('git branch --show-current'))\nprint('--- últimos 5 commits ---')\nprint(run('git log --oneline -5'))\nprint('--- archivos modificados ---')\nprint(run('git status -s') or '(working tree limpio)')"),
        Cell("md", "## 2️⃣ Commits atómicos + mensajes convencionales\n\n**Atómico** = un commit = un cambio lógico que puede revertirse solo.\n\n**Mensaje convencional**: `tipo(scope): descripción corta`\n\nTipos comunes:\n- `feat` — nueva funcionalidad\n- `fix` — bugfix\n- `docs` — solo documentación\n- `refactor` — refactor sin cambio de comportamiento\n- `test` — añade/modifica tests\n- `chore` — mantenimiento (deps, build)\n\nEjemplos buenos:\n- `feat(api): agregar endpoint /predict para modelo v2`\n- `fix(loader): manejar nulos en columna fecha`\n- `docs(readme): aclarar requisitos de instalación`\n\nEjemplos malos:\n- `update` ← ¿qué?\n- `fix bug` ← ¿cuál bug?\n- `wip` ← no llega a main"),
        Cell("md", "## 3️⃣ Branches: crear, mergear, conflicto\n\n```bash\ngit switch -c feature/nuevo-modelo    # crea y cambia a nueva rama\n# … editas, commits …\ngit switch main\ngit merge feature/nuevo-modelo        # merge\n```\n\n**Conflicto** = git no puede decidir qué versión gana en una línea. Git marca el archivo así:\n\n```\n<<<<<<< HEAD\nversión de main\n=======\nversión de la rama\n>>>>>>> feature/nuevo-modelo\n```\n\n**Resolución**: edita el archivo dejando solo lo que quieres, borra los marcadores, `git add <archivo>`, `git commit` (mensaje pre-rellenado).\n\n**Merge vs rebase** (regla simple): merge para ramas compartidas, rebase solo para tu rama local antes de PR."),
        Cell("md", "## 4️⃣ `.gitignore` para data science\n\nLas reglas que **siempre** van en un proyecto de DS:\n\n```gitignore\n# Entornos\n.venv/\nvenv/\n__pycache__/\n*.pyc\n\n# Notebooks\n.ipynb_checkpoints/\n# (opcional) limpiar outputs: usa nbstripout en pre-commit\n\n# Datos\ndata/raw/*\ndata/interim/*\n!data/raw/.gitkeep\n!data/interim/.gitkeep\n\n# Modelos y artefactos\nmodels/*.pkl\nmodels/*.joblib\n*.h5\n\n# Secretos\n.env\n.env.*\n!.env.example\n\n# IDE\n.vscode/\n.idea/\n.DS_Store\n```\n\n**Regla de oro:** todo lo que pese >100 MB o sea sensible NUNCA al repo. Para datos versionados usa DVC (clase 159)."),
        Cell("code", "# Demo: simular qué se commitearía\nignored_examples = ['.venv/lib/site-packages/numpy.py', 'data/raw/customers.csv', '.env', 'models/v2.pkl', '.DS_Store']\nrespected = ['src/loader.py', 'README.md', 'tests/test_loader.py', 'data/raw/.gitkeep']\n\nprint('❌ Estos NO deben aparecer en git status:')\nfor f in ignored_examples:\n    print(f'   {f}')\nprint()\nprint('✅ Estos SÍ deben aparecer:')\nfor f in respected:\n    print(f'   {f}')"),
        Cell("md", "## 5️⃣ Pull Requests con `gh`\n\n```bash\n# Una vez por máquina\ngh auth login\n\n# En tu repo, después de push\ngh pr create --title \"feat: nuevo modelo de churn\" --body \"## Resumen\\n- ...\"\ngh pr list\ngh pr view 12 --web\ngh pr merge 12 --squash\n```\n\nEl PR es donde ocurre la **revisión técnica**. Un PR bueno:\n- Hace UNA cosa.\n- Tiene descripción del *por qué* (el qué ya está en el diff).\n- Pasa CI antes de pedir review.\n- Incluye screenshots / outputs si es visual."),
        Cell("md", "## 6️⃣ `git reflog` — la red de seguridad\n\n**Borraste una rama por error. Tranquilo.** Git guarda referencias al HEAD durante ~90 días:\n\n```bash\ngit reflog                           # lista todo lo que ha sido HEAD\n# Encuentra el SHA de tu commit perdido\ngit switch -c rescate <sha>           # nueva rama desde ese punto\n```\n\nMientras no hayas hecho `git gc` agresivo, casi nada se pierde."),
        Cell("code", "# Demo: muestra tus últimas 5 entradas del reflog\nprint(run('git reflog -5'))"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Mis commits son atómicos y tienen mensajes convencionales\n- [ ] Sé crear branches, mergear y resolver un conflicto\n- [ ] Mi `.gitignore` cubre `.venv/`, datos, secrets y outputs\n- [ ] Sé abrir y mergear un PR con `gh`\n- [ ] Sé que `git reflog` existe y para qué sirve"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Repo público en GitHub con 5+ commits convencionales, branch mergeada, `.gitignore` de DS y 1 PR cerrado."),
        Cell("md", "## 🔗 Referencias\n\n- [Pro Git book](https://git-scm.com/book) — gratis online\n- [Conventional Commits](https://www.conventionalcommits.org/)\n\n➡️ **Siguiente:** [004 — Estructura reproducible de proyecto](../004-estructura-reproducible-de-proyecto-cookiecutter-data-science/README.md)"),
    ],
))


add(ClassSpec(
    folder="004-estructura-reproducible-de-proyecto-cookiecutter-data-science",
    number="004",
    title="Estructura reproducible de proyecto (cookiecutter-data-science)",
    duration="60 min",
    source="cookiecutter-data-science v2 · *Hidden Technical Debt in ML Systems* (Sculley et al., 2015).",
    objetivo=(
        "Que el alumno deje de crear proyectos como \"una carpeta con notebooks\" y empiece a usar "
        "una estructura estándar que separa código, datos, modelos, notebooks de exploración y "
        "documentación. Esto no es estética — es lo que permite que un compañero entienda el "
        "proyecto en 5 minutos y que el código viva más allá del notebook donde nació."
    ),
    resultados=[
        "**Generar** un proyecto con la plantilla `cookiecutter-data-science` (CCDS v2).",
        "**Justificar** la separación `data/raw` (inmutable) ↔ `data/interim` ↔ `data/processed`.",
        "**Mover código** de un notebook a `src/` cuando deja de ser exploratorio.",
        "**Documentar** dependencias en `pyproject.toml` (no en `requirements.txt` suelto).",
        "**Reconocer** los olores de un proyecto mal estructurado (notebooks con números 01/02/03, código duplicado, datos en git).",
    ],
    temas=[
        ("Estructura CCDS v2", "Convención > improvisación."),
        ("`data/raw` es sagrado", "Nunca se modifica; siempre se puede regenerar todo desde ahí."),
        ("`notebooks/` vs `src/`", "Exploración vs producción."),
        ("`pyproject.toml` como fuente de verdad de deps", "Reemplaza `requirements.txt` suelto."),
        ("`Makefile` como interfaz", "`make data`, `make train`, `make test` — lo lee humano y máquina."),
        ("Olores típicos", "`Untitled27.ipynb`, datos en git, `final_FINAL_v2.py`."),
    ],
    dataset=(
        "Para el ejercicio principal, descarga el dataset de Palmer Penguins "
        "(https://github.com/allisonhorst/palmerpenguins) — pequeño (~13 KB), público, ideal "
        "para que `data/raw/penguins.csv` ocupe poco y se pueda commitear sin mala práctica."
    ),
    ejercicios=[
        "**Genera un proyecto CCDS.** `pipx run cookiecutter https://github.com/drivendataorg/cookiecutter-data-science` con nombre `ds-lab-004`. Explora la estructura.",
        "**Mueve código a `src/`.** Toma una función de un notebook tuyo previo y muévela a `src/<proyecto>/features.py`. Importa desde el notebook con `from <proyecto>.features import …`.",
        "**Convierte `requirements.txt` a `pyproject.toml`** (sección `[project.dependencies]`).",
        "**Refactoriza un notebook caótico.** Toma uno con bloques copy-paste y extrae 2 funciones a `src/`.",
        "**Lista 5 olores** en un repo público que conozcas y propón cómo arreglarlos.",
    ],
    homework=(
        "Un repo público con estructura CCDS, `data/raw/` con un dataset pequeño, al menos 1 notebook "
        "que importa funciones desde `src/`, `pyproject.toml` con deps, Makefile con `make setup` y `make data`."
    ),
    homework_criterio=(
        "Un compañero clona, corre `make setup && make data` y obtiene la misma estructura de datos "
        "procesados que tú reportaste. README explica el flujo."
    ),
    referencias=[
        "[cookiecutter-data-science v2 docs](https://cookiecutter-data-science.drivendata.org/)",
        "Sculley et al., [*Hidden Technical Debt in ML Systems*](https://papers.nips.cc/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) (NeurIPS 2015).",
        "[Palmer Penguins dataset](https://github.com/allisonhorst/palmerpenguins)",
    ],
    siguiente=("005-vs-code-cursor-para-python-y-jupyter", "VS Code / Cursor para Python y Jupyter"),
    cells=[
        Cell("md", "# Clase 004 — Estructura reproducible de proyecto\n\n**Parte 0 — Prerrequisitos** · cookiecutter-data-science v2.\n\n> 🎯 Pasar de \"carpeta con notebooks\" a proyecto profesional con separación de datos, código y documentación.\n\n> ⏱️ ~60 min"),
        Cell("md", "## 🗺️ La estructura estándar (CCDS v2)\n\n```\nmi-proyecto/\n├── README.md\n├── pyproject.toml          ← deps y metadata\n├── Makefile                ← comandos del proyecto\n├── data/\n│   ├── raw/                ← INMUTABLE. Nunca editar.\n│   ├── interim/            ← transformaciones intermedias\n│   ├── processed/          ← listo para modelar\n│   └── external/           ← datos de terceros\n├── notebooks/\n│   ├── 0.01-jvp-eda.ipynb  ← convención: <fase>.<n>-<iniciales>-<descripción>\n│   └── 1.02-jvp-modelo.ipynb\n├── src/\n│   └── mi_proyecto/\n│       ├── __init__.py\n│       ├── data/           ← carga/limpieza\n│       ├── features/       ← feature engineering\n│       ├── models/         ← entrenamiento, predicción\n│       └── visualization/  ← gráficos\n├── reports/\n│   └── figures/\n├── tests/\n└── docs/\n```\n\nNo es dogma — es **convención**. La ventaja: cualquier DS que la conozca sabe dónde buscar."),
        Cell("md", "## ⚙️ Por qué `data/raw` es sagrado\n\nRegla: **nunca modifiques un archivo en `data/raw/`**. Todo procesamiento escribe a `data/interim/` o `data/processed/`.\n\n**Por qué**:\n- Si tu pipeline rompe, puedes regenerar todo desde el origen.\n- Permite re-ejecutar análisis con datos diferentes (nuevo período, otra fuente).\n- Hace explícito el grafo de dependencias (raw → interim → processed)."),
        Cell("code", "# Demo: estructura típica creada con Path (simulación, no genera nada en disco)\nfrom pathlib import Path\n\nestructura = [\n    'mi-proyecto/data/raw/',\n    'mi-proyecto/data/interim/',\n    'mi-proyecto/data/processed/',\n    'mi-proyecto/notebooks/0.01-eda.ipynb',\n    'mi-proyecto/src/mi_proyecto/__init__.py',\n    'mi-proyecto/src/mi_proyecto/features.py',\n    'mi-proyecto/pyproject.toml',\n    'mi-proyecto/Makefile',\n    'mi-proyecto/README.md',\n]\nfor p in estructura:\n    icon = '📁' if p.endswith('/') else '📄'\n    print(f'{icon} {p}')"),
        Cell("md", "## 🐍 Notebooks vs `src/`\n\n**Notebooks** = exploración. Bocetos. Análisis ad-hoc.\n**`src/`** = código de producción que se reutiliza.\n\n**Regla práctica**: cuando copias-pegas una función entre 2 notebooks, es momento de moverla a `src/`. Luego desde notebook:\n\n```python\nfrom mi_proyecto.features import limpia_fechas\ndf = limpia_fechas(df)\n```\n\nPara que esto funcione, el paquete debe estar **instalado en modo editable**:\n\n```bash\npip install -e .   # desde la raíz del proyecto, con pyproject.toml\n```"),
        Cell("md", "## 📦 `pyproject.toml` como fuente de verdad\n\nEn 2026, `pyproject.toml` es el estándar (PEP 621). Reemplaza `setup.py`, `setup.cfg`, y deja `requirements.txt` solo para lockfiles.\n\nEjemplo mínimo:\n\n```toml\n[project]\nname = \"mi-proyecto\"\nversion = \"0.1.0\"\nrequires-python = \">=3.12\"\ndependencies = [\n    \"numpy>=2.0\",\n    \"pandas>=2.2\",\n    \"matplotlib>=3.8\",\n    \"scikit-learn>=1.4\",\n]\n\n[project.optional-dependencies]\ndev = [\"pytest>=8\", \"ruff>=0.5\", \"mypy>=1.10\"]\n\n[build-system]\nrequires = [\"setuptools>=61\"]\nbuild-backend = \"setuptools.build_meta\"\n```\n\nLuego: `pip install -e \".[dev]\"` instala todo + tools de desarrollo."),
        Cell("md", "## 🔧 `Makefile` como interfaz humana\n\n```makefile\n.PHONY: setup data train test clean\n\nsetup:\n\tpython -m venv .venv && . .venv/bin/activate && pip install -e \".[dev]\"\n\ndata:\n\tpython -m mi_proyecto.data.make_dataset data/raw data/processed\n\ntrain:\n\tpython -m mi_proyecto.models.train\n\ntest:\n\tpytest tests/ -v\n\nclean:\n\trm -rf data/interim/* data/processed/* models/*\n```\n\nVentaja: `make data` es más legible que recordar el comando exacto, y CI puede llamarlo igual que tú."),
        Cell("md", "## 🚩 Olores de proyecto mal estructurado\n\nSi ves alguno de estos, hay deuda técnica:\n\n- `Untitled27.ipynb` ← notebook sin nombre = código que nadie va a leer\n- `final_FINAL_v2.py` ← versionado a mano\n- `data/customers_20240801_backup.csv` en git ← datos en git, fecha en filename\n- 8 notebooks que cargan y limpian el CSV de la misma forma ← función no extraída\n- `requirements.txt` con `numpy` (sin versión) ← reproducibilidad rota\n- `notebook.ipynb` con celdas vacías y outputs gigantes ← `nbstripout` lo arregla"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé generar un proyecto con `cookiecutter-data-science`\n- [ ] Entiendo por qué `data/raw/` no se modifica\n- [ ] Sé importar desde `src/` en mis notebooks\n- [ ] Mi proyecto tiene `pyproject.toml`, no `requirements.txt` suelto\n- [ ] Reconozco al menos 3 olores de proyectos mal estructurados"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Repo CCDS con `data/raw/penguins.csv`, notebook que importa de `src/`, `Makefile` con `make setup` y `make data`."),
        Cell("md", "## 🔗 Referencias\n\n- [cookiecutter-data-science v2](https://cookiecutter-data-science.drivendata.org/)\n- Sculley et al., *Hidden Technical Debt in ML Systems* (NeurIPS 2015)\n\n➡️ **Siguiente:** [005 — VS Code / Cursor para Python y Jupyter](../005-vs-code-cursor-para-python-y-jupyter/README.md)"),
    ],
))


add(ClassSpec(
    folder="005-vs-code-cursor-para-python-y-jupyter",
    number="005",
    title="VS Code / Cursor para Python y Jupyter",
    duration="60 min",
    source="VS Code Python docs · Cursor docs · *The Pragmatic Programmer* cap. \"Power Editing\".",
    objetivo=(
        "Que el alumno deje de usar VS Code como Notepad y lo configure como un IDE serio para "
        "Python + Jupyter: selector de intérprete, debugger gráfico, linter (ruff), formatter "
        "(ruff format), tests integrados y notebooks editables. Bonus: cuándo conviene Cursor "
        "(VS Code + IA integrada)."
    ),
    resultados=[
        "**Configurar VS Code** con la extensión Python + Jupyter, seleccionando el intérprete del venv del proyecto.",
        "**Debuggear** un script Python paso a paso desde el panel gráfico (breakpoints, watch, call stack).",
        "**Editar y ejecutar notebooks** sin Jupyter web — con autocompletado, type hints y debug de celda.",
        "**Configurar ruff** como linter + formatter (reemplaza black + isort + flake8 en un solo tool).",
        "**Decidir cuándo usar Cursor** (idéntico a VS Code + IA integrada con autorización por chat).",
    ],
    temas=[
        ("Selección de intérprete por workspace", "El bug \"funciona en terminal pero no en VS Code\" se evita aquí."),
        ("Debugger gráfico vs `print`", "Breakpoints, watch, evaluación expresiones — mucho más rápido."),
        ("Notebooks nativos en VS Code", "Mejor UX que Jupyter web para edición; mismo backend."),
        ("ruff = linter + formatter en uno", "Reemplaza black/isort/flake8/pylint. Más rápido (Rust)."),
        ("Tests integrados (`pytest`)", "Run/debug tests con un click; coverage inline."),
        ("Extensiones esenciales", "Python, Jupyter, GitLens, ruff, Even Better TOML."),
        ("Cursor: cuándo sí", "Cuando quieres pair-programming con IA sin salir del editor."),
    ],
    dataset=(
        "Sin dataset externo. Usamos un script Python con un bug intencional para practicar debug "
        "gráfico, y un notebook trivial para verificar autocompletado/type hints."
    ),
    ejercicios=[
        "**Selecciona intérprete.** En VS Code: `Ctrl+Shift+P` → \"Python: Select Interpreter\" → elige el del `.venv` del proyecto. Verifica con `print(sys.executable)` en una celda.",
        "**Debug paso a paso.** Toma un script con un bug, pon breakpoint (F9), ejecuta con F5, navega con F10 (next), F11 (step in), Shift+F11 (step out). Inspecciona variables en panel.",
        "**Configura ruff.** En `pyproject.toml`: `[tool.ruff]` con `line-length = 100`, `[tool.ruff.lint]` con `select = [\"E\", \"F\", \"I\", \"UP\"]`. Habilita format on save.",
        "**Edita un notebook.** Abre `notebook.ipynb` en VS Code, ejecuta una celda, comprueba que el autocompletado funciona con type hints de pandas.",
        "**Tests con un click.** Instala `pytest`, crea `tests/test_simple.py` con 2 tests (uno OK, uno FAIL). Usa el panel \"Testing\" para correr/debuggear.",
    ],
    homework=(
        "Repo con `pyproject.toml` que incluye `[tool.ruff]`, `.vscode/settings.json` con `python.defaultInterpreterPath` "
        "y format-on-save habilitado, screenshot del debugger gráfico mostrando un breakpoint activo "
        "y variables inspeccionadas."
    ),
    homework_criterio=(
        "Otro alumno clona el repo, abre en VS Code, y al guardar un .py se aplica ruff format "
        "automáticamente. El screenshot muestra al menos 1 breakpoint y la variable inspeccionada."
    ),
    referencias=[
        "[VS Code Python docs](https://code.visualstudio.com/docs/python/python-tutorial)",
        "[VS Code Jupyter docs](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)",
        "[ruff docs](https://docs.astral.sh/ruff/)",
        "[Cursor docs](https://docs.cursor.com/)",
    ],
    siguiente=("006-python-tipos-estructuras-control-de-flujo", "Python: tipos, estructuras, control de flujo"),
    cells=[
        Cell("md", "# Clase 005 — VS Code / Cursor para Python y Jupyter\n\n**Parte 0 — Prerrequisitos** · VS Code Python docs.\n\n> 🎯 Configurar VS Code como IDE serio para Python+Jupyter: intérprete por workspace, debugger gráfico, ruff, tests integrados.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup mínimo\n\n**Extensiones obligatorias:**\n- `ms-python.python` — soporte Python\n- `ms-toolsai.jupyter` — notebooks nativos\n- `charliermarsh.ruff` — linter + formatter\n- `tamasfe.even-better-toml` — soporte `pyproject.toml`\n- `eamodio.gitlens` — git superpoderes\n\nInstala todas con:\n\n```bash\ncode --install-extension ms-python.python\ncode --install-extension ms-toolsai.jupyter\ncode --install-extension charliermarsh.ruff\ncode --install-extension tamasfe.even-better-toml\ncode --install-extension eamodio.gitlens\n```"),
        Cell("md", "## 1️⃣ Selector de intérprete (el bug invisible)\n\nVS Code recuerda **un intérprete por workspace** en `.vscode/settings.json`. Si no lo configuras, usará el primero que encuentre — generalmente el del sistema. Resultado: `import` funciona en terminal pero no en VS Code (o al revés).\n\n**Cómo configurarlo bien:**\n\n```json\n// .vscode/settings.json\n{\n  \"python.defaultInterpreterPath\": \"${workspaceFolder}/.venv/bin/python\",\n  \"python.terminal.activateEnvironment\": true,\n  \"editor.formatOnSave\": true,\n  \"[python]\": {\n    \"editor.defaultFormatter\": \"charliermarsh.ruff\",\n    \"editor.codeActionsOnSave\": {\n      \"source.fixAll.ruff\": \"explicit\",\n      \"source.organizeImports.ruff\": \"explicit\"\n    }\n  }\n}\n```\n\nEn Windows: `\"${workspaceFolder}/.venv/Scripts/python.exe\"`."),
        Cell("code", "import sys\nfrom pathlib import Path\n\nprint('Intérprete que ejecuta esta celda:')\nprint(f'  {sys.executable}')\nprint()\n\nin_venv = sys.prefix != sys.base_prefix\nprint(f'¿Estás en un venv? {in_venv}')\nif in_venv:\n    print(f'  prefix: {Path(sys.prefix).name}')\nelse:\n    print('⚠️  Selecciona un intérprete del venv del proyecto en VS Code.')"),
        Cell("md", "## 2️⃣ Debugger gráfico — el fin de los `print(\"AQUI 1\")`\n\nEl debug por `print` es lento y no escala. VS Code te da:\n- **Breakpoints** (F9): para la ejecución en la línea\n- **Step over** (F10): siguiente línea\n- **Step into** (F11): entra a la función\n- **Step out** (Shift+F11): sale de la función\n- **Variables** (panel izquierdo): valores actuales en el scope\n- **Watch**: expresiones que evalúas en tiempo real\n- **Call stack**: cómo llegaste aquí\n\nConfig mínima (`.vscode/launch.json`):\n\n```json\n{\n  \"version\": \"0.2.0\",\n  \"configurations\": [\n    {\n      \"name\": \"Python: Archivo actual\",\n      \"type\": \"debugpy\",\n      \"request\": \"launch\",\n      \"program\": \"${file}\",\n      \"console\": \"integratedTerminal\",\n      \"justMyCode\": false\n    }\n  ]\n}\n```\n\n`justMyCode: false` te deja entrar a código de librerías (útil cuando un error viene de pandas)."),
        Cell("md", "## 3️⃣ Notebooks nativos en VS Code\n\nMejor UX que Jupyter web para edición:\n- Autocompletado con type hints reales (no solo nombres de variables)\n- Hover muestra docstring de funciones de pandas/sklearn\n- Debug de celda con breakpoint\n- Git integrado (ves diffs por celda)\n- Outline lateral con headers de markdown\n\nSelector de kernel arriba a la derecha: elige el mismo intérprete del workspace para que `pip install` funcione consistente."),
        Cell("code", "# Demo: autocompletado funciona con type hints\nfrom typing import Iterable\n\ndef promedio(xs: Iterable[float]) -> float:\n    \"\"\"Promedio aritmético — escribe `promedio(` y mira el hint.\"\"\"\n    xs = list(xs)\n    return sum(xs) / len(xs) if xs else 0.0\n\nprint(promedio([1, 2, 3, 4, 5]))\nprint(promedio.__doc__)"),
        Cell("md", "## 4️⃣ ruff — un solo tool reemplaza 4\n\nEn 2026, **ruff** (Astral, Rust) sustituye al stack tradicional:\n- ❌ `black` (formatter) → ✅ `ruff format`\n- ❌ `isort` (import sort) → ✅ `ruff check --select I --fix`\n- ❌ `flake8` (linter) → ✅ `ruff check`\n- ❌ `pylint` (linter más estricto) → ✅ `ruff check --select PL`\n\nVentaja: 10–100× más rápido, 1 tool, 1 config.\n\nConfig recomendada (`pyproject.toml`):\n\n```toml\n[tool.ruff]\nline-length = 100\ntarget-version = \"py312\"\n\n[tool.ruff.lint]\nselect = [\n    \"E\",   # pycodestyle errors\n    \"F\",   # pyflakes\n    \"I\",   # isort\n    \"UP\",  # pyupgrade (sintaxis moderna)\n    \"B\",   # flake8-bugbear (bugs comunes)\n    \"N\",   # pep8-naming\n]\nignore = [\"E501\"]  # line-too-long lo deja al formatter\n\n[tool.ruff.format]\nquote-style = \"double\"\n```"),
        Cell("md", "## 5️⃣ Tests integrados\n\nPanel **Testing** (icono matraz). Con `pytest` instalado y tests en `tests/`:\n- VS Code descubre automáticamente\n- Click derecho → \"Run Test\" o \"Debug Test\"\n- Output inline (verde/rojo) en el archivo\n- Coverage opcional con `coverage.py` extension\n\nConfig (`pyproject.toml`):\n\n```toml\n[tool.pytest.ini_options]\ntestpaths = [\"tests\"]\npython_files = \"test_*.py\"\naddopts = \"-v --tb=short\"\n```"),
        Cell("md", "## 6️⃣ ¿Cuándo Cursor en vez de VS Code?\n\n**Cursor** = fork de VS Code con IA integrada (chat con contexto del proyecto, edición multi-archivo, autocompletado avanzado).\n\n**Usa Cursor si:**\n- Quieres pair programming con IA sin saltar a otra app\n- Trabajas mucho en refactors o exploración de código nuevo\n- Estás OK con pagar la suscripción\n\n**Quédate con VS Code si:**\n- Tu organización tiene políticas estrictas sobre IA\n- Ya pagas Copilot y te alcanza\n- No quieres dependencias adicionales\n\nAmbos comparten extensiones — migrar es trivial."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Mi VS Code apunta al intérprete del venv del proyecto\n- [ ] Sé poner un breakpoint y debuggear sin `print`\n- [ ] Edito notebooks en VS Code con autocompletado\n- [ ] Tengo ruff configurado en `pyproject.toml`\n- [ ] Sé correr tests desde el panel Testing"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Repo con `.vscode/settings.json`, `pyproject.toml` con ruff, y screenshot del debugger en acción."),
        Cell("md", "## 🔗 Referencias\n\n- [VS Code Python tutorial](https://code.visualstudio.com/docs/python/python-tutorial)\n- [ruff docs](https://docs.astral.sh/ruff/)\n\n➡️ **Siguiente:** [006 — Python: tipos, estructuras, control de flujo](../006-python-tipos-estructuras-control-de-flujo/README.md)"),
    ],
))


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────

def main() -> int:
    print(f"Generating {len(SPECS)} classes under {CLASSES.relative_to(ROOT)}")
    for s in SPECS:
        write_class(s)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
