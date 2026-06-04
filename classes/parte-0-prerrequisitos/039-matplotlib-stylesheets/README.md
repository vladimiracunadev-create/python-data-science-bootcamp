# Clase 039 — Matplotlib: stylesheets

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

## 📖 Definiciones y características

**Stylesheet**
: Conjunto de rcParams predefinidos en un archivo `.mplstyle`. Activa con `plt.style.use('nombre')`. Cambia colors, fonts, grids, spines, etc., consistentemente.

**`plt.style.available`**
: Lista de stylesheets built-in: `default`, `ggplot`, `seaborn-v0_8-whitegrid`, `bmh`, `grayscale`, `dark_background`, etc.

**`plt.style.context(name)`**
: Aplica style solo dentro de un `with` block; al salir, vuelve al anterior. Útil cuando quieres style distinto para 1 plot sin afectar el resto.

**`.mplstyle` propio**
: Archivo de texto con `clave: valor` (igual sintaxis que rcParams). Ubícalo donde sea y carga con `plt.style.use('/ruta/al.mplstyle')`.

**rcParams override en context**
: `with plt.rc_context({'figure.figsize': (12, 6)}):` aplica overrides temporales sobre el style activo.

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

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| `plt.style.use('seaborn')` da error | Renombraron a `seaborn-v0_8-whitegrid` (y variantes). **Fix**: `plt.style.use('seaborn-v0_8-whitegrid')` o `'seaborn-v0_8-darkgrid'`. |
| Style activado pero un plot no lo respeta | Aplicado **después** de crear el axes. Style afecta defaults, no plots existentes. **Fix**: aplica `style.use` ANTES de `plt.subplots`. |
| Colors definidos en `.mplstyle` no aparecen | Sintaxis cycler incorrecta. **Fix**: `axes.prop_cycle: cycler('color', ['#FF0000', '#00FF00'])` con quotes simples. |
| `dark_background` rompe scatter color | Background oscuro, color de marker default es oscuro. **Fix**: override `axes.edgecolor: white` o usa cmap claro. |
| Style se mantiene tras cerrar notebook | `style.use` afecta rcParams globales del kernel. **Fix**: usa `with plt.style.context(...)` para uso temporal. |

## ❓ Preguntas frecuentes

**❓ ¿Style propio o usar built-in?**

**Built-in** para empezar. **Propio** cuando tu organización/proyecto tiene paleta corporativa o convenciones específicas.

**❓ ¿Style afecta seaborn?**

Seaborn maneja su propio system con `sns.set_theme()`. Coordinar ambos puede colisionar. Recomendado: elige uno (style de matplotlib O sns.set_theme).

**❓ ¿Cómo veo todos los styles?**

`plt.style.available` lista todos. Para galería visual: [matplotlib style sheets reference](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html).

**❓ ¿`bmh` qué es?**

Style del libro *Bayesian Methods for Hackers* — popular para gráficos estadísticos limpios.

**❓ ¿Style para impresión B&N?**

**`grayscale`** convierte automáticamente. Pero verifica: cmaps con poca variación de luminancia (`'jet'`) quedan ilegibles. Mejor `'viridis'` o linestyles distintos.

## 🔗 Referencias

- VanderPlas, **cap. 4** § 4.11.
- [matplotlib stylesheets gallery](https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html)

## ➡️ Siguiente clase

[Clase 040 — Matplotlib: 3D plotting](../040-matplotlib-3d-plotting/README.md)
