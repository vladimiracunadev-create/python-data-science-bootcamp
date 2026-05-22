# Clase 029 — Pandas: pivot tables y crosstab

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.10 *Pivot Tables*.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno construya tablas pivot (estilo Excel) con `pivot_table` y tablas de contingencia con `crosstab`. Son atajos sobre groupby pensados para **resumen×visualización rápida**.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Usar `pivot_table`** con `index`, `columns`, `values`, `aggfunc`.
2. **Añadir totales** con `margins=True`.
3. **Construir tablas de contingencia** con `pd.crosstab` y normalizar (`normalize='all'/'index'/'columns'`).
4. **Diferenciar** `pivot` (sin agregar) vs `pivot_table` (con aggfunc, agrega duplicados).
5. **Visualizar** una pivot como heatmap básico para confirmar patrones.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `pivot` vs `pivot_table` | pivot no acepta duplicados; pivot_table sí (agrega). |
| 2 | Parámetros: index, columns, values, aggfunc | Análogos a Excel. |
| 3 | `margins=True`: totales | Útil para verificar. |
| 4 | `crosstab`: tabla de contingencia | Counts entre dos categóricas. |
| 5 | `normalize` en crosstab | Proporciones por fila/col/total. |
| 6 | Pivot → heatmap | Detectar patrones visualmente. |

## 📂 Dataset / recursos

Palmer Penguins. Sin descarga adicional.

## 🧪 Ejercicios

**1.** **Pivot básico.** Penguins: índice species, columnas sex, valores body_mass mean.

**2.** **Pivot con totales.** Mismo con `margins=True`.

**3.** **Crosstab counts.** Counts species × island.

**4.** **Crosstab normalizado.** Mismo con `normalize='index'` (% por fila).

**5.** **Pivot → heatmap.** Toma un pivot table y plotéala con matplotlib `imshow`.

## 📝 Homework verificable

Notebook con penguins: (a) pivot_table (species × island, mean body_mass); (b) crosstab species × island, count y normalizado; (c) verificación de totales con margins; (d) heatmap simple del pivot.

**Criterio de aceptación:** Pivot con shape correcto; sum de normalize='index' = 1.0 por fila.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.10.
- [pandas Pivot guide](https://pandas.pydata.org/docs/user_guide/reshaping.html)

## ➡️ Siguiente clase

[Clase 030 — Pandas: operaciones vectorizadas sobre strings](../030-pandas-operaciones-vectorizadas-sobre-strings/README.md)
