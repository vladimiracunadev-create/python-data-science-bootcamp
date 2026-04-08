# Documento teorico - Clase 09: Introduccion a machine learning

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Mostrar machine learning como extension del analisis, no como magia negra.

## Por que importa este modulo

Comprender que es un modelo supervisado y construir una primera regresion simple con scikit-learn.

## Bloque de codigo documentado

### Preparacion de variables y split

Definimos columnas de entrada y la variable objetivo antes de entrenar.

**Que hace:** problema -> X / y -> train/test

```python
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/ventas_tienda.csv")
X = df[["precio_unitario", "unidades_vendidas", "descuento_pct"]]
y = df["total_neto"]

X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=42
)
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 10 compara modelos supervisados y metricas segun el objetivo.
