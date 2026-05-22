# Clase 018 — NumPy: boolean masks y fancy indexing

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 2**, §§ 2.6–2.7 *Comparisons, Masks, and Boolean Logic* + *Fancy Indexing*.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno seleccione, filtre y modifique sub-arrays de tres formas: slicing (visto), máscaras booleanas (`arr[arr > 0]`) y fancy indexing (`arr[[0, 3, 5]]`). Saber cuál devuelve **vista** vs **copia** y cuándo cada uno es la herramienta correcta.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Filtrar** elementos con máscaras booleanas: `arr[arr > 0]`, `arr[(a > 0) & (a < 10)]`.
2. **Combinar máscaras** con `&`, `|`, `~` — NO con `and`/`or` (no vectorizan).
3. **Seleccionar por índices** con fancy indexing: `arr[[0, 3, 5]]` o `arr[idx_array]`.
4. **Modificar in-place** con máscara: `arr[arr < 0] = 0` (clipping).
5. **Diferenciar vista vs copia**: slicing es vista; fancy indexing y máscara son copia.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Comparaciones elementwise → arrays bool | `arr > 0` no devuelve un bool, devuelve un array de bools. |
| 2 | `np.count_nonzero`, `np.sum` sobre bool | Cuenta cuántos True. |
| 3 | Combinar máscaras con `&`, `|`, `~` | Operadores bitwise — no `and`/`or`. |
| 4 | Fancy indexing con array de índices | Selección no contigua. |
| 5 | Vista vs copia | Slicing = vista; mask/fancy = copia. |
| 6 | `np.where(cond)` (sin alternativas) | Devuelve índices donde se cumple. |

## 📂 Dataset / recursos

Sintético: array de precipitación diaria (365 valores). Sin descarga.

## 🧪 Ejercicios

**1.** **Cuenta días lluviosos.** Dado array de 365 días con precipitación (mm), cuenta cuántos tuvieron >5mm.

**2.** **Estadísticos por máscara.** Calcula precipitación media solo en días lluviosos (>0mm).

**3.** **AND/OR combinados.** Días entre 1 y 10 mm. Días <1 o >50 mm.

**4.** **Clipping.** Reemplaza valores negativos por 0 in-place (`arr[arr < 0] = 0`).

**5.** **Vista vs copia.** Demuestra con un experimento que `arr[:5]` modifica el original pero `arr[arr > 0]` no.

## 📝 Homework verificable

Notebook con array sintético de 365 días de precipitación generado con seed. Calcula: (a) días lluviosos y su media, (b) días extremos (>50mm), (c) demo de vista vs copia, (d) clipping in-place, (e) índices del top 10 días más lluviosos con `argsort`.

**Criterio de aceptación:** Resultados reproducibles. Demo vista/copia muestra comportamiento opuesto.

## 🔗 Referencias

- VanderPlas, **cap. 2** §§ 2.6, 2.7.
- [NumPy indexing user guide](https://numpy.org/doc/stable/user/basics.indexing.html)

## ➡️ Siguiente clase

[Clase 019 — NumPy: ordenamiento y búsqueda](../019-numpy-ordenamiento-y-busqueda/README.md)
