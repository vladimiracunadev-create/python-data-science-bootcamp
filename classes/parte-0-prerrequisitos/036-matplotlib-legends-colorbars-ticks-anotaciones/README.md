# Clase 036 — Matplotlib: legends, colorbars, ticks, anotaciones

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** §§ 4.7–4.9 *Customizing Legends, Colorbars, Ticks*.
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno controle los detalles que distinguen un plot ad-hoc de uno publicable: leyenda fuera del gráfico, colorbar discreto, ticks personalizados, y anotaciones (flechas, texto) para guiar la atención del lector.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Posicionar leyenda** fuera del axes con `bbox_to_anchor`.
2. **Configurar colorbar** con label, ticks discretos, y categoría.
3. **Personalizar ticks**: rotación, formato (`FuncFormatter`, `PercentFormatter`), scale log.
4. **Anotar puntos** con `ax.annotate(..., xy=..., xytext=..., arrowprops=...)`.
5. **Añadir líneas de referencia** con `axhline`/`axvline` (umbrales, medias).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Legend con bbox_to_anchor | Sacarla del axes. |
| 2 | Colorbar con label y ticks discretos | Cuando hay codificación por color. |
| 3 | Tick formatters: percent, scientific, custom | Legibilidad. |
| 4 | `ax.annotate` con flecha | Resaltar un punto específico. |
| 5 | `axhline` / `axvline` / `axhspan` | Líneas y bandas de referencia. |
| 6 | Log scale: `ax.set_yscale('log')` | Cuando hay rango grande. |

## 📂 Dataset / recursos

Sintético: serie con outliers, scatter con categorías.

## 🧪 Ejercicios

**1.** **Leyenda fuera.** Plot con 5 líneas, leyenda a la derecha fuera del axes.

**2.** **Colorbar.** Scatter con `c=` continuo (ej: density), colorbar con label.

**3.** **PercentFormatter.** Bar chart con eje Y formateado como porcentaje.

**4.** **Anotar outlier.** Scatter con un punto extremo; flecha + texto identificándolo.

**5.** **Log scale.** Plot de valores con rango grande (1, 10, 100, 1000); compara linear vs log.

## 📝 Homework verificable

Notebook con: (a) plot multi-línea con leyenda externa; (b) scatter con colorbar etiquetado; (c) bar % usando PercentFormatter; (d) plot con anotación de máximo via flecha; (e) comparativa lineal vs log en datos exponenciales.

**Criterio de aceptación:** Cada elemento visual tiene propósito. Anotaciones legibles, no superpuestas.

## 🔗 Referencias

- VanderPlas, **cap. 4** §§ 4.7-4.9.
- [matplotlib text and annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

## ➡️ Siguiente clase

[Clase 037 — Matplotlib: stylesheets](../037-matplotlib-stylesheets/README.md)
