# 🧠 Documento teórico — Clase 11: Evaluación y pipelines

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

Pasar de un modelo que parece funcionar a un flujo de evaluación más confiable.

## ❓ Por qué importa este módulo

La evaluación rigurosa ayuda a distinguir entre una buena demostración y un flujo que realmente generaliza mejor.

## 💻 Bloque de código documentado

### Pipeline con validación cruzada

El pipeline encapsula el preprocesamiento junto con el modelo y evita pasos manuales inconsistentes.

**Qué hace:** preprocesar + modelar → validar → comparar

**Para qué sirve:** Sirve para introducir una práctica más robusta sin perder claridad sobre cada componente.

```python
# Qué hace: preprocesar + modelar → validar → comparar.
# Para qué sirve: Sirve para introducir una práctica más robusta sin perder claridad sobre cada componente.
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("datasets/estudiantes.csv")
df["alto_desempeno"] = (
    (df["evaluacion_python"] >= 75) & (df["evaluacion_pandas"] >= 75)
).astype(int)

X = df[["asistencia_pct", "evaluacion_python", "evaluacion_pandas", "edad"]]
y = df["alto_desempeno"]

pipeline = Pipeline(
    [("scaler", StandardScaler()), ("model", LogisticRegression(max_iter=300))]
)
scores = cross_val_score(pipeline, X, y, cv=5, scoring="f1")
print(scores.mean())
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 12 integra todo el recorrido en un proyecto final con cierre.
