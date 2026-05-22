# Clase 025 — Pandas: datos faltantes

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.5 *Handling Missing Data*.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno **detecte, cuantifique y maneje** datos faltantes con criterio. Eliminar es la opción fácil pero suele ser incorrecta: cuándo eliminar, cuándo imputar (media, mediana, forward-fill), y cuándo el faltante es **señal** que merece su propia columna.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Detectar** NaN con `isna()`, `notna()` y cuantificar por columna/fila.
2. **Eliminar** filas/columnas con NaN usando `dropna` con `how`/`thresh`/`subset`.
3. **Imputar** con `fillna`: valor escalar, media/mediana, forward/backward fill, interpolación.
4. **Distinguir** `NaN` vs `None` vs `pd.NA` y por qué importan los dtypes nullable (`Int64`, `boolean`).
5. **Decidir** entre eliminar/imputar/dejar — y crear columna `was_missing` cuando el faltante es informativo.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Tipos de missing en pandas: NaN, None, NaT, pd.NA | Cada uno tiene caso de uso. |
| 2 | Detección: `isna`, `notna`, `isna().sum()` | First-look obligatorio. |
| 3 | `dropna`: how='any'/'all', thresh, subset | Eliminar con precisión. |
| 4 | `fillna`: escalar, dict, ffill, bfill, interpolate | Imputar según contexto. |
| 5 | Dtypes nullable: Int64, Float64, boolean | El nuevo missing nativo. |
| 6 | `was_missing` como feature | Cuando el missing es señal. |

## 📂 Dataset / recursos

Palmer Penguins (tiene NaN reales en sex y mediciones). Sin descarga adicional si ya está en clases anteriores.

## 🧪 Ejercicios

**1.** **Cuantifica.** Carga penguins, reporta % de NaN por columna y por fila.

**2.** **Eliminar filas con cualquier NaN.** `df.dropna(how='any')`. Compara shape antes/después.

**3.** **Eliminar solo filas con NaN en `sex`.** `df.dropna(subset=['sex'])`. Más selectivo.

**4.** **Imputar.** Rellena `bill_length_mm` con la mediana **por especie** (groupby + transform). Justifica por qué la mediana es mejor que la media aquí.

**5.** **Forward fill en series temporales.** Crea una Series con NaN intercalados. Aplica `ffill`, `bfill`, `interpolate`. Compara.

## 📝 Homework verificable

Notebook con penguins: (a) reporte completo de missing (% por col, % por fila, filas más incompletas); (b) 3 estrategias: drop all, drop subset, imputar por grupo; (c) columna `bill_was_missing` y demuestra que el flag puede mejorar un modelo simple; (d) demo de dtypes nullable `Int64`.

**Criterio de aceptación:** Imputación por grupo no introduce sesgo; el flag was_missing añade información.

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.5.
- [pandas — Missing data user guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [pandas nullable Integer dtypes](https://pandas.pydata.org/docs/user_guide/integer_na.html)

## ➡️ Siguiente clase

[Clase 026 — Pandas: MultiIndex](../026-pandas-multiindex/README.md)
