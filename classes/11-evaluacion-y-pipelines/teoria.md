# 🧠 Documento TeÃ³rico â€” Clase 11: EvaluaciÃ³n robusta y Pipelines de ML

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.


> **Nivel:** Intermedio-Avanzado Â· **DuraciÃ³n estimada de lectura:** 30 minutos

---

## 1. El problema de la evaluaciÃ³n con un solo split

Cuando usamos un Ãºnico train/test split, el score de evaluaciÃ³n depende de **quÃ© datos cayeron en el conjunto de test**. Con datasets pequeÃ±os, la varianza puede ser enorme.

**Ejemplo del problema:**

| Split | Accuracy |
|---|---|
| Split A (seed=1) | 0.81 |
| Split B (seed=2) | 0.74 |
| Split C (seed=3) | 0.87 |

**Â¿CuÃ¡l es el "verdadero" performance del modelo?** â†’ Ninguno de forma aislada.

---

## 2. ValidaciÃ³n Cruzada (Cross-Validation)

### 2.1 K-Fold Cross-Validation

Divide los datos en K grupos iguales. En cada iteraciÃ³n, un grupo es test y el resto es train. Se promedian los K scores.

```
Datos: [1][2][3][4][5]

Iter 1: Test=[1] Train=[2][3][4][5] â†’ score_1
Iter 2: Test=[2] Train=[1][3][4][5] â†’ score_2
Iter 3: Test=[3] Train=[1][2][4][5] â†’ score_3
Iter 4: Test=[4] Train=[1][2][3][5] â†’ score_4
Iter 5: Test=[5] Train=[1][2][3][4] â†’ score_5

Score final: mean(score_1...score_5) Â± std(score_1...score_5)
```

### 2.2 ImplementaciÃ³n

```python
from sklearn.model_selection import cross_val_score, KFold

kf = KFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=kf, scoring="f1_weighted")

print(f"Scores por fold: {scores.round(3)}")
print(f"Media:           {scores.mean():.3f}")
print(f"Desv. estÃ¡ndar:  {scores.std():.3f}")
print(f"Intervalo 95%:   [{scores.mean()-2*scores.std():.3f}, {scores.mean()+2*scores.std():.3f}]")
```

### 2.3 Tipos de Cross-Validation

| Tipo | DescripciÃ³n | CuÃ¡ndo usar |
|---|---|---|
| **K-Fold** | K divisiones aleatorias | Caso general |
| **Stratified K-Fold** | Mantiene proporciÃ³n de clases en cada fold | Clases desbalanceadas |
| **Leave-One-Out (LOO)** | K=n (cada ejemplo es un fold) | Datasets muy pequeÃ±os |
| **Time Series Split** | Respeta orden temporal | Series de tiempo |

```python
from sklearn.model_selection import StratifiedKFold

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(model, X, y, cv=skf, scoring="f1")
```

---

## 3. Overfitting y Underfitting

### 3.1 DiagnÃ³stico visual

| Escenario | Train Score | Test Score | Brecha | DiagnÃ³stico |
|---|---|---|---|---|
| Modelo ideal | 0.90 | 0.88 | PequeÃ±a | âœ… Generaliza bien |
| Overfitting leve | 0.95 | 0.85 | Media | âš ï¸ Revisar complejidad |
| Overfitting grave | 0.99 | 0.65 | Grande | âŒ Memoriza, no aprende |
| Underfitting | 0.65 | 0.63 | Muy pequeÃ±a | âŒ Demasiado simple |

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

plt.plot(train_sizes, val_scores.mean(axis=1), "o-", label="ValidaciÃ³n", color="#3b82f6")
plt.fill_between(train_sizes,
    val_scores.mean(axis=1) - val_scores.std(axis=1),
    val_scores.mean(axis=1) + val_scores.std(axis=1),
    alpha=0.15, color="#3b82f6")

