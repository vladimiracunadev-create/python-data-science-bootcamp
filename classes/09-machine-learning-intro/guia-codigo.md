# 💻 Guía de código — Clase 09: Introducción a machine learning

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Separar variables de entrada y variable objetivo

```python
import pandas as pd

# Cargamos el dataset de estudiantes en un DataFrame.
df = pd.read_csv("datasets/estudiantes.csv")

# X contiene las variables de entrada: lo que el modelo usará para predecir.
# Elegimos columnas que tengan relación lógica con la variable que queremos predecir.
X = df[["asistencia_pct", "evaluacion_python", "edad"]]

# y es la variable objetivo: lo que queremos que el modelo aprenda a estimar.
y = df["evaluacion_pandas"]

print("Filas y columnas de X:", X.shape)
print("Primeras filas de X:")
print(X.head())
print("\nPrimeros valores de y:")
print(y.head())
```

**¿Qué hace este bloque?**
Carga el dataset y lo divide en dos partes: la matriz de características `X` (variables de entrada) y el vector objetivo `y` (la variable a predecir). Esta separación es el primer paso obligatorio antes de entrenar cualquier modelo supervisado.

**¿Por qué se escribe así y no de otra forma?**
Mantener `X` e `y` como objetos separados es la convención de scikit-learn. Todos los métodos de entrenamiento (`.fit(X, y)`) esperan esta estructura. Usar nombres en mayúscula para `X` y minúscula para `y` sigue la notación matemática estándar de álgebra lineal.

**Resultado esperado:**
```
Filas y columnas de X: (120, 3)
Primeras filas de X:
   asistencia_pct  evaluacion_python  edad
0            85.0               72.0    24
1            90.0               88.0    22
2            70.0               65.0    26
3            95.0               91.0    23
4            60.0               55.0    28

Primeros valores de y:
0    68.0
1    84.0
2    61.0
3    89.0
4    52.0
```

---

## Bloque 2: Dividir en conjunto de entrenamiento y de prueba

```python
from sklearn.model_selection import train_test_split

# Dividimos los datos en dos conjuntos:
# - Entrenamiento (80 %): el modelo aprenderá de estos datos.
# - Prueba (20 %): evaluaremos el modelo con datos que nunca vio.
# random_state garantiza que la división sea reproducible (siempre la misma).
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Tamaño de entrenamiento:", X_train.shape)
print("Tamaño de prueba:       ", X_test.shape)
```

**¿Qué hace este bloque?**
Divide los datos de forma aleatoria en dos subconjuntos estratificados por `random_state`. El 80 % se usa para entrenar y el 20 % queda reservado para simular datos nuevos que el modelo nunca vio.

**¿Por qué se escribe así y no de otra forma?**
Sin esta división, el modelo podría "memorizar" los datos de entrenamiento y dar resultados artificialmente buenos. Evaluar siempre en datos no vistos es la práctica mínima para medir si el modelo generaliza bien.

**Resultado esperado:**
```
Tamaño de entrenamiento: (96, 3)
Tamaño de prueba:        (24, 3)
```

---

## Bloque 3: Entrenar una regresión lineal y generar predicciones

```python
from sklearn.linear_model import LinearRegression

# Creamos el modelo: la clase LinearRegression encapsula todos los parámetros.
modelo = LinearRegression()

# fit() es el paso de "aprendizaje": el modelo ajusta sus coeficientes internos
# para minimizar el error entre sus predicciones y los valores reales de y_train.
modelo.fit(X_train, y_train)

# predict() aplica el modelo entrenado a datos nuevos (X_test).
# El resultado son los valores estimados de evaluacion_pandas para cada fila.
predicciones = modelo.predict(X_test)

print("Primeras 5 predicciones:", predicciones[:5].round(2))
print("Valores reales:         ", y_test.values[:5])
```

**¿Qué hace este bloque?**
Instancia el modelo, lo entrena con los datos de entrenamiento y luego genera predicciones para el conjunto de prueba. Comparar `predicciones` con `y_test` permite ver cuán cerca está el modelo de los valores reales.

**¿Por qué se escribe así y no de otra forma?**
La API de scikit-learn sigue siempre el mismo patrón: `instanciar → fit → predict`. Aprenderlo aquí sirve para todos los modelos del ecosistema (árboles, regresión logística, bosques aleatorios, etc.) sin cambiar la estructura del código.

**Resultado esperado:**
```
Primeras 5 predicciones: [71.43 83.12 59.87 88.56 64.20]
Valores reales:          [68.   84.   61.   89.   52.  ]
```

---

## Bloque 4: Evaluar el modelo con métricas numéricas

```python
from sklearn.metrics import mean_absolute_error, r2_score

# MAE (Error Absoluto Medio): promedio de cuánto se equivoca el modelo en cada fila.
# Un MAE de 5 significa que en promedio el modelo se aleja 5 puntos del valor real.
mae = mean_absolute_error(y_test, predicciones)

# R² (coeficiente de determinación): qué proporción de la variación en y explica el modelo.
# R² = 1.0 es perfecto. R² = 0.0 es tan bueno como predecir siempre el promedio.
r2 = r2_score(y_test, predicciones)

print(f"MAE (Error Absoluto Medio): {mae:.2f} puntos")
print(f"R² (Bondad de ajuste):      {r2:.3f}")

# También podemos inspeccionar los coeficientes para entender el modelo.
import pandas as pd
coef = pd.Series(modelo.coef_, index=X.columns)
print("\nCoeficientes del modelo:")
print(coef.sort_values(ascending=False))
```

**¿Qué hace este bloque?**
Cuantifica qué tan bueno es el modelo usando dos métricas complementarias: MAE (cuánto se equivoca en promedio, en las mismas unidades que y) y R² (cuánta variación de y captura el modelo). Además muestra los coeficientes para entender qué variable pesa más.

**¿Por qué se escribe así y no de otra forma?**
Un solo número de accuracy no es suficiente para entender un modelo de regresión. MAE es fácil de comunicar ("el modelo se equivoca ±5 puntos en promedio"); R² da contexto proporcional. Combinar ambas evita interpretar el modelo de forma incompleta.

**Resultado esperado:**
```
MAE (Error Absoluto Medio): 5.83 puntos
R² (Bondad de ajuste):      0.741

Coeficientes del modelo:
evaluacion_python    0.831
asistencia_pct       0.412
edad                -0.203
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `NotFittedError: This LinearRegression instance is not fitted yet` | Se llama a `.predict()` antes de llamar a `.fit()` | Asegurarse de ejecutar `modelo.fit(X_train, y_train)` antes de `modelo.predict(X_test)` |
| `ValueError: Input contains NaN` | El DataFrame tiene valores nulos en X o y | Revisar con `X.isnull().sum()` y eliminar o imputar antes de entrenar |
| `ValueError: could not convert string to float` | Alguna columna de X contiene texto en lugar de números | Convertir columnas categóricas con `pd.get_dummies()` o `OrdinalEncoder` antes del split |
| `KeyError: 'nombre_columna'` | El nombre de la columna tiene un espacio o error tipográfico | Verificar con `df.columns.tolist()` antes de construir X |
| R² negativo | El modelo es peor que predecir siempre el promedio | Revisar si X e y están mezclados, o si los datos tienen muchos outliers sin tratar |
