# 🧠 Documento teórico — Clase 18: Feature engineering — crear mejores variables
> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central
Los modelos de machine learning aprenden mejor cuando las variables son claras, relevantes y bien preparadas.

## ❓ Por qué importa este módulo
La mayoría de los modelos de machine learning no trabajan directamente con texto, fechas o categorías en bruto. Necesitan números bien estructurados que capturen la información de manera útil. El feature engineering es el proceso de transformar los datos crudos en esas variables. Está documentado que el 70-80% del tiempo de un proyecto de ciencia de datos se dedica a esta etapa. Un modelo sencillo con buenas variables suele superar a un modelo complejo con variables mal preparadas.

## 💻 Bloque de código documentado

### Carga y exploración inicial del dataset
**Qué hace:** Carga el dataset de ventas y examina su estructura antes de crear nuevas variables.
**Para qué sirve:** Identificar qué columnas existen, qué tipos de datos tienen y qué transformaciones son posibles o necesarias.

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Cargar el dataset
ventas = pd.read_csv("datasets/ventas_tienda.csv")
estudiantes = pd.read_csv("datasets/estudiantes.csv")

# Explorar estructura
print(ventas.dtypes)
print(ventas.head())
print(ventas.shape)
```

### Creación de variables numéricas derivadas
**Qué hace:** Calcula nuevas columnas combinando columnas existentes con operaciones aritméticas.
**Para qué sirve:** Captura relaciones que el modelo no vería fácilmente por sí solo. Por ejemplo, el ingreso neto combina precio, cantidad y descuento en una sola señal.

```python
# total_neto: ingreso real después del descuento
# Suponemos que "descuento" es un porcentaje (0 a 100)
ventas["total_neto"] = ventas["precio_unitario"] * ventas["unidades"] * (1 - ventas["descuento"] / 100)

# margen_por_unidad: diferencia entre precio y costo por unidad
ventas["margen_por_unidad"] = ventas["precio_unitario"] - ventas["costo_unitario"]

# tasa_descuento_efectiva: qué fracción del precio total se descontó
ventas["tasa_descuento_efectiva"] = ventas["descuento"] / 100

print(ventas[["precio_unitario", "unidades", "descuento", "total_neto", "margen_por_unidad"]].head())
```

### Extracción de información desde fechas
**Qué hace:** Descompone una columna de fecha en múltiples variables numéricas o binarias que capturan información temporal útil.
**Para qué sirve:** Los modelos no pueden operar directamente con fechas en formato texto o datetime, pero sí con el mes, el día o si es fin de semana.

```python
# Convertir la columna de fecha al tipo datetime
ventas["fecha"] = pd.to_datetime(ventas["fecha"])

# Extraer componentes temporales
ventas["mes"]          = ventas["fecha"].dt.month           # 1 a 12
ventas["dia_semana"]   = ventas["fecha"].dt.dayofweek       # 0=Lunes, 6=Domingo
ventas["dia_mes"]      = ventas["fecha"].dt.day             # 1 a 31
ventas["trimestre"]    = ventas["fecha"].dt.quarter         # 1 a 4
ventas["es_fin_semana"] = (ventas["dia_semana"] >= 5).astype(int)  # 1 si sábado o domingo

print(ventas[["fecha", "mes", "dia_semana", "es_fin_semana"]].head())
```

### Codificación de variables categóricas: one-hot encoding
**Qué hace:** Convierte cada categoría de una variable en una columna binaria (0 o 1). Se llama "one-hot" porque exactamente una columna tiene valor 1 por fila.
**Para qué sirve:** La mayoría de los modelos solo aceptan variables numéricas. `pd.get_dummies` automatiza esta transformación.

```python
# Codificación one-hot de la columna "categoría"
dummies_categoria = pd.get_dummies(ventas["categoría"], prefix="cat")

# Agregar las nuevas columnas al dataframe
ventas = pd.concat([ventas, dummies_categoria], axis=1)

# Verificar las nuevas columnas
print(dummies_categoria.head())
print("Columnas creadas:", dummies_categoria.columns.tolist())
```

### Codificación ordinal con map
**Qué hace:** Asigna un número entero a cada categoría según un orden explícito definido manualmente.
**Para qué sirve:** Para variables que tienen un orden natural (pequeño < mediano < grande) donde one-hot perdería esa información de jerarquía.

```python
# Supongamos que "nivel_riesgo" tiene valores: "bajo", "medio", "alto"
mapa_nivel = {"bajo": 0, "medio": 1, "alto": 2}
ventas["nivel_riesgo_cod"] = ventas["nivel_riesgo"].map(mapa_nivel)

# En estudiantes: codificar el turno como ordinal
mapa_turno = {"mañana": 0, "tarde": 1, "noche": 2}
estudiantes["turno_cod"] = estudiantes["turno"].map(mapa_turno)

