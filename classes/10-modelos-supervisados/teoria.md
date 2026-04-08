# 🧠 Documento TeÃ³rico â€” Clase 10: Modelos Supervisados â€” ClasificaciÃ³n

> **Nivel:** Intermedio Â· **DuraciÃ³n estimada de lectura:** 25â€“30 minutos

---

## 1. ClasificaciÃ³n vs. RegresiÃ³n

| Aspecto | RegresiÃ³n | ClasificaciÃ³n |
|---|---|---|
| Output | NÃºmero continuo | CategorÃ­a / clase |
| Ejemplo | Predecir ventas: $45.200 | Â¿Cliente se va? SÃ­ / No |
| MÃ©trica principal | MAE, RMSE, RÂ² | Accuracy, F1, AUC |
| Algoritmos comunes | RegresiÃ³n Lineal, SVR | Ãrbol, LR LogÃ­stica, SVM |

---

## 2. Ãrbol de DecisiÃ³n

### 2.1 Â¿CÃ³mo funciona?

Divide el espacio de los datos en regiones usando preguntas binarias (nodos). Cada camino desde la raÃ­z hasta una hoja es una regla de decisiÃ³n.

```
Â¿AntigÃ¼edad > 24 meses?
        â”‚
    SÃ­â”€â”€â”¤         Noâ”€â”€â”
        â†“              â†“
Â¿Reclamos > 2?    Â¿Productos > 1?
   SÃ­ â†’ CHURN       No â†’ CHURN
   No â†’ RETIENE     SÃ­ â†’ RETIENE
```

### 2.2 HiperparÃ¡metros clave

| HiperparÃ¡metro | QuÃ© controla | Valor tÃ­pico |
|---|---|---|
| `max_depth` | Profundidad mÃ¡xima del Ã¡rbol | 3â€“7 |
| `min_samples_split` | MÃ­nimo de ejemplos para dividir | 5â€“20 |
| `min_samples_leaf` | MÃ­nimo de ejemplos en hoja | 2â€“10 |
| `criterion` | FunciÃ³n de impureza | "gini" o "entropy" |

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

| âœ… Ventajas | âŒ Desventajas |
|---|---|
| Muy interpretable | Propenso a overfitting |
| Sin necesidad de escalar | Inestable con pequeÃ±os cambios en datos |
| Maneja categorÃ­as y numÃ©ricos | Baja precisiÃ³n en datasets complejos |
| Identifica features importantes | Sesgado hacia features con muchos valores |

---

## 3. RegresiÃ³n LogÃ­stica

### 3.1 Â¿CÃ³mo funciona?

A pesar del nombre, es un **clasificador**. Estima la probabilidad de que una instancia pertenezca a la clase positiva usando la funciÃ³n sigmoide:

```
P(y=1|X) = 1 / (1 + e^(âˆ’(Î²â‚€ + Î²â‚Â·xâ‚ + ... + Î²â‚™Â·xâ‚™)))
```

La salida estÃ¡ siempre entre 0 y 1. Si P > 0.5 â†’ clase 1; si P â‰¤ 0.5 â†’ clase 0.

### 3.2 Umbral de decisiÃ³n

```python
# Probabilidades en lugar de clases directas
proba = model.predict_proba(X_test)[:, 1]  # prob de clase 1

# Cambiar el umbral (por defecto 0.5)
threshold = 0.3  # mÃ¡s sensible (detecta mÃ¡s positivos)
y_pred_custom = (proba >= threshold).astype(int)
```

Bajar el umbral â†’ mÃ¡s recall, menos precisiÃ³n.
Subir el umbral â†’ mÃ¡s precisiÃ³n, menos recall.

---

## 4. La Matriz de ConfusiÃ³n

### 4.1 Estructura

|  | **Predicho: Negativo (0)** | **Predicho: Positivo (1)** |
|---|---|---|
| **Real: Negativo (0)** | TN â€” Verdadero Negativo | FP â€” Falso Positivo (Error tipo I) |
| **Real: Positivo (1)** | FN â€” Falso Negativo (Error tipo II) | TP â€” Verdadero Positivo |

### 4.2 Â¿CuÃ¡ndo importa cada error?

| Contexto | Error mÃ¡s costoso | MÃ©trica a priorizar |
|---|---|---|
| DetecciÃ³n de cÃ¡ncer | FN (no detectar enfermo) | Recall |
| Filtro de spam | FP (bloquear email legÃ­timo) | PrecisiÃ³n |
| RetenciÃ³n de clientes | FN (no detectar cliente que se va) | Recall |
| Fraude bancario | FP + FN (ambos costosos) | F1 o AUC |

