# Clase 014 — NumPy: tipos, creación, atributos

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, *Python Data Science Handbook*, **cap. 2** — *Introduction to NumPy*, §§ 2.1–2.2.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno entienda el modelo mental de un `ndarray` — bloque contiguo de memoria con shape, dtype y strides — y sepa crear arrays de las 6 formas más útiles (`array`, `zeros`, `arange`, `linspace`, `random`, desde lista). Sin este modelo, todo el rendimiento de NumPy parece magia.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Explicar** por qué `ndarray` es 50–100× más rápido que `list` (memoria contigua + dtype fijo + sin overhead Python).
2. **Crear arrays** con `np.array`, `np.zeros`, `np.ones`, `np.full`, `np.arange`, `np.linspace`.
3. **Inspeccionar** un array con `shape`, `dtype`, `ndim`, `size`, `nbytes`, `itemsize`.
4. **Cambiar dtype** explícitamente con `astype` y entender promociones implícitas (`int + float = float`).
5. **Generar arrays aleatorios reproducibles** con `np.random.default_rng(seed)`.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `ndarray`: memoria contigua + dtype fijo | Lo que lo hace rápido. |
| 2 | Creación: `array`, `zeros`, `arange`, `linspace` | Las 6 formas más usadas. |
| 3 | `dtype`: int8/16/32/64, float32/64, bool | Memoria y precisión. |
| 4 | Atributos: shape, dtype, ndim, size, nbytes | Diagnóstico instantáneo. |
| 5 | `astype` y promoción de tipos | El bug clásico de overflow int8. |
| 6 | `random` moderno: `default_rng(seed)` | El API legacy `np.random.seed` está deprecated. |

## 📂 Dataset / recursos

Sintético: arrays generados en el notebook (escalares, matrices, aleatorios reproducibles). Sin descarga.

## 🧪 Ejercicios

**1.** **Memoria.** Crea `list(range(1_000_000))` y `np.arange(1_000_000)`. Compara `sys.getsizeof` y `arr.nbytes`. Calcula el ratio.

**2.** **Las 6 formas.** Crea: vector 100 ceros, matriz 5×5 unos, vector 0..1 con 50 puntos equiespaciados, matriz 3×3 de 7s, vector de 100 aleatorios uniformes [0,1).

**3.** **Bug de dtype.** Crea `np.array([100, 200, 50], dtype=np.int8)` y suma 200 a cada elemento. Observa el resultado y explica.

**4.** **Diagnóstico.** Dado un array, escribe una función que imprima shape, dtype, ndim, size, nbytes y memoria humana (KB/MB).

**5.** **Random reproducible.** Genera 1000 normales N(0,1) con seed=42. Calcula media y std. Repite — debe dar exactamente lo mismo.

## 📝 Homework verificable

Notebook que: (a) compara memoria list vs ndarray para N=1M con tabla; (b) crea las 6 formas y reporta dtype default de cada una; (c) reproduce el bug de overflow int8 con explicación; (d) función `info(arr)` con diagnóstico completo.

**Criterio de aceptación:** El ratio memoria list/ndarray es >5×. La función `info` reporta todos los atributos.

## 🔗 Referencias

- VanderPlas, **cap. 2**, §§ 2.1–2.2 *Understanding Data Types* + *The Basics of NumPy Arrays*.
- [NumPy user guide — Array creation](https://numpy.org/doc/stable/user/basics.creation.html)
- [NumPy dtypes](https://numpy.org/doc/stable/reference/arrays.dtypes.html)
- [`Generator` random API](https://numpy.org/doc/stable/reference/random/generator.html)

## ➡️ Siguiente clase

[Clase 015 — NumPy: ufuncs y vectorización](../015-numpy-ufuncs-y-vectorizacion/README.md)
