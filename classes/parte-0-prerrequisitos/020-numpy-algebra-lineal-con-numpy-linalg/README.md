# Clase 020 — NumPy: álgebra lineal con numpy.linalg

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 2** § 2.9 *Structured Arrays* (referencia) · *Numerical Linear Algebra* (Trefethen & Bau).
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno opere con vectores y matrices al nivel necesario para entender ML: producto punto, multiplicación matricial, inversa, sistema de ecuaciones (`solve`), descomposiciones (SVD, eigen). Saber **cuándo no usar la inversa** (lentitud + inestabilidad numérica).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Multiplicar** vectores y matrices con `@` (operador moderno) y `np.dot`.
2. **Resolver** sistemas `Ax = b` con `np.linalg.solve` (NO con `inv(A) @ b`).
3. **Calcular** norma, determinante, rango, traza.
4. **Computar** SVD con `np.linalg.svd` y entender qué retorna.
5. **Calcular eigenvalores/eigenvectores** con `np.linalg.eig` / `eigh` (simétrica).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `@` operador (PEP 465): multiplicación matricial | Reemplaza `np.matmul`. |
| 2 | Producto punto vs producto matricial | Vector·vector vs matriz·matriz. |
| 3 | Resolver sistemas: `solve` vs `inv` | Por qué NUNCA usar `inv`. |
| 4 | Norma, det, rank, trace | Diagnóstico estructural de matrices. |
| 5 | SVD — la factorización universal | Base de PCA, regresión lineal, recomendadores. |
| 6 | Eigen | Base de PCA conceptual. |

## 📂 Dataset / recursos

Sintético: matrices y vectores para los ejercicios. Sin descarga.

## 🧪 Ejercicios

**1.** **Producto punto.** Dados dos vectores 100-dim aleatorios, calcula `np.dot(a, b)` y verifica que coincide con `sum(a*b)`.

**2.** **Multiplicación matricial.** `(50, 30) @ (30, 20)` → `(50, 20)`. Verifica shapes y un elemento manualmente.

**3.** **Resuelve sistema.** Genera `A = (5,5)` aleatoria, `b = (5,)`, resuelve `Ax = b` con `solve`. Verifica `A @ x ≈ b`.

**4.** **Inv vs solve benchmark.** Para `A (1000,1000)` y `b (1000,)`, mide tiempo de `inv(A) @ b` vs `solve(A, b)`. Reporta speedup.

**5.** **SVD de matriz baja rank.** Crea `M = u @ v.T` (rank 1). Calcula SVD y observa que solo el primer valor singular es no-cero.

## 📝 Homework verificable

Notebook que: (a) compara `inv(A) @ b` vs `solve(A, b)` en tiempo Y precisión (`np.allclose`); (b) implementa regresión lineal cerrada `β = (XᵀX)⁻¹ Xᵀy` y luego con `solve`; (c) calcula SVD de una matriz y verifica `M = U @ diag(s) @ Vt`; (d) eigen de matriz de covarianza.

**Criterio de aceptación:** `solve` más rápido y más preciso que `inv`. SVD reconstruye la matriz dentro de tolerancia.

## 🔗 Referencias

- VanderPlas cap. 2 (overview NumPy).
- [`numpy.linalg` reference](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [PEP 465 — `@` operator](https://peps.python.org/pep-0465/)
- Trefethen & Bau, *Numerical Linear Algebra* (1997) — fondo matemático.

## ➡️ Siguiente clase

[Clase 021 — NumPy: aleatoriedad y semillas](../021-numpy-aleatoriedad-y-semillas/README.md)
