# 🏋️ Ejercicios — Clase 25: Ajuste de Hiperparámetros y Selección de Modelos

> Completa estos ejercicios en orden. Cada uno construye sobre el anterior.

---

## Ejercicio 1 — Identificar parámetros vs hiperparámetros

**Instrucciones:** Clasifica cada elemento de la lista como **parámetro** (lo aprende el modelo) o **hiperparámetro** (lo definimos nosotros).

| Elemento | ¿Parámetro o hiperparámetro? |
|---|---|
| Los coeficientes de una regresión lineal | |
| `max_depth=5` en un árbol de decisión | |
| Los pesos de una red neuronal | |
| `n_neighbors=7` en KNN | |
| El umbral de decisión de un árbol (qué valor de qué variable usar) | |
| `C=0.1` en SVM | |
| `n_estimators=200` en RandomForest | |
| Las probabilidades de cada clase en Naive Bayes | |

---

## Ejercicio 2 — Primer modelo sin optimizar

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Cargar datos
df = pd.read_csv('datasets/estudiantes.csv')

# Preparar features (ajusta según las columnas disponibles)
X = df.drop(columns=['aprobado'])
y = df['aprobado']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar con parámetros por defecto
modelo_base = RandomForestClassifier(random_state=42)
modelo_base.fit(X_train, y_train)

accuracy_base = accuracy_score(y_test, modelo_base.predict(X_test))
print(f"Accuracy base (parámetros por defecto): {accuracy_base:.4f}")
print(f"Parámetros por defecto: n_estimators={modelo_base.n_estimators}, max_depth={modelo_base.max_depth}")
```

**Preguntas:**
1. ¿Cuál es el accuracy con parámetros por defecto?
2. ¿Cuál es el `max_depth` por defecto? ¿Qué significa cuando es `None`?

---

## Ejercicio 3 — GridSearchCV básico

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None]
}

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X_train, y_train)

print("Mejores parámetros:", grid_search.best_params_)
print("Mejor score CV:", grid_search.best_score_:.4f)
print("Score en test:", grid_search.score(X_test, y_test):.4f)
```

**Preguntas:**
1. ¿Cuántas combinaciones total probó GridSearchCV?
2. ¿Cuántos modelos entrenó en total (combinaciones × folds)?
3. ¿Mejoraron los resultados respecto al modelo base?

---

## Ejercicio 4 — Explorar los resultados del grid

```python
import pandas as pd

# Resultados de todas las combinaciones
resultados = pd.DataFrame(grid_search.cv_results_)

# Ver columnas disponibles
print(resultados.columns.tolist())

# Las 5 mejores combinaciones
top5 = resultados.sort_values('rank_test_score')[
    ['params', 'mean_test_score', 'std_test_score', 'rank_test_score']
].head(5)

print(top5)
```

**Preguntas:**
1. ¿Cuál fue la combinación con el score más alto?
2. ¿Qué combinación tuvo el menor `std_test_score`? ¿Por qué importa la desviación estándar?
3. ¿Hay combinaciones con score similar pero con menos `n_estimators`? ¿Cuál elegirías y por qué?

---

## Ejercicio 5 — RandomizedSearchCV

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    'n_estimators': randint(50, 300),
    'max_depth': randint(2, 15),
    'min_samples_split': randint(2, 20),
    'min_samples_leaf': randint(1, 10)
}

random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=30,
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)

print("Mejores parámetros:", random_search.best_params_)
print("Mejor score CV:", random_search.best_score_:.4f)
print("Score en test:", random_search.score(X_test, y_test):.4f)
```

**Preguntas:**
1. ¿Qué tan diferente es el resultado de GridSearchCV vs RandomizedSearchCV?
2. ¿Cuánto tiempo tardó cada uno (usa `%%time` en la celda)?
3. ¿Cuándo preferirías usar RandomizedSearchCV sobre GridSearchCV?

---

## Ejercicio 6 — Curva de validación (visualización)

```python
from sklearn.model_selection import validation_curve
import matplotlib.pyplot as plt
import numpy as np

param_range = [2, 5, 10, 15, 20, 30, 50]

train_scores, val_scores = validation_curve(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X_train, y_train,
    param_name='max_depth',
    param_range=param_range,
    cv=5,
    scoring='accuracy'
)

plt.figure(figsize=(10, 5))
plt.plot(param_range, train_scores.mean(axis=1), 'o-', label='Entrenamiento', color='steelblue')
plt.fill_between(param_range,
                 train_scores.mean(axis=1) - train_scores.std(axis=1),
                 train_scores.mean(axis=1) + train_scores.std(axis=1),
                 alpha=0.1, color='steelblue')

plt.plot(param_range, val_scores.mean(axis=1), 'o-', label='Validación', color='darkorange')
plt.fill_between(param_range,
                 val_scores.mean(axis=1) - val_scores.std(axis=1),
                 val_scores.mean(axis=1) + val_scores.std(axis=1),
                 alpha=0.1, color='darkorange')

plt.xlabel('max_depth')
plt.ylabel('Accuracy')
plt.title('Curva de validación: efecto de max_depth')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Preguntas:**
1. ¿A partir de qué valor de `max_depth` empieza el sobreajuste?
2. ¿Cuál es el `max_depth` óptimo según la curva?
3. ¿Qué ocurre con la curva de entrenamiento cuando `max_depth` es muy alto?

---

## Ejercicio 7 — Desafío integrador

Usando los mejores hiperparámetros encontrados en los ejercicios anteriores:

1. Entrena el modelo final con `best_params_` sobre todos los datos de entrenamiento.
2. Evalúa en el test set con accuracy, precisión, recall y f1-score.
3. Compara el accuracy del modelo base vs el modelo optimizado.
4. ¿Cuánto mejoraste en porcentaje?

```python
from sklearn.metrics import classification_report

# Tu código aquí
modelo_final = RandomForestClassifier(**grid_search.best_params_, random_state=42)
modelo_final.fit(X_train, y_train)

y_pred = modelo_final.predict(X_test)
print(classification_report(y_test, y_pred))

mejora = (accuracy_score(y_test, y_pred) - accuracy_base) * 100
print(f"Mejora respecto al modelo base: +{mejora:.2f}%")
```

---

## Criterios de evaluación

- Ejercicios 1-3: comprensión conceptual y código funcionando.
- Ejercicios 4-5: interpretación de resultados y comparación.
- Ejercicio 6: interpretación visual de la curva.
- Ejercicio 7: integración y reflexión sobre la mejora obtenida.
