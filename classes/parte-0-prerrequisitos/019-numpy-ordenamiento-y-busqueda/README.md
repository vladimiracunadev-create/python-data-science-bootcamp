# Clase 019 — NumPy: ordenamiento y búsqueda

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 2** § 2.8 *Sorting Arrays* · NumPy sorting reference.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno ordene arrays con criterio: `sort` vs `argsort`, ordenamiento por eje, partial sort con `partition`, y búsqueda binaria con `searchsorted`. Útil para top-K, rankings, alineación de series.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Ordenar** con `np.sort(arr)` (devuelve copia) y `arr.sort()` (in-place).
2. **Obtener índices del orden** con `argsort` — base de top-K y rankings.
3. **Ordenar por eje** en matrices con `axis=0` o `axis=1`.
4. **Top-K eficiente** con `np.partition` (no ordena completo, solo separa).
5. **Búsqueda binaria** con `np.searchsorted` en arrays ordenados (O(log n)).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `np.sort` vs `arr.sort()` | Copia vs in-place. |
| 2 | `argsort`: el truco del top-K | Índices que ordenarían el array. |
| 3 | Ordenamiento por eje | Por fila o por columna. |
| 4 | `np.partition` para top-K | Más rápido que sort completo. |
| 5 | `np.searchsorted` — binaria O(log n) | Inserción en array ordenado. |
| 6 | `np.unique` | Únicos + opcionalmente cuentas. |

## 📂 Dataset / recursos

Sintético: puntajes de 1M estudiantes. Sin descarga.

## 🧪 Ejercicios

**1.** **Top-10.** Dado array de 1M puntajes, obtén los 10 más altos. Compara `np.sort()[-10:]` vs `np.partition`.

**2.** **Ranking.** Con `argsort`, asigna a cada estudiante su ranking (1 = mejor).

**3.** **Ordena matriz por columna.** Matriz 10×5; ordena cada columna por su valor.

**4.** **Mediana por bisect.** Implementa una función que dado un valor `v` y un array ordenado, devuelve su posición percentil usando `searchsorted`.

**5.** **`np.unique` con cuentas.** Dado array de categorías, obtén valores únicos y sus frecuencias.

## 📝 Homework verificable

Notebook con array de 100k puntajes: (a) top-100 con `partition` y benchmark vs sort completo; (b) ranking con `argsort.argsort()`; (c) percentil de un valor dado con `searchsorted`; (d) `unique` con `return_counts` y barplot top-10 categorías.

**Criterio de aceptación:** `partition` >10× más rápido que sort completo para N=100k y K=100.

## 🔗 Referencias

- VanderPlas, **cap. 2** § 2.8.
- [NumPy sorting reference](https://numpy.org/doc/stable/reference/routines.sort.html)

## ➡️ Siguiente clase

[Clase 020 — NumPy: álgebra lineal con numpy.linalg](../020-numpy-algebra-lineal-con-numpy-linalg/README.md)
