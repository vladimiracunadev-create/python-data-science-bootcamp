"""Classes 037-040 — viz B: stylesheets, 3D, seaborn, geo."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="037-matplotlib-stylesheets",
    number="037",
    title="Matplotlib: stylesheets",
    duration="30 min",
    source="VanderPlas, **cap. 4** § 4.11 *Customizing Matplotlib: Configurations and Stylesheets*.",
    objetivo=(
        "Que el alumno aproveche **stylesheets** built-in y propios para mantener consistencia "
        "visual entre plots y proyectos — y deje de configurar manualmente rcParams en cada notebook."
    ),
    resultados=[
        "**Listar stylesheets disponibles** con `plt.style.available`.",
        "**Aplicar** un style globalmente (`plt.style.use(...)`) o solo a un bloque (`with plt.style.context(...)`).",
        "**Crear style propio** en un archivo `.mplstyle` y usarlo.",
        "**Combinar styles** (uno + ajustes manuales).",
        "**Elegir style** según contexto (informe, presentación, B&N para impresión).",
    ],
    temas=[
        ("`plt.style.available`", "Catálogo built-in."),
        ("`plt.style.use(...)` global", "Afecta todos los plots subsiguientes."),
        ("`with plt.style.context(...)`", "Temporal, ideal para un bloque."),
        ("Archivo `.mplstyle` propio", "Reusar entre proyectos."),
        ("Stylesheets comunes", "default, seaborn-v0_8-whitegrid, ggplot, fivethirtyeight, grayscale."),
        ("rcParams override puntual", "Style + ajuste fino."),
    ],
    dataset="Sintético: mismo plot en varios styles. Sin descarga.",
    ejercicios=[
        "**Catalogo.** Imprime `plt.style.available`. Identifica 5 que suenen útiles.",
        "**Galería visual.** Mismo scatter plot bajo 4 styles distintos (default, ggplot, seaborn-whitegrid, grayscale).",
        "**Bloque temporal.** Con `with plt.style.context('seaborn-v0_8-darkgrid'):` aplica style solo a 1 figura.",
        "**Style propio.** Crea `mi_style.mplstyle` con tus defaults preferidos. Úsalo.",
        "**Style + override.** Aplica `ggplot` y luego cambia `figure.figsize` para un plot específico.",
    ],
    homework=(
        "Notebook: (a) galería de 4 styles sobre un mismo dataset; (b) crear `informe.mplstyle` "
        "con paleta corporativa simulada (3 colores principales); (c) demo de uso temporal con "
        "`plt.style.context`; (d) comparativa B&N (`grayscale`) vs color para una figura que "
        "podría imprimirse."
    ),
    homework_criterio="Galería con plots reconocibles; style propio aplica colores definidos.",
    referencias=[
        "VanderPlas, **cap. 4** § 4.11.",
        "[matplotlib stylesheets gallery](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)",
    ],
    siguiente=("038-matplotlib-3d-plotting", "Matplotlib: 3D plotting"),
    cells=[
        Cell("md", "# Clase 037 — Stylesheets\n\n**Parte 0** · VanderPlas cap. 4 § 4.11.\n\n> 🎯 Consistencia visual sin reconfigurar rcParams en cada notebook.\n\n> ⏱️ ~30 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport matplotlib.pyplot as plt\nrng = np.random.default_rng(42)\n\nstyles = sorted(plt.style.available)\nprint(f'{len(styles)} styles disponibles. Primeros 10:')\nfor s in styles[:10]:\n    print(f'  - {s}')"),
        Cell("md", "## 1️⃣ Galería: mismo plot, 4 styles"),
        Cell("code", "x = np.linspace(0, 10, 100)\nseries = [np.sin(x + i*0.5) + i*0.3 for i in range(4)]\n\nselected = ['default', 'ggplot', 'seaborn-v0_8-whitegrid', 'grayscale']\n# Filtrar los que existen en esta versión\nselected = [s for s in selected if s in styles or s == 'default']\n\nfig, axes = plt.subplots(1, len(selected), figsize=(4*len(selected), 3.5), constrained_layout=True)\nif len(selected) == 1:\n    axes = [axes]\n\nfor ax, style in zip(axes, selected):\n    with plt.style.context(style):\n        # Crear axes nuevo dentro del context para que herede el style\n        for i, s in enumerate(series):\n            ax.plot(x, s, label=f'{i}')\n        ax.set_title(style)\n        ax.legend(fontsize=8)\nplt.show()"),
        Cell("md", "## 2️⃣ Aplicar globalmente vs contextual\n\n```python\n# Globalmente — afecta TODOS los plots subsiguientes\nplt.style.use('ggplot')\n\n# Temporalmente — solo dentro del with\nwith plt.style.context('seaborn-v0_8-darkgrid'):\n    fig, ax = plt.subplots()\n    ax.plot(x, y)\n```"),
        Cell("md", "## 3️⃣ Style propio (`.mplstyle`)\n\nUn archivo de texto con pares `clave: valor` (igual que rcParams):\n\n```\n# informe.mplstyle\nfigure.figsize: 10, 5\nfigure.facecolor: white\nfont.family: sans-serif\nfont.size: 11\naxes.titlesize: 14\naxes.labelsize: 11\naxes.spines.top: False\naxes.spines.right: False\naxes.grid: True\ngrid.alpha: 0.3\nlines.linewidth: 2\naxes.prop_cycle: cycler('color', ['#0F766E', '#D9A441', '#7C3AED'])\n```\n\nLuego: `plt.style.use('/ruta/a/informe.mplstyle')`."),
        Cell("md", "## 4️⃣ Style + override puntual\n\nEl style sienta los defaults; rcParams puede overridear para un plot específico:\n\n```python\nplt.style.use('ggplot')\n\nwith plt.rc_context({'figure.figsize': (12, 6), 'font.size': 14}):\n    fig, ax = plt.subplots()\n    # ...\n```"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Conozco styles built-in (`plt.style.available`)\n- [ ] Aplico style globalmente o con context\n- [ ] Puedo crear `.mplstyle` propio\n- [ ] Override con `plt.rc_context` para casos puntuales"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Galería 4 styles, `informe.mplstyle` propio, B&N vs color."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 4 § 4.11\n- [stylesheets gallery](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)\n\n➡️ **Siguiente:** [038 — 3D plotting](../038-matplotlib-3d-plotting/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="038-matplotlib-3d-plotting",
    number="038",
    title="Matplotlib: 3D plotting",
    duration="45 min",
    source="VanderPlas, **cap. 4** § 4.12 *Three-Dimensional Plotting in Matplotlib*.",
    objetivo=(
        "Que el alumno sepa cuándo (raramente) usar 3D y cómo hacerlo bien: scatter 3D, "
        "superficies (`plot_surface`), wireframes y contornos. Spoiler: la mayoría de las "
        "veces un buen 2D + color comunica mejor."
    ),
    resultados=[
        "**Crear axes 3D** con `projection='3d'`.",
        "**Scatter, line, surface, wireframe, contour** en 3D.",
        "**Controlar ángulo de vista** con `ax.view_init(elev, azim)`.",
        "**Reconocer cuándo NO usar 3D**: la mayoría de las veces hay una alternativa 2D mejor.",
    ],
    temas=[
        ("`projection='3d'`", "Habilita el 3D toolkit."),
        ("Scatter 3D con codificación por color", "3 dims + 4 (color)."),
        ("`plot_surface` para z = f(x, y)", "Funciones bivariadas."),
        ("`plot_wireframe` y `contour3D`", "Alternativas más simples."),
        ("`view_init`: rotar interactivo", "En notebooks con `%matplotlib widget`."),
        ("Cuándo NO usar 3D", "Casi siempre."),
    ],
    dataset="Sintético: superficie analítica + nube de puntos. Sin descarga.",
    ejercicios=[
        "**Scatter 3D.** 200 puntos con coords (x, y, z) y color por una 4ª variable.",
        "**Superficie.** `z = sin(sqrt(x² + y²))` en mesh 50×50. `plot_surface` con colormap.",
        "**Wireframe + contour.** Misma función con `plot_wireframe`. Compara legibilidad con superficie llena.",
        "**view_init.** Cambia `(elev, azim)` a 4 ángulos y graba una grilla 2×2.",
        "**Reto: 2D que vence al 3D.** Para tu scatter 3D del ejercicio 1, propón un 2D + color/tamaño que comunique igual o mejor.",
    ],
    homework=(
        "Notebook: (a) scatter 3D con 4 dimensiones (xyz + color); (b) superficie z=f(x,y); "
        "(c) wireframe del mismo z; (d) grilla 2×2 con 4 view_init distintos; "
        "(e) ejercicio de \"2D vence al 3D\": versión 2D del scatter."
    ),
    homework_criterio="Plots 3D legibles (no espagueti). Versión 2D del scatter comparable.",
    referencias=[
        "VanderPlas, **cap. 4** § 4.12.",
        "[matplotlib mplot3d tutorial](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html)",
    ],
    siguiente=("039-seaborn-distribuciones-relaciones-categoricas-facetas", "Seaborn: distribuciones, relaciones, categóricas, facetas"),
    cells=[
        Cell("md", "# Clase 038 — 3D plotting\n\n**Parte 0** · VanderPlas cap. 4 § 4.12.\n\n> 🎯 Cuándo (raramente) usar 3D y cómo hacerlo bien.\n\n> ⏱️ ~45 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport matplotlib.pyplot as plt\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Habilitar 3D\n\n```python\nfig = plt.figure()\nax = fig.add_subplot(111, projection='3d')\n```"),
        Cell("md", "## 2️⃣ Scatter 3D"),
        Cell("code", "N = 200\nxs = rng.normal(0, 1, N)\nys = rng.normal(0, 1, N)\nzs = rng.normal(0, 1, N)\ncolors = xs*ys*zs   # 4ª dimensión codificada en color\n\nfig = plt.figure(figsize=(7, 5))\nax = fig.add_subplot(111, projection='3d')\nsc = ax.scatter(xs, ys, zs, c=colors, cmap='coolwarm', s=30, alpha=0.7)\nax.set_xlabel('x'); ax.set_ylabel('y'); ax.set_zlabel('z')\nfig.colorbar(sc, label='x·y·z')\nplt.title('Scatter 3D')\nplt.show()"),
        Cell("md", "## 3️⃣ Superficie z = f(x, y)"),
        Cell("code", "x = np.linspace(-5, 5, 50)\ny = np.linspace(-5, 5, 50)\nX, Y = np.meshgrid(x, y)\nZ = np.sin(np.sqrt(X**2 + Y**2))\n\nfig = plt.figure(figsize=(7, 5))\nax = fig.add_subplot(111, projection='3d')\nsurf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.9)\nfig.colorbar(surf, shrink=0.5)\nax.set_title('z = sin(√(x²+y²))')\nplt.show()"),
        Cell("md", "## 4️⃣ Wireframe y contour"),
        Cell("code", "fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), subplot_kw={'projection': '3d'})\nax1.plot_wireframe(X, Y, Z, color='steelblue', alpha=0.6)\nax1.set_title('wireframe')\nax2.contour3D(X, Y, Z, levels=20, cmap='viridis')\nax2.set_title('contour3D')\nplt.show()"),
        Cell("md", "## 5️⃣ Rotar con `view_init(elev, azim)`"),
        Cell("code", "angles = [(20, 30), (20, 90), (60, 30), (10, 60)]\nfig, axes = plt.subplots(2, 2, figsize=(10, 8), subplot_kw={'projection': '3d'})\nfor ax, (e, a) in zip(axes.flat, angles):\n    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')\n    ax.view_init(elev=e, azim=a)\n    ax.set_title(f'elev={e}, azim={a}')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 🚫 Cuándo NO usar 3D\n\nLa mayoría de las veces, un 2D bien hecho comunica mejor:\n\n- **Scatter 3D con muchos puntos** → confuso por oclusión. Mejor: 2D + color para la 3ª dim.\n- **Bar 3D** → casi siempre engaña en proporciones. Mejor: heatmap o bar agrupado 2D.\n- **Pie 3D** → mentira visual. Usa bar.\n\n**Sí usa 3D para**:\n- Superficies analíticas obvias (z = f(x, y)) cuando la forma 3D **es** el mensaje.\n- Datos físicos con 3 dimensiones reales (geología, partículas).\n- Cuando es interactivo (rotable con `%matplotlib widget`)."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé habilitar 3D con `projection='3d'`\n- [ ] Hago scatter/surface/wireframe/contour 3D\n- [ ] Roto con `view_init`\n- [ ] Pregunto siempre: \"¿hay una versión 2D que comunique mejor?\""),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Scatter 3D, superficie, wireframe, grilla de view_init, versión 2D alternativa."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 4 § 4.12\n- [mplot3d tutorial](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html)\n\n➡️ **Siguiente:** [039 — Seaborn](../039-seaborn-distribuciones-relaciones-categoricas-facetas/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="039-seaborn-distribuciones-relaciones-categoricas-facetas",
    number="039",
    title="Seaborn: distribuciones, relaciones, categóricas, facetas",
    duration="75 min",
    source="VanderPlas, **cap. 4** § 4.13 *Visualization with Seaborn* · seaborn docs.",
    objetivo=(
        "Que el alumno use seaborn cuando aporta sobre matplotlib puro: defaults estéticos, "
        "API tipada para DataFrames (`x=`, `y=`, `hue=`, `col=`), distribuciones (`histplot`, "
        "`kdeplot`, `displot`), relaciones (`scatterplot`, `lmplot`), categóricas (`boxplot`, "
        "`violinplot`, `swarmplot`), y **facetas** (grilla automática por categoría)."
    ),
    resultados=[
        "**Usar la API moderna** (`figure-level` vs `axes-level`) y elegir la correcta.",
        "**Construir un pairplot** para EDA rápido de un DataFrame.",
        "**Codificar 3 dimensiones** con `hue`, `style`, `size`.",
        "**Hacer facetas** con `col=` y `row=` para grillas automáticas.",
        "**Personalizar themes** con `sns.set_theme(style=..., palette=...)`.",
    ],
    temas=[
        ("seaborn vs matplotlib", "Seaborn es matplotlib + defaults + API tipada para DataFrames."),
        ("Figure-level (`displot`, `relplot`, `catplot`) vs axes-level (`histplot`, `scatterplot`, `boxplot`)", "Cuándo cada uno."),
        ("`hue`, `style`, `size`", "Codificar dimensiones extra."),
        ("Facetas con `col`, `row`", "Grilla automática por categoría."),
        ("`pairplot` para EDA", "Matriz de scatters."),
        ("Themes y paletas", "Defaults consistentes."),
    ],
    dataset="Palmer Penguins (seaborn lo trae built-in via `sns.load_dataset('penguins')`).",
    ejercicios=[
        "**Pairplot.** Penguins, color por species. EDA en 1 línea.",
        "**Scatter con hue + size.** body_mass vs flipper, hue por species, size por bill_length.",
        "**KDE distribución.** body_mass por species (3 KDE en mismo plot).",
        "**Boxplot + swarm.** Combinar boxplot con swarm para ver puntos individuales.",
        "**Facetas.** `sns.relplot(...col='species', row='sex')` para 3×2 = 6 subplots automáticos.",
    ],
    homework=(
        "Notebook con penguins: (a) pairplot completo; (b) violin + swarm de body_mass por "
        "(species, sex); (c) faceta 2×3 de scatter; (d) tema custom + paleta; (e) decisión "
        "documentada: cuándo usar figure-level vs axes-level."
    ),
    homework_criterio="Plots de EDA legibles. Decisiones de hue/style/col justificadas.",
    referencias=[
        "VanderPlas, **cap. 4** § 4.13.",
        "[seaborn user guide](https://seaborn.pydata.org/tutorial.html)",
        "Waskom, [seaborn paper (JOSS, 2021)](https://joss.theoj.org/papers/10.21105/joss.03021)",
    ],
    siguiente=("040-visualizacion-geografica-plotly-folium", "Visualización geográfica (Plotly / folium)"),
    cells=[
        Cell("md", "# Clase 039 — Seaborn\n\n**Parte 0** · VanderPlas cap. 4 § 4.13.\n\n> 🎯 matplotlib + defaults + API tipada para DataFrames. Pairplot, hue, facetas.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n\nsns.set_theme(style='whitegrid', palette='deep')\n\ntry:\n    peng = sns.load_dataset('penguins').dropna()\n    print(f'penguins cargado: {peng.shape}')\nexcept Exception as e:\n    print(f'fallback sintético: {e}')\n    rng = np.random.default_rng(42)\n    peng = pd.DataFrame({\n        'species': np.repeat(['Adelie', 'Chinstrap', 'Gentoo'], [50, 30, 40]),\n        'sex'    : np.tile(['Male', 'Female'], 60),\n        'bill_length_mm'  : np.concatenate([rng.normal(39, 2, 50), rng.normal(48, 3, 30), rng.normal(48, 3, 40)]),\n        'bill_depth_mm'   : np.concatenate([rng.normal(18, 1, 50), rng.normal(18, 1, 30), rng.normal(15, 1, 40)]),\n        'flipper_length_mm': np.concatenate([rng.normal(190, 6, 50), rng.normal(196, 7, 30), rng.normal(217, 7, 40)]),\n        'body_mass_g'     : np.concatenate([rng.normal(3700, 400, 50), rng.normal(3700, 400, 30), rng.normal(5050, 500, 40)]),\n    })"),
        Cell("md", "## 1️⃣ Pairplot — EDA en una línea"),
        Cell("code", "g = sns.pairplot(peng, hue='species', diag_kind='kde', height=2)\nplt.show()"),
        Cell("md", "## 2️⃣ Figure-level vs axes-level\n\n| Categoría | Figure-level | Axes-level |\n|---|---|---|\n| Distribuciones | `displot` | `histplot`, `kdeplot`, `ecdfplot` |\n| Relaciones | `relplot` | `scatterplot`, `lineplot` |\n| Categóricas | `catplot` | `boxplot`, `violinplot`, `stripplot`, `swarmplot` |\n\n**Figure-level**: hace su propia figure, soporta facetas (`col`, `row`).  \n**Axes-level**: dibuja en un `ax` que tú le pases — integra con grids matplotlib custom.\n\nRegla simple: si quieres facetas, figure-level. Si necesitas control fino del layout, axes-level."),
        Cell("md", "## 3️⃣ Scatter con hue, style, size"),
        Cell("code", "fig, ax = plt.subplots(figsize=(9, 6))\nsns.scatterplot(\n    data=peng, x='bill_length_mm', y='body_mass_g',\n    hue='species', style='sex', size='flipper_length_mm',\n    sizes=(20, 200), alpha=0.7, ax=ax,\n)\nax.legend(bbox_to_anchor=(1.02, 1), loc='upper left')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 4️⃣ Distribuciones"),
        Cell("code", "fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4))\nsns.histplot(data=peng, x='body_mass_g', hue='species', kde=True, ax=a1)\na1.set_title('histplot + KDE')\nsns.violinplot(data=peng, x='species', y='body_mass_g', ax=a2)\na2.set_title('violin')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 5️⃣ Boxplot + swarmplot combinado"),
        Cell("code", "fig, ax = plt.subplots(figsize=(8, 5))\nsns.boxplot(data=peng, x='species', y='body_mass_g', ax=ax, color='lightgray')\nsns.swarmplot(data=peng, x='species', y='body_mass_g', hue='sex', ax=ax, size=4)\nplt.title('box + swarm (mejor de ambos mundos)')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 6️⃣ Facetas — figure-level"),
        Cell("code", "g = sns.relplot(\n    data=peng, x='bill_length_mm', y='body_mass_g',\n    hue='sex', col='species', kind='scatter', height=4, aspect=1,\n)\ng.set_titles('{col_name}')\nplt.show()"),
        Cell("md", "## 7️⃣ Themes y paletas\n\n```python\nsns.set_theme(\n    style='whitegrid',          # darkgrid, white, dark, ticks\n    palette='deep',             # muted, bright, pastel, dark, colorblind, husl\n    font_scale=1.0,\n)\n```\n\nUn solo `set_theme` afecta todos los plots de la sesión (incluso matplotlib puro)."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Uso pairplot para EDA inicial\n- [ ] Distingo figure-level (facetas) vs axes-level (control fino)\n- [ ] Codifico con hue/style/size\n- [ ] Hago facetas con col=/row=\n- [ ] Configuro tema global con set_theme"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Pairplot, violin+swarm, facetas 2×3, tema custom."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 4 § 4.13\n- [seaborn tutorial](https://seaborn.pydata.org/tutorial.html)\n\n➡️ **Siguiente:** [040 — Visualización geográfica](../040-visualizacion-geografica-plotly-folium/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="040-visualizacion-geografica-plotly-folium",
    number="040",
    title="Visualización geográfica (Plotly / folium)",
    duration="60 min",
    source="Plotly Choropleth docs · folium docs · *Cartographies of the Mind* (background).",
    objetivo=(
        "Que el alumno construya mapas básicos cuando los datos tienen componente geográfico: "
        "**folium** (mapas Leaflet interactivos, markers, choropleth), **plotly** (choropleth, "
        "scatter geo). Sin entrar a GIS profundo (eso es geopandas, fuera del scope de Parte 0)."
    ),
    resultados=[
        "**Crear mapa folium** centrado, con tile layer básico.",
        "**Añadir markers** con popup, tooltip, color según valor.",
        "**Construir choropleth** (mapa de calor por región) con folium o plotly.",
        "**Decidir entre folium y plotly geo** según destino (HTML standalone vs dashboard).",
        "**Citar fuentes** de tiles y GeoJSON públicos.",
    ],
    temas=[
        ("Sistemas de coordenadas: lat/lng", "Convención: lat primero en folium, lng primero en plotly."),
        ("folium: mapa + markers + popups", "Mapas Leaflet en notebook."),
        ("folium choropleth con GeoJSON", "Mapas de calor por país/región."),
        ("plotly choropleth y scatter_geo", "Cuando ya usas plotly."),
        ("Tile providers (OSM, CartoDB)", "Estética y licencia."),
        ("Cuándo geopandas", "Análisis geoespacial real."),
    ],
    dataset=(
        "Sintético: lista de ciudades con coords + métrica simulada. GeoJSON de países "
        "público desde un CDN para choropleth."
    ),
    ejercicios=[
        "**Mapa con markers.** 5 ciudades españolas con marker y popup mostrando nombre + población.",
        "**Markers coloreados.** Mismo, pero color verde si pop>1M, rojo si <500k.",
        "**Choropleth folium.** Mapa mundial con un valor sintético por país (ej: PIB).",
        "**Choropleth plotly.** Lo mismo con `plotly.express.choropleth`.",
        "**Comparar.** ¿Cuándo folium (mapa físico explorable) vs plotly (integra con dashboard)?",
    ],
    homework=(
        "Notebook: (a) mapa folium con 10+ markers + popups + tooltips; (b) choropleth folium "
        "de un dataset por país; (c) mismo choropleth con plotly express; (d) reporte 1-párrafo "
        "comparando ambos."
    ),
    homework_criterio="Mapas funcionales en notebook; popups muestran info correcta; choropleth con leyenda.",
    referencias=[
        "[folium docs](https://python-visualization.github.io/folium/)",
        "[plotly choropleth docs](https://plotly.com/python/choropleth-maps/)",
        "[Natural Earth GeoJSON](https://datahub.io/core/geo-countries)",
    ],
    siguiente=("041-sql-fundamental-select-where-join-group-by-having", "SQL fundamental"),
    cells=[
        Cell("md", "# Clase 040 — Mapas (folium / plotly)\n\n**Parte 0** · folium + plotly docs.\n\n> 🎯 Mapas básicos para datos con componente geográfico. Sin entrar a GIS profundo.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup\n\n```bash\npip install folium plotly\n```"),
        Cell("code", "try:\n    import folium\n    import plotly.express as px\n    print(f'folium: {folium.__version__}')\n    print('plotly OK')\nexcept ImportError as e:\n    print(f'Instala dependencias: pip install folium plotly  ({e})')"),
        Cell("md", "## 1️⃣ folium — mapa con markers"),
        Cell("code", "ciudades = [\n    {'nombre': 'Madrid',    'lat': 40.4168, 'lng': -3.7038, 'pop': 3_300_000},\n    {'nombre': 'Barcelona', 'lat': 41.3851, 'lng':  2.1734, 'pop': 1_640_000},\n    {'nombre': 'Valencia',  'lat': 39.4699, 'lng': -0.3763, 'pop':   800_000},\n    {'nombre': 'Sevilla',   'lat': 37.3891, 'lng': -5.9845, 'pop':   690_000},\n    {'nombre': 'Zaragoza',  'lat': 41.6488, 'lng': -0.8891, 'pop':   680_000},\n]\n\nm = folium.Map(location=[40, -4], zoom_start=6, tiles='OpenStreetMap')\nfor c in ciudades:\n    color = 'green' if c['pop'] > 1_000_000 else ('orange' if c['pop'] > 700_000 else 'red')\n    folium.CircleMarker(\n        location=[c['lat'], c['lng']],\n        radius=8,\n        color=color, fill=True, fill_color=color, fill_opacity=0.7,\n        popup=folium.Popup(f\"<b>{c['nombre']}</b><br>pop: {c['pop']:,}\", max_width=200),\n        tooltip=c['nombre'],\n    ).add_to(m)\n\nm   # en notebook se renderiza inline"),
        Cell("md", "## 2️⃣ Convenciones de coordenadas\n\n⚠️ **Cuidado**:\n- **folium / Leaflet**: `[lat, lng]` (lat primero)\n- **plotly / GeoJSON**: `[lng, lat]` (lng primero, estándar GeoJSON)\n\nEste es el error #1 al hacer mapas."),
        Cell("md", "## 3️⃣ plotly choropleth\n\nMapa de calor por país (o región) — plotly tiene shapes built-in para países usando códigos ISO-3:"),
        Cell("code", "try:\n    import pandas as pd\n    rng = __import__('numpy').random.default_rng(42)\n    \n    paises_iso = ['ESP', 'FRA', 'DEU', 'ITA', 'PRT', 'GBR', 'POL', 'NLD', 'BEL', 'CHE']\n    nombres    = ['España', 'Francia', 'Alemania', 'Italia', 'Portugal', 'Reino Unido', 'Polonia', 'Países Bajos', 'Bélgica', 'Suiza']\n    valor      = rng.uniform(100, 500, len(paises_iso)).round(1)\n    df = pd.DataFrame({'iso': paises_iso, 'nombre': nombres, 'valor': valor})\n    \n    fig = px.choropleth(\n        df, locations='iso', color='valor', hover_name='nombre',\n        color_continuous_scale='Viridis', scope='europe',\n        title='Choropleth Europa (valor sintético)',\n    )\n    fig.show()\nexcept ImportError:\n    print('Instala plotly: pip install plotly')"),
        Cell("md", "## 4️⃣ folium choropleth con GeoJSON\n\n```python\nm = folium.Map(location=[0, 0], zoom_start=2)\nfolium.Choropleth(\n    geo_data='https://...countries.geojson',   # GeoJSON con shapes\n    name='choropleth',\n    data=df,                                    # DataFrame con (codigo, valor)\n    columns=['codigo', 'valor'],\n    key_on='feature.properties.ISO3',          # ruta dentro del GeoJSON\n    fill_color='YlGn',\n    legend_name='valor',\n).add_to(m)\n```\n\nVentaja folium: mapa físico explorable (zoom, pan, popup). plotly: integra mejor con dashboards."),
        Cell("md", "## 5️⃣ Tile providers\n\n- **OpenStreetMap** (default) — colaborativo, gratis.\n- **CartoDB Positron** — limpio y discreto.\n- **CartoDB DarkMatter** — para dark themes.\n- **Stamen Terrain** — relieve.\n- **Mapbox** (require API key).\n\n```python\nfolium.Map(tiles='CartoDB positron')\nfolium.TileLayer('CartoDB dark_matter').add_to(m)   # capa adicional\n```"),
        Cell("md", "## 6️⃣ Cuándo geopandas\n\nEsta clase cubre **mapas para visualización**. Si necesitas:\n- Operaciones espaciales (intersection, buffer, dissolve)\n- Re-proyecciones entre CRS\n- Análisis raster\n\n…usa **geopandas** (extiende pandas con geometrías Shapely). Fuera del scope de Parte 0; aparecería en un curso aparte de GIS."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé crear mapa folium con markers y popups\n- [ ] Conozco el bug lat/lng vs lng/lat\n- [ ] Hago choropleth con folium o plotly\n- [ ] Elijo tile provider según estética\n- [ ] Sé cuándo necesito geopandas (no para esto)"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Mapa con 10+ markers, choropleth folium y plotly, reporte comparativo."),
        Cell("md", "## 🔗 Referencias\n\n- [folium docs](https://python-visualization.github.io/folium/)\n- [plotly choropleth](https://plotly.com/python/choropleth-maps/)\n\n➡️ **Siguiente:** [041 — SQL fundamental](../041-sql-fundamental-select-where-join-group-by-having/README.md)"),
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
