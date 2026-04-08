# 🖥 Slides â€” Clase 10: Modelos Supervisados â€” ClasificaciÃ³n

> 🖥 Guion visual breve para conducir la sesion sin sobrecargar la clase.


## 🧱 Bloque 1 (20 min) â€” Â¿RegresiÃ³n o ClasificaciÃ³n?

| Problema | Tipo | Ejemplo |
|---|---|---|
| Predecir precio | RegresiÃ³n | $150.000 |
| Predecir si compra | ClasificaciÃ³n | SÃ­ / No |
| Predecir categorÃ­a | ClasificaciÃ³n multiclase | A / B / C |

**Hoy:** clasificaciÃ³n binaria. Â¿Este cliente se va o se queda?

---

## 🧱 Bloque 2 (30 min) â€” Ãrbol de DecisiÃ³n

```
Â¿Tiene mÃ¡s de 2 aÃ±os como cliente?
    â”œâ”€â”€ SÃ­ â†’ Â¿Ha tenido reclamos este aÃ±o?
    â”‚        â”œâ”€â”€ SÃ­ â†’ ðŸ”´ RIESGO DE CHURN
    â”‚        â””â”€â”€ No â†’ ðŸŸ¢ RETIENE
    â””â”€â”€ No â†’ Â¿Usa mÃ¡s de 1 producto?
             â”œâ”€â”€ SÃ­ â†’ ðŸŸ¢ RETIENE
             â””â”€â”€ No â†’ ðŸ”´ RIESGO DE CHURN
```

**PrÃ¡ctica:**
```python
from sklearn.tree import DecisionTreeClassifier, plot_tree
model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
```

---

## 🧱 Bloque 3 (25 min) â€” EvaluaciÃ³n de clasificadores

**La matriz de confusiÃ³n:**

|  | Predicho: No | Predicho: SÃ­ |
|---|---|---|
| **Real: No** | TN (correcto) | FP (falsa alarma) |
| **Real: SÃ­** | FN (perdido) | TP (correcto) |

**Â¿CuÃ¡ndo usar cada mÃ©trica?**

- **Accuracy:** cuando las clases estÃ¡n balanceadas.
- **Recall:** cuando el costo de un FN es alto (ej: cancer, fraude).
- **PrecisiÃ³n:** cuando el costo de un FP es alto (ej: spam bloqueado).
- **F1:** balance entre precisiÃ³n y recall.

---

## ✅ Cierre (15 min)

Comparar Ã¡rbol de decisiÃ³n vs. regresiÃ³n logÃ­stica en el mismo dataset. Â¿CuÃ¡l tiene mejor F1? Â¿CuÃ¡l es mÃ¡s interpretable?
