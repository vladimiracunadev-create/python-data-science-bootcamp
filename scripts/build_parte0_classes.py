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
    # v2 — secciones pedagógicas adicionales
    definiciones: list[tuple[str, str]] = field(default_factory=list)  # (término, definición + características)
    faq: list[tuple[str, str]] = field(default_factory=list)            # (pregunta, respuesta)
    errores_comunes: list[tuple[str, str]] = field(default_factory=list)  # (error/síntoma, causa + fix)


# ──────────────────────────────────────────────────────────────────────────────
# README + notebook writers
# ──────────────────────────────────────────────────────────────────────────────

def render_readme(s: ClassSpec) -> str:
    temas_md = "\n".join(f"| {i+1} | {t} | {w} |" for i, (t, w) in enumerate(s.temas))
    resultados_md = "\n".join(f"{i+1}. {r}" for i, r in enumerate(s.resultados))
    ejercicios_md = "\n\n".join(f"**{i+1}.** {e}" for i, e in enumerate(s.ejercicios))
    refs_md = "\n".join(f"- {r}" for r in s.referencias)

    definiciones_md = ""
    if s.definiciones:
        defs = "\n\n".join(f"**{t}**\n: {d}" for t, d in s.definiciones)
        definiciones_md = f"\n## 📖 Definiciones y características\n\n{defs}\n"

    faq_md = ""
    if s.faq:
        items = "\n\n".join(f"**❓ {q}**\n\n{a}" for q, a in s.faq)
        faq_md = f"\n## ❓ Preguntas frecuentes\n\n{items}\n"

    err_md = ""
    if s.errores_comunes:
        rows = "\n".join(f"| {sym} | {fix} |" for sym, fix in s.errores_comunes)
        err_md = f"\n## ⚠️ Errores comunes\n\n| Síntoma / mensaje | Causa y cómo arreglar |\n|---|---|\n{rows}\n"

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
{definiciones_md}
## 📂 Dataset / recursos

{s.dataset}

## 🧪 Ejercicios

{ejercicios_md}

## 📝 Homework verificable

{s.homework}

**Criterio de aceptación:** {s.homework_criterio}
{err_md}{faq_md}
## 🔗 Referencias

{refs_md}

## ➡️ Siguiente clase