### 4.3 CÃ³digo

```python
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
import matplotlib.pyplot as plt

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(cm, display_labels=["Se quedÃ³", "Se fue"])
disp.plot(cmap="Blues")
plt.title("Matriz de ConfusiÃ³n â€” Modelo de Churn")
plt.show()
```

---

## 5. MÃ©tricas de clasificaciÃ³n

### 5.1 FÃ³rmulas

| MÃ©trica | FÃ³rmula | Rango |
|---|---|---|
| **Accuracy** | (TP + TN) / Total | 0â€“1 |
| **PrecisiÃ³n** | TP / (TP + FP) | 0â€“1 |
| **Recall (Sensibilidad)** | TP / (TP + FN) | 0â€“1 |
| **F1-Score** | 2 Â· (Prec Â· Recall) / (Prec + Recall) | 0â€“1 |
| **Especificidad** | TN / (TN + FP) | 0â€“1 |

### 5.2 El problema de la accuracy con clases desbalanceadas

Si el 95% de los clientes **no** hace churn:

- Un modelo que siempre predice "No hace churn" â†’ **Accuracy = 95%**
- Pero **Recall = 0%** (nunca detecta a quienes se van)

Siempre revisar el balance de clases antes de elegir la mÃ©trica.

```python
print(y_train.value_counts(normalize=True))
```

### 5.3 Classification Report completo

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred,
    target_names=["Se quedÃ³", "Se fue"],
    digits=3))
```

---

## 6. Importancia de variables

### 6.1 Ãrbol de DecisiÃ³n

```python
import pandas as pd
import matplotlib.pyplot as plt

importances = pd.Series(
    model.feature_importances_,
    index=feature_names
).sort_values(ascending=True)

importances.plot(kind="barh", color="#22c55e", figsize=(8, 5))
plt.title("Importancia de variables â€” Ãrbol de DecisiÃ³n")
plt.xlabel("Importancia (Gini)")
plt.tight_layout()
plt.show()
```

### 6.2 RegresiÃ³n LogÃ­stica

```python
coef = pd.Series(
    model.coef_[0],
    index=feature_names
).sort_values()

colors = ["#ef4444" if c < 0 else "#22c55e" for c in coef]
coef.plot(kind="barh", color=colors, figsize=(8, 5))
plt.title("Coeficientes â€” RegresiÃ³n LogÃ­stica")
plt.axvline(0, color="white", lw=0.5)
plt.tight_layout()
plt.show()
```

---

## 7. ComparaciÃ³n de algoritmos

### 7.1 Tabla comparativa general

| Criterio | Ãrbol DecisiÃ³n | Reg. LogÃ­stica | Random Forest | SVM |
|---|---|---|---|---|
| Interpretabilidad | âœ… Alta | âœ… Alta | âŒ Baja | âŒ Baja |
| Velocidad entrenamiento | âœ… RÃ¡pido | âœ… RÃ¡pido | âš ï¸ Medio | âŒ Lento |
| Requiere escalar features | âŒ No | âœ… SÃ­ | âŒ No | âœ… SÃ­ |
| Maneja no-linealidad | âš ï¸ Parcial | âŒ No | âœ… SÃ­ | âœ… SÃ­ |
| Overfitting | âŒ Alto riesgo | âœ… Bajo riesgo | âœ… Bajo (ensemble) | âœ… Bajo |

---

## 8. Errores frecuentes en clasificaciÃ³n

| Error | DescripciÃ³n | SoluciÃ³n |
|---|---|---|
| **Evaluar solo con accuracy** | EngaÃ±oso con clases desbalanceadas | Usar F1, AUC, o confusion matrix |
| **No verificar balance de clases** | El modelo aprende la clase mayoritaria | Analizar `value_counts()` |
| **Ignorar el umbral** | 0.5 no siempre es el mejor umbral | Ajustar segÃºn el costo del error |
| **No comparar modelos** | Un solo modelo no tiene referencia | Comparar con baseline y al menos otro modelo |
| **Olvidar el contexto de negocio** | F1 alto no significa modelo Ãºtil | Traducir mÃ©tricas a impacto real |

---

## 9. Resumen rÃ¡pido

```
âœ… ClasificaciÃ³n = predecir categorÃ­as (binario o multiclase)
âœ… Ãrbol de decisiÃ³n = interpretable, riesgo de overfitting
âœ… RegresiÃ³n logÃ­stica = estima probabilidades, requiere escalar
âœ… Matriz de confusiÃ³n = base de todas las mÃ©tricas
âœ… F1 = balance entre precisiÃ³n y recall
âœ… Ajustar umbral segÃºn el costo del error en el negocio
```
