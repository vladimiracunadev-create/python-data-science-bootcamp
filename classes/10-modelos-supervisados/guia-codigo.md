# 💻 Guía de código — Clase 10: Modelos supervisados

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Crear una etiqueta supervisada desde reglas de negocio

```python
import pandas as pd

df = pd.read_csv("datasets/estudiantes.csv")

# Definimos "alto desempeño" como tener nota >= 75 en ambas evaluaciones.
# La condición produce una Serie booleana (True/False).
# .astype(int) la convierte en 1 (alto desempeño) o 0 (no lo es).
df["alto_desempeno"] = (
    (df["evaluacion_python"] >= 75) & (df["evaluacion_pandas"] >= 75)
).astype(int)

# Verificamos el balance de clases: cuántos estudiantes hay en cada categoría.
print("Distribución de la etiqueta:")
print(df["alto_desempeno"].value_counts())
print(f"\nProporción clase positiva: {df['alto_desempeno'].mean():.1%}")
```

**¿Qué hace este bloque?**
Transforma el problema continuo (dos notas numéricas) en un problema de clasificación binaria. El operador `&` aplica la condición de forma vectorizada a todas las filas a la vez. Revisar el balance de clases es importante antes de elegir métricas.

**¿Por qué se escribe así y no de otra forma?**
Convertir booleanos a enteros con `.astype(int)` es el formato que scikit-learn espera para `y`. Definir el umbral como regla explícita (>= 75) hace que el criterio de clasificación sea transparente y debatible con el equipo o cliente.

**Resultado esperado:**
```
Distribución de la etiqueta:
0    78
1    42
Name: alto_desempeno, dtype: int64

Proporción clase positiva: 35.0%
```

---

## Bloque 2: Entrenar un árbol de decisión interpretable

```python
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Definimos X e y para clasificación.
X = df[["asistencia_pct", "evaluacion_python", "edad"]]
y = df["alto_desempeno"]

# Dividimos respetando la distribución de clases con stratify.
# stratify=y garantiza que el 35 % de clase positiva se mantenga en ambos subconjuntos.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# max_depth limita la profundidad del árbol para evitar sobreajuste.
# Un árbol muy profundo "memoriza" los datos de entrenamiento.
modelo = DecisionTreeClassifier(max_depth=3, random_state=42)
modelo.fit(X_train, y_train)

print("Clases del modelo:", modelo.classes_)
print("Predicciones (primeras 5):", modelo.predict(X_test[:5]))
print("Probabilidades (primeras 5):")
print(modelo.predict_proba(X_test[:5]).round(2))
```

**¿Qué hace este bloque?**
Entrena un árbol de decisión con profundidad máxima 3, que produce reglas interpretables tipo "si asistencia > 80 % Y nota_python >= 75, entonces alto desempeño". `predict_proba` devuelve la probabilidad de cada clase, no solo la clase ganadora.

**¿Por qué se escribe así y no de otra forma?**
`max_depth=3` es un punto de partida razonable para datasets pequeños: suficiente para capturar patrones pero sin memorizar ruido. `stratify=y` evita que el split por azar deje todas las muestras de una clase en el conjunto de prueba.

**Resultado esperado:**
```
Clases del modelo: [0 1]
Predicciones (primeras 5): [0 1 0 1 0]
Probabilidades (primeras 5):
[[0.88 0.12]
 [0.14 0.86]
 [0.91 0.09]
 [0.07 0.93]
 [0.82 0.18]]
```

---

## Bloque 3: Evaluar con métricas de clasificación

