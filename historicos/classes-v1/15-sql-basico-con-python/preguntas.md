# ❓ Preguntas — Clase 15: SQL básico con Python

> Preguntas de comprensión, discusión y evaluación para consolidar esta clase.

## 🧠 Preguntas de comprensión

1. ¿Qué es SQLite y en qué se diferencia de bases de datos como MySQL o PostgreSQL? ¿Por qué es útil para aprender SQL sin instalar nada?
2. ¿Qué hace la función `pd.read_sql()` y qué dos argumentos mínimos necesita para funcionar?
3. ¿Cuál es la diferencia entre `WHERE` y `HAVING` en SQL? ¿Cuándo es obligatorio usar `HAVING` en lugar de `WHERE`?
4. ¿Para qué sirve `GROUP BY` en SQL? Explica con un ejemplo de ventas por categoría.
5. ¿Qué hace exactamente `ORDER BY columna DESC`? ¿Qué pasa si no escribes `DESC`?

## 💬 Preguntas de discusión

1. ¿Cuándo preferirías usar SQL en lugar de pandas para analizar datos? ¿Y cuándo preferirías pandas? ¿Hay situaciones donde conviene usar los dos juntos?
2. Si trabajas en una empresa con millones de registros de ventas almacenados en una base de datos, ¿por qué sería mejor filtrar con SQL en el servidor que cargar todos los datos a Python primero?
3. ¿En qué se parece `GROUP BY` de SQL al método `.groupby()` de pandas? ¿En qué difieren en sintaxis y en cuándo se calculan los resultados?

## 🧪 Preguntas de código

1. Escribe el código Python completo para crear una conexión SQLite, cargar el DataFrame `df` en una tabla llamada `ventas`, y luego ejecutar una consulta que devuelva las primeras 10 filas ordenadas por ventas de mayor a menor.
2. Escribe una consulta SQL que calcule el total y el promedio de ventas por `categoría`, mostrando solo las categorías con más de 100 registros, ordenadas por total de mayor a menor.
3. Escribe la consulta SQL equivalente a este código pandas: `df[df['precio'] > 50].groupby('ciudad')['ventas'].sum()`.

## 🎯 Pregunta integradora

Tienes una base de datos SQLite con dos tablas: `ventas` (con columnas `id`, `fecha`, `producto_id`, `cantidad`, `precio_unitario`, `ciudad`) y `productos` (con columnas `id`, `nombre`, `categoría`). Escribe las consultas SQL necesarias para responder estas tres preguntas de negocio: (1) ¿Cuál es el ingreso total por categoría de producto? (2) ¿Qué ciudad generó más ingresos este año? (3) ¿Qué productos tienen más de 50 ventas registradas? Explica el razonamiento detrás de cada consulta, incluyendo por qué usas `JOIN`, `GROUP BY` o `HAVING` en cada caso.
