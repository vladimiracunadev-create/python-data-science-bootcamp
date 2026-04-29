# 💻 Guía de código — Clase 29: Introducción a Redes Neuronales

> Explicación detallada del código clave, bloque por bloque.

## Bloque 1: Preparar datos y escalar (obligatorio para redes neuronales)

```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report, accuracy_score

# Cargar datos
df = pd.read_csv("estudiantes.csv")

# Separar features y target
X = df.drop(columns=["aprobado"])
y = df["aprobado"]

# Dividir en train y test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# PASO OBLIGATORIO: Escalar los datos
# fit_transform en train: aprende la media y desviación estándar del train
# transform en test: aplica la misma escala (no aprende de test)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"Datos de entrenamiento: {X_train_scaled.shape}")
print(f"Media de una columna antes de escalar: {X_train['horas_estudio'].mean():.2f}")
print(f"Media de esa columna después de escalar: {X_train_scaled[:, 0].mean():.4f}")
print(f"Desviación estándar después de escalar: {X_train_scaled[:, 0].std():.4f}")
```

**¿Qué hace este bloque?** Prepara los datos aplicando `StandardScaler` que transforma cada variable para tener media 0 y desviación estándar 1. Esta transformación es indispensable para redes neuronales.

**¿Por qué se escribe así?** Las redes neuronales son muy sensibles a la escala de los datos. Si una variable tiene rango [0, 100] y otra [0, 0.001], los gradientes durante el entrenamiento serán muy desiguales y la red aprenderá muy lentamente o no convergerá. Con `StandardScaler`, todas las variables contribuyen por igual al inicio. Aplicar `.fit_transform()` solo en train y `.transform()` en test es fundamental para evitar data leakage.

**Resultado esperado:** La columna escalada tendrá media aproximadamente 0 y desviación estándar aproximadamente 1. Esto confirma que el escalado funcionó correctamente.

---

## Bloque 2: Entrenar MLPClassifier y evaluar

```python
# Crear la red neuronal
# hidden_layer_sizes=(100, 50) = dos capas ocultas: 100 neuronas y luego 50
mlp = MLPClassifier(
    hidden_layer_sizes=(100, 50),    # arquitectura de la red
    activation="relu",               # función de activación en capas ocultas
    solver="adam",                   # algoritmo de optimización
    max_iter=500,                    # máximo de épocas de entrenamiento
    random_state=42,
    verbose=False                    # True para ver el progreso de pérdida
)

# Entrenar (solo con datos de entrenamiento escalados)
mlp.fit(X_train_scaled, y_train)

print(f"Convergió: {mlp.n_iter_ < mlp.max_iter}")
print(f"Épocas entrenadas: {mlp.n_iter_}")
print(f"Pérdida final: {mlp.loss_:.4f}")

# Evaluar en test
y_pred = mlp.predict(X_test_scaled)
print(f"\nAccuracy en test: {accuracy_score(y_test, y_pred):.3f}")
print("\nReporte detallado:")
print(classification_report(y_test, y_pred))
```

**¿Qué hace este bloque?** Crea y entrena una red neuronal con dos capas ocultas (100 y 50 neuronas). El parámetro `activation="relu"` define la función de activación para las capas ocultas. Adam es el optimizador más popular en la práctica.

**¿Por qué se escribe así?** `hidden_layer_sizes=(100, 50)` significa: capa oculta 1 con 100 neuronas, capa oculta 2 con 50 neuronas. La capa de entrada y salida se determinan automáticamente por el número de features y de clases. Si `n_iter_ < max_iter`, la red convergió antes de agotar las iteraciones (buena señal). Si `n_iter_ == max_iter`, puede que necesite más iteraciones.

**Resultado esperado:** Un reporte de clasificación con precisión, recall y F1-score. Para un dataset de estudiantes de tamaño moderado, se espera accuracy entre 75% y 92% dependiendo de la calidad de los datos y la arquitectura.

---

## Bloque 3: Visualizar la curva de pérdida

```python
import matplotlib.pyplot as plt

# La curva de pérdida muestra cómo mejora el modelo durante el entrenamiento
plt.figure(figsize=(10, 5))
plt.plot(mlp.loss_curve_, color="steelblue", linewidth=2)
plt.title("Curva de pérdida durante el entrenamiento")
plt.xlabel("Época (iteración)")
plt.ylabel("Pérdida (Cross-Entropy Loss)")
plt.grid(True, alpha=0.3)

# Marcar el punto de menor pérdida
min_loss_iter = mlp.loss_curve_.index(min(mlp.loss_curve_))
plt.scatter(min_loss_iter, min(mlp.loss_curve_),
            color="red", s=100, zorder=5, label=f"Mínimo: época {min_loss_iter}")
plt.legend()
plt.tight_layout()
plt.savefig("curva_perdida_red_neuronal.png", dpi=150)
plt.show()

print(f"\nPérdida inicial: {mlp.loss_curve_[0]:.4f}")
print(f"Pérdida final: {mlp.loss_curve_[-1]:.4f}")
print(f"Reducción total: {(1 - mlp.loss_curve_[-1]/mlp.loss_curve_[0]) * 100:.1f}%")
```

