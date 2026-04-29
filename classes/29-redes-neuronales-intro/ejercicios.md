# 🏋️ Ejercicios — Clase 29: Introducción a redes neuronales

---

## Ejercicio 1: Cálculo manual de una neurona

Calcula manualmente la salida de esta neurona:

**Datos:**
- Entradas: x1 = 2.0, x2 = -1.0, x3 = 0.5
- Pesos: w1 = 0.3, w2 = 0.8, w3 = -0.5
- Bias: b = 0.1

**Pasos:**
1. Calcula z = x1·w1 + x2·w2 + x3·w3 + b
2. Aplica sigmoid: f(z) = 1 / (1 + e^(-z))
3. Aplica ReLU: f(z) = max(0, z)

```python
import numpy as np

x = np.array([2.0, -1.0, 0.5])
w = np.array([0.3, 0.8, -0.5])
b = 0.1

# Tu código aquí
z = np.dot(x, w) + b
print(f'z = {z}')

# Sigmoid
sigmoid = 1 / (1 + np.exp(-z))
print(f'Sigmoid(z) = {sigmoid:.4f}')

# ReLU
relu = max(0, z)
print(f'ReLU(z) = {relu:.4f}')
```

**Pregunta:** Si aumentas w1 a 1.0, ¿cómo cambia la salida? ¿Qué nos dice esto sobre el papel de los pesos?

---

## Ejercicio 2: Visualizar funciones de activación

```python
import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(-5, 5, 200)

# Sigmoid
sigmoid = 1 / (1 + np.exp(-z))

# ReLU
relu = np.maximum(0, z)

# Tanh
tanh = np.tanh(z)

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(z, sigmoid, color='blue', linewidth=2)
axes[0].set_title('Sigmoid')
axes[0].set_xlabel('z')
axes[0].axhline(y=0.5, color='gray', linestyle='--', alpha=0.5)
axes[0].grid(True)

axes[1].plot(z, relu, color='green', linewidth=2)
axes[1].set_title('ReLU')
axes[1].set_xlabel('z')
axes[1].grid(True)

axes[2].plot(z, tanh, color='red', linewidth=2)
axes[2].set_title('Tanh')
axes[2].set_xlabel('z')
axes[2].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
axes[2].grid(True)

plt.suptitle('Funciones de activación', fontsize=14)
plt.tight_layout()
plt.show()
```

**Preguntas:**
1. ¿Cuál función "apaga" completamente neuronas cuando z < 0?
2. ¿Cuál función siempre da salidas entre -1 y 1?
3. ¿Por qué ReLU podría ser más eficiente computacionalmente?

---

## Ejercicio 3: Tu primer MLPClassifier

```python
import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report

np.random.seed(42)
n = 400
cursos = np.random.choice(['A', 'B', 'C'], size=n, p=[0.4, 0.4, 0.2])
nota_mate = np.where(cursos == 'A', np.random.normal(7.5, 1.2, n),
                     np.where(cursos == 'B', np.random.normal(7.0, 1.3, n),
                              np.random.normal(5.8, 1.5, n))).clip(1, 10)
nota_lengua = np.where(cursos == 'A', np.random.normal(7.2, 1.1, n),
                       np.where(cursos == 'B', np.random.normal(6.8, 1.2, n),
                                np.random.normal(5.5, 1.4, n))).clip(1, 10)
asistencia = np.where(cursos == 'C', np.random.uniform(0.55, 0.85, n),
                      np.random.uniform(0.70, 0.99, n))
prob = (nota_mate * 0.4 + nota_lengua * 0.4 + asistencia * 10 * 0.2) / 10
aprobado = (np.random.uniform(0, 1, n) < prob).astype(int)
edades = np.random.randint(18, 35, size=n)

df = pd.DataFrame({
    'nota_matematicas': nota_mate.round(1),
    'nota_lengua': nota_lengua.round(1),
    'asistencia': asistencia.round(2),
    'edad': edades,
    'aprobado': aprobado
})

features = ['nota_matematicas', 'nota_lengua', 'asistencia', 'edad']
X = df[features]
y = df['aprobado']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# IMPORTANTE: Las redes neuronales requieren normalización de datos
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Entrena un MLPClassifier
# a) Con una capa oculta de 50 neuronas
mlp_simple = MLPClassifier(
    hidden_layer_sizes=(50,),
    activation='relu',
    max_iter=300,
    random_state=42
)
mlp_simple.fit(X_train_scaled, y_train)
pred_simple = mlp_simple.predict(X_test_scaled)

print('=== MLP Simple (50,) ===')
print(f'Precisión: {accuracy_score(y_test, pred_simple):.2%}')
print()
print(classification_report(y_test, pred_simple, target_names=['Reprobado', 'Aprobado']))
```

