# 🎞️ Slides — Clase 25: Ajuste de Hiperparámetros y Selección de Modelos

---

## Slide 1 — ¿Qué problema resolvemos hoy?

Entrenaste un modelo. Obtienes un 72% de accuracy.
¿Cómo mejorar sin cambiar los datos?

**Respuesta:** ajustando los hiperparámetros.

---

## Slide 2 — Parámetros vs Hiperparámetros

| Concepto | Quién lo define | Ejemplo |
|---|---|---|
| **Parámetro** | El modelo (lo aprende) | pesos de una red, coeficientes de regresión |
| **Hiperparámetro** | Nosotros (lo configuramos) | max_depth, n_estimators, C, k |

> 💡 Analogía: la receta es el modelo, el horno es el hiperparámetro.
> Puedes tener la mejor receta del mundo, pero si el horno está a la temperatura equivocada, el resultado no sirve.

---

## Slide 3 — Hiperparámetros comunes

```
RandomForest:   n_estimators, max_depth, min_samples_split
SVM:            C, kernel, gamma
KNN:            n_neighbors, metric
Regresión L1/L2: alpha
```

Cada algoritmo tiene su propio "panel de control".

---

## Slide 4 — ¿Cómo encontrar los mejores valores?

**Opción 1: A mano** — probar uno por uno (lento, subjetivo)

**Opción 2: GridSearchCV** — prueba TODAS las combinaciones

**Opción 3: RandomizedSearchCV** — prueba combinaciones ALEATORIAS (más rápido)

---

## Slide 5 — GridSearchCV en acción

```python
from sklearn.model_selection import GridSearchCV

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10]
}
# 3 x 3 = 9 combinaciones

grid = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid.fit(X_train, y_train)

print(grid.best_params_)
print(grid.best_score_)
```

Con `cv=5` cada combinación se evalúa 5 veces → más robusto.

---

## Slide 6 — RandomizedSearchCV: más rápido

```python
from sklearn.model_selection import RandomizedSearchCV

param_dist = {
    'n_estimators': range(50, 500),
    'max_depth': range(2, 20)
}

random_search = RandomizedSearchCV(
    RandomForestClassifier(), param_dist,
    n_iter=20, cv=5, random_state=42
)
random_search.fit(X_train, y_train)
```

Solo prueba 20 combinaciones aleatorias en lugar de cientos.

---

## Slide 7 — Curva de aprendizaje

Pregunta: ¿agregar más datos mejoraría el modelo?

```
Score
 1.0 |      ___________
 0.9 |     /           \___________
 0.8 |    /
 0.7 |   /
     |__________________
       100  500  1000  5000   N datos
```

Si la curva de validación sigue subiendo → necesitas más datos.
Si ya se estabilizó → más datos no ayudan mucho.

---

## Slide 8 — Curva de validación

Pregunta: ¿cómo afecta UN hiperparámetro específico al rendimiento?

```python
from sklearn.model_selection import validation_curve

train_scores, val_scores = validation_curve(
    RandomForestClassifier(), X, y,
    param_name='max_depth',
    param_range=range(1, 15),
    cv=5
)
```

Busca el punto donde validación es máxima sin sobreajuste.

---

## Slide 9 — Resumen del flujo completo

```
Datos → Split train/test
      → GridSearchCV (cv=5 dentro de train)
      → best_params_ → modelo final
      → evaluar en test (solo al final)
```

> ⚠️ Nunca uses el test set para elegir hiperparámetros.
> El test set es para la evaluación final, no para decisiones de diseño.

---

## Slide 10 — Conclusión

- Los hiperparámetros son ajustes que nosotros controlamos.
- GridSearchCV prueba todo; RandomizedSearchCV prueba una muestra.
- La validación cruzada hace la evaluación más confiable.
- Las curvas de aprendizaje y validación te ayudan a diagnosticar el modelo.
