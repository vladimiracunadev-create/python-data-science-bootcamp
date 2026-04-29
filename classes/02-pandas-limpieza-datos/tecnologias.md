# 🛠️ Tecnologías complementarias — Clase 02: Pandas y limpieza de datos

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| pandas | 2.x | Cargar CSV, inspeccionar estructura, detectar nulos y aplicar limpiezas sobre columnas |
| numpy | 1.26+ | Representación interna de valores nulos (`np.nan`) y operaciones vectorizadas de soporte |
| Python (stdlib) | 3.10+ | Manejo de rutas con `pathlib`, apertura de archivos y control de flujo básico |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| OpenRefine | Herramienta visual de limpieza de datos sin código | Cuando el dataset tiene muchos valores inconsistentes y se necesita una revisión manual rápida |
| Great Expectations | Librería para definir y validar contratos de calidad sobre datos | Cuando se trabaja en proyectos de equipo donde la calidad del dato debe estar garantizada automáticamente |
| pandas-profiling / ydata-profiling | Genera un reporte HTML automático con estadísticas, nulos y distribuciones del DataFrame | En la exploración inicial de un dataset nuevo para obtener una visión global en segundos |
| csvkit | Conjunto de herramientas de línea de comandos para inspeccionar y transformar CSV | Cuando se necesita explorar un CSV grande sin abrirlo en Python ni en Excel |

## 📚 Recursos para profundizar

- [Documentación oficial de pandas — User Guide](https://pandas.pydata.org/docs/user_guide/index.html): guía completa sobre DataFrame, indexación, operaciones con nulos y transformaciones de texto
- [pandas — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html): referencia específica para detectar, rellenar y eliminar valores nulos con criterio
- [Real Python — Pandas Data Cleaning](https://realpython.com/python-data-cleaning-numpy-pandas/): tutorial práctico con ejemplos de estandarización, tipos de dato y detección de duplicados
- [ydata-profiling en GitHub](https://github.com/ydataai/ydata-profiling): herramienta para generar reportes de calidad de datos en una sola línea de código

## ⚡ Comandos de instalación

```bash
pip install pandas numpy ydata-profiling
```
