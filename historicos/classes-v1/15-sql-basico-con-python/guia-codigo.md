# 💻 Guía de código — Clase 15: SQL básico con Python

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Cargar datos en SQLite desde pandas

```python
import sqlite3
import pandas as pd

# Cargar el CSV en un DataFrame
df = pd.read_csv("ventas_tienda.csv")

# Crear conexión a SQLite (crea el archivo si no existe)
conn = sqlite3.connect("ventas.db")

# Guardar el DataFrame como tabla SQL
df.to_sql("ventas", conn, if_exists="replace", index=False)

print("Tabla cargada con", len(df), "registros")
```

**¿Qué hace este bloque?**
- `sqlite3.connect("ventas.db")`: crea o abre una conexión a una base de datos SQLite almacenada en el archivo `ventas.db`. Si el archivo no existe, SQLite lo crea automáticamente.
- `df.to_sql("ventas", conn, ...)`: escribe el contenido del DataFrame como una tabla llamada `"ventas"` en la base de datos.
- `if_exists="replace"`: si la tabla ya existe, la elimina y la vuelve a crear. Las opciones son `"replace"`, `"append"` (agrega filas sin borrar las existentes) y `"fail"` (lanza error si ya existe).
- `index=False`: no guarda el índice numérico del DataFrame como columna en la tabla SQL.

**¿Por qué se escribe así y no de otra forma?**
Esta es la forma estándar de crear un "puente" entre pandas y SQL. Es muy útil para explorar datos con SQL cuando el dataset ya vive como CSV o DataFrame, sin necesidad de instalar un servidor de base de datos.

**Resultado esperado:**
```
Tabla cargada con 500 registros
```
Y el archivo `ventas.db` aparece en la carpeta del proyecto.

---

## Bloque 2: Consultas básicas con SELECT, WHERE y ORDER BY

```python
# Ver las primeras 5 filas de la tabla
query1 = "SELECT * FROM ventas LIMIT 5"
resultado1 = pd.read_sql(query1, conn)
print(resultado1)

# Filtrar y ordenar
query2 = """
    SELECT producto, ventas, categoría
    FROM ventas
    WHERE ventas > 200
    ORDER BY ventas DESC
"""
resultado2 = pd.read_sql(query2, conn)
print(resultado2.head(10))
```

**¿Qué hace este bloque?**
- `SELECT * FROM ventas LIMIT 5`: selecciona todas las columnas de la tabla `ventas` pero limita la salida a 5 filas. El `*` significa "todas las columnas".
- `SELECT producto, ventas, categoría`: selecciona solo esas tres columnas, en el orden indicado.
- `WHERE ventas > 200`: filtra y devuelve solo las filas donde el valor de `ventas` supera 200.
- `ORDER BY ventas DESC`: ordena los resultados de mayor a menor. Sin `DESC` el orden sería ascendente (de menor a mayor).
- `pd.read_sql(query, conn)`: ejecuta la consulta SQL y convierte el resultado en un DataFrame de pandas.

**¿Por qué se escribe así y no de otra forma?**
Las consultas multilínea se escriben con comillas triples (`"""..."""`) para mayor legibilidad. Es una buena práctica separar cada cláusula SQL en su propia línea. `pd.read_sql` es la función que actúa de puente entre el resultado SQL y el ecosistema de pandas.

**Resultado esperado:**
Un DataFrame con las columnas `producto`, `ventas`, `categoría`, mostrando solo los registros con ventas mayores a 200, ordenado de mayor a menor.

---

## Bloque 3: Agregaciones con GROUP BY y HAVING

```python
# Resumen de ventas por categoría
query3 = """
    SELECT
        categoría,
        COUNT(*)          AS num_registros,
        SUM(ventas)       AS ventas_totales,
        AVG(ventas)       AS ventas_promedio,
        MAX(ventas)       AS venta_maxima
    FROM ventas
    GROUP BY categoría
    ORDER BY ventas_totales DESC
"""
resumen = pd.read_sql(query3, conn)
print(resumen)

# Solo categorías con más de 50 registros (HAVING filtra grupos)
query4 = """
    SELECT categoría, COUNT(*) AS total
    FROM ventas
    GROUP BY categoría
    HAVING COUNT(*) > 50
    ORDER BY total DESC
"""
categorias_grandes = pd.read_sql(query4, conn)
print(categorias_grandes)
```

