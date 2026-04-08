# Ejercicios — Clase 11: Evaluación robusta y Pipelines de ML

## Ejercicio 1 — Detectar overfitting (fácil)

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Entrena árboles con distintas profundidades
for depth in [1, 3, 5, 10, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    print(f"Depth={depth:>4} | Train: {train_score:.3f} | Test: {test_score:.3f}")
```

¿A qué profundidad comienza el overfitting? ¿Cuál es la mejor profundidad?

---

## Ejercicio 2 — Validación cruzada (guiado)

```python
from sklearn.model_selection import cross_val_score

model = DecisionTreeClassifier(max_depth=4, random_state=42)
scores = cross_val_score(model, X, y, cv=5, scoring="f1_weighted")
print(f"F1 por fold: {scores}")
print(f"Promedio: {scores.mean():.3f} ± {scores.std():.3f}")
```

Compara este resultado con el F1 del ejercicio anterior. ¿Coinciden?

---

## Ejercicio 3 — Construir un Pipeline (guiado)

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

numeric_features = ["antiguedad_meses", "n_productos"]
categorical_features = ["segmento"]

preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])

pipe = Pipeline([
    ("prep", preprocessor),
    ("model", LogisticRegression(max_iter=500))
])

pipe.fit(X_train, y_train)
print(f"Test F1: {f1_score(y_test, pipe.predict(X_test)):.3f}")
```

---

## Ejercicio 4 — GridSearchCV (medio)

```python
from sklearn.model_selection import GridSearchCV

params = {
    "model__C": [0.01, 0.1, 1, 10, 100],
    "model__max_iter": [200, 500]
}
gs = GridSearchCV(pipe, params, cv=5, scoring="f1", n_jobs=-1)
gs.fit(X_train, y_train)
print(f"Mejor combinación: {gs.best_params_}")
print(f"Mejor F1 CV: {gs.best_score_:.3f}")
```

---

## Desafío opcional

Grafica la curva de aprendizaje usando `learning_curve` de scikit-learn para el Pipeline. ¿Necesitas más datos o un modelo más complejo?
