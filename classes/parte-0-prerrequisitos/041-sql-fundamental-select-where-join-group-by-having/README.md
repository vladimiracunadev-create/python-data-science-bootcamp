# Clase 041 — SQL fundamental: SELECT, WHERE, JOIN, GROUP BY, HAVING

> Parte: **0 — Prerrequisitos** · Fuente: *SQL for Data Scientists* (Tanimura) caps. 1-3 · SQLite docs · DuckDB docs.
> ⏱️ Duración estimada: **120 min**.

---

## 🎯 Objetivo

Que el alumno escriba consultas SQL no triviales — SELECT con filtros, JOINs (inner/left), agregaciones con GROUP BY y filtros sobre agregados con HAVING. Y entienda **el orden de ejecución lógico** (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT), que es lo que confunde a todo el mundo al principio.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Escribir SELECT** con filtros WHERE y operadores (=, <>, IN, BETWEEN, LIKE, IS NULL).
2. **Hacer JOIN** (INNER, LEFT, RIGHT, FULL) y reconocer cuándo cada uno.
3. **Agrupar y agregar** con GROUP BY + COUNT, SUM, AVG, MAX, MIN.
4. **Filtrar agregados** con HAVING (no se puede con WHERE).
5. **Recitar el orden lógico**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | SELECT, FROM, WHERE | Lo básico, sin trampa. |
| 2 | Operadores WHERE | =, <>, IN, BETWEEN, LIKE, IS NULL. |
| 3 | JOINs (inner/left/right/full) | Análogos a pandas merge. |
| 4 | GROUP BY + agregadas | COUNT/SUM/AVG/MAX/MIN. |
| 5 | HAVING vs WHERE | HAVING filtra después de GROUP BY. |
| 6 | ORDER BY, LIMIT, OFFSET | Final del pipeline. |
| 7 | Orden lógico ≠ orden escrito | El gran malentendido. |

## 📂 Dataset / recursos

SQLite en memoria con 2 tablas sintéticas: `clientes` (10 filas) y `ordenes` (30 filas). Generado en el notebook con `sqlite3` stdlib. Sin descarga.

## 🧪 Ejercicios

**1.** **SELECT básico.** Lista de clientes con país = 'ES'.

**2.** **JOIN.** Cada orden con el nombre del cliente.

**3.** **LEFT JOIN.** Todos los clientes, sumando órdenes (NaN si no tienen).

**4.** **GROUP BY + HAVING.** Clientes con más de 3 órdenes y monto total > 200.

**5.** **Orden lógico.** Explica con tus palabras por qué `WHERE total > 100` no funciona si total es `SUM(monto)` — necesitas HAVING.

## 📝 Homework verificable

Notebook con SQLite en memoria: (a) crea 2 tablas y carga datos sintéticos; (b) 5 consultas progresivas (filter, join, group, having, top-N); (c) explica el orden lógico con un ejemplo; (d) mismo ejercicio con `DuckDB` (sustituye `sqlite3.connect(':memory:')`).

**Criterio de aceptación:** Las 5 consultas producen el resultado esperado; DuckDB devuelve igual.

## 🔗 Referencias

- Tanimura, *SQL for Data Scientists*, caps. 1-3.
- [SQLite SELECT docs](https://www.sqlite.org/lang_select.html)
- [DuckDB docs](https://duckdb.org/docs/)

## ➡️ Siguiente clase

[Clase 042 — SQL avanzado: CTEs, window functions](../042-sql-avanzado-ctes-window-functions-subqueries-correlacionadas/README.md)
