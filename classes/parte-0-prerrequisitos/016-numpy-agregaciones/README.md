# Clase 016 — NumPy: agregaciones

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 2** § 2.4 *Aggregations: Min, Max, and Everything in Between*.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno reduzca arrays a estadísticos (sum, mean, std, percentile, min, max) controlando el `axis` correcto — la fuente del 50% de los bugs de pandas/sklearn cuando alguien se confunde de eje. También: variantes `nan*` y reducciones acumulativas.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Calcular** sum, mean, std, var, median, percentile sobre arrays.
2. **Controlar el eje** con `axis=0` (a lo largo de filas, da resultado por columna) y `axis=1` (a lo largo de columnas, da por fila).
3. **Usar variantes `nan*`** (nansum, nanmean, etc.) cuando hay datos faltantes.
4. **Reducciones acumulativas** con `cumsum` y `cumprod`.
5. **Encontrar índice** del min/max con `argmin`/`argmax`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Reducciones básicas | sum, mean, std, var, min, max, median, percentile. |
| 2 | Eje: el bug más común | `axis=0` reduce filas (resultado por columna). |
| 3 | Variantes NaN-aware | nansum, nanmean, nanmedian, nanstd. |
| 4 | Acumulativas | cumsum, cumprod — útiles para series temporales. |
| 5 | argmin/argmax | Posición del extremo. |
| 6 | `all` y `any` | Reducciones booleanas. |

## 📂 Dataset / recursos

Sintético (matriz aleatoria 100×10 simulando "10 features × 100 muestras") generado en el notebook. Sin descarga.

## 🧪 Ejercicios

**1.** **Promedio por columna.** Dada matriz 100×4 de ventas (filas=día, cols=tienda), calcula la media por tienda y por día.

**2.** **Estadísticos completos.** Para un array de 1000 normales, reporta mean, std, median, p25, p75, min, max.

**3.** **Con NaN.** Inserta 50 NaN aleatorios en el array anterior. Compara `mean` (propaga) vs `nanmean`.

**4.** **Cumsum.** Genera array de retornos diarios aleatorios. Calcula el precio acumulado con `cumprod(1+r)`.

**5.** **Mejor tienda.** Con la matriz del ejercicio 1, usa `argmax(axis=0)` para encontrar el día de mayor venta de cada tienda.

## 📝 Homework verificable

Notebook con matriz simulada 365 días × 5 tiendas de ventas, reportando: media/std por tienda, mejor y peor día de cada tienda, cumsum total anual, % de días con NaN simulados (20 aleatorios) usando variantes nan*.

**Criterio de aceptación:** Eje correcto en todas las agregaciones; valores reproducibles con seed.

## 🔗 Referencias

- VanderPlas, **cap. 2** § 2.4.
- [NumPy statistics functions](https://numpy.org/doc/stable/reference/routines.statistics.html)

## ➡️ Siguiente clase

[Clase 017 — NumPy: broadcasting](../017-numpy-broadcasting/README.md)
