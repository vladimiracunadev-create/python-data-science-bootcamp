# 🔧 Tecnologías complementarias — Clase 16: Seaborn y visualización estadística

> Herramientas, librerías y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `seaborn` | Visualización estadística de alto nivel construida sobre matplotlib | Básico |
| `matplotlib` | Base de Seaborn; control fino de figuras, ejes, colores y estilos | Básico |
| `pandas` (plot) | Método `.plot()` integrado en DataFrames para gráficos rápidos sin importar nada extra | Básico |
| `plotly express` | API similar a Seaborn pero genera gráficos interactivos con zoom y tooltips | Intermedio |
| `altair` | Visualización declarativa basada en la gramática Vega-Lite, muy elegante | Intermedio |
| `missingno` | Visualización especializada en patrones de datos faltantes (nulos) en un DataFrame | Básico |
| `bokeh` | Gráficos interactivos para integrar en aplicaciones web y dashboards | Avanzado |
| `plotnine` | Equivalente a ggplot2 de R en Python, basado en la gramática de gráficos | Intermedio |
| `yellowbrick` | Visualizaciones específicas para evaluar modelos de machine learning (ROC, aprendizaje) | Avanzado |

## 🌐 Recursos recomendados

- **Documentación oficial**: Seaborn — [seaborn.pydata.org](https://seaborn.pydata.org/) — galería completa de gráficos con código de ejemplo listo para copiar y adaptar para cada tipo de visualización
- **Tutorial recomendado**: "Python Graph Gallery" — [python-graph-gallery.com](https://python-graph-gallery.com/) — catálogo visual de cientos de gráficos con código organizado por tipo
- **Concepto clave para buscar**: "cuándo usar cada tipo de gráfico estadístico" / "choosing the right chart type" — entender cuándo un boxplot es mejor que un histograma es tan importante como saber cómo hacerlo

## 🚀 Próximos pasos sugeridos

- Aprender a personalizar gráficos de Seaborn con matplotlib a fondo: fuentes, paletas de colores personalizadas, múltiples ejes y exportación en alta resolución
- Explorar `FacetGrid` de Seaborn para crear cuadrículas de gráficos automáticamente según categorías, una herramienta muy potente para comparar grupos
- Estudiar gráficos interactivos con Plotly Express para presentaciones y aplicaciones web donde el usuario puede explorar los datos
- Investigar Streamlit para convertir análisis de datos en aplicaciones web interactivas con pocas líneas de Python

## 🧰 Herramientas alternativas

| Herramienta | Descripción breve | Cuándo conviene usarla |
|---|---|---|
| ggplot2 (R) | La gramática de gráficos original, extremadamente expresiva y elegante | Publicaciones académicas o proyectos donde ya se trabaja en R |
| Plotly Dash | Framework para crear aplicaciones web completas de análisis de datos | Dashboards interactivos para clientes o stakeholders que usan el navegador |
| Tableau | Herramienta de Business Intelligence visual sin código | Presentaciones ejecutivas y análisis exploratorio para no programadores |
| D3.js | Librería JavaScript para visualizaciones web completamente personalizadas | Visualizaciones web altamente interactivas y únicas que se publican en internet |
