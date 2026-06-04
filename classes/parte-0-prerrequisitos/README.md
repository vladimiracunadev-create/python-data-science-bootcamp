# Parte 0 — Prerrequisitos: Python + NumPy + pandas + visualización + SQL + APIs

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏭️ Parte siguiente](../parte-1-machine-learning-clasico/README.md)

**49 clases** · ~11–13 semanas a ritmo moderado · ✅ Contenido completo**

**Fuentes (por bloque):**

- **VanderPlas** ([*Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/)) — NumPy (014–021), pandas (022–032), visualización (033–039).
- **Ramalho** ([*Fluent Python* 2e](https://www.fluentpython.com/)) — Python idiomático (006–013).
- **Tanimura** ([*SQL for Data Scientists*](https://www.oreilly.com/library/view/sql-for-data/9781492088776/)) — SQL (041–042).
- **Mitchell** ([*Web Scraping with Python* 2e](https://www.oreilly.com/library/view/web-scraping-with/9781491985564/)) — clase 046.
- **Docs oficiales** (Python, requests, BeautifulSoup, folium/plotly, MongoDB) cuando son la mejor referencia.

Cada clase tiene su `README.md` con objetivo, resultados de aprendizaje verificables, dataset recomendado, 5 ejercicios y homework con criterio de aceptación. Cada `notebook.ipynb` trae 10–18 celdas mezclando markdown explicativo + código ejecutable (basado en VanderPlas/Ramalho donde aplica).

**✨ Ampliación pedagógica (v2.2.0):** todas las 49 clases incluyen además tres secciones nuevas:

- **📖 Definiciones y características** — términos técnicos con explicación y características clave.
- **⚠️ Errores comunes** — tabla de síntomas/mensajes con causa y solución concretas (los bugs que ven los alumnos en clase).
- **❓ Preguntas frecuentes** — FAQs auténticas que aparecen al estudiar cada tema.

---

## 🎯 ¿De qué trata esta parte?

Esta parte construye **toda la base técnica** que el resto del programa da por sentada. No es "introducción a Python" — es el conjunto mínimo de herramientas con las que un data scientist trabaja a diario: el lenguaje, los entornos reproducibles, el control de versiones, el stack numérico (NumPy / pandas), la visualización (matplotlib / seaborn / plotly), el acceso a datos (SQL, NoSQL, APIs, scraping) y la disciplina de proyecto (logging, type hints, manejo de errores, estructura cookiecutter).

El recorrido es deliberadamente extenso porque cada laguna acá se convierte en deuda invisible que aparece después en Parte 1 (ML clásico) y Parte 2 (Deep Learning). Quien complete bien esta parte puede leer cualquier notebook profesional, reproducirlo, modificarlo y debuggearlo.

## 🧩 Problemas que resuelve

- Configurar un entorno Python aislado y reproducible (venv / uv / conda) sin colisiones de dependencias.
- Manipular datasets tabulares de tamaño medio (cientos de miles de filas) sin caer en bucles ni código lento.
- Limpiar, transformar y unir datos sucios usando pandas (faltantes, tipos, formatos, joins, groupby).
- Producir gráficos publicables (no solo `df.plot()`) con matplotlib + seaborn, incluyendo mapas geográficos.
- Consultar bases relacionales con SQL avanzado (CTEs, window functions) y conectarlas desde Python.
- Acceder a datos externos vía APIs REST y, cuando no hay API, mediante web scraping responsable.

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Levantar un proyecto nuevo con estructura reproducible, dependencias fijadas y `pre-commit` en menos de 10 minutos.
- Escribir código NumPy/pandas vectorizado (sin loops) y justificar por qué es más rápido.
- Diseñar visualizaciones efectivas que comuniquen una conclusión, no solo "que se vean lindas".
- Escribir consultas SQL no triviales (window functions, CTEs recursivas) y traducirlas a pandas y viceversa.
- Extraer datos de una API o sitio web y dejarlos listos para análisis, manejando paginación y rate-limiting.

## 🗺️ Estructura temática

- **Setup y reproducibilidad** — clases 001–005 — instalación, Jupyter, Git/GitHub, estructura de proyecto, editor.
- **Python para data science** — clases 006–013 — tipos, comprehensions, funciones, OOP, pathlib, logging, type hints.
- **NumPy (8 clases)** — clases 014–021 — creación, ufuncs, agregaciones, broadcasting, masks, álgebra lineal, aleatoriedad.
- **pandas + Polars + Parquet/Arrow (14 clases)** — clases 022–034 — Series/DataFrame, indexación, joins, groupby, pivot, strings, series de tiempo.
- **Visualización** — clases 035–042 — matplotlib en profundidad, seaborn, visualización geográfica.
- **SQL** — clases 043–045 — desde fundamentos a window functions y conexión desde Python.
- **Acceso a datos externos** — clases 046–048 + 049 (async/httpx moderno) — MongoDB, APIs REST, web scraping con BeautifulSoup.

## 📚 Índice de clases (49)

- [001 — Instalación de Python 3.12+ y entornos virtuales (venv, uv, conda)](001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda/README.md)
- [002 — Jupyter y JupyterLab — kernels, magics, debugging, profiling](002-jupyter-y-jupyterlab-kernels-magics-debugging-profiling/README.md)
- [003 — Git y GitHub para data scientists](003-git-y-github-para-data-scientists/README.md)
- [004 — Estructura reproducible de proyecto (cookiecutter-data-science)](004-estructura-reproducible-de-proyecto-cookiecutter-data-science/README.md)
- [005 — VS Code / Cursor para Python y Jupyter](005-vs-code-cursor-para-python-y-jupyter/README.md)
- [006 — Python: tipos, estructuras, control de flujo](006-python-tipos-estructuras-control-de-flujo/README.md)
- [007 — Comprehensions y generadores](007-comprehensions-y-generadores/README.md)
- [008 — Funciones: args, kwargs, lambdas, closures](008-funciones-args-kwargs-lambdas-closures/README.md)
- [009 — Manejo de excepciones y context managers](009-manejo-de-excepciones-y-context-managers/README.md)
- [010 — OOP básico, dataclasses, herencia](010-oop-basico-dataclasses-herencia/README.md)
- [011 — pathlib, lectura y escritura de archivos](011-pathlib-lectura-y-escritura-de-archivos/README.md)
- [012 — Logging](012-logging/README.md)
- [013 — Type hints y mypy](013-type-hints-y-mypy/README.md)
- [014 — NumPy: tipos, creación, atributos](014-numpy-tipos-creacion-atributos/README.md)
- [015 — NumPy: ufuncs y vectorización](015-numpy-ufuncs-y-vectorizacion/README.md)
- [016 — NumPy: agregaciones](016-numpy-agregaciones/README.md)
- [017 — NumPy: broadcasting](017-numpy-broadcasting/README.md)
- [018 — NumPy: boolean masks y fancy indexing](018-numpy-boolean-masks-y-fancy-indexing/README.md)
- [019 — NumPy: ordenamiento y búsqueda](019-numpy-ordenamiento-y-busqueda/README.md)
- [020 — NumPy: álgebra lineal con numpy.linalg](020-numpy-algebra-lineal-con-numpy-linalg/README.md)
- [021 — NumPy: aleatoriedad y semillas](021-numpy-aleatoriedad-y-semillas/README.md)
- [022 — Pandas: Series y DataFrame](022-pandas-series-y-dataframe/README.md)
- [023 — Pandas: indexación (loc, iloc, at, iat)](023-pandas-indexacion-loc-iloc-at-iat/README.md)
- [024 — Pandas: operaciones y alineación](024-pandas-operaciones-y-alineacion/README.md)
- [025 — Pandas: datos faltantes](025-pandas-datos-faltantes/README.md)
- [026 — Pandas: MultiIndex](026-pandas-multiindex/README.md)
- [027 — Pandas: concat, merge, join](027-pandas-concat-merge-join/README.md)
- [028 — Pandas: groupby (split-apply-combine)](028-pandas-groupby-split-apply-combine/README.md)
- [029 — Pandas: pivot tables y crosstab](029-pandas-pivot-tables-y-crosstab/README.md)
- [030 — Pandas: operaciones vectorizadas sobre strings](030-pandas-operaciones-vectorizadas-sobre-strings/README.md)
- [031 — Pandas: series de tiempo, resampling, rolling](031-pandas-series-de-tiempo-resampling-rolling/README.md)
- [032 — Pandas: eval y query](032-pandas-eval-y-query/README.md)
- [033 — Polars: DataFrames modernos](033-polars-dataframes-modernos/README.md)
- [034 — Parquet, Arrow, PyArrow, DuckDB](034-parquet-arrow-pyarrow-duckdb/README.md)
- [035 — Matplotlib: anatomía figura/axes](035-matplotlib-anatomia-figura-axes/README.md)
- [036 — Matplotlib: line, scatter, bar, histogram, boxplot](036-matplotlib-line-scatter-bar-histogram-boxplot/README.md)
- [037 — Matplotlib: subplots y gridspec](037-matplotlib-subplots-y-gridspec/README.md)
- [038 — Matplotlib: legends, colorbars, ticks, anotaciones](038-matplotlib-legends-colorbars-ticks-anotaciones/README.md)
- [039 — Matplotlib: stylesheets](039-matplotlib-stylesheets/README.md)
- [040 — Matplotlib: 3D plotting](040-matplotlib-3d-plotting/README.md)
- [041 — Seaborn: distribuciones, relaciones, categóricas, facetas](041-seaborn-distribuciones-relaciones-categoricas-facetas/README.md)
- [042 — Visualización geográfica (Plotly / folium)](042-visualizacion-geografica-plotly-folium/README.md)
- [043 — SQL fundamental: SELECT, WHERE, JOIN, GROUP BY, HAVING](043-sql-fundamental-select-where-join-group-by-having/README.md)
- [044 — SQL avanzado: CTEs, window functions, subqueries correlacionadas](044-sql-avanzado-ctes-window-functions-subqueries-correlacionadas/README.md)
- [045 — SQL desde Python: sqlite3, SQLAlchemy, DuckDB](045-sql-desde-python-sqlite3-sqlalchemy-duckdb/README.md)
- [046 — NoSQL: MongoDB con pymongo](046-nosql-mongodb-con-pymongo/README.md)
- [047 — APIs REST con requests](047-apis-rest-con-requests/README.md)
- [048 — Web scraping con BeautifulSoup](048-web-scraping-con-beautifulsoup/README.md)
- [049 — async / httpx / aiohttp para data scientists](049-async-httpx-aiohttp-para-data-scientists/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏭️ Parte siguiente](../parte-1-machine-learning-clasico/README.md)
