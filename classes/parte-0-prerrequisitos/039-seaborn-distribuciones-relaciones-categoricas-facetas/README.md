# Clase 039 — Seaborn: distribuciones, relaciones, categóricas, facetas

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** § 4.13 *Visualization with Seaborn* · seaborn docs.
> ⏱️ Duración estimada: **75 min**.

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

## 🔗 Referencias

- VanderPlas, **cap. 4** § 4.13.
- [seaborn user guide](https://seaborn.pydata.org/tutorial.html)
- Waskom, [seaborn paper (JOSS, 2021)](https://joss.theoj.org/papers/10.21105/joss.03021)

## ➡️ Siguiente clase

[Clase 040 — Visualización geográfica (Plotly / folium)](../040-visualizacion-geografica-plotly-folium/README.md)
