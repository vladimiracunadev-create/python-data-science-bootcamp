# 🧪 Ejercicios — Clase 15

> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar

- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.
- Explica qué hace cada transformación relevante y para qué sirve.

## 🧭 Trabajo guiado

### Configuración inicial (ejecutar primero)

```python
import sqlite3
import pandas as pd

# Cargar el dataset y crear la base de datos en memoria
df = pd.read_csv("../../datasets/ventas_tienda.csv")
conn = sqlite3.connect(":memory:")
df.to_sql("ventas", conn, if_exists="replace", index=False)
print("Base de datos lista. Registros cargados:", len(df))
```

### Ejercicio 1: SELECT básico

Usando `pd.read_sql()` y la conexión `conn`, escribe consultas SQL que respondan:

a) Muestra las primeras 10 filas de la tabla, con todas las columnas
b) Selecciona solo las columnas `producto`, `precio_unitario` y `unidades` para los primeros 15 registros
c) Cuenta el total de registros en la tabla con `SELECT COUNT(*) FROM ventas`
d) Muestra todos los valores únicos de la columna `categoria` usando `SELECT DISTINCT`

### Ejercicio 2: WHERE — filtrar con condiciones

Escribe consultas SQL que devuelvan:

a) Todos los registros donde `precio_unitario` sea mayor a 40
b) Todos los registros donde `unidades` sea menor o igual a 5
c) Registros donde `precio_unitario` esté entre 20 y 60 (usa `BETWEEN 20 AND 60`)
d) Registros de una categoría específica (elige cualquier categoría que exista en tus datos)
e) Registros con `precio_unitario > 30` **Y** `unidades > 8` (usa AND)

Para cada consulta, imprime cuántos registros devuelve con `len(resultado)`.

### Ejercicio 3: GROUP BY — preguntas de negocio

Escribe consultas SQL que respondan estas preguntas de negocio:

a) ¿Cuántos registros hay por categoría? (usa `COUNT(*)`)
b) ¿Cuál es el precio promedio por categoría? (usa `AVG`)
c) ¿Cuántas unidades totales se vendieron por categoría? (usa `SUM`)
d) ¿Cuál es el precio máximo y mínimo por categoría? (usa `MAX` y `MIN`)
e) Muestra las categorías ordenadas de mayor a menor por suma de unidades

### Ejercicio 4: Comparación pandas vs SQL

Para cada una de estas operaciones, escribe **primero la versión pandas** y **luego la versión SQL** que produzcan el mismo resultado:

a) Filtrar registros donde `precio_unitario > 50`
b) Calcular el promedio de `precio_unitario` por `categoria`
c) Ordenar todos los registros por `precio_unitario` de mayor a menor y mostrar los 5 primeros

Compara los resultados de ambas versiones para verificar que son equivalentes.

### Ejercicio 5 (desafío): Consulta combinada

Escribe una sola consulta SQL que:
- Agrupe por `categoria`
- Calcule: total de unidades, promedio de precio unitario, y total de ingresos (`SUM(precio_unitario * unidades)`)
- Filtre solo las categorías con más de 5 registros (pista: esto requiere `HAVING COUNT(*) > 5`)
- Ordene el resultado por total de ingresos de mayor a menor

> `HAVING` es como `WHERE` pero se aplica **después** de agrupar.

## ✅ Criterios de autocorrección

- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
- Las versiones pandas y SQL del ejercicio 4 producen resultados equivalentes.
- La consulta del ejercicio 5 usa GROUP BY, una función de agregación para el filtro HAVING, y ORDER BY.
