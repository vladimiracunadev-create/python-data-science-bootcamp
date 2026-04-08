# Slides — Clase 10: Modelos Supervisados — Clasificación

## Bloque 1 (20 min) — ¿Regresión o Clasificación?

| Problema | Tipo | Ejemplo |
|---|---|---|
| Predecir precio | Regresión | $150.000 |
| Predecir si compra | Clasificación | Sí / No |
| Predecir categoría | Clasificación multiclase | A / B / C |

**Hoy:** clasificación binaria. ¿Este cliente se va o se queda?

---

## Bloque 2 (30 min) — Árbol de Decisión

```
¿Tiene más de 2 años como cliente?
    ├── Sí → ¿Ha tenido reclamos este año?
    │        ├── Sí → 🔴 RIESGO DE CHURN
    │        └── No → 🟢 RETIENE
    └── No → ¿Usa más de 1 producto?
             ├── Sí → 🟢 RETIENE
             └── No → 🔴 RIESGO DE CHURN
```

**Práctica:**
```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
```

---

## Bloque 3 (25 min) — Evaluación de clasificadores

**La matriz de confusión:**

|  | Predicho: No | Predicho: Sí |
|---|---|---|
| **Real: No** | TN (correcto) | FP (falsa alarma) |
| **Real: Sí** | FN (perdido) | TP (correcto) |

**¿Cuándo usar cada métrica?**

- **Accuracy:** cuando las clases están balanceadas.
- **Recall:** cuando el costo de un FN es alto (ej: cancer, fraude).
- **Precisión:** cuando el costo de un FP es alto (ej: spam bloqueado).
- **F1:** balance entre precisión y recall.

---

## Cierre (15 min)

Comparar árbol de decisión vs. regresión logística en el mismo dataset. ¿Cuál tiene mejor F1? ¿Cuál es más interpretable?
