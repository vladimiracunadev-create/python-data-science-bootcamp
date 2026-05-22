# Clase 033 — Matplotlib: anatomía figura/axes

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** § 4.1 *Visualization with Matplotlib*.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno entienda la **jerarquía de objetos** de matplotlib (Figure → Axes → Artist) y use la **API orientada a objetos** (`fig, ax = plt.subplots()`) en vez del interfaz pyplot estilo MATLAB. Esto es lo que separa gráficos publicables de notebooks de cualquier curso introductorio.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Explicar** la jerarquía Figure → Axes → Artist y por qué la API OO es preferible.
2. **Crear** una figura con `fig, ax = plt.subplots(figsize=(8, 4))` y configurar título, ejes, leyenda.
3. **Guardar** una figura a PNG/SVG/PDF con DPI controlado.
4. **Cerrar figuras** explícitamente para liberar memoria en notebooks que generan muchas.
5. **Configurar defaults** con `plt.rcParams` (font, line width, colors).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Figure (canvas) → Axes (gráfico) → Artist (elementos) | Modelo mental. |
| 2 | pyplot vs OO API | `plt.plot` (state-based) vs `ax.plot` (explícito). |
| 3 | `fig, ax = plt.subplots()` | El patrón canónico. |
| 4 | `fig.savefig` y formatos | PNG raster vs SVG/PDF vector. |
| 5 | Liberar memoria: `plt.close(fig)` | Importante en loops. |
| 6 | `plt.rcParams` y stylesheets | Defaults globales. |

## 📂 Dataset / recursos

Sintético: serie temporal corta + scatter. Sin descarga.

## 🧪 Ejercicios

**1.** **Hello world.** Crea figura 8×4, plot de `y = sin(x)` para `x ∈ [0, 2π]`. Título, xlabel, ylabel.

**2.** **Dos líneas en un axes.** Misma figura: `sin(x)` y `cos(x)` con colores distintos y leyenda.

**3.** **Guarda 3 formatos.** Mismo plot a PNG (100 DPI), PNG (300 DPI), SVG. Compara tamaños.

**4.** **Loop sin leak.** Genera 20 plots en loop. Cierra cada uno con `plt.close(fig)`. Verifica que `len(plt.get_fignums())` queda en 0.

**5.** **rcParams.** Cambia `font.size` y `lines.linewidth` para tu sesión. Verifica el efecto.

## 📝 Homework verificable

Notebook: (a) figura `sin/cos` con todos los elementos (título, labels, leyenda, grid); (b) guardar PNG@300dpi y SVG; (c) generar 50 plots en loop sin memory leak; (d) demo de rcParams modificados.

**Criterio de aceptación:** Plot publicable (labels, leyenda, tamaño razonable). Loop deja 0 figuras abiertas.

## 🔗 Referencias

- VanderPlas, **cap. 4** § 4.1.
- [matplotlib quick start](https://matplotlib.org/stable/users/explain/quick_start.html)
- [Anatomy of a figure (matplotlib gallery)](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

## ➡️ Siguiente clase

[Clase 034 — Matplotlib: line, scatter, bar, histogram, boxplot](../034-matplotlib-line-scatter-bar-histogram-boxplot/README.md)
