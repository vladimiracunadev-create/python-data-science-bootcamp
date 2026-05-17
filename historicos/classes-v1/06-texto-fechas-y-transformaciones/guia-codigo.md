# 💻 Guía de código — Clase 06: Texto, fechas y transformaciones

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Convertir la columna de fecha y verificar el resultado

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")

# ANTES de convertir: la columna es texto (dtype object)
print("Tipo ANTES:", df["fecha"].dtype)
print(df["fecha"].head(3))

# Convertimos al tipo datetime de pandas
df["fecha"] = pd.to_datetime(df["fecha"])

# DESPUÉS de convertir: el dtype cambia a datetime64
print("\nTipo DESPUÉS:", df["fecha"].dtype)
print(df["fecha"].head(3))
```

**¿Qué hace este bloque?** Carga el CSV, muestra que `fecha` inicialmente es texto (`object`) y la convierte a `datetime64` con `pd.to_datetime`. Imprime el tipo antes y después para que la diferencia sea visible.

**¿Por qué se escribe así?** Siempre conviene verificar el dtype antes y después de una conversión. Si la conversión falla silenciosamente o produce `NaT`, el `print` lo revelará de inmediato.

**Resultado esperado:** Antes muestra `object` con strings como `"2024-01-15"`; después muestra `datetime64[ns]` con el mismo valor pero en formato de fecha real.

---

## Bloque 2: Crear columnas derivadas de fecha

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

# Columnas derivadas que abren nuevas preguntas de análisis
df["mes"]        = df["fecha"].dt.to_period("M").astype(str)  # "2024-01", "2024-02", ...
df["dia_semana"] = df["fecha"].dt.day_name()                  # "Monday", "Tuesday", ...
df["trimestre"]  = df["fecha"].dt.quarter                     # 1, 2, 3, 4
df["anio"]       = df["fecha"].dt.year                        # 2024, 2025, ...

# Verificamos las columnas nuevas
print(df[["fecha", "mes", "dia_semana", "trimestre", "anio"]].head(6))

# Contamos cuántas ventas hay por día de la semana
print("\nVentas por día de la semana:")
print(df["dia_semana"].value_counts())
```

**¿Qué hace este bloque?** Crea cuatro columnas nuevas a partir de la columna `fecha` convertida, cada una respondiendo una dimensión temporal distinta (mes, día, trimestre, año).

**¿Por qué se escribe así?** Las columnas derivadas se guardan en el DataFrame para poder reutilizarlas en filtros, agrupaciones y gráficos. `to_period("M").astype(str)` genera etiquetas ordenables como `"2024-01"` que funcionan bien en el eje X de un gráfico.

**Resultado esperado:** Un DataFrame con cinco columnas de fecha, y un conteo de ventas por día de la semana mostrando cuál día tiene más registros.

---

## Bloque 3: Normalizar texto para evitar duplicados de categoría

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")

# Problema: la misma categoría puede aparecer con variaciones
print("Valores únicos ANTES de normalizar:")
print(df["producto"].unique()[:10])   # Muestra los primeros 10 valores únicos

# Normalización en tres pasos:
# 1. strip() elimina espacios al inicio y al final
# 2. lower() convierte todo a minúsculas
df["producto_normalizado"] = (
    df["producto"]
    .str.strip()
    .str.lower()
)

print("\nValores únicos DESPUÉS de normalizar:")
print(df["producto_normalizado"].unique()[:10])

# Comparamos la cantidad de valores únicos
print(f"\nÚnicos antes:  {df['producto'].nunique()}")
print(f"Únicos después: {df['producto_normalizado'].nunique()}")
```

**¿Qué hace este bloque?** Muestra cuántos valores únicos hay antes y después de normalizar la columna de texto. La normalización elimina diferencias invisibles (espacios) y de capitalización.

**¿Por qué se escribe así?** El encadenamiento `.str.strip().str.lower()` es el patrón estándar de normalización mínima. Se guarda en una columna nueva (`producto_normalizado`) para no destruir los datos originales.

**Resultado esperado:** El número de valores únicos después de normalizar es igual o menor al de antes. Si había `"Laptop"`, `" laptop"` y `"LAPTOP"`, después los tres se convierten en `"laptop"` y cuentan como uno.

---

## Bloque 4: Combinar transformaciones y usar el resultado en análisis

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
df["fecha"] = pd.to_datetime(df["fecha"])

# Aplicamos todas las transformaciones en secuencia
df["mes"]                 = df["fecha"].dt.to_period("M").astype(str)
df["dia_semana"]          = df["fecha"].dt.day_name()
df["producto_normalizado"] = df["producto"].str.strip().str.lower()

# Ahora podemos responder preguntas que antes no eran posibles:
# ¿Cuáles son los 3 productos más vendidos (por conteo de transacciones)?
top_productos = (
    df.groupby("producto_normalizado")["producto_normalizado"]
    .count()
    .sort_values(ascending=False)
    .head(3)
)
print("Top 3 productos más vendidos:")
print(top_productos)

# ¿En qué mes se registraron más ventas?
print("\nVentas por mes:")
print(df["mes"].value_counts().sort_index())
```

**¿Qué hace este bloque?** Aplica todas las transformaciones y las usa para responder preguntas de negocio concretas mediante agrupaciones y conteos.

**¿Por qué se escribe así?** El encadenamiento `.groupby().count().sort_values().head()` es un patrón compacto y legible para obtener un ranking. Se usa `sort_index()` en el conteo por mes para que los meses aparezcan en orden cronológico.

**Resultado esperado:** Una lista de los 3 productos más frecuentes en el dataset y un conteo de transacciones por mes ordenado cronológicamente.

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `AttributeError: Can only use .dt accessor with datetimelike values` | Se intenta usar `.dt.month` antes de convertir la columna con `pd.to_datetime` | Siempre ejecutar `df["fecha"] = pd.to_datetime(df["fecha"])` antes de usar `.dt` |
| `AttributeError: Can only use .str accessor with string values` | La columna ya es numérica o datetime, no texto | Verificar `df["columna"].dtype` antes de aplicar `.str.strip()` |
| `ParserError` al usar `pd.to_datetime` | El formato de la fecha no es estándar (ej. `"15/Ene/24"`) | Usar el parámetro `format` explícito: `pd.to_datetime(df["fecha"], format="%d/%b/%y")` |
| Los valores únicos no se reducen tras normalizar | El problema era de formato, no solo de capitalización (ej. caracteres especiales) | Agregar `.str.replace("[^a-z0-9 ]", "", regex=True)` para quitar caracteres especiales |
