# 📖 Teoría — Clase 29: Introducción a redes neuronales

## 1. La inspiración biológica

El cerebro humano tiene aproximadamente 86 mil millones de neuronas. Cada neurona está conectada con miles de otras a través de sinapsis. Cuando una neurona recibe suficientes señales, "dispara" y transmite la señal a otras neuronas.

Las redes neuronales artificiales toman prestado este concepto, pero de forma muy simplificada. No son un modelo del cerebro — son una herramienta matemática inspirada en él. El objetivo no es simular la biología, sino construir un sistema que pueda aprender patrones complejos a partir de datos.

---

## 2. Una neurona artificial

### La fórmula

Una neurona artificial hace un cálculo muy simple:

```
z = (x1 × w1) + (x2 × w2) + ... + (xn × wn) + b
salida = f(z)
```

Donde:
- `x1, x2, ..., xn` son las entradas (las variables del dataset)
- `w1, w2, ..., wn` son los **pesos** (cuánto importa cada entrada)
- `b` es el **bias** (un término de ajuste independiente)
- `f` es la **función de activación**

### ¿Qué hace el peso?

El peso controla cuánto influye cada entrada en la salida. Un peso alto (positivo) significa que esa variable importa mucho y empuja la predicción hacia arriba. Un peso negativo la empuja hacia abajo. Un peso cercano a cero significa que esa variable casi no importa.

### ¿Qué hace el bias?

El bias permite que la neurona "encienda" o "apague" incluso cuando todas las entradas son cero. Es similar al término independiente en una regresión lineal.

---

## 3. Funciones de activación

### 3.1 ¿Por qué necesitamos una función de activación?

Sin una función de activación no lineal, una red de muchas capas sería equivalente a una sola capa lineal (la composición de funciones lineales es lineal). La no linealidad es lo que permite a las redes aprender patrones complejos.

### 3.2 Sigmoid

```
f(z) = 1 / (1 + e^(-z))
```

- Rango de salida: [0, 1]
- Interpreta la salida como una probabilidad
- Problema: cuando z es muy grande o muy pequeño, el gradiente se vuelve casi cero (problema del gradiente que desaparece)
- Uso actual: principalmente en la capa de salida para clasificación binaria

### 3.3 ReLU (Rectified Linear Unit)

```
f(z) = max(0, z)
```

- Si z ≤ 0, la salida es 0 (la neurona "se apaga")
- Si z > 0, la salida es igual a z
- Muy simple de calcular
- Funciona bien en práctica y es la más usada en capas ocultas
- Variante: Leaky ReLU, que permite pequeños valores negativos

### 3.4 Tanh

```
f(z) = (e^z - e^(-z)) / (e^z + e^(-z))
```

- Rango de salida: [-1, 1]
- Similar a sigmoid pero centrada en cero
- Menos usada hoy en día

---

## 4. Arquitectura de una red

### Capas

Una red neuronal tiene tres tipos de capas:

1. **Capa de entrada (input layer):** Recibe los datos. Tiene tantas neuronas como variables tiene el dataset. No realiza cálculos — solo pasa los datos a la siguiente capa.

2. **Capas ocultas (hidden layers):** Hacen el trabajo pesado. Cada neurona calcula z = Σ(xi × wi) + b y aplica la función de activación. Pueden haber una, dos, diez o más capas ocultas.

3. **Capa de salida (output layer):** Genera la predicción final. Para clasificación binaria: 1 neurona con sigmoid. Para clasificación multiclase: una neurona por clase con softmax.

### ¿Cuántas capas y neuronas usar?

No hay una regla universal. En la práctica:

| Problema | Arquitectura sugerida para empezar |
|----------|----------------------------------|
| Clasificación tabular simple | `(50,)` o `(100,)` |
| Clasificación tabular compleja | `(100, 50)` |
| Datos complejos | `(256, 128, 64)` |

Más capas y neuronas = más capacidad, pero también más riesgo de overfitting y más tiempo de entrenamiento.

---

## 5. Cómo aprende: el proceso de entrenamiento

### 5.1 Forward pass (propagación hacia adelante)

