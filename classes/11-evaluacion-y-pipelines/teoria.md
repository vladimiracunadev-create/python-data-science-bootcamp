# Documento Teórico — Clase 11: Evaluación robusta y Pipelines de ML

> **Nivel:** Intermedio-Avanzado · **Duración estimada de lectura:** 30 minutos

---

## 1. El problema de la evaluación con un solo split

Cuando usamos un único train/test split, el score de evaluación depende de **qué datos cayeron en el conjunto de test**. Con datasets pequeños, la varianza puede ser enorme.

**Ejemplo del problema:**

| Split | Accuracy |
|---|---|
| Split A (seed=1) | 0.81 |
| Split B (seed=2) | 0.74 |
| Split C (seed=3) | 0.87 |

**¿Cuál es el "verdadero" performance del modelo?** → Ninguno de forma aislada.

---

## 2. Validación Cruzada (Cross-Validation)

### 2.1 K-Fold Cross-Validation

Divide los datos en K grupos iguales. En cada iteración, un grupo es test y el resto es train. Se promedian los K scores.

```
Datos: [1][2][3][4][5]

Iter 1: Test=[1] Train=[2][3][4][5] → score_1
Iter 2: Test=[2] Train=[1][3][4][5] → score_2
Iter 3: Test=[3] Train=[1][2][4][5] → score_3
Iter 4: Test=[4] Train=[1][2][3][5] → score_4
Iter 5: Test=[5] Train=[1][2][3][4] → score_5

Score final: mean(score_1...score_5) ± std(score_1...score_5)
```

### 2.2 Implementación

```python
from sklearn.model_selection import cross_val_score, KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf, scoring="f1_weighted")

print(f"Scores por fold: {scores.round(3)}")
print(f"Media:           {scores.mean():.3f}")
print(f"Desv. estándar:  {scores.std():.3f}")
print(f"Intervalo 95%:   [{scores.mean()-2*scores.std():.3f}, {scores.mean()+2*scores.std():.3f}]")
```

### 2.3 Tipos de Cross-Validation

| Tipo | Descripción | Cuándo usar |
|---|---|---|
| **K-Fold** | K divisiones aleatorias | Caso general |
| **Stratified K-Fold** | Mantiene proporción de clases en cada fold | Clases desbalanceadas |
| **Leave-One-Out (LOO)** | K=n (cada ejemplo es un fold) | Datasets muy pequeños |
| **Time Series Split** | Respeta orden temporal | Series de tiempo |

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring="f1")
```

---

## 3. Overfitting y Underfitting

### 3.1 Diagnóstico visual

| Escenario | Train Score | Test Score | Brecha | Diagnóstico |
|---|---|---|---|---|
| Modelo ideal | 0.90 | 0.88 | Pequeña | ✅ Generaliza bien |
| Overfitting leve | 0.95 | 0.85 | Media | ⚠️ Revisar complejidad |
| Overfitting grave | 0.99 | 0.65 | Grande | ❌ Memoriza, no aprende |
| Underfitting | 0.65 | 0.63 | Muy pequeña | ❌ Demasiado simple |

### 3.2 Curva de aprendizaje

```python
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

train_sizes, train_scores, val_scores = learning_curve(
    model, X, y,
    cv=5, scoring="f1",
    train_sizes=np.linspace(0.1, 1.0, 10),
    n_jobs=-1
)

plt.figure(figsize=(10, 5))
plt.plot(train_sizes, train_scores.mean(axis=1), "o-", label="Train", color="#22c55e")
plt.fill_between(train_sizes,
    train_scores.mean(axis=1) - train_scores.std(axis=1),
    train_scores.mean(axis=1) + train_scores.std(axis=1),
    alpha=0.15, color="#22c55e")

plt.plot(train_sizes, val_scores.mean(axis=1), "o-", label="Validación", color="#3b82f6")
plt.fill_between(train_sizes,
    val_scores.mean(axis=1) - val_scores.std(axis=1),
    val_scores.mean(axis=1) + val_scores.std(axis=1),
    alpha=0.15, color="#3b82f6")

plt.xlabel("Tamaño del conjunto de entrenamiento")
plt.ylabel("F1-Score")
plt.title("Curva de Aprendizaje")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

**Interpretación:**
- Si ambas curvas convergen en un valor alto → ✅ Bien.
- Si hay gran brecha entre train y val → Overfitting (reducir complejidad o agregar datos).
- Si ambas curvas convergen en un valor bajo → Underfitting (aumentar complejidad o agregar features).

---

## 4. Pipelines de scikit-learn

### 4.1 ¿Por qué usar Pipelines?