**¿Qué hace este bloque?** Grafica la curva de pérdida almacenada en `loss_curve_`, que registra el valor de la función de pérdida al final de cada época de entrenamiento. Muestra cómo la red "aprende" progresivamente a hacer mejores predicciones.

**¿Por qué se escribe así?** La curva de pérdida es el diagnóstico más básico de una red neuronal. Una curva que decrece suavemente y se estabiliza indica un entrenamiento saludable. Una curva que oscila mucho puede indicar tasa de aprendizaje muy alta. Una curva que no baja puede indicar que los datos no están escalados, la red es muy pequeña, o hay un problema en los datos.

**Resultado esperado:** Una curva que desciende rápido al principio y luego se aplana. La pérdida final debe ser significativamente menor que la inicial (reducción del 50% o más es típico). Si la curva tiene muchos picos, agregar `early_stopping=True` al MLPClassifier puede ayudar.

---

## Bloque 4: Comparar MLP con modelos basados en árboles

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import time

# Diccionario de modelos a comparar
modelos = {
    "Árbol de Decisión": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Red Neuronal (MLP)": MLPClassifier(
        hidden_layer_sizes=(100, 50), max_iter=500, random_state=42
    )
}

resultados = []

for nombre, modelo in modelos.items():
    inicio = time.time()
    
    # Los árboles no necesitan escalar, la red sí
    if "Neuronal" in nombre:
        modelo.fit(X_train_scaled, y_train)
        y_pred = modelo.predict(X_test_scaled)
    else:
        modelo.fit(X_train, y_train)
        y_pred = modelo.predict(X_test)
    
    tiempo = time.time() - inicio
    accuracy = accuracy_score(y_test, y_pred)
    
    resultados.append({
        "Modelo": nombre,
        "Accuracy": f"{accuracy:.3f}",
        "Tiempo (seg)": f"{tiempo:.2f}"
    })
    print(f"{nombre}: accuracy={accuracy:.3f}, tiempo={tiempo:.2f}s")

# Resumen comparativo
df_resultados = pd.DataFrame(resultados)
print("\n=== Resumen de comparación ===")
print(df_resultados.to_string(index=False))
```

**¿Qué hace este bloque?** Compara tres tipos de modelos en el mismo dataset, midiendo tanto el rendimiento (accuracy) como el tiempo de entrenamiento. Permite tomar una decisión informada sobre qué modelo usar en producción.

**¿Por qué se escribe así?** La comparación es justa: todos los modelos usan el mismo train/test split. Los árboles reciben datos sin escalar (no lo necesitan) y la red neuronal recibe datos escalados. `time.time()` antes y después del entrenamiento mide el tiempo real de CPU. Esta comparación es el punto de partida para cualquier selección de modelo.

**Resultado esperado:** Una tabla con tres filas. Típicamente, el árbol de decisión entrena en menos de 1 segundo, el Random Forest en 1-5 segundos, y la red neuronal en 5-60 segundos dependiendo del dataset. En datasets pequeños, el Random Forest suele igualar o superar a la red neuronal sin necesitar escalado ni tantos hiperparámetros.

---

## Errores comunes y cómo resolverlos

| Error | Causa | Solución |
|---|---|---|
| `ConvergenceWarning: Stochastic Optimizer did not converge` | El modelo no convergió en `max_iter` iteraciones | Aumentar `max_iter` a 1000 o más, o aumentar `tol` |
| Accuracy muy baja o siempre predice la misma clase | Los datos NO fueron escalados antes de entrenar | Aplicar `StandardScaler` y verificar que `X_train_scaled` tiene media ~0 |
| La pérdida oscila mucho sin bajar | Tasa de aprendizaje demasiado alta | Agregar `learning_rate_init=0.0001` al MLPClassifier |
| `ValueError: Input contains NaN` | El dataset tiene valores faltantes | Usar `SimpleImputer` antes del escalado para rellenar NaN |
| `AttributeError: 'MLPClassifier' object has no attribute 'loss_curve_'` | El modelo no fue entrenado aún | Llamar `.fit()` antes de acceder a `loss_curve_` |
| La red tarda demasiado en entrenar | Dataset grande o arquitectura con demasiadas neuronas | Reducir `hidden_layer_sizes`, usar `batch_size` más pequeño, o cambiar a `solver='sgd'` |
