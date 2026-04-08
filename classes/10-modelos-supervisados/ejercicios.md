# Ejercicios — Clase 10: Modelos Supervisados — Clasificación

## Ejercicio 1 — Preparar datos para clasificación (fácil)

Con `datasets/retencion_clientes.csv`:

1. Carga el dataset e inspecciona las primeras filas.
2. Identifica la columna target (churn/retención).
3. Convierte la columna target a 0/1 si no lo está.
4. ¿Cuántos clientes se fueron vs. se quedaron? ¿Está balanceado el dataset?

---

## Ejercicio 2 — Árbol de decisión (guiado)

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Prepara X e y
X = df[["antiguedad_meses", "n_productos", "reclamos_ultimo_año"]]
y = df["churned"]  # 1 = se fue, 0 = se quedó

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred, target_names=["Se quedó", "Se fue"]))
```

¿Qué dice el reporte? ¿El modelo es bueno para detectar clientes que se van?

---

## Ejercicio 3 — Matriz de confusión (guiado)

```python
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

ConfusionMatrixDisplay.from_estimator(model, X_test, y_test,
    display_labels=["Se quedó", "Se fue"], cmap="Blues")
plt.title("Matriz de Confusión")
plt.show()
```

Identifica: ¿cuántos clientes que se fueron NO fueron detectados (falsos negativos)?

---

## Ejercicio 4 — Comparar dos modelos (medio)

Entrena también una `LogisticRegression` y compara el F1-score de ambos modelos.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print(f"F1 Árbol:              {f1_score(y_test, y_pred):.3f}")
print(f"F1 Regresión Logíst.: {f1_score(y_test, y_pred_lr):.3f}")
```

---

## Desafío opcional

Visualiza el árbol de decisión con `plot_tree` y explica en palabras qué regla de decisión aprendió el modelo. ¿Tiene sentido para el negocio?
