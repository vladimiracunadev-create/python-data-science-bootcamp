# Clase 043 — SQL desde Python: sqlite3, SQLAlchemy, DuckDB

> Parte: **0 — Prerrequisitos** · Fuente: Python stdlib `sqlite3` · SQLAlchemy docs · DuckDB Python docs.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno conecte Python con SQL de las 3 formas que va a encontrar en producción: `sqlite3` (stdlib, demo local), `SQLAlchemy` (ORM/engine genérico para PostgreSQL/MySQL), y `DuckDB` (columnar embebido para análisis sobre CSV/Parquet sin servidor).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Conectar y consultar** con `sqlite3` stdlib, usando placeholders `?` (NUNCA concatenar SQL).
2. **Usar SQLAlchemy `create_engine(URL)`** + `pd.read_sql` para queries a cualquier RDBMS.
3. **Usar DuckDB** para hacer SQL sobre DataFrames y CSV/Parquet directamente.
4. **Prevenir SQL injection** con queries parametrizadas.
5. **Decidir** entre sqlite/SQLAlchemy/DuckDB según el caso.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | `sqlite3` stdlib: connect, cursor, fetchall | Para demos y BDs ligeras. |
| 2 | Placeholders `?` y `:nombre` | NUNCA concatenar strings. |
| 3 | SQLAlchemy `create_engine('postgresql://...')` | Soporta todos los RDBMS. |
| 4 | `pd.read_sql` y `df.to_sql` | Pasarela pandas ↔ BD. |
| 5 | DuckDB: SQL sobre DataFrames y archivos | `duckdb.query('SELECT ... FROM df')`. |
| 6 | Cuándo cada uno | Trade-offs. |

## 📂 Dataset / recursos

Penguins descargado a CSV local para DuckDB; datos sintéticos para sqlite/SQLAlchemy.

## 🧪 Ejercicios

**1.** **sqlite3 con placeholders.** Crea tabla, inserta 5 filas usando `executemany` con tuples, consulta con `?` placeholder. Demuestra el bug si concatenas.

**2.** **`df.to_sql` y `pd.read_sql`.** Carga un DataFrame a SQLite y consulta de vuelta.

**3.** **SQLAlchemy engine.** Crea engine SQLite. Usa `pd.read_sql` con engine.

**4.** **DuckDB sobre DataFrame.** Carga penguins en df. `duckdb.query('SELECT species, AVG(body_mass_g) FROM df GROUP BY species').df()`.

**5.** **DuckDB sobre CSV.** Mismo query pero `FROM 'penguins.csv'` directo, sin cargar a pandas.

## 📝 Homework verificable

Notebook con 3 backends del mismo análisis: (a) sqlite3 stdlib + cursor; (b) SQLAlchemy engine + pd.read_sql; (c) DuckDB sobre CSV. Documenta cuándo elegirías cada uno. Demuestra explícitamente el peligro de SQL injection con concatenación vs placeholders.

**Criterio de aceptación:** Las 3 versiones devuelven el mismo resultado. Demo de injection sin daño real.

## 🔗 Referencias

- [Python `sqlite3` docs](https://docs.python.org/3/library/sqlite3.html)
- [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)
- [DuckDB Python API](https://duckdb.org/docs/api/python/overview)
- [OWASP — SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

## ➡️ Siguiente clase

[Clase 044 — NoSQL: MongoDB con pymongo](../044-nosql-mongodb-con-pymongo/README.md)
