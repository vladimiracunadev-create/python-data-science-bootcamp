# Clase 006 — Python: tipos, estructuras, control de flujo

> Parte: **0 — Prerrequisitos** · Fuente: *Python Tutorial* oficial (caps. 3-5) · *Fluent Python* (Ramalho, 2ª ed.) cap. 1.
> ⏱️ Duración estimada: **120 min**.

---

## 🎯 Objetivo

Refrescar (o instalar) los cimientos de Python que el resto del programa asume: tipos primitivos, las 4 estructuras built-in (list, tuple, set, dict), control de flujo (if/for/while), unpacking, truthiness y la diferencia entre mutables e inmutables — la fuente del 90% de bugs sutiles.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Diferenciar** tipos mutables (list, dict, set) vs inmutables (tuple, str, int, frozenset) y predecir el efecto en asignaciones.
2. **Usar las 4 estructuras** eligiendo bien: list (orden + duplicados), tuple (inmutable, rápida), set (unicidad), dict (lookup O(1)).
3. **Aplicar unpacking** en for, returns múltiples y `*args`/`**kwargs`.
4. **Evaluar truthiness** correctamente (`[]`, `{}`, `0`, `''`, `None` son falsy; el resto es truthy).
5. **Identificar el bug del default mutable** en funciones (`def f(x, lst=[])`) y por qué es trampa.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Mutables vs inmutables | Define qué pasa con `a = b`. |
| 2 | list, tuple, set, dict — cuándo cada uno | Complejidad y semántica distintas. |
| 3 | Iteración: for, enumerate, zip | Idiomático > C-style. |
| 4 | Unpacking y starred expressions | `a, *b, c = [1,2,3,4,5]`. |
| 5 | Truthiness y operadores `and`/`or` | Evalúan al objeto, no al booleano. |
| 6 | Default mutables: el clásico | `def f(x, lst=[])` comparte la lista entre llamadas. |

## 📂 Dataset / recursos

Datos sintéticos pequeños generados en el notebook (lista de diccionarios simulando estudiantes). No requiere descarga.

## 🧪 Ejercicios

**1.** **Cuenta palabras.** Dado un texto, devuelve un `dict[str, int]` con frecuencias. Sin usar `Counter`.

**2.** **Unique con orden.** Recibe `list[int]`, devuelve la lista de únicos manteniendo el orden de primera aparición.

**3.** **Reproduce el bug del default mutable.** Escribe `def add(item, target=[])`, llámala 3 veces con `add('x')`. Observa. Explica por qué y arregla.

**4.** **Top-K palabras.** Mismo texto del ejercicio 1, devuelve las 5 más frecuentes ordenadas por frecuencia descendente.

**5.** **Grupos por inicial.** Dado `list[str]`, devuelve `dict[str, list[str]]` agrupando por primera letra (case-insensitive).

## 📝 Homework verificable

Notebook `homework.ipynb` con las 5 funciones de los ejercicios, cada una con: (a) implementación, (b) 3 casos de prueba (incluyendo edge cases — lista vacía, string vacío), (c) docstring corto explicando complejidad.

**Criterio de aceptación:** Las 5 funciones pasan sus casos de prueba; los edge cases manejados sin excepción.

## 🔗 Referencias

- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
- Ramalho, *Fluent Python* 2e — cap. 1 *The Python Data Model*.
- [Python Tutorial — Control flow](https://docs.python.org/3/tutorial/controlflow.html)

## ➡️ Siguiente clase

[Clase 007 — Comprehensions y generadores](../007-comprehensions-y-generadores/README.md)
