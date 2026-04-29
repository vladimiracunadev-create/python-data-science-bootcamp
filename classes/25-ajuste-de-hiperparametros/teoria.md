# 📖 Teoría — Clase 25: Ajuste de Hiperparámetros y Selección de Modelos

## 1. ¿Qué es un parámetro y qué es un hiperparámetro?

Cuando entrenamos un modelo de Machine Learning, existen dos tipos de valores que determinan su comportamiento:

**Parámetros:** Son los valores que el modelo aprende automáticamente durante el entrenamiento. No los configuramos nosotros; el algoritmo los ajusta para minimizar el error.
- En regresión lineal: los coeficientes (pesos) de cada variable.
- En una red neuronal: los pesos de las conexiones entre neuronas.
- En un árbol de decisión: qué variable usar para dividir en cada nodo.

**Hiperparámetros:** Son los valores que nosotros definimos antes de entrenar el modelo. El algoritmo no los aprende; los recibe como configuración.
- `max_depth` en un árbol: cuántos niveles puede tener el árbol.
- `n_estimators` en RandomForest: cuántos árboles construir.
- `C` en SVM: qué tan flexible es el margen de separación.
- `k` en KNN: cuántos vecinos considerar para clasificar.

### La analogía del horno

Imagina que estás horneando pan. La receta (ingredientes, proporciones, pasos) es el modelo. El horno es el entorno controlado. La temperatura del horno y el tiempo de cocción son los **hiperparámetros**: tú los decides antes de poner el pan. Si la temperatura es demasiado baja, el pan quedará crudo. Si es demasiado alta, se quemará. Encontrar la temperatura perfecta es análogo a encontrar los mejores hiperparámetros.

---

## 2. Hiperparámetros comunes en algoritmos populares

### RandomForest
- `n_estimators`: número de árboles en el bosque (más árboles = más robusto, más lento).
- `max_depth`: profundidad máxima de cada árbol (None = sin límite, puede sobreajustar).
- `min_samples_split`: mínimo de muestras para dividir un nodo (valores altos = árbol más simple).
- `min_samples_leaf`: mínimo de muestras en una hoja.

### SVM (Support Vector Machine)
- `C`: penalización por clasificar mal (alto C = intenta clasificar todo bien = puede sobreajustar).
- `kernel`: función que transforma el espacio ('linear', 'rbf', 'poly').
- `gamma`: cuánto influye cada punto de entrenamiento ('scale', 'auto', o valor numérico).

### KNN (K-Nearest Neighbors)
- `n_neighbors`: número de vecinos a considerar.
- `metric`: distancia usada ('euclidean', 'manhattan', 'cosine').

### Árboles de Decisión
- `max_depth`, `min_samples_split`, `min_samples_leaf`, `criterion` ('gini' o 'entropy').

---

## 3. GridSearchCV: búsqueda exhaustiva

`GridSearchCV` prueba **todas las combinaciones posibles** de los hiperparámetros que le especificamos, y para cada combinación aplica validación cruzada (cross-validation).

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [3, 5, 10, None]
}
# Total de combinaciones: 3 × 4 = 12

grid_search = GridSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_grid=param_grid,
    cv=5,           # 5-fold cross-validation
    scoring='accuracy',
    n_jobs=-1       # usar todos los núcleos del procesador
)

grid_search.fit(X_train, y_train)

print("Mejores parámetros:", grid_search.best_params_)
print("Mejor score CV:", grid_search.best_score_)
```

**Ventaja:** Garantiza encontrar la mejor combinación del grid.
**Desventaja:** Si el grid es grande, puede tardar mucho tiempo. Con 10 hiperparámetros y 5 valores cada uno → 10^5 = 100,000 combinaciones.

---

## 4. RandomizedSearchCV: búsqueda aleatoria

En lugar de probar todas las combinaciones, `RandomizedSearchCV` prueba un número fijo de combinaciones aleatorias. Es especialmente útil cuando el espacio de búsqueda es grande.

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

param_dist = {
    'n_estimators': randint(50, 500),
    'max_depth': randint(2, 20),
    'min_samples_split': randint(2, 20)
}

random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=50,       # probar 50 combinaciones aleatorias
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)

random_search.fit(X_train, y_train)

print("Mejores parámetros:", random_search.best_params_)
print("Mejor score CV:", random_search.best_score_)
```

