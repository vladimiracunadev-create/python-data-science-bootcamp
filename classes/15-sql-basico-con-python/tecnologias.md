# 🔧 Tecnologías complementarias — Clase 15: SQL básico con Python

> Herramientas, librerías y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `sqlite3` | Módulo estándar de Python para SQLite; sin instalación adicional | Básico |
| `pandas` (read_sql) | Ejecutar consultas SQL y recibir el resultado directamente como DataFrame | Básico |
| `pandasql` | Permite escribir consultas SQL directamente sobre DataFrames de pandas | Básico |
| `SQLAlchemy` | ORM y toolkit SQL para conectar Python con cualquier motor de base de datos | Intermedio |
| `psycopg2` | Driver nativo para conectar Python con bases de datos PostgreSQL | Intermedio |
| `duckdb` | Base de datos analítica embebida, muy rápida para queries sobre DataFrames y archivos Parquet | Intermedio |
| `ibis` | Framework para escribir SQL de forma programática y portable entre motores | Avanzado |
| `sqlfluff` | Linter y formateador automático de código SQL | Intermedio |
| `mysql-connector-python` | Driver oficial para conectar Python con bases de datos MySQL | Intermedio |

## 🌐 Recursos recomendados

- **Documentación oficial**: SQLite — [sqlite.org/docs.html](https://www.sqlite.org/docs.html) — referencia completa del motor, sus tipos de datos y funciones disponibles
- **Tutorial recomendado**: SQLZoo — [sqlzoo.net](https://sqlzoo.net/) — ejercicios interactivos de SQL por niveles, desde SELECT básico hasta JOINs complejos, completamente en el navegador sin instalar nada
- **Concepto clave para buscar**: "SQL GROUP BY HAVING diferencia" / "SQL GROUP BY vs HAVING" — uno de los conceptos más confusos para principiantes y el más preguntado en entrevistas técnicas

## 🚀 Próximos pasos sugeridos

- Aprender SQL avanzado: `JOIN` (INNER, LEFT, RIGHT, FULL OUTER), subconsultas y CTEs (`WITH nombre AS (...)`)
- Explorar SQLAlchemy para conectar Python a bases de datos de producción (PostgreSQL, MySQL) sin cambiar mucho el código
- Investigar bases de datos analíticas como DuckDB que ejecutan SQL directamente sobre archivos CSV o Parquet sin crear tablas
- Aprender sobre índices en SQL: por qué aceleran enormemente las consultas con `WHERE` y `JOIN` en tablas grandes

## 🧰 Herramientas alternativas

| Herramienta | Descripción breve | Cuándo conviene usarla |
|---|---|---|
| DuckDB | Base de datos analítica embebida que ejecuta SQL sobre CSV/Parquet directamente | Análisis local rápido sobre archivos grandes sin configurar un servidor |
| PostgreSQL | Base de datos relacional robusta y gratuita con extensiones avanzadas | Aplicaciones web y APIs que necesitan una base de datos de producción |
| Google BigQuery | Data warehouse en la nube con SQL para petabytes de datos | Análisis empresarial a escala masiva con datos en Google Cloud |
| DBeaver / TablePlus | IDEs gráficos para explorar y ejecutar consultas en bases de datos | Cuando necesitas navegar visualmente la estructura de la base de datos |
