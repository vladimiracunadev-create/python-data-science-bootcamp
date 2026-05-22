# Clase 008 — Funciones: args, kwargs, lambdas, closures

> Parte: **0 — Prerrequisitos** · Fuente: Ramalho, *Fluent Python* 2e — cap. 7 (Functions as First-Class Objects), cap. 9 (Decorators and Closures).
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno use funciones como ciudadanos de primera clase: pasarlas como argumento, retornarlas, escribir lambdas cuando aportan, y entender closures — la base de los decoradores que verán más adelante. Sin esto, el código pandas/sklearn parece magia.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Definir funciones** con argumentos posicionales, keyword-only, `*args` y `**kwargs`.
2. **Pasar funciones como argumento** (callbacks: `sorted(xs, key=fn)`, `df.apply(fn)`).
3. **Usar lambdas** donde son legibles (callbacks cortos) y evitarlas donde no (lógica).
4. **Explicar y escribir closures** (función que captura variables del scope exterior).
5. **Anticipar** la diferencia entre `*args` y `*, args` (keyword-only marker).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Argumentos: posicional, keyword, default | Cuatro modos, una sintaxis. |
| 2 | `*args` y `**kwargs` | Funciones que aceptan número variable. |
| 3 | Keyword-only con `*` separador | `def f(a, *, b)` → b solo nombrado. |
| 4 | Funciones como objetos | Asignables, pasables, retornables. |
| 5 | Lambdas: dónde sí y dónde no | Callbacks cortos sí; lógica compleja no. |
| 6 | Closures: capturando scope | Base mental de los decoradores. |

## 📂 Dataset / recursos

Datos sintéticos pequeños (lista de dicts simulando ventas). Sin descarga.

## 🧪 Ejercicios

**1.** **Función con todo.** Define `f(a, b=10, *args, c, **kwargs)`. Llámala de 3 formas distintas que sean válidas. Identifica qué llamadas son inválidas y por qué.

**2.** **`sorted` con key.** Dada `list[dict]` de personas, ordena por edad (asc) y por nombre alfabético. Usa lambda primero, luego `operator.itemgetter`.

**3.** **Closure contador.** Escribe `make_counter()` que retorna una función que cada vez que se llama incrementa y retorna un contador interno. ¿Por qué funciona?

**4.** **Memoización manual.** Implementa un decorador `@memoize` usando closure + dict. Aplícalo a Fibonacci recursivo y mide el speedup con `%timeit`.

**5.** **Compose.** Escribe `compose(f, g, h)` que retorna una función equivalente a `lambda x: f(g(h(x)))`.

## 📝 Homework verificable

Notebook con: (a) implementación y demo de `make_counter` explicando con comentario por qué el contador persiste; (b) `@memoize` aplicado a Fibonacci recursivo con benchmark (N=35) antes/después; (c) ordenamiento de `list[dict]` por 2 criterios usando `itemgetter`.

**Criterio de aceptación:** `memoize` reduce Fibonacci(35) de segundos a milisegundos. Counter independiente entre instancias.

## 🔗 Referencias

- Ramalho, *Fluent Python* 2e — caps. 7 y 9.
- [Python docs — More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [PEP 3102 — Keyword-Only Arguments](https://peps.python.org/pep-3102/)

## ➡️ Siguiente clase

[Clase 009 — Manejo de excepciones y context managers](../009-manejo-de-excepciones-y-context-managers/README.md)
