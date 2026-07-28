# Clase 038 — Matplotlib: legends, colorbars, ticks, anotaciones

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** §§ 4.7–4.9 *Customizing Legends, Colorbars, Ticks*.
> ⏱️ Duración estimada: **60 min**.
> 🎚️ **Nivel:** Básico

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

## 📖 Definiciones y características

**Leyenda (`ax.legend`)**
: Mapeo labels↔elementos del plot. Auto-detecta si pones `label=` en `plot/scatter`. Posición con `loc=` o `bbox_to_anchor=` para colocarla fuera del axes.

**Colorbar**
: Escala de color para plots con codificación continua (`scatter(c=valor)`, `imshow`). Indica cómo se mapean valores a colores. **Siempre etiqueta** con `cbar.set_label(...)`.

**Tick / TickFormatter**
: Marcas en los ejes y sus etiquetas. **Formatter** define el formato: `PercentFormatter`, `FuncFormatter(lambda x,p: f'${x:,.0f}')`, `LogFormatter`.

**`ax.annotate`**
: Texto con flecha apuntando a un punto. Parámetros: `xy` (punto a apuntar), `xytext` (posición del texto), `arrowprops` (estilo flecha).

**Líneas/bandas de referencia**
: `axhline(y)` horizontal, `axvline(x)` vertical, `axhspan(y1, y2)` banda horizontal. Útiles para umbrales, medias, eventos.

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

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Leyenda tapa parte del plot | Default es 'best' que a veces no encuentra hueco. **Fix**: `ax.legend(loc='upper left')` explícito, o sácala fuera con `bbox_to_anchor=(1.02, 1), loc='upper left'`. |
| Colorbar es enorme/desproporcionada | Default fill toda la altura. **Fix**: `fig.colorbar(im, shrink=0.7)` o usa `make_axes_locatable` para control fino. |
| Ticks rotados se cortan | Texto rotado no entra en el bounding box. **Fix**: `ax.tick_params(axis='x', rotation=45)` + `constrained_layout=True` o `bbox_inches='tight'` al guardar. |
| `annotate` con flecha que apunta mal | `xy` y `xytext` están en coordenadas de datos por default. Si querés relativas al axes, pasa `xycoords='axes fraction'`. |
| `axhline(media)` invisible | Pintada gris claro encima de fondo similar. **Fix**: `color='red', linewidth=1.5, linestyle='--'` para destacarla. |

## ❓ Preguntas frecuentes

**❓ ¿Leyenda dentro o fuera?**

**Dentro** si hay espacio (1-3 series, plot no saturado). **Fuera** (`bbox_to_anchor`) si son 5+ series o el plot está denso.

**❓ ¿Colorbar discreta o continua?**

**Continua** si los datos son continuos (densidad, precio). **Discreta** (con N boundaries) si son categóricas/cuantiles — `BoundaryNorm` + `ListedColormap`.

**❓ ¿`set_xticks` o `set_xticklabels`?**

**`set_xticks`** define dónde van las marcas. **`set_xticklabels`** define qué texto se muestra. Usa ambos juntos para control fino; nunca uses solo el segundo (deprecation warning).

**❓ ¿Cómo añado emojis/Unicode a texts?**

Default font (DejaVu Sans) trae básicos. Para emoji color, fuente especial (`'Segoe UI Emoji'` en Windows). Mejor: evita emojis dentro del plot, úsalos en título/labels markdown.

**❓ ¿Log scale para presentaciones?**

Si los datos cubren >2 órdenes de magnitud (1, 100, 10000), sí. Pero **siempre indícalo** en el título o axis label ("escala log") — no es obvio.

## 🔗 Referencias

- VanderPlas, **cap. 4** §§ 4.7-4.9.
- [matplotlib text and annotations](https://matplotlib.org/stable/users/explain/text/annotations.html)

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-038-matplotlib-legends-colorbars-ticks-anotaciones-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-038-matplotlib-legends-colorbars-ticks-anotaciones-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 039 — Matplotlib: stylesheets](../039-matplotlib-stylesheets/README.md)
