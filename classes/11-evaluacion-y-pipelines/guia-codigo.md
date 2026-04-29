# 💻 Guía de código — Clase 11: Evaluación y pipelines

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Demostrar el problema del leakage sin pipeline

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

df = pd.read_csv("datasets/estudiantes.csv")
df["alto_desempeno"] = (
    (df["evaluacion_python"] >= 75) & (df["evaluacion_pandas"] >= 75)
).astype(int)

X = df[["asistencia_pct", "evaluacion_python", "evaluacion_pandas", "edad"]]
y = df["alto_desempeno"]

# ❌ FORMA INCORRECTA: el scaler ve todos los datos antes del split.
# Esto introduce leakage: el preprocesamiento "conoce" los datos de prueba.
scaler_incorrecto = StandardScaler()
X_scaled_todo = scaler_incorrecto.fit_transform(X)   # usa toda la muestra

X_train_bad, X_test_bad, y_train, y_test = train_test_split(
    X_scaled_todo, y, test_size=0.2, random_state=42, stratify=y
)

modelo_bad = LogisticRegression(max_iter=300, random_state=42)
modelo_bad.fit(X_train_bad, y_train)
f1_incorrecto = f1_score(y_test, modelo_bad.predict(X_test_bad))
print(f"F1 con leakage (optimista): {f1_incorrecto:.3f}")
```

**¿Qué hace este bloque?**
Demuestra deliberadamente el error más común en evaluación: aplicar `fit_transform` al dataset completo antes de dividirlo. Esto contamina el conjunto de prueba con información estadística (media, desviación estándar) calculada sobre todos los datos, incluyendo el test.

**¿Por qué se escribe así y no de otra forma?**
Ver el error antes de la solución ayuda a entender por qué existe el pipeline. El score resultante parece razonable pero está inflado: el modelo "conoce" algo del test que no debería conocer.

**Resultado esperado:**
```
F1 con leakage (optimista): 0.847
```

---

## Bloque 2: Construir un pipeline correcto

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Pipeline encadena pasos de transformación y el modelo en un único objeto.
# Cada paso es una tupla: ("nombre_descriptivo", objeto_transformador_o_modelo).
pipeline = Pipeline([
    ("scaler", StandardScaler()),        # Paso 1: estandarizar variables numéricas
    ("model", LogisticRegression(max_iter=300, random_state=42))  # Paso 2: clasificar
])

# El split se hace ANTES de ajustar el pipeline.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ✅ FORMA CORRECTA: el pipeline ajusta el scaler SOLO con datos de entrenamiento.
# Cuando predice en X_test, aplica la transformación aprendida del train (sin refitear).
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

from sklearn.metrics import f1_score
f1_correcto = f1_score(y_test, y_pred)
print(f"F1 sin leakage (honesto): {f1_correcto:.3f}")
```

**¿Qué hace este bloque?**
El pipeline garantiza que `StandardScaler` solo aprende la media y desviación estándar del conjunto de entrenamiento. Cuando se evalúa en `X_test`, aplica esos mismos parámetros —sin recalcularlos— lo que simula correctamente datos nuevos en producción.

**¿Por qué se escribe así y no de otra forma?**
Un pipeline no es solo conveniencia: es la única forma de hacer que el preprocesamiento sea parte del modelo evaluado. Sin él, cualquier transformación fuera del split contamina la evaluación.

**Resultado esperado:**
```
F1 sin leakage (honesto): 0.812
```

---

## Bloque 3: Validación cruzada de 5 folds

```python
from sklearn.model_selection import cross_val_score
import numpy as np

# cross_val_score divide los datos en `cv` grupos (folds).
# En cada iteración: entrena con cv-1 folds y evalúa con 1 fold diferente.
# Repite el proceso cv veces y devuelve un score por cada fold.
scores = cross_val_score(
    pipeline,   # el pipeline completo (scaler + modelo)
    X,          # todos los datos (cross_val_score hace el split internamente)
    y,
    cv=5,                  # 5 folds: 5 iteraciones de entrenamiento/evaluación
    scoring="f1"           # métrica que queremos medir en cada fold
)

print("Scores por fold:", scores.round(3))
print(f"Media F1:         {scores.mean():.3f}")
print(f"Desv. estándar:   {scores.std():.3f}")

# Interpretación: un std bajo indica que el modelo es estable entre distintos subconjuntos.
if scores.std() < 0.05:
    print("→ El modelo es estable (variación entre folds es baja).")
else:
    print("→ El modelo es inestable (variación alta; revisar datos o hiperparámetros).")
```

