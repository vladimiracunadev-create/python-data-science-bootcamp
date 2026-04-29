# 🧠 Documento teórico — Clase 15: SQL básico con Python

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

SQL es el lenguaje universal para consultar bases de datos — toda base de datos empresarial se consulta así.

## ❓ Por qué importa este módulo

Los datos del mundo real rara vez vienen en archivos CSV listos para analizar. Viven en bases de datos relacionales: sistemas como MySQL, PostgreSQL, SQL Server u Oracle que almacenan millones de registros de forma estructurada y eficiente. Para acceder a esos datos, la herramienta universal es SQL. No importa el sistema: la sintaxis básica es la misma en todos. Este módulo te da ese lenguaje común.

## 📖 ¿Qué es SQL?

SQL (Structured Query Language) es un lenguaje declarativo diseñado para consultar y manipular datos en bases de datos relacionales. "Declarativo" significa que describes **qué** quieres obtener, no **cómo** conseguirlo paso a paso — el motor de base de datos elige la forma más eficiente de ejecutar tu consulta.

Una base de datos relacional organiza los datos en **tablas** (similares a hojas de cálculo) que pueden relacionarse entre sí mediante llaves.

## 🏗️ Estructura básica de una consulta SQL

```sql
SELECT columnas
FROM tabla
WHERE condición
GROUP BY columnas_de_agrupación
ORDER BY columna_de_orden
LIMIT número_de_filas
```

Cada cláusula es opcional excepto `SELECT` y `FROM`. El motor ejecuta internamente en este orden: FROM → WHERE → GROUP BY → SELECT → ORDER BY → LIMIT.

## 💻 Bloque de código documentado

### Crear una base de datos SQLite en memoria con Python

**Qué hace:** crea una base de datos temporal en RAM, carga datos de un CSV y la deja lista para consultas.

**Para qué sirve:** practicar SQL sin instalar un servidor de base de datos; SQLite es perfecto para aprender y para proyectos pequeños.

```python
import sqlite3
import pandas as pd

# Cargamos el dataset con pandas
df = pd.read_csv("datasets/ventas_tienda.csv")

# Creamos una conexión a una base de datos en memoria
# ":memory:" significa que la BD existe solo en RAM — no se guarda en disco
conn = sqlite3.connect(":memory:")

# Volcamos el DataFrame en la BD como una tabla llamada "ventas"
# if_exists="replace" sobreescribe la tabla si ya existía
df.to_sql("ventas", conn, if_exists="replace", index=False)

print("Base de datos creada con la tabla 'ventas'")
print(f"Registros cargados: {len(df)}")
```

### SELECT básico — leer columnas y filas

**Qué hace:** recupera datos de la tabla.

**Para qué sirve:** es la consulta más básica; todo análisis empieza seleccionando las columnas relevantes.

```python
# Seleccionar todas las columnas de las primeras 5 filas
query = """
    SELECT *
    FROM ventas
    LIMIT 5
"""
resultado = pd.read_sql(query, conn)
print(resultado)

# Seleccionar solo columnas específicas
query = """
    SELECT producto, precio_unitario, unidades
    FROM ventas
    LIMIT 10
"""
resultado = pd.read_sql(query, conn)
print(resultado)
```

### WHERE — filtrar filas por condición

**Qué hace:** devuelve solo las filas que cumplen la condición especificada.

**Para qué sirve:** equivalente a `df[df['columna'] > valor]` en pandas.

```python
# Ventas con precio mayor a 50
query = """
    SELECT producto, precio_unitario, unidades
    FROM ventas
    WHERE precio_unitario > 50
    ORDER BY precio_unitario DESC
"""
resultado = pd.read_sql(query, conn)
print(resultado)

# Combinar condiciones con AND / OR
query = """
    SELECT *
    FROM ventas
    WHERE precio_unitario > 20
      AND unidades >= 10
"""
resultado = pd.read_sql(query, conn)
print(f"Registros que cumplen la condición: {len(resultado)}")
```

### GROUP BY con funciones de agregación

**Qué hace:** agrupa filas por una columna y aplica una función de resumen a cada grupo.

**Para qué sirve:** equivalente a `df.groupby('columna').agg(...)` en pandas; responde preguntas como "¿cuánto vendimos por categoría?".

```python
# Total de ventas por categoría
query = """
    SELECT
        categoria,
        COUNT(*)            AS cantidad_registros,
        SUM(unidades)       AS total_unidades,
        AVG(precio_unitario) AS precio_promedio,
        MAX(precio_unitario) AS precio_maximo
    FROM ventas
    GROUP BY categoria
    ORDER BY total_unidades DESC
"""
resultado = pd.read_sql(query, conn)
print(resultado)
```

### ORDER BY y LIMIT — ordenar y paginar resultados

**Qué hace:** ordena el resultado y limita cuántas filas se devuelven.

**Para qué sirve:** encontrar el top N, los más recientes, los más vendidos — sin traer toda la tabla.

```python
# Top 5 productos por precio unitario
query = """
    SELECT producto, precio_unitario
    FROM ventas
    ORDER BY precio_unitario DESC
    LIMIT 5
"""
resultado = pd.read_sql(query, conn)
print(resultado)
```

## 📊 Tabla comparativa: pandas vs SQL

| Operación | pandas | SQL |
|---|---|---|
| Leer todas las filas | `df` | `SELECT * FROM tabla` |
| Seleccionar columnas | `df[['col1', 'col2']]` | `SELECT col1, col2 FROM tabla` |
| Filtrar filas | `df[df['col'] > valor]` | `WHERE col > valor` |
| Agrupar y sumar | `df.groupby('col')['val'].sum()` | `GROUP BY col` + `SUM(val)` |
| Ordenar | `df.sort_values('col', ascending=False)` | `ORDER BY col DESC` |
| Primeras N filas | `df.head(5)` | `LIMIT 5` |
| Contar registros | `len(df)` | `SELECT COUNT(*) FROM tabla` |

## ⚠️ Errores frecuentes a vigilar

- **GROUP BY sin función de agregación**: si seleccionas una columna no agrupada sin agregarla (SUM, AVG, etc.), obtendrás un error o resultados inesperados
- **Confundir WHERE con HAVING**: WHERE filtra filas **antes** de agrupar; HAVING filtra grupos **después** de GROUP BY
- **Nombres de columnas sensibles a mayúsculas**: en SQLite los nombres de columna no distinguen mayúsculas, pero en otros motores sí
- **Olvidar cerrar la conexión**: `conn.close()` libera los recursos; en scripts largos es buena práctica

## 🔗 Conexión con el siguiente módulo

Con SQL, NumPy y pandas dominados, tienes todas las herramientas para recolectar, limpiar y explorar datos. El siguiente paso natural es volver al ciclo CRISP-DM: con datos bien preparados, puedes construir modelos de machine learning más robustos y conectar cada técnica al problema de negocio que la origina.
