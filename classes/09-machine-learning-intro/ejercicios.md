# Ejercicios — Clase 09: Introducción al Machine Learning

## Ejercicio 1 — Identificar variables (fácil)

Con el dataset `ventas_tienda.csv`:

1. Lista todas las columnas del dataset.
2. ¿Cuál sería una buena variable objetivo (target) para predecir?
3. ¿Cuáles serían buenas variables predictoras (features)?
4. ¿Hay alguna columna que NO deberías usar como feature? ¿Por qué?

---

## Ejercicio 2 — Train/Test split (guiado)

```python
from sklearn.model_selection import train_test_split
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
# Completa:
X = df[["unidades_vendidas", "precio_unitario"]]
y = df["___"]  # ¿qué predecimos?

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {len(X_train)} filas | Test: {len(X_test)} filas")
```

¿Por qué usamos `random_state=42`? ¿Qué pasaría si no lo ponemos?

---

## Ejercicio 3 — Primer modelo (guiado)

```python
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, root_mean_squared_error

model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(f"MAE:  {mean_absolute_error(y_test, y_pred):.2f}")
print(f"RMSE: {root_mean_squared_error(y_test, y_pred):.2f}")
```

Interpreta los resultados: ¿el error es aceptable para el negocio?

---

## Ejercicio 4 — Línea base (medio)

Calcula el MAE de un modelo "tonto" que siempre predice el promedio de `y_train`.

```python
import numpy as np
baseline_pred = np.full(len(y_test), y_train.mean())
baseline_mae = mean_absolute_error(y_test, baseline_pred)
print(f"MAE línea base: {baseline_mae:.2f}")
```

¿Nuestro modelo supera la línea base? Si no, hay un problema.

---

## Desafío opcional

Agrega una tercera variable al modelo (por ejemplo, `descuento_pct`) y compara el nuevo MAE con el anterior. ¿Mejoró? Grafica los residuos (diferencia entre predicción y valor real) con `plt.hist`.