print(estudiantes[["turno", "turno_cod"]].drop_duplicates())
```

### Binning: convertir variables continuas en rangos
**Qué hace:** Divide una variable numérica continua en intervalos (bins) y asigna una etiqueta a cada intervalo.
**Para qué sirve:** Para capturar relaciones no lineales o para crear variables de grupo cuando la magnitud exacta no importa tanto como el rango.

```python
# pd.cut: define los bordes de los rangos manualmente
ventas["rango_venta"] = pd.cut(
    ventas["total_venta"],
    bins=[0, 500, 1500, 5000, float("inf")],
    labels=["bajo", "medio", "alto", "premium"]
)

# pd.qcut: divide en rangos de igual cantidad de observaciones (cuartiles)
estudiantes["rango_nota"] = pd.qcut(
    estudiantes["nota_final"],
    q=4,
    labels=["Q1", "Q2", "Q3", "Q4"]
)

print(ventas["rango_venta"].value_counts())
print(estudiantes["rango_nota"].value_counts())
```

### Escalado de variables numéricas
**Qué hace:** Transforma los valores de una variable para que queden en un rango estándar. `StandardScaler` lleva la variable a media 0 y desviación estándar 1. `MinMaxScaler` comprime los valores al rango [0, 1].
**Para qué sirve:** Muchos modelos (regresión, SVM, redes neuronales, KNN) son sensibles a la escala de las variables. Sin escalado, una variable con valores en miles domina sobre una con valores entre 0 y 1.

```python
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Seleccionar columnas numéricas para escalar
columnas_num = ["precio_unitario", "unidades", "total_neto", "descuento"]

# StandardScaler: media=0, std=1 — útil cuando los datos siguen distribución normal
scaler_std = StandardScaler()
ventas_std = scaler_std.fit_transform(ventas[columnas_num])
ventas_std_df = pd.DataFrame(ventas_std, columns=[c + "_std" for c in columnas_num])

# MinMaxScaler: rango [0, 1] — útil cuando se necesita una cota absoluta
scaler_mm = MinMaxScaler()
ventas_mm = scaler_mm.fit_transform(ventas[columnas_num])
ventas_mm_df = pd.DataFrame(ventas_mm, columns=[c + "_mm" for c in columnas_num])

print(ventas_std_df.describe().round(2))
```

### Variables de interacción
**Qué hace:** Multiplica o combina dos variables existentes para capturar el efecto conjunto que ninguna tiene por separado.
**Para qué sirve:** Cuando la relación entre dos variables es multiplicativa (el efecto de una depende del nivel de la otra), la interacción la hace explícita para el modelo.

```python
# Interacción precio × descuento: captura el impacto económico real del descuento
ventas["precio_x_descuento"] = ventas["precio_unitario"] * ventas["descuento"]

# Interacción asistencia × horas_estudio: esfuerzo combinado del estudiante
estudiantes["esfuerzo"] = estudiantes["asistencia"] * estudiantes["horas_estudio"]

print(estudiantes[["asistencia", "horas_estudio", "esfuerzo", "nota_final"]].head())
```

### Selección de variables por correlación con el target
**Qué hace:** Calcula la correlación de cada variable con la variable objetivo (target) y elimina las que tienen poca relación o están muy correlacionadas entre sí.
**Para qué sirve:** Reduce el ruido en el dataset y evita la multicolinealidad, mejorando la estabilidad y la interpretabilidad del modelo.

```python
# Correlación de todas las variables numéricas con la nota final
correlaciones = estudiantes.select_dtypes(include="number").corr()["nota_final"].sort_values(ascending=False)
print("Correlación con nota_final:")
print(correlaciones)

# Eliminar variables con correlación absoluta menor a 0.1 (poco informativas)
variables_utiles = correlaciones[correlaciones.abs() > 0.1].index.tolist()
print("\nVariables seleccionadas:", variables_utiles)
```

## ⚠️ Errores frecuentes a vigilar
- Escalar antes de dividir en train/test: el escalador debe ajustarse solo en el conjunto de entrenamiento y luego aplicarse al de test, no al revés.
- Usar one-hot en variables ordinales con muchos niveles: genera demasiadas columnas y puede causar overfitting.
- Olvidar convertir la columna de fecha a datetime antes de extraer componentes.
- Crear variables derivadas con divisiones sin verificar que el denominador no sea cero.
- Eliminar variables por correlación baja sin verificar si son importantes para el contexto del negocio.

## 🔗 Conexión con el siguiente módulo
Con el dataset preparado y las variables bien construidas, el siguiente paso es introducir los primeros modelos de machine learning supervisado. El trabajo de feature engineering realizado en esta clase es exactamente lo que esos modelos necesitan como entrada para hacer predicciones útiles y confiables.
