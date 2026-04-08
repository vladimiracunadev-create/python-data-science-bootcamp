# 🧪 Ejercicios â€” Clase 09: IntroducciÃ³n al Machine Learning

> 🧪 Practica guiada para trabajar en clase y consolidar el aprendizaje.


## 🧪 Ejercicio 1 â€” Identificar variables (fÃ¡cil)

Con el dataset `ventas_tienda.csv`:

1. Lista todas las columnas del dataset.
2. Â¿CuÃ¡l serÃ­a una buena variable objetivo (target) para predecir?
3. Â¿CuÃ¡les serÃ­an buenas variables predictoras (features)?
4. Â¿Hay alguna columna que NO deberÃ­as usar como feature? Â¿Por quÃ©?

---

## 🧪 Ejercicio 2 â€” Train/Test split (guiado)

```python
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
# Completa:
X = df[["unidades_vendidas", "precio_unitario"]]
y = df["___"]  # Â¿quÃ© predecimos?

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {len(X_train)} filas | Test: {len(X_test)} filas")
```

Â¿Por quÃ© usamos `random_state=42`? Â¿QuÃ© pasarÃ­a si no lo ponemos?

---

## 🧪 Ejercicio 3 â€” Primer modelo (guiado)

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"MAE:  {mean_absolute_error(y_test, y_pred):.2f}")
print(f"RMSE: {root_mean_squared_error(y_test, y_pred):.2f}")
```

Interpreta los resultados: Â¿el error es aceptable para el negocio?

---

## 🧪 Ejercicio 4 â€” LÃ­nea base (medio)

Calcula el MAE de un modelo "tonto" que siempre predice el promedio de `y_train`.

```python
import numpy as np
baseline_pred = np.full(len(y_test), y_train.mean())
baseline_mae = mean_absolute_error(y_test, baseline_pred)
print(f"MAE lÃ­nea base: {baseline_mae:.2f}")
```

Â¿Nuestro modelo supera la lÃ­nea base? Si no, hay un problema.

---

## ✨ DesafÃ­o opcional

Agrega una tercera variable al modelo (por ejemplo, `descuento_pct`) y compara el nuevo MAE con el anterior. Â¿MejorÃ³? Grafica los residuos (diferencia entre predicciÃ³n y valor real) con `plt.hist`.
