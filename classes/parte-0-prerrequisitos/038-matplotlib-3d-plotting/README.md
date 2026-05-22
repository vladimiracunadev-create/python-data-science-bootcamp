# Clase 038 — Matplotlib: 3D plotting

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** § 4.12 *Three-Dimensional Plotting in Matplotlib*.
> ⏱️ Duración estimada: **45 min**.

---

## 🎯 Objetivo

Que el alumno sepa cuándo (raramente) usar 3D y cómo hacerlo bien: scatter 3D, superficies (`plot_surface`), wireframes y contornos. Spoiler: la mayoría de las veces un buen 2D + color comunica mejor.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Crear axes 3D** con `projection='3d'`.
2. **Scatter, line, surface, wireframe, contour** en 3D.
3. **Controlar ángulo de vista** con `ax.view_init(elev, azim)`.
4. **Reconocer cuándo NO usar 3D**: la mayoría de las veces hay una alternativa 2D mejor.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `projection='3d'` | Habilita el 3D toolkit. |
| 2 | Scatter 3D con codificación por color | 3 dims + 4 (color). |
| 3 | `plot_surface` para z = f(x, y) | Funciones bivariadas. |
| 4 | `plot_wireframe` y `contour3D` | Alternativas más simples. |
| 5 | `view_init`: rotar interactivo | En notebooks con `%matplotlib widget`. |
| 6 | Cuándo NO usar 3D | Casi siempre. |

## 📂 Dataset / recursos

Sintético: superficie analítica + nube de puntos. Sin descarga.

## 🧪 Ejercicios

**1.** **Scatter 3D.** 200 puntos con coords (x, y, z) y color por una 4ª variable.

**2.** **Superficie.** `z = sin(sqrt(x² + y²))` en mesh 50×50. `plot_surface` con colormap.

**3.** **Wireframe + contour.** Misma función con `plot_wireframe`. Compara legibilidad con superficie llena.

**4.** **view_init.** Cambia `(elev, azim)` a 4 ángulos y graba una grilla 2×2.

**5.** **Reto: 2D que vence al 3D.** Para tu scatter 3D del ejercicio 1, propón un 2D + color/tamaño que comunique igual o mejor.

## 📝 Homework verificable

Notebook: (a) scatter 3D con 4 dimensiones (xyz + color); (b) superficie z=f(x,y); (c) wireframe del mismo z; (d) grilla 2×2 con 4 view_init distintos; (e) ejercicio de "2D vence al 3D": versión 2D del scatter.

**Criterio de aceptación:** Plots 3D legibles (no espagueti). Versión 2D del scatter comparable.

## 🔗 Referencias

- VanderPlas, **cap. 4** § 4.12.
- [matplotlib mplot3d tutorial](https://matplotlib.org/stable/users/explain/toolkits/mplot3d.html)

## ➡️ Siguiente clase

[Clase 039 — Seaborn: distribuciones, relaciones, categóricas, facetas](../039-seaborn-distribuciones-relaciones-categoricas-facetas/README.md)
