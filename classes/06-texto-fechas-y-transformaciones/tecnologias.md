# 🛠️ Tecnologías complementarias — Clase 06: Texto, fechas y transformaciones

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| `pandas` | >= 2.0 | Conversión de fechas con `to_datetime`, creación de columnas derivadas y normalización de texto con `.str` |
| `numpy` | >= 1.24 | Operaciones numéricas auxiliares al crear columnas derivadas numéricas |
| `matplotlib` | >= 3.7 | Visualizar las columnas transformadas (ej. ventas por mes, por día de la semana) |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `dateutil` | Biblioteca para parsear fechas en formatos no estándar | Cuando `pd.to_datetime` no reconoce el formato del CSV (ej. `"15 Ene 2024"`) |
| `pytz` / `zoneinfo` | Manejo de zonas horarias | Cuando los datos vienen de sistemas con timestamps UTC y se necesita convertir a zona local |
| `re` (módulo estándar) | Expresiones regulares para limpieza avanzada de texto | Cuando `str.strip().str.lower()` no es suficiente y hay patrones complejos en el texto |
| `fuzzywuzzy` / `rapidfuzz` | Comparación difusa de cadenas de texto | Cuando hay errores tipográficos en categorías (ej. `"Electrónico"` vs `"Electronico"`) |

## 📚 Recursos para profundizar

- Guía de fechas en pandas: https://pandas.pydata.org/docs/user_guide/timeseries.html
- Guía de operaciones con texto en pandas: https://pandas.pydata.org/docs/user_guide/text.html
- Tabla de códigos de formato de fecha (`%Y`, `%m`, `%d`, etc.): https://strftime.org/
- Documentación de `pd.Period` y `dt.to_period`: https://pandas.pydata.org/docs/reference/api/pandas.Period.html

## ⚡ Comandos de instalación

```bash
pip install pandas numpy matplotlib
# Opcionales para manejo avanzado:
pip install python-dateutil pytz rapidfuzz
```