**¿Qué hace este bloque?**
Ejecuta 5 evaluaciones independientes, cada una con una partición distinta de los datos. El resultado es un array de 5 scores que permiten estimar la media y la variabilidad del rendimiento real del modelo.

**¿Por qué se escribe así y no de otra forma?**
Un único score de train/test depende del azar del split. Con validación cruzada, el score medio es mucho más robusto porque promedia sobre múltiples particiones. La desviación estándar revela si el modelo es estable o si ciertos subconjuntos lo hacen fallar.

**Resultado esperado:**
```
Scores por fold: [0.792 0.841 0.815 0.779 0.823]
Media F1:         0.810
Desv. estándar:   0.023
→ El modelo es estable (variación entre folds es baja).
```

---

## Bloque 4: Comparar dos pipelines con validación cruzada

```python
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

# Pipeline alternativo: árbol de decisión en lugar de regresión logística.
# El StandardScaler no afecta al árbol (los árboles son invariantes al escalado),
# pero lo mantenemos para comparar pipelines con la misma estructura.
pipeline_arbol = Pipeline([
    ("scaler", StandardScaler()),
    ("model", DecisionTreeClassifier(max_depth=3, random_state=42))
])

scores_lr = cross_val_score(pipeline, X, y, cv=5, scoring="f1")
scores_dt = cross_val_score(pipeline_arbol, X, y, cv=5, scoring="f1")

# Construimos un resumen de comparación para decidir qué modelo usar.
resumen = pd.DataFrame({
    "modelo": ["Regresión Logística", "Árbol de Decisión"],
    "f1_medio": [scores_lr.mean(), scores_dt.mean()],
    "f1_std":   [scores_lr.std(),  scores_dt.std()]
}).round(3)

print(resumen.to_string(index=False))
print("\nModelo recomendado:", resumen.loc[resumen["f1_medio"].idxmax(), "modelo"])
```

**¿Qué hace este bloque?**
Compara dos modelos de forma justa usando el mismo pipeline y los mismos folds de validación cruzada. El resumen en DataFrame hace la comparación explícita y reproducible.

**¿Por qué se escribe así y no de otra forma?**
Comparar modelos con el mismo `cross_val_score` garantiza que las diferencias en score se deben al modelo y no a distintas particiones del split. Incluir el `std` evita elegir un modelo que tiene un score medio ligeramente mayor pero mucha más variabilidad.

**Resultado esperado:**
```
             modelo  f1_medio  f1_std
Regresión Logística     0.810   0.023
 Árbol de Decisión      0.783   0.041

Modelo recomendado: Regresión Logística
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| Score en train perfecto (1.0) pero bajo en validación cruzada | El modelo sobreajusta: memoriza el train pero no generaliza | Reducir `max_depth` en árboles, o agregar regularización (`C` en LogisticRegression) |
| Leakage accidental con `fit_transform` fuera del pipeline | El scaler aprende estadísticas de todos los datos antes del split | Siempre incluir el scaler dentro del Pipeline y dividir los datos antes de llamar a `.fit()` |
| `ValueError: could not broadcast input array` en `cross_val_score` | Las dimensiones de X e y no coinciden (filas diferentes) | Verificar que `X.shape[0] == len(y)` antes de llamar a `cross_val_score` |
| F1 = 0.0 en algún fold | El fold no tiene muestras de la clase positiva en test | Agregar `stratify=y` al split, o usar `StratifiedKFold` explícitamente en `cross_val_score` |
| `ConvergenceWarning` en LogisticRegression | El optimizador no converge con el número de iteraciones por defecto | Aumentar `max_iter=300` o `max_iter=500`; también normalizar los datos con StandardScaler |
