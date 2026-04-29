# 🧠 Documento teórico — Clase 19: Regresión lineal y múltiple

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

La regresión lineal encuentra la línea que mejor resume la relación entre una variable y lo que queremos predecir.

## ❓ Por qué importa este módulo

Muchos problemas reales requieren predecir un número: ¿cuánto venderemos la próxima semana?, ¿cuál será la nota final del estudiante?, ¿a qué precio se venderá una casa? La regresión lineal es el punto de partida más claro para responder esas preguntas.

## 📖 Conceptos clave

### Regresión vs clasificación
- **Clasificación**: el resultado es una categoría (aprobado / reprobado, sí / no).
- **Regresión**: el resultado es un número continuo (3500 pesos, 87.4 puntos, 12.6 kg).

### Intuición de la línea de regresión
Imagina un scatter plot donde cada punto es un alumno: el eje X es horas de estudio y el eje Y es su nota. La regresión lineal busca la línea recta que pasa más cerca de todos los puntos a la vez. Esa línea tiene la forma:

```
y = intercepto + coeficiente × x
```

**Analogía accesible:** en una pizzería, el precio final es:
```
precio = costo_fijo + precio_por_ingrediente × cantidad_ingredientes
```
El `costo_fijo` es el intercepto (la base que pagas aunque no agregues nada extra).
El `precio_por_ingrediente` es el coeficiente (cuánto sube el precio por cada unidad extra).

### Regresión múltiple
Cuando hay más de una variable predictora:
```
y = intercepto + coef1×x1 + coef2×x2 + ...
```
Cada coeficiente dice "cuánto cambia Y cuando esa variable sube 1 unidad, manteniendo el resto igual".

### R² — coeficiente de determinación
- Valor entre 0 y 1.
- **R² = 1**: el modelo explica perfectamente todos los datos.
- **R² = 0**: el modelo no explica nada (no es mejor que usar el promedio).
- **Regla práctica**: R² > 0.7 suele ser considerado aceptable en ciencias sociales; en algunos contextos industriales se espera > 0.9.

### Residuos
El residuo de una predicción es la diferencia entre el valor real y el valor predicho:
```
residuo = y_real − y_predicho
```
- Residuos grandes indican casos donde el modelo se equivoca más.
- Graficar los residuos ayuda a detectar si el modelo tiene sesgos sistemáticos.

## 💻 Bloque de código documentado

### Regresión lineal simple

**Qué hace:** cargar datos → definir X e y → entrenar → leer coeficientes → calcular R²

**Para qué sirve:** predecir `total_neto` a partir de una sola variable y entender qué significa el coeficiente.

```python
# Qué hace: cargar datos → definir X e y → entrenar → leer coeficientes → calcular R²
# Para qué sirve: predecir total_neto con una variable y entender el coeficiente.
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/ventas_tienda.csv")

X = df[["unidades"]]        # variable predictora (matriz 2D)
y = df["total_neto"]        # variable objetivo

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("Intercepto:", modelo.intercept_)
print("Coeficiente:", modelo.coef_[0])
print("R²:", modelo.score(X_test, y_test))
```

### Regresión múltiple con residuos

```python
# Qué hace: añade más variables y calcula residuos para ver dónde falla el modelo.
# Para qué sirve: entender si agregar variables mejora la predicción.
import matplotlib.pyplot as plt

X2 = df[["unidades", "descuento_pct"]]
X2_train, X2_test, y2_train, y2_test = train_test_split(
    X2, y, test_size=0.2, random_state=42
)

modelo2 = LinearRegression()
modelo2.fit(X2_train, y2_train)

y_pred = modelo2.predict(X2_test)
residuos = y2_test.values - y_pred

print("R² múltiple:", modelo2.score(X2_test, y2_test))

plt.scatter(y_pred, residuos, alpha=0.5)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Valores predichos")
plt.ylabel("Residuos")
plt.title("Gráfico de residuos")
plt.tight_layout()
plt.show()
```

## ⚠️ Errores frecuentes a vigilar

- Usar una sola columna como array 1D en lugar de `df[["columna"]]` (necesita doble corchete para ser 2D).
- Confundir R² alto con que el modelo es perfecto: puede estar sobreajustado.
- Olvidar que la regresión asume una relación lineal; si la relación es curva, el modelo fallará sistemáticamente.

## 🔗 Conexión con el siguiente módulo

La clase 20 introduce los árboles de decisión, que capturan relaciones no lineales sin necesidad de suponer ninguna forma matemática específica.
