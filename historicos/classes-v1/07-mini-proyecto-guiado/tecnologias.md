# 🛠️ Tecnologías complementarias — Clase 07: Mini proyecto guiado

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| `pandas` | >= 2.0 | Cargar datos, transformar columnas, agrupar y calcular métricas de resumen |
| `matplotlib` | >= 3.7 | Visualizar los resultados del análisis: rankings por categoría, evolución temporal |
| `numpy` | >= 1.24 | Operaciones numéricas al calcular columnas derivadas como `total_neto` |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `seaborn` | Gráficos estadísticos de alto nivel sobre matplotlib | Para graficar rankings o distribuciones con menos código y mejor estética por defecto |
| `Jupyter Notebook` | Entorno que permite mezclar texto, código y visualizaciones en un solo documento | Para construir el notebook del proyecto con secciones claras: pregunta, datos, análisis, conclusión |
| `pandas Profiling / ydata-profiling` | Genera un reporte HTML completo con estadísticas del dataset | Para exploración inicial rápida antes de definir la pregunta del proyecto |
| `nbformat` | Librería para manipular archivos `.ipynb` por código | Útil si se quiere automatizar la generación de notebooks de proyecto |

## 📚 Recursos para profundizar

- Guía de agrupaciones con pandas (`groupby`): https://pandas.pydata.org/docs/user_guide/groupby.html
- Tutorial de análisis exploratorio de datos paso a paso: https://realpython.com/pandas-python-explore-dataset/
- Plantillas de proyectos de data science en Kaggle: https://www.kaggle.com/code
- «Python for Data Analysis» de Wes McKinney — capítulos de agrupación y agregación
- Documentación de `DataFrame.copy()` y por qué evitar `SettingWithCopyWarning`: https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy

## ⚡ Comandos de instalación

```bash
pip install pandas numpy matplotlib

# Opcionales para profundizar:
pip install seaborn ydata-profiling
```
