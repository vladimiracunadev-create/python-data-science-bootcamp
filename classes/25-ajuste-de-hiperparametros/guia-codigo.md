# 💻 Guía de código — Clase 25: Ajuste de Hiperparámetros

> Explicación detallada del código clave, bloque por bloque.

## Bloque 1: Preparar datos y definir la grilla de búsqueda

```python
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Cargar datos
df = pd.read_csv("estudiantes.csv")

# Separar features y target
X = df.drop(columns=["aprobado"])
y = df["aprobado"]

# Dividir en entrenamiento y test ANTES de cualquier búsqueda
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Definir la grilla de hiperparámetros a explorar
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10, None],
    "min_samples_split": [2, 5, 10]
}
```

**¿Qué hace este bloque?** Carga el dataset, separa las variables de entrada (`X`) de la variable objetivo (`y`), divide los datos en entrenamiento y test, y define el diccionario `param_grid` con todas las combinaciones de hiperparámetros que queremos probar.

**¿Por qué se escribe así?** Es fundamental dividir los datos en train/test ANTES de hacer la búsqueda. Si incluimos el test en el proceso de búsqueda, el modelo "ve" datos que no debería conocer y el rendimiento reportado será engañosamente optimista (data leakage).

**Resultado esperado:** Un diccionario con 3 × 4 × 3 = 36 combinaciones posibles de hiperparámetros. Con 5-fold CV, se entrenarán 36 × 5 = 180 modelos.

---

## Bloque 2: Entrenar GridSearchCV y extraer resultados

```python
# Crear el modelo base
modelo_base = RandomForestClassifier(random_state=42)

# Crear GridSearchCV: combina modelo + grilla + validación cruzada
grid_search = GridSearchCV(
    estimator=modelo_base,
    param_grid=param_grid,
    cv=5,                    # 5-fold cross-validation
    scoring="accuracy",      # métrica de evaluación
    n_jobs=-1,               # usar todos los núcleos disponibles
    verbose=1                # mostrar progreso en pantalla
)

# Entrenar: prueba todas las combinaciones en los datos de entrenamiento
grid_search.fit(X_train, y_train)

# Ver los mejores hiperparámetros encontrados
print("Mejores hiperparámetros:", grid_search.best_params_)
print("Mejor score (CV):", grid_search.best_score_)

# Evaluar en el conjunto de test (solo se hace UNA vez al final)
score_test = grid_search.score(X_test, y_test)
print("Score en test:", score_test)
```

**¿Qué hace este bloque?** `GridSearchCV` prueba todas las combinaciones del `param_grid`, entrenando y evaluando cada una con validación cruzada de 5 pliegues. Al final, `best_params_` contiene la combinación ganadora y `best_score_` el promedio de accuracy en los 5 pliegues con esa combinación.

**¿Por qué se escribe así?** El parámetro `n_jobs=-1` es importante para aprovechar todos los núcleos del procesador y reducir el tiempo de búsqueda. `verbose=1` permite ver el progreso para no pensar que el programa se colgó. Llamar `.score(X_test, y_test)` al final usa automáticamente el mejor modelo encontrado.

**Resultado esperado:** Imprime algo como `Mejores hiperparámetros: {'max_depth': 5, 'min_samples_split': 2, 'n_estimators': 200}` y dos scores entre 0 y 1. El score de CV puede ser ligeramente más alto que el de test; una diferencia grande indica sobreajuste.

---

## Bloque 3: RandomizedSearchCV para espacios grandes

```python
from sklearn.model_selection import RandomizedSearchCV
from scipy.stats import randint

# Definir distribuciones de probabilidad (no listas fijas)
param_dist = {
    "n_estimators": randint(50, 500),          # entero aleatorio entre 50 y 500
    "max_depth": [3, 5, 10, 15, 20, None],
    "min_samples_split": randint(2, 20),
    "max_features": ["sqrt", "log2", None]
}

# RandomizedSearchCV: prueba solo n_iter combinaciones elegidas al azar
random_search = RandomizedSearchCV(
    estimator=RandomForestClassifier(random_state=42),
    param_distributions=param_dist,
    n_iter=30,              # probar solo 30 combinaciones aleatorias
    cv=5,
    scoring="accuracy",
    n_jobs=-1,
    random_state=42,        # para reproducibilidad
    verbose=1
)

random_search.fit(X_train, y_train)

print("Mejores hiperparámetros (Random):", random_search.best_params_)
print("Mejor score (CV):", random_search.best_score_)
```