```python
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

y_pred = modelo.predict(X_test)

# Accuracy: proporción de predicciones correctas sobre el total.
# Puede ser engañoso si las clases están desbalanceadas.
print(f"Accuracy: {accuracy_score(y_test, y_pred):.3f}")

# classification_report muestra precisión, recall y F1 para cada clase.
# Precisión: de los que predije como positivos, ¿cuántos lo eran realmente?
# Recall: de los que eran positivos, ¿cuántos detecté?
print("\nReporte de clasificación:")
print(classification_report(y_test, y_pred, target_names=["Normal", "Alto desempeño"]))

# Matriz de confusión: vista completa de aciertos y errores por clase.
ConfusionMatrixDisplay.from_predictions(
    y_test, y_pred,
    display_labels=["Normal", "Alto desempeño"],
    cmap="Blues"
)
plt.title("Matriz de confusión — Árbol de decisión")
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?**
Calcula tres perspectivas del error: accuracy global, el reporte detallado por clase (precisión/recall/F1) y la matriz de confusión que muestra los cuatro tipos de resultados posibles (verdaderos positivos, falsos positivos, verdaderos negativos, falsos negativos).

**¿Por qué se escribe así y no de otra forma?**
Con clases desbalanceadas (35 % vs 65 %), el accuracy puede ser engañoso: un modelo que predice "siempre clase 0" tendrá 65 % de accuracy sin haber aprendido nada. El F1-score y la matriz de confusión dan una imagen más honesta del rendimiento.

**Resultado esperado:**
```
Accuracy: 0.833

Reporte de clasificación:
                 precisión  recall  f1-score  support
Normal               0.87    0.88      0.88       16
Alto desempeño       0.75    0.75      0.75        8

accuracy                         0.83       24
macro avg            0.81    0.81      0.81       24
weighted avg         0.83    0.83      0.83       24
```

---

## Bloque 4: Visualizar e interpretar el árbol

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 6))

# plot_tree dibuja el árbol de decisión entrenado.
# filled=True colorea los nodos según la clase dominante.
# feature_names y class_names hacen el árbol legible sin conocer los índices.
plot_tree(
    modelo,
    feature_names=X.columns.tolist(),
    class_names=["Normal", "Alto desempeño"],
    filled=True,
    rounded=True,
    ax=ax
)
plt.title("Árbol de decisión — max_depth=3")
plt.tight_layout()
plt.show()

# Importancia de variables: qué tan útil fue cada columna para las divisiones del árbol.
importancias = pd.Series(modelo.feature_importances_, index=X.columns)
print("Importancia de variables:")
print(importancias.sort_values(ascending=False))
```

**¿Qué hace este bloque?**
Visualiza el árbol completo para que cualquier persona pueda leer las reglas de decisión. Además, muestra la importancia de cada variable: cuánto contribuyó cada columna a mejorar las divisiones del árbol.

**¿Por qué se escribe así y no de otra forma?**
La interpretabilidad es una de las mayores ventajas de los árboles. Mostrar el árbol gráficamente permite que un cliente o docente valide si las reglas tienen sentido desde el dominio, algo imposible con modelos de "caja negra".

**Resultado esperado:**
```
Importancia de variables:
evaluacion_python    0.681
asistencia_pct       0.278
edad                 0.041
dtype: float64
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `ValueError: Unknown label type: 'continuous'` | Se pasó una variable continua como `y` a un clasificador | Convertir `y` a etiquetas enteras con `.astype(int)` o discretizar con un umbral explícito |
| Accuracy perfecto (1.0) en train, bajo en test | El árbol sobreajustó porque `max_depth` es muy grande o no está limitado | Reducir `max_depth` o agregar `min_samples_leaf` para evitar divisiones con pocas muestras |
| Clase positiva con recall muy bajo | El dataset está muy desbalanceado y el modelo ignora la clase minoritaria | Usar `class_weight="balanced"` en `DecisionTreeClassifier` o revisar el umbral de predicción |
| `ValueError: Input X contains NaN` durante `predict` | Hay filas con valores nulos en el conjunto de prueba | Imputar nulos antes del split o usar un `Pipeline` con `SimpleImputer` |
| Árbol ilegible porque tiene muchos nodos | `max_depth` es demasiado grande para visualizar | Reducir `max_depth=3` o `max_depth=4` para visualizaciones; usar mayor profundidad solo para el modelo final |
