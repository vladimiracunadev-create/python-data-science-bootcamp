# 🧠 Documento teórico — Clase 02: Pandas y limpieza de datos

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

No se analiza una tabla seria sin inspeccionarla y documentar primero sus problemas.

## ❓ Por qué importa este módulo

Pandas es la puerta de entrada al trabajo real con datos tabulares y a la toma de decisiones sobre calidad.

## 💻 Bloque de código documentado

### Carga e inspección de un CSV

El primer paso no es graficar: es entender qué columnas existen, cómo vienen escritas y si podemos confiar en ellas.

**Qué hace:** cargar → inspeccionar → limpiar → verificar

**Para qué sirve:** Sirve para instalar una rutina mínima de calidad antes de cualquier análisis o visualización.

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")

# Revisamos primeras filas, tipos y valores faltantes antes de seguir.
print(df.head())
print(df.info())
print(df.isna().sum())

# Ejemplo simple de limpieza visible.
df["medio_pago"] = df["medio_pago"].str.strip()
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 03 usa tablas más confiables para explorar patrones visuales.