[Clase {s.siguiente[0][:3]} — {s.siguiente[1]}](../{s.siguiente[0]}/README.md)
"""


def _build_extra_cells(s: ClassSpec) -> list[Cell]:
    """Insert pedagogical extras (definiciones / faq / errores) before the final reference cell.

    Returns a list of Cell objects ready to splice in.
    """
    extras: list[Cell] = []
    if s.definiciones:
        lines = ["## 📖 Definiciones y características", ""]
        for term, defin in s.definiciones:
            lines.append(f"**{term}**")
            lines.append("")
            lines.append(defin)
            lines.append("")
        extras.append(Cell("md", "\n".join(lines).rstrip()))
    if s.errores_comunes:
        lines = ["## ⚠️ Errores comunes", "",
                 "| Síntoma / mensaje | Causa y cómo arreglar |", "|---|---|"]
        for sym, fix in s.errores_comunes:
            lines.append(f"| {sym} | {fix} |")
        extras.append(Cell("md", "\n".join(lines)))
    if s.faq:
        lines = ["## ❓ Preguntas frecuentes", ""]
        for q, a in s.faq:
            lines.append(f"**❓ {q}**")
            lines.append("")
            lines.append(a)
            lines.append("")
        extras.append(Cell("md", "\n".join(lines).rstrip()))
    return extras


def _splice_extras(cells: list[Cell], extras: list[Cell]) -> list[Cell]:
    """Insert extras BEFORE the last markdown cell (typically the 'Referencias' cell).

    If no clear final cell is detected, append at the end.
    """
    if not extras:
        return cells
    # Find last cell that looks like references / next-class navigation
    insert_at = len(cells)
    for i in range(len(cells) - 1, -1, -1):
        c = cells[i]
        if c.kind == "md" and ("Referencias" in c.src or "Siguiente" in c.src or "➡️" in c.src):
            insert_at = i
            break
    return cells[:insert_at] + extras + cells[insert_at:]


def render_notebook(s: ClassSpec) -> dict:
    all_cells = _splice_extras(s.cells, _build_extra_cells(s))
    cells = []
    for c in all_cells:
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
    definiciones=[
        ("Kernel", "Proceso Python (u otro lenguaje) que ejecuta el código de las celdas. Vive separado del frontend; si lo matas, pierdes el estado en memoria pero los archivos siguen intactos. Cada notebook se asocia a UN kernel, normalmente el del venv del proyecto."),
        ("Frontend", "La interfaz visual (Notebook clásico, JupyterLab, VS Code, Cursor, Colab). Todas hablan el mismo protocolo con el kernel — puedes cambiar de frontend sin perder datos si guardas el `.ipynb`."),
        ("Magic", "Comando especial de IPython, no de Python. Empieza con `%` (afecta una línea) o `%%` (afecta la celda entera). Ejemplos: `%timeit`, `%matplotlib inline`, `%%time`, `%debug`. No funcionan fuera de IPython/Jupyter."),
        ("`%timeit` vs `%%time`", "`%timeit` corre la expresión **muchas veces**, descarta outliers y reporta el mejor → microbenchmark estadísticamente serio. `%%time` mide **una sola corrida** del bloque → bueno para operaciones largas donde repetir cuesta. Característica clave: usa `%timeit` para algo en milisegundos, `%%time` para algo en segundos."),
        ("pdb / `%debug`", "Debugger interactivo de Python. `%debug` lo lanza en modo **post-mortem** después de una excepción — entras al stack en el punto del error sin re-correr nada. Comandos: `n` siguiente línea, `s` entra a función, `c` continúa, `p var` imprime, `u/d` sube/baja en stack, `q` salir."),
    ],
    errores_comunes=[
        ("`ModuleNotFoundError` aunque acabo de instalar el paquete", "El kernel activo NO es el venv donde corriste `pip install`. **Fix**: en una celda, `import sys; print(sys.executable)` — si no apunta a tu venv, cambia el kernel (menú Kernel → Change Kernel) o registra el venv con `python -m ipykernel install --user --name <nombre>`."),
        ("El notebook está \"congelado\" / la barra dice `[*]`", "Una celda quedó atrapada en bucle infinito o esperando input. **Fix**: menú Kernel → Interrupt (Esc + I dos veces). Si no responde, Restart Kernel — perderás variables en memoria pero los archivos quedan intactos."),
        ("Cambié código de un módulo importado y el notebook ignora el cambio", "Python cachea módulos importados. **Fix**: `%load_ext autoreload` + `%autoreload 2` al inicio del notebook; recarga automáticamente al ejecutar."),
        ("`%timeit` en una celda con asignación da error \"NameError\"", "Las variables creadas dentro de `%timeit` **no quedan** en el namespace (corre en sandbox). **Fix**: usa `%%timeit` (cell magic) si quieres preservar variables, o asigna fuera de la magic."),
        ("Outputs gigantes hacen el .ipynb pesado y el diff de git ilegible", "Cada output (imagen, tabla) queda guardado en el JSON del notebook. **Fix**: pre-commit hook con `nbstripout` (limpia outputs antes de commitear) o `Cell → All Output → Clear` antes de guardar."),
    ],
    faq=[
        ("¿Notebook clásico o JupyterLab o VS Code?",
         "Para aprender, **VS Code** (mismo backend, mejor UX: autocomplete con type hints, debug gráfico, git inline). Para reuniones colaborativas en navegador, JupyterLab. El Notebook clásico es legacy — sigue funcionando pero ya no recibe features."),
        ("¿Debo crear un kernel por proyecto o usar uno global?",
         "**Uno por proyecto.** Cada proyecto tiene dependencias distintas que entran en conflicto: el kernel global tarde o temprano se rompe. Comando: `python -m ipykernel install --user --name <proyecto>`."),
        ("¿Cuándo `%timeit` no es confiable?",
         "Cuando lo que mides toca disco/red/GPU — la varianza es enorme y el min no representa típico. Usa `%%time` con varios runs manuales y reporta mediana. Tampoco confiable si la primera corrida hace JIT (numba) — calienta con un run previo."),
        ("`%debug` no funciona, no muestra prompt",
         "Necesita haber ocurrido una excepción **en el kernel** justo antes. Si la celda falló pero el kernel se reinició, perdiste el stack. También: en VS Code Jupyter, usa el panel de debug en su lugar (más cómodo)."),
        ("¿Por qué mi notebook tarda 30 segundos en abrir si pesa solo 200 KB?",
         "Probablemente trae outputs binarios grandes (imágenes inline en base64). El JSON parece chico pero al renderizar el navegador procesa MB. Limpia outputs y guarda."),
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
    definiciones=[
        ("Repositorio (repo)", "Carpeta con un subdirectorio `.git/` que guarda toda la historia. Características: contenido inmutable identificado por SHA-1, ramas son punteros móviles, todo cambio publicado es eterno (aunque borres el commit, vive en reflog 90 días)."),
        ("Commit", "Snapshot inmutable del estado del repo en un momento. Tiene SHA-1, padre(s), autor, fecha, mensaje. Característica: **atómico** — debería poder revertirse solo sin romper nada."),
        ("Branch (rama)", "Puntero móvil a un commit. Mover el puntero es barato. `HEAD` apunta a la rama actual. La rama `main` no es especial; solo es la rama por defecto del proyecto."),
        ("Working tree / Staging / Repo / Remote", "Las 4 zonas: working tree (lo que editas) → staging area (lo preparado con `git add`) → repo local (lo commiteado) → remote (GitHub/GitLab). Cada `git` mueve cosas entre estas 4 zonas."),
        ("Merge vs Rebase", "**Merge** crea un commit nuevo que junta dos historias (preserva ambas). **Rebase** reescribe los commits de tu rama encima de otra (historia lineal pero modificada). Característica clave: **nunca rebases ramas compartidas** — reescribir SHAs rompe a tus compañeros."),
        ("Conventional Commits", "Convención que prescribe `tipo(scope): descripción`. Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `style`. Beneficio: changelogs y semver automáticos."),
    ],
    errores_comunes=[
        ("`error: failed to push some refs to 'origin/main'`", "El remote tiene commits que no tienes localmente (alguien más empujó). **Fix**: `git pull --rebase` primero, resuelve conflictos si los hay, luego `git push`."),
        ("`fatal: refusing to merge unrelated histories`", "Estás juntando dos repos sin ancestro común. **Fix**: `git pull --allow-unrelated-histories` (raro, asegúrate de que es lo que querías)."),
        ("Hice `git reset --hard` y perdí mi trabajo 😱", "Si fue local y no había commit: perdido. Si había commit, **`git reflog`** lo recupera: busca el SHA antes del reset y `git reset --hard <sha>`."),
        ("`Please tell me who you are` al hacer commit", "Falta config global. **Fix**: `git config --global user.name \"Tu Nombre\"` y `git config --global user.email \"tu@email.com\"`."),
        ("Commit con archivo enorme; ahora `git push` rechaza por >100 MB", "GitHub bloquea blobs >100 MB. **Fix**: NO basta con borrar el archivo en un commit nuevo (queda en historia). Usa `git filter-repo` o BFG para reescribir historia, o agrega a `.gitignore` desde el inicio."),
        ("Mergeé un PR pero ahora hay conflictos en `main`", "Alguien mergeó algo antes y tu base local es vieja. **Fix**: `git switch main && git pull` y resuelve los conflictos en una nueva rama, no directo en main."),
        ("`.gitignore` no funciona — el archivo sigue apareciendo en `git status`", "Si el archivo **ya estaba trackeado** antes del `.gitignore`, git lo sigue viendo. **Fix**: `git rm --cached <archivo>` y commitea — desde ahora lo ignora."),
    ],
    faq=[
        ("¿Merge o rebase?",
         "Regla simple: **merge para todo lo público, rebase solo localmente antes de PR** para limpiar tus propios commits. Nunca rebases una rama que alguien más usa."),
        ("¿Force push (`git push -f`) es siempre malo?",
         "En `main` o ramas compartidas: catástrofe. En tu propia rama de feature después de rebase: aceptable. Mejor usar `--force-with-lease` que falla si alguien más empujó mientras."),
        ("¿Cómo deshago el último commit?",
         "Si NO empujaste: `git reset --soft HEAD~1` (mantiene cambios staged) o `--hard` (los borra). Si YA empujaste y quieres revertirlo sin reescribir historia: `git revert HEAD` (crea commit nuevo que deshace)."),
        ("¿Squash o no squash al mergear?",
         "Squash = un solo commit final con todo el PR. Bueno para mantener historia limpia en main. Pierdes el detalle de pasos intermedios. Política común: squash en PRs pequeños, merge commit en grandes."),
        ("¿Está bien commitear el `.venv/` o el `data/raw/customers.csv`?",
         "NO. `.venv/` se reconstruye con `requirements.txt`. Datos grandes/sensibles van fuera del repo (DVC, S3, etc.) — ver clase 159 Parte 4."),
        ("Tengo 30 commits \"wip\" en mi rama, ¿qué hago antes del PR?",
         "`git rebase -i main` para entrar al rebase interactivo. Cambia `pick` por `squash` (o `fixup`) en los commits intermedios; quedará un historial limpio."),
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
    definiciones=[
        ("Cookiecutter", "Generador de proyectos a partir de plantillas. Tomas una plantilla (URL de un repo), respondes 3-5 preguntas y obtienes un proyecto con estructura pre-armada. Característica: idempotente — la plantilla no sabe ni le importa el contenido futuro del proyecto."),
        ("CCDS (cookiecutter-data-science)", "Plantilla específica para proyectos de DS, v2 (2023+). Separa `data/raw`, `data/interim`, `data/processed`, `src/`, `notebooks/`, `reports/`, `docs/`. Es **convención**, no dogma."),
        ("Editable install (`pip install -e .`)", "Instala el paquete pero apuntando al código fuente — los cambios se reflejan sin reinstalar. Habilita `from mi_proyecto.features import x` desde notebooks dentro del repo."),
        ("`pyproject.toml`", "Estándar moderno (PEP 621) para metadata + dependencias + config de tools (ruff, mypy, pytest). Reemplaza `setup.py` + `setup.cfg` + `requirements.txt` suelto + configs sueltas."),
        ("`Makefile`", "Archivo con \"recetas\" nombradas (`make data`, `make train`). Escrito en tabs (no espacios), las dependencias se declaran arriba (`target: dep1 dep2`). En proyectos DS funciona como interfaz humana a comandos típicos."),
    ],
    errores_comunes=[
        ("`ModuleNotFoundError: No module named 'mi_proyecto'` al importar desde notebook", "El paquete no está instalado en el venv del kernel. **Fix**: con el venv activo, `pip install -e .` desde la raíz del proyecto (necesita `pyproject.toml` con `[project] name='mi_proyecto'`)."),
        ("CSV en `data/raw/` apareció en `git status` y pesa 200 MB", "El `.gitignore` no cubre `data/raw/*` o no se aplicó a tiempo. **Fix**: añade `data/raw/*` al `.gitignore` + `!data/raw/.gitkeep` (mantén placeholder); si ya commiteaste, `git rm --cached data/raw/customers.csv`."),
        ("Tengo 3 notebooks con la misma función `limpiar_fechas`", "Copy-paste. **Fix**: extrae a `src/mi_proyecto/features/cleaning.py` y haz `from mi_proyecto.features.cleaning import limpiar_fechas` en cada notebook. Si modificas la función, todos los notebooks la heredan."),
        ("El compañero clonó el repo y `make data` falla con \"command not found\"", "Make no está instalado en Windows por default. **Fix**: instalar make (Git Bash trae uno) o documentar el comando equivalente en README; alternativamente, usa scripts Python directos."),
        ("Edité `pyproject.toml` y los imports siguen viejos", "Tras cambios en metadata o entry-points debes reinstalar. **Fix**: `pip install -e . --force-reinstall --no-deps` (sin deps si no las cambiaste)."),
    ],
    faq=[
        ("¿Realmente necesito una plantilla? ¿No puedo improvisar?",
         "Puedes, pero perderás el 80% de la ganancia: el compañero que ya conoce CCDS sabe dónde buscar; sin plantilla, cada proyecto es una caja de sorpresas."),
        ("¿`data/raw/` o `data/01_raw/`?",
         "CCDS v2 usa `data/raw/`, `data/interim/`, `data/processed/`, `data/external/`. La numeración `01_/02_/03_` la verás en Kedro y en algunas variantes — ambas son válidas, sigue una sola convención por proyecto."),
        ("¿`requirements.txt` o `pyproject.toml`?",
         "**`pyproject.toml`** para declarar las deps de tu paquete. **`requirements.txt`** (generado con `pip freeze` o `uv pip compile`) es el **lockfile** con versiones exactas para reproducir. No están en conflicto; conviven."),
        ("¿Y si el proyecto es solo un notebook exploratorio?",
         "No fuerces CCDS. Carpeta con `notebook.ipynb`, `data.csv` y `README.md` está bien. La estructura completa aporta cuando el proyecto vive >3 meses o tiene >1 persona."),
        ("¿Por qué los notebooks tienen prefijo numérico como `0.01-jvp-eda.ipynb`?",
         "Convención CCDS: `<fase>.<orden>-<iniciales>-<tema>`. Fase 0=exploración, 1=features, 2=modelos, 3=reportes. Iniciales del autor evitan conflictos cuando varias personas crean notebooks."),
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
    definiciones=[
        ("Workspace", "Concepto de VS Code = una carpeta (o conjunto de carpetas) con configuración asociada en `.vscode/settings.json`. La configuración del workspace **override** a la del usuario. Característica: pones `.vscode/` en git para que todos los colaboradores hereden la misma config."),
        ("Intérprete Python", "Ejecutable concreto (`/path/to/.venv/bin/python`). VS Code recuerda **uno por workspace**. Es el origen del 90% de los \"funciona en mi máquina\" entre IDE y terminal."),
        ("ruff", "Linter + formatter en un solo binario, escrito en Rust. Reemplaza black + isort + flake8 + (parte de) pylint con un único tool 10–100× más rápido. Config en `[tool.ruff]` de `pyproject.toml`."),
        ("Breakpoint", "Marca en una línea (F9) que pausa la ejecución cuando llega ahí. Permite inspeccionar variables, paso a paso, evaluar expresiones — mil veces más eficiente que `print`."),
        ("`launch.json`", "Config de debug de VS Code. Define perfiles: \"debug archivo actual\", \"debug tests\", \"debug Django\", etc. Cada perfil tiene su `program`, `args`, `env`, `justMyCode`."),
    ],
    errores_comunes=[
        ("\"Python interpreter is not selected\" al abrir un .py", "Workspace nuevo, VS Code no eligió uno. **Fix**: `Ctrl+Shift+P` → \"Python: Select Interpreter\" → elige el del `.venv` del proyecto. Guarda en `.vscode/settings.json` para que persista."),
        ("Format-on-save no aplica ruff aunque está instalado", "Falta declarar ruff como formatter por default para Python. **Fix**: en `settings.json`, `\"[python]\": { \"editor.defaultFormatter\": \"charliermarsh.ruff\" }` y `\"editor.formatOnSave\": true`."),
        ("Debugger arranca pero se salta mis breakpoints", "Estás corriendo el archivo (Ctrl+F5 = sin debug) en vez de debug (F5). O `justMyCode: true` está saltando código que vive en librerías que sí querías inspeccionar."),
        ("Tests no aparecen en el panel \"Testing\"", "VS Code no detectó pytest. **Fix**: `Ctrl+Shift+P` → \"Python: Configure Tests\" → pytest → carpeta `tests`. O añade `[tool.pytest.ini_options] testpaths = [\"tests\"]` en `pyproject.toml`."),
        ("Cambié interpreter y los imports siguen rotos", "VS Code cachea symbols del intérprete viejo. **Fix**: `Ctrl+Shift+P` → \"Python: Restart Language Server\". Si persiste, recarga la ventana (`Reload Window`)."),
    ],
    faq=[
        ("¿VS Code o Cursor?",
         "Cursor = VS Code + IA integrada (chat con contexto del repo, edición multi-archivo). Si pagas Copilot o no te interesa IA, quédate en VS Code. Si quieres pair-programming con IA sin saltar a otra app, Cursor. Las extensiones son las mismas."),
        ("¿Debo commitear `.vscode/`?",
         "**Sí** la parte compartida: `settings.json` (interpreter path relativo, formatter, etc.), `extensions.json` (recomendaciones). **No** lo personal: `.vscode/launch.json` con paths absolutos del tester."),
        ("¿Notebook en VS Code o en JupyterLab?",
         "VS Code para escribir/refactorizar (autocomplete con type hints, debug por celda, git inline). JupyterLab cuando alguien necesita un navegador y no quiere instalar VS Code (alumno, demo en proyector)."),
        ("¿Para qué `justMyCode: false`?",
         "Por default, el debugger se salta código de librerías de terceros (numpy, pandas) — útil para no perderte. Pero a veces el bug viene **desde dentro de pandas** (datos malformados); con `false` puedes entrar a ver."),
        ("¿Ruff reemplaza todo el stack? ¿No necesito black?",
         "Sí — `ruff format` es drop-in replacement de black (mismo output prácticamente). Mismo con isort (`ruff check --select I --fix`) y flake8 (`ruff check`). Único caso donde aún conviene black: si tu org ya tiene CI con black configurado y no quieres tocar."),
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
