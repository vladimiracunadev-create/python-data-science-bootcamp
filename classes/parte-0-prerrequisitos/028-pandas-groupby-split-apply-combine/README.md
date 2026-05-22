# Clase 028 — Pandas: groupby (split-apply-combine)

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.9 *Aggregation and Grouping*.
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno aplique el patrón **split-apply-combine** que es **el** patrón fundamental de análisis tabular: dividir por grupo, aplicar función, recombinar. Saber elegir entre `agg`, `transform`, `filter` y `apply` — cada uno tiene su rol.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Agrupar** por una o más columnas con `groupby` y aplicar agregaciones (`sum`, `mean`, `count`).
2. **Usar `agg` con dict** para distintas funciones por columna: `agg({'a': 'sum', 'b': 'mean'})`.
3. **`transform`** para preservar la shape original (broadcasting del estadístico de grupo).
4. **`filter`** para filtrar grupos enteros según condición.
5. **Diferenciar** los 4 métodos del groupby y elegir el correcto.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Split-apply-combine: el patrón | El más común en análisis tabular. |
| 2 | `agg` (= aggregate) | Reduce a una fila por grupo. |
| 3 | `transform` | Misma shape — útil para imputar/normalizar por grupo. |
| 4 | `filter` | Conserva grupos completos según condición. |
| 5 | `apply`: el más flexible, el más lento | Cuando los 3 anteriores no alcanzan. |
| 6 | Múltiples columnas de agrupación | groupby(['a','b']) → MultiIndex. |

## 📂 Dataset / recursos

Palmer Penguins (groupby por species y/o sex).

## 🧪 Ejercicios

**1.** **Agg básico.** Penguins agrupado por species: media de cada feature numérica.

**2.** **Agg con dict.** Por species: mean de bill_length, max de body_mass, count de filas.

**3.** **Transform: z-score por grupo.** Crea columna `mass_z` = z-score de body_mass dentro de su species.

**4.** **Filter: solo grupos grandes.** Conserva solo species con >100 individuos.

**5.** **Apply custom.** Por species, devuelve el pingüino con mayor body_mass (un DataFrame por grupo).

## 📝 Homework verificable

Notebook con penguins: (a) agg múltiple por (species, sex); (b) transform z-score por species; (c) filter species con n>50; (d) apply que devuelva el top-3 más pesado por species; (e) tabla `groupby.size()` por sex × island.

**Criterio de aceptación:** z-score por grupo tiene media ≈ 0 y std ≈ 1 dentro de cada species.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.9.
- [pandas groupby user guide](https://pandas.pydata.org/docs/user_guide/groupby.html)
- Wickham, ["The split-apply-combine strategy for data analysis"](https://www.jstatsoft.org/article/view/v040i01) (J Stat Software, 2011).

## ➡️ Siguiente clase

[Clase 029 — Pandas: pivot tables y crosstab](../029-pandas-pivot-tables-y-crosstab/README.md)
