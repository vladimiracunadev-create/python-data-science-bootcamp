# 📊 Slides — Clase 29: Introducción a redes neuronales

---

## Slide 1: ¿Qué es una red neuronal?

Una red neuronal artificial está **inspirada en el cerebro humano**, pero no es idéntica a él.

**En el cerebro:**
- Las neuronas biológicas reciben señales eléctricas
- Si la señal es suficientemente fuerte, la neurona "dispara"
- Las conexiones entre neuronas se fortalecen con el uso

**En una red neuronal artificial:**
- Las neuronas artificiales reciben números como entrada
- Calculan una suma ponderada y aplican una función
- Los "pesos" de las conexiones se ajustan durante el entrenamiento

---

## Slide 2: Una sola neurona

```
Entradas        Pesos        Suma + Bias     Activación     Salida
x1 = 0.8   ──► w1 = 0.5 ──►
x2 = 0.3   ──► w2 = 1.2 ──►  z = Σ(xi·wi) + b  ──►  f(z)  ──►  ŷ
x3 = 0.6   ──► w3 = 0.8 ──►
```

**Fórmula:**
```
z = x1·w1 + x2·w2 + x3·w3 + b
ŷ = f(z)
```

Donde `f` es la **función de activación**.

---

## Slide 3: Funciones de activación

### Sigmoid σ(z)
```
f(z) = 1 / (1 + e^(-z))
```
- Salida entre 0 y 1
- Útil para capas de salida en clasificación binaria
- Problema: gradientes que desaparecen en redes profundas

### ReLU (Rectified Linear Unit)
```
f(z) = max(0, z)
```
- Si z < 0, salida = 0
- Si z ≥ 0, salida = z
- Simple, eficiente, funciona bien en práctica
- La más usada en capas ocultas hoy en día

---

## Slide 4: Capas de una red neuronal

```
ENTRADA       CAPA OCULTA 1    CAPA OCULTA 2    SALIDA
  o                o                 o
  o     ────►     o      ────►      o      ────►   o (predicción)
  o                o                 o
  o                o                 o
```

- **Capa de entrada:** una neurona por cada variable del dataset
- **Capas ocultas:** extraen patrones intermedios
- **Capa de salida:** genera la predicción final

**¿Por qué "profunda"?** Cuantas más capas ocultas, más "profunda" es la red.

---

## Slide 5: Analogía — capas de filtros

Imagina que procesas una foto para identificar si hay un gato:

| Capa | Qué detecta |
|------|-------------|
| Capa 1 | Bordes y contornos |
| Capa 2 | Formas simples (círculos, líneas curvas) |
| Capa 3 | Partes (orejas, ojos, bigotes) |
| Capa 4 | El objeto completo (gato) |

Cada capa construye sobre lo que aprendió la capa anterior.

---

## Slide 6: Cómo aprende una red neuronal

### 1. Forward pass (propagación hacia adelante)
- Los datos entran por la izquierda
- Cada neurona calcula su valor y lo pasa a la siguiente capa
- Al final obtenemos una predicción ŷ

### 2. Calcular el error (loss)
- Comparamos ŷ con el valor real y
- Usamos una función de pérdida: `loss = (y - ŷ)²` o similar

### 3. Backward pass (backpropagation)
- Calculamos cómo cambiar cada peso para reducir el error
- Usamos la derivada de la función de pérdida
- Los pesos se actualizan en pequeños pasos (learning rate)

### 4. Repetir miles de veces (epochs)
- Con cada repetición, el error va disminuyendo
- El modelo "aprende" ajustando los pesos iterativamente

---

## Slide 7: MLPClassifier en scikit-learn

MLP = Multi-Layer Perceptron. Es la red neuronal más básica.

```python
from sklearn.neural_network import MLPClassifier

modelo = MLPClassifier(
    hidden_layer_sizes=(100, 50),  # 2 capas: 100 y 50 neuronas
    activation='relu',              # función de activación
    max_iter=300,                   # épocas máximas
    random_state=42
)

modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)
```

---

## Slide 8: Parámetros clave de MLPClassifier

| Parámetro | Qué controla | Valor típico |
|-----------|-------------|-------------|
| `hidden_layer_sizes` | Arquitectura de la red | `(100,)` o `(100, 50)` |
| `activation` | Función de activación | `'relu'` (recomendado) |
| `max_iter` | Épocas de entrenamiento | `200-500` |
| `learning_rate_init` | Tamaño del paso de ajuste | `0.001` |
| `random_state` | Reproducibilidad | cualquier número |

---

## Slide 9: ¿Cuándo usar redes neuronales?

### Redes neuronales brillan cuando:
- Tienes **muchos datos** (miles o millones de ejemplos)
- Los patrones son **muy complejos** y no lineales
- Trabajas con **imágenes, texto o audio**
- Tienes suficiente **capacidad computacional**

### Prefiere árboles/Random Forest cuando:
- Tienes **pocos datos** (decenas o cientos de filas)
- Trabajas con **datos tabulares estructurados**
- Necesitas **interpretabilidad** (explicar las decisiones)
- El tiempo de entrenamiento es limitado

---

## Slide 10: El siguiente nivel — Keras y TensorFlow

Scikit-learn es perfecto para empezar, pero para proyectos complejos usamos:

**TensorFlow / Keras**
- Librería de Google para redes neuronales profundas
- Más flexible y potente
- Permite construir arquitecturas complejas (CNNs, RNNs, Transformers)

**PyTorch**
- Librería de Meta (Facebook)
- Muy popular en investigación
- Más control sobre los detalles de implementación

```python
# Preview de Keras (lo veremos en clases futuras)
from tensorflow import keras

modelo = keras.Sequential([
    keras.layers.Dense(100, activation='relu'),
    keras.layers.Dense(50, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])
```

---

## Slide 11: Resumen

> Una red neuronal aprende representaciones progresivamente más complejas de los datos, pasando la información por capas de transformación.

**Lo que vimos hoy:**
- Cómo funciona una neurona artificial
- Qué son las funciones de activación (sigmoid, ReLU)
- Cómo aprende una red (forward pass → loss → backprop)
- Cómo usar MLPClassifier en scikit-learn
- Cuándo usar redes vs modelos de árbol
