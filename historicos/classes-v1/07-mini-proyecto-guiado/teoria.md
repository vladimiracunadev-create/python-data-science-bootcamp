# 🧠 Documento teórico — Clase 07: Mini proyecto guiado

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

El proyecto ordena técnicas sueltas dentro de un proceso con sentido.

## ❓ Por qué importa este módulo

Este módulo ayuda a unir análisis, limpieza y visualización en un flujo coherente y comunicable.

## 💻 Bloque de código documentado

### Definición de pregunta y base de trabajo

Antes de calcular, conviene dejar escrita la pregunta y recortar solo las columnas necesarias.

**Qué hace:** pregunta → recorte → base de trabajo → análisis

**Para qué sirve:** Sirve para evitar notebooks dispersos y para mostrar que el proyecto comienza delimitando el problema.

```python
# Qué hace: pregunta → recorte → base de trabajo → análisis.
# Para qué sirve: Sirve para evitar notebooks dispersos y para mostrar que el proyecto comienza delimitando el problema.
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

pregunta = "¿Qué categoría concentra mayor ingreso neto?"
columnas = ["fecha", "sucursal", "categoría", "producto", "medio_pago", "total_neto"]
proyecto = df[columnas].copy()

print(pregunta)
print(proyecto.head())
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 08 convierte ese trabajo en una presentación breve de hallazgos.
