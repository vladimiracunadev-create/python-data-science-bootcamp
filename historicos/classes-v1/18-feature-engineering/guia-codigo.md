# 💻 Guía de código — Clase 18: Feature Engineering — crear mejores variables

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Features derivadas y descomposición de fechas

```python
import pandas as pd
import numpy as np

df = pd.read_csv("ventas_tienda.csv")

# Convertir columna de texto a tipo datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# Descomponer la fecha en múltiples features numéricas
df["anio"]         = df["fecha"].dt.year
df["mes"]          = df["fecha"].dt.month
df["dia"]          = df["fecha"].dt.day
df["dia_semana"]   = df["fecha"].dt.dayofweek    # 0=Lunes, 6=Domingo
df["nombre_dia"]   = df["fecha"].dt.day_name()   # "Monday", "Tuesday"...
df["es_fin_semana"] = df["dia_semana"].isin([5, 6]).astype(int)  # 1=sí, 0=no
df["trimestre"]    = df["fecha"].dt.quarter       # 1, 2, 3 o 4

# Features derivadas numéricas
df["ingreso_total"]  = df["precio"] * df["cantidad"]
df["precio_final"]   = df["precio"] * (1 - df["descuento_pct"] / 100)

print("Columnas nuevas:")
print(df[["fecha", "mes", "dia_semana", "es_fin_semana", "ingreso_total"]].head())
```

**¿Qué hace este bloque?**
- `pd.to_datetime(df["fecha"])`: convierte la columna de texto (tipo `object`) al tipo especial `datetime64` de pandas, que habilita el acceso al atributo `.dt` para extraer componentes de la fecha.
- `df["fecha"].dt.year`, `.dt.month`, etc.: accede a partes específicas de la fecha como números enteros.
- `df["fecha"].dt.dayofweek`: devuelve 0 para Lunes y 6 para Domingo.
- `.isin([5, 6]).astype(int)`: crea una columna binaria — `True` si es sábado o domingo, convertida a `int` para obtener 1 o 0 en lugar de `True`/`False`.
- `df["precio"] * df["cantidad"]`: multiplicación vectorizada que crea el ingreso total de cada fila.

**¿Por qué se escribe así y no de otra forma?**
Las fechas en bruto son prácticamente inútiles para la mayoría de los modelos de ML porque no pueden interpretar "2024-01-15" como dato numérico significativo. Al descomponer la fecha en partes numéricas, el modelo puede aprender patrones temporales: "las ventas del fin de semana son mayores", "diciembre siempre tiene pico", etc.

**Resultado esperado:**
El DataFrame original con 9 columnas nuevas: año, mes, día, día de la semana, nombre del día, indicador fin de semana, trimestre, ingreso total y precio final con descuento.

---

## Bloque 2: Encoding de variables categóricas

```python
df_est = pd.read_csv("estudiantes.csv")

# ONE-HOT ENCODING para variables nominales (sin orden natural)
# drop_first=True elimina una columna para evitar multicolinealidad perfecta
df_dummies = pd.get_dummies(
    df_est,
    columns=["ciudad", "carrera"],
    drop_first=True,
    dtype=int          # 0/1 enteros en lugar de True/False
)

print("Columnas después de one-hot encoding:")
print([c for c in df_dummies.columns if "ciudad" in c or "carrera" in c])

# ENCODING ORDINAL para variables con orden natural
orden_educacion = {"Secundaria": 0, "Técnico": 1, "Universitario": 2, "Posgrado": 3}
df_est["nivel_educacion_num"] = df_est["nivel_educacion"].map(orden_educacion)

print("\nMapeo de nivel de educación:")
print(
    df_est[["nivel_educacion", "nivel_educacion_num"]]
    .drop_duplicates()
    .sort_values("nivel_educacion_num")
)
```

**¿Qué hace este bloque?**
- `pd.get_dummies(df, columns=["ciudad"])`: por cada valor único en `ciudad`, crea una nueva columna binaria. Si hay 5 ciudades, crea 5 columnas (o 4 con `drop_first=True`).
- `drop_first=True`: elimina la primera categoría generada. Esto evita la "multicolinealidad perfecta": si tienes N columnas, la Nésima se puede deducir de las demás, lo que confunde a los modelos lineales.
- `dtype=int`: genera columnas con valores 0 y 1 (enteros) en lugar de `True`/`False` (booleanos). Es más compatible con scikit-learn.
- `.map(diccionario)`: reemplaza cada texto por su número correspondiente, preservando el orden natural de la categoría.

**¿Por qué se escribe así y no de otra forma?**
Para categorías SIN orden (ciudad, color, carrera) se usa one-hot encoding. Para categorías CON orden (bajo/medio/alto, secundaria/universitario/posgrado) se usa encoding ordinal, porque en ese caso el número mayor sí significa "más" de algo. Usar ordinal en variables sin orden forzaría una relación matemática que no existe en realidad.

**Resultado esperado:**
Un DataFrame con columnas como `ciudad_Bogotá`, `ciudad_Medellín` (con 0 o 1) en lugar de la columna texto `ciudad`, más la nueva columna `nivel_educacion_num` con valores 0, 1, 2, 3.

---

## Bloque 3: Binning con pd.cut y pd.qcut

