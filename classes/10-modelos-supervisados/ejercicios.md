# 🧪 Ejercicios â€” Clase 10: Modelos Supervisados â€” ClasificaciÃ³n

## Ejercicio 1 â€” Preparar datos para clasificaciÃ³n (fÃ¡cil)

Con `datasets/retencion_clientes.csv`:

1. Carga el dataset e inspecciona las primeras filas.
2. Identifica la columna target (churn/retenciÃ³n).
3. Convierte la columna target a 0/1 si no lo estÃ¡.
4. Â¿CuÃ¡ntos clientes se fueron vs. se quedaron? Â¿EstÃ¡ balanceado el dataset?

---

## Ejercicio 2 â€” Ãrbol de decisiÃ³n (guiado)

```python
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Prepara X e y
X = df[["antiguedad_meses", "n_productos", "reclamos_ultimo_aÃ±o"]]
y = df["churned"]  # 1 = se fue, 0 = se quedÃ³

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred, target_names=["Se quedÃ³", "Se fue"]))
```

Â¿QuÃ© dice el reporte? Â¿El modelo es bueno para detectar clientes que se van?

---

## Ejercicio 3 â€” Matriz de confusiÃ³n (guiado)

```python
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

ConfusionMatrixDisplay.from_estimator(model, X_test, y_test,
    display_labels=["Se quedÃ³", "Se fue"], cmap="Blues")
plt.title("Matriz de ConfusiÃ³n")
plt.show()
```

Identifica: Â¿cuÃ¡ntos clientes que se fueron NO fueron detectados (falsos negativos)?

---

## Ejercicio 4 â€” Comparar dos modelos (medio)

Entrena tambiÃ©n una `LogisticRegression` y compara el F1-score de ambos modelos.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

lr = LogisticRegression(max_iter=200)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

print(f"F1 Ãrbol:              {f1_score(y_test, y_pred):.3f}")
print(f"F1 RegresiÃ³n LogÃ­st.: {f1_score(y_test, y_pred_lr):.3f}")
```

---

## DesafÃ­o opcional

Visualiza el Ã¡rbol de decisiÃ³n con `plot_tree` y explica en palabras quÃ© regla de decisiÃ³n aprendiÃ³ el modelo. Â¿Tiene sentido para el negocio?
