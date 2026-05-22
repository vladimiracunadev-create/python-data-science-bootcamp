# Clase 017 — NumPy: broadcasting

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 2** § 2.5 *Computation on Arrays: Broadcasting*.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno **internalice las reglas de broadcasting** — el mecanismo por el que NumPy operó arrays de shapes distintos sin copiar datos. Es lo que hace que `M - M.mean(axis=0)` centrado por columna sea una línea, no un bucle anidado.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Recitar las 3 reglas** de broadcasting (alinea por la derecha, dim 1 estira, falla si no es 1 ni igual).
2. **Predecir** la shape del resultado de una operación entre arrays de shapes distintos.
3. **Centrar y escalar** matrices por fila/columna sin loops.
4. **Usar `np.newaxis`** (o `None`) para promover un vector a matriz fila/columna.
5. **Diagnosticar** un `ValueError: operands could not be broadcast together` leyendo las shapes.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Las 3 reglas | Padding a la derecha, dim 1 estira, error si no coincide. |
| 2 | Vector + matriz | Vector como fila o como columna. |
| 3 | `np.newaxis` / `None` | Insertar eje de tamaño 1. |
| 4 | Caso canónico: centrar/escalar | `X - X.mean(axis=0)` y `(X - μ) / σ`. |
| 5 | Outer product sin loop | `a[:, None] * b[None, :]`. |
| 6 | ValueError común: "operands could not be broadcast together" | Cómo leerlo. |

## 📂 Dataset / recursos

Sintético: matriz de features 100×5 para estandarización. Sin descarga.

## 🧪 Ejercicios

**1.** **Predice antes de ejecutar.** Para shapes `(3,)`, `(3,1)`, `(1,3)`, `(2,3,4)` × `(4,)`, predice la shape del resultado. Verifica.

**2.** **Estandariza features.** Matriz 100×5 aleatoria. Resta media por columna y divide por std por columna en una línea.

**3.** **Outer product.** Vectores `a=[1,2,3]`, `b=[10,20,30,40]`. Calcula la matriz outer (3×4) sin `np.outer`, solo broadcasting.

**4.** **Distance matrix.** Dados 5 puntos 2D, construye matriz 5×5 de distancias euclídeas entre pares — sin `cdist`, solo broadcasting.

**5.** **Diagnostica error.** Intenta `np.ones((3,4)) + np.ones((4,3))`. Lee el ValueError y explica.

## 📝 Homework verificable

Notebook que: (a) predice shapes de 4 operaciones broadcasting y verifica; (b) estandariza una matriz feature por columna en una línea; (c) construye distance matrix de 100 puntos sin loop; (d) provoca y explica un error de broadcasting.

**Criterio de aceptación:** Las predicciones coinciden. Estandarización: media≈0, std≈1 por columna.

## 🔗 Referencias

- VanderPlas, **cap. 2** § 2.5 *Broadcasting*.
- [NumPy broadcasting docs](https://numpy.org/doc/stable/user/basics.broadcasting.html)

## ➡️ Siguiente clase

[Clase 018 — NumPy: boolean masks y fancy indexing](../018-numpy-boolean-masks-y-fancy-indexing/README.md)