```python
df_est = pd.read_csv("estudiantes.csv")

# pd.cut — intervalos de ancho fijo (los rangos son iguales)
df_est["rango_edad"] = pd.cut(
    df_est["edad"],
    bins=[0, 18, 25, 35, 50, 100],
    labels=["Menor de edad", "Joven", "Adulto joven", "Adulto", "Mayor"]
)

# pd.qcut — intervalos por cuantiles (cada grupo tiene el mismo n de personas)
df_est["cuartil_nota"] = pd.qcut(
    df_est["nota_final"],
    q=4,
    labels=["Bajo", "Medio-bajo", "Medio-alto", "Alto"]
)

print("Distribución por rango de edad:")
print(df_est["rango_edad"].value_counts().sort_index())

print("\nDistribución por cuartil de nota:")
print(df_est["cuartil_nota"].value_counts().sort_index())
```

**¿Qué hace este bloque?**
- `pd.cut(columna, bins=[...], labels=[...])`: divide la columna numérica en intervalos de los rangos especificados. Cada persona se asigna al intervalo donde cae su valor. Los rangos tienen el mismo ancho pero pueden tener diferente cantidad de personas.
- `pd.qcut(columna, q=4, labels=[...])`: divide en 4 grupos (cuartiles) garantizando que cada grupo tenga aproximadamente el mismo número de observaciones, aunque los rangos puedan ser de distinto ancho.
- La diferencia clave: `cut` fija los rangos; `qcut` fija la cantidad de personas por grupo.

**¿Por qué se escribe así y no de otra forma?**
El binning transforma una variable continua en categórica. `cut` es útil cuando los rangos tienen significado concreto (ej. grupos de edad establecidos por ley o protocolo médico). `qcut` es útil para crear grupos balanceados, especialmente para visualización comparativa, evitando que un solo rango tenga el 90% de los datos.

**Resultado esperado:**
```
Distribución por rango de edad:
Menor de edad     5
Joven            32
Adulto joven     28
Adulto           15
Mayor             5

Distribución por cuartil de nota (aproximadamente iguales):
Bajo         21
Medio-bajo   21
Medio-alto   21
Alto         22
```

---

## Bloque 4: Escalado con StandardScaler y MinMaxScaler

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("ventas_tienda.csv")
columnas = ["precio", "cantidad", "descuento_pct", "ingreso_total"]
df_num = df[columnas].copy()

# STANDARDSCALER: transforma a media=0, desviación estándar=1
scaler_std = StandardScaler()
datos_std = scaler_std.fit_transform(df_num)
df_std = pd.DataFrame(datos_std, columns=[c + "_std" for c in columnas])

print("Después de StandardScaler:")
print(df_std.describe().round(2))

# MINMAXSCALER: transforma todos los valores al rango [0, 1]
scaler_mm = MinMaxScaler()
datos_mm = scaler_mm.fit_transform(df_num)
df_mm = pd.DataFrame(datos_mm, columns=[c + "_mm" for c in columnas])

print("\nDespués de MinMaxScaler:")
print(df_mm.describe().round(2))

# Para invertir la transformación y recuperar los valores originales
precios_originales = scaler_std.inverse_transform(datos_std)[:, 0]
print("\nPrimeros 5 precios recuperados:", precios_originales[:5].round(2))
```

**¿Qué hace este bloque?**
- `StandardScaler`: transforma cada valor a `(x - media) / desviación_estándar`. El resultado tiene media=0 y std=1. Conserva la forma de la distribución y no elimina outliers (los valores extremos siguen siendo extremos, pero en otra escala).
- `MinMaxScaler`: transforma cada valor a `(x - min) / (max - min)`. El resultado queda en el rango [0, 1]. Un único outlier puede comprimir todos los demás valores hacia el centro.
- `fit_transform(df_num)`: `.fit()` aprende los parámetros (media, std, o min, max) del dataset; `.transform()` aplica la transformación. Se combinan en un solo paso conveniente.
- `inverse_transform(...)`: aplica la transformación inversa para recuperar los valores en la escala original (útil para interpretar predicciones).

**¿Por qué se escribe así y no de otra forma?**
La regla más importante: hacer `fit_transform()` solo sobre los datos de entrenamiento, y solo `.transform()` (sin `.fit()`) sobre los datos de prueba. Si aplicas `.fit()` sobre los datos de prueba, introduces data leakage porque el scaler "aprende" información del futuro.

**Resultado esperado:**
```
Después de StandardScaler:
       precio_std  cantidad_std  ...
mean         0.00          0.00
std          1.00          1.00

Después de MinMaxScaler:
       precio_mm  cantidad_mm  ...
min         0.00        0.00
max         1.00        1.00
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `ValueError: could not convert string to float` en el scaler | La columna tiene texto mezclado o valores `NaN` | Limpiar con `df.dropna()` o imputar valores antes de escalar; verificar con `df.isnull().sum()` |
| One-hot encoding genera demasiadas columnas | La columna categórica tiene alta cardinalidad (muchos valores únicos) | Agrupar categorías poco frecuentes en "Otros" o usar Target Encoding con `category_encoders` |
| Data leakage al escalar | Se aplicó `fit_transform()` sobre todo el dataset antes de dividir en train/test | Dividir primero con `train_test_split()`, luego `fit_transform` solo en train y `transform` en test |
| `pd.cut` produce `NaN` para algunos valores | Hay valores fuera de los límites definidos en `bins` | Extender el primer bin a `-np.inf` y el último a `np.inf`: `bins=[-np.inf, 18, 35, np.inf]` |
| `get_dummies` no convierte una columna | La columna no está en `columns=` o no tiene tipo `object` | Especificar explícitamente: `columns=["mi_columna"]` o convertir con `.astype(str)` primero |
