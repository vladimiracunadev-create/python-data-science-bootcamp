# 🧠 Documento teórico — Clase 06: Texto, fechas y transformaciones

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

Muchas preguntas nuevas aparecen cuando una columna se transforma bien.

## ❓ Por qué importa este módulo

Las transformaciones abren preguntas más útiles y preparan mejor la base de trabajo.

## 💻 Bloque de código documentado

### Fechas y texto listos para analizar

Convertir y normalizar columnas no es maquillaje: cambia lo que se puede preguntar después.

**Qué hace:** convertir → derivar → normalizar → reutilizar

**Para qué sirve:** Sirve para preparar columnas que luego alimentan gráficos, filtros o variables de modelado.

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

# Creamos columnas nuevas para responder preguntas posteriores.
df["mes"] = df["fecha"].dt.to_period("M").astype(str)
df["dia_semana"] = df["fecha"].dt.day_name()
df["producto_normalizado"] = df["producto"].str.strip().str.lower()

print(df[["fecha", "mes", "dia_semana", "producto_normalizado"]].head())
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 07 usa estas habilidades dentro de un mini proyecto guiado.