Los datos de entrenamiento entran por la capa de entrada. Cada capa calcula sus valores y los pasa a la siguiente hasta llegar a la capa de salida, que produce una predicción.

### 5.2 Función de pérdida (loss function)

Mide cuán equivocada está la predicción. Para clasificación binaria se usa comúnmente la entropía cruzada (binary cross-entropy):

```
loss = -[y × log(ŷ) + (1-y) × log(1-ŷ)]
```

Para regresión se usa el Error Cuadrático Medio (MSE):

```
loss = (y - ŷ)²
```

### 5.3 Backward pass (backpropagation)

El algoritmo calcula el gradiente de la función de pérdida con respecto a cada peso de la red. El gradiente indica en qué dirección y cuánto mover cada peso para reducir el error.

Usando la regla de la cadena del cálculo diferencial, este proceso se hace capa por capa de atrás hacia adelante (de ahí el nombre "backpropagation").

### 5.4 Actualización de pesos (descenso de gradiente)

Cada peso se actualiza según:

```
w_nuevo = w_viejo - learning_rate × gradiente
```

El `learning_rate` (tasa de aprendizaje) controla el tamaño del paso. Si es muy grande, el modelo puede oscilar y no converger. Si es muy pequeño, el entrenamiento será muy lento.

### 5.5 Epochs

Un epoch es una pasada completa por todo el dataset de entrenamiento. El entrenamiento consiste en repetir este ciclo (forward → loss → backward → actualizar pesos) muchas veces, reduciendo el error progresivamente.

---

## 6. MLPClassifier en scikit-learn

`MLPClassifier` (Multi-Layer Perceptron Classifier) es la implementación de red neuronal de scikit-learn. Es perfecta para aprender los conceptos porque comparte la misma API que el resto de los modelos de sklearn.

```python
from sklearn.neural_network import MLPClassifier

# Arquitectura: 2 capas ocultas de 100 y 50 neuronas
modelo = MLPClassifier(
    hidden_layer_sizes=(100, 50),
    activation='relu',
    solver='adam',          # algoritmo de optimización
    max_iter=300,           # número máximo de epochs
    learning_rate_init=0.001,
    random_state=42
)
```

### El solver Adam

Adam (Adaptive Moment Estimation) es el algoritmo de optimización estándar para redes neuronales. Adapta automáticamente la tasa de aprendizaje para cada parámetro, lo que lo hace más eficiente que el descenso de gradiente clásico.

---

## 7. Comparación: MLP vs árboles

| Aspecto | MLP | Decisión Tree | Random Forest |
|---------|-----|---------------|---------------|
| Necesita muchos datos | Sí | No | No |
| Interpreta features | Difícil | Sí | Parcialmente |
| Tiempo de entrenamiento | Medio-alto | Rápido | Medio |
| Overfitting | Controlable | Fácil de controlar | Robusto |
| Datos tabulares | Bueno | Muy bueno | Excelente |
| Imágenes/texto | Excelente | Malo | Malo |

---

## 8. Keras y TensorFlow — el próximo nivel

`scikit-learn` es excelente para comenzar, pero tiene limitaciones. Para proyectos reales de deep learning se usan:

### TensorFlow / Keras

Keras es la API de alto nivel de TensorFlow (de Google). Permite construir redes más complejas con pocas líneas de código.

```python
# Ejemplo conceptual — no necesita ejecutarse hoy
from tensorflow import keras

modelo = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(n_features,)),
    keras.layers.Dropout(0.2),          # regularización
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
modelo.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)
```

### PyTorch

Desarrollado por Meta, es la opción más popular en investigación. Ofrece más control y flexibilidad que Keras.

El bootcamp se enfoca en el concepto y en scikit-learn. Keras/TensorFlow se verán en una extensión avanzada.

---

## Resumen

Una red neuronal es una función matemática paramétrica que transforma los datos de entrada en una predicción, pasándolos por capas de neuronas artificiales. Durante el entrenamiento, los pesos se ajustan iterativamente para minimizar el error entre la predicción y el valor real. Para datos tabulares pequeños-medianos, los modelos basados en árboles suelen ser igual o más efectivos con menos complejidad.
