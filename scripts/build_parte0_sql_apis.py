"""Classes 041-046 — SQL + NoSQL + APIs + scraping."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="041-sql-fundamental-select-where-join-group-by-having",
    number="041",
    title="SQL fundamental: SELECT, WHERE, JOIN, GROUP BY, HAVING",
    duration="120 min",
    source="*SQL for Data Scientists* (Tanimura) caps. 1-3 · SQLite docs · DuckDB docs.",
    objetivo=(
        "Que el alumno escriba consultas SQL no triviales — SELECT con filtros, JOINs (inner/left), "
        "agregaciones con GROUP BY y filtros sobre agregados con HAVING. Y entienda **el orden de "
        "ejecución lógico** (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT), que es "
        "lo que confunde a todo el mundo al principio."
    ),
    resultados=[
        "**Escribir SELECT** con filtros WHERE y operadores (=, <>, IN, BETWEEN, LIKE, IS NULL).",
        "**Hacer JOIN** (INNER, LEFT, RIGHT, FULL) y reconocer cuándo cada uno.",
        "**Agrupar y agregar** con GROUP BY + COUNT, SUM, AVG, MAX, MIN.",
        "**Filtrar agregados** con HAVING (no se puede con WHERE).",
        "**Recitar el orden lógico**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.",
    ],
    temas=[
        ("SELECT, FROM, WHERE", "Lo básico, sin trampa."),
        ("Operadores WHERE", "=, <>, IN, BETWEEN, LIKE, IS NULL."),
        ("JOINs (inner/left/right/full)", "Análogos a pandas merge."),
        ("GROUP BY + agregadas", "COUNT/SUM/AVG/MAX/MIN."),
        ("HAVING vs WHERE", "HAVING filtra después de GROUP BY."),
        ("ORDER BY, LIMIT, OFFSET", "Final del pipeline."),
        ("Orden lógico ≠ orden escrito", "El gran malentendido."),
    ],
    dataset=(
        "SQLite en memoria con 2 tablas sintéticas: `clientes` (10 filas) y `ordenes` (30 filas). "
        "Generado en el notebook con `sqlite3` stdlib. Sin descarga."
    ),
    ejercicios=[
        "**SELECT básico.** Lista de clientes con país = 'ES'.",
        "**JOIN.** Cada orden con el nombre del cliente.",
        "**LEFT JOIN.** Todos los clientes, sumando órdenes (NaN si no tienen).",
        "**GROUP BY + HAVING.** Clientes con más de 3 órdenes y monto total > 200.",
        "**Orden lógico.** Explica con tus palabras por qué `WHERE total > 100` no funciona si total es `SUM(monto)` — necesitas HAVING.",
    ],
    homework=(
        "Notebook con SQLite en memoria: (a) crea 2 tablas y carga datos sintéticos; "
        "(b) 5 consultas progresivas (filter, join, group, having, top-N); (c) explica el orden "
        "lógico con un ejemplo; (d) mismo ejercicio con `DuckDB` (sustituye `sqlite3.connect(':memory:')`)."
    ),
    homework_criterio="Las 5 consultas producen el resultado esperado; DuckDB devuelve igual.",
    referencias=[
        "Tanimura, *SQL for Data Scientists*, caps. 1-3.",
        "[SQLite SELECT docs](https://www.sqlite.org/lang_select.html)",
        "[DuckDB docs](https://duckdb.org/docs/)",
    ],
    siguiente=("042-sql-avanzado-ctes-window-functions-subqueries-correlacionadas", "SQL avanzado: CTEs, window functions"),
    cells=[
        Cell("md", "# Clase 041 — SQL fundamental\n\n**Parte 0** · Tanimura caps. 1-3.\n\n> 🎯 SELECT/WHERE/JOIN/GROUP BY/HAVING + orden lógico de ejecución.\n\n> ⏱️ ~120 min"),
        Cell("md", "## ⚙️ Setup — SQLite en memoria"),
        Cell("code", "import sqlite3\nimport pandas as pd\n\ncon = sqlite3.connect(':memory:')\ncon.executescript('''\nCREATE TABLE clientes (\n    cliente_id INTEGER PRIMARY KEY,\n    nombre TEXT NOT NULL,\n    pais TEXT,\n    plan TEXT\n);\nCREATE TABLE ordenes (\n    orden_id INTEGER PRIMARY KEY,\n    cliente_id INTEGER REFERENCES clientes(cliente_id),\n    fecha DATE,\n    monto REAL\n);\n\nINSERT INTO clientes (nombre, pais, plan) VALUES\n    ('Ana',  'ES', 'pro'),\n    ('Bob',  'ES', 'free'),\n    ('Cris', 'CL', 'pro'),\n    ('Dan',  'MX', 'free'),\n    ('Eli',  'ES', 'pro');\n\nINSERT INTO ordenes (cliente_id, fecha, monto) VALUES\n    (1, '2024-01-15', 120),\n    (1, '2024-02-20',  80),\n    (1, '2024-03-12', 150),\n    (1, '2024-04-05',  60),\n    (2, '2024-02-10',  40),\n    (3, '2024-01-22', 200),\n    (3, '2024-03-15', 180),\n    (5, '2024-02-28', 300),\n    (5, '2024-03-22',  90);\n''')\nprint('OK')"),
        Cell("md", "## 1️⃣ SELECT + WHERE\n\nOperadores típicos: `=`, `<>` (distinto), `IN`, `BETWEEN`, `LIKE` (con wildcards `%` y `_`), `IS NULL`."),
        Cell("code", "q = '''\nSELECT cliente_id, nombre, plan\nFROM clientes\nWHERE pais = 'ES' AND plan = 'pro'\n'''\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 2️⃣ JOIN — inner y left"),
        Cell("code", "# INNER: solo clientes con orden\nq = '''\nSELECT c.nombre, o.fecha, o.monto\nFROM clientes c\nINNER JOIN ordenes o ON c.cliente_id = o.cliente_id\nORDER BY o.fecha\nLIMIT 5\n'''\nprint('INNER:')\nprint(pd.read_sql(q, con))\n\n# LEFT: TODOS los clientes (incl. los sin orden)\nq = '''\nSELECT c.nombre, COUNT(o.orden_id) AS n_ordenes\nFROM clientes c\nLEFT JOIN ordenes o ON c.cliente_id = o.cliente_id\nGROUP BY c.cliente_id, c.nombre\nORDER BY n_ordenes DESC\n'''\nprint('\\nLEFT + GROUP:')\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 3️⃣ GROUP BY + agregadas"),
        Cell("code", "q = '''\nSELECT c.pais,\n       COUNT(DISTINCT c.cliente_id) AS n_clientes,\n       COUNT(o.orden_id)             AS n_ordenes,\n       ROUND(SUM(o.monto), 2)         AS total_monto,\n       ROUND(AVG(o.monto), 2)         AS monto_medio\nFROM clientes c\nLEFT JOIN ordenes o ON c.cliente_id = o.cliente_id\nGROUP BY c.pais\nORDER BY total_monto DESC\n'''\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 4️⃣ HAVING — filtrar agregados\n\n**WHERE** filtra **antes** de agrupar (rows individuales).  \n**HAVING** filtra **después** de agrupar (grupos)."),
        Cell("code", "q = '''\nSELECT c.cliente_id, c.nombre,\n       COUNT(o.orden_id) AS n_ord,\n       SUM(o.monto)      AS total\nFROM clientes c\nINNER JOIN ordenes o ON c.cliente_id = o.cliente_id\nGROUP BY c.cliente_id, c.nombre\nHAVING COUNT(o.orden_id) >= 2 AND SUM(o.monto) > 200\nORDER BY total DESC\n'''\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 5️⃣ Orden lógico de ejecución\n\nEscribimos:\n```sql\nSELECT col, AGG(otra)\nFROM tabla\nWHERE cond\nGROUP BY col\nHAVING AGG(otra) > 100\nORDER BY col\nLIMIT 10\n```\n\nPero SQL **ejecuta en este orden** (es lo que importa para entender errores):\n\n```\n1. FROM       ← lee las tablas\n2. WHERE      ← filtra filas individuales\n3. GROUP BY   ← agrupa\n4. HAVING     ← filtra grupos\n5. SELECT     ← calcula expresiones del select\n6. ORDER BY   ← ordena\n7. LIMIT      ← corta\n```\n\nPor eso `WHERE SUM(...)` da error: WHERE corre **antes** de GROUP BY, no hay agregado todavía. Usa HAVING."),
        Cell("md", "## 6️⃣ DuckDB — drop-in con superpoderes\n\n```python\nimport duckdb\ncon = duckdb.connect(':memory:')\ncon.execute(\"CREATE TABLE clientes AS SELECT * FROM 'clientes.csv'\")\n# Soporta SQL estándar moderno + window functions + lee CSV/Parquet directo\n```\n\nDuckDB es como SQLite pero pensado para análisis (columnar, vectorizado). Lo verás en clase 043."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Escribo SELECT con WHERE, operadores variados\n- [ ] Hago INNER y LEFT JOIN según el caso\n- [ ] Uso GROUP BY + agregadas (COUNT/SUM/AVG)\n- [ ] Sé cuándo HAVING (no WHERE) sobre agregados\n- [ ] Recito el orden lógico FROM→WHERE→GROUP→HAVING→SELECT→ORDER→LIMIT"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. SQLite en memoria, 5 consultas progresivas, mismo en DuckDB."),
        Cell("md", "## 🔗 Referencias\n\n- Tanimura, *SQL for Data Scientists*\n- [SQLite SELECT](https://www.sqlite.org/lang_select.html)\n- [DuckDB](https://duckdb.org/docs/)\n\n➡️ **Siguiente:** [042 — SQL avanzado](../042-sql-avanzado-ctes-window-functions-subqueries-correlacionadas/README.md)"),
    ],
    definiciones=[
        ("SQL (Structured Query Language)", "Lenguaje declarativo para bases de datos relacionales. Describes **qué** quieres (no cómo) y el motor lo ejecuta. Estandarizado pero con dialectos (SQLite, PostgreSQL, MySQL, BigQuery)."),
        ("Orden lógico vs escrito", "**Escribes**: SELECT-FROM-WHERE-GROUP-HAVING-ORDER. **Ejecuta**: FROM-WHERE-GROUP-HAVING-SELECT-ORDER-LIMIT. Por eso `WHERE SUM(...)` falla (aún no agrupado) — usa HAVING."),
        ("JOIN", "Combina filas de 2+ tablas por una key. Tipos: INNER (intersección), LEFT (todo left + match right), RIGHT (espejo), FULL OUTER (todo unión), CROSS (producto cartesiano)."),
        ("GROUP BY + HAVING", "**GROUP BY**: agrupa filas por valor(es). **HAVING**: filtra los **grupos** después de agregar (no se puede con WHERE)."),
        ("Funciones de agregación", "Operan sobre grupos: `COUNT(*)`, `COUNT(DISTINCT x)`, `SUM`, `AVG`, `MIN`, `MAX`, `STDDEV`. Devuelven UN valor por grupo."),
        ("DuckDB", "Motor SQL embebido (como SQLite) pero **columnar** y optimizado para analytics. Lee CSV/Parquet directo (`FROM 'file.csv'`). Drop-in para queries analíticas, mucho más rápido que SQLite en agregados."),
    ],
    errores_comunes=[
        ("`column \"x\" must appear in GROUP BY clause or be used in an aggregate function`", "Seleccionaste col no agregada ni en GROUP BY. **Fix**: añade a GROUP BY, o agrega con `MAX(x)`, `MIN(x)` (cuando da igual)."),
        ("`WHERE SUM(monto) > 100` falla", "WHERE corre ANTES de GROUP. **Fix**: usa `HAVING SUM(monto) > 100`."),
        ("INNER JOIN pierde filas que esperaba ver", "La key no matchea (NULL, tipos, espacios). **Fix**: LEFT JOIN + `WHERE r.id IS NULL` para diagnóstico."),
        ("`COUNT(col)` devuelve menos que `COUNT(*)`", "`COUNT(col)` ignora NULL en esa columna. **Fix**: si quieres todas las filas, `COUNT(*)`."),
        ("`SELECT *` después de JOIN trae cols duplicadas con mismo nombre", "Ambas tablas tienen `id`. **Fix**: aliasea: `SELECT c.id AS cliente_id, o.id AS orden_id`."),
    ],
    faq=[
        ("¿`COUNT(*)` o `COUNT(1)`?",
         "**Equivalentes** en motores modernos (parser optimiza). `COUNT(*)` es más legible — úsalo."),
        ("¿Cuándo `DISTINCT`?",
         "Cuando hay filas duplicadas que no deberían contarse. **Cuidado**: en SELECT con muchas cols puede ser caro. Mejor agrupa con GROUP BY si vas a agregar después."),
        ("¿`UNION` o `UNION ALL`?",
         "**`UNION`** quita duplicados (más caro). **`UNION ALL`** mantiene todo (más rápido). Usa ALL si sabes que no hay duplicados (más común)."),
        ("¿SQLite o PostgreSQL para aprender?",
         "**SQLite** para arrancar (sin servidor, 1 archivo). El SQL es 90% igual. Migras a PostgreSQL cuando necesites: tipos avanzados, concurrencia, escala, JSON nativo."),
        ("¿Cómo trato fechas en SQL?",
         "Cada motor su dialecto. SQLite: strings ISO `'2024-01-15'` + `date()`, `strftime()`. PostgreSQL: tipo `DATE`/`TIMESTAMP` nativo. Estándar: `DATE '2024-01-15'`."),
    ],
))


SPECS.append(ClassSpec(
    folder="042-sql-avanzado-ctes-window-functions-subqueries-correlacionadas",
    number="042",
    title="SQL avanzado: CTEs, window functions, subqueries correlacionadas",
    duration="120 min",
    source="Tanimura, *SQL for Data Scientists* caps. 4-5 · PostgreSQL docs (window functions).",
    objetivo=(
        "Que el alumno escriba SQL legible y potente: **CTEs** (`WITH`) para descomponer queries "
        "complejas, **window functions** (`OVER`) para rankings/totales corridos/lag/lead sin "
        "perder filas, y **subqueries correlacionadas** cuando aportan."
    ),
    resultados=[
        "**Escribir CTEs** con `WITH name AS (...)` para mejorar legibilidad.",
        "**Encadenar múltiples CTEs**: `WITH a AS (...), b AS (...) SELECT ...`.",
        "**Aplicar window functions**: `ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER (PARTITION BY ... ORDER BY ...)`.",
        "**Calcular ranking** por grupo con `ROW_NUMBER() OVER (PARTITION BY ...)`.",
        "**Diferenciar** subquery (independiente) vs correlacionada (depende de la outer).",
    ],
    temas=[
        ("CTEs: `WITH name AS (...)`", "Descomponer queries largas."),
        ("Múltiples CTEs encadenadas", "Pipeline legible."),
        ("Recursive CTEs", "Jerarquías, grafos."),
        ("Window functions: `OVER (PARTITION BY ... ORDER BY ...)`", "Agregar sin colapsar filas."),
        ("`ROW_NUMBER`, `RANK`, `DENSE_RANK`", "Diferencias sutiles."),
        ("`LAG`, `LEAD`: comparar con fila anterior/siguiente", "Series temporales."),
        ("Subqueries correlacionadas", "Cuando la subquery depende de la outer."),
    ],
    dataset="SQLite con `ordenes` (cliente_id, fecha, monto) de clase 041 — extendido. Sin descarga.",
    ejercicios=[
        "**CTE básica.** Reescribe una query con subquery anidada usando `WITH`.",
        "**ROW_NUMBER por grupo.** Top-1 orden por cliente (mayor monto).",
        "**Total corrido.** `SUM(monto) OVER (PARTITION BY cliente_id ORDER BY fecha)` — total acumulado por cliente.",
        "**LAG.** Por cliente, diferencia entre el monto actual y el anterior.",
        "**Recursive CTE.** Genera serie de fechas día a día desde 2024-01-01 a 2024-01-31.",
    ],
    homework=(
        "Notebook: (a) 3 versiones de la misma query (anidada → CTE → CTEs múltiples) comparando "
        "legibilidad; (b) top-3 órdenes por cliente con `ROW_NUMBER`; (c) total corrido y "
        "delta vs orden anterior; (d) recursive CTE para calendario diario."
    ),
    homework_criterio="Las 3 versiones devuelven exactamente el mismo resultado. Window functions sin error.",
    referencias=[
        "Tanimura, *SQL for Data Scientists*, caps. 4-5.",
        "[PostgreSQL window functions tutorial](https://www.postgresql.org/docs/current/tutorial-window.html)",
        "[Modern SQL — CTEs](https://modern-sql.com/feature/with)",
    ],
    siguiente=("043-sql-desde-python-sqlite3-sqlalchemy-duckdb", "SQL desde Python (sqlite3, SQLAlchemy, DuckDB)"),
    cells=[
        Cell("md", "# Clase 042 — SQL avanzado\n\n**Parte 0** · Tanimura caps. 4-5.\n\n> 🎯 CTEs (WITH), window functions (OVER), subqueries correlacionadas.\n\n> ⏱️ ~120 min"),
        Cell("md", "## ⚙️ Setup — reutilizamos la BD de clase 041"),
        Cell("code", "import sqlite3\nimport pandas as pd\n\ncon = sqlite3.connect(':memory:')\ncon.executescript('''\nCREATE TABLE ordenes (\n    orden_id INTEGER PRIMARY KEY,\n    cliente_id INTEGER,\n    fecha DATE,\n    monto REAL\n);\nINSERT INTO ordenes (cliente_id, fecha, monto) VALUES\n    (1, '2024-01-15', 120),(1, '2024-02-20',  80),(1, '2024-03-12', 150),(1, '2024-04-05',  60),\n    (2, '2024-02-10',  40),(2, '2024-03-15',  70),(2, '2024-04-22',  50),\n    (3, '2024-01-22', 200),(3, '2024-03-15', 180),(3, '2024-04-01', 220),\n    (5, '2024-02-28', 300),(5, '2024-03-22',  90),(5, '2024-04-15', 400);\n''')"),
        Cell("md", "## 1️⃣ CTEs (`WITH`) — descomponer queries\n\nUna CTE es una \"vista temporal\" del scope de la query. Hace queries complejas legibles."),
        Cell("code", "# Sin CTE (anidado) — ilegible\nq_nested = '''\nSELECT pais, AVG(monto_cliente) AS avg_por_cliente\nFROM (\n    SELECT cliente_id, 'ES' AS pais, SUM(monto) AS monto_cliente\n    FROM ordenes\n    GROUP BY cliente_id\n)\nGROUP BY pais\n'''\n\n# Con CTE — paso a paso\nq_cte = '''\nWITH total_por_cliente AS (\n    SELECT cliente_id, SUM(monto) AS monto\n    FROM ordenes\n    GROUP BY cliente_id\n)\nSELECT cliente_id, monto\nFROM total_por_cliente\nORDER BY monto DESC\n'''\nprint(pd.read_sql(q_cte, con))"),
        Cell("md", "## 2️⃣ Múltiples CTEs encadenadas\n\nPipeline legible: cada paso es una CTE con nombre:"),
        Cell("code", "q = '''\nWITH\nmonto_por_cliente AS (\n    SELECT cliente_id, SUM(monto) AS total\n    FROM ordenes\n    GROUP BY cliente_id\n),\nranking AS (\n    SELECT cliente_id, total,\n           ROW_NUMBER() OVER (ORDER BY total DESC) AS rnk\n    FROM monto_por_cliente\n)\nSELECT * FROM ranking WHERE rnk <= 3\n'''\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 3️⃣ Window functions — el superpoder\n\n```\nFUNC() OVER (\n    PARTITION BY grupo      -- (opcional) recalcula por cada grupo\n    ORDER BY columna        -- (opcional) define el orden\n    ROWS BETWEEN x AND y    -- (opcional) ventana móvil\n)\n```\n\nNo colapsa filas como `GROUP BY` — agrega información manteniendo cada fila."),
        Cell("code", "# Top-1 orden por cliente (mayor monto)\nq = '''\nWITH ranked AS (\n    SELECT cliente_id, fecha, monto,\n           ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY monto DESC) AS rnk\n    FROM ordenes\n)\nSELECT cliente_id, fecha, monto FROM ranked WHERE rnk = 1\n'''\nprint('Top-1 orden por cliente:')\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 4️⃣ Total corrido — `SUM() OVER (PARTITION BY ... ORDER BY ...)`"),
        Cell("code", "q = '''\nSELECT cliente_id, fecha, monto,\n       SUM(monto) OVER (PARTITION BY cliente_id ORDER BY fecha) AS total_corrido\nFROM ordenes\nORDER BY cliente_id, fecha\n'''\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 5️⃣ `LAG` / `LEAD` — comparar con fila anterior/siguiente"),
        Cell("code", "q = '''\nSELECT cliente_id, fecha, monto,\n       LAG(monto)  OVER (PARTITION BY cliente_id ORDER BY fecha) AS monto_prev,\n       monto - LAG(monto) OVER (PARTITION BY cliente_id ORDER BY fecha) AS delta\nFROM ordenes\nORDER BY cliente_id, fecha\n'''\nprint(pd.read_sql(q, con))"),
        Cell("md", "## 6️⃣ ROW_NUMBER vs RANK vs DENSE_RANK\n\n```\nvalor: 10, 20, 20, 30\nROW_NUMBER: 1,  2,  3,  4    (siempre único)\nRANK      : 1,  2,  2,  4    (huecos)\nDENSE_RANK: 1,  2,  2,  3    (sin huecos)\n```"),
        Cell("md", "## 7️⃣ Subqueries correlacionadas\n\nUna subquery **correlacionada** se ejecuta una vez por cada fila de la outer query (referencia columnas del outer). Útiles pero suelen ser reescribibles con joins o window functions:"),
        Cell("code", "# \"clientes cuyo monto promedio supera el promedio global\"\nq = '''\nSELECT cliente_id, AVG(monto) AS avg_cliente\nFROM ordenes o\nGROUP BY cliente_id\nHAVING AVG(monto) > (SELECT AVG(monto) FROM ordenes)\n'''\nprint(pd.read_sql(q, con))"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Uso CTEs para descomponer queries\n- [ ] Encadeno múltiples CTEs\n- [ ] Uso ROW_NUMBER OVER PARTITION para top-K por grupo\n- [ ] Calculo totales corridos con SUM() OVER\n- [ ] Comparo con anterior/siguiente con LAG/LEAD"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 3 versiones (nested/CTE/multi-CTE), top-3 con ROW_NUMBER, total corrido + delta, recursive calendario."),
        Cell("md", "## 🔗 Referencias\n\n- Tanimura, *SQL for Data Scientists*, caps. 4-5\n- [Modern SQL — CTEs](https://modern-sql.com/feature/with)\n\n➡️ **Siguiente:** [043 — SQL desde Python](../043-sql-desde-python-sqlite3-sqlalchemy-duckdb/README.md)"),
    ],
    definiciones=[
        ("CTE (Common Table Expression)", "Vista temporal dentro de una query con `WITH nombre AS (...)`. Descompone queries complejas en pasos legibles. Puedes encadenar múltiples: `WITH a AS (...), b AS (...) SELECT ...`."),
        ("Recursive CTE", "CTE que se referencia a sí misma. Útil para jerarquías (árbol organizacional), grafos, generar series (calendario diario). Sintaxis: `WITH RECURSIVE t AS (caso_base UNION ALL caso_recursivo)`."),
        ("Window function", "Agregación que **no colapsa filas** — añade el resultado por fila. Sintaxis: `FUNC() OVER (PARTITION BY col ORDER BY col2)`. Ejemplos: `ROW_NUMBER`, `RANK`, `LAG`, `LEAD`, `SUM() OVER (...)`."),
        ("`PARTITION BY` vs `GROUP BY`", "**PARTITION BY** (en window): subgrupos para la función, pero mantiene cada fila. **GROUP BY**: reduce a una fila por grupo."),
        ("`LAG` / `LEAD`", "Acceden a la fila anterior/siguiente dentro de la partition. `LAG(monto, 1) OVER (PARTITION BY cliente ORDER BY fecha)`. Útil para diffs, growth rates."),
        ("Subquery correlacionada", "Subquery que **depende** de la outer query (referencia sus columnas). Se ejecuta una vez por cada fila de la outer. Más lenta que JOIN equivalente."),
    ],
    errores_comunes=[
        ("`syntax error at or near \"OVER\"`", "Motor sin soporte de window functions (SQLite <3.25, MySQL <8). **Fix**: actualiza motor o reescribe con subqueries / self-join."),
        ("`ROW_NUMBER()` da números repetidos", "Olvidaste `OVER (...)`. Sin él, no es window function. **Fix**: `ROW_NUMBER() OVER (ORDER BY col)`."),
        ("CTE recursiva nunca termina", "Caso base falta o caso recursivo no converge. **Fix**: añade `LIMIT N` para debug, asegura que cada iteración acerca al caso base."),
        ("`LAG(x) OVER (ORDER BY fecha)` da NULL en la primera fila", "Comportamiento esperado — no hay fila anterior. **Fix**: `LAG(x, 1, 0)` para default 0, o filtra con `WHERE row > 1`."),
        ("CTE da mismo resultado pero más lento que subquery", "Algunos motores no inlineaban CTEs (PostgreSQL <12). **Fix**: actualiza, o reescribe como subquery temporalmente."),
    ],
    faq=[
        ("¿CTE o subquery?",
         "**CTE** si el lector necesita entender qué hace cada paso (legibilidad). **Subquery** si es trivial y de un solo uso. Para queries >10 líneas, CTE casi siempre gana."),
        ("¿`ROW_NUMBER`, `RANK` o `DENSE_RANK`?",
         "Para valores `[10, 20, 20, 30]`: **ROW_NUMBER** `[1,2,3,4]` (siempre único). **RANK** `[1,2,2,4]` (huecos). **DENSE_RANK** `[1,2,2,3]` (sin huecos). Elige según semántica."),
        ("¿Window function es lo mismo que groupby+merge en pandas?",
         "Conceptualmente sí — `g.transform(...)` en pandas hace lo equivalente. Window functions son la versión SQL más eficiente."),
        ("¿Cuándo subquery correlacionada vs JOIN?",
         "Casi siempre **JOIN o window function** es más rápido. Correlacionada solo cuando no tiene equivalente JOIN (raro) o el optimizador del motor la maneja bien (motores modernos)."),
        ("¿Top-N por grupo?",
         "**Patrón estándar**: `WITH ranked AS (SELECT *, ROW_NUMBER() OVER (PARTITION BY grupo ORDER BY metric DESC) rn FROM tabla) SELECT * FROM ranked WHERE rn <= N`."),
    ],
))


SPECS.append(ClassSpec(
    folder="043-sql-desde-python-sqlite3-sqlalchemy-duckdb",
    number="043",
    title="SQL desde Python: sqlite3, SQLAlchemy, DuckDB",
    duration="75 min",
    source="Python stdlib `sqlite3` · SQLAlchemy docs · DuckDB Python docs.",
    objetivo=(
        "Que el alumno conecte Python con SQL de las 3 formas que va a encontrar en producción: "
        "`sqlite3` (stdlib, demo local), `SQLAlchemy` (ORM/engine genérico para PostgreSQL/MySQL), "
        "y `DuckDB` (columnar embebido para análisis sobre CSV/Parquet sin servidor)."
    ),
    resultados=[
        "**Conectar y consultar** con `sqlite3` stdlib, usando placeholders `?` (NUNCA concatenar SQL).",
        "**Usar SQLAlchemy `create_engine(URL)`** + `pd.read_sql` para queries a cualquier RDBMS.",
        "**Usar DuckDB** para hacer SQL sobre DataFrames y CSV/Parquet directamente.",
        "**Prevenir SQL injection** con queries parametrizadas.",
        "**Decidir** entre sqlite/SQLAlchemy/DuckDB según el caso.",
    ],
    temas=[
        ("`sqlite3` stdlib: connect, cursor, fetchall", "Para demos y BDs ligeras."),
        ("Placeholders `?` y `:nombre`", "NUNCA concatenar strings."),
        ("SQLAlchemy `create_engine('postgresql://...')`", "Soporta todos los RDBMS."),
        ("`pd.read_sql` y `df.to_sql`", "Pasarela pandas ↔ BD."),
        ("DuckDB: SQL sobre DataFrames y archivos", "`duckdb.query('SELECT ... FROM df')`."),
        ("Cuándo cada uno", "Trade-offs."),
    ],
    dataset=(
        "Penguins descargado a CSV local para DuckDB; datos sintéticos para sqlite/SQLAlchemy."
    ),
    ejercicios=[
        "**sqlite3 con placeholders.** Crea tabla, inserta 5 filas usando `executemany` con tuples, consulta con `?` placeholder. Demuestra el bug si concatenas.",
        "**`df.to_sql` y `pd.read_sql`.** Carga un DataFrame a SQLite y consulta de vuelta.",
        "**SQLAlchemy engine.** Crea engine SQLite. Usa `pd.read_sql` con engine.",
        "**DuckDB sobre DataFrame.** Carga penguins en df. `duckdb.query('SELECT species, AVG(body_mass_g) FROM df GROUP BY species').df()`.",
        "**DuckDB sobre CSV.** Mismo query pero `FROM 'penguins.csv'` directo, sin cargar a pandas.",
    ],
    homework=(
        "Notebook con 3 backends del mismo análisis: (a) sqlite3 stdlib + cursor; (b) SQLAlchemy "
        "engine + pd.read_sql; (c) DuckDB sobre CSV. Documenta cuándo elegirías cada uno. "
        "Demuestra explícitamente el peligro de SQL injection con concatenación vs placeholders."
    ),
    homework_criterio="Las 3 versiones devuelven el mismo resultado. Demo de injection sin daño real.",
    referencias=[
        "[Python `sqlite3` docs](https://docs.python.org/3/library/sqlite3.html)",
        "[SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/)",
        "[DuckDB Python API](https://duckdb.org/docs/api/python/overview)",
        "[OWASP — SQL injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)",
    ],
    siguiente=("044-nosql-mongodb-con-pymongo", "NoSQL: MongoDB con pymongo"),
    cells=[
        Cell("md", "# Clase 043 — SQL desde Python\n\n**Parte 0** · sqlite3 + SQLAlchemy + DuckDB.\n\n> 🎯 Las 3 formas que vas a usar en producción. Parametrización para evitar injection.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import sqlite3\nimport pandas as pd\nimport numpy as np\nrng = np.random.default_rng(42)\n\n# DataFrame demo\ndf = pd.DataFrame({\n    'cliente_id': range(1, 11),\n    'nombre': [f'Cliente {i}' for i in range(1, 11)],\n    'pais': rng.choice(['ES', 'CL', 'MX'], 10),\n    'monto': rng.uniform(50, 500, 10).round(2),\n})\nprint(df.head())"),
        Cell("md", "## 1️⃣ `sqlite3` stdlib\n\nFlow básico: `connect` → `cursor` → `execute(sql, params)` → `fetchall()`."),
        Cell("code", "con = sqlite3.connect(':memory:')\ncur = con.cursor()\ncur.execute('CREATE TABLE clientes (id INTEGER, nombre TEXT, pais TEXT, monto REAL)')\n\n# executemany con tuples para insertar varios\ndatos = [(row.cliente_id, row.nombre, row.pais, row.monto) for row in df.itertuples()]\ncur.executemany('INSERT INTO clientes VALUES (?, ?, ?, ?)', datos)\ncon.commit()\n\n# Consulta con placeholder ?\nfor row in cur.execute('SELECT * FROM clientes WHERE pais = ? AND monto > ?', ('ES', 200)):\n    print(row)"),
        Cell("md", "## 2️⃣ ⚠️ NUNCA concatenes SQL\n\n```python\n# ❌ MAL — vulnerable a injection\nuser_input = \"ES'; DROP TABLE clientes; --\"\ncur.execute(f\"SELECT * FROM clientes WHERE pais = '{user_input}'\")  # ¡catástrofe!\n\n# ✅ BIEN — placeholder seguro\ncur.execute('SELECT * FROM clientes WHERE pais = ?', (user_input,))\n```\n\nEl driver escapa el valor automáticamente. Es **la** regla de seguridad de SQL desde código."),
        Cell("md", "## 3️⃣ `pd.read_sql` y `df.to_sql`\n\nPandas tiene pasarela bidireccional:"),
        Cell("code", "# DataFrame → tabla\ndf.to_sql('clientes_pd', con, if_exists='replace', index=False)\n\n# Tabla → DataFrame\nresult = pd.read_sql('SELECT pais, AVG(monto) AS avg_m FROM clientes_pd GROUP BY pais', con)\nprint(result)"),
        Cell("md", "## 4️⃣ SQLAlchemy — backend-agnostic\n\n```python\nfrom sqlalchemy import create_engine\n\n# URLs por motor:\n#   sqlite:///archivo.db           — SQLite local\n#   sqlite:///:memory:             — SQLite en memoria\n#   postgresql://user:pw@host/db   — Postgres\n#   mysql+pymysql://user:pw@host/db— MySQL\n\nengine = create_engine('sqlite:///:memory:')\ndf.to_sql('clientes', engine, if_exists='replace', index=False)\nresult = pd.read_sql('SELECT * FROM clientes WHERE monto > 200', engine)\n```\n\nVentaja: cambias 1 string en el engine y migras de SQLite a Postgres sin tocar el resto del código."),
        Cell("code", "try:\n    from sqlalchemy import create_engine\n    engine = create_engine('sqlite:///:memory:')\n    df.to_sql('cl', engine, if_exists='replace', index=False)\n    print(pd.read_sql('SELECT pais, COUNT(*) c FROM cl GROUP BY pais', engine))\nexcept ImportError:\n    print('Instala SQLAlchemy: pip install sqlalchemy')"),
        Cell("md", "## 5️⃣ DuckDB — SQL sobre DataFrames y archivos\n\nDuckDB es como SQLite pero **columnar** (optimizado para analytics) y **lee CSV/Parquet directamente** sin cargar a memoria:\n\n```python\nimport duckdb\n# Sobre DataFrame en memoria\nduckdb.query('SELECT species, AVG(body_mass_g) FROM df GROUP BY species').df()\n\n# Sobre CSV directo (sin pandas)\nduckdb.query(\"SELECT species, COUNT(*) FROM 'penguins.csv' GROUP BY species\").df()\n\n# Sobre Parquet (mucho más rápido)\nduckdb.query(\"SELECT * FROM 'datos.parquet' LIMIT 100\").df()\n```"),
        Cell("code", "try:\n    import duckdb\n    # SQL sobre nuestro DataFrame\n    result = duckdb.query('''\n        SELECT pais,\n               COUNT(*)       AS n,\n               AVG(monto)     AS avg_monto,\n               MAX(monto)     AS max_monto\n        FROM df\n        GROUP BY pais\n        ORDER BY avg_monto DESC\n    ''').df()\n    print(result.round(2))\nexcept ImportError:\n    print('Instala DuckDB: pip install duckdb')"),
        Cell("md", "## 🧭 Cuándo cada uno\n\n| Tool | Caso |\n|---|---|\n| `sqlite3` stdlib | Demos, tests, BDs locales pequeñas, scripts one-shot |\n| SQLAlchemy | Producción con PostgreSQL/MySQL; ORMs, migraciones |\n| DuckDB | Análisis ad-hoc sobre CSV/Parquet, EDA rápido con SQL |"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Uso placeholders `?` en sqlite3 (NUNCA concatenar)\n- [ ] Sé pasarela `df.to_sql` / `pd.read_sql`\n- [ ] Conozco SQLAlchemy para producción\n- [ ] Uso DuckDB para SQL sobre CSV/Parquet sin cargar a pandas\n- [ ] Sé qué tool elegir según contexto"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 3 backends mismo análisis + demo injection."),
        Cell("md", "## 🔗 Referencias\n\n- [sqlite3](https://docs.python.org/3/library/sqlite3.html)\n- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/tutorial/)\n- [DuckDB Python](https://duckdb.org/docs/api/python/overview)\n\n➡️ **Siguiente:** [044 — MongoDB](../044-nosql-mongodb-con-pymongo/README.md)"),
    ],
    definiciones=[
        ("`sqlite3` (stdlib)", "Driver Python para SQLite. Sin dependencias externas. Patrón: `connect(...)` → `cursor()` → `execute(sql, params)` → `fetchall()`."),
        ("Parameterized query (`?` o `:name`)", "Placeholder donde el driver substituye valores escapados. **Única forma segura** de pasar datos de usuario — previene SQL injection."),
        ("SQLAlchemy", "Toolkit ORM + Core para Python. Backend-agnostic: cambias el URL del engine y migras entre SQLite/Postgres/MySQL sin tocar queries. `create_engine('postgresql://...')`."),
        ("DuckDB", "OLAP DB embebida. SQL sobre DataFrames pandas (`duckdb.query('SELECT ... FROM df')`) y archivos CSV/Parquet directos (`FROM 'data.csv'`). Mucho más rápido que sqlite3 para analytics."),
        ("SQL injection", "Inyección de SQL malicioso via concatenación de strings con input de usuario. **Prevención**: SIEMPRE parameterized queries, nunca f-string con valores externos."),
        ("`pd.read_sql` / `df.to_sql`", "Pasarela pandas↔BD. Acepta connection o engine. `read_sql_query` para queries complejas; `read_sql_table` para tablas completas."),
    ],
    errores_comunes=[
        ("`OperationalError: no such table: X` después de insert", "Falta `con.commit()`. sqlite3 no auto-commit. **Fix**: `con.commit()` tras INSERT/UPDATE/DELETE, o `con = sqlite3.connect(':memory:', isolation_level=None)` para auto-commit."),
        ("Concatené input de usuario en query y funcionó", "Hasta que el usuario malicioso prueba `'; DROP TABLE clientes; --`. **Fix**: NUNCA `f\"SELECT * FROM x WHERE id={user}\"`. Siempre `(?, ?)` placeholders."),
        ("SQLAlchemy 2.0 — `Engine.execute` no existe", "API cambió: ahora `with engine.connect() as con: con.execute(text('SELECT ...'))`. Tutorial oficial actualizado."),
        ("DuckDB lee CSV pero pierde tipos", "Pandas adivina mejor. **Fix**: `duckdb.read_csv('x.csv', dtype={'col': 'INT'})` o convierte después."),
        ("`pd.read_sql` lento con N grande", "Driver Python carga todo a Python. **Fix**: `chunksize=10000` itera por bloques, o usa DuckDB directo sobre BD (cuando aplica)."),
    ],
    faq=[
        ("¿sqlite3, SQLAlchemy o DuckDB?",
         "**sqlite3** para demos/tests/scripts locales. **SQLAlchemy** para producción con Postgres/MySQL. **DuckDB** para EDA sobre CSV/Parquet sin servidor — el más rápido para analytics."),
        ("¿`pd.read_sql` es seguro contra injection?",
         "Sí si pasas params: `read_sql('SELECT * FROM t WHERE x=:val', con, params={'val': user_input})`. No si concatenas strings."),
        ("¿ORM (SQLAlchemy declarative) o queries directas?",
         "ORM cuando el modelo se usa en muchas partes (web app con N modelos). Queries directas para análisis ad-hoc. Pueden coexistir."),
        ("¿DuckDB sobre Parquet vs sobre pandas?",
         "**Parquet directo** es más rápido (no carga a Python). **Pandas** cuando ya tienes el DataFrame en memoria. DuckDB es smart: optimiza ambos casos."),
        ("¿Cerrar conexión manualmente?",
         "Usa context manager: `with sqlite3.connect(...) as con: ...` o `con.close()` en `finally`. Conexiones dejadas abiertas consumen handles del OS."),
    ],
))


SPECS.append(ClassSpec(
    folder="044-nosql-mongodb-con-pymongo",
    number="044",
    title="NoSQL: MongoDB con pymongo",
    duration="75 min",
    source="MongoDB docs · pymongo docs · *MongoDB: The Definitive Guide* (Bradshaw et al.) cap. 1.",
    objetivo=(
        "Que el alumno entienda el modelo NoSQL documento (collections de JSON-like), cuándo "
        "conviene sobre SQL, y use `pymongo` para CRUD básico + queries con operadores típicos. "
        "Sin pretender competir con un curso entero de MongoDB."
    ),
    resultados=[
        "**Diferenciar** modelo relacional (tablas + filas) vs documento (collections + docs JSON).",
        "**Reconocer** cuándo NoSQL aporta (schema flexible, datos jerárquicos, escala horizontal).",
        "**Conectar con pymongo**, hacer insert/find/update/delete.",
        "**Filtrar** con operadores: `$gt`, `$lt`, `$in`, `$regex`, `$and`, `$or`.",
        "**Hacer agregaciones** con el pipeline (`$match`, `$group`, `$sort`).",
    ],
    temas=[
        ("SQL vs NoSQL — cuándo cada uno", "No \"NoSQL es mejor\" — distinto."),
        ("Modelo documento: collections + docs JSON", "Schema flexible."),
        ("pymongo: connect, insert_one, find, update_one", "CRUD básico."),
        ("Operadores de query: $gt/$lt/$in/$regex", "Equivalentes a WHERE."),
        ("Aggregation pipeline", "$match/$group/$sort — análogo a SQL."),
        ("Cuándo NO usar Mongo", "Cuando relacional es claramente mejor."),
    ],
    dataset=(
        "MongoDB local (Docker o Atlas free tier) — o usar `mongomock` para tests. "
        "Datos sintéticos: collection de productos."
    ),
    ejercicios=[
        "**CRUD básico.** Conecta a Mongo (o mongomock), inserta 5 productos, lee todos, actualiza uno, borra uno.",
        "**Find con operadores.** Productos con `precio > 100` y categoría en `['libros', 'musica']`.",
        "**Update con `$set` y `$inc`.** Incrementa stock de un producto en 10 unidades.",
        "**Aggregation pipeline.** Promedio de precio por categoría con `$group`.",
        "**Documento jerárquico.** Inserta un producto con array de `reviews` (sub-documentos). Consulta los que tienen alguna review con `rating < 3` usando `$elemMatch`.",
    ],
    homework=(
        "Notebook con `mongomock` (no requiere Mongo real): (a) collection productos con 20 docs "
        "sintéticos; (b) 5 queries demostrando operadores; (c) aggregation pipeline con `$match` "
        "→ `$group` → `$sort`; (d) reporte: 3 casos donde Mongo es mejor que SQL y 3 donde no."
    ),
    homework_criterio="Las queries funcionan; el reporte tiene casos justificados.",
    referencias=[
        "[pymongo docs](https://pymongo.readthedocs.io/)",
        "[MongoDB query operators](https://www.mongodb.com/docs/manual/reference/operator/query/)",
        "[mongomock](https://github.com/mongomock/mongomock)",
        "Bradshaw, *MongoDB: The Definitive Guide* 3e, cap. 1.",
    ],
    siguiente=("045-apis-rest-con-requests", "APIs REST con requests"),
    cells=[
        Cell("md", "# Clase 044 — MongoDB / pymongo\n\n**Parte 0** · MongoDB + pymongo docs.\n\n> 🎯 Modelo documento, CRUD, queries con operadores, aggregation pipeline.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup\n\nPara este notebook usamos `mongomock` para no requerir Mongo real:\n\n```bash\npip install mongomock pymongo\n```\n\nLa API es idéntica a pymongo — solo cambia `MongoClient` por `mongomock.MongoClient`."),
        Cell("code", "try:\n    import mongomock\n    client = mongomock.MongoClient()\n    print('mongomock OK')\nexcept ImportError:\n    print('Instala: pip install mongomock')\n\ndb = client['lab044']\nproductos = db['productos']"),
        Cell("md", "## 1️⃣ SQL vs NoSQL — el modelo\n\n| | SQL | NoSQL documento (Mongo) |\n|---|---|---|\n| Unidad | Fila en tabla | Documento JSON en collection |\n| Schema | Rígido (CREATE TABLE) | Flexible (cada doc puede tener cols distintas) |\n| Relaciones | JOINs entre tablas | Documentos anidados (denormalización) |\n| Escala | Vertical (más CPU/RAM) | Horizontal (más nodos) |\n| Transacciones ACID | Sí, fuerte | Sí pero más limitado |\n| Mejor para | Datos estructurados, integridad referencial | Schema variable, datos jerárquicos, alta escala write |"),
        Cell("md", "## 2️⃣ Insert"),
        Cell("code", "docs = [\n    {'nombre': 'Libro Python', 'categoria': 'libros',  'precio': 30, 'stock': 50, 'tags': ['programacion', 'python']},\n    {'nombre': 'Guitarra',     'categoria': 'musica',  'precio': 800, 'stock': 5,  'tags': ['acustica']},\n    {'nombre': 'Auriculares',  'categoria': 'audio',   'precio': 120, 'stock': 30, 'tags': ['wireless', 'bluetooth']},\n    {'nombre': 'Libro Pandas', 'categoria': 'libros',  'precio': 35, 'stock': 40, 'tags': ['programacion', 'datos']},\n    {'nombre': 'Mouse',        'categoria': 'audio',   'precio': 45, 'stock': 100, 'tags': ['wireless']},\n]\nresult = productos.insert_many(docs)\nprint(f'insertados: {len(result.inserted_ids)} docs')"),
        Cell("md", "## 3️⃣ Find con operadores\n\n| Operador | Equivalente SQL |\n|---|---|\n| `$gt`, `$lt`, `$gte`, `$lte` | `>`, `<`, `>=`, `<=` |\n| `$eq`, `$ne` | `=`, `<>` |\n| `$in`, `$nin` | `IN`, `NOT IN` |\n| `$and`, `$or`, `$not` | `AND`, `OR`, `NOT` |\n| `$regex` | `LIKE` con regex |\n| `$exists` | `IS NULL`/`IS NOT NULL` |"),
        Cell("code", "# Productos > 100 y en categorías específicas\nquery = {\n    'precio': {'$gt': 100},\n    'categoria': {'$in': ['libros', 'audio']},\n}\nfor doc in productos.find(query):\n    print(f\"{doc['nombre']:20s}  cat={doc['categoria']:8s}  €{doc['precio']}\")"),
        Cell("md", "## 4️⃣ Update con `$set` y `$inc`"),
        Cell("code", "productos.update_one(\n    {'nombre': 'Auriculares'},\n    {'$inc': {'stock': 10}, '$set': {'oferta': True}}\n)\nprint(productos.find_one({'nombre': 'Auriculares'}))"),
        Cell("md", "## 5️⃣ Aggregation pipeline\n\nPipeline de etapas — análogo a SQL pero más componible:"),
        Cell("code", "pipeline = [\n    {'$match': {'precio': {'$lt': 500}}},\n    {'$group': {\n        '_id': '$categoria',\n        'n': {'$sum': 1},\n        'precio_medio': {'$avg': '$precio'},\n    }},\n    {'$sort': {'precio_medio': -1}},\n]\nfor doc in productos.aggregate(pipeline):\n    print(doc)"),
        Cell("md", "## 6️⃣ Documentos jerárquicos — el valor real de NoSQL\n\nUna review embebida en un producto evita un JOIN. `$elemMatch` filtra por condiciones en sub-documentos:"),
        Cell("code", "productos.update_one(\n    {'nombre': 'Libro Python'},\n    {'$set': {'reviews': [\n        {'user': 'ana', 'rating': 5, 'comentario': 'excelente'},\n        {'user': 'bob', 'rating': 2, 'comentario': 'no me gustó'},\n        {'user': 'cris', 'rating': 4, 'comentario': 'bueno'},\n    ]}}\n)\n\n# Buscar productos con alguna review baja\nmalos = list(productos.find({'reviews': {'$elemMatch': {'rating': {'$lt': 3}}}}))\nfor m in malos:\n    print(f\"{m['nombre']} tiene reviews bajas\")"),
        Cell("md", "## 🚫 Cuándo NO usar Mongo\n\n- **Necesitas integridad referencial fuerte** (relaciones ⊥ desnormalización).\n- **Tu modelo es naturalmente tabular** — usar Mongo añade complejidad sin ganancia.\n- **Reporting y BI son críticos** — SQL es mucho mejor para analítica.\n- **Tu equipo no quiere aprender otro paradigma** — costo de oportunidad."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Entiendo modelo documento vs relacional\n- [ ] Hago CRUD con pymongo\n- [ ] Uso operadores ($gt, $in, $regex, etc.)\n- [ ] Hago aggregation pipeline ($match/$group/$sort)\n- [ ] Sé cuándo NO conviene Mongo"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 20 productos, 5 queries, pipeline, reporte cuándo Mongo vs SQL."),
        Cell("md", "## 🔗 Referencias\n\n- [pymongo](https://pymongo.readthedocs.io/)\n- [MongoDB operators](https://www.mongodb.com/docs/manual/reference/operator/query/)\n\n➡️ **Siguiente:** [045 — APIs REST](../045-apis-rest-con-requests/README.md)"),
    ],
    definiciones=[
        ("NoSQL documento", "Familia de DBs que almacena **documentos JSON-like** (BSON en Mongo) en lugar de filas en tablas. Schema flexible — cada documento puede tener campos distintos."),
        ("Collection", "Equivalente a una tabla en SQL, pero sin schema fijo. Contiene documentos del mismo \"tipo\" lógico (productos, usuarios, eventos)."),
        ("Documento (`dict` BSON)", "Unidad de almacenamiento. JSON con tipos extra (Date, ObjectId, Decimal128). Puede contener arrays y sub-documentos anidados."),
        ("Operador (`$gt`, `$in`, `$elemMatch`)", "Prefijo `$` en las queries Mongo: `{'precio': {'$gt': 100}}` ≈ `WHERE precio > 100`. La query es un dict JSON, no string."),
        ("Aggregation pipeline", "Equivalente Mongo a CTEs encadenadas: lista de etapas (`$match`, `$group`, `$sort`, `$project`, `$lookup`) que procesan documentos secuencialmente."),
        ("`$elemMatch`", "Operador para filtrar por condiciones sobre **elementos de un array** dentro del documento. Útil con arrays de sub-docs (reviews dentro de producto)."),
    ],
    errores_comunes=[
        ("`pymongo.errors.ServerSelectionTimeoutError`", "No conecta al servidor. **Fix**: verifica que Mongo está corriendo (`docker ps`), URI correcta (`mongodb://localhost:27017`), firewall."),
        ("Update sin `$set` reemplaza el documento entero", "`update_one(filter, {'precio': 100})` reemplaza TODO el doc. **Fix**: usa `{'$set': {'precio': 100}}` para modificar solo ese campo."),
        ("Aggregation con `$group` sin `_id` falla", "`$group` requiere `_id` (la key de agrupación, puede ser `None` para agrupar todo). **Fix**: `{'$group': {'_id': '$categoria', 'total': {'$sum': '$monto'}}}`."),
        ("Query con `{}` devuelve todo (no None)", "`{}` es \"sin filtro\" en Mongo. Si querías matchear todo, OK; si querías nada, `{'_id': {'$exists': False}}` o similar."),
        ("Cuento con `count_documents({})` y va lento", "Sin filtro, recorre toda la collection. **Fix**: para counts aproximados rápidos, `db.coll.estimated_document_count()`."),
    ],
    faq=[
        ("¿SQL o NoSQL?",
         "**SQL** para datos tabulares con relaciones, integridad referencial, reporting/BI. **NoSQL documento** para schema variable, datos jerárquicos naturales, escala write masiva. No es \"mejor\" — distinto."),
        ("¿`find_one` o `find`?",
         "`find_one` devuelve dict (o None). `find` devuelve cursor iterable. Para 1 doc: `find_one`. Para muchos: `list(coll.find(query))` o iterar el cursor."),
        ("¿pymongo vs Motor (async)?",
         "**pymongo** síncrono, default. **Motor** asíncrono (asyncio) — para web apps con muchas concurrent connections."),
        ("¿Cómo tipo los documentos en Python?",
         "Usa **pydantic** con `BaseModel`. Convierte dict ↔ tipo validado. Combinado con FastAPI, casi gratis (verás en MLOps)."),
        ("¿Mongo para data science?",
         "Como **fuente** sí (extraes datos con aggregation, los pasas a pandas). Para **análisis** ya no — pandas/DuckDB son mejores. Mongo brilla en operaciones (logs, eventos)."),
    ],
))


SPECS.append(ClassSpec(
    folder="045-apis-rest-con-requests",
    number="045",
    title="APIs REST con requests",
    duration="90 min",
    source="*HTTP: The Definitive Guide* caps. 1-2 · requests docs.",
    objetivo=(
        "Que el alumno consuma APIs REST públicas con `requests`: GET con parámetros, manejo de "
        "status codes, autenticación (header, bearer token), paginación, rate limiting con `Retry`, "
        "y carga eficiente con `Session`. Lo mínimo para no romper la API del proveedor ni tu pipeline."
    ),
    resultados=[
        "**Hacer GET/POST** con `requests`, manejar params, headers, body JSON.",
        "**Verificar status code** (200 vs 4xx vs 5xx) y usar `raise_for_status()`.",
        "**Autenticarse** con header `Authorization: Bearer ...` o API key en header/query.",
        "**Paginar** correctamente cuando la API devuelve resultados en páginas.",
        "**Rate-limiting** con `urllib3.util.retry.Retry` para reintentos exponenciales.",
        "**Reusar conexión** con `requests.Session` para múltiples requests.",
    ],
    temas=[
        ("Métodos HTTP: GET, POST, PUT, DELETE", "Verbos REST."),
        ("Status codes: 2xx/3xx/4xx/5xx", "Cómo reaccionar a cada uno."),
        ("Params, headers, body", "Las 3 formas de mandar datos."),
        ("Autenticación: Bearer token, API key", "Header `Authorization`."),
        ("Paginación: offset/limit, cursor, link header", "3 patrones comunes."),
        ("Rate limiting + retry exponencial", "No tirar la API ajena."),
        ("`requests.Session` para reuso", "Más rápido + cookies persistentes."),
    ],
    dataset="API pública sin auth: https://api.coingecko.com (precios cripto). Sin API key necesaria.",
    ejercicios=[
        "**GET básico.** `requests.get('https://api.github.com')`. Inspecciona `status_code`, `headers`, `.json()`.",
        "**Con params.** GitHub search: `https://api.github.com/search/repositories?q=python+ml&sort=stars`. Imprime top 5.",
        "**`raise_for_status` + try.** Pega a una URL que devuelve 404 (`/notfound`) y maneja la excepción.",
        "**Paginación.** GitHub events API. Itera 3 páginas con `page=1,2,3`.",
        "**Session + Retry.** Configura una `Session` con `HTTPAdapter` + `Retry` (3 intentos, backoff 1s). Verifica que reintenta en 5xx simulado.",
    ],
    homework=(
        "Notebook que: (a) consulta una API pública (CoinGecko, GitHub, JSONPlaceholder) con GET; "
        "(b) maneja status codes con try/except; (c) pagina 3+ páginas; (d) configura Session "
        "con Retry exponencial; (e) reporta cuánto se tardó vs un loop sin Session."
    ),
    homework_criterio="Maneja al menos un error sin crash. Pagination devuelve datos esperados.",
    referencias=[
        "[requests docs](https://requests.readthedocs.io/)",
        "[urllib3 Retry](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry)",
        "[GitHub REST API](https://docs.github.com/en/rest)",
        "[HTTP status codes (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)",
    ],
    siguiente=("046-web-scraping-con-beautifulsoup", "Web scraping con BeautifulSoup"),
    cells=[
        Cell("md", "# Clase 045 — APIs REST con requests\n\n**Parte 0** · requests docs.\n\n> 🎯 GET/POST, status codes, auth, paginación, rate limiting, Session.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import requests\nimport time\nfrom requests.adapters import HTTPAdapter\nfrom urllib3.util.retry import Retry\nprint(f'requests: {requests.__version__}')"),
        Cell("md", "## 1️⃣ GET básico\n\n```python\nr = requests.get('https://api.github.com')\nr.status_code   # 200\nr.headers       # dict con metadata\nr.json()        # parsea response body como JSON\nr.text          # raw string\n```"),
        Cell("code", "try:\n    r = requests.get('https://api.github.com', timeout=10)\n    print(f'status: {r.status_code}')\n    print(f'content-type: {r.headers.get(\"content-type\")}')\n    body = r.json()\n    print(f'keys: {list(body.keys())[:5]}...')\nexcept requests.RequestException as e:\n    print(f'sin red: {e}')"),
        Cell("md", "## 2️⃣ Params y headers\n\n```python\nr = requests.get(\n    'https://api.github.com/search/repositories',\n    params={'q': 'python ml', 'sort': 'stars', 'per_page': 5},\n    headers={'Accept': 'application/vnd.github+json'},\n    timeout=10,\n)\n```\n\n`params` se convierten a `?q=...&sort=...` automáticamente, con encoding seguro."),
        Cell("code", "try:\n    r = requests.get(\n        'https://api.github.com/search/repositories',\n        params={'q': 'python machine learning', 'sort': 'stars', 'per_page': 5},\n        timeout=10,\n    )\n    r.raise_for_status()\n    for item in r.json()['items'][:5]:\n        print(f\"{item['stargazers_count']:>7,}  {item['full_name']}\")\nexcept requests.RequestException as e:\n    print(f'error: {e}')"),
        Cell("md", "## 3️⃣ Status codes — qué significan\n\n| Familia | Significado | Reacción típica |\n|---|---|---|\n| 2xx | Éxito | continuar |\n| 3xx | Redirección | requests sigue automáticamente |\n| 4xx | Error cliente (404, 401, 403, 429) | revisar tu request |\n| 5xx | Error servidor | reintentar con backoff |\n\n**`raise_for_status()`** lanza `HTTPError` si status >= 400:"),
        Cell("code", "try:\n    r = requests.get('https://api.github.com/this/does/not/exist', timeout=10)\n    r.raise_for_status()\nexcept requests.HTTPError as e:\n    print(f'HTTP error: {e}')\n    print(f'status fue: {r.status_code}')"),
        Cell("md", "## 4️⃣ Autenticación\n\n```python\n# Bearer token\nr = requests.get(URL, headers={'Authorization': f'Bearer {TOKEN}'})\n\n# API key en header\nr = requests.get(URL, headers={'X-API-Key': KEY})\n\n# Basic auth (legacy)\nfrom requests.auth import HTTPBasicAuth\nr = requests.get(URL, auth=HTTPBasicAuth('user', 'pw'))\n```\n\n**Regla**: tokens y keys NUNCA hardcoded en el código. Usa variables de entorno o secret manager:\n\n```python\nimport os\nTOKEN = os.environ['GITHUB_TOKEN']\n```"),
        Cell("md", "## 5️⃣ Paginación\n\nPatrones comunes:\n\n1. **Offset/limit**: `?page=2&per_page=100`\n2. **Cursor**: `?after=<id_anterior>`\n3. **Link header**: la respuesta incluye `Link: <...>; rel=\"next\"`\n\nGitHub usa los 3 según endpoint."),
        Cell("code", "# Demo paginación con events (3 páginas)\ntry:\n    total = []\n    for page in range(1, 4):\n        r = requests.get(\n            'https://api.github.com/events',\n            params={'page': page, 'per_page': 5},\n            timeout=10,\n        )\n        if r.status_code != 200:\n            print(f'page {page}: status {r.status_code}, parar')\n            break\n        data = r.json()\n        total.extend(data)\n        print(f'page {page}: {len(data)} events')\n        time.sleep(0.5)   # cortesía\n    print(f'total acumulado: {len(total)}')\nexcept requests.RequestException as e:\n    print(f'error: {e}')"),
        Cell("md", "## 6️⃣ Rate limiting + retry exponencial\n\n```python\nfrom requests.adapters import HTTPAdapter\nfrom urllib3.util.retry import Retry\n\nretry = Retry(\n    total=3,\n    backoff_factor=1.0,   # espera 1s, 2s, 4s entre intentos\n    status_forcelist=[429, 500, 502, 503, 504],\n    allowed_methods=['GET'],\n)\nadapter = HTTPAdapter(max_retries=retry)\n\nsession = requests.Session()\nsession.mount('https://', adapter)\nsession.mount('http://', adapter)\n\n# Ahora cualquier session.get() reintenta automáticamente en 5xx/429\nr = session.get('https://api.github.com')\n```"),
        Cell("md", "## 7️⃣ `Session` — reutilizar conexión\n\nMejora rendimiento al reusar el TCP/TLS handshake, y mantiene cookies entre requests:"),
        Cell("code", "# Comparar Session vs requests directo\nN = 10\nurl = 'https://api.github.com/zen'   # endpoint trivial\n\nt0 = time.perf_counter()\nfor _ in range(N):\n    try:\n        requests.get(url, timeout=10)\n    except Exception:\n        pass\nt1 = time.perf_counter()\n\nt2 = time.perf_counter()\nwith requests.Session() as s:\n    for _ in range(N):\n        try:\n            s.get(url, timeout=10)\n        except Exception:\n            pass\nt3 = time.perf_counter()\n\nprint(f'sin session: {(t1-t0)*1000:.0f} ms')\nprint(f'con session: {(t3-t2)*1000:.0f} ms')\nprint(f'speedup    : {(t1-t0)/(t3-t2):.2f}× (sólo notable con muchas requests)')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé GET/POST con params/headers/json\n- [ ] Verifico status code (raise_for_status)\n- [ ] Manejo auth con header Bearer\n- [ ] Pagino con loop hasta que no haya más\n- [ ] Configuro Retry para 5xx/429\n- [ ] Uso Session para múltiples requests"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. API pública, manejo errores, pagination, Session+Retry, benchmark."),
        Cell("md", "## 🔗 Referencias\n\n- [requests docs](https://requests.readthedocs.io/)\n- [urllib3 Retry](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry)\n\n➡️ **Siguiente:** [046 — Web scraping con BeautifulSoup](../046-web-scraping-con-beautifulsoup/README.md)"),
    ],
    definiciones=[
        ("REST (REpresentational State Transfer)", "Estilo arquitectónico para APIs web sobre HTTP. Recursos identificados por URLs, operaciones por verbos HTTP (GET=leer, POST=crear, PUT=update, DELETE=borrar)."),
        ("`requests`", "Librería Python de facto para hacer HTTP. API simple: `requests.get(url, params=..., headers=..., timeout=...)`. Soporta auth, cookies, sessions, retry."),
        ("Status code", "Número HTTP que indica resultado: **2xx** éxito, **3xx** redirect, **4xx** error cliente (404 no encontrado, 401 no auth, 403 prohibido, 429 rate limited), **5xx** error servidor."),
        ("Paginación", "API que devuelve resultados en bloques (no todo de golpe). Patrones: **offset/limit** (`?page=2`), **cursor** (`?after=<id>`), **Link header** (`<url>; rel=\"next\"`)."),
        ("Rate limiting", "Política del servidor: máximo N requests/seg/usuario. Excederlo → 429. **Respétalo** con delays y retries exponenciales."),
        ("`Session`", "Reuso de conexión TCP/TLS entre requests. Mantiene cookies. ~10× más rápido para múltiples requests al mismo host vs `requests.get` repetido."),
        ("Bearer token", "Esquema de auth común: `Authorization: Bearer <token>` header. Token suele ser JWT o opaque string emitido por OAuth/login."),
    ],
    errores_comunes=[
        ("`requests.exceptions.ConnectTimeout` o `Timeout`", "API lenta o sin red. **Fix**: siempre pasa `timeout=10` (segundos) — sin él, request puede colgarse indefinidamente."),
        ("API responde 200 pero `.json()` lanza error", "Body no es JSON (HTML de error, vacío). **Fix**: verifica `r.headers['content-type']` o usa `try: r.json() except ValueError: print(r.text)`."),
        ("Hardcodeé el token en el código y subí a GitHub", "**Catástrofe de seguridad** — el token es público. **Fix**: rota el token YA, usa `.env` + `python-dotenv`, añade `.env` a `.gitignore`."),
        ("Mi script tira la API ajena (HTTP 429)", "Sin rate limiting. **Fix**: `time.sleep()` entre requests, o `Session` con `Retry(backoff_factor=2)` para reintentos exponenciales."),
        ("HTTPError no se lanza con status 4xx", "`requests` NO lanza por default. **Fix**: `r.raise_for_status()` después de `requests.get(...)` para lanzar en 4xx/5xx."),
    ],
    faq=[
        ("¿`requests` o `httpx`?",
         "**`requests`** sigue siendo la default (estable, ubícua). **`httpx`** drop-in con async support (`async with httpx.AsyncClient() as client:`). Para async/HTTP2, httpx; para todo lo demás, requests."),
        ("¿Cuándo Session?",
         "Más de 2-3 requests al mismo host. La primera request hace handshake TCP/TLS (~100ms); Session lo reusa. Para single request, no aporta."),
        ("¿`json=` o `data=` en POST?",
         "**`json=dict`**: serializa a JSON y setea `Content-Type: application/json`. **`data=dict`**: form-encoded (`application/x-www-form-urlencoded`). Para APIs REST modernas, casi siempre `json=`."),
        ("¿Cómo paginar genéricamente?",
         "Loop hasta que la API diga \"no más\": `while True: r = requests.get(url, params=...); items.extend(r.json()['data']); if not r.json().get('next'): break`."),
        ("¿Auth OAuth desde Python?",
         "Para casos simples (Bearer fijo): pasa el header. Para OAuth flow completo: `authlib`, `requests-oauthlib`. Para producción: librería oficial del proveedor (`google-auth`, `pyOpenSSL`, etc.)."),
    ],
))


SPECS.append(ClassSpec(
    folder="046-web-scraping-con-beautifulsoup",
    number="046",
    title="Web scraping con BeautifulSoup",
    duration="75 min",
    source="*Web Scraping with Python* (Mitchell, 2ª ed.) caps. 1-3 · BeautifulSoup docs.",
    objetivo=(
        "Que el alumno extraiga datos de páginas HTML cuando **no hay API disponible**, usando "
        "`requests` + `BeautifulSoup`. Y entienda los **límites éticos y legales**: robots.txt, "
        "rate limiting humano, ToS, datos personales, copyright. Lo último que debe hacer al "
        "scrapear es tirar abajo el sitio o meterse en problemas."
    ),
    resultados=[
        "**Parsear HTML** con `BeautifulSoup(html, 'html.parser')`.",
        "**Encontrar elementos** con `find`, `find_all`, `select` (CSS selectors).",
        "**Extraer texto y atributos** (`.text`, `['href']`).",
        "**Respetar `robots.txt`** y rate limit (delay entre requests).",
        "**Identificar** cuándo scraping es buena idea vs cuándo buscar otra fuente (API, dataset público).",
    ],
    temas=[
        ("HTTP → HTML → parser tree", "Cómo funciona scraping."),
        ("BeautifulSoup: find vs select", "Selectores CSS son más potentes."),
        ("Extracción de texto y atributos", "`.text`, `.get_text(strip=True)`, `['href']`."),
        ("Páginas dinámicas (JS) — `requests` no las renderiza", "Para eso: Playwright/Selenium."),
        ("robots.txt — qué dice y por qué respetar", "`User-agent`, `Disallow`, `Crawl-delay`."),
        ("Ética: ToS, rate limiting, datos personales", "Lo que sí, lo que no."),
    ],
    dataset=(
        "Página HTML simple servida desde un string en el notebook (sin tocar internet). "
        "Ejercicios opcionales con `https://quotes.toscrape.com` (sitio diseñado para practicar)."
    ),
    ejercicios=[
        "**Parsea HTML local.** Crea un HTML con 3 productos (`<div class='product'>`). Extrae nombres y precios con `find_all`.",
        "**Selectores CSS.** Lo mismo con `soup.select('.product .price')`.",
        "**Tabla a DataFrame.** `pd.read_html(url)` para una tabla HTML — bonus: `requests` + `BeautifulSoup` para tablas custom.",
        "**Scrape ético.** Scrapea `quotes.toscrape.com` (público, diseñado para esto). Respeta `Crawl-delay`. 3 páginas con `time.sleep(1)` entre cada una.",
        "**Inspeccionar robots.txt.** Lee `https://quotes.toscrape.com/robots.txt` con requests. Identifica qué paths están `Disallow`.",
    ],
    homework=(
        "Notebook: (a) HTML local con 5 productos, extrae nombre/precio/url; (b) scrape "
        "`quotes.toscrape.com` (3 páginas, con delay); (c) consulta robots.txt y razona; "
        "(d) listado de 3 escenarios cuando scrapear es buena idea y 3 cuando no."
    ),
    homework_criterio="Scraping respeta delays. Análisis de robots.txt correcto.",
    referencias=[
        "Mitchell, *Web Scraping with Python* 2e, caps. 1-3.",
        "[BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)",
        "[quotes.toscrape.com](https://quotes.toscrape.com/) (sitio para practicar)",
        "[Google — robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)",
    ],
    siguiente=("../parte-1-machine-learning-clasico/047-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based", "Parte 1 — Panorama del ML"),
    cells=[
        Cell("md", "# Clase 046 — Web scraping con BeautifulSoup\n\n**Parte 0** · Mitchell caps. 1-3.\n\n> 🎯 Extraer datos cuando no hay API. Con respeto: robots.txt, delays, ética.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup\n\n```bash\npip install beautifulsoup4 lxml\n```"),
        Cell("code", "import requests\nimport time\nfrom bs4 import BeautifulSoup\nprint(f'bs4 OK')"),
        Cell("md", "## 1️⃣ Parsear HTML\n\n```python\nsoup = BeautifulSoup(html_string, 'html.parser')\n# alternativas: 'lxml' (más rápido), 'html5lib' (más permisivo)\n```"),
        Cell("code", "html = '''\n<html><body>\n  <div class=\"product\" data-id=\"1\">\n    <h2 class=\"name\">Libro Python</h2>\n    <span class=\"price\">$30</span>\n    <a href=\"/libros/python\">ver</a>\n  </div>\n  <div class=\"product\" data-id=\"2\">\n    <h2 class=\"name\">Guitarra</h2>\n    <span class=\"price\">$800</span>\n    <a href=\"/musica/guitarra\">ver</a>\n  </div>\n  <div class=\"product\" data-id=\"3\">\n    <h2 class=\"name\">Auriculares</h2>\n    <span class=\"price\">$120</span>\n    <a href=\"/audio/auriculares\">ver</a>\n  </div>\n</body></html>\n'''\n\nsoup = BeautifulSoup(html, 'html.parser')\nfor prod in soup.find_all('div', class_='product'):\n    nombre = prod.find('h2', class_='name').get_text(strip=True)\n    precio = prod.find('span', class_='price').get_text(strip=True)\n    url    = prod.find('a')['href']\n    id_    = prod['data-id']\n    print(f'id={id_}  {nombre:20s}  {precio:6s}  {url}')"),
        Cell("md", "## 2️⃣ Selectores CSS — `soup.select(...)`\n\nMás potentes que `find_all` para queries complejos:\n\n```python\nsoup.select('.product')                    # class\nsoup.select('#main')                        # id\nsoup.select('div > a')                      # hijo directo\nsoup.select('div.product .price')          # descendiente con class\nsoup.select('a[href^=\"/\"]')                 # atributo con prefijo\nsoup.select('div:nth-of-type(2)')          # pseudo-class\n```"),
        Cell("code", "for precio in soup.select('.product .price'):\n    print(precio.get_text(strip=True))"),
        Cell("md", "## 3️⃣ Páginas dinámicas (JS) — limitación\n\n`requests` descarga el HTML **original** del servidor, sin ejecutar JavaScript. Si el contenido aparece tras AJAX/SPA frameworks (React, Vue), no lo verás.\n\n**Soluciones**:\n- `playwright` o `selenium`: navegadores headless que renderizan JS.\n- Inspeccionar Network tab del DevTools — muchas veces la SPA hace XHR a un endpoint JSON que puedes consumir directo con requests (mejor que scraping)."),
        Cell("md", "## 4️⃣ Tabla HTML → DataFrame\n\npandas tiene un shortcut para tablas: `pd.read_html(url)` devuelve lista de DataFrames, uno por `<table>` en la página."),
        Cell("code", "import pandas as pd\nhtml_tabla = '''\n<table>\n  <tr><th>producto</th><th>precio</th></tr>\n  <tr><td>A</td><td>100</td></tr>\n  <tr><td>B</td><td>200</td></tr>\n  <tr><td>C</td><td>150</td></tr>\n</table>\n'''\ntablas = pd.read_html(html_tabla)\nprint(tablas[0])"),
        Cell("md", "## 5️⃣ Ética y `robots.txt`\n\n**`robots.txt`** vive en la raíz del dominio (`https://sitio.com/robots.txt`). Indica qué paths puede crawlear cada bot:\n\n```\nUser-agent: *\nDisallow: /private/\nDisallow: /admin/\nAllow: /public/\nCrawl-delay: 1\n```\n\n**Reglas mínimas**:\n1. Lee `robots.txt` antes de scrapear (`urllib.robotparser` lo parsea).\n2. **Respeta `Crawl-delay`** y, si no existe, pon mínimo 1s entre requests.\n3. Identifica tu bot con `User-Agent` honesto (`'MyBot 1.0 (contact: email@example.com)'`).\n4. **No scrapees datos personales** sin base legal (GDPR/LGPD).\n5. **Lee los ToS** — algunos sitios prohíben scraping explícitamente.\n6. Si hay API oficial, **úsala**. Es más fácil para ti y respeta al proveedor."),
        Cell("md", "## 6️⃣ Cuándo scrapear vs cuándo NO\n\n**Sí**:\n- No hay API y los datos son públicos.\n- Sitio diseñado para esto (`quotes.toscrape.com`, datasets gov.).\n- Análisis personal/educativo a pequeña escala.\n\n**No**:\n- Hay API oficial → úsala.\n- Datos personales sin consentimiento.\n- Volumen masivo que afecta al sitio.\n- ToS lo prohíbe.\n- Contenido con copyright que vas a redistribuir."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Parseo HTML con BeautifulSoup\n- [ ] Uso find/find_all y CSS selectors\n- [ ] Extraigo texto y atributos\n- [ ] Sé que `requests` no ejecuta JS\n- [ ] Respeto robots.txt y rate limiting\n- [ ] Conozco los límites éticos/legales"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. HTML local, quotes.toscrape, robots.txt, ética."),
        Cell("md", "## 🔗 Referencias\n\n- Mitchell, *Web Scraping with Python* 2e\n- [BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)\n- [quotes.toscrape.com](https://quotes.toscrape.com/)\n\n---\n\n## 🎉 ¡Parte 0 completada!\n\nHas cubierto los 46 fundamentos: setup, Python, NumPy, pandas, visualización, SQL/NoSQL, APIs y scraping. Tienes todo lo que el resto del programa asume.\n\n➡️ **Siguiente:** [Parte 1 — Machine Learning clásico](../../parte-1-machine-learning-clasico/README.md) (43 clases)"),
    ],
    definiciones=[
        ("Web scraping", "Extracción programática de datos de páginas HTML cuando no hay API. Pipeline típico: descargar HTML con `requests`, parsear con `BeautifulSoup`, extraer con selectores."),
        ("BeautifulSoup", "Parser HTML tolerante a errores. `soup = BeautifulSoup(html, 'html.parser')`. Permite navegar el árbol y buscar por tag, atributo o selector CSS."),
        ("CSS selector", "Sintaxis para localizar elementos: `'.class'`, `'#id'`, `'tag'`, `'parent > child'`, `'tag[attr=val]'`. Usados con `soup.select(...)`. Más expresivos que `find_all`."),
        ("DOM (Document Object Model)", "Representación en árbol del HTML. Cada tag es un nodo; tiene padre, hermanos, hijos. BeautifulSoup navega este árbol con `.parent`, `.next_sibling`, `.find_all`, etc."),
        ("`robots.txt`", "Archivo en raíz del dominio (`/robots.txt`) que declara qué paths pueden crawlear los bots. Estándar de facto; respetarlo es **legalmente** importante (variable por jurisdicción) y **éticamente** siempre."),
        ("JS rendering", "Páginas SPA (React, Vue) cargan contenido vía JavaScript tras el HTML inicial. `requests` solo trae el HTML inicial — JS no se ejecuta. **Solución**: Playwright o Selenium (navegador headless)."),
    ],
    errores_comunes=[
        ("`soup.find('div')` devuelve None aunque hay divs", "Buscas un atributo específico que no matchea. **Fix**: imprime `soup.prettify()[:500]` para ver el HTML real recibido; verifica clase/atributo."),
        ("Scrapeo y recibo HTML distinto al que veo en el navegador", "El sitio renderiza con JavaScript. `requests` no ejecuta JS. **Fix**: inspecciona Network tab del navegador — quizás hay endpoint JSON que puedes consumir directo. Si no, Playwright/Selenium."),
        ("HTTP 403 Forbidden", "El sitio detecta tu bot (User-Agent vacío o sospechoso). **Fix**: `headers={'User-Agent': 'Mozilla/5.0 ...'}` honesto, respeta robots.txt, rate limit."),
        ("Site funciona en navegador pero scraper devuelve `Captcha`", "Anti-bot agresivo (Cloudflare, reCAPTCHA). **Fix**: respeta sus términos — si te bloquean, claramente NO quieren scraping. Busca API oficial."),
        ("Encoding raro (acentos `Ã¡`)", "Pandas/requests dedujo encoding mal. **Fix**: `r.encoding = 'utf-8'` antes de `r.text`, o usa `r.content` (bytes) y decodifica explícito."),
    ],
    faq=[
        ("¿Scraping es legal?",
         "**Depende**: jurisdicción, ToS del sitio, naturaleza del dato. Datos personales = casi siempre regulado (GDPR/LGPD). Datos públicos sin ToS prohibitivo = generalmente OK. **Consulta abogado** para casos serios."),
        ("¿`find_all` o `select`?",
         "**`select`** (CSS selectors) — más potente, sintaxis estándar web, más legible. **`find_all`** para casos simples o cuando integras con código heredado."),
        ("¿Cómo descargo imágenes?",
         "`r = requests.get(url_imagen); open('img.jpg', 'wb').write(r.content)`. Para muchas, usa Session + thread pool."),
        ("¿Scrapy vs BeautifulSoup?",
         "**BeautifulSoup**: librería de parsing. Una página, una request. **Scrapy**: framework completo (crawler, pipelines, throttling). Para proyectos serios (miles de páginas), Scrapy."),
        ("¿Y si el sitio me bloquea?",
         "Respeta. Aumentar agresividad (proxies, rotating User-Agents) puede ser ilegal en algunas jurisdicciones (CFAA en USA). Considera: ¿realmente vale la pena? ¿hay otra fuente?"),
    ],
))


def main() -> int:
    print(f"Generating {len(SPECS)} classes")
    for s in SPECS:
        write_class(s)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
