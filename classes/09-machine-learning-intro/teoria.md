# 🧠 Documento teórico — Clase 09: Introducción a machine learning

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

Machine learning se presenta como una extensión del análisis, no como magia negra.

## ❓ Por qué importa este módulo

Ayuda a entender cómo un conjunto de variables puede apoyar una predicción supervisada básica.

## 💻 Bloque de código documentado

### Primera regresión con variables académicas

Antes de entrenar, conviene declarar con claridad qué queremos predecir y qué datos usaremos como entrada.

**Qué hace:** problema → X / y → split → entrenar → predecir

**Para qué sirve:** Sirve para mostrar la estructura mínima de un flujo supervisado sin saturar al estudiante con complejidad.

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/estudiantes.csv")
X = df[["asistencia_pct", "evaluacion_python", "edad"]]
y = df["evaluacion_pandas"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)
print(predicciones[:5])
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 10 compara modelos supervisados y sus métricas más comunes.
