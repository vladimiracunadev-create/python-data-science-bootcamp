"""Classes 030-032 — pandas C: strings, time series, eval/query."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="030-pandas-operaciones-vectorizadas-sobre-strings",
    number="030",
    title="Pandas: operaciones vectorizadas sobre strings",
    duration="60 min",
    source="VanderPlas, **cap. 3** § 3.11 *Vectorized String Operations*.",
    objetivo=(
        "Que el alumno limpie y transforme columnas de texto sin caer en `apply(lambda x: ...)`, "
        "usando el accessor `.str` de pandas — vectorizado, NaN-aware, con métodos análogos a "
        "los de Python (`lower`, `strip`, `replace`, `split`, `contains`, regex)."
    ),
    resultados=[
        "**Usar `.str`** para aplicar operaciones de string vectorizadamente a una Series.",
        "**Manejar NaN automáticamente** (los métodos `.str` propagan NaN sin error).",
        "**Aplicar regex** con `.str.contains(patron)`, `.str.extract(...)`, `.str.replace(...)`.",
        "**Dividir y unir** con `.str.split(sep, expand=True)` que produce un DataFrame.",
        "**Trabajar con categorical** cuando el cardinalidad es baja (memoria y speedup).",
    ],
    temas=[
        ("Accessor `.str`", "Métodos vectorizados que respetan NaN."),
        ("Casos típicos: lower, strip, replace, contains", "El 80% del trabajo."),
        ("Regex con `.str.extract` y grupos nombrados", "Extracción estructurada."),
        ("`.str.split(expand=True)` → DataFrame", "Desnormalizar columnas combinadas."),
        ("`dtype='string'` (nullable) vs object", "El moderno y NA-aware."),
        ("`Categorical` para baja cardinalidad", "Menos memoria, groupby más rápido."),
    ],
    dataset="Sintético: emails, nombres con espacios, fechas como string.",
    ejercicios=[
        "**Lower + strip.** Lista de emails con mayúsculas y espacios. Normaliza con `.str.lower().str.strip()`.",
        "**Extract dominio.** De una columna de emails, extrae el dominio con regex (`@(.+)$`).",
        "**Split nombre completo.** Columna `'Ana García'` → `nombre`, `apellido` en columnas separadas.",
        "**Filtro por contains.** Filas donde la columna `descripcion` contiene la palabra (case-insensitive) `'urgente'`.",
        "**Categorical.** Convierte una columna con 5 valores únicos en 100k filas a `Categorical`. Compara memoria.",
    ],
    homework=(
        "Notebook con CSV sintético de contactos (nombre, email, teléfono): (a) normalizar email "
        "(lower+strip); (b) extraer dominio; (c) separar nombre/apellido; (d) flag de email "
        "corporativo (no gmail/yahoo/hotmail); (e) convertir país a Categorical y reportar memoria."
    ),
    homework_criterio="Operaciones manejan NaN sin error. Categorical reduce memoria al menos 5×.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.11.",
        "[pandas Text data user guide](https://pandas.pydata.org/docs/user_guide/text.html)",
        "[pandas Categorical](https://pandas.pydata.org/docs/user_guide/categorical.html)",
    ],
    siguiente=("031-pandas-series-de-tiempo-resampling-rolling", "Pandas: series de tiempo, resampling, rolling"),
    cells=[
        Cell("md", "# Clase 030 — Strings vectorizados\n\n**Parte 0** · VanderPlas cap. 3 § 3.11.\n\n> 🎯 Limpiar texto sin `apply(lambda)`. El accessor `.str` es vectorizado y NaN-aware.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import pandas as pd\nimport numpy as np"),
        Cell("md", "## 1️⃣ El accessor `.str`\n\nPandas expone métodos string vectorizados via `.str`:\n\n```python\ns.str.lower()\ns.str.strip()\ns.str.replace('a', 'b')\ns.str.contains('patron', regex=True)\ns.str.extract(r'(\\d+)')\ns.str.split(',', expand=True)\ns.str.len()\n```\n\n**Ventaja sobre `apply(lambda)`**: vectorizado (5–10× más rápido) y maneja NaN automáticamente."),
        Cell("code", "emails = pd.Series([' Ana@Example.com', 'BOB@gmail.com  ', np.nan, 'cris@FOO.io', 'dan@example.com'])\nprint('original:')\nprint(emails)\n\nlimpio = emails.str.lower().str.strip()\nprint('\\nnormalizado:')\nprint(limpio)\nprint('\\nNaN se preserva sin error.')"),
        Cell("md", "## 2️⃣ Regex con `.str.extract`\n\nPattern con grupos `()` → DataFrame con una columna por grupo:"),
        Cell("code", "dominios = limpio.str.extract(r'@(?P<dominio>[\\w\\.]+)$')\nprint(dominios)\n\n# Combinar con el original\nprint('\\ncombinado:')\nprint(pd.concat([limpio.rename('email'), dominios], axis=1))"),
        Cell("md", "## 3️⃣ `.str.contains` + regex para filtros"),
        Cell("code", "df = pd.DataFrame({\n    'email': ['ana@example.com', 'bob@gmail.com', 'cris@empresa.es', 'dan@yahoo.com'],\n    'desc' : ['Comentario URGENTE', 'normal', 'urgente revisar', 'bug critico']\n})\n\n# Email corporativo (no es de proveedor mainstream)\nmainstream = r'gmail|yahoo|hotmail|outlook'\ndf['corp'] = ~df['email'].str.contains(mainstream, case=False, regex=True)\n\n# Descripción urgente (case-insensitive)\ndf['urgente'] = df['desc'].str.contains('urgente', case=False)\n\nprint(df)"),
        Cell("md", "## 4️⃣ `.str.split(expand=True)` — desnormalizar"),
        Cell("code", "nombres = pd.Series(['Ana García', 'Bob Smith Jr', 'Cris López-Mora'])\npartes = nombres.str.split(' ', n=1, expand=True)\npartes.columns = ['nombre', 'apellido']\nprint(partes)"),
        Cell("md", "## 5️⃣ Dtypes string vs object\n\n```python\npd.Series(['a','b','c'], dtype='string')  # nullable, NA-aware\npd.Series(['a','b','c'])                  # default: object (mezcla Python)\n```\n\nEl dtype `'string'` es el moderno: integra con `pd.NA`, optimizaciones futuras."),
        Cell("md", "## 6️⃣ `Categorical` — para baja cardinalidad\n\nSi una columna tiene pocos valores únicos comparado al total de filas (ej: país, sexo, tipo), `Categorical` ahorra memoria masivamente y acelera `groupby`/`sort`:"),
        Cell("code", "rng = np.random.default_rng(42)\nN = 100_000\npaises = rng.choice(['ES', 'CL', 'MX', 'AR', 'CO'], N)\n\ns_obj = pd.Series(paises)\ns_cat = pd.Series(paises, dtype='category')\n\nprint(f'object   : {s_obj.memory_usage(deep=True)/1024:.0f} KB')\nprint(f'category : {s_cat.memory_usage(deep=True)/1024:.0f} KB')\nprint(f'ratio    : {s_obj.memory_usage(deep=True)/s_cat.memory_usage(deep=True):.1f}×')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Uso `.str.lower()`, `.str.strip()`, etc. — no `apply(lambda)`\n- [ ] Sé que `.str` maneja NaN automáticamente\n- [ ] Aplico regex con `.str.extract` y `.str.contains`\n- [ ] Uso `.str.split(expand=True)` para desnormalizar\n- [ ] Uso `Categorical` para columnas de baja cardinalidad"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. CSV contactos: normalizar email, extraer dominio, separar nombre, flag corp, Categorical país."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.11\n- [pandas Text](https://pandas.pydata.org/docs/user_guide/text.html)\n- [pandas Categorical](https://pandas.pydata.org/docs/user_guide/categorical.html)\n\n➡️ **Siguiente:** [031 — Series de tiempo](../031-pandas-series-de-tiempo-resampling-rolling/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="031-pandas-series-de-tiempo-resampling-rolling",
    number="031",
    title="Pandas: series de tiempo, resampling, rolling",
    duration="90 min",
    source="VanderPlas, **cap. 3** § 3.12 *Working with Time Series*.",
    objetivo=(
        "Que el alumno trabaje con datos temporales correctamente: parsear fechas, indexar por "
        "`DatetimeIndex`, hacer **resampling** (cambiar la frecuencia) y **rolling** (ventanas "
        "móviles para tendencias)."
    ),
    resultados=[
        "**Parsear** strings de fecha con `pd.to_datetime(..., format=..., errors=...)`.",
        "**Indexar** por `DatetimeIndex` y slicear con strings de fecha (`df.loc['2024-01':'2024-03']`).",
        "**Resamplear** a otra frecuencia: `df.resample('M').sum()`, `'W'`, `'D'`, `'H'`.",
        "**Aplicar ventanas móviles** con `rolling(window).mean()` para suavizar tendencias.",
        "**Manejar zonas horarias** con `tz_localize` y `tz_convert`.",
    ],
    temas=[
        ("`pd.to_datetime` con errors='coerce'", "Parseo robusto."),
        ("DatetimeIndex y slicing por fecha", "Sintaxis natural: `'2024-01':'2024-03'`."),
        ("Resampling: 'D', 'W', 'M', 'Q', 'Y', 'H'", "Cambiar frecuencia + agregar."),
        ("Rolling windows", "Suavizado, medias móviles."),
        ("`shift` y `diff`", "Diferencias entre periodos, lag features."),
        ("Timezones: localize → convert", "Cuando los datos tienen TZ."),
    ],
    dataset="Sintético: serie diaria de 2 años de ventas. Sin descarga.",
    ejercicios=[
        "**Parseo robusto.** Lista de fechas con formatos mixtos (`'2024-01-15'`, `'15/02/2024'`, `'foo'`). Parsea con `errors='coerce'`. Reporta NaT.",
        "**Slice por fecha.** Con índice datetime, selecciona Q1 2024 con `df.loc['2024-01':'2024-03']`.",
        "**Resample diaria → mensual.** Suma ventas por mes con `df.resample('M').sum()`.",
        "**Rolling 7-day mean.** Calcula media móvil de 7 días sobre ventas diarias. Plotea junto a la serie original.",
        "**`shift` para lag feature.** Crea columna `ventas_lag_1` con `shift(1)`. Útil para features de ML.",
    ],
    homework=(
        "Notebook con serie sintética de 2 años: (a) parseo robusto; (b) slice por trimestre; "
        "(c) resample a mensual con sum y mean; (d) rolling 7/30 días con plot; "
        "(e) diff y pct_change para variación."
    ),
    homework_criterio="Plots muestran tendencia clara. Resample correcto (#meses esperado).",
    referencias=[
        "VanderPlas, **cap. 3** § 3.12.",
        "[pandas Time Series user guide](https://pandas.pydata.org/docs/user_guide/timeseries.html)",
    ],
    siguiente=("032-pandas-eval-y-query", "Pandas: eval y query"),
    cells=[
        Cell("md", "# Clase 031 — Series de tiempo\n\n**Parte 0** · VanderPlas cap. 3 § 3.12.\n\n> 🎯 Parsear, indexar, resamplear y rolling sobre datos temporales.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\n\nrng = np.random.default_rng(42)\nfechas = pd.date_range('2024-01-01', '2025-12-31', freq='D')\nventas = pd.Series(\n    rng.normal(1000, 200, len(fechas)).cumsum().clip(min=0).astype(int),\n    index=fechas,\n    name='ventas',\n)\nprint(ventas.head())"),
        Cell("md", "## 1️⃣ `pd.to_datetime` — parseo robusto\n\n```python\npd.to_datetime(s, format='%Y-%m-%d', errors='coerce')\n```\n\n`errors='coerce'` convierte lo no parseable a `NaT` (Not a Time) en vez de lanzar excepción."),
        Cell("code", "raw = pd.Series(['2024-01-15', '15/02/2024', '2024-03-20', 'foo', '2024-04-10'])\nfechas_parsed = pd.to_datetime(raw, format='mixed', errors='coerce')\nprint(fechas_parsed)\nprint(f'\\nNaT count: {fechas_parsed.isna().sum()}')"),
        Cell("md", "## 2️⃣ DatetimeIndex y slicing\n\nCon índice datetime, puedes slicear con strings:"),
        Cell("code", "# Trimestre Q1 2024\nq1 = ventas.loc['2024-01':'2024-03']\nprint(f'Q1 2024: {len(q1)} días')\n\n# Solo enero 2025\nene_25 = ventas.loc['2025-01']\nprint(f'Enero 2025: {len(ene_25)} días')\n\n# Componentes\nprint(f'\\naño/mes/día/dow de la primera fecha:')\nprint(f'  year={ventas.index[0].year}')\nprint(f'  month={ventas.index[0].month}')\nprint(f'  day_name={ventas.index[0].day_name()}')"),
        Cell("md", "## 3️⃣ Resampling — cambiar frecuencia\n\n| Alias | Frecuencia |\n|---|---|\n| `'D'` | día |\n| `'W'` | semana |\n| `'ME'` | mes (end) |\n| `'QE'` | trimestre |\n| `'YE'` | año |\n| `'h'` | hora |\n| `'min'` | minuto |\n\nResampling **siempre requiere agregación**: sum, mean, last, ohlc."),
        Cell("code", "# Diaria → mensual\nmensual = ventas.resample('ME').agg(['sum', 'mean', 'std']).round(0)\nprint(mensual.head())\n\n# Diaria → semanal (suma)\nsemanal = ventas.resample('W').sum()\nprint(f'\\nsemanas: {len(semanal)}')"),
        Cell("md", "## 4️⃣ Rolling windows — medias móviles\n\nVentana móvil: a cada punto, aplicar función a los últimos N puntos. Suaviza tendencias."),
        Cell("code", "rolling_7  = ventas.rolling(7).mean()\nrolling_30 = ventas.rolling(30).mean()\n\nfig, ax = plt.subplots(figsize=(11, 4))\nventas.plot(ax=ax, alpha=0.4, label='diaria', linewidth=0.7)\nrolling_7.plot(ax=ax, label='rolling 7d', linewidth=1.2)\nrolling_30.plot(ax=ax, label='rolling 30d', linewidth=1.5)\nax.set_title('Ventas — original vs ventanas móviles')\nax.legend()\nax.set_ylabel('ventas')\nplt.tight_layout()\nplt.show()"),
        Cell("md", "## 5️⃣ `shift` y `diff` — lag y variación\n\n```python\ns.shift(1)        # adelanta 1 paso (NaN al inicio)\ns.diff(1)         # s - s.shift(1) → cambio absoluto\ns.pct_change()    # cambio relativo (%)\n```"),
        Cell("code", "df = pd.DataFrame({\n    'ventas'      : ventas,\n    'lag_1'       : ventas.shift(1),\n    'diff_1'      : ventas.diff(1),\n    'pct_change'  : ventas.pct_change() * 100,\n})\nprint(df.head(6).round(2))"),
        Cell("md", "## 6️⃣ Timezones — `tz_localize` y `tz_convert`\n\n```python\ns.tz_localize('UTC')           # asigna TZ (no convierte)\ns.tz_convert('America/Santiago')  # convierte a otra TZ\n```\n\nRegla: primero **localize** (asigna), luego **convert** (mueve)."),
        Cell("code", "naive = pd.Series([1, 2, 3], index=pd.date_range('2024-01-01', periods=3, freq='h'))\nutc = naive.tz_localize('UTC')\nscl = utc.tz_convert('America/Santiago')   # -3h o -4h según DST\nprint('UTC:'); print(utc)\nprint('Santiago:'); print(scl)"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Parseo fechas con `to_datetime(errors='coerce')`\n- [ ] Indexo por fecha y sliceo con strings\n- [ ] Resampleo a la frecuencia objetivo + agg\n- [ ] Uso rolling para suavizar tendencias\n- [ ] Sé hacer lag features con `shift`/`diff`"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Parseo, slice por trimestre, resample mensual, rolling 7/30 con plot, diff."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.12\n- [pandas Time Series](https://pandas.pydata.org/docs/user_guide/timeseries.html)\n\n➡️ **Siguiente:** [032 — eval y query](../032-pandas-eval-y-query/README.md)"),
    ],
))


SPECS.append(ClassSpec(
    folder="032-pandas-eval-y-query",
    number="032",
    title="Pandas: eval y query",
    duration="45 min",
    source="VanderPlas, **cap. 3** § 3.13 *High-Performance Pandas: eval and query*.",
    objetivo=(
        "Que el alumno conozca `df.eval` y `df.query` — herramientas para expresar operaciones "
        "y filtros con sintaxis tipo SQL en strings. Útiles para legibilidad en cadenas largas "
        "y, en datasets muy grandes, también más rápidos (usan `numexpr`)."
    ),
    resultados=[
        "**Filtrar** con `df.query(\"col > 10 and other == 'X'\")`.",
        "**Calcular columnas nuevas** con `df.eval('z = x + y')` o `df.eval('x * 2')`.",
        "**Referenciar variables locales** en query/eval con prefijo `@`: `df.query('x > @threshold')`.",
        "**Decidir** cuándo usar query (legibilidad en cadenas largas) vs filtro tradicional (mejor autocompletado IDE).",
        "**Saber** que el speedup real solo aparece con datasets >10k filas y expresiones complejas.",
    ],
    temas=[
        ("`df.query` — sintaxis tipo SQL", "Una sola string en vez de máscara compuesta."),
        ("`df.eval` — expresiones aritméticas", "Calcula columnas sin temporales."),
        ("Variables locales con `@`", "Pasar valores del scope."),
        ("`numexpr` para speedup", "Solo en datasets grandes."),
        ("Trade-off: legibilidad vs introspección IDE", "Query strings no tienen autocompletado."),
    ],
    dataset="Sintético: DataFrame grande para benchmark. Sin descarga.",
    ejercicios=[
        "**Filter tradicional vs query.** `df[(df.a > 10) & (df.b < 5) & (df.c == 'x')]` vs `df.query('a > 10 and b < 5 and c == \"x\"')`. Compara legibilidad.",
        "**Variable local.** `threshold = 100`; filtra con `df.query('precio > @threshold')`.",
        "**eval para nueva columna.** `df.eval('total = precio * cantidad', inplace=True)`.",
        "**Benchmark.** Genera df 1M filas. Compara filter tradicional vs query con `%timeit`.",
        "**eval con `inplace=False`** vs cálculo tradicional `df['total'] = df['precio'] * df['cantidad']` — verifica resultados idénticos.",
    ],
    homework=(
        "Notebook con df 100k filas: (a) 3 filtros equivalentes (mask, query, query con @var); "
        "(b) eval para crear 2 columnas derivadas; (c) benchmark tradicional vs query en N=100k "
        "y N=1M; (d) reporte: cuándo conviene cada uno."
    ),
    homework_criterio="Resultados idénticos entre métodos. Speedup de query aparece en N≥100k.",
    referencias=[
        "VanderPlas, **cap. 3** § 3.13.",
        "[pandas eval/query docs](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)",
        "[`numexpr` project](https://numexpr.readthedocs.io/)",
    ],
    siguiente=("033-matplotlib-anatomia-figura-axes", "Matplotlib: anatomía figura/axes"),
    cells=[
        Cell("md", "# Clase 032 — eval y query\n\n**Parte 0** · VanderPlas cap. 3 § 3.13.\n\n> 🎯 Filtros y cálculos como strings tipo SQL. Útil para legibilidad y datasets grandes.\n\n> ⏱️ ~45 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport pandas as pd\nimport time\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ `df.query` — filtro como string"),
        Cell("code", "df = pd.DataFrame({\n    'precio'    : rng.uniform(10, 1000, 20).round(2),\n    'cantidad'  : rng.integers(1, 50, 20),\n    'categoria' : rng.choice(['A', 'B', 'C'], 20),\n})\n\n# Filtro tradicional\nmask = (df['precio'] > 100) & (df['cantidad'] < 30) & (df['categoria'] == 'A')\nfiltrado_a = df[mask]\n\n# Equivalente con query\nfiltrado_b = df.query('precio > 100 and cantidad < 30 and categoria == \"A\"')\n\nprint('mismo resultado:', filtrado_a.equals(filtrado_b))\nprint(filtrado_b)"),
        Cell("md", "## 2️⃣ Variables locales con `@`\n\nReferencia variables del scope con prefijo `@`:"),
        Cell("code", "threshold_precio = 500\ncategoria_objetivo = 'A'\n\nresult = df.query('precio > @threshold_precio and categoria == @categoria_objetivo')\nprint(result)"),
        Cell("md", "## 3️⃣ `df.eval` — expresiones aritméticas\n\nCalcula columnas sin temporales y, en datasets grandes, usando `numexpr` (más rápido)."),
        Cell("code", "# Tradicional\ndf['total_a'] = df['precio'] * df['cantidad']\n\n# Con eval\ndf['total_b'] = df.eval('precio * cantidad')\n\n# inplace: añade al DataFrame\ndf.eval('descuento = precio * 0.1', inplace=True)\n\nprint(df[['precio', 'cantidad', 'total_a', 'total_b', 'descuento']].head())\nprint('\\niguales total_a == total_b?', (df['total_a'] == df['total_b']).all())"),
        Cell("md", "## 4️⃣ Cuándo conviene query/eval\n\n**Sí**:\n- Cadenas de filtros largas → más legible una string que `(a) & (b) & (c) & (d)`.\n- Datasets grandes (>10k filas) con expresiones complejas → `numexpr` da speedup.\n- Filtros parametrizables (con `@`) sin construir máscaras complejas.\n\n**No**:\n- Datasets pequeños — overhead del parser no compensa.\n- Cuando necesitas autocomplete del IDE — strings no se autocompletan.\n- Cuando el filtro usa métodos custom (no es solo aritmética/comparación)."),
        Cell("md", "## 5️⃣ Benchmark — speedup en grandes"),
        Cell("code", "N = 1_000_000\nbig = pd.DataFrame({\n    'a': rng.normal(0, 1, N),\n    'b': rng.normal(0, 1, N),\n    'c': rng.choice(['x','y','z'], N),\n})\n\nt0 = time.perf_counter()\n_ = big[(big['a'] > 0.5) & (big['b'] < -0.5) & (big['c'] == 'x')]\nt1 = time.perf_counter()\n\nt2 = time.perf_counter()\n_ = big.query('a > 0.5 and b < -0.5 and c == \"x\"')\nt3 = time.perf_counter()\n\nprint(f'tradicional : {(t1-t0)*1000:.1f} ms')\nprint(f'query       : {(t3-t2)*1000:.1f} ms')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé escribir filtros largos con `df.query`\n- [ ] Uso `@var` para referenciar variables locales\n- [ ] Uso `df.eval` para columnas derivadas sin temporales\n- [ ] Sé que el speedup aparece en datasets grandes\n- [ ] Reconozco trade-off: legibilidad vs autocomplete IDE"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 3 filtros equivalentes, eval para cols, benchmark en 1M filas."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 3 § 3.13\n- [pandas enhancing perf](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)\n\n➡️ **Siguiente:** [033 — Matplotlib: anatomía figura/axes](../033-matplotlib-anatomia-figura-axes/README.md)"),
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