**¿Qué hace este bloque?** En lugar de probar todas las combinaciones posibles (que podrían ser miles), `RandomizedSearchCV` muestrea aleatoriamente `n_iter=30` combinaciones del espacio de búsqueda. `randint(50, 500)` permite explorar valores continuos, no solo unos pocos predefinidos.

**¿Por qué se escribe así?** Cuando la grilla tiene muchos hiperparámetros o rangos amplios, la búsqueda exhaustiva es computacionalmente imposible. La investigación ha demostrado que búsquedas aleatorias de tamaño moderado encuentran combinaciones casi tan buenas como la búsqueda exhaustiva, con una fracción del tiempo. `random_state=42` garantiza reproducibilidad.

**Resultado esperado:** Resultados similares a `GridSearchCV` pero en mucho menos tiempo. Con 30 iteraciones y 5 folds, solo se entrenan 150 modelos en vez de potencialmente miles.

---

## Bloque 4: Visualizar resultados con curvas de validación

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import validation_curve

# Evaluar cómo cambia el score al variar un hiperparámetro
param_range = [10, 50, 100, 200, 300, 500]

train_scores, val_scores = validation_curve(
    RandomForestClassifier(random_state=42),
    X_train, y_train,
    param_name="n_estimators",    # hiperparámetro a variar
    param_range=param_range,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

# Calcular medias y desviaciones estándar
train_mean = np.mean(train_scores, axis=1)
val_mean = np.mean(val_scores, axis=1)
train_std = np.std(train_scores, axis=1)
val_std = np.std(val_scores, axis=1)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(param_range, train_mean, label="Entrenamiento", color="blue")
plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, alpha=0.2, color="blue")
plt.plot(param_range, val_mean, label="Validación cruzada", color="orange")
plt.fill_between(param_range, val_mean - val_std, val_mean + val_std, alpha=0.2, color="orange")
plt.xlabel("n_estimators")
plt.ylabel("Accuracy")
plt.title("Curva de validación: n_estimators")
plt.legend()
plt.grid(True)
plt.show()
```

**¿Qué hace este bloque?** Genera una **curva de validación** que muestra cómo evoluciona el rendimiento del modelo en entrenamiento y en validación cruzada a medida que se varía el valor de `n_estimators`. La región sombreada representa la variabilidad entre los 5 folds.

**¿Por qué se escribe así?** Las curvas de validación son una herramienta diagnóstica fundamental. Si la curva de entrenamiento es alta pero la de validación es baja → sobreajuste. Si ambas curvas son bajas → subajuste. La banda de incertidumbre (`fill_between`) muestra cuán estable es el modelo.

**Resultado esperado:** Una gráfica donde se puede identificar el rango óptimo de `n_estimators`. Generalmente, el score de validación crece rápido al principio y luego se estabiliza o baja levemente, indicando el punto de rendimientos decrecientes.

---

## Errores comunes y cómo resolverlos

| Error | Causa | Solución |
|---|---|---|
| `ValueError: could not convert string to float` | El dataset tiene columnas de texto que no fueron codificadas | Usar `LabelEncoder` o `pd.get_dummies()` antes del GridSearch |
| El GridSearch tarda horas | La grilla es demasiado grande o el dataset es enorme | Usar `RandomizedSearchCV` con `n_iter` pequeño, o reducir el rango de la grilla |
| `best_score_` muy alto pero score en test muy bajo | Data leakage: los datos de test contaminaron el entrenamiento | Asegurarse de dividir train/test ANTES de llamar a `.fit()` |
| `MemoryError` durante GridSearch | Demasiados modelos en paralelo consumen toda la RAM | Reducir `n_jobs` o el tamaño de la grilla |
| Todos los scores iguales en `cv_results_` | El modelo siempre predice la clase mayoritaria | Revisar si el dataset está desbalanceado y usar `scoring='f1'` en lugar de `accuracy` |
| `KeyError` al acceder a `best_params_` | El GridSearch no terminó de entrenarse | Verificar que se llamó `.fit()` antes de acceder a atributos del resultado |
