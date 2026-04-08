# 🧠 Documento teórico — Clase 10: Modelos supervisados

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

El modelo y la métrica se eligen por la pregunta, no por popularidad.

## ❓ Por qué importa este módulo

Ayuda a comparar enfoques y a entender qué cambia entre predecir valores y predecir clases.

## 💻 Bloque de código documentado

### Clasificación binaria con árbol

Primero definimos una etiqueta supervisada simple y luego entrenamos un modelo interpretable.

**Qué hace:** crear etiqueta → separar variables → entrenar → revisar

**Para qué sirve:** Sirve para introducir clasificación sin perder transparencia en la lógica del modelo.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv("datasets/estudiantes.csv")
df["alto_desempeno"] = (
    (df["evaluacion_python"] >= 75) & (df["evaluacion_pandas"] >= 75)
).astype(int)

X = df[["asistencia_pct", "evaluacion_python", "edad"]]
y = df["alto_desempeno"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)
print(modelo.predict(X_test[:5]))
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 11 endurece la evaluación con validación cruzada y pipelines.
