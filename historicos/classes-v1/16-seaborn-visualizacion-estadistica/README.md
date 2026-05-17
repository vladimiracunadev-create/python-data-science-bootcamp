# 📘 Clase 16: Seaborn y visualización estadística

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Aprender a usar la librería Seaborn para crear visualizaciones estadísticas claras y expresivas con pocas líneas de código. El estudiante explorará distribuciones, relaciones entre variables y patrones en los datos usando gráficos como histogramas, boxplots, violinplots, heatmaps y pairplots, aplicados sobre datasets reales de ventas y estudiantes.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/ventas_tienda.csv`
- `datasets/estudiantes.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Importar y configurar Seaborn para producir gráficos con estilos profesionales.
- Elegir el tipo de gráfico adecuado según si la variable es numérica, categórica o una relación entre dos variables.
- Interpretar visualmente distribuciones, outliers, correlaciones y tendencias en un dataset real.

## 🧭 Temas clave
- Por qué Seaborn (construido sobre matplotlib, mejores valores por defecto para gráficos estadísticos)
- `import seaborn as sns` + `sns.set_theme()`
- `histplot` y `kdeplot` (distribución de una variable)
- `boxplot` (distribución + outliers por categoría)
- `violinplot` (combina boxplot + densidad)
- `barplot` con intervalos de confianza
- `scatterplot` con parámetros `hue` y `size`
- `heatmap` para la matriz de correlación
- `pairplot` para relaciones entre múltiples variables
- Personalización con `palette`, `figsize` y títulos

## 🧰 Materiales del módulo
- `README.md`
- `slides.md`
- `teoria.md`
- `ejercicios.md`
- `homework.md`
- `notebook.ipynb`
- `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.
- Antes de pasar al siguiente paso, verifica que entiendes la salida.

## 💡 Idea central
Seaborn convierte datos en gráficos estadísticos con pocas líneas de código, revelando patrones que las tablas ocultan.

## 👩‍🏫 Nota para el docente
Empieza mostrando el mismo gráfico con matplotlib puro y luego con Seaborn para que el contraste hable por sí solo. Invita a los estudiantes a elegir qué gráfico harían para responder una pregunta específica antes de mostrárselo — así aprenden a pensar en visualización como una decisión, no solo como estética.
