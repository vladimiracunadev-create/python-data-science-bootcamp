# 💻 Guía de código — Clase 02: Pandas y limpieza de datos

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Cargar el CSV e inspeccionar la estructura general

```python
import pandas as pd

# Cargamos el archivo CSV en un DataFrame.
# El parámetro encoding evita errores con caracteres especiales en español.
df = pd.read_csv("datasets/ventas_tienda.csv", encoding="utf-8")

# head() muestra las primeras 5 filas para ver si las columnas tienen sentido.
print(df.head())

# info() revela nombres de columnas, tipo de dato y cantidad de valores no nulos.
# Es la primera herramienta de diagnóstico: muestra cuánto falta en cada columna.
print(df.info())
```

**¿Qué hace este bloque?**
Carga el CSV en memoria como un DataFrame y ejecuta dos inspecciones complementarias: `head()` muestra los primeros registros para verificar que el archivo se cargó correctamente, mientras que `info()` revela los tipos de dato y cuántos valores faltan por columna.

**¿Por qué se escribe así y no de otra forma?**
Separar `head()` e `info()` en dos llamadas distintas es intencional: responden preguntas diferentes. `head()` responde "¿qué contiene?", `info()` responde "¿cómo está estructurado?". Combinarlos en un solo vistazo hace que el estudiante pierda detalles críticos de tipo y nulos.

**Resultado esperado:**
```
   producto  unidades  precio_unitario medio_pago  descuento_pct
0     Mouse         3             8990    efectivo           0.10
1    Teclado         2            15990    tarjeta           0.05
...

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 120 entries, 0 to 119
Data columns (total 5 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   producto         120 non-null    object
 1   unidades         118 non-null    float64
 2   precio_unitario  120 non-null    int64
 3   medio_pago       115 non-null    object
 4   descuento_pct    120 non-null    float64
```

---

## Bloque 2: Detectar y cuantificar valores nulos

```python
# isna() devuelve True en cada celda que es NaN (valor faltante).
# .sum() cuenta cuántos True hay por columna.
nulos_por_columna = df.isna().sum()
print("Valores nulos por columna:")
print(nulos_por_columna)

# Calculamos el porcentaje de nulos respecto al total de filas.
# Esto ayuda a decidir si eliminar o imputar: si supera el 30%, hay un problema mayor.
porcentaje_nulos = (df.isna().sum() / len(df) * 100).round(1)
print("\nPorcentaje de nulos (%):")
print(porcentaje_nulos)
```

**¿Qué hace este bloque?**
Calcula cuántos valores faltan en cada columna y qué porcentaje representan del total de filas. Esta información es la base para decidir si eliminar filas, imputar valores o escalar el problema a quien generó los datos.

**¿Por qué se escribe así y no de otra forma?**
Ver solo el conteo de nulos sin el porcentaje puede ser engañoso: 10 nulos en un dataset de 20 filas es catastrófico, pero en uno de 10.000 filas es insignificante. El porcentaje provee el contexto necesario.

**Resultado esperado:**
```
Valores nulos por columna:
producto            0
unidades            2
precio_unitario     0
medio_pago          5
descuento_pct       0
dtype: int64

Porcentaje de nulos (%):
producto            0.0
unidades            1.7
precio_unitario     0.0
medio_pago          4.2
descuento_pct       0.0
```

---

## Bloque 3: Limpiar columnas de texto — estandarizar valores

```python
# Los valores de texto suelen llegar con espacios extra o mayúsculas inconsistentes.
# strip() elimina espacios al inicio y al final.
# lower() convierte todo a minúsculas para evitar que "Efectivo" y "efectivo" cuenten como distintos.
df["medio_pago"] = df["medio_pago"].str.strip().str.lower()

# Verificamos los valores únicos después de la limpieza.
# Si había inconsistencias, ahora deben estar unificadas.
print("Medios de pago únicos tras limpieza:")
print(df["medio_pago"].value_counts())
```

**¿Qué hace este bloque?**
Estandariza la columna `medio_pago` eliminando espacios y normalizando a minúsculas. Luego verifica el resultado con `value_counts()` para confirmar que los valores quedaron unificados.

**¿Por qué se escribe así y no de otra forma?**
Aplicar `str.strip()` y `str.lower()` en cadena es la forma idiomática en pandas para limpiar texto. Hacerlo antes de cualquier agrupación o filtro es crítico: si `"Tarjeta"` y `"tarjeta"` existen a la vez, cualquier `groupby` las contará como categorías distintas, produciendo resultados incorrectos.

**Resultado esperado:**
```
Medios de pago únicos tras limpieza:
efectivo    52
tarjeta     48
transferencia  15
dtype: int64
```

---

## Bloque 4: Manejar nulos con criterio — eliminar o imputar

```python
# Opción 1: eliminar filas donde 'unidades' sea nulo.
# Se justifica si la fila completa no tiene sentido sin ese dato.
df_sin_nulos = df.dropna(subset=["unidades"])
print(f"Filas originales: {len(df)} | Filas tras dropna: {len(df_sin_nulos)}")

# Opción 2: imputar 'medio_pago' nulo con el valor más frecuente (moda).
# Se justifica cuando perder la fila eliminaría información valiosa de otras columnas.
moda_pago = df["medio_pago"].mode()[0]
df["medio_pago"] = df["medio_pago"].fillna(moda_pago)
print(f"Nulos restantes en medio_pago: {df['medio_pago'].isna().sum()}")
```

**¿Qué hace este bloque?**
Muestra dos estrategias distintas según el tipo de columna: `dropna()` para eliminar filas donde falta un dato crítico (como las unidades vendidas), y `fillna()` con la moda para imputar una categoría cuando perder toda la fila sería un desperdicio de información.

**¿Por qué se escribe así y no de otra forma?**
No existe una única respuesta correcta: la decisión depende del contexto del negocio. Documentar el criterio (como los comentarios de este bloque) es tan importante como el código mismo, porque permite que otra persona entienda y cuestione las decisiones tomadas.

**Resultado esperado:**
```
Filas originales: 120 | Filas tras dropna: 118
Nulos restantes en medio_pago: 0
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `UnicodeDecodeError` al leer el CSV | El archivo usa una codificación distinta a UTF-8 (común en archivos exportados desde Excel en Windows) | Probar `pd.read_csv(..., encoding="latin-1")` o `encoding="cp1252"` |
| `KeyError: 'columna'` al acceder a un campo | El nombre de la columna tiene espacios extra o mayúsculas inesperadas | Ejecutar `df.columns.tolist()` para ver los nombres exactos; renombrar con `df.columns = df.columns.str.strip().str.lower()` |
| `fillna()` no modifica el DataFrame original | pandas devuelve una copia por defecto; el resultado no se reasigna | Usar `df["col"] = df["col"].fillna(valor)` o el parámetro `inplace=True` (no recomendado en código moderno) |
| `AttributeError: 'float' object has no attribute 'strip'` | Se aplica `.str.strip()` a una columna que tiene valores nulos; pandas los interpreta como float | Usar `df["col"].str.strip()` solo después de confirmar que no hay nulos, o agregar `.fillna("")` antes |
