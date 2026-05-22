# Clase 031 — Pandas: series de tiempo, resampling, rolling

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 3** § 3.12 *Working with Time Series*.
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno trabaje con datos temporales correctamente: parsear fechas, indexar por `DatetimeIndex`, hacer **resampling** (cambiar la frecuencia) y **rolling** (ventanas móviles para tendencias).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Parsear** strings de fecha con `pd.to_datetime(..., format=..., errors=...)`.
2. **Indexar** por `DatetimeIndex` y slicear con strings de fecha (`df.loc['2024-01':'2024-03']`).
3. **Resamplear** a otra frecuencia: `df.resample('M').sum()`, `'W'`, `'D'`, `'H'`.
4. **Aplicar ventanas móviles** con `rolling(window).mean()` para suavizar tendencias.
5. **Manejar zonas horarias** con `tz_localize` y `tz_convert`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `pd.to_datetime` con errors='coerce' | Parseo robusto. |
| 2 | DatetimeIndex y slicing por fecha | Sintaxis natural: `'2024-01':'2024-03'`. |
| 3 | Resampling: 'D', 'W', 'M', 'Q', 'Y', 'H' | Cambiar frecuencia + agregar. |
| 4 | Rolling windows | Suavizado, medias móviles. |
| 5 | `shift` y `diff` | Diferencias entre periodos, lag features. |
| 6 | Timezones: localize → convert | Cuando los datos tienen TZ. |

## 📂 Dataset / recursos

Sintético: serie diaria de 2 años de ventas. Sin descarga.

## 🧪 Ejercicios

**1.** **Parseo robusto.** Lista de fechas con formatos mixtos (`'2024-01-15'`, `'15/02/2024'`, `'foo'`). Parsea con `errors='coerce'`. Reporta NaT.

**2.** **Slice por fecha.** Con índice datetime, selecciona Q1 2024 con `df.loc['2024-01':'2024-03']`.

**3.** **Resample diaria → mensual.** Suma ventas por mes con `df.resample('M').sum()`.

**4.** **Rolling 7-day mean.** Calcula media móvil de 7 días sobre ventas diarias. Plotea junto a la serie original.

**5.** **`shift` para lag feature.** Crea columna `ventas_lag_1` con `shift(1)`. Útil para features de ML.

## 📝 Homework verificable

Notebook con serie sintética de 2 años: (a) parseo robusto; (b) slice por trimestre; (c) resample a mensual con sum y mean; (d) rolling 7/30 días con plot; (e) diff y pct_change para variación.

**Criterio de aceptación:** Plots muestran tendencia clara. Resample correcto (#meses esperado).

## 🔗 Referencias

- VanderPlas, **cap. 3** § 3.12.
- [pandas Time Series user guide](https://pandas.pydata.org/docs/user_guide/timeseries.html)

## ➡️ Siguiente clase

[Clase 032 — Pandas: eval y query](../032-pandas-eval-y-query/README.md)
