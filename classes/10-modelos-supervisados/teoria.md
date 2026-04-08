# Documento teorico - Clase 10: Modelos supervisados

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Elegir modelo y metrica por la pregunta, no por popularidad.

## Por que importa este modulo

Comparar modelos supervisados basicos y elegir metricas segun el tipo de problema.

## Bloque de codigo documentado

### Clasificacion basica con arbol

Convertimos un problema en una etiqueta binaria y entrenamos un modelo simple e interpretable.

**Que hace:** crear etiqueta -> entrenar -> predecir

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("datasets/ventas_tienda.csv")
df["venta_alta"] = (df["total_neto"] >= df["total_neto"].median()).astype(int)

X = df[["precio_unitario", "unidades_vendidas", "descuento_pct"]]
y = df["venta_alta"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

arbol = DecisionTreeClassifier(max_depth=4, random_state=42)
arbol.fit(X_train, y_train)
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 11 endurece la evaluacion con validacion cruzada y pipelines.
