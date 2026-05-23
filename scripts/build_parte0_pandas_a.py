"""Classes 022-025 — pandas A: Series/DataFrame, indexing, operaciones, datos faltantes.

Basado en VanderPlas cap. 3 (Data Manipulation with Pandas).
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="022-pandas-series-y-dataframe",
    number="022",
    title="Pandas: Series y DataFrame",
    duration="90 min",
    source="VanderPlas, **cap. 3**, §§ 3.1–3.2 *Introducing Pandas Objects*.",
    objetivo=(
        "Que el alumno entienda **qué es** una `Series` (ndarray + index) y un `DataFrame` "
        "(dict de Series alineadas por index), cómo se construyen desde 5 fuentes distintas, "
        "y por qué el **index** es el rasgo que distingue pandas de NumPy."
    ),
    resultados=[
        "**Crear Series y DataFrames** desde dict, lista de tuplas, arrays NumPy, CSV y desde otro DataFrame.",
        "**Inspeccionar** un DataFrame con `head`, `tail`, `info`, `describe`, `dtypes`, `shape`.",
        "**Acceder** a columnas como atributo (`df.col`) y como key (`df['col']`) — y saber cuándo cada uno falla.",
        "**Modificar el index** con `set_index`, `reset_index`, `rename`.",
        "**Convertir** Series ↔ DataFrame ↔ ndarray cuando sea necesario.",
    ],
    temas=[
        ("Series = ndarray + index", "Index permite alineación automática."),
        ("DataFrame = dict de Series alineadas", "Por eso `df['col']` devuelve Series."),
        ("Construcción desde 5 fuentes", "dict, lista de dicts, arrays, CSV, Series."),
        ("`.loc` vs `.iloc` vs `[]`", "Tres formas de acceso."),
        ("Index labels vs posición", "El bug clásico cuando el index no es 0..N."),
        ("`info` y `describe` como first-look", "Lo primero que mira un DS."),
    ],
    dataset=(
        "Palmer Penguins (descargable con seaborn/palmerpenguins) — 344 filas × 7 columnas, "
        "públicas, sin issues de licencia. Reemplaza al iris dataset."
    ),
    ejercicios=[
        "**Series desde dict.** Crea Series con población de 5 ciudades. Accede por label y por posición.",
        "**DataFrame desde dict de listas.** Construye DataFrame de 5 estudiantes (nombre, edad, nota). Inspecciona con `info()` y `describe()`.",
        "**Lee Palmer Penguins.** `pd.read_csv` desde URL pública. Reporta shape, dtypes, % de NaN por columna.",
        "**Index labeled.** Setea `species` como index. Compara `df.loc['Adelie']` vs `df.iloc[0]`.",
        "**Alineación automática.** Crea 2 Series con index parcialmente solapado. Súmalas. Observa los NaN.",
    ],
    homework=(
        "Notebook que: (a) carga Palmer Penguins y reporta `info()`, `describe()`, missing por col; "
        "(b) muestra los 3 métodos de acceso a una columna (`df.col`, `df['col']`, `df.loc[:, 'col']`); "
        "(c) cambia el index a `species`, vuelve a default con `reset_index`; (d) demuestra alineación "
        "automática sumando dos Series."
    ),
    homework_criterio="Carga sin error, los 3 accesos producen la misma Series, alineación produce NaN donde corresponde.",
    referencias=[
        "VanderPlas, **cap. 3** §§ 3.1, 3.2.",
        "[pandas user guide — DataFrame](https://pandas.pydata.org/docs/user_guide/dsintro.html)",
        "[Palmer Penguins](https://github.com/allisonhorst/palmerpenguins)",
    ],
    siguiente=("023-pandas-indexacion-loc-iloc-at-iat", "Pandas: indexación (loc, iloc, at, iat)"),
    cells=[
        Cell("md", "# Clase 022 — Pandas: Series y DataFrame\n\n**Parte 0** · VanderPlas cap. 3 §§ 3.1-3.2.\n\n> 🎯 Entender qué es Series (ndarray + index) y DataFrame (dict de Series alineadas).\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nprint('pandas:', pd.__version__)\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Series — ndarray + index\n\nUna `Series` es un ndarray 1D con un **index** asociado (labels para cada elemento). Los labels pueden ser cualquier cosa hashable: enteros, strings, fechas."),
        Cell("code", "poblacion = pd.Series({\n    'Madrid': 3_300_000,\n    'Barcelona': 1_640_000,\n    'Valencia': 800_000,\n    'Sevilla': 690_000,\n    'Zaragoza': 680_000,\n})\nprint(poblacion)\nprint()\nprint(f'index : {poblacion.index.tolist()}')\nprint(f'values: {poblacion.values}')\nprint(f'dtype : {poblacion.dtype}')"),
        Cell("md", "## 2️⃣ Acceso por label vs posición"),
        Cell("code", "# Por label (key del dict original)\nprint(f\"Madrid: {poblacion['Madrid']:,}\")\n\n# Por posición — usa .iloc\nprint(f'primera: {poblacion.iloc[0]:,}')\n\n# Slicing por label (INCLUSIVO en el final, distinto a Python)\nprint('Madrid a Valencia:')\nprint(poblacion['Madrid':'Valencia'])\n\n# Slicing por posición (exclusivo, como Python)\nprint('\\nprimeras 3 (iloc):')\nprint(poblacion.iloc[:3])"),
        Cell("md", "## 3️⃣ DataFrame — dict de Series\n\nUn `DataFrame` es como un dict de Series que **comparten el mismo index**. Por eso `df['col']` devuelve una Series."),
        Cell("code", "df = pd.DataFrame({\n    'nombre': ['Ana', 'Bob', 'Cris', 'Dan', 'Eli'],\n    'edad'  : [30, 25, 28, 35, 22],\n    'nota'  : [7.5, 6.0, 8.2, 5.8, 9.1],\n    'aprobado': [True, True, True, False, True],\n})\nprint(df)\nprint()\nprint(f'shape : {df.shape}')\nprint(f'dtypes:\\n{df.dtypes}')"),
        Cell("md", "## 4️⃣ `info()` y `describe()` — el first-look obligatorio\n\n**Antes de tocar nada**, mira:"),
        Cell("code", "print('--- info() ---')\ndf.info()\nprint()\nprint('--- describe() ---')\nprint(df.describe())"),
        Cell("md", "## 5️⃣ Las 5 formas de crear un DataFrame"),
        Cell("code", "# (1) Desde dict de listas (el más común)\na = pd.DataFrame({'x': [1,2,3], 'y': [4,5,6]})\n\n# (2) Desde lista de dicts\nb = pd.DataFrame([\n    {'x': 1, 'y': 4},\n    {'x': 2, 'y': 5},\n    {'x': 3, 'y': 6},\n])\n\n# (3) Desde ndarray 2D + nombres de columnas\nc = pd.DataFrame(rng.normal(0, 1, (3, 2)), columns=['x', 'y'])\n\n# (4) Desde Series (cada Series una columna)\ns1 = pd.Series([1,2,3], name='x')\ns2 = pd.Series([4,5,6], name='y')\nd_df = pd.concat([s1, s2], axis=1)\n\n# (5) Desde CSV/URL\n# df_csv = pd.read_csv('archivo.csv')\n\nprint('todos iguales en shape:', a.shape == b.shape == c.shape == d_df.shape)"),
        Cell("md", "## 6️⃣ Cargar Palmer Penguins desde URL"),
        Cell("code", "URL = 'https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv'\ntry:\n    peng = pd.read_csv(URL)\n    print(f'shape  : {peng.shape}')\n    print(f'cols   : {peng.columns.tolist()}')\n    print(f'\\nfirst 3 rows:')\n    print(peng.head(3))\n    print(f'\\nmissing por columna:')\n    print(peng.isna().sum())\nexcept Exception as e:\n    print(f'No se pudo descargar (¿sin internet?): {e}')\n    print('Crea un mock localmente con el dataset que tengas a mano.')"),
        Cell("md", "## 7️⃣ Index — el rasgo distintivo\n\nEl index permite **alineación automática** entre Series/DataFrames. Esto es lo que diferencia pandas de NumPy."),
        Cell("code", "a = pd.Series([1, 2, 3], index=['x', 'y', 'z'])\nb = pd.Series([10, 20, 30], index=['y', 'z', 'w'])\nprint('a:'); print(a)\nprint('b:'); print(b)\nprint('\\na + b (alineación por index):')\nprint(a + b)   # NaN donde no hay match"),
        Cell("md", "**`set_index`** mueve una columna al índice; **`reset_index`** lo devuelve a default 0..N:"),
        Cell("code", "df2 = df.set_index('nombre')\nprint('con index=nombre:')\nprint(df2)\nprint('\\ndf2.loc[\"Ana\"]:')\nprint(df2.loc['Ana'])\n\ndf3 = df2.reset_index()\nprint(f'\\nreset_index → index {df3.index.tolist()[:3]}...')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé que Series = ndarray + index\n- [ ] Sé que DataFrame = dict de Series alineadas\n- [ ] Uso `info()` + `describe()` como first-look\n- [ ] Distingo acceso por label (`.loc`) vs posición (`.iloc`)\n- [ ] Entiendo la alineación automática por index"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Carga Penguins, 3 accesos a columna, set/reset_index, alineación con NaN."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 §§ 3.1-3.2\n- [pandas DataFrame intro](https://pandas.pydata.org/docs/user_guide/dsintro.html)\n\n➡️ **Siguiente:** [023 — Indexación (loc, iloc, at, iat)](../023-pandas-indexacion-loc-iloc-at-iat/README.md)"),
    ],
    definiciones=[
        ("`Series`", "Estructura 1D = ndarray + index labelled. `s[label]` accede por etiqueta, `s.iloc[N]` por posición. Característica clave: el index permite alineación automática entre Series."),
        ("`DataFrame`", "Estructura 2D = dict de Series que **comparten el mismo index**. Cada columna puede tener su propio dtype (a diferencia de un ndarray). `df['col']` devuelve Series."),
        ("`Index`", "Estructura que etiqueta cada fila (o columna). Puede ser entero default (RangeIndex), strings, fechas (DatetimeIndex), o jerárquico (MultiIndex). Inmutable — para cambiarlo, `set_index`/`reset_index`."),
        ("Alineación automática", "Cuando operas dos Series/DataFrames, pandas alinea por **index**, NO por posición. Posiciones sin match → NaN. Esto es lo que distingue pandas de NumPy."),
        ("`dtype` en pandas", "Cada columna tiene su dtype. Tipos clásicos: `int64`, `float64`, `bool`, `object` (strings o mixto). Modernos (NA-aware): `Int64`, `Float64`, `boolean`, `string`, `category`."),
    ],
    errores_comunes=[
        ("`AttributeError` al hacer `df.column with space`", "Acceso como atributo solo funciona con nombres válidos Python (sin espacios, sin números iniciales, sin chocar con métodos como `shape`). **Fix**: siempre `df['column with space']`."),
        ("`KeyError: 'columna'` aunque está en el DataFrame", "Espacios invisibles o capitalización distinta. **Fix**: `df.columns.tolist()` para ver exactamente cómo se llama. `df.columns = df.columns.str.strip()` para limpiar."),
        ("Sumar dos Series y aparecen NaN inesperados", "Index no coincide en algunos labels. **Fix**: `s1.add(s2, fill_value=0)` o reindexa con `s.reindex(target_index, fill_value=0)`."),
        ("`pd.read_csv` infiere mal los dtypes", "Pandas adivina por las primeras filas; si hay strings en una col mayormente numérica, queda `object`. **Fix**: pasa `dtype={'col': 'float64'}` o `na_values=['N/A', '?', '']`."),
        ("`DataFrame is not callable: TypeError: 'DataFrame' object is not callable`", "Hiciste `df()` por error en vez de `df` (paréntesis sobrantes). Típico al copiar código."),
    ],
    faq=[
        ("¿`df['col']` o `df.col`?",
         "**`df['col']`** siempre — funciona con cualquier nombre, no choca con métodos. `df.col` falla con espacios, choca con `.shape`, `.head`, etc. Solo úsalo en exploración rápida."),
        ("¿Por qué `read_csv` me da `Unnamed: 0`?",
         "El CSV se guardó con index (`df.to_csv('x.csv')`). **Fix**: al leer, `pd.read_csv('x.csv', index_col=0)`. O al guardar, `df.to_csv('x.csv', index=False)`."),
        ("¿Cuándo Series y cuándo DataFrame de 1 columna?",
         "**Series** es más liviana y la mayoría de operaciones la prefieren. **DataFrame de 1 col** cuando vas a concatenar con otros DataFrames o necesitas mantener la columna nombrada. `s.to_frame()` convierte."),
        ("¿`copy()` cuándo?",
         "Cuando vas a modificar un subset y NO quieres afectar el original. `subset = df[cond].copy()`. Si solo lees, no necesitas copy — y consumes el doble de memoria."),
        ("¿Qué pasa con NaN en una columna `int`?",
         "Pandas la promueve a `float64` automáticamente (porque NumPy int no soporta NaN). Para mantener `int`: usa dtype nullable `Int64` (mayúscula) que sí permite `pd.NA`."),
    ],
))


SPECS.append(ClassSpec(
    folder="023-pandas-indexacion-loc-iloc-at-iat",
    number="023",
    title="Pandas: indexación (loc, iloc, at, iat)",
    duration="75 min",
    source="VanderPlas, **cap. 3** § 3.3 *Data Indexing and Selection*.",
    objetivo=(
        "Que el alumno **domine los 4 indexers** de pandas y elija el correcto según el caso. "
        "El bug \"`SettingWithCopyWarning`\" y el bug del slicing por label inclusivo nacen aquí — "
        "saber qué indexer usar evita ambos."
    ),
    resultados=[
        "**Usar `.loc[row_label, col_label]`** para acceso por etiqueta (inclusivo en slicing).",
        "**Usar `.iloc[row_pos, col_pos]`** para acceso por posición entera (exclusivo, como Python).",
        "**Usar `.at` / `.iat`** para acceso a un único valor (más rápido que loc/iloc).",
        "**Evitar `SettingWithCopyWarning`** usando `.loc` para asignar en una vista.",
        "**Filtrar filas con boolean mask** dentro de `.loc`: `df.loc[df['edad'] > 30, 'nombre']`.",
    ],
    temas=[
        ("`[]` directo: shortcut con quirks", "Columnas → Series; filas → KeyError."),
        ("`.loc`: por label, slicing inclusivo", "El indexer principal del 80% del tiempo."),
        ("`.iloc`: por posición, slicing exclusivo (como Python)", "Cuando no te importa el label."),
        ("`.at` / `.iat`: single value", "Optimizado para 1 celda — útil en loops."),
        ("Mask + loc para filtros con asignación", "`df.loc[mask, 'col'] = valor`."),
        ("`SettingWithCopyWarning`: qué es y cómo evitarlo", "Usar `.loc` para asignar."),
    ],
    dataset="Palmer Penguins desde URL (mismo de clase 022) o el sintético si no hay internet.",
    ejercicios=[
        "**Acceso simple.** Carga penguins. Obtén la columna `species` con los 3 métodos: `df.species`, `df['species']`, `df.loc[:, 'species']`.",
        "**loc inclusivo vs iloc exclusivo.** Con index 0..N por default, compara `df.loc[0:5]` vs `df.iloc[0:5]`. ¿Cuántas filas devuelve cada uno?",
        "**Filtro + columnas seleccionadas.** Pingüinos Adelie machos con bill_length > 40: `df.loc[(df.species=='Adelie') & (df.sex=='male') & (df.bill_length_mm > 40), ['species', 'island', 'bill_length_mm']]`.",
        "**Asignación segura.** Crea una columna `is_big` que sea True si `body_mass_g > 4500`, usando `.loc`.",
        "**Provoca y arregla SettingWithCopyWarning.** Slicea con `df[df.x > 0]` y modifica → ve warning. Hazlo con `.loc` → sin warning.",
    ],
    homework=(
        "Notebook que: (a) muestra los 3 métodos de acceso a columna; (b) compara loc vs iloc en "
        "slicing con tabla; (c) filtra Adelie machos con bill_length>40 mostrando 3 columnas; "
        "(d) reproduce y arregla SettingWithCopyWarning con explicación."
    ),
    homework_criterio="Los filtros producen el subset correcto; la versión con `.loc` no emite warning.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.3.",
        "[pandas Indexing user guide](https://pandas.pydata.org/docs/user_guide/indexing.html)",
        "[SettingWithCopyWarning explained](https://pandas.pydata.org/docs/user_guide/indexing.html#returning-a-view-versus-a-copy)",
    ],
    siguiente=("024-pandas-operaciones-y-alineacion", "Pandas: operaciones y alineación"),
    cells=[
        Cell("md", "# Clase 023 — Indexación (loc, iloc, at, iat)\n\n**Parte 0** · VanderPlas cap. 3 § 3.3.\n\n> 🎯 4 indexers, cuándo usar cada uno, evitar SettingWithCopyWarning.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nrng = np.random.default_rng(42)\n\n# DataFrame de demo\ndf = pd.DataFrame({\n    'nombre': ['Ana', 'Bob', 'Cris', 'Dan', 'Eli'],\n    'edad'  : [30, 25, 28, 35, 22],\n    'nota'  : [7.5, 6.0, 8.2, 5.8, 9.1],\n}, index=['a', 'b', 'c', 'd', 'e'])\nprint(df)"),
        Cell("md", "## 1️⃣ Los 4 indexers\n\n| Indexer | Selector | Inclusivo slicing? | Uso |\n|---|---|---|---|\n| `df[...]` | label de columna | — | shortcut, devuelve Series |\n| `.loc[row, col]` | **label** | **sí** (incluye end) | el del 80% del tiempo |\n| `.iloc[row, col]` | **posición** entera | no (Python style) | cuando no importa el label |\n| `.at[row, col]` | label, single value | — | rápido, 1 celda |\n| `.iat[row, col]` | posición, single value | — | rápido, 1 celda |"),
        Cell("md", "## 2️⃣ Acceso por columna — los 3 caminos"),
        Cell("code", "# Atributo: cómodo pero quirky\nprint('df.nombre:')\nprint(df.nombre.values)\n\n# Bracket: el más explícito\nprint('\\ndf[\"nombre\"]:')\nprint(df['nombre'].values)\n\n# .loc: el más rico (permite combinar filas + cols)\nprint('\\ndf.loc[:, \"nombre\"]:')\nprint(df.loc[:, 'nombre'].values)\n\nprint('\\n⚠️ atributo falla si el nombre tiene espacios, choca con métodos (df.shape), o es número.')"),
        Cell("md", "## 3️⃣ loc inclusivo vs iloc exclusivo\n\nEsto sorprende a todo el mundo viniendo de Python puro:"),
        Cell("code", "print('df.loc[\"a\":\"c\"] — INCLUSIVE end (3 filas: a, b, c):')\nprint(df.loc['a':'c'])\nprint('\\ndf.iloc[0:3] — EXCLUSIVE end (3 filas: posiciones 0, 1, 2):')\nprint(df.iloc[0:3])"),
        Cell("md", "## 4️⃣ Filtro + columnas con loc"),
        Cell("code", "# Filas donde nota > 7, columnas nombre y nota\nresult = df.loc[df['nota'] > 7, ['nombre', 'nota']]\nprint(result)"),
        Cell("md", "## 5️⃣ `.at` y `.iat` — single value rápido\n\nÚtiles cuando estás en un loop y solo quieres una celda — son ~10× más rápidos que `.loc`/`.iloc` para single value."),
        Cell("code", "import time\n\n# Mucho más rápido para 1 celda\nt0 = time.perf_counter()\nfor _ in range(10_000):\n    _ = df.loc['a', 'nota']\nt1 = time.perf_counter()\n\nt2 = time.perf_counter()\nfor _ in range(10_000):\n    _ = df.at['a', 'nota']\nt3 = time.perf_counter()\n\nprint(f'.loc 10k veces: {(t1-t0)*1000:.1f} ms')\nprint(f'.at  10k veces: {(t3-t2)*1000:.1f} ms')\nprint(f'speedup       : {(t1-t0)/(t3-t2):.1f}×')"),
        Cell("md", "## 6️⃣ ⚠️ `SettingWithCopyWarning`\n\nEl bug más confuso de pandas. Ocurre cuando asignas a una **vista** y pandas no sabe si afectará al original:\n\n```python\nsubset = df[df['edad'] > 25]   # ¿vista o copia?\nsubset['nuevo'] = 1            # SettingWithCopyWarning\n```\n\n**Fix**: usa `.loc` para hacer la asignación en una sola expresión:\n\n```python\ndf.loc[df['edad'] > 25, 'nuevo'] = 1   # sin warning\n```\n\nEn pandas 3+ esto será error duro, no warning."),
        Cell("code", "import warnings\n\n# Provoca el warning\ndf_copy = df.copy()\nwith warnings.catch_warnings():\n    warnings.simplefilter('always')\n    try:\n        subset = df_copy[df_copy['edad'] > 25]\n        subset['nuevo'] = 1\n    except Exception as e:\n        print(f'En pandas modernos puede ser error: {e}')\n\n# Forma correcta\ndf_copy.loc[df_copy['edad'] > 25, 'nuevo'] = 1\nprint(df_copy)"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé los 4 indexers (loc, iloc, at, iat) y cuándo cada uno\n- [ ] Recuerdo que `.loc` slicing es inclusivo, `.iloc` exclusivo\n- [ ] Uso `.loc[mask, cols]` para filtrar y seleccionar\n- [ ] Asigno con `.loc` para evitar SettingWithCopyWarning\n- [ ] Uso `.at`/`.iat` cuando estoy en loops"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 3 métodos acceso, loc vs iloc, filtro complejo, SettingWithCopyWarning."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.3\n- [pandas Indexing](https://pandas.pydata.org/docs/user_guide/indexing.html)\n\n➡️ **Siguiente:** [024 — Operaciones y alineación](../024-pandas-operaciones-y-alineacion/README.md)"),
    ],
    definiciones=[
        ("`.loc[fila, col]`", "Acceso por **etiqueta**. Slicing es **inclusivo** en ambos extremos (`df.loc['a':'c']` incluye 'c'). Acepta booleano: `df.loc[df['x'] > 0, 'col']`."),
        ("`.iloc[fila, col]`", "Acceso por **posición entera**. Slicing es **exclusivo** del extremo (estilo Python). `df.iloc[0:5]` da 5 filas (índices 0..4)."),
        ("`.at[fila, col]` / `.iat[fila, col]`", "Versiones para acceder/asignar **un único valor**. ~10× más rápidos que `.loc`/`.iloc` cuando estás en loops. Mismo patrón label vs posición."),
        ("Indexer chaining (`df[cond][col] = x`)", "Encadenar dos `[]` operaciones de acceso. Crea ambigüedad: ¿es vista o copia? Origen del `SettingWithCopyWarning`. **Evítalo siempre**."),
        ("`SettingWithCopyWarning`", "Aviso de pandas: \"estoy haciendo algo ambiguo, puede que tu asignación se pierda\". Causado por chaining o asignación sobre subset no-explícito. Solución universal: `.loc[cond, col] = x` en una sola operación."),
    ],
    errores_comunes=[
        ("`SettingWithCopyWarning` aparece y no sé por qué", "Estás asignando sobre un resultado de slicing/filter que podría ser vista o copia. **Fix**: `df.loc[mask, 'col'] = valor` (una sola operación) en vez de `df[mask]['col'] = valor`."),
        ("`df.loc[0:5]` da 6 filas no 5", "loc es **inclusive end**. Para 5 filas: `df.iloc[0:5]` (exclusivo) o `df.loc[0:4]` (inclusivo, manual)."),
        ("`KeyError` con `.loc[5]` cuando hice `set_index('id')`", "El index ya no es 0..N — es la columna `id`. **Fix**: usa `.iloc[5]` para posición, o `.loc[<valor_id_real>]` para etiqueta."),
        ("Asignación a vista no modifica el original", "Pandas 3+ va a ser estricto: la vista no se considera modificable. **Fix**: siempre `.loc` para asignar; si necesitas copia, `.copy()` explícito."),
        ("`df.col1 = x` no actualiza la columna", "Como atributo, asignar no agrega columna nueva (lanza UserWarning). **Fix**: `df['col1'] = x` siempre."),
    ],
    faq=[
        ("¿`loc` o `iloc`?",
         "**`loc`** cuando el index es semántico (nombres, fechas, ids). **`iloc`** cuando solo importa la posición (top-K por orden, primeros 10, último). Mezclarlos en el mismo código causa confusión."),
        ("¿Por qué `loc` slicing es inclusivo?",
         "Decisión histórica: para labels (strings, fechas), incluir el end es lo intuitivo (`'enero':'marzo'` debe incluir marzo). Para enteros default queda raro — usa `iloc` ahí."),
        ("¿`at` vale la pena vs `loc` para single value?",
         "Solo en hot loops (>10k iteraciones). Para uso interactivo, `loc` es lo suficientemente rápido y más legible."),
        ("¿Cómo selecciono múltiples columnas?",
         "**Lista entre brackets**: `df[['a', 'b', 'c']]` (devuelve DataFrame). Notar el `[[]]`. Un solo `[]` con string devuelve Series."),
        ("¿`.loc[mask, cols]` o `.query() + [cols]`?",
         "Ambos válidos. `.loc[mask, cols]` para máscaras computadas; `.query()` para filtros declarativos largos. Misma velocidad para datasets <100k."),
    ],
))


SPECS.append(ClassSpec(
    folder="024-pandas-operaciones-y-alineacion",
    number="024",
    title="Pandas: operaciones y alineación",
    duration="60 min",
    source="VanderPlas, **cap. 3** § 3.4 *Operating on Data in Pandas*.",
    objetivo=(
        "Que el alumno entienda cómo pandas **alinea automáticamente por index** en operaciones "
        "entre Series/DataFrames, cómo manejar NaN resultantes, y use `apply`/`map` para "
        "transformaciones custom (con consciencia de cuándo es lento)."
    ),
    resultados=[
        "**Predecir** el resultado de operar dos Series/DataFrames con indexes parcialmente distintos.",
        "**Usar `fill_value`** en operaciones para no propagar NaN: `s1.add(s2, fill_value=0)`.",
        "**Aplicar funciones** con `apply` (lento, flexible), `map` (Series), `applymap` / `df.map` (elementwise).",
        "**Vectorizar** transformaciones cuando se puede en vez de `apply` (10–100× más rápido).",
        "**Usar ufuncs NumPy** sobre Series — pandas las soporta directamente y preserva el index.",
    ],
    temas=[
        ("Alineación automática por index", "Producto, suma, todo — pandas alinea, no asume orden."),
        ("`fill_value` para operaciones", "Reemplaza el NaN antes de calcular."),
        ("`apply` axis=0 vs axis=1", "Por columna vs por fila — costoso en filas."),
        ("`map` para Series con dict", "`s.map({'A': 1, 'B': 2})`."),
        ("`df.map` (era `applymap`) — elementwise", "Cell-by-cell, lento."),
        ("Vectorización > apply", "Si puedes hacerlo con ufunc, hazlo."),
    ],
    dataset="Sintético + Palmer Penguins. Sin descarga adicional.",
    ejercicios=[
        "**Suma con alineación.** Dos Series con index parcialmente solapado. Súmalas (default) y con `fill_value=0`.",
        "**`apply` por fila.** Define una función que reciba una fila de penguins y devuelva BMI = body_mass / bill_length². Aplica con `axis=1`.",
        "**Mismo cálculo vectorizado.** Implementa BMI con operaciones vectorizadas. Mide ambos con `%timeit`.",
        "**`map` con dict.** Mapea `species` a códigos: `{'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}`.",
        "**ufunc NumPy preserva index.** Aplica `np.log` a una columna; verifica que el index sigue intacto.",
    ],
    homework=(
        "Notebook con penguins: (a) BMI por fila con `apply` vs vectorizado (tabla `%timeit`); "
        "(b) species → código numérico con `map`; (c) demo de alineación con `fill_value`; "
        "(d) `np.log` sobre body_mass preservando index."
    ),
    homework_criterio="Vectorizado >50× más rápido que apply. Mapping y alineación correctos.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.4.",
        "[pandas — apply, map](https://pandas.pydata.org/docs/user_guide/basics.html#function-application)",
    ],
    siguiente=("025-pandas-datos-faltantes", "Pandas: datos faltantes"),
    cells=[
        Cell("md", "# Clase 024 — Operaciones y alineación\n\n**Parte 0** · VanderPlas cap. 3 § 3.4.\n\n> 🎯 Alineación por index, apply vs vectorización, fill_value.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nimport time"),
        Cell("md", "## 1️⃣ Alineación automática\n\nOperar dos Series alinea por **index**, no por posición:"),
        Cell("code", "a = pd.Series([100, 200, 300], index=['x', 'y', 'z'])\nb = pd.Series([10, 20, 30],    index=['y', 'z', 'w'])\n\nprint('a:'); print(a)\nprint('\\nb:'); print(b)\nprint('\\na + b — alinea, NaN donde no hay match:')\nprint(a + b)"),
        Cell("md", "## 2️⃣ `fill_value` evita propagar NaN"),
        Cell("code", "print('a.add(b, fill_value=0):')\nprint(a.add(b, fill_value=0))\n# x: 100+0=100  y: 200+10=210  z: 300+20=320  w: 0+30=30"),
        Cell("md", "## 3️⃣ `apply` — flexible pero lento por fila\n\n**Regla**: si puedes hacerlo con ufunc/operadores vectorizados, **no uses apply**. Si necesitas lógica compleja por fila, sí."),
        Cell("code", "df = pd.DataFrame({\n    'masa': [3750, 3800, 3250, 4400, 3700],\n    'pico': [39.1, 39.5, 40.3, 36.7, 39.3],\n})\n\n# apply axis=1: una fila por iteración (lento)\ndef bmi_fila(row):\n    return row['masa'] / (row['pico'] ** 2)\n\nbmi_apply = df.apply(bmi_fila, axis=1)\nprint('con apply:')\nprint(bmi_apply.round(3))\n\n# Vectorizado: una operación sobre todo el array (rápido)\nbmi_vec = df['masa'] / (df['pico'] ** 2)\nprint('\\nvectorizado:')\nprint(bmi_vec.round(3))\nprint(f'\\niguales? {(bmi_apply.round(6) == bmi_vec.round(6)).all()}')"),
        Cell("md", "## 4️⃣ Benchmark apply vs vectorizado"),
        Cell("code", "rng = np.random.default_rng(42)\ngrande = pd.DataFrame({\n    'masa': rng.uniform(3000, 5000, 10_000),\n    'pico': rng.uniform(35, 50, 10_000),\n})\n\nt0 = time.perf_counter(); grande.apply(bmi_fila, axis=1); t1 = time.perf_counter()\nt2 = time.perf_counter(); grande['masa'] / (grande['pico'] ** 2); t3 = time.perf_counter()\n\nprint(f'apply        : {(t1-t0)*1000:.1f} ms')\nprint(f'vectorizado  : {(t3-t2)*1000:.2f} ms')\nprint(f'speedup      : {(t1-t0)/(t3-t2):.0f}×')"),
        Cell("md", "## 5️⃣ `map` para Series — recodificación con dict\n\nÚtil para mapear categorías a códigos o relabelar:"),
        Cell("code", "species = pd.Series(['Adelie', 'Chinstrap', 'Gentoo', 'Adelie', 'Gentoo'])\ncodigo = species.map({'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2})\nprint(pd.DataFrame({'species': species, 'codigo': codigo}))"),
        Cell("md", "## 6️⃣ `df.map` — elementwise (era `applymap`)\n\nAplica una función a **cada celda** del DataFrame. Lento — úsalo solo cuando vectorización no aplica:"),
        Cell("code", "df_num = pd.DataFrame({'A': [1.234, 5.678], 'B': [9.0, 0.1234]})\nformat_pct = df_num.map(lambda x: f'{x*100:.2f}%')\nprint(format_pct)"),
        Cell("md", "## 7️⃣ ufuncs NumPy preservan index\n\nPandas \"sabe\" NumPy — aplicar `np.log`, `np.sqrt`, etc., a una Series mantiene el index:"),
        Cell("code", "s = pd.Series([1, 10, 100, 1000], index=['a', 'b', 'c', 'd'])\nprint('s:'); print(s)\nprint('\\nnp.log(s):'); print(np.log(s).round(3))"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé que pandas alinea por index automáticamente\n- [ ] Uso `fill_value` para evitar NaN en operaciones\n- [ ] Prefiero vectorización a apply\n- [ ] Uso `map` para recodificar Series con dict\n- [ ] Sé que ufuncs NumPy preservan el index"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. BMI con apply vs vectorizado + benchmark, map species, alineación con fill_value."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.4\n- [pandas function application](https://pandas.pydata.org/docs/user_guide/basics.html#function-application)\n\n➡️ **Siguiente:** [025 — Datos faltantes](../025-pandas-datos-faltantes/README.md)"),
    ],
    definiciones=[
        ("Alineación por index", "Operación matemática entre dos pandas (Series + Series, DF + Series, etc.) alinea por **etiqueta** de index. Labels que no estén en ambos → NaN."),
        ("`fill_value` en operaciones", "Parámetro que reemplaza NaN durante la operación: `s1.add(s2, fill_value=0)` trata índices ausentes como 0 en vez de propagar NaN."),
        ("`apply`", "Aplica función a cada fila (`axis=1`) o columna (`axis=0`) de un DataFrame, o cada elemento de una Series. **Lento** porque itera en Python. Usa solo si vectorización no aplica."),
        ("`map` (Series)", "Aplica función o **dict** a cada elemento. Útil para recodificación rápida: `s.map({'A': 1, 'B': 2})`. Más rápido que `apply` por su API más restringida."),
        ("`df.map` (antes `applymap`)", "Aplica función a **cada celda** del DataFrame (elementwise). Lento; usa solo cuando vectorización no aplica. `applymap` está deprecated en pandas 2.1+."),
        ("Ufunc-aware", "Pandas Series respeta ufuncs NumPy: `np.log(s)`, `np.sqrt(s)` funcionan y **preservan el index**. Ventaja sobre convertir a array y perder labels."),
    ],
    errores_comunes=[
        ("`apply` toma 10× más que vectorización equivalente", "Iteración Python por fila. **Fix**: piensa si tu lógica es expresable con operaciones vectorizadas (`df['a'] * df['b']`); 99% de los `apply` simples se pueden eliminar."),
        ("`s1 + s2` produce NaN aunque los datos están completos", "Index distinto (incluso por orden diferente). **Fix**: alinea antes (`s2 = s2.reindex(s1.index)`) o usa `s1.add(s2, fill_value=0)`."),
        ("`df.apply(func, axis=1)` rompe con `KeyError`", "Tu función accede `row['col_x']` pero esa col no existe. **Fix**: imprime `row.index` dentro de la función para ver qué hay."),
        ("`df.map(lambda x: ...)` falla \"object has no attribute 'map'\"", "Es método de DataFrame solo en pandas ≥2.1. Para versiones viejas: `df.applymap(...)`. Para Series: `s.map(...)`."),
        ("`np.log(df['x'])` da error con NaN", "Si NaN está presente, log da NaN. Si negativos, lanza warning y NaN. **Fix**: filtra primero (`df[df['x'] > 0]`) o usa `np.log1p` para log(1+x)."),
    ],
    faq=[
        ("¿Cuándo `apply` y cuándo NO?",
         "**NO**: si lo puedes hacer con `df['a'] * df['b']` u operación pandas built-in (groupby, transform, etc.). **SÍ**: lógica compleja por fila que no se descompone."),
        ("¿`apply(axis=1)` con tipos mixtos da problemas?",
         "Sí — pandas convierte cada row a Series con dtype común. Si tienes `int` y `str`, queda `object` y los operadores `<`, `>` rompen. Mejor extrae columnas y opera directo."),
        ("¿Cómo paralelizo apply?",
         "`pandarallel`, `swifter`, `modin` — drop-in replacements. Pero antes de paralelizar, asegúrate que tu apply no es vectorizable (el speedup es mayor)."),
        ("¿`s.map(dict)` o `s.replace(dict)`?",
         "**`map`**: mapea uno-a-uno; valores no encontrados en dict → NaN. **`replace`**: reemplaza solo los que aparecen; el resto queda igual. Elige según comportamiento deseado en valores faltantes."),
        ("¿Por qué pandas a veces es más lento que NumPy?",
         "Overhead del index, manejo de NaN, dtype-aware. Para operaciones puramente numéricas sobre datos limpios y rectangulares, NumPy puede ser 2-5× más rápido. Pandas vale por la API, no por velocidad raw."),
    ],
))


SPECS.append(ClassSpec(
    folder="025-pandas-datos-faltantes",
    number="025",
    title="Pandas: datos faltantes",
    duration="75 min",
    source="VanderPlas, **cap. 3** § 3.5 *Handling Missing Data*.",
    objetivo=(
        "Que el alumno **detecte, cuantifique y maneje** datos faltantes con criterio. Eliminar "
        "es la opción fácil pero suele ser incorrecta: cuándo eliminar, cuándo imputar (media, "
        "mediana, forward-fill), y cuándo el faltante es **señal** que merece su propia columna."
    ),
    resultados=[
        "**Detectar** NaN con `isna()`, `notna()` y cuantificar por columna/fila.",
        "**Eliminar** filas/columnas con NaN usando `dropna` con `how`/`thresh`/`subset`.",
        "**Imputar** con `fillna`: valor escalar, media/mediana, forward/backward fill, interpolación.",
        "**Distinguir** `NaN` vs `None` vs `pd.NA` y por qué importan los dtypes nullable (`Int64`, `boolean`).",
        "**Decidir** entre eliminar/imputar/dejar — y crear columna `was_missing` cuando el faltante es informativo.",
    ],
    temas=[
        ("Tipos de missing en pandas: NaN, None, NaT, pd.NA", "Cada uno tiene caso de uso."),
        ("Detección: `isna`, `notna`, `isna().sum()`", "First-look obligatorio."),
        ("`dropna`: how='any'/'all', thresh, subset", "Eliminar con precisión."),
        ("`fillna`: escalar, dict, ffill, bfill, interpolate", "Imputar según contexto."),
        ("Dtypes nullable: Int64, Float64, boolean", "El nuevo missing nativo."),
        ("`was_missing` como feature", "Cuando el missing es señal."),
    ],
    dataset="Palmer Penguins (tiene NaN reales en sex y mediciones). Sin descarga adicional si ya está en clases anteriores.",
    ejercicios=[
        "**Cuantifica.** Carga penguins, reporta % de NaN por columna y por fila.",
        "**Eliminar filas con cualquier NaN.** `df.dropna(how='any')`. Compara shape antes/después.",
        "**Eliminar solo filas con NaN en `sex`.** `df.dropna(subset=['sex'])`. Más selectivo.",
        "**Imputar.** Rellena `bill_length_mm` con la mediana **por especie** (groupby + transform). Justifica por qué la mediana es mejor que la media aquí.",
        "**Forward fill en series temporales.** Crea una Series con NaN intercalados. Aplica `ffill`, `bfill`, `interpolate`. Compara.",
    ],
    homework=(
        "Notebook con penguins: (a) reporte completo de missing (% por col, % por fila, filas más "
        "incompletas); (b) 3 estrategias: drop all, drop subset, imputar por grupo; (c) "
        "columna `bill_was_missing` y demuestra que el flag puede mejorar un modelo simple; "
        "(d) demo de dtypes nullable `Int64`."
    ),
    homework_criterio="Imputación por grupo no introduce sesgo; el flag was_missing añade información.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.5.",
        "[pandas — Missing data user guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)",
        "[pandas nullable Integer dtypes](https://pandas.pydata.org/docs/user_guide/integer_na.html)",
    ],
    siguiente=("026-pandas-multiindex", "Pandas: MultiIndex"),
    cells=[
        Cell("md", "# Clase 025 — Datos faltantes\n\n**Parte 0** · VanderPlas cap. 3 § 3.5.\n\n> 🎯 Detectar, cuantificar y manejar NaN con criterio. Eliminar no siempre es la respuesta.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Tipos de missing en pandas\n\n| Valor | Tipo | Caso |\n|---|---|---|\n| `np.nan` (float NaN) | float | numérico clásico — incluso en columnas \"int\" |\n| `None` | object | strings y mixto |\n| `pd.NaT` | datetime | timestamps |\n| `pd.NA` | NA-aware | dtypes nullable (Int64, boolean, string) |\n\n**Gotcha histórico**: una columna `int` con NaN se promueve a `float64` (porque NumPy int no tiene NaN). Solución: usa `pd.Int64` (nullable)."),
        Cell("md", "## 2️⃣ Detección y cuantificación"),
        Cell("code", "df = pd.DataFrame({\n    'a': [1, 2, np.nan, 4, 5],\n    'b': [np.nan, 'x', 'y', np.nan, 'z'],\n    'c': [10, 20, 30, 40, 50],\n})\n\nprint('isna() (matriz bool):')\nprint(df.isna())\nprint()\nprint('Por columna (count NaN):')\nprint(df.isna().sum())\nprint()\nprint('% NaN por columna:')\nprint((df.isna().mean() * 100).round(1))\nprint()\nprint('Filas con al menos un NaN:')\nprint(df.isna().any(axis=1).sum())"),
        Cell("md", "## 3️⃣ `dropna` — eliminar con precisión\n\n```python\ndf.dropna()                            # filas con cualquier NaN\ndf.dropna(how='all')                   # solo filas con TODOS NaN\ndf.dropna(thresh=2)                    # mantén filas con >= 2 no-NaN\ndf.dropna(subset=['col_clave'])        # NaN solo en esta col cuenta\ndf.dropna(axis=1)                      # eliminar COLUMNAS con NaN\n```"),
        Cell("code", "print(f'shape original           : {df.shape}')\nprint(f'dropna() any            : {df.dropna().shape}')\nprint(f'dropna(subset=[\"a\"])    : {df.dropna(subset=[\"a\"]).shape}')\nprint(f'dropna(axis=1)          : {df.dropna(axis=1).shape}  ← elimina cols b'); print()\nprint(df.dropna(subset=['a']))"),
        Cell("md", "## 4️⃣ `fillna` — imputar\n\n```python\ndf.fillna(0)                           # constante\ndf.fillna({'a': 0, 'b': 'missing'})    # por columna\ndf.fillna(df.mean(numeric_only=True))  # media por columna\ndf['col'].fillna(df['col'].median())   # mediana en una col\ndf['x'].ffill()                        # último válido hacia adelante\ndf['x'].bfill()                        # próximo válido hacia atrás\ndf['x'].interpolate(method='linear')   # interpolación\n```"),
        Cell("code", "# Imputar con dict por columna\ndf2 = df.fillna({'a': df['a'].median(), 'b': 'desconocido'})\nprint(df2)"),
        Cell("md", "## 5️⃣ Imputación por grupo — la opción correcta\n\nImputar con la media **global** introduce sesgo. Imputar con la **media del grupo** (por especie, por región, etc.) es mucho mejor:"),
        Cell("code", "# Demo: imputar nota por curso (grupo)\nnotas = pd.DataFrame({\n    'curso': ['A', 'A', 'A', 'B', 'B', 'B', 'C', 'C'],\n    'nota' : [7.0, 8.0, np.nan, 4.0, 5.0, np.nan, 9.0, np.nan],\n})\n\n# Mediana por grupo\nnotas['nota_imp'] = notas.groupby('curso')['nota'].transform(\n    lambda s: s.fillna(s.median())\n)\nprint(notas)\nprint('\\nMediana global =', notas['nota'].median(), '← sería sesgada por A y C')"),
        Cell("md", "## 6️⃣ `was_missing` como feature\n\nA veces el faltante es **señal** (ej: respuesta opcional → \"prefiero no contestar\"). Antes de imputar, guarda un flag:"),
        Cell("code", "df3 = df.copy()\ndf3['a_was_missing'] = df3['a'].isna()\ndf3['a'] = df3['a'].fillna(df3['a'].mean())\nprint(df3)"),
        Cell("md", "## 7️⃣ Dtypes nullable (modernos)\n\nDesde pandas 1.0+, hay dtypes que soportan NaN sin promover a float:"),
        Cell("code", "# int normal: NaN promueve a float\ns_old = pd.Series([1, 2, np.nan, 4])\nprint(f'dtype int+NaN antiguo : {s_old.dtype}')   # float64\n\n# int nullable: mantiene int\ns_new = pd.Series([1, 2, pd.NA, 4], dtype='Int64')\nprint(f'dtype Int64 (nullable): {s_new.dtype}')   # Int64\nprint(s_new)"),
        Cell("md", "## 🎯 Cómo decidir: eliminar, imputar o flag\n\n| Situación | Estrategia |\n|---|---|\n| <1% missing, distribución aleatoria | `dropna` (rápido, bajo costo) |\n| 5-30% missing, MCAR (Missing Completely At Random) | imputar (media/mediana global) |\n| Missing por grupo (especie, región) | imputar por grupo (`groupby.transform`) |\n| Missing es informativo (encuesta opcional) | imputar + flag `was_missing` |\n| >50% missing | considerar eliminar la columna |\n| Series temporal | `ffill`/`interpolate` |"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Cuantifico NaN antes de actuar (% por col y fila)\n- [ ] Uso `dropna(subset=...)` en vez de `dropna()` ciego\n- [ ] Imputo por grupo cuando hay estructura\n- [ ] Creo flag `was_missing` cuando el missing es señal\n- [ ] Uso `Int64` para columnas enteras con NaN"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Reporte missing penguins, 3 estrategias dropna/impute, flag was_missing, Int64."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.5\n- [Missing data user guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)\n\n➡️ **Siguiente:** [026 — MultiIndex](../026-pandas-multiindex/README.md)"),
    ],
    definiciones=[
        ("`NaN` (Not a Number)", "Float especial IEEE 754 que representa missing en columnas numéricas. Característica: NO es igual a sí mismo (`np.nan == np.nan` → False). Usa `pd.isna()` para detectarlo."),
        ("`None` vs `NaN`", "**`None`** es objeto Python (en columnas `object`). **`NaN`** es float (en columnas numéricas). Pandas trata ambos como missing pero internamente son distintos."),
        ("`pd.NA`", "Sentinel \"missing universal\" (pandas 1.0+) compatible con dtypes nullable (`Int64`, `boolean`, `string`). Comportamiento más consistente que NaN en operaciones."),
        ("MCAR / MAR / MNAR", "**MCAR** (Missing Completely At Random): missing es aleatorio. **MAR** (Missing At Random): missing depende de variables observadas. **MNAR** (Missing Not At Random): depende del propio valor missing (peor caso)."),
        ("Imputación", "Reemplazar missing con un valor estimado. Estrategias: media/mediana/moda global, por grupo (`groupby.transform`), forward-fill (series temporales), KNN, regresión, MICE."),
        ("`was_missing` flag", "Columna booleana adicional que registra qué filas tenían missing antes de imputar. Permite al modelo usar el hecho de que faltaba como feature (a veces es informativo)."),
    ],
    errores_comunes=[
        ("`if df['col'] == np.nan` no funciona", "NaN no es igual a nada (incluso a sí mismo). **Fix**: `df['col'].isna()` o `pd.isna(df['col'])`."),
        ("`df.dropna()` borra todo", "Sin parámetros, borra fila con CUALQUIER NaN. Si tienes muchos NaN repartidos, te queda 0 filas. **Fix**: `dropna(subset=['col_clave'])` para ser selectivo."),
        ("Imputar con media global introduce sesgo", "Si los grupos tienen medias muy distintas, imputar global aplana las diferencias. **Fix**: imputa por grupo con `groupby.transform(lambda s: s.fillna(s.median()))`."),
        ("Una columna `int` se volvió `float` tras leer CSV", "Tiene NaN → promoción automática (NumPy int no soporta NaN). **Fix**: dtype nullable `Int64`: `df['col'] = df['col'].astype('Int64')`."),
        ("`fillna(0)` mata el flag de \"missing\"", "Pierdes la información de que faltaba. **Fix**: crea `df['col_was_missing'] = df['col'].isna()` ANTES de imputar."),
    ],
    faq=[
        ("¿Eliminar, imputar o flag?",
         "Depende: **<1% missing aleatorio** → drop. **5-30% MAR** → imputar (mediana por grupo). **>50%** → eliminar columna o tratar como categoría 'missing'. **Si missing es informativo** → flag + imputar."),
        ("¿Mediana o media para imputar?",
         "**Mediana** es más robusta a outliers (recomendada por default). **Media** si la distribución es ~normal y sin outliers. Para categóricas: **moda**."),
        ("¿`ffill` siempre bueno para series temporales?",
         "Bueno cuando los valores cambian poco entre observaciones (precios, temperaturas). Malo si los gaps son largos o el dato es volátil. Considera `interpolate(method='time')` para mejor resultado."),
        ("¿Cómo sé si la imputación afecta mi modelo?",
         "Compara métricas: (a) baseline drop, (b) imputación X, (c) imputación + flag. Si el flag mejora el modelo, el missing era informativo (caso MNAR)."),
        ("¿KNN/MICE para imputación en pandas?",
         "No nativo. Usa `sklearn.impute.KNNImputer` o `IterativeImputer` (= MICE). Más caro pero mejor que mediana en datasets con correlaciones fuertes."),
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
