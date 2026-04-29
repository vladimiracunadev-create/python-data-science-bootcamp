# 📝 Tarea — Clase 29: Introducción a redes neuronales

**Entrega:** Antes de la próxima clase  
**Formato:** Jupyter Notebook  
**Modalidad:** Individual

---

## Parte 1: Exploración de arquitecturas (30 minutos)

Usa el dataset `estudiantes.csv` y entrena 5 versiones distintas de `MLPClassifier`, variando los parámetros. Registra los resultados en una tabla.

### Configuraciones a probar:

| # | hidden_layer_sizes | activation | max_iter | Precisión (completa tú) |
|---|-------------------|------------|----------|------------------------|
| 1 | `(10,)` | `relu` | 200 | |
| 2 | `(100,)` | `relu` | 200 | |
| 3 | `(100, 50)` | `relu` | 300 | |
| 4 | `(100, 50)` | `tanh` | 300 | |
| 5 | `(200, 100, 50)` | `relu` | 500 | |

### Código base:

```python
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import time

# Cargar datos (o crear el dataset de ejemplo)
np.random.seed(42)
n = 400
# ... (usa el código de generación de la clase)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

# Entrena y registra cada configuración
configuraciones = [
    {'hidden_layer_sizes': (10,), 'activation': 'relu', 'max_iter': 200},
    {'hidden_layer_sizes': (100,), 'activation': 'relu', 'max_iter': 200},
    # ... agrega las demás
]

for config in configuraciones:
    inicio = time.time()
    modelo = MLPClassifier(**config, random_state=42)
    modelo.fit(X_train_sc, y_train)
    tiempo = time.time() - inicio
    acc = accuracy_score(y_test, modelo.predict(X_test_sc))
    print(f'{config[\"hidden_layer_sizes\"]} | {config[\"activation\"]} | {acc:.2%} | {tiempo:.2f}s')
```

**Preguntas:**
1. ¿Cuál configuración obtuvo mejor precisión?
2. ¿Más neuronas siempre mejora el resultado?
3. ¿Hubo diferencia entre usar `relu` y `tanh`?
4. ¿Cuál configuración fue más rápida de entrenar? ¿Por qué?

---

## Parte 2: Comparación final de modelos (30 minutos)

Entrena los siguientes 4 modelos en el mismo dataset y compara su rendimiento:

1. `MLPClassifier` con la mejor configuración que encontraste
2. `DecisionTreeClassifier(max_depth=5)`
3. `RandomForestClassifier(n_estimators=100)`
4. `LogisticRegression()`

Para cada modelo, reporta:
- Precisión en test set
- Tiempo de entrenamiento
- ¿Requiere normalización? Sí/No

Presenta los resultados en una tabla ordenada de mayor a menor precisión.

---

## Parte 3: Análisis de la curva de aprendizaje (15 minutos)

Con la mejor configuración de MLP que encontraste:

1. gráfica la `loss_curve_` del modelo
2. Describe en 2-3 oraciones qué muestra el gráfico
3. Responde: ¿El modelo convergió? ¿Cómo lo sabes?

```python
plt.figure(figsize=(10, 4))
plt.plot(mejor_modelo.loss_curve_)
plt.title('Curva de aprendizaje')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()
```

---

## Parte 4: Reflexión conceptual (sin código)

Responde en 3-5 oraciones cada pregunta:

1. **Analogía propia:** Describe con tus propias palabras cómo funciona una red neuronal usando una analogía distinta a la de los filtros fotográficos. Puede ser de cocina, deporte, música, lo que se te ocurra.

2. **¿Cuándo NO usar MLP?** Da dos situaciones concretas donde preferirías usar un Random Forest en lugar de una red neuronal, y explica por qué.

3. **El futuro:** Ahora que entiendes los conceptos básicos, ¿qué tipos de problemas te gustaría resolver con redes neuronales más avanzadas? ¿Por qué?

---

## BONUS (opcional, +10 puntos extra)

Instala la librería `tensorflow` y ejecuta el siguiente código de Keras. Compara el resultado con tu mejor MLPClassifier.

```bash
pip install tensorflow
```

```python
import tensorflow as tf
from tensorflow import keras

modelo_keras = keras.Sequential([
    keras.layers.Dense(100, activation='relu', input_shape=(X_train_sc.shape[1],)),
    keras.layers.Dense(50, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

modelo_keras.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

history = modelo_keras.fit(
    X_train_sc, y_train,
    epochs=50,
    batch_size=32,
    validation_split=0.2,
    verbose=0
)

loss, acc = modelo_keras.evaluate(X_test_sc, y_test, verbose=0)
print(f'Keras - Precisión en test: {acc:.2%}')

# Graficar historial de entrenamiento
plt.plot(history.history['accuracy'], label='train')
plt.plot(history.history['val_accuracy'], label='validación')
plt.title('Precisión durante entrenamiento (Keras)')
plt.legend()
plt.show()
```

**Pregunta bonus:** ¿Cuál es la diferencia entre `mlp_final.loss_curve_` de sklearn y `history.history['loss']` de Keras? ¿Qué información adicional da Keras?

---

## Criterios de evaluación

| Criterio | Puntaje |
|----------|---------|
| Tabla de configuraciones completa y correcta | 25 pts |
| Comparación de modelos con análisis | 25 pts |
| Gráfico y descripción de curva de aprendizaje | 20 pts |
| Reflexión conceptual clara y personal | 20 pts |
| Código limpio y comentado | 10 pts |
| **Total** | **100 pts** |
