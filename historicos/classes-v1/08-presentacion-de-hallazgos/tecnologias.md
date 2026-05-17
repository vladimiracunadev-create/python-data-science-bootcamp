# 🛠️ Tecnologías complementarias — Clase 08: Presentación de hallazgos

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| `matplotlib` | >= 3.7 | Crear visualizaciones finales con anotaciones, colores destacados y personalización para presentación |
| `pandas` | >= 2.0 | Calcular métricas de resumen, porcentajes y rankings que se convierten en hallazgos |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `seaborn` | Estilos visuales más pulidos con menos configuración | Cuando se quiere una presentación estética sin escribir mucho CSS/estilo |
| `plotly` | Gráficos interactivos exportables a HTML | Para presentaciones donde la audiencia puede explorar los datos por cuenta propia |
| `Canva` / `PowerPoint` | Herramientas de diseño de diapositivas | Para armar la presentación final con los gráficos exportados desde Python |
| `nbconvert` | Convierte notebooks de Jupyter a HTML, PDF o slides | Para compartir el análisis como documento navegable sin instalar Python |
| `matplotlib.patches` | Módulo para agregar formas geométricas (rectángulos, flechas) sobre gráficos | Para resaltar visualmente la categoría o período más relevante en el gráfico de hallazgos |

## 📚 Recursos para profundizar

- «Storytelling with Data» de Cole Nussbaumer Knaflic — el referente del género, con principios aplicables directamente a matplotlib
- Guía de anotaciones en matplotlib: https://matplotlib.org/stable/tutorials/text/annotations.html
- Cómo exportar notebooks a presentaciones con `nbconvert`: https://nbconvert.readthedocs.io/en/latest/usage.html
- Principios de diseño de gráficos para audiencias no técnicas: https://datajournalism.com/read/longreads/the-chartmaker-directory
- Galería de visualizaciones con contexto narrativo: https://www.visualcinnamon.com/

## ⚡ Comandos de instalación

```bash
pip install matplotlib pandas

# Opcionales para presentación enriquecida:
pip install seaborn plotly nbconvert
```