---

## Ejercicio 4: Comparar arquitecturas

Entrena 3 versiones del MLP con distintas arquitecturas y compara:

```python
arquitecturas = {
    'MLP pequeño (50,)': (50,),
    'MLP mediano (100, 50)': (100, 50),
    'MLP grande (200, 100, 50)': (200, 100, 50)
}

print('=== Comparación de arquitecturas ===')
for nombre, capas in arquitecturas.items():
    mlp = MLPClassifier(
        hidden_layer_sizes=capas,
        activation='relu',
        max_iter=500,
        random_state=42
    )
    mlp.fit(X_train_scaled, y_train)
    acc = accuracy_score(y_test, mlp.predict(X_test_scaled))
    print(f'{nombre}: {acc:.2%}')
```

**Pregunta:** ¿Más capas siempre significa mejor rendimiento? ¿Por qué sí o por qué no?

---

## Ejercicio 5: MLP vs Decision Tree vs Random Forest

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

resultados = {}

# MLP
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=300, random_state=42)
mlp.fit(X_train_scaled, y_train)
resultados['MLP (100, 50)'] = accuracy_score(y_test, mlp.predict(X_test_scaled))

# Decision Tree (no necesita escalado)
tree = DecisionTreeClassifier(max_depth=5, random_state=42)
tree.fit(X_train, y_train)
resultados['Decision Tree'] = accuracy_score(y_test, tree.predict(X_test))

# Random Forest (no necesita escalado)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
resultados['Random Forest'] = accuracy_score(y_test, rf.predict(X_test))

print('=== Comparación de modelos ===')
for modelo, acc in sorted(resultados.items(), key=lambda x: x[1], reverse=True):
    print(f'{modelo}: {acc:.2%}')

print()
print('REFLEXIÓN: ¿En datos tabulares simples, qué modelo gana usualmente?')
print('¿Significa eso que las redes neuronales son inútiles? ¿En qué casos brillan?')
```

---

## Ejercicio 6: La importancia de normalizar

Demuestra qué pasa si no normalizas los datos antes de usar MLP:

```python
# Sin normalización
mlp_sin_escalar = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42)
mlp_sin_escalar.fit(X_train, y_train)
acc_sin = accuracy_score(y_test, mlp_sin_escalar.predict(X_test))

# Con normalización
mlp_con_escalar = MLPClassifier(hidden_layer_sizes=(100,), max_iter=300, random_state=42)
mlp_con_escalar.fit(X_train_scaled, y_train)
acc_con = accuracy_score(y_test, mlp_con_escalar.predict(X_test_scaled))

print(f'MLP sin normalización: {acc_sin:.2%}')
print(f'MLP con normalización: {acc_con:.2%}')
print()
print('¿Por qué la normalización es tan importante para redes neuronales?')
print('Pista: piensa en los pesos y en cómo las variables con escalas distintas')
print('afectan el cálculo de z = Σ(xi × wi) + b')
```

---

## Ejercicio 7: Visualizar la curva de pérdida

```python
mlp_final = MLPClassifier(
    hidden_layer_sizes=(100, 50),
    activation='relu',
    max_iter=300,
    random_state=42
)
mlp_final.fit(X_train_scaled, y_train)

# La curva de pérdida muestra cómo fue aprendiendo el modelo
plt.figure(figsize=(8, 4))
plt.plot(mlp_final.loss_curve_, color='#4C72B0', linewidth=2)
plt.title('Curva de aprendizaje del MLP\n(cómo disminuye el error durante el entrenamiento)')
plt.xlabel('Iteración (epoch)')
plt.ylabel('Pérdida (loss)')
plt.grid(True)
plt.tight_layout()
plt.show()

print(f'Pérdida inicial: {mlp_final.loss_curve_[0]:.4f}')
print(f'Pérdida final: {mlp_final.loss_curve_[-1]:.4f}')
print(f'Epochs completados: {len(mlp_final.loss_curve_)}')
```

**Preguntas:**
1. ¿Cómo cambia la pérdida a lo largo del entrenamiento?
2. ¿En qué momento el modelo "aprende más rápido"?
3. ¿Qué indicaría una pérdida que no baja en absoluto?
