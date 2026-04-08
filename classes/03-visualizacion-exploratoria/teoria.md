# 🧠 Documento teórico — Clase 03: Visualización exploratoria

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

La visualización exploratoria ayuda a mirar mejor y a formular preguntas más útiles.

## ❓ Por qué importa este módulo

El estudiante necesita aprender a comparar categorías y detectar patrones antes de avanzar a análisis más complejos.

## 💻 Bloque de código documentado

### Ventas netas por categoría

Antes de graficar conviene preparar un resumen que reduzca el ruido de filas individuales.

**Qué hace:** calcular métrica → agrupar → ordenar → graficar

**Para qué sirve:** Sirve para mostrar cómo un gráfico nace de una decisión previa de agregación y no de un clic automático.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

resumen = (
    df.groupby("categoria", as_index=False)["total_neto"]
    .sum()
    .sort_values("total_neto", ascending=False)
)

plt.figure(figsize=(8, 4))
plt.bar(resumen["categoria"], resumen["total_neto"])
plt.title("Ventas netas por categoría")
plt.ylabel("CLP")
plt.xticks(rotation=20)
plt.tight_layout()
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 04 profundiza en cómo resumir datos con medidas descriptivas.
