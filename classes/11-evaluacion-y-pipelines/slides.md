# 🖥 Slides â€” Clase 11: EvaluaciÃ³n robusta y Pipelines de ML

> 🖥 Guion visual breve para conducir la sesion sin sobrecargar la clase.


## 🧱 Bloque 1 (20 min) â€” El problema del overfitting

**DiagnÃ³stico:**

| Escenario | Train score | Test score | DiagnÃ³stico |
|---|---|---|---|
| Perfecto | Alto | Alto | âœ… Bien |
| Overfitting | Alto | Bajo | âŒ Memoriza |
| Underfitting | Bajo | Bajo | âŒ Demasiado simple |
| Varianza | Variable | Variable | âš ï¸ Inestable |

**Causa mÃ¡s comÃºn de overfitting:** modelo demasiado complejo para el volumen de datos.

---

## 🧱 Bloque 2 (25 min) â€” ValidaciÃ³n cruzada

En lugar de un solo train/test split:

```
Fold 1: [Test] [Train] [Train] [Train] [Train]
Fold 2: [Train] [Test] [Train] [Train] [Train]
Fold 3: [Train] [Train] [Test] [Train] [Train]
Fold 4: [Train] [Train] [Train] [Test] [Train]
Fold 5: [Train] [Train] [Train] [Train] [Test]
```

**Resultado:** 5 scores â†’ media y desviaciÃ³n estÃ¡ndar. Mucho mÃ¡s confiable.

```python
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5, scoring="f1")
print(f"F1 promedio: {scores.mean():.3f} Â± {scores.std():.3f}")
```

---

## 🧱 Bloque 3 (30 min) â€” Pipelines

**Sin Pipeline (peligroso):**
```python
scaler.fit(X_train)       # OK
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)  # Â¿se te olvidarÃ¡ en prod?
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
pipe.predict(X_test)  # escala automÃ¡ticamente
```

---

## ✅ Cierre (15 min) â€” GridSearchCV

```python
from sklearn.model_selection import GridSearchCV
params = {"model__C": [0.01, 0.1, 1, 10]}
gs = GridSearchCV(pipe, params, cv=5, scoring="f1")
gs.fit(X_train, y_train)
print(gs.best_params_)
```
