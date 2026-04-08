# Documento teorico - Clase 03: Visualizacion exploratoria

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

La visualizacion exploratoria ayuda a mirar y preguntar mejor.

## Por que importa este modulo

Usar visualizaciones exploratorias para describir patrones y abrir nuevas preguntas de analisis.

## Bloque de codigo documentado

### Ventas por categoria

Agrupamos antes de graficar porque queremos comparar categorias, no filas sueltas.

**Que hace:** agrupar -> ordenar -> graficar

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
resumen = df.groupby("categoria", as_index=False)["total_neto"].sum()
resumen = resumen.sort_values("total_neto", ascending=False)

resumen.plot.bar(x="categoria", y="total_neto", legend=False)
plt.title("Ventas netas por categoria")
plt.tight_layout()
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 04 profundiza con medidas descriptivas.
