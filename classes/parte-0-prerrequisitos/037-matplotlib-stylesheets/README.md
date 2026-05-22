# Clase 037 — Matplotlib: stylesheets

> Parte: **0 — Prerrequisitos** · Fuente: VanderPlas, **cap. 4** § 4.11 *Customizing Matplotlib: Configurations and Stylesheets*.
> ⏱️ Duración estimada: **30 min**.

---

## 🎯 Objetivo

Que el alumno aproveche **stylesheets** built-in y propios para mantener consistencia visual entre plots y proyectos — y deje de configurar manualmente rcParams en cada notebook.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Listar stylesheets disponibles** con `plt.style.available`.
2. **Aplicar** un style globalmente (`plt.style.use(...)`) o solo a un bloque (`with plt.style.context(...)`).
3. **Crear style propio** en un archivo `.mplstyle` y usarlo.
4. **Combinar styles** (uno + ajustes manuales).
5. **Elegir style** según contexto (informe, presentación, B&N para impresión).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `plt.style.available` | Catálogo built-in. |
| 2 | `plt.style.use(...)` global | Afecta todos los plots subsiguientes. |
| 3 | `with plt.style.context(...)` | Temporal, ideal para un bloque. |
| 4 | Archivo `.mplstyle` propio | Reusar entre proyectos. |
| 5 | Stylesheets comunes | default, seaborn-v0_8-whitegrid, ggplot, fivethirtyeight, grayscale. |
| 6 | rcParams override puntual | Style + ajuste fino. |

## 📂 Dataset / recursos

Sintético: mismo plot en varios styles. Sin descarga.

## 🧪 Ejercicios

**1.** **Catalogo.** Imprime `plt.style.available`. Identifica 5 que suenen útiles.

**2.** **Galería visual.** Mismo scatter plot bajo 4 styles distintos (default, ggplot, seaborn-whitegrid, grayscale).

**3.** **Bloque temporal.** Con `with plt.style.context('seaborn-v0_8-darkgrid'):` aplica style solo a 1 figura.

**4.** **Style propio.** Crea `mi_style.mplstyle` con tus defaults preferidos. Úsalo.

**5.** **Style + override.** Aplica `ggplot` y luego cambia `figure.figsize` para un plot específico.

## 📝 Homework verificable

Notebook: (a) galería de 4 styles sobre un mismo dataset; (b) crear `informe.mplstyle` con paleta corporativa simulada (3 colores principales); (c) demo de uso temporal con `plt.style.context`; (d) comparativa B&N (`grayscale`) vs color para una figura que podría imprimirse.

**Criterio de aceptación:** Galería con plots reconocibles; style propio aplica colores definidos.

## 🔗 Referencias

- VanderPlas, **cap. 4** § 4.11.
- [matplotlib stylesheets gallery](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

## ➡️ Siguiente clase

[Clase 038 — Matplotlib: 3D plotting](../038-matplotlib-3d-plotting/README.md)
