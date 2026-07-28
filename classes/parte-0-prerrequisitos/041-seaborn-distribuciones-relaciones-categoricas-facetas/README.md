# Clase 041 — Seaborn: distribuciones, relaciones, categóricas, facetas

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** § 4.13 *Visualization with Seaborn* · seaborn docs.
> ⏱️ Duración estimada: **75 min**.
> 🎚️ **Nivel:** Básico

---

## 🎯 Objetivo

Que el alumno use seaborn cuando aporta sobre matplotlib puro: defaults estéticos, API tipada para DataFrames (`x=`, `y=`, `hue=`, `col=`), distribuciones (`histplot`, `kdeplot`, `displot`), relaciones (`scatterplot`, `lmplot`), categóricas (`boxplot`, `violinplot`, `swarmplot`), y **facetas** (grilla automática por categoría).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Usar la API moderna** (`figure-level` vs `axes-level`) y elegir la correcta.
2. **Construir un pairplot** para EDA rápido de un DataFrame.
3. **Codificar 3 dimensiones** con `hue`, `style`, `size`.
4. **Hacer facetas** con `col=` y `row=` para grillas automáticas.
5. **Personalizar themes** con `sns.set_theme(style=..., palette=...)`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | seaborn vs matplotlib | Seaborn es matplotlib + defaults + API tipada para DataFrames. |
| 2 | Figure-level (`displot`, `relplot`, `catplot`) vs axes-level (`histplot`, `scatterplot`, `boxplot`) | Cuándo cada uno. |
| 3 | `hue`, `style`, `size` | Codificar dimensiones extra. |
| 4 | Facetas con `col`, `row` | Grilla automática por categoría. |
| 5 | `pairplot` para EDA | Matriz de scatters. |
| 6 | Themes y paletas | Defaults consistentes. |

## 📖 Definiciones y características

**Seaborn**
: Wrapper sobre matplotlib con (1) defaults estéticos mejores, (2) API tipada para DataFrames (`x=`, `y=`, `hue=`), (3) plots estadísticos directos (regresión, distribuciones, facetas).

**Figure-level (displot, relplot, catplot)**
: Funciones que crean su propia figura, soportan **facetas** (`col=`, `row=` para grilla automática). Más alto nivel, menos control fino.

**Axes-level (histplot, scatterplot, boxplot)**
: Funciones que dibujan en un `ax` que tú pasas. Más bajo nivel, integran con layouts custom de matplotlib.

**`hue`, `style`, `size`**
: Codifican dimensiones extra: **`hue`** (color por categoría), **`style`** (marker por categoría), **`size`** (tamaño por valor continuo).

**`pairplot`**
: Matriz de scatterplots de todas las parejas de variables numéricas, diagonal con KDE/histograma. EDA visual en una línea.

**Faceta (col/row)**
: Una sub-figura por cada valor de una categórica. `relplot(..., col='species', row='sex')` produce grilla `n_species × n_sex` de plots automática.

## 📂 Dataset / recursos

Palmer Penguins (seaborn lo trae built-in via `sns.load_dataset('penguins')`).

## 🧪 Ejercicios

**1.** **Pairplot.** Penguins, color por species. EDA en 1 línea.

**2.** **Scatter con hue + size.** body_mass vs flipper, hue por species, size por bill_length.

**3.** **KDE distribución.** body_mass por species (3 KDE en mismo plot).

**4.** **Boxplot + swarm.** Combinar boxplot con swarm para ver puntos individuales.

**5.** **Facetas.** `sns.relplot(...col='species', row='sex')` para 3×2 = 6 subplots automáticos.

## 📝 Homework verificable

Notebook con penguins: (a) pairplot completo; (b) violin + swarm de body_mass por (species, sex); (c) faceta 2×3 de scatter; (d) tema custom + paleta; (e) decisión documentada: cuándo usar figure-level vs axes-level.

**Criterio de aceptación:** Plots de EDA legibles. Decisiones de hue/style/col justificadas.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Mezclo `sns.set_theme()` con `plt.style.use(...)` | Compiten por los rcParams. **Fix**: elige uno. Si usas seaborn, `sns.set_theme(style='whitegrid')` cubre todo. |
| Figure-level no me deja agregar `ax.set_title()` | Devuelve `FacetGrid`, no axes. **Fix**: `g.set_titles('{col_name}')` o `g.fig.suptitle(...)` para título global; `g.axes_dict` para acceder a subplots. |
| `pairplot` con muchas columnas tarda eternidades | N² scatters; con 20 cols son 400 plots. **Fix**: selecciona subset relevante (`peng[['masa','pico','aleta','species']]`) o usa `corr()` heatmap. |
| `hue` con muchas categorías → leyenda enorme | Default muestra todas las categorías. **Fix**: limita con `hue_order=[5 más relevantes]`, o agrupa las menores en "otros". |
| `sns.scatterplot(...)` no aparece en notebook | Falta capturar return o `plt.show()`. **Fix**: asignar a `ax = sns.scatterplot(...)` o llamar `plt.show()` al final. |

## ❓ Preguntas frecuentes

**❓ ¿`seaborn` o `matplotlib` puro?**

**Seaborn** para plots estadísticos rápidos con DataFrame (`hue`, facetas, defaults). **Matplotlib** para control fino, customización extrema, o plots que no son estadísticos.

**❓ ¿Cuándo figure-level vs axes-level?**

**Figure-level** si quieres facetas o el plot es el output completo. **Axes-level** si necesitas integrar con layout custom (subplots manuales).

**❓ ¿`pairplot` o `corrmatrix`?**

**`pairplot`** muestra relaciones visualmente (no lineales, outliers, clusters). **Heatmap de `corr()`** muestra coeficiente Pearson (solo lineal). Complementarios.

**❓ ¿Tema corporativo en seaborn?**

`sns.set_theme(palette=['#0F766E', '#D9A441', '#7C3AED'])` o palette custom: `sns.color_palette('husl', n_colors=5)`. Combina con `style='whitegrid'`.

**❓ ¿Seaborn maneja datasets grandes (>1M)?**

Plots scatter/hist sí. Pairplot con muchas cols se vuelve lento. Para datasets enormes, considera datashader o downsample antes.

## 🔗 Referencias

- VanderPlas, **cap. 4** § 4.13.
- [seaborn user guide](https://seaborn.pydata.org/tutorial.html)
- Waskom, [seaborn paper (JOSS, 2021)](https://joss.theoj.org/papers/10.21105/joss.03021)

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-041-seaborn-distribuciones-relaciones-categoricas-facetas-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-041-seaborn-distribuciones-relaciones-categoricas-facetas-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 042 — Visualización geográfica (Plotly / folium)](../042-visualizacion-geografica-plotly-folium/README.md)
