# Documento teorico - Clase 07: Mini proyecto guiado

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Dejar de pensar la clase como tecnicas sueltas y verla como un proceso coherente.

## Por que importa este modulo

Integrar las habilidades vistas hasta ahora en un mini proyecto guiado de principio a fin.

## Bloque de codigo documentado

### Pregunta y recorte de trabajo

Antes de calcular, recortamos columnas y dejamos visible la pregunta del proyecto.

**Que hace:** pregunta -> columnas utiles -> base de trabajo

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")

# Pregunta del proyecto: que categorias concentran mayor venta neta
columnas = ["fecha", "categoria", "region", "total_neto"]
proyecto = df[columnas].copy()
print(proyecto.head())
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 08 convierte ese trabajo en presentacion de hallazgos.
