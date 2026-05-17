# 📝 Homework — Clase 25: Ajuste de Hiperparámetros y Selección de Modelos

> Entrega individual. Plazo: antes de la próxima clase.

---

## Tarea 1 — Optimizar un modelo diferente (obligatoria)

En clase optimizamos RandomForest. Ahora aplica GridSearchCV a un algoritmo diferente: **KNN** (K-Nearest Neighbors).

```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import classification_report
import pandas as pd

df = pd.read_csv('datasets/estudiantes.csv')
X = df.drop(columns=['aprobado'])
y = df['aprobado']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define el grid de hiperparámetros para KNN
param_grid_knn = {
    'n_neighbors': [3, 5, 7, 11, 15, 21],
    'metric': ['euclidean', 'manhattan'],
    'weights': ['uniform', 'distance']
}

# Tu código aquí: GridSearchCV, fit, resultados
```

**Entrega:**
1. Código funcionando con resultados impresos.
2. ¿Cuál combinación de hiperparámetros fue la mejor?
3. ¿Mejoró respecto al modelo KNN con parámetros por defecto? ¿Cuánto?
4. ¿El mejor `n_neighbors` te sorprendió? ¿Por qué crees que ese número fue el mejor?

---

## Tarea 2 — Curva de aprendizaje propia (obligatoria)

Genera y gráfica la curva de aprendizaje del RandomForest optimizado (con los `best_params_` de clase).

```python
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

train_sizes, train_scores, val_scores = learning_curve(
    RandomForestClassifier(**mejores_params, random_state=42),
    X, y,
    cv=5,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy',
    n_jobs=-1
)

# Gráfica train_scores.mean(axis=1) y val_scores.mean(axis=1) vs train_sizes
```

**Preguntas para responder en comentarios del código:**
1. ¿El modelo se beneficiaría de más datos? ¿Cómo lo sabes por la gráfica?
2. ¿Hay evidencia de overfitting? ¿En qué parte de la curva se ve?
3. Si pudieras conseguir 500 muestras más de datos, ¿crees que mejoraría el modelo?

---

## Tarea 3 — Investigación breve (opcional, +1 punto)

Investiga y responde en máximo 3 párrafos:

**¿Qué es Bayesian Optimization para búsqueda de hiperparámetros?**

Pistas para buscar:
- Librería `optuna` en Python
- Cómo se diferencia de GridSearch y RandomSearch
- ¿Por qué puede ser más eficiente?

No necesitas implementarlo, solo explicarlo con tus propias palabras y dar un ejemplo de cuándo usarías cada estrategia de búsqueda.

---

## Formato de entrega

- Archivo `.ipynb` o `.py` con código comentado.
- Incluye tus respuestas a las preguntas como comentarios o celdas de markdown.
- Nombre del archivo: `homework_clase25_[tu_nombre].ipynb`

---

## Rúbrica

| Criterio | Puntos |
|---|---|
| Tarea 1: código funcionando | 3 |
| Tarea 1: análisis de resultados | 2 |
| Tarea 2: curva generada y graficada | 3 |
| Tarea 2: interpretación correcta | 2 |
| Tarea 3 (opcional) | 1 |
| **Total** | **10 (+1)** |
