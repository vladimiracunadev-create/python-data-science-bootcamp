# 🛠️ Tecnologías complementarias — Clase 03: Visualización exploratoria

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| pandas | 2.x | Agrupar datos con `groupby`, calcular métricas por categoría y preparar el resumen antes de graficar |
| matplotlib | 3.8+ | Crear gráficos de barras controlados, configurar tamaño, título, etiquetas y rotación de ejes |
| numpy | 1.26+ | Soporte interno de matplotlib para operaciones numéricas sobre los valores graficados |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| Seaborn | Capa de alto nivel sobre matplotlib con estilos más atractivos y gráficos estadísticos integrados | Cuando se necesitan gráficos más complejos (boxplot, heatmap, pairplot) con menos código de configuración |
| Plotly Express | Librería de gráficos interactivos exportables a HTML | Cuando el gráfico se compartirá en un dashboard web o se necesita que el usuario pueda hacer zoom y hover |
| pandas `.plot()` | Método integrado en pandas que llama a matplotlib internamente | Para exploración rápida sin configurar axes manualmente; menos control pero más velocidad |
| Tableau Public | Herramienta de visualización visual sin código, gratuita para uso público | Cuando se necesita compartir resultados con personas no técnicas que deben explorar los datos por su cuenta |

## 📚 Recursos para profundizar

- [Documentación oficial de matplotlib](https://matplotlib.org/stable/gallery/index.html): galería de ejemplos con código para decenas de tipos de gráfico
- [Seaborn — Tutorial oficial](https://seaborn.pydata.org/tutorial.html): tutorial paso a paso con ejemplos de gráficos estadísticos sobre DataFrames de pandas
- [Storytelling with Data (libro)](https://www.storytellingwithdata.com/): referencia clásica sobre cómo elegir el gráfico correcto según la pregunta y la audiencia
- [Python Graph Gallery](https://python-graph-gallery.com/): catálogo visual de gráficos en Python con código fuente para matplotlib, seaborn y plotly

## ⚡ Comandos de instalación

```bash
pip install matplotlib seaborn plotly
```
