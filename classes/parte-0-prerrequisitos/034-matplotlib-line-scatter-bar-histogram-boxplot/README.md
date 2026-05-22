# Clase 034 — Matplotlib: line, scatter, bar, histogram, boxplot

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** §§ 4.2–4.5 *Simple Line/Scatter/Bar/Histogram Plots*.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno conozca los **5 plots básicos** que cubren el 80% del trabajo de EDA, y sepa **cuándo cada uno**: line (tendencia temporal), scatter (relación dos variables), bar (categóricas), histogram (distribución), boxplot (5 estadísticos + outliers).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Elegir el plot correcto** según el tipo de variables (continua/categórica) y el objetivo.
2. **Ajustar marker, color, linestyle, alpha** para legibilidad.
3. **Construir histogramas** con bins adecuados (regla de Freedman-Diaconis o `'auto'`).
4. **Interpretar boxplot**: mediana, Q1/Q3, whiskers, outliers.
5. **Combinar** bar + error bars para mostrar incertidumbre.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Line: tendencias y series temporales | El más fácil de leer mal. |
| 2 | Scatter: relación entre dos variables | Con `c=` y `s=` para 3ª/4ª dimensión. |
| 3 | Bar y barh: categóricas | Vertical vs horizontal. |
| 4 | Histogram: distribución de una continua | Bins importan. |
| 5 | Boxplot: distribución resumida + outliers | Cuando hay muchos grupos. |
| 6 | Errorbar y fill_between | Mostrar incertidumbre. |

## 📂 Dataset / recursos

Palmer Penguins. Sin descarga adicional.

## 🧪 Ejercicios

**1.** **Line.** Serie temporal de ventas mensuales (sintética). Anota máximo con flecha.

**2.** **Scatter.** body_mass vs bill_length, color por species. Adicionalmente: `s=` con flipper_length para tamaño.

**3.** **Bar.** Count por species, ordenado descendente. Vertical y horizontal — compara legibilidad.

**4.** **Histogram.** Distribución de body_mass con bins='auto' y bins=10. Compara.

**5.** **Boxplot.** body_mass por species: 3 cajas lado a lado. Identifica outliers.

## 📝 Homework verificable

Notebook con penguins: (a) 5 plots básicos cada uno bien etiquetado; (b) scatter decorado con color y tamaño codificando 3 dimensiones; (c) bar con errorbars de std; (d) boxplot agrupado con interpretación de outliers.

**Criterio de aceptación:** Cada plot tiene título, labels, leyenda donde aplica. Bins justificados.

## 🔗 Referencias

- VanderPlas, **cap. 4** §§ 4.2-4.5.
- [matplotlib gallery](https://matplotlib.org/stable/gallery/index.html)

## ➡️ Siguiente clase

[Clase 035 — Matplotlib: subplots y gridspec](../035-matplotlib-subplots-y-gridspec/README.md)
