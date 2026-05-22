# Clase 007 — Comprehensions y generadores

> Parte: **0 — Prerrequisitos** · Fuente: Ramalho, *Fluent Python* 2e — caps. 2 (Sequences) y 17 (Iterators, Generators, Coroutines).
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno escriba código Python idiomático: list/dict/set comprehensions en vez de for+append, generadores cuando el dataset no cabe en memoria, y entienda la diferencia fundamental entre **construir una lista** y **producir un iterable perezoso**.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Convertir** loops `for+append` a list/dict/set comprehensions sin perder legibilidad.
2. **Usar generadores** (`yield` y generator expressions) para procesar datos que no caben en RAM.
3. **Distinguir** `[x for x in xs]` (lista) vs `(x for x in xs)` (generador): memoria y consumo.
4. **Encadenar** generadores con `itertools` (`chain`, `islice`, `takewhile`, `groupby`).
5. **Identificar** cuándo NO usar comprehension (lógica compleja, side effects, debug difícil).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | List comprehension: `[expr for x in xs if cond]` | Idiomático, eficiente, legible si es simple. |
| 2 | Dict/set comprehensions | Mismo patrón, otra estructura. |
| 3 | Generator expressions: `(expr for x in xs)` | Perezoso, memoria O(1). |
| 4 | Funciones generadoras con `yield` | Reescribe procesos como streams. |
| 5 | `itertools` — la caja de herramientas | `chain`, `islice`, `groupby`, `accumulate`, `combinations`. |
| 6 | Comprehension vs loop: cuándo NO | Lógica >2 líneas, side effects, debug. |

## 📂 Dataset / recursos

Datos sintéticos: rango grande de números (1M elementos) para mostrar diferencia memoria lista vs generador. Sin descarga.

## 🧪 Ejercicios

**1.** **De for a comprehension.** Toma 3 loops `for+append` (cuadrados, filtra pares, mapea a strings) y conviértelos.

**2.** **Generador de Fibonacci infinito.** Función con `yield` que produce Fibonacci. Úsala con `itertools.islice` para tomar los primeros 20.

**3.** **Memoria: lista vs generador.** Mide RAM (con `tracemalloc`) de `sum([i*i for i in range(10_000_000)])` vs `sum(i*i for i in range(10_000_000))`. Reporta la diferencia.

**4.** **Procesa CSV línea por línea.** Lee un archivo grande con `yield` línea por línea, filtra por una condición, cuenta sin cargar todo en memoria.

**5.** **Pivot con dict comprehension.** Dada `list[tuple[str, int]]` (nombre, puntaje), construye `dict[str, list[int]]` agrupando puntajes por nombre.

## 📝 Homework verificable

Notebook que: (1) reescribe 3 loops como comprehensions, (2) implementa generador Fibonacci con `islice`, (3) comparativa RAM lista vs generador con `tracemalloc` y tabla de resultados, (4) lee un CSV ≥10k filas con generador y filtra sin cargar entero.

**Criterio de aceptación:** La medición de RAM muestra >100× menos memoria con generador. CSV se procesa sin OOM.

## 🔗 Referencias

- Ramalho, *Fluent Python* 2e — caps. 2 y 17.
- [PEP 202 — List Comprehensions](https://peps.python.org/pep-0202/)
- [PEP 255 — Simple Generators](https://peps.python.org/pep-0255/)
- [`itertools` docs](https://docs.python.org/3/library/itertools.html)

## ➡️ Siguiente clase

[Clase 008 — Funciones: args, kwargs, lambdas, closures](../008-funciones-args-kwargs-lambdas-closures/README.md)
