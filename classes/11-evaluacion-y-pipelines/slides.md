# Slides — Clase 11: Evaluación robusta y Pipelines de ML

## Bloque 1 (20 min) — El problema del overfitting

**Diagnóstico:**

| Escenario | Train score | Test score | Diagnóstico |
|---|---|---|---|
| Perfecto | Alto | Alto | ✅ Bien |
| Overfitting | Alto | Bajo | ❌ Memoriza |
| Underfitting | Bajo | Bajo | ❌ Demasiado simple |
| Varianza | Variable | Variable | ⚠️ Inestable |

**Causa más común de overfitting:** modelo demasiado complejo para el volumen de datos.

---

## Bloque 2 (25 min) — Validación cruzada

En lugar de un solo train/test split:

```
Fold 1: [Test] [Train] [Train] [Train] [Train]
Fold 2: [Train] [Test] [Train] [Train] [Train]
Fold 3: [Train] [Train] [Test] [Train] [Train]
Fold 4: [Train] [Train] [Train] [Test] [Train]
Fold 5: [Train] [Train] [Train] [Train] [Test]
```

**Resultado:** 5 scores → media y desviación estándar. Mucho más confiable.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print(f"F1 promedio: {scores.mean():.3f} ± {scores.std():.3f}")
```

---

## Bloque 3 (30 min) — Pipelines

**Sin Pipeline (peligroso):**
```python
scaler.fit(X_train)       # OK
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)  # ¿se te olvidará en prod?
```

**Con Pipeline (seguro):**
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
pipe.fit(X_train, y_train)
pipe.predict(X_test)  # escala automáticamente
```

---

## Cierre (15 min) — GridSearchCV

```python
from sklearn.model_selection import GridSearchCV
params = {"model__C": [0.01, 0.1, 1, 10]}
gs = GridSearchCV(pipe, params, cv=5, scoring="f1")
gs.fit(X_train, y_train)
print(gs.best_params_)
```
