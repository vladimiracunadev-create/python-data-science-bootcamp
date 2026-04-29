# 📘 Clase 15: SQL básico con Python

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo

Aprender a consultar datos usando SQL desde Python, creando una base de datos SQLite en memoria y usando `pd.read_sql()` para obtener resultados como DataFrames. Al finalizar, el estudiante podrá escribir consultas SELECT con WHERE, GROUP BY, ORDER BY y funciones de agregación, y entenderá la equivalencia entre pandas y SQL para operaciones comunes.

## ⏱️ Duración sugerida

90 minutos

## 📦 Dataset base

- `datasets/ventas_tienda.csv` (cargado en una base de datos SQLite en memoria)

## ✅ Resultados esperados

Al finalizar, el estudiante podrá:

- Explicar qué es SQL y por qué los científicos de datos lo necesitan
- Crear una base de datos SQLite en memoria desde Python y cargar datos de un CSV
- Escribir consultas SELECT básicas para leer filas y columnas
- Filtrar registros con WHERE usando condiciones simples y combinadas
- Agrupar datos con GROUP BY y aplicar funciones de agregación (COUNT, SUM, AVG, MAX, MIN)
- Ordenar resultados con ORDER BY
- Obtener resultados como DataFrame con `pd.read_sql()`
- Identificar la equivalencia entre operaciones de pandas y consultas SQL

## 🧭 Temas clave

- Qué es SQL y qué es una base de datos relacional
- Por qué los científicos de datos necesitan SQL
- Crear una base de datos SQLite en memoria con Python (`sqlite3`)
- La instrucción SELECT básica
- Filtrar filas con WHERE
- Agrupar con GROUP BY y funciones de agregación: COUNT, SUM, AVG, MAX, MIN
- Ordenar resultados con ORDER BY
- Limitar resultados con LIMIT
- Usar `pd.read_sql()` para obtener resultados como DataFrame
- Tabla comparativa: pandas vs SQL

## 🧰 Materiales del módulo

- `README.md`
- `slides.md`
- `teoria.md`
- `ejercicios.md`
- `homework.md`
- `notebook.ipynb`
- `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase

- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.
- Antes de pasar al siguiente paso, verifica que entiendes la salida.

## 💡 Idea central

SQL es el lenguaje universal para consultar bases de datos — toda base de datos empresarial se consulta así.

## 👩‍🏫 Nota para el docente

Muestra siempre el equivalente en pandas junto a cada consulta SQL. Ver la misma operación en dos lenguajes refuerza ambos. Enfatiza que en el mundo laboral los datos rara vez vienen en CSV — lo más común es conectarse a una base de datos y traer datos con SQL. El dominio de SQL es una de las habilidades más demandadas en ofertas de trabajo de datos.
