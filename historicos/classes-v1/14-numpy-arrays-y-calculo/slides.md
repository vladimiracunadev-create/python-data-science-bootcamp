# 🖥️ Diapositivas sugeridas — Clase 14

> 🖥️ Guion visual breve para conducir la sesión sin sobrecargar la clase.

## 🚪 Apertura

- Presentar el objetivo y la pregunta central del módulo.
- Conectar la sesión con el recorrido general del bootcamp.
- Pregunta inicial: "Si tienes que sumar 1 millón de números, ¿lo harías uno por uno o todos a la vez?"

## 🛤️ Ruta de la sesión

| Tramo | Tiempo sugerido | Enfoque | Evidencia |
|---|---|---|---|
| Inicio | 10 min | Activar contexto — velocidad de listas vs arrays | Demo de tiempo de ejecución en vivo |
| Desarrollo 1 | 20 min | Crear arrays, ver propiedades, indexar y hacer slicing | Primer bloque ejecutado con salida comentada |
| Desarrollo 2 | 25 min | Operaciones vectorizadas y funciones estadísticas | Cálculos sobre columnas de ventas_tienda.csv |
| Práctica | 25 min | Ejercicios de filtrado, reshaping y cálculos combinados | Entregable: respuestas a 3 preguntas con arrays |
| Cierre | 10 min | Síntesis y conexión con pandas y scikit-learn | Autoevaluación breve |

## 📌 Puntos que deben quedar claros

- Un array NumPy es una colección de elementos del mismo tipo almacenados de forma continua en memoria
- Las operaciones vectorizadas aplican la misma operación a todos los elementos sin escribir un bucle
- `shape` describe las dimensiones del array: `(filas, columnas)` para arrays 2D
- El boolean indexing permite filtrar elementos que cumplen una condición, igual que WHERE en SQL
- Las columnas de un DataFrame de pandas son internamente arrays NumPy — por eso son rápidas

## 🏁 Cierre esperado

Al terminar esta clase, el estudiante comprende por qué NumPy existe y cómo se relaciona con pandas. La clase 15 introduce SQL con Python, donde verán que muchas operaciones de agrupación que hacemos con pandas o NumPy también se pueden hacer con una sola consulta SQL.
