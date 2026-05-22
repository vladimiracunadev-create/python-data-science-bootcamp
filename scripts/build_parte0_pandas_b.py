"""Classes 026-029 — pandas B: MultiIndex, concat/merge/join, groupby, pivot."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="026-pandas-multiindex",
    number="026",
    title="Pandas: MultiIndex",
    duration="75 min",
    source="VanderPlas, **cap. 3** § 3.6 *Hierarchical Indexing*.",
    objetivo=(
        "Que el alumno use índices jerárquicos (MultiIndex) cuando hay estructura natural en "
        "los datos (país × ciudad, año × mes, sector × empresa). Saber cuándo aporta vs cuándo "
        "complica — el 80% del tiempo en data science aplanado es mejor."
    ),
    resultados=[
        "**Crear MultiIndex** desde tuplas, arrays, producto cartesiano (`from_product`).",
        "**Indexar** con `.loc[(nivel1, nivel2)]` y `.loc[:, ('grupo', 'col')]`.",
        "**Aplanar y reconstruir** con `unstack()`, `stack()`, `reset_index()`.",
        "**Decidir** cuándo MultiIndex aporta (groupby con múltiples claves devuelve uno automáticamente) y cuándo es más legible aplanar.",
        "**Renombrar niveles** con `rename(level=...)` y reordenarlos con `swaplevel`.",
    ],
    temas=[
        ("MultiIndex: motivación", "Datos con jerarquía natural."),
        ("Construcción: tuples, arrays, from_product", "3 formas comunes."),
        ("Indexación: tuple selector", "`.loc[('A', 2024)]`."),
        ("`stack` / `unstack` — pivot rápido", "Mover niveles entre filas y columnas."),
        ("groupby + multiindex resultado", "groupby con 2+ claves devuelve MultiIndex."),
        ("Cuándo aplanar", "Para CSV de salida, plot, scikit-learn."),
    ],
    dataset="Sintético: ventas por país/año.",
    ejercicios=[
        "**Construye desde tuplas.** Crea DataFrame con index `[(España, 2023), (España, 2024), (Chile, 2023), (Chile, 2024)]` y 2 cols ventas/clientes.",
        "**`from_product`.** Mismo con `pd.MultiIndex.from_product([paises, años])`.",
        "**Acceso jerárquico.** `df.loc['España']`, `df.loc[('España', 2024)]`. Compara con `df.xs(2024, level=1)` para slice por nivel.",
        "**`unstack` y `stack`.** Convierte tu MultiIndex en wide (años como columnas) y de vuelta.",
        "**groupby produce MultiIndex.** Carga penguins, agrupa por `(species, sex)` y agrega `mean()`. Aplana con `reset_index()`.",
    ],
    homework=(
        "Notebook con ventas trimestre×región sintéticas (4 trimestres × 3 regiones × 2 años): "
        "(a) construir con `from_product`; (b) acceso a un trimestre específico; (c) total por "
        "región (unstack); (d) groupby penguins por (species, sex) → MultiIndex → aplanar."
    ),
    homework_criterio="MultiIndex con shape correcto; unstack/stack reversibles.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.6.",
        "[pandas MultiIndex user guide](https://pandas.pydata.org/docs/user_guide/advanced.html)",
    ],
    siguiente=("027-pandas-concat-merge-join", "Pandas: concat, merge, join"),
    cells=[
        Cell("md", "# Clase 026 — MultiIndex\n\n**Parte 0** · VanderPlas cap. 3 § 3.6.\n\n> 🎯 Índices jerárquicos cuando hay estructura natural. Aplanar cuando complica.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Motivación\n\nDatos con jerarquía natural (país→ciudad, año→mes, sector→empresa) caben en un índice de 1 nivel **aplanando**, pero el MultiIndex deja explícita la estructura y facilita el slicing por nivel."),
        Cell("code", "# 3 formas de construir un MultiIndex\n\n# (a) Desde tuplas\nidx_a = pd.MultiIndex.from_tuples([\n    ('España', 2023), ('España', 2024),\n    ('Chile', 2023),  ('Chile', 2024),\n])\n\n# (b) Desde arrays\nidx_b = pd.MultiIndex.from_arrays([\n    ['España', 'España', 'Chile', 'Chile'],\n    [2023, 2024, 2023, 2024],\n], names=['país', 'año'])\n\n# (c) Producto cartesiano (más limpio si todas las combinaciones existen)\nidx_c = pd.MultiIndex.from_product([['España', 'Chile'], [2023, 2024]], names=['país', 'año'])\n\nprint('idx_c:')\nprint(idx_c)"),
        Cell("md", "## 2️⃣ DataFrame con MultiIndex"),
        Cell("code", "df = pd.DataFrame({\n    'ventas'  : [100, 120, 80, 95],\n    'clientes': [50, 65, 40, 48],\n}, index=idx_c)\nprint(df)"),
        Cell("md", "## 3️⃣ Indexación jerárquica"),
        Cell("code", "# Por primer nivel\nprint('df.loc[\"España\"]:')\nprint(df.loc['España'])\n\n# Por tupla completa\nprint('\\ndf.loc[(\"España\", 2024)]:')\nprint(df.loc[('España', 2024)])\n\n# Slice por segundo nivel con xs\nprint('\\ndf.xs(2024, level=\"año\"):')\nprint(df.xs(2024, level='año'))"),
        Cell("md", "## 4️⃣ `unstack` y `stack` — pivot rápido\n\n- `unstack(level)` mueve un nivel del **index** a **columnas** (wide format).\n- `stack(level)` lo opuesto (long format).\n\nÚtil para visualización rápida."),
        Cell("code", "wide = df.unstack(level='año')   # años como columnas\nprint('wide (unstack):')\nprint(wide)\n\nlong = wide.stack(future_stack=True)   # vuelve a long\nprint('\\nde vuelta a long (stack):')\nprint(long)"),
        Cell("md", "## 5️⃣ groupby produce MultiIndex automáticamente\n\nCuando agrupas por 2+ columnas, pandas devuelve un MultiIndex:"),
        Cell("code", "# Demo sin penguins (sintético)\nventas = pd.DataFrame({\n    'tienda' : ['A', 'A', 'B', 'B', 'A', 'B'],\n    'mes'    : ['ene', 'feb', 'ene', 'feb', 'ene', 'feb'],\n    'monto'  : [100, 120, 80, 95, 110, 90],\n})\n\nagg = ventas.groupby(['tienda', 'mes'])['monto'].sum()\nprint('groupby (MultiIndex Series):')\nprint(agg)\nprint(f'\\ntype: {type(agg.index).__name__}')\n\n# Aplanar a DataFrame normal\nflat = agg.reset_index()\nprint('\\nflat (DataFrame):')\nprint(flat)"),
        Cell("md", "## 6️⃣ Cuándo aplanar\n\n- **Para CSV de salida**: cliente final espera tabla rectangular.\n- **Para plot**: matplotlib/seaborn esperan columnas, no niveles.\n- **Para scikit-learn**: features son columnas planas.\n- **Para joins**: merge funciona mejor con index plano.\n\n**Cuándo dejar MultiIndex**: análisis interactivo donde el slicing por nivel es frecuente."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé construir MultiIndex con tuples/arrays/from_product\n- [ ] Indexo con `.loc[('a', 'b')]` y `df.xs(v, level=...)`\n- [ ] Convierto wide ↔ long con `unstack`/`stack`\n- [ ] Reconozco que groupby con N keys devuelve MultiIndex\n- [ ] Aplano con `reset_index` cuando aporta"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Ventas trimestre×región, accesos por nivel, unstack/stack, groupby penguins."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.6\n- [MultiIndex guide](https://pandas.pydata.org/docs/user_guide/advanced.html)\n\n➡️ **Siguiente:** [027 — concat, merge, join](../027-pandas-concat-merge-join/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="027-pandas-concat-merge-join",
    number="027",
    title="Pandas: concat, merge, join",
    duration="90 min",
    source="VanderPlas, **cap. 3** §§ 3.7–3.8 *Combining Datasets: Concat/Merge*.",
    objetivo=(
        "Que el alumno **junte datasets** correctamente: `concat` (apilado simple), `merge` "
        "(SQL-style joins) y `join` (atajo por index). El error más común es usar el join "
        "equivocado y obtener duplicados o filas perdidas — saber qué tipo (inner/left/right/outer) "
        "evita semanas de bugs."
    ),
    resultados=[
        "**Apilar** DataFrames con `pd.concat` por filas (`axis=0`) o columnas (`axis=1`).",
        "**Hacer joins SQL-style** con `pd.merge`: inner, left, right, outer, cross.",
        "**Diagnosticar** duplicados generados por merge con `validate='one_to_one' | 'many_to_one' | …`.",
        "**Joinear por index** con `df1.join(df2)` (atajo para merge por index).",
        "**Usar `indicator=True`** para saber qué filas vienen de cada lado del merge.",
    ],
    temas=[
        ("`concat` axis=0 (filas) vs axis=1 (columnas)", "Apilado simple con alineación de index."),
        ("`merge` how='inner'/'left'/'right'/'outer'", "Los 4 tipos de join SQL."),
        ("`on` vs `left_on`/`right_on`", "Cuando los nombres de columna difieren."),
        ("`validate` para evitar duplicación", "1:1, 1:m, m:1, m:m."),
        ("`indicator=True` para auditar", "Columna `_merge` con left_only/right_only/both."),
        ("`df.join` por index", "Atajo idiomático."),
    ],
    dataset="Sintético: tabla de clientes + tabla de órdenes (relación 1:N).",
    ejercicios=[
        "**Concat por filas.** 3 DataFrames mensuales con mismas columnas → uno anual. `ignore_index=True`.",
        "**Inner join.** Clientes + órdenes por `cliente_id`. Verifica que solo aparecen clientes con al menos 1 orden.",
        "**Left join.** Clientes + órdenes, conservando clientes sin órdenes (NaN en cols de orden).",
        "**Detectar duplicados.** Provoca un merge muchos-a-muchos no intencional. Usa `validate='one_to_many'` para que falle si hay duplicación oculta.",
        "**`indicator=True`.** Auditar cuántas filas son left_only / right_only / both.",
    ],
    homework=(
        "Notebook con clientes (10) + órdenes (25): (a) 4 tipos de join con `_merge` indicator; "
        "(b) tabla con conteo de cada tipo; (c) detección de relación con `validate`; "
        "(d) join por index con `df.join`."
    ),
    homework_criterio="Counts de cada join coherentes (inner ≤ left ≤ outer). `validate` lanza excepción si la relación esperada falla.",
    referencias=[
        "VanderPlas, **cap. 3** §§ 3.7-3.8.",
        "[pandas Merge user guide](https://pandas.pydata.org/docs/user_guide/merging.html)",
    ],
    siguiente=("028-pandas-groupby-split-apply-combine", "Pandas: groupby (split-apply-combine)"),
    cells=[
        Cell("md", "# Clase 027 — concat, merge, join\n\n**Parte 0** · VanderPlas cap. 3 §§ 3.7-3.8.\n\n> 🎯 Juntar datasets sin generar duplicados ni perder filas. SQL-style joins en pandas.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd"),
        Cell("md", "## 1️⃣ `concat` — apilado simple\n\nAlinea por index (`axis=0` apila filas) o por columnas (`axis=1`)."),
        Cell("code", "ene = pd.DataFrame({'tienda': ['A','B'], 'monto': [100, 80]})\nfeb = pd.DataFrame({'tienda': ['A','B'], 'monto': [110, 90]})\nmar = pd.DataFrame({'tienda': ['A','B'], 'monto': [105, 95]})\n\ntrim = pd.concat([ene, feb, mar], ignore_index=True)\nprint(trim)\n\n# Con keys para mantener trazabilidad\ntrim_keys = pd.concat([ene, feb, mar], keys=['ene', 'feb', 'mar'])\nprint('\\ncon keys (MultiIndex):')\nprint(trim_keys)"),
        Cell("md", "## 2️⃣ Los 4 tipos de join (SQL)\n\n```\nA  |  B          INNER     LEFT      RIGHT     OUTER\n1  |  10         A∩B       A         B         A∪B\n2  |  20         (común)   (todo A)  (todo B)  (todos, NaN donde falta)\n3  |  --\n--|  30\n```"),
        Cell("code", "clientes = pd.DataFrame({\n    'cliente_id': [1, 2, 3, 4],\n    'nombre'    : ['Ana', 'Bob', 'Cris', 'Dan'],\n})\nordenes = pd.DataFrame({\n    'orden_id'  : [101, 102, 103, 104, 105],\n    'cliente_id': [1, 1, 2, 5, 5],   # 5 no está en clientes; 3 y 4 no tienen orden\n    'monto'     : [50, 80, 30, 40, 60],\n})\n\nprint('clientes:')\nprint(clientes)\nprint('\\nordenes:')\nprint(ordenes)"),
        Cell("code", "# INNER join: solo clientes CON órdenes\nprint('--- INNER ---')\nprint(pd.merge(clientes, ordenes, on='cliente_id', how='inner'))\n\n# LEFT join: TODOS los clientes, NaN si no tienen orden\nprint('\\n--- LEFT ---')\nprint(pd.merge(clientes, ordenes, on='cliente_id', how='left'))\n\n# OUTER: todos los clientes Y todas las órdenes\nprint('\\n--- OUTER ---')\nprint(pd.merge(clientes, ordenes, on='cliente_id', how='outer'))"),
        Cell("md", "## 3️⃣ `validate` — atajo anti-bugs\n\nDeclara qué relación **esperas** (`1:1`, `1:m`, `m:1`, `m:m`); si los datos no la cumplen, pandas lanza excepción **antes** de generar duplicados."),
        Cell("code", "# Esperamos que cada cliente tenga muchas órdenes (1:m)\nresult = pd.merge(clientes, ordenes, on='cliente_id', how='left', validate='one_to_many')\nprint('OK (1:m válido)')\n\n# Si esperaras 1:1 cuando realmente es 1:m, falla:\ntry:\n    pd.merge(clientes, ordenes, on='cliente_id', validate='one_to_one')\nexcept pd.errors.MergeError as e:\n    print(f'\\nMergeError correcto: {e}')"),
        Cell("md", "## 4️⃣ `indicator=True` — auditoría\n\nAgrega columna `_merge` con `'left_only'`, `'right_only'`, `'both'`. Útil para entender qué pasó:"),
        Cell("code", "audit = pd.merge(clientes, ordenes, on='cliente_id', how='outer', indicator=True)\nprint(audit)\nprint('\\nResumen:')\nprint(audit['_merge'].value_counts())"),
        Cell("md", "## 5️⃣ `df.join` — atajo por index\n\nCuando ambos tienen el index alineado a la key del join, `df1.join(df2)` es más corto que `merge`:"),
        Cell("code", "c = clientes.set_index('cliente_id')\no = ordenes.set_index('cliente_id')\nprint('join por index:')\nprint(c.join(o, how='left'))"),
        Cell("md", "## 6️⃣ `on` con columnas distintas: `left_on`/`right_on`"),
        Cell("code", "tablaA = pd.DataFrame({'id_cliente': [1, 2], 'pais': ['ES', 'CL']})\ntablaB = pd.DataFrame({'cliente_id': [1, 2], 'plan': ['pro', 'free']})\n\nprint(pd.merge(tablaA, tablaB, left_on='id_cliente', right_on='cliente_id'))"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Distingo `concat` (apilar) de `merge` (joinear)\n- [ ] Elijo inner/left/right/outer según necesidad\n- [ ] Uso `validate` para no generar duplicados ocultos\n- [ ] Uso `indicator=True` para auditar el merge\n- [ ] Conozco `df.join` como atajo por index"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 4 joins con indicator, validate, join por index."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 §§ 3.7-3.8\n- [pandas Merge guide](https://pandas.pydata.org/docs/user_guide/merging.html)\n\n➡️ **Siguiente:** [028 — groupby](../028-pandas-groupby-split-apply-combine/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="028-pandas-groupby-split-apply-combine",
    number="028",
    title="Pandas: groupby (split-apply-combine)",
    duration="90 min",
    source="VanderPlas, **cap. 3** § 3.9 *Aggregation and Grouping*.",
    objetivo=(
        "Que el alumno aplique el patrón **split-apply-combine** que es **el** patrón "
        "fundamental de análisis tabular: dividir por grupo, aplicar función, recombinar. "
        "Saber elegir entre `agg`, `transform`, `filter` y `apply` — cada uno tiene su rol."
    ),
    resultados=[
        "**Agrupar** por una o más columnas con `groupby` y aplicar agregaciones (`sum`, `mean`, `count`).",
        "**Usar `agg` con dict** para distintas funciones por columna: `agg({'a': 'sum', 'b': 'mean'})`.",
        "**`transform`** para preservar la shape original (broadcasting del estadístico de grupo).",
        "**`filter`** para filtrar grupos enteros según condición.",
        "**Diferenciar** los 4 métodos del groupby y elegir el correcto.",
    ],
    temas=[
        ("Split-apply-combine: el patrón", "El más común en análisis tabular."),
        ("`agg` (= aggregate)", "Reduce a una fila por grupo."),
        ("`transform`", "Misma shape — útil para imputar/normalizar por grupo."),
        ("`filter`", "Conserva grupos completos según condición."),
        ("`apply`: el más flexible, el más lento", "Cuando los 3 anteriores no alcanzan."),
        ("Múltiples columnas de agrupación", "groupby(['a','b']) → MultiIndex."),
    ],
    dataset="Palmer Penguins (groupby por species y/o sex).",
    ejercicios=[
        "**Agg básico.** Penguins agrupado por species: media de cada feature numérica.",
        "**Agg con dict.** Por species: mean de bill_length, max de body_mass, count de filas.",
        "**Transform: z-score por grupo.** Crea columna `mass_z` = z-score de body_mass dentro de su species.",
        "**Filter: solo grupos grandes.** Conserva solo species con >100 individuos.",
        "**Apply custom.** Por species, devuelve el pingüino con mayor body_mass (un DataFrame por grupo).",
    ],
    homework=(
        "Notebook con penguins: (a) agg múltiple por (species, sex); (b) transform z-score por "
        "species; (c) filter species con n>50; (d) apply que devuelva el top-3 más pesado por "
        "species; (e) tabla `groupby.size()` por sex × island."
    ),
    homework_criterio="z-score por grupo tiene media ≈ 0 y std ≈ 1 dentro de cada species.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.9.",
        "[pandas groupby user guide](https://pandas.pydata.org/docs/user_guide/groupby.html)",
        "Wickham, [\"The split-apply-combine strategy for data analysis\"](https://www.jstatsoft.org/article/view/v040i01) (J Stat Software, 2011).",
    ],
    siguiente=("029-pandas-pivot-tables-y-crosstab", "Pandas: pivot tables y crosstab"),
    cells=[
        Cell("md", "# Clase 028 — groupby (split-apply-combine)\n\n**Parte 0** · VanderPlas cap. 3 § 3.9.\n\n> 🎯 El patrón fundamental del análisis tabular. 4 métodos: agg, transform, filter, apply.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nrng = np.random.default_rng(42)\n\n# Mini-dataset penguin-like\ndf = pd.DataFrame({\n    'species': ['Adelie']*5 + ['Chinstrap']*4 + ['Gentoo']*5,\n    'sex'    : ['M','F','M','F','M', 'M','F','M','F',  'M','F','M','F','M'],\n    'masa'   : [3750, 3800, 3650, 3900, 3700,  3500, 3400, 3600, 3550,  5050, 4800, 5200, 4900, 5100],\n    'pico'   : [39.1, 39.5, 40.3, 38.8, 39.3,  46.5, 46.0, 46.8, 45.9,  48.6, 47.5, 49.0, 48.2, 48.8],\n})\nprint(df.head())"),
        Cell("md", "## 1️⃣ Split-apply-combine\n\n```\nsplit:  divide el DataFrame por valores de una columna\napply:  aplica función a cada grupo\ncombine: junta los resultados\n```\n\nEl objeto `GroupBy` no calcula nada hasta que llamas una operación (lazy):"),
        Cell("code", "g = df.groupby('species')\nprint(f'tipo: {type(g).__name__}')\nprint(f'grupos: {list(g.groups.keys())}')\nprint(f'tamaño por grupo:')\nprint(g.size())"),
        Cell("md", "## 2️⃣ `agg` — reduce a una fila por grupo"),
        Cell("code", "# Una sola función\nprint('media por species:')\nprint(g[['masa','pico']].mean().round(2))\n\n# Dict de funciones distintas\nprint('\\nagg con dict:')\nprint(g.agg({'masa': 'mean', 'pico': ['min','max']}).round(2))\n\n# Funciones nombradas (named aggregation)\nprint('\\nnamed aggregation:')\nprint(g.agg(\n    masa_media=('masa', 'mean'),\n    pico_max=('pico', 'max'),\n    n=('masa', 'count'),\n).round(2))"),
        Cell("md", "## 3️⃣ `transform` — misma shape, broadcast por grupo\n\nÚtil para crear features dentro de un grupo (z-score, ratio sobre el grupo, imputación)."),
        Cell("code", "# z-score de masa POR ESPECIE\ndf['masa_z'] = g['masa'].transform(lambda s: (s - s.mean()) / s.std())\nprint(df.round(3))\n\n# Verifica: cada grupo tiene media ≈ 0 y std ≈ 1\nprint('\\nMedia z por species:')\nprint(df.groupby('species')['masa_z'].mean().round(3))\nprint('\\nStd z por species:')\nprint(df.groupby('species')['masa_z'].std().round(3))"),
        Cell("md", "## 4️⃣ `filter` — conserva grupos completos"),
        Cell("code", "# Solo species con más de 4 individuos\nresult = g.filter(lambda x: len(x) > 4)\nprint(result['species'].value_counts())"),
        Cell("md", "## 5️⃣ `apply` — flexible y lento\n\nÚsalo cuando los 3 anteriores no alcanzan (típicamente cuando necesitas devolver un DataFrame por grupo)."),
        Cell("code", "# El más pesado de cada species\ntop = g.apply(lambda x: x.nlargest(1, 'masa'), include_groups=False)\nprint(top)"),
        Cell("md", "## 6️⃣ Múltiples columnas de agrupación"),
        Cell("code", "by_sex = df.groupby(['species', 'sex'])['masa'].mean().round(0)\nprint('media por species × sex (MultiIndex):')\nprint(by_sex)\nprint('\\nunstack(sex) → wide:')\nprint(by_sex.unstack('sex'))"),
        Cell("md", "## 🧠 Cuándo cada método\n\n| Método | Shape salida | Caso típico |\n|---|---|---|\n| `agg` | filas = #grupos | resumen estadístico |\n| `transform` | filas = original | z-score, normalizar por grupo |\n| `filter` | subset de original | excluir grupos pequeños/raros |\n| `apply` | flexible | cuando los otros 3 no alcanzan |"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Entiendo split-apply-combine\n- [ ] Uso named aggregation con `agg(...)`\n- [ ] Sé cuándo `transform` (preserva shape) vs `agg` (reduce)\n- [ ] Uso `filter` para excluir grupos enteros\n- [ ] Reservo `apply` para casos que los 3 anteriores no resuelven"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. agg múltiple, transform z-score, filter por n, apply top-3."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.9\n- [pandas groupby](https://pandas.pydata.org/docs/user_guide/groupby.html)\n- Wickham, *Split-apply-combine* (2011)\n\n➡️ **Siguiente:** [029 — pivot tables y crosstab](../029-pandas-pivot-tables-y-crosstab/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="029-pandas-pivot-tables-y-crosstab",
    number="029",
    title="Pandas: pivot tables y crosstab",
    duration="60 min",
    source="VanderPlas, **cap. 3** § 3.10 *Pivot Tables*.",
    objetivo=(
        "Que el alumno construya tablas pivot (estilo Excel) con `pivot_table` y tablas de "
        "contingencia con `crosstab`. Son atajos sobre groupby pensados para "
        "**resumen×visualización rápida**."
    ),
    resultados=[
        "**Usar `pivot_table`** con `index`, `columns`, `values`, `aggfunc`.",
        "**Añadir totales** con `margins=True`.",
        "**Construir tablas de contingencia** con `pd.crosstab` y normalizar (`normalize='all'/'index'/'columns'`).",
        "**Diferenciar** `pivot` (sin agregar) vs `pivot_table` (con aggfunc, agrega duplicados).",
        "**Visualizar** una pivot como heatmap básico para confirmar patrones.",
    ],
    temas=[
        ("`pivot` vs `pivot_table`", "pivot no acepta duplicados; pivot_table sí (agrega)."),
        ("Parámetros: index, columns, values, aggfunc", "Análogos a Excel."),
        ("`margins=True`: totales", "Útil para verificar."),
        ("`crosstab`: tabla de contingencia", "Counts entre dos categóricas."),
        ("`normalize` en crosstab", "Proporciones por fila/col/total."),
        ("Pivot → heatmap", "Detectar patrones visualmente."),
    ],
    dataset="Palmer Penguins. Sin descarga adicional.",
    ejercicios=[
        "**Pivot básico.** Penguins: índice species, columnas sex, valores body_mass mean.",
        "**Pivot con totales.** Mismo con `margins=True`.",
        "**Crosstab counts.** Counts species × island.",
        "**Crosstab normalizado.** Mismo con `normalize='index'` (% por fila).",
        "**Pivot → heatmap.** Toma un pivot table y plotéala con matplotlib `imshow`.",
    ],
    homework=(
        "Notebook con penguins: (a) pivot_table (species × island, mean body_mass); "
        "(b) crosstab species × island, count y normalizado; (c) verificación de totales con "
        "margins; (d) heatmap simple del pivot."
    ),
    homework_criterio="Pivot con shape correcto; sum de normalize='index' = 1.0 por fila.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.10.",
        "[pandas Pivot guide](https://pandas.pydata.org/docs/user_guide/reshaping.html)",
    ],
    siguiente=("030-pandas-operaciones-vectorizadas-sobre-strings", "Pandas: operaciones vectorizadas sobre strings"),
    cells=[
        Cell("md", "# Clase 029 — pivot_table y crosstab\n\n**Parte 0** · VanderPlas cap. 3 § 3.10.\n\n> 🎯 Resumen rápido tipo Excel + tablas de contingencia.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nrng = np.random.default_rng(42)\n\ndf = pd.DataFrame({\n    'species': np.repeat(['Adelie', 'Chinstrap', 'Gentoo'], [12, 8, 10]),\n    'island' : rng.choice(['Biscoe', 'Dream', 'Torgersen'], 30),\n    'sex'    : rng.choice(['M', 'F'], 30),\n    'masa'   : rng.normal(4200, 600, 30),\n})\nprint(df.head())"),
        Cell("md", "## 1️⃣ `pivot_table` — el Excel de pandas\n\n```python\ndf.pivot_table(\n    index='species',\n    columns='sex',\n    values='masa',\n    aggfunc='mean',\n    margins=True,    # totales\n)\n```"),
        Cell("code", "pivot = df.pivot_table(\n    index='species',\n    columns='sex',\n    values='masa',\n    aggfunc='mean',\n)\nprint('mean masa por species × sex:')\nprint(pivot.round(0))"),
        Cell("md", "## 2️⃣ Con totales (`margins=True`)"),
        Cell("code", "pivot_m = df.pivot_table(\n    index='species', columns='sex', values='masa',\n    aggfunc='mean', margins=True, margins_name='Total',\n)\nprint(pivot_m.round(0))"),
        Cell("md", "## 3️⃣ Múltiples aggfunc"),
        Cell("code", "pivot_multi = df.pivot_table(\n    index='species', columns='sex', values='masa',\n    aggfunc=['mean', 'count'],\n)\nprint(pivot_multi.round(0))"),
        Cell("md", "## 4️⃣ `crosstab` — contingencia\n\nCount cuando se cruzan dos categóricas:"),
        Cell("code", "ct = pd.crosstab(df['species'], df['island'])\nprint('counts species × island:')\nprint(ct)\nprint('\\nnormalizado por fila (% por species):')\nprint(pd.crosstab(df['species'], df['island'], normalize='index').round(2))\nprint('\\nnormalizado total:')\nprint(pd.crosstab(df['species'], df['island'], normalize='all').round(3))"),
        Cell("md", "## 5️⃣ `pivot` (sin agregar)\n\n`pivot` falla si hay duplicados en la combinación `(index, columns)`. **Solo úsalo cuando garantizas unicidad** — para todo lo demás, `pivot_table`."),
        Cell("md", "## 6️⃣ Heatmap rápido"),
        Cell("code", "fig, ax = plt.subplots(figsize=(6, 3))\nim = ax.imshow(pivot.values, cmap='viridis', aspect='auto')\nax.set_xticks(range(len(pivot.columns)))\nax.set_xticklabels(pivot.columns)\nax.set_yticks(range(len(pivot.index)))\nax.set_yticklabels(pivot.index)\nax.set_xlabel('sex')\nax.set_title('Mean masa (g)')\nplt.colorbar(im)\n\n# anotar valores\nfor i in range(pivot.shape[0]):\n    for j in range(pivot.shape[1]):\n        ax.text(j, i, f'{pivot.values[i,j]:.0f}', ha='center', va='center', color='white')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé construir pivot_table con index/columns/values/aggfunc\n- [ ] Añado margins=True para totales\n- [ ] Uso crosstab para counts entre categóricas\n- [ ] Normalizo crosstab por fila/col/total\n- [ ] Sé que `pivot` (sin _table) requiere unicidad"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. pivot species × island, crosstab + normalize, heatmap."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.10\n- [pandas Reshaping](https://pandas.pydata.org/docs/user_guide/reshaping.html)\n\n➡️ **Siguiente:** [030 — Operaciones sobre strings](../030-pandas-operaciones-vectorizadas-sobre-strings/README.md)"),
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