plt.xlabel("TamaÃ±o del conjunto de entrenamiento")
plt.ylabel("F1-Score")
plt.title("Curva de Aprendizaje")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

**InterpretaciÃ³n:**
- Si ambas curvas convergen en un valor alto â†’ âœ… Bien.
- Si hay gran brecha entre train y val â†’ Overfitting (reducir complejidad o agregar datos).
- Si ambas curvas convergen en un valor bajo â†’ Underfitting (aumentar complejidad o agregar features).

---

## 4. Pipelines de scikit-learn

### 4.1 Â¿Por quÃ© usar Pipelines?

**Problema sin Pipeline:**
```python
# El scaler aprende la media/std del TOTAL de datos â†’ data leakage
scaler.fit(X)               # âŒ MAL: incluye datos de test
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
pipe.predict(X_test)          # aplica la misma transformaciÃ³n automÃ¡ticamente
```

### 4.2 Pipeline con ColumnTransformer

Cuando hay columnas numÃ©ricas y categÃ³ricas que necesitan transformaciones distintas:

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier

numeric_features = ["antiguedad_meses", "n_productos", "reclamos"]
categorical_features = ["segmento", "canal_adquisicion"]

# Transformaciones para numÃ©ricos
numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Transformaciones para categÃ³ricos
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

| Ventaja | DescripciÃ³n |
|---|---|
| **Sin data leakage** | Transformaciones se aprenden solo en train |
| **Reproducibilidad** | El mismo objeto aplica en train y producciÃ³n |
| **CÃ³digo limpio** | Un objeto para todo el proceso |
| **Compatible con CV** | Se puede pasar directamente a `cross_val_score` |
| **Serializable** | Se puede guardar con `pickle` o `joblib` |

---

## 5. GridSearchCV â€” BÃºsqueda de HiperparÃ¡metros

### 5.1 Â¿QuÃ© son los hiperparÃ¡metros?

Los hiperparÃ¡metros son configuraciones del modelo que **no se aprenden de los datos** â€” los define el usuario antes del entrenamiento.

| Modelo | HiperparÃ¡metros tÃ­picos |
|---|---|
| Ãrbol de decisiÃ³n | `max_depth`, `min_samples_leaf` |
| RegresiÃ³n LogÃ­stica | `C` (regularizaciÃ³n), `solver` |
| Random Forest | `n_estimators`, `max_depth`, `max_features` |
| SVM | `C`, `kernel`, `gamma` |

### 5.2 ImplementaciÃ³n

```python
from sklearn.model_selection import GridSearchCV

# Prefijo "model__" para acceder a hiperparÃ¡metros dentro del Pipeline
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

print(f"Mejor combinaciÃ³n: {gs.best_params_}")
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
plt.title("F1 por combinaciÃ³n de hiperparÃ¡metros")
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

## ✅ 7. Resumen de mejores prÃ¡cticas

```
âœ… Siempre usar Pipeline (evitar data leakage)
âœ… Evaluar con cross-validation, no un solo split
âœ… Buscar hiperparÃ¡metros con GridSearchCV dentro del Pipeline
âœ… Evaluar con el test set UNA sola vez al final
âœ… Guardar el Pipeline completo (no solo el modelo)
âœ… Documentar el proceso con comentarios y print statements
```

---

## 8. Flujo completo recomendado

```python
# 1. Dividir datos (una sola vez, al principio)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Construir Pipeline
pipe = Pipeline([...])

# 3. Buscar hiperparÃ¡metros con CV en train
gs = GridSearchCV(pipe, param_grid, cv=5, scoring="f1")
gs.fit(X_train, y_train)

# 4. Evaluar en test (UNA SOLA VEZ)
final_score = f1_score(y_test, gs.predict(X_test))
print(f"Score final en test: {final_score:.4f}")

# 5. Guardar el mejor modelo
joblib.dump(gs.best_estimator_, "modelo_final.pkl")
```
