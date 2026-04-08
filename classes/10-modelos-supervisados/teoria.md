# Documento Teórico — Clase 10: Modelos Supervisados — Clasificación

> **Nivel:** Intermedio · **Duración estimada de lectura:** 25–30 minutos

---

## 1. Clasificación vs. Regresión

| Aspecto | Regresión | Clasificación |
|---|---|---|
| Output | Número continuo | Categoría / clase |
| Ejemplo | Predecir ventas: $45.200 | ¿Cliente se va? Sí / No |
| Métrica principal | MAE, RMSE, R² | Accuracy, F1, AUC |
| Algoritmos comunes | Regresión Lineal, SVR | Árbol, LR Logística, SVM |

---

## 2. Árbol de Decisión

### 2.1 ¿Cómo funciona?

Divide el espacio de los datos en regiones usando preguntas binarias (nodos). Cada camino desde la raíz hasta una hoja es una regla de decisión.

```
¿Antigüedad > 24 meses?
        │
    Sí──┤         No──┐
        ↓              ↓
¿Reclamos > 2?    ¿Productos > 1?
   Sí → CHURN       No → CHURN
   No → RETIENE     Sí → RETIENE
```

### 2.2 Hiperparámetros clave

| Hiperparámetro | Qué controla | Valor típico |
|---|---|---|
| `max_depth` | Profundidad máxima del árbol | 3–7 |
| `min_samples_split` | Mínimo de ejemplos para dividir | 5–20 |
| `min_samples_leaf` | Mínimo de ejemplos en hoja | 2–10 |
| `criterion` | Función de impureza | "gini" o "entropy" |

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    max_depth=4,
    min_samples_leaf=5,
    random_state=42
)
model.fit(X_train, y_train)
```

### 2.3 Ventajas y desventajas

| ✅ Ventajas | ❌ Desventajas |
|---|---|
| Muy interpretable | Propenso a overfitting |
| Sin necesidad de escalar | Inestable con pequeños cambios en datos |
| Maneja categorías y numéricos | Baja precisión en datasets complejos |
| Identifica features importantes | Sesgado hacia features con muchos valores |

---

## 3. Regresión Logística

### 3.1 ¿Cómo funciona?

A pesar del nombre, es un **clasificador**. Estima la probabilidad de que una instancia pertenezca a la clase positiva usando la función sigmoide:

```
P(y=1|X) = 1 / (1 + e^(−(β₀ + β₁·x₁ + ... + βₙ·xₙ)))
```

La salida está siempre entre 0 y 1. Si P > 0.5 → clase 1; si P ≤ 0.5 → clase 0.

### 3.2 Umbral de decisión

```python
# Probabilidades en lugar de clases directas
proba = model.predict_proba(X_test)[:, 1]  # prob de clase 1

# Cambiar el umbral (por defecto 0.5)
threshold = 0.3  # más sensible (detecta más positivos)
y_pred_custom = (proba >= threshold).astype(int)
```

Bajar el umbral → más recall, menos precisión.
Subir el umbral → más precisión, menos recall.

---

## 4. La Matriz de Confusión

### 4.1 Estructura

|  | **Predicho: Negativo (0)** | **Predicho: Positivo (1)** |
|---|---|---|
| **Real: Negativo (0)** | TN — Verdadero Negativo | FP — Falso Positivo (Error tipo I) |
| **Real: Positivo (1)** | FN — Falso Negativo (Error tipo II) | TP — Verdadero Positivo |

### 4.2 ¿Cuándo importa cada error?

| Contexto | Error más costoso | Métrica a priorizar |
|---|---|---|
| Detección de cáncer | FN (no detectar enfermo) | Recall |
| Filtro de spam | FP (bloquear email legítimo) | Precisión |
| Retención de clientes | FN (no detectar cliente que se va) | Recall |
| Fraude bancario | FP + FN (ambos costosos) | F1 o AUC |

### 4.3 Código

```python
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=["Se quedó", "Se fue"])
disp.plot(cmap="Blues")
plt.title("Matriz de Confusión — Modelo de Churn")
plt.show()
```

---

## 5. Métricas de clasificación

### 5.1 Fórmulas

| Métrica | Fórmula | Rango |
|---|---|---|
| **Accuracy** | (TP + TN) / Total | 0–1 |
| **Precisión** | TP / (TP + FP) | 0–1 |
| **Recall (Sensibilidad)** | TP / (TP + FN) | 0–1 |
| **F1-Score** | 2 · (Prec · Recall) / (Prec + Recall) | 0–1 |
| **Especificidad** | TN / (TN + FP) | 0–1 |

### 5.2 El problema de la accuracy con clases desbalanceadas

Si el 95% de los clientes **no** hace churn:

- Un modelo que siempre predice "No hace churn" → **Accuracy = 95%**
- Pero **Recall = 0%** (nunca detecta a quienes se van)

Siempre revisar el balance de clases antes de elegir la métrica.

```python
print(y_train.value_counts(normalize=True))
```

### 5.3 Classification Report completo

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred,
    target_names=["Se quedó", "Se fue"],
    digits=3))
```