**Ventaja:** Mucho más rápido que GridSearchCV en espacios grandes.
**Desventaja:** No garantiza encontrar la combinación óptima absoluta, pero en la práctica suele encontrar soluciones muy buenas.

---

## 5. Validación cruzada (Cross-Validation)

La validación cruzada es una técnica para evaluar el rendimiento real de un modelo de forma más robusta que una simple división train/test.

### K-Fold Cross-Validation

Con `cv=5`:
1. Los datos de entrenamiento se dividen en 5 partes (folds).
2. El modelo se entrena 5 veces, usando 4 partes para entrenar y 1 para validar, rotando cuál parte se usa para validar.
3. El score final es el promedio de los 5 scores.

```
Fold 1: [V][T][T][T][T]
Fold 2: [T][V][T][T][T]
Fold 3: [T][T][V][T][T]
Fold 4: [T][T][T][V][T]
Fold 5: [T][T][T][T][V]

V = Validación, T = Entrenamiento
Score final = promedio de los 5 scores
```

Esto hace la evaluación más confiable porque el modelo es evaluado en diferentes subconjuntos de datos.

---

## 6. Curvas de aprendizaje

Una curva de aprendizaje muestra cómo cambia el rendimiento del modelo a medida que aumenta el tamaño del conjunto de entrenamiento. Sirve para diagnosticar si el modelo se beneficiaría de más datos.

```python
from sklearn.model_selection import learning_curve
import numpy as np
import matplotlib.pyplot as plt

train_sizes, train_scores, val_scores = learning_curve(
    RandomForestClassifier(**best_params),
    X, y,
    cv=5,
    train_sizes=np.linspace(0.1, 1.0, 10),
    scoring='accuracy'
)

plt.plot(train_sizes, train_scores.mean(axis=1), label='Entrenamiento')
plt.plot(train_sizes, val_scores.mean(axis=1), label='Validación')
plt.xlabel('Tamaño del conjunto de entrenamiento')
plt.ylabel('Accuracy')
plt.legend()
plt.title('Curva de aprendizaje')
```

**Interpretación:**
- Si la curva de validación sigue subiendo al final → más datos ayudarían.
- Si la curva de validación se estabilizó → más datos no mejorarán el modelo; busca mejor feature engineering o modelo diferente.
- Si hay mucha diferencia entre entrenamiento y validación → sobreajuste (overfitting).

---

## 7. Curvas de validación

Una curva de validación muestra cómo afecta un hiperparámetro específico al rendimiento del modelo.

```python
from sklearn.model_selection import validation_curve

param_range = [2, 5, 10, 15, 20, None]

train_scores, val_scores = validation_curve(
    RandomForestClassifier(n_estimators=100, random_state=42),
    X_train, y_train,
    param_name='max_depth',
    param_range=param_range,
    cv=5,
    scoring='accuracy'
)
```

Busca el valor del hiperparámetro donde la curva de validación es máxima. Si sigue subiendo conforme aumenta el hiperparámetro y hay poca diferencia con la de entrenamiento → puedes subir más ese valor.

---

## 8. Flujo completo recomendado

```
1. Separar datos en train y test (ej: 80/20)
2. Sobre train: aplicar GridSearchCV o RandomizedSearchCV con cv=5
3. Obtener best_params_ y best_score_
4. Reentrenar el modelo con best_params_ sobre TODO el train
5. Evaluar UNA SOLA VEZ sobre el test set
```

> ⚠️ **Regla de oro:** El test set solo se usa al final. Si lo usas para elegir hiperparámetros, estás "haciendo trampa" — el modelo habrá visto esos datos indirectamente y el score no será representativo del mundo real.

---

## 9. Resumen de conceptos

| Concepto | Descripción |
|---|---|
| Hiperparámetro | Configuración definida antes del entrenamiento |
| Parámetro | Valor aprendido durante el entrenamiento |
| GridSearchCV | Prueba todas las combinaciones del grid |
| RandomizedSearchCV | Prueba combinaciones aleatorias |
| cv=5 | Validación cruzada con 5 folds |
| best_params_ | Mejor combinación encontrada |
| best_score_ | Score promedio de esa mejor combinación |
| Curva de aprendizaje | Efecto del tamaño de datos en el rendimiento |
| Curva de validación | Efecto de un hiperparámetro en el rendimiento |
