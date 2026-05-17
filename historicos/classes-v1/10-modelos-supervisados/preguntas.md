# ❓ Preguntas de evaluación — Clase 10: Modelos supervisados

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Cuál es la diferencia fundamental entre un problema de regresión y uno de clasificación? Da un ejemplo de cada uno usando datos de estudiantes.
2. ¿Por qué un árbol de decisión se considera un modelo "interpretable"? ¿Qué ventaja tiene eso frente a un modelo más complejo?
3. ¿Qué significa el parámetro `max_depth` en un `DecisionTreeClassifier`? ¿Qué riesgo existe si lo dejas sin límite?
4. ¿Qué diferencia hay entre `accuracy`, `precisión` y `recall`? ¿Cuándo priorizarías recall sobre precisión?
5. ¿Por qué la métrica que eliges debe depender del problema y no del modelo que uses? Da un ejemplo donde un accuracy alto puede ser engañoso.

## 💻 Preguntas de código

1. ¿Qué hace esta línea y qué tipo de variable genera? ¿Por qué se usa `.astype(int)` al final?

```python
df["alto_desempeno"] = (
    (df["evaluacion_python"] >= 75) & (df["evaluacion_pandas"] >= 75)
).astype(int)
```

2. Lee el siguiente fragmento. ¿Qué imprimirán las últimas dos líneas y qué representa cada valor?

```python
from sklearn.metrics import accuracy_score, classification_report
y_pred = modelo.predict(X_test)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))
```

3. ¿Qué problema tiene este código y cómo se corrige para que la evaluación sea válida?

```python
modelo = DecisionTreeClassifier(max_depth=3)
modelo.fit(X, y)                         # usa todos los datos
score = accuracy_score(y, modelo.predict(X))  # evalúa en los mismos datos
print("Accuracy:", score)
```

4. ¿Qué diferencia práctica hay entre estos dos clasificadores al aumentar el volumen de datos?

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
modelo_a = DecisionTreeClassifier(max_depth=3)
modelo_b = KNeighborsClassifier(n_neighbors=5)
```

## 🔗 Preguntas integradoras

1. Un hospital quiere predecir si un paciente reingresará en los próximos 30 días. ¿Qué tipo de problema es (regresión o clasificación)? ¿Qué métrica usarías y por qué el accuracy puede ser una mala elección si solo el 5 % de los pacientes reingresa?
2. Tienes que elegir entre un árbol de decisión con accuracy 0.82 y una regresión logística con accuracy 0.80. ¿Siempre elegirías el árbol? ¿Qué otros factores considerarías antes de decidir?
3. ¿Por qué crear la etiqueta supervisada (como `alto_desempeno`) antes de explorar los datos puede introducir un sesgo en el análisis? ¿Qué orden recomendarías?
