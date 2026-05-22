"""Classes 033-036 — viz A: matplotlib anatomy, basic plots, subplots, anotaciones."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="033-matplotlib-anatomia-figura-axes",
    number="033",
    title="Matplotlib: anatomía figura/axes",
    duration="60 min",
    source="VanderPlas, **cap. 4** § 4.1 *Visualization with Matplotlib*.",
    objetivo=(
        "Que el alumno entienda la **jerarquía de objetos** de matplotlib (Figure → Axes → "
        "Artist) y use la **API orientada a objetos** (`fig, ax = plt.subplots()`) en vez del "
        "interfaz pyplot estilo MATLAB. Esto es lo que separa gráficos publicables de notebooks "
        "de cualquier curso introductorio."
    ),
    resultados=[
        "**Explicar** la jerarquía Figure → Axes → Artist y por qué la API OO es preferible.",
        "**Crear** una figura con `fig, ax = plt.subplots(figsize=(8, 4))` y configurar título, ejes, leyenda.",
        "**Guardar** una figura a PNG/SVG/PDF con DPI controlado.",
        "**Cerrar figuras** explícitamente para liberar memoria en notebooks que generan muchas.",
        "**Configurar defaults** con `plt.rcParams` (font, line width, colors).",
    ],
    temas=[
        ("Figure (canvas) → Axes (gráfico) → Artist (elementos)", "Modelo mental."),
        ("pyplot vs OO API", "`plt.plot` (state-based) vs `ax.plot` (explícito)."),
        ("`fig, ax = plt.subplots()`", "El patrón canónico."),
        ("`fig.savefig` y formatos", "PNG raster vs SVG/PDF vector."),
        ("Liberar memoria: `plt.close(fig)`", "Importante en loops."),
        ("`plt.rcParams` y stylesheets", "Defaults globales."),
    ],
    dataset="Sintético: serie temporal corta + scatter. Sin descarga.",
    ejercicios=[
        "**Hello world.** Crea figura 8×4, plot de `y = sin(x)` para `x ∈ [0, 2π]`. Título, xlabel, ylabel.",
        "**Dos líneas en un axes.** Misma figura: `sin(x)` y `cos(x)` con colores distintos y leyenda.",
        "**Guarda 3 formatos.** Mismo plot a PNG (100 DPI), PNG (300 DPI), SVG. Compara tamaños.",
        "**Loop sin leak.** Genera 20 plots en loop. Cierra cada uno con `plt.close(fig)`. Verifica que `len(plt.get_fignums())` queda en 0.",
        "**rcParams.** Cambia `font.size` y `lines.linewidth` para tu sesión. Verifica el efecto.",
    ],
    homework=(
        "Notebook: (a) figura `sin/cos` con todos los elementos (título, labels, leyenda, grid); "
        "(b) guardar PNG@300dpi y SVG; (c) generar 50 plots en loop sin memory leak; "
        "(d) demo de rcParams modificados."
    ),
    homework_criterio="Plot publicable (labels, leyenda, tamaño razonable). Loop deja 0 figuras abiertas.",
    referencias=[
        "VanderPlas, **cap. 4** § 4.1.",
        "[matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html)",
        "[Anatomy of a figure (matplotlib gallery)](https://matplotlib.org/stable/gallery/showcase/anatomy.html)",
    ],
    siguiente=("034-matplotlib-line-scatter-bar-histogram-boxplot", "Matplotlib: line, scatter, bar, histogram, boxplot"),
    cells=[
        Cell("md", "# Clase 033 — Matplotlib: anatomía\n\n**Parte 0** · VanderPlas cap. 4 § 4.1.\n\n> 🎯 Figure → Axes → Artist. API OO en vez de pyplot estilo MATLAB.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport matplotlib.pyplot as plt\nprint('matplotlib:', plt.matplotlib.__version__)"),
        Cell("md", "## 1️⃣ Jerarquía\n\n```\nFigure (canvas, contiene N axes)\n └── Axes (un gráfico — el rectángulo con sus ejes)\n      ├── Line2D, Scatter, Bar, ...   (Artists — lo dibujado)\n      ├── XAxis / YAxis                 (los ejes con sus ticks)\n      ├── Legend\n      └── Title\n```\n\n**Figure** = el canvas (ventana, archivo). **Axes** = un gráfico (puedes tener varios en una figura). **Artist** = todo lo demás (líneas, puntos, texto)."),
        Cell("md", "## 2️⃣ pyplot vs API OO\n\n```python\n# ❌ pyplot — state-based (estilo MATLAB)\nplt.plot(x, y)\nplt.title('Título')\nplt.xlabel('x')\nplt.savefig('out.png')\n\n# ✅ OO — explícito, escalable\nfig, ax = plt.subplots(figsize=(8, 4))\nax.plot(x, y)\nax.set_title('Título')\nax.set_xlabel('x')\nfig.savefig('out.png')\n```\n\nLa OO te obliga a nombrar el axes que estás manipulando — esto escala a 4 subplots sin confusión."),
        Cell("md", "## 3️⃣ El patrón canónico"),
        Cell("code", "x = np.linspace(0, 2*np.pi, 200)\n\nfig, ax = plt.subplots(figsize=(9, 4))\nax.plot(x, np.sin(x), label='sin(x)', linewidth=2)\nax.plot(x, np.cos(x), label='cos(x)', linewidth=2, linestyle='--')\nax.set_title('sin y cos')\nax.set_xlabel('x (radianes)')\nax.set_ylabel('valor')\nax.legend(loc='upper right')\nax.grid(alpha=0.3)\nax.axhline(0, color='black', linewidth=0.5)\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 4️⃣ Guardar — raster vs vector\n\n```python\nfig.savefig('out.png', dpi=300)          # raster, fixed resolution\nfig.savefig('out.svg')                   # vector, escala infinita\nfig.savefig('out.pdf', bbox_inches='tight')   # vector, ideal para LaTeX\n```\n\n- **PNG**: para web, presentaciones. DPI ≥ 150 para que se vea decente.\n- **SVG/PDF**: para informes editables o LaTeX. Tamaño pequeño si no hay scatter denso.\n- **`bbox_inches='tight'`**: recorta márgenes vacíos.\n- **`facecolor='white'`**: por default fondo transparente — explicítalo si lo quieres blanco."),
        Cell("md", "## 5️⃣ Liberar memoria en loops\n\nCada `plt.subplots()` deja una Figure viva en memoria. En notebooks que generan muchas figuras, esto causa OOM."),
        Cell("code", "import gc\n\nantes = len(plt.get_fignums())\nfor i in range(20):\n    fig, ax = plt.subplots()\n    ax.plot([1, 2, 3])\n    plt.close(fig)   # ← libera\n    gc.collect()\n\nprint(f'figuras abiertas: {len(plt.get_fignums())} (esperado: {antes})')"),
        Cell("md", "## 6️⃣ `rcParams` — defaults globales\n\n```python\nplt.rcParams['figure.figsize'] = (10, 5)\nplt.rcParams['lines.linewidth'] = 2\nplt.rcParams['font.size'] = 12\nplt.rcParams['axes.grid'] = True\nplt.rcParams['axes.spines.top'] = False\nplt.rcParams['axes.spines.right'] = False\n```\n\nO usa stylesheets predefinidos (clase 037): `plt.style.use('seaborn-v0_8-whitegrid')`."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Entiendo Figure → Axes → Artist\n- [ ] Uso `fig, ax = plt.subplots()` en vez de pyplot directo\n- [ ] Guardo en formato apropiado (PNG/SVG/PDF)\n- [ ] Cierro figuras explícitamente en loops\n- [ ] Sé configurar rcParams"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. sin/cos publicable, savefig 3 formatos, loop sin leak, rcParams demo."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 4 § 4.1\n- [matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html)\n\n➡️ **Siguiente:** [034 — line/scatter/bar/hist/box](../034-matplotlib-line-scatter-bar-histogram-boxplot/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="034-matplotlib-line-scatter-bar-histogram-boxplot",
    number="034",
    title="Matplotlib: line, scatter, bar, histogram, boxplot",
    duration="75 min",
    source="VanderPlas, **cap. 4** §§ 4.2–4.5 *Simple Line/Scatter/Bar/Histogram Plots*.",
    objetivo=(
        "Que el alumno conozca los **5 plots básicos** que cubren el 80% del trabajo de EDA, y "
        "sepa **cuándo cada uno**: line (tendencia temporal), scatter (relación dos variables), "
        "bar (categóricas), histogram (distribución), boxplot (5 estadísticos + outliers)."
    ),
    resultados=[
        "**Elegir el plot correcto** según el tipo de variables (continua/categórica) y el objetivo.",
        "**Ajustar marker, color, linestyle, alpha** para legibilidad.",
        "**Construir histogramas** con bins adecuados (regla de Freedman-Diaconis o `'auto'`).",
        "**Interpretar boxplot**: mediana, Q1/Q3, whiskers, outliers.",
        "**Combinar** bar + error bars para mostrar incertidumbre.",
    ],
    temas=[
        ("Line: tendencias y series temporales", "El más fácil de leer mal."),
        ("Scatter: relación entre dos variables", "Con `c=` y `s=` para 3ª/4ª dimensión."),
        ("Bar y barh: categóricas", "Vertical vs horizontal."),
        ("Histogram: distribución de una continua", "Bins importan."),
        ("Boxplot: distribución resumida + outliers", "Cuando hay muchos grupos."),
        ("Errorbar y fill_between", "Mostrar incertidumbre."),
    ],
    dataset="Palmer Penguins. Sin descarga adicional.",
    ejercicios=[
        "**Line.** Serie temporal de ventas mensuales (sintética). Anota máximo con flecha.",
        "**Scatter.** body_mass vs bill_length, color por species. Adicionalmente: `s=` con flipper_length para tamaño.",
        "**Bar.** Count por species, ordenado descendente. Vertical y horizontal — compara legibilidad.",
        "**Histogram.** Distribución de body_mass con bins='auto' y bins=10. Compara.",
        "**Boxplot.** body_mass por species: 3 cajas lado a lado. Identifica outliers.",
    ],
    homework=(
        "Notebook con penguins: (a) 5 plots básicos cada uno bien etiquetado; (b) scatter "
        "decorado con color y tamaño codificando 3 dimensiones; (c) bar con errorbars de std; "
        "(d) boxplot agrupado con interpretación de outliers."
    ),
    homework_criterio="Cada plot tiene título, labels, leyenda donde aplica. Bins justificados.",
    referencias=[
        "VanderPlas, **cap. 4** §§ 4.2-4.5.",
        "[matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)",
    ],
    siguiente=("035-matplotlib-subplots-y-gridspec", "Matplotlib: subplots y gridspec"),
    cells=[
        Cell("md", "# Clase 034 — Plots básicos\n\n**Parte 0** · VanderPlas cap. 4 §§ 4.2-4.5.\n\n> 🎯 5 plots que cubren 80% del EDA. Saber cuándo cada uno.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nrng = np.random.default_rng(42)\n\n# Penguins-like sintético\ndf = pd.DataFrame({\n    'species'    : np.repeat(['Adelie', 'Chinstrap', 'Gentoo'], [50, 30, 40]),\n    'body_mass'  : np.concatenate([rng.normal(3700, 400, 50), rng.normal(3700, 400, 30), rng.normal(5050, 500, 40)]),\n    'bill_length': np.concatenate([rng.normal(39, 2, 50),     rng.normal(48, 3, 30),     rng.normal(48, 3, 40)]),\n    'flipper'    : np.concatenate([rng.normal(190, 6, 50),    rng.normal(196, 7, 30),    rng.normal(217, 7, 40)]),\n})"),
        Cell("md", "## 1️⃣ Line — tendencias temporales\n\nÚsalo cuando el eje X tiene **orden natural** (tiempo, espacio). NO uses line para variables categóricas — engaña al ojo."),
        Cell("code", "fechas = pd.date_range('2024-01-01', periods=24, freq='ME')\nventas = (rng.normal(0, 0.5, 24).cumsum() + 10) * 100\n\nfig, ax = plt.subplots(figsize=(10, 4))\nax.plot(fechas, ventas, marker='o', linewidth=2, color='steelblue')\nmax_idx = ventas.argmax()\nax.annotate(f'pico: {ventas[max_idx]:.0f}',\n            xy=(fechas[max_idx], ventas[max_idx]),\n            xytext=(fechas[max_idx], ventas[max_idx] + 100),\n            arrowprops=dict(arrowstyle='->', color='red'),\n            ha='center')\nax.set_title('Ventas mensuales 2024')\nax.set_ylabel('USD')\nax.grid(alpha=0.3)\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 2️⃣ Scatter — relación entre dos continuas\n\nCon `c=` puedes codificar una 3ª dimensión (color), y con `s=` una 4ª (tamaño). Cuidado: más de 3 dimensiones en un scatter sobrecarga."),
        Cell("code", "fig, ax = plt.subplots(figsize=(8, 5))\ncolors = {'Adelie': 'C0', 'Chinstrap': 'C1', 'Gentoo': 'C2'}\nfor sp, sub in df.groupby('species'):\n    ax.scatter(sub['bill_length'], sub['body_mass'],\n               s=sub['flipper']*1.5, alpha=0.6, label=sp,\n               color=colors[sp], edgecolors='white', linewidth=0.5)\nax.set_xlabel('bill_length (mm)')\nax.set_ylabel('body_mass (g)')\nax.set_title('body_mass vs bill_length (tamaño ∝ flipper)')\nax.legend()\nax.grid(alpha=0.3)\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 3️⃣ Bar — categóricas\n\nVertical vs horizontal:\n- **Vertical**: si las etiquetas son cortas.\n- **Horizontal**: si hay muchas categorías o nombres largos (no tienes que rotar texto)."),
        Cell("code", "counts = df['species'].value_counts()\n\nfig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))\n\nax1.bar(counts.index, counts.values, color=['C0','C1','C2'])\nax1.set_title('bar vertical')\nax1.set_ylabel('count')\n\nax2.barh(counts.index[::-1], counts.values[::-1], color=['C2','C1','C0'])\nax2.set_title('bar horizontal (≈ misma info, mejor con nombres largos)')\n\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 4️⃣ Histogram — distribución\n\n**Bins** son críticos:\n- Pocos → escondes estructura.\n- Muchos → ruido visual.\n- `bins='auto'` usa Freedman-Diaconis, buen default."),
        Cell("code", "fig, axes = plt.subplots(1, 3, figsize=(12, 3.5))\n\naxes[0].hist(df['body_mass'], bins=5,     edgecolor='white')\naxes[0].set_title('bins=5 (pocos, esconde)')\n\naxes[1].hist(df['body_mass'], bins='auto', edgecolor='white')\naxes[1].set_title(\"bins='auto' (Freedman-Diaconis)\")\n\naxes[2].hist(df['body_mass'], bins=50,    edgecolor='white')\naxes[2].set_title('bins=50 (muchos, ruidoso)')\n\nfor a in axes: a.set_xlabel('body_mass')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 5️⃣ Boxplot — distribución resumida\n\n```\n           ┌─── max (whisker)\n           │\n           │   ┌── Q3 (75%)\n           │  ╶┤\n           │   │   ── mediana (50%)\n           │  ╶┤\n           │   └── Q1 (25%)\n           │\n           └─── min (whisker)\n  ° outliers (fuera de whisker = > 1.5×IQR)\n```\n\nÚtil para comparar **muchos grupos** rápido."),
        Cell("code", "fig, ax = plt.subplots(figsize=(8, 4))\ndatos_por_sp = [sub['body_mass'].values for _, sub in df.groupby('species')]\nax.boxplot(datos_por_sp, labels=df['species'].unique().tolist(), patch_artist=True)\nax.set_ylabel('body_mass (g)')\nax.set_title('body_mass por species')\nax.grid(axis='y', alpha=0.3)\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 6️⃣ Bar con errorbars + fill_between para bandas"),
        Cell("code", "medias = df.groupby('species')['body_mass'].mean()\nstds   = df.groupby('species')['body_mass'].std()\n\nfig, ax = plt.subplots(figsize=(7, 4))\nax.bar(medias.index, medias.values, yerr=stds.values, capsize=8, color=['C0','C1','C2'], alpha=0.7)\nax.set_ylabel('body_mass (g)')\nax.set_title('Media ± std por species')\nax.grid(axis='y', alpha=0.3)\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Elijo line solo para ejes X con orden natural\n- [ ] Uso scatter + c/s para codificar 3-4 dimensiones\n- [ ] Pongo bins='auto' por default en histogramas\n- [ ] Interpreto las 5 partes de un boxplot\n- [ ] Añado errorbars cuando muestro promedios"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 5 plots básicos sobre penguins, scatter 3D, bar con errorbars, boxplot agrupado."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 4 §§ 4.2-4.5\n- [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)\n\n➡️ **Siguiente:** [035 — subplots y gridspec](../035-matplotlib-subplots-y-gridspec/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="035-matplotlib-subplots-y-gridspec",
    number="035",
    title="Matplotlib: subplots y gridspec",
    duration="60 min",
    source="VanderPlas, **cap. 4** § 4.6 *Multiple Subplots*.",
    objetivo=(
        "Que el alumno organice múltiples plots en una sola figura — con `plt.subplots(n, m)` "
        "para grillas regulares y con `GridSpec` para layouts irregulares (un plot grande + "
        "varios pequeños). Crítico para informes y dashboards."
    ),
    resultados=[
        "**Crear grillas regulares** con `fig, axes = plt.subplots(2, 3, figsize=...)`.",
        "**Iterar sobre `axes.flat`** para llenar la grilla con loops.",
        "**Compartir ejes** con `sharex=True, sharey=True` para comparar.",
        "**Usar `GridSpec`** para layouts irregulares (1 grande + 3 pequeños).",
        "**Usar `constrained_layout=True`** en vez de `tight_layout()` (más confiable).",
    ],
    temas=[
        ("`plt.subplots(nrows, ncols)`", "Grilla regular."),
        ("Iterar con `.flat`", "Llenar muchos plots en loop."),
        ("`sharex`/`sharey`", "Comparar con misma escala."),
        ("`GridSpec` para layouts irregulares", "1 grande + N pequeños."),
        ("`constrained_layout` vs `tight_layout`", "El primero es mejor."),
        ("`add_subplot` con posiciones custom", "Cuando necesitas full control."),
    ],
    dataset="Palmer Penguins. Sin descarga.",
    ejercicios=[
        "**Grilla 2×2.** 4 histogramas de las 4 features numéricas de penguins en una figura.",
        "**Grilla con loop.** Itera `axes.flat` para plot consistente.",
        "**`sharey=True`.** 3 boxplots por species lado a lado con misma escala Y.",
        "**GridSpec irregular.** Un scatter grande (2×2) + 1 hist arriba (1×2) + 1 hist a la derecha (2×1) — marginal histograms.",
        "**`constrained_layout`.** Compara una figura compleja con `tight_layout()` vs `constrained_layout=True` — observa diferencia.",
    ],
    homework=(
        "Notebook con penguins: (a) grilla 2×2 hists; (b) 3 boxplots con sharey; (c) layout "
        "GridSpec con scatter central + marginales arriba/derecha; (d) misma figura comparando "
        "tight_layout vs constrained_layout."
    ),
    homework_criterio="Sin superposición de labels. Layouts limpios. Marginales alineadas al scatter.",
    referencias=[
        "VanderPlas, **cap. 4** § 4.6.",
        "[GridSpec tutorial](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)",
    ],
    siguiente=("036-matplotlib-legends-colorbars-ticks-anotaciones", "Matplotlib: legends, colorbars, ticks, anotaciones"),
    cells=[
        Cell("md", "# Clase 035 — subplots y gridspec\n\n**Parte 0** · VanderPlas cap. 4 § 4.6.\n\n> 🎯 Múltiples plots en una figura. Grillas regulares + GridSpec para irregulares.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom matplotlib.gridspec import GridSpec\nrng = np.random.default_rng(42)\n\nN = 200\ndf = pd.DataFrame({\n    'x'   : rng.normal(0, 1, N),\n    'y'   : rng.normal(0, 1, N),\n    'mass': rng.uniform(3000, 5000, N),\n    'bill': rng.uniform(35, 50, N),\n})"),
        Cell("md", "## 1️⃣ Grilla regular — `plt.subplots(n, m)`"),
        Cell("code", "fig, axes = plt.subplots(2, 2, figsize=(10, 7), constrained_layout=True)\nfeats = ['x', 'y', 'mass', 'bill']\n\nfor ax, col in zip(axes.flat, feats):\n    ax.hist(df[col], bins='auto', edgecolor='white')\n    ax.set_title(col)\n    ax.grid(alpha=0.3)\n\nfig.suptitle('Distribuciones (grilla 2×2)', fontsize=14)\nplt.show()"),
        Cell("md", "## 2️⃣ `sharex` / `sharey` — comparar con misma escala"),
        Cell("code", "fig, axes = plt.subplots(1, 3, figsize=(11, 4), sharey=True, constrained_layout=True)\nfor ax, sp in zip(axes, ['Adelie', 'Chinstrap', 'Gentoo']):\n    data = rng.normal({'Adelie': 3700, 'Chinstrap': 3700, 'Gentoo': 5050}[sp], 400, 100)\n    ax.boxplot(data, vert=True)\n    ax.set_title(sp)\n    ax.grid(axis='y', alpha=0.3)\naxes[0].set_ylabel('body_mass (g)')\nfig.suptitle('body_mass por species — sharey=True')\nplt.show()"),
        Cell("md", "## 3️⃣ `GridSpec` — layouts irregulares\n\nScatter central + marginales arriba/derecha (\"joint plot\"):"),
        Cell("code", "fig = plt.figure(figsize=(8, 8), constrained_layout=True)\ngs = GridSpec(4, 4, figure=fig)\n\nax_main  = fig.add_subplot(gs[1:, :-1])        # filas 1-3, cols 0-2\nax_xhist = fig.add_subplot(gs[0,  :-1])         # fila 0, cols 0-2\nax_yhist = fig.add_subplot(gs[1:, -1])          # filas 1-3, col 3\n\n# Scatter principal\nax_main.scatter(df['x'], df['y'], alpha=0.5)\nax_main.set_xlabel('x')\nax_main.set_ylabel('y')\nax_main.grid(alpha=0.3)\n\n# Marginal X (arriba)\nax_xhist.hist(df['x'], bins='auto', color='steelblue', alpha=0.7)\nax_xhist.axis('off')\n\n# Marginal Y (derecha) — horizontal\nax_yhist.hist(df['y'], bins='auto', color='steelblue', alpha=0.7, orientation='horizontal')\nax_yhist.axis('off')\n\nfig.suptitle('Joint plot con GridSpec')\nplt.show()"),
        Cell("md", "## 4️⃣ `constrained_layout` vs `tight_layout`\n\nAmbos evitan superposición de labels/leyendas. **`constrained_layout=True`** (al crear la figura) es más nuevo y más confiable; `tight_layout()` se llama después y a veces falla con leyendas externas o colorbars."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Creo grillas con `plt.subplots(n, m)`\n- [ ] Itero con `axes.flat` para llenar en loop\n- [ ] Uso `sharex/sharey` para comparar\n- [ ] Sé construir layouts irregulares con GridSpec\n- [ ] Prefiero `constrained_layout=True` a `tight_layout()`"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Grilla 2×2 hists, 3 boxplots sharey, joint plot con GridSpec, comparativa layouts."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 4 § 4.6\n- [GridSpec tutorial](https://matplotlib.org/stable/users/explain/axes/arranging_axes.html)\n\n➡️ **Siguiente:** [036 — Legends, colorbars, ticks, anotaciones](../036-matplotlib-legends-colorbars-ticks-anotaciones/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="036-matplotlib-legends-colorbars-ticks-anotaciones",
    number="036",
    title="Matplotlib: legends, colorbars, ticks, anotaciones",
    duration="60 min",
    source="VanderPlas, **cap. 4** §§ 4.7–4.9 *Customizing Legends, Colorbars, Ticks*.",
    objetivo=(
        "Que el alumno controle los detalles que distinguen un plot ad-hoc de uno publicable: "
        "leyenda fuera del gráfico, colorbar discreto, ticks personalizados, y anotaciones "
        "(flechas, texto) para guiar la atención del lector."
    ),
    resultados=[
        "**Posicionar leyenda** fuera del axes con `bbox_to_anchor`.",
        "**Configurar colorbar** con label, ticks discretos, y categoría.",
        "**Personalizar ticks**: rotación, formato (`FuncFormatter`, `PercentFormatter`), scale log.",
        "**Anotar puntos** con `ax.annotate(..., xy=..., xytext=..., arrowprops=...)`.",
        "**Añadir líneas de referencia** con `axhline`/`axvline` (umbrales, medias).",
    ],
    temas=[
        ("Legend con bbox_to_anchor", "Sacarla del axes."),
        ("Colorbar con label y ticks discretos", "Cuando hay codificación por color."),
        ("Tick formatters: percent, scientific, custom", "Legibilidad."),
        ("`ax.annotate` con flecha", "Resaltar un punto específico."),
        ("`axhline` / `axvline` / `axhspan`", "Líneas y bandas de referencia."),
        ("Log scale: `ax.set_yscale('log')`", "Cuando hay rango grande."),
    ],
    dataset="Sintético: serie con outliers, scatter con categorías.",
    ejercicios=[
        "**Leyenda fuera.** Plot con 5 líneas, leyenda a la derecha fuera del axes.",
        "**Colorbar.** Scatter con `c=` continuo (ej: density), colorbar con label.",
        "**PercentFormatter.** Bar chart con eje Y formateado como porcentaje.",
        "**Anotar outlier.** Scatter con un punto extremo; flecha + texto identificándolo.",
        "**Log scale.** Plot de valores con rango grande (1, 10, 100, 1000); compara linear vs log.",
    ],
    homework=(
        "Notebook con: (a) plot multi-línea con leyenda externa; (b) scatter con colorbar "
        "etiquetado; (c) bar % usando PercentFormatter; (d) plot con anotación de máximo "
        "via flecha; (e) comparativa lineal vs log en datos exponenciales."
    ),
    homework_criterio="Cada elemento visual tiene propósito. Anotaciones legibles, no superpuestas.",
    referencias=[
        "VanderPlas, **cap. 4** §§ 4.7-4.9.",
        "[matplotlib text and annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)",
    ],
    siguiente=("037-matplotlib-stylesheets", "Matplotlib: stylesheets"),
    cells=[
        Cell("md", "# Clase 036 — Legends, colorbars, ticks, anotaciones\n\n**Parte 0** · VanderPlas cap. 4 §§ 4.7-4.9.\n\n> 🎯 Los detalles que separan plot ad-hoc de plot publicable.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport matplotlib.pyplot as plt\nfrom matplotlib.ticker import PercentFormatter, FuncFormatter\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Leyenda fuera del axes\n\nCuando el gráfico está saturado, sácala con `bbox_to_anchor`:"),
        Cell("code", "x = np.linspace(0, 10, 100)\n\nfig, ax = plt.subplots(figsize=(9, 4))\nfor i in range(5):\n    ax.plot(x, np.sin(x + i*0.5) + i*0.3, label=f'serie {i+1}')\n\nax.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)\nax.set_title('Leyenda fuera del axes (a la derecha)')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 2️⃣ Colorbar\n\nCuando codificas info en color (continuo o discreto), añade colorbar:"),
        Cell("code", "x = rng.normal(0, 1, 500)\ny = rng.normal(0, 1, 500)\ndensity = np.exp(-(x**2 + y**2)/2)\n\nfig, ax = plt.subplots(figsize=(7, 5))\nsc = ax.scatter(x, y, c=density, cmap='viridis', s=20)\ncbar = fig.colorbar(sc, ax=ax)\ncbar.set_label('densidad')\nax.set_xlabel('x'); ax.set_ylabel('y')\nax.set_title('Scatter coloreado por densidad')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 3️⃣ Tick formatters\n\nCuando el eje representa porcentaje, dinero, fechas raras, etc.:"),
        Cell("code", "categorias = ['A', 'B', 'C', 'D', 'E']\nporcentajes = [0.45, 0.22, 0.15, 0.10, 0.08]   # como fracción\n\nfig, ax = plt.subplots(figsize=(7, 4))\nax.bar(categorias, porcentajes, color='steelblue')\nax.yaxis.set_major_formatter(PercentFormatter(xmax=1.0))\nax.set_title('Distribución por categoría')\nax.grid(axis='y', alpha=0.3)\nplt.tight_layout()\nplt.show()"),
        Cell("code", "# Formatter custom: USD con miles\ndef usd(x, pos):\n    return f'${x:,.0f}'\n\nventas = rng.uniform(50_000, 200_000, 6)\nfig, ax = plt.subplots(figsize=(7, 3))\nax.bar(range(6), ventas, color='seagreen')\nax.yaxis.set_major_formatter(FuncFormatter(usd))\nax.set_title('Ventas 2024 (USD)')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 4️⃣ Anotar puntos con flecha"),
        Cell("code", "x = np.arange(20)\ny = rng.normal(50, 10, 20).cumsum()\n\nfig, ax = plt.subplots(figsize=(9, 4))\nax.plot(x, y, marker='o', color='steelblue')\n\n# Anotar el máximo\nmax_i = y.argmax()\nax.annotate(\n    f'pico: {y[max_i]:.1f}',\n    xy=(x[max_i], y[max_i]),                  # punto a apuntar\n    xytext=(x[max_i] + 2, y[max_i] + 5),       # posición del texto\n    arrowprops=dict(arrowstyle='->', color='crimson', lw=1.5),\n    fontsize=11, color='crimson',\n)\nax.set_title('Anotando el máximo con flecha')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 5️⃣ Líneas y bandas de referencia"),
        Cell("code", "fig, ax = plt.subplots(figsize=(9, 4))\nax.plot(x, y, color='steelblue')\n\nax.axhline(y.mean(), color='gray', linestyle='--', label=f'media={y.mean():.0f}')\nax.axhspan(y.mean()-y.std(), y.mean()+y.std(), color='gray', alpha=0.15, label='±1 std')\nax.axvline(10, color='red', linestyle=':', linewidth=1, label='evento x=10')\n\nax.legend()\nax.set_title('Líneas y bandas de referencia')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 6️⃣ Log scale\n\nCuando los datos cubren varios órdenes de magnitud:"),
        Cell("code", "valores = np.array([1, 10, 100, 1_000, 10_000, 100_000])\nfig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4))\n\na1.plot(valores, marker='o', color='steelblue'); a1.set_title('lineal'); a1.grid(alpha=0.3)\na2.plot(valores, marker='o', color='steelblue'); a2.set_yscale('log'); a2.set_title('log'); a2.grid(alpha=0.3, which='both')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Saco leyenda con bbox_to_anchor cuando satura\n- [ ] Añado colorbar con label cuando hay codificación por color\n- [ ] Formateo ticks con PercentFormatter/FuncFormatter\n- [ ] Anoto puntos específicos con `annotate` + flecha\n- [ ] Uso `axhline`/`axvline`/`axhspan` para referencias"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 5 mejoras de presentación sobre plots básicos."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 4 §§ 4.7-4.9\n- [annotations docs](https://matplotlib.org/stable/users/explain/text/annotations.html)\n\n➡️ **Siguiente:** [037 — Stylesheets](../037-matplotlib-stylesheets/README.md)"),
    ],
))


def main() -> int:
    print(f"Generating {len(SPECS)} classes")
    for s in SPECS:
        write_class(s)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
