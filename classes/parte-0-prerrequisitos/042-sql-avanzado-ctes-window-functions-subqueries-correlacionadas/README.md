# Clase 042 — SQL avanzado: CTEs, window functions, subqueries correlacionadas

> Parte: **0 — Prerrequisitos** · Fuente: Tanimura, *SQL for Data Scientists* caps. 4-5 · PostgreSQL docs (window functions).
> ⏱️ Duración estimada: **120 min**.

---

## 🎯 Objetivo

Que el alumno escriba SQL legible y potente: **CTEs** (`WITH`) para descomponer queries complejas, **window functions** (`OVER`) para rankings/totales corridos/lag/lead sin perder filas, y **subqueries correlacionadas** cuando aportan.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Escribir CTEs** con `WITH name AS (...)` para mejorar legibilidad.
2. **Encadenar múltiples CTEs**: `WITH a AS (...), b AS (...) SELECT ...`.
3. **Aplicar window functions**: `ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER (PARTITION BY ... ORDER BY ...)`.
4. **Calcular ranking** por grupo con `ROW_NUMBER() OVER (PARTITION BY ...)`.
5. **Diferenciar** subquery (independiente) vs correlacionada (depende de la outer).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | CTEs: `WITH name AS (...)` | Descomponer queries largas. |
| 2 | Múltiples CTEs encadenadas | Pipeline legible. |
| 3 | Recursive CTEs | Jerarquías, grafos. |
| 4 | Window functions: `OVER (PARTITION BY ... ORDER BY ...)` | Agregar sin colapsar filas. |
| 5 | `ROW_NUMBER`, `RANK`, `DENSE_RANK` | Diferencias sutiles. |
| 6 | `LAG`, `LEAD`: comparar con fila anterior/siguiente | Series temporales. |
| 7 | Subqueries correlacionadas | Cuando la subquery depende de la outer. |

## 📂 Dataset / recursos

SQLite con `ordenes` (cliente_id, fecha, monto) de clase 041 — extendido. Sin descarga.

## 🧪 Ejercicios

**1.** **CTE básica.** Reescribe una query con subquery anidada usando `WITH`.

**2.** **ROW_NUMBER por grupo.** Top-1 orden por cliente (mayor monto).

**3.** **Total corrido.** `SUM(monto) OVER (PARTITION BY cliente_id ORDER BY fecha)` — total acumulado por cliente.

**4.** **LAG.** Por cliente, diferencia entre el monto actual y el anterior.

**5.** **Recursive CTE.** Genera serie de fechas día a día desde 2024-01-01 a 2024-01-31.

## 📝 Homework verificable

Notebook: (a) 3 versiones de la misma query (anidada → CTE → CTEs múltiples) comparando legibilidad; (b) top-3 órdenes por cliente con `ROW_NUMBER`; (c) total corrido y delta vs orden anterior; (d) recursive CTE para calendario diario.

**Criterio de aceptación:** Las 3 versiones devuelven exactamente el mismo resultado. Window functions sin error.

## 🔗 Referencias

- Tanimura, *SQL for Data Scientists*, caps. 4-5.
- [PostgreSQL window functions tutorial](https://www.postgresql.org/docs/current/tutorial-window.html)
- [Modern SQL — CTEs](https://modern-sql.com/feature/with)

## ➡️ Siguiente clase

[Clase 043 — SQL desde Python (sqlite3, SQLAlchemy, DuckDB)](../043-sql-desde-python-sqlite3-sqlalchemy-duckdb/README.md)
