# Clase 015 — NumPy: ufuncs y vectorización

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 2**, § 2.3 *Computation on NumPy Arrays: Universal Functions*.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno **abandone los `for` loops** sobre arrays NumPy y use ufuncs (universal functions) para operaciones elementwise — la fuente real del speedup. Ufuncs son C compilado vectorizado; un `for` Python sobre array es lo peor de ambos mundos.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Identificar** una ufunc (`np.add`, `np.multiply`, `np.sin`, `np.exp`, `np.log`, comparadores).
2. **Reemplazar** un `for+append` por una expresión vectorizada y medir el speedup.
3. **Usar el parámetro `out=`** para escribir el resultado in-place (evita allocar memoria extra).
4. **Combinar** ufuncs con operadores aritméticos (`+`, `-`, `*`, `/`, `**`).
5. **Reconocer** las trampas de la vectorización (overflow, NaN propagación, división por cero).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | ¿Qué es una ufunc? | Función C vectorizada elementwise. |
| 2 | Ufuncs unarias y binarias | `np.exp(x)` vs `np.add(x, y)`. |
| 3 | Operadores → ufuncs | `a + b` ≡ `np.add(a, b)`. |
| 4 | `out=` para in-place | Memoria O(1) extra. |
| 5 | Trampas: overflow, NaN, inf, división por cero | NumPy avisa pero no para. |
| 6 | `np.where(cond, a, b)` | Ternario vectorizado. |

## 📂 Dataset / recursos

Sintético: arrays grandes para benchmark. Sin descarga.

## 🧪 Ejercicios

**1.** **Benchmark.** Calcula `[x*x + 2*x + 1 for x in range(1_000_000)]` vs `arr*arr + 2*arr + 1`. Mide con `%timeit`.

**2.** **Logaritmo y exponencial.** Con `np.exp` y `np.log`, verifica que `log(exp(x)) ≈ x` para 1000 valores. Reporta el error máximo.

**3.** **In-place vs alloc.** `arr = arr * 2 + 1` vs `np.multiply(arr, 2, out=arr); np.add(arr, 1, out=arr)`. Compara `tracemalloc`.

**4.** **`np.where` ternario.** Dado un array de notas, crea otro array con `'aprobado'` si nota >= 4, `'reprobado'` si no.

**5.** **Trampa NaN.** Crea `np.array([1, 2, np.nan, 4]).sum()` y `.mean()`. Compara con `np.nansum` y `np.nanmean`.

## 📝 Homework verificable

Notebook: (a) reescribe 3 loops como expresiones vectorizadas + tabla con `%timeit` (3 N distintos); (b) demuestra `out=` con `tracemalloc`; (c) usa `np.where` para clasificar datos; (d) maneja NaN con `nansum/nanmean` y compara con propagación.

**Criterio de aceptación:** Speedup >50× en N=1M. `out=` muestra memoria ≈ 0 extra. NaN-handling correcto.

## 🔗 Referencias

- VanderPlas, **cap. 2** § 2.3 *Computation on NumPy Arrays*.
- [NumPy ufuncs reference](https://numpy.org/doc/stable/reference/ufuncs.html)

## ➡️ Siguiente clase

[Clase 016 — NumPy: agregaciones](../016-numpy-agregaciones/README.md)
