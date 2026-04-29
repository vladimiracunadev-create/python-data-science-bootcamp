# 💻 Guía de código — Clase 19: Regresión Lineal y Múltiple

> Walkthrough del código clave, bloque por bloque.

## Bloque 1: Regresión lineal simple con sklearn

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("ventas_tienda.csv")

# Preparar X e y
X = df[["publicidad"]]   # debe ser 2D (DataFrame, no Series)
y = df["ventas"]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Inspeccionar modelo
print(f"Intercepto: {model.intercept_:.2f}")
print(f"Coeficiente: {model.coef_[0]:.2f}")
print(f"R² en test: {model.score(X_test, y_test):.4f}")
```

**¿Qué hace?** Entrena una recta `ventas = intercepto + coef * publicidad` que minimiza el error cuadrático entre predicciones y valores reales.

**¿Por qué así?** `X` debe ser 2D porque sklearn espera una matriz de features. `train_test_split` garantiza que evaluamos en datos que el modelo nunca vio.

**Resultado esperado:** Intercepto (ventas base sin publicidad), coeficiente (cuántas unidades de ventas gana por cada unidad de publicidad) y R² entre 0 y 1.

---

## Bloque 2: Visualizar la línea de regresión y los residuales

```python
import numpy as np
from sklearn.metrics import mean_squared_error

# Predicciones
y_pred = model.predict(X_test)

# Gráfico 1: dispersión con línea de regresión
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.scatter(X_test, y_test, alpha=0.6, label="Datos reales")
plt.plot(X_test, y_pred, color="red", label="Línea de regresión")
plt.xlabel("Publicidad")
plt.ylabel("Ventas")
plt.title("Regresión Lineal")
plt.legend()

# Gráfico 2: residuales
residuales = y_test - y_pred
plt.subplot(1, 2, 2)
plt.scatter(y_pred, residuales, alpha=0.6)
plt.axhline(y=0, color="red", linestyle="--")
plt.xlabel("Valores predichos")
plt.ylabel("Residuales")
plt.title("Gráfico de Residuales")

plt.tight_layout()
plt.show()

# RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE: {rmse:.2f}")
```

**¿Qué hace?** Crea dos gráficos: el primero muestra qué tan bien se ajusta la línea a los datos, el segundo revela si los errores tienen algún patrón (no deberían).

**¿Por qué así?** Los residuales deben estar dispersos aleatoriamente alrededor de cero. Si forman una curva o embudo, el modelo lineal no es el más adecuado.

**Resultado esperado:** Nube de puntos aleatoria en el gráfico de residuales; RMSE en las mismas unidades que la variable `ventas`.

---

## Bloque 3: Regresión múltiple con varias variables

```python
# Cargar dataset de estudiantes
df = pd.read_csv("estudiantes.csv")

# Variables de entrada (múltiples features)
features = ["horas_estudio", "ausencias", "promedio_anterior"]
X = df[features]
y = df["calificacion_final"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar regresión múltiple (misma clase, más columnas)
model_multi = LinearRegression()
model_multi.fit(X_train, y_train)

# Interpretar coeficientes
for feature, coef in zip(features, model_multi.coef_):
    print(f"  {feature}: {coef:.3f}")
print(f"  Intercepto: {model_multi.intercept_:.3f}")
print(f"\nR² en test: {model_multi.score(X_test, y_test):.4f}")

rmse_multi = np.sqrt(mean_squared_error(y_test, model_multi.predict(X_test)))
print(f"RMSE: {rmse_multi:.2f}")
```

**¿Qué hace?** Ajusta un plano (o hiperplano) a los datos en lugar de una recta. Cada coeficiente indica cuánto cambia la calificación por cada unidad que aumenta esa variable, manteniendo las demás constantes.

**¿Por qué así?** Pasar una lista de columnas a `X` es todo lo que necesita sklearn para hacer regresión múltiple. No cambia la API, solo cambia la forma de los datos.

**Resultado esperado:** Un coeficiente por variable. Por ejemplo: `horas_estudio: 1.8` significa que estudiar una hora más se asocia con 1.8 puntos más en la calificación.

---

## ⚠️ Errores comunes y cómo resolverlos

| Error | Por qué ocurre | Solución |
|---|---|---|
| `ValueError: Expected 2D array, got 1D array` | Se pasó una Series en lugar de un DataFrame como X | Usar `df[["columna"]]` (doble corchete) en lugar de `df["columna"]` |
| R² negativo en test | El modelo es peor que predecir siempre la media; posible data leakage invertido o features sin relación | Revisar que el split sea correcto y que las features tengan correlación con y |
| RMSE muy alto comparado con la escala de y | El modelo no captura bien la variabilidad; puede haber outliers o relación no lineal | Escalar features, revisar outliers o probar regresión polinomial |
| `coef_` con valores enormes (ej: 10000) | Features en escalas muy distintas inflan los coeficientes | Aplicar `StandardScaler` antes de entrenar para comparar coeficientes correctamente |