**¿Qué hace este bloque?**
- `GROUP BY categoría`: agrupa todas las filas que tienen el mismo valor en `categoría`. Las funciones de agregación operan dentro de cada grupo, no sobre toda la tabla.
- `COUNT(*)`: cuenta el número de filas en cada grupo (incluyendo nulos).
- `SUM(ventas)`, `AVG(ventas)`, `MAX(ventas)`: calculan la suma, promedio y máximo de la columna `ventas` dentro de cada grupo.
- `AS nombre`: asigna un nombre alternativo (alias) a la columna calculada, lo que hace el resultado más legible.
- `HAVING COUNT(*) > 50`: filtra los grupos **después** de la agregación. Esta es la diferencia clave con `WHERE`, que filtra filas individuales **antes** de agrupar.

**¿Por qué se escribe así y no de otra forma?**
`HAVING` existe porque `WHERE` no puede usar funciones de agregación como `COUNT` o `SUM`. La regla: `WHERE` filtra filas individuales antes de agrupar; `HAVING` filtra grupos después de agregar. Confundirlos es uno de los errores más comunes en SQL.

**Resultado esperado:**
Una tabla con una fila por categoría, mostrando el conteo, suma, promedio y máximo de ventas, ordenada de mayor a menor total.

---

## Bloque 4: Equivalencia SQL vs pandas

```python
# La misma operación escrita de dos formas equivalentes

# --- VERSIÓN SQL ---
query_sql = """
    SELECT categoría, AVG(ventas) AS promedio
    FROM ventas
    WHERE ventas > 100
    GROUP BY categoría
    HAVING AVG(ventas) > 150
    ORDER BY promedio DESC
"""
resultado_sql = pd.read_sql(query_sql, conn)

# --- VERSIÓN PANDAS (equivalente exacto) ---
resultado_pandas = (
    df[df["ventas"] > 100]                         # WHERE
    .groupby("categoría")["ventas"]                # GROUP BY
    .mean()                                        # AVG()
    .reset_index()
    .rename(columns={"ventas": "promedio"})
    .query("promedio > 150")                       # HAVING
    .sort_values("promedio", ascending=False)      # ORDER BY DESC
)

print("SQL:\n", resultado_sql)
print("\nPandas:\n", resultado_pandas.reset_index(drop=True))
```

**¿Qué hace este bloque?**
Ambos bloques producen exactamente el mismo resultado: el promedio de ventas por categoría, solo para registros con ventas > 100, mostrando solo las categorías con promedio > 150, ordenadas de mayor a menor.

**¿Por qué se escribe así y no de otra forma?**
Esta comparación directa es clave para entender la equivalencia entre paradigmas. La tabla de equivalencias es:
- `WHERE` ↔ `df[condicion]`
- `GROUP BY` ↔ `.groupby()`
- `AVG()` ↔ `.mean()`
- `HAVING` ↔ `.query()`
- `ORDER BY DESC` ↔ `.sort_values(ascending=False)`

**Resultado esperado:**
Dos DataFrames con columnas `categoría` y `promedio`, con los mismos valores (aunque posiblemente con leve diferencia de precisión decimal por redondeo interno).

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `OperationalError: no such table: ventas` | La tabla no fue creada o se usa una conexión diferente | Verificar que `df.to_sql()` se ejecutó correctamente con la misma variable `conn` |
| `OperationalError: no such column: ventas` | El nombre de la columna en SQL no coincide exactamente con el del DataFrame | Verificar nombres con `df.columns.tolist()` y usarlos exactamente igual en SQL |
| `HAVING` sin `GROUP BY` | `HAVING` requiere que haya una cláusula `GROUP BY` antes | Siempre acompañar `HAVING` con su `GROUP BY` correspondiente |
| Consulta muy lenta con muchos registros | No hay índice en las columnas usadas en `WHERE` o `JOIN` | Crear índice: `cursor.execute("CREATE INDEX idx ON ventas(categoría)")` |
| `pd.read_sql` devuelve error de tipo | Se pasó la query como bytes en lugar de string | Asegurarse de que la query sea un string de Python, no una variable de otro tipo |