**Problema sin Pipeline:**
```python
# El scaler aprende la media/std del TOTAL de datos → data leakage
scaler.fit(X)               # ❌ MAL: incluye datos de test
X_scaled = scaler.transform(X)
X_train, X_test = train_test_split(X_scaled, ...)
```

**Con Pipeline (correcto):**
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])

pipe.fit(X_train, y_train)    # scaler aprende SOLO de train
pipe.predict(X_test)          # aplica la misma transformación automáticamente
```

### 4.2 Pipeline con ColumnTransformer

Cuando hay columnas numéricas y categóricas que necesitan transformaciones distintas:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

numeric_features = ["antiguedad_meses", "n_productos", "reclamos"]
categorical_features = ["segmento", "canal_adquisicion"]

# Transformaciones para numéricos
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Transformaciones para categóricos
categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore", sparse_output=False))
])

# Unir todo en un preprocesador
preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

# Pipeline final
pipe = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier(n_estimators=100, random_state=42))
])

pipe.fit(X_train, y_train)
print(f"Test F1: {f1_score(y_test, pipe.predict(X_test)):.3f}")
```

### 4.3 Ventajas del Pipeline

| Ventaja | Descripción |
|---|---|
| **Sin data leakage** | Transformaciones se aprenden solo en train |
| **Reproducibilidad** | El mismo objeto aplica en train y producción |
| **Código limpio** | Un objeto para todo el proceso |
| **Compatible con CV** | Se puede pasar directamente a `cross_val_score` |
| **Serializable** | Se puede guardar con `pickle` o `joblib` |

---

## 5. GridSearchCV — Búsqueda de Hiperparámetros

### 5.1 ¿Qué son los hiperparámetros?

Los hiperparámetros son configuraciones del modelo que **no se aprenden de los datos** — los define el usuario antes del entrenamiento.

| Modelo | Hiperparámetros típicos |
|---|---|
| Árbol de decisión | `max_depth`, `min_samples_leaf` |
| Regresión Logística | `C` (regularización), `solver` |
| Random Forest | `n_estimators`, `max_depth`, `max_features` |
| SVM | `C`, `kernel`, `gamma` |

### 5.2 Implementación

```python
from sklearn.model_selection import GridSearchCV

# Prefijo "model__" para acceder a hiperparámetros dentro del Pipeline
param_grid = {
    "model__C": [0.01, 0.1, 1, 10, 100],
    "model__max_iter": [200, 500, 1000]
}

gs = GridSearchCV(
    pipe,
    param_grid,
    cv=5,
    scoring="f1",
    n_jobs=-1,              # usar todos los cores
    refit=True,             # reentrenar con los mejores params en todos los datos
    verbose=1
)

gs.fit(X_train, y_train)

print(f"Mejor combinación: {gs.best_params_}")
print(f"Mejor F1 en CV:    {gs.best_score_:.4f}")
print(f"F1 en Test:        {f1_score(y_test, gs.predict(X_test)):.4f}")
```

### 5.3 Visualizar los resultados del GridSearch

```python
import pandas as pd

results = pd.DataFrame(gs.cv_results_)
pivot = results.pivot_table(
    index="param_model__C",
    columns="param_model__max_iter",
    values="mean_test_score"
)

import seaborn as sns
sns.heatmap(pivot, annot=True, fmt=".3f", cmap="YlGn")
plt.title("F1 por combinación de hiperparámetros")
plt.tight_layout()
plt.show()
```

---

## 6. Guardar y cargar modelos

```python
import joblib

# Guardar
joblib.dump(gs.best_estimator_, "modelo_churn_v1.pkl")

# Cargar
modelo_cargado = joblib.load("modelo_churn_v1.pkl")
predicciones = modelo_cargado.predict(nuevos_datos)
```

---

## 7. Resumen de mejores prácticas

```
✅ Siempre usar Pipeline (evitar data leakage)
✅ Evaluar con cross-validation, no un solo split
✅ Buscar hiperparámetros con GridSearchCV dentro del Pipeline
✅ Evaluar con el test set UNA sola vez al final
✅ Guardar el Pipeline completo (no solo el modelo)
✅ Documentar el proceso con comentarios y print statements
```

---

## 8. Flujo completo recomendado

```python
# 1. Dividir datos (una sola vez, al principio)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Construir Pipeline
pipe = Pipeline([...])

# 3. Buscar hiperparámetros con CV en train
gs = GridSearchCV(pipe, param_grid, cv=5, scoring="f1")
gs.fit(X_train, y_train)

# 4. Evaluar en test (UNA SOLA VEZ)
final_score = f1_score(y_test, gs.predict(X_test))
print(f"Score final en test: {final_score:.4f}")

# 5. Guardar el mejor modelo
joblib.dump(gs.best_estimator_, "modelo_final.pkl")
```
