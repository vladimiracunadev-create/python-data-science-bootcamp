# 🖥️ Diapositivas sugeridas — Clase 15

> 🖥️ Guion visual breve para conducir la sesión sin sobrecargar la clase.

## 🚪 Apertura

- Presentar el objetivo y la pregunta central del módulo.
- Conectar la sesión con el recorrido general del bootcamp.
- Pregunta inicial: "Si los datos de tu empresa vivieran en miles de archivos CSV, ¿cómo los consultarías? — En la realidad, viven en bases de datos y se consultan con SQL."

## 🛤️ Ruta de la sesión

| Tramo | Tiempo sugerido | Enfoque | Evidencia |
|---|---|---|---|
| Inicio | 10 min | Activar contexto — qué es una base de datos y por qué SQL importa | Diagrama de arquitectura de datos empresariales |
| Desarrollo 1 | 20 min | Crear la BD en memoria, SELECT, WHERE | Consulta ejecutada con salida como DataFrame |
| Desarrollo 2 | 25 min | GROUP BY con agregaciones y ORDER BY | 3 preguntas de negocio respondidas con SQL |
| Práctica | 25 min | Ejercicios de consultas + comparación con pandas | Tabla pandas vs SQL completada |
| Cierre | 10 min | Síntesis y siguiente paso | Autoevaluación breve |

## 📌 Puntos que deben quedar claros

- SQL es declarativo: describes qué quieres, no cómo obtenerlo paso a paso
- Toda consulta SQL devuelve una tabla resultado
- `pd.read_sql()` es el puente entre SQL y el ecosistema pandas/Python
- GROUP BY sin función de agregación generalmente no tiene sentido
- La mayoría de los sistemas de datos del mundo (empresas, bancos, hospitales, gobierno) usan bases de datos relacionales y SQL

## 🏁 Cierre esperado

Al terminar esta clase, el estudiante puede conectarse a una base de datos SQLite, escribir consultas básicas y traer resultados a pandas. Esto cierra el ciclo de herramientas fundamentales del bootcamp: Python (bases), pandas (tablas), NumPy (cálculo), visualización (gráficas), machine learning (modelos) y ahora SQL (fuentes de datos reales).