---

## 6. Importancia de variables

### 6.1 Árbol de Decisión

```python
import pandas as pd
import matplotlib.pyplot as plt

importances = pd.Series(
    model.feature_importances_,
    index=feature_names
).sort_values(ascending=True)

importances.plot(kind="barh", color="#22c55e", figsize=(8, 5))
plt.title("Importancia de variables — Árbol de Decisión")
plt.xlabel("Importancia (Gini)")
plt.tight_layout()
plt.show()
```

### 6.2 Regresión Logística

```python
coef = pd.Series(
    model.coef_[0],
    index=feature_names
).sort_values()

colors = ["#ef4444" if c < 0 else "#22c55e" for c in coef]
coef.plot(kind="barh", color=colors, figsize=(8, 5))
plt.title("Coeficientes — Regresión Logística")
plt.axvline(0, color="white", lw=0.5)
plt.tight_layout()
plt.show()
```

---

## 7. Comparación de algoritmos

### 7.1 Tabla comparativa general

| Criterio | Árbol Decisión | Reg. Logística | Random Forest | SVM |
|---|---|---|---|---|
| Interpretabilidad | ✅ Alta | ✅ Alta | ❌ Baja | ❌ Baja |
| Velocidad entrenamiento | ✅ Rápido | ✅ Rápido | ⚠️ Medio | ❌ Lento |
| Requiere escalar features | ❌ No | ✅ Sí | ❌ No | ✅ Sí |
| Maneja no-linealidad | ⚠️ Parcial | ❌ No | ✅ Sí | ✅ Sí |
| Overfitting | ❌ Alto riesgo | ✅ Bajo riesgo | ✅ Bajo (ensemble) | ✅ Bajo |

---

## 8. Errores frecuentes en clasificación

| Error | Descripción | Solución |
|---|---|---|
| **Evaluar solo con accuracy** | Engañoso con clases desbalanceadas | Usar F1, AUC, o confusion matrix |
| **No verificar balance de clases** | El modelo aprende la clase mayoritaria | Analizar `value_counts()` |
| **Ignorar el umbral** | 0.5 no siempre es el mejor umbral | Ajustar según el costo del error |
| **No comparar modelos** | Un solo modelo no tiene referencia | Comparar con baseline y al menos otro modelo |
| **Olvidar el contexto de negocio** | F1 alto no significa modelo útil | Traducir métricas a impacto real |

---

## 9. Resumen rápido

```
✅ Clasificación = predecir categorías (binario o multiclase)
✅ Árbol de decisión = interpretable, riesgo de overfitting
✅ Regresión logística = estima probabilidades, requiere escalar
✅ Matriz de confusión = base de todas las métricas
✅ F1 = balance entre precisión y recall
✅ Ajustar umbral según el costo del error en el negocio
```
