# ❓ Preguntas de evaluación — Clase 11: Evaluación y pipelines

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Qué es el "data leakage" y por qué es un problema grave en machine learning? Da un ejemplo concreto con preprocesamiento.
2. ¿Qué diferencia hay entre evaluar un modelo con un único train/test split versus usar validación cruzada de 5 folds?
3. ¿Por qué el `StandardScaler` debe ajustarse (fit) solo con los datos de entrenamiento y no con el dataset completo?
4. ¿Qué ventaja ofrece envolver el preprocesamiento y el modelo en un `Pipeline` de scikit-learn?
5. Si la validación cruzada da scores de `[0.78, 0.91, 0.80, 0.85, 0.79]`, ¿cómo interpretas la media y la desviación estándar? ¿Es un modelo estable?

## 💻 Preguntas de código

1. ¿Por qué el siguiente código introduce leakage? Reescríbelo usando un `Pipeline` para corregirlo.

```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)          # ajusta sobre todos los datos
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2)
```

2. ¿Qué devuelve `cross_val_score` y qué significa cada elemento del array resultante?

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(pipeline, X, y, cv=5, scoring="f1")
print(scores)
print(scores.mean(), scores.std())
```

3. ¿Qué hace `Pipeline([("scaler", StandardScaler()), ("model", LogisticRegression())])` paso a paso cuando llamas a `.fit(X_train, y_train)`?

4. El siguiente código da un score perfecto de 1.0. ¿Por qué es sospechoso y qué deberías revisar primero?

```python
pipeline.fit(X_train, y_train)
print(pipeline.score(X_train, y_train))   # imprime 1.0
```

## 🔗 Preguntas integradoras

1. Un equipo de ciencia de datos normalizó los datos completos antes de dividirlos en train/test. El modelo tuvo un F1 de 0.93 en pruebas pero solo 0.74 en producción. ¿Qué pudo haber salido mal? ¿Cómo lo solucionarías?
2. ¿Por qué usar validación cruzada en vez de un simple train/test split es especialmente importante cuando el dataset tiene pocas filas (por ejemplo, menos de 200 registros)?
3. Tu pipeline incluye `StandardScaler` antes de un `DecisionTreeClassifier`. ¿El escalado afecta el resultado del árbol? ¿Por qué sí o por qué no? ¿Cambiarías algo en el pipeline?
