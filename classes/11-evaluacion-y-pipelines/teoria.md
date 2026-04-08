# Documento teorico - Clase 11: Evaluacion y pipelines

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Pasar de un modelo que parece funcionar a un flujo de evaluacion mas confiable.

## Por que importa este modulo

Evaluar modelos con mayor rigor y evitar leakage o sobreajuste.

## Bloque de codigo documentado

### Pipeline con validacion cruzada

El pipeline encapsula escalado y modelo, y la validacion cruzada entrega una medida menos fragil.

**Que hace:** pipeline -> CV -> score medio

```python
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("datasets/retencion_clientes.csv")
X = df[["clientes_activos", "clientes_perdidos"]]
y = (df["clientes_perdidos"] > df["clientes_perdidos"].median()).astype(int)

pipe = Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression(max_iter=300))])
scores = cross_val_score(pipe, X, y, cv=5, scoring="f1")
print(scores.mean())
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 12 integra todo en un proyecto final con cierre.
