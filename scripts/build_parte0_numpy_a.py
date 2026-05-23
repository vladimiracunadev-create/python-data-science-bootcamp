"""Classes 014-017 — NumPy A: tipos/creación, ufuncs, agregaciones, broadcasting.

Basado en VanderPlas cap. 2 (Introduction to NumPy).
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="014-numpy-tipos-creacion-atributos",
    number="014",
    title="NumPy: tipos, creación, atributos",
    duration="75 min",
    source="VanderPlas, *Python Data Science Handbook*, **cap. 2** — *Introduction to NumPy*, §§ 2.1–2.2.",
    objetivo=(
        "Que el alumno entienda el modelo mental de un `ndarray` — bloque contiguo de memoria con "
        "shape, dtype y strides — y sepa crear arrays de las 6 formas más útiles (`array`, `zeros`, "
        "`arange`, `linspace`, `random`, desde lista). Sin este modelo, todo el rendimiento de NumPy "
        "parece magia."
    ),
    resultados=[
        "**Explicar** por qué `ndarray` es 50–100× más rápido que `list` (memoria contigua + dtype fijo + sin overhead Python).",
        "**Crear arrays** con `np.array`, `np.zeros`, `np.ones`, `np.full`, `np.arange`, `np.linspace`.",
        "**Inspeccionar** un array con `shape`, `dtype`, `ndim`, `size`, `nbytes`, `itemsize`.",
        "**Cambiar dtype** explícitamente con `astype` y entender promociones implícitas (`int + float = float`).",
        "**Generar arrays aleatorios reproducibles** con `np.random.default_rng(seed)`.",
    ],
    temas=[
        ("`ndarray`: memoria contigua + dtype fijo", "Lo que lo hace rápido."),
        ("Creación: `array`, `zeros`, `arange`, `linspace`", "Las 6 formas más usadas."),
        ("`dtype`: int8/16/32/64, float32/64, bool", "Memoria y precisión."),
        ("Atributos: shape, dtype, ndim, size, nbytes", "Diagnóstico instantáneo."),
        ("`astype` y promoción de tipos", "El bug clásico de overflow int8."),
        ("`random` moderno: `default_rng(seed)`", "El API legacy `np.random.seed` está deprecated."),
    ],
    dataset=(
        "Sintético: arrays generados en el notebook (escalares, matrices, aleatorios reproducibles). "
        "Sin descarga."
    ),
    ejercicios=[
        "**Memoria.** Crea `list(range(1_000_000))` y `np.arange(1_000_000)`. Compara `sys.getsizeof` y `arr.nbytes`. Calcula el ratio.",
        "**Las 6 formas.** Crea: vector 100 ceros, matriz 5×5 unos, vector 0..1 con 50 puntos equiespaciados, matriz 3×3 de 7s, vector de 100 aleatorios uniformes [0,1).",
        "**Bug de dtype.** Crea `np.array([100, 200, 50], dtype=np.int8)` y suma 200 a cada elemento. Observa el resultado y explica.",
        "**Diagnóstico.** Dado un array, escribe una función que imprima shape, dtype, ndim, size, nbytes y memoria humana (KB/MB).",
        "**Random reproducible.** Genera 1000 normales N(0,1) con seed=42. Calcula media y std. Repite — debe dar exactamente lo mismo.",
    ],
    homework=(
        "Notebook que: (a) compara memoria list vs ndarray para N=1M con tabla; (b) crea las 6 formas "
        "y reporta dtype default de cada una; (c) reproduce el bug de overflow int8 con explicación; "
        "(d) función `info(arr)` con diagnóstico completo."
    ),
    homework_criterio="El ratio memoria list/ndarray es >5×. La función `info` reporta todos los atributos.",
    referencias=[
        "VanderPlas, **cap. 2**, §§ 2.1–2.2 *Understanding Data Types* + *The Basics of NumPy Arrays*.",
        "[NumPy user guide — Array creation](https://numpy.org/doc/stable/user/basics.creation.html)",
        "[NumPy dtypes](https://numpy.org/doc/stable/reference/arrays.dtypes.html)",
        "[`Generator` random API](https://numpy.org/doc/stable/reference/random/generator.html)",
    ],
    siguiente=("015-numpy-ufuncs-y-vectorizacion", "NumPy: ufuncs y vectorización"),
    cells=[
        Cell("md", "# Clase 014 — NumPy: tipos, creación, atributos\n\n**Parte 0** · VanderPlas cap. 2 §§ 2.1-2.2.\n\n> 🎯 Entender por qué `ndarray` es rápido y crear arrays de las 6 formas más usadas.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import sys\nimport numpy as np\nprint('numpy:', np.__version__)"),
        Cell("md", "## 1️⃣ ¿Por qué `ndarray` es rápido?\n\nUn `list` de Python es **un array de punteros a objetos PyObject**:\n```\nlist = [→PyInt(1), →PyInt(2), →PyInt(3), ...]\n```\nCada elemento tiene overhead (~28 bytes en CPython 3.12). Operaciones llaman al intérprete para cada elemento.\n\nUn `ndarray` es **un bloque contiguo de memoria con dtype fijo**:\n```\nndarray(int64) = [1, 2, 3, ...]   ← 8 bytes por elemento, sin overhead\n```\nOperaciones se ejecutan en C, vectorizadas (SIMD)."),
        Cell("code", "import sys\nN = 100_000\n\nlst = list(range(N))\narr = np.arange(N)\n\n# Memoria list (sum de getsizeof de cada elemento + overhead lista)\nmem_list = sys.getsizeof(lst) + sum(sys.getsizeof(x) for x in lst[:100]) * (N // 100)\nmem_arr  = arr.nbytes\n\nprint(f'list  : ~{mem_list/1024:.0f} KB')\nprint(f'array : {mem_arr/1024:.0f} KB')\nprint(f'ratio : {mem_list/mem_arr:.1f}×')"),
        Cell("md", "## 2️⃣ Las 6 formas de crear arrays\n\nVanderPlas las llama \"the array creation routines\":"),
        Cell("code", "# 1) Desde lista Python\na1 = np.array([1, 2, 3, 4])\nprint('array:', a1, '  dtype:', a1.dtype)\n\n# 2) Zeros / ones / full (forma y dtype controlados)\nprint('zeros(5):', np.zeros(5))                        # float64 por default\nprint('ones((2,3), int):', np.ones((2,3), dtype=int))\nprint('full((2,2), 7):', np.full((2,2), 7))\n\n# 3) Rangos\nprint('arange(0,10,2):', np.arange(0, 10, 2))\nprint('linspace(0,1,5):', np.linspace(0, 1, 5))\n\n# 4) Aleatorios (API moderno con Generator)\nrng = np.random.default_rng(seed=42)\nprint('uniform(3):', rng.random(3))\nprint('normal(3):', rng.normal(0, 1, 3))\n\n# 5) Identidad y eye\nprint('eye(3):'); print(np.eye(3))\n\n# 6) Empty (sin inicializar — más rápido, contenido basura)\ne = np.empty(3)\nprint('empty(3):', e, '  ← contenido no inicializado, NO confiar')"),
        Cell("md", "## 3️⃣ Atributos: diagnóstico instantáneo\n\nCuando algo no funciona, **antes de pensar**, mira los atributos:"),
        Cell("code", "M = np.arange(24).reshape(2, 3, 4)\nprint(f'shape    : {M.shape}')     # (2, 3, 4)\nprint(f'ndim     : {M.ndim}')      # 3 dimensiones\nprint(f'size     : {M.size}')      # 24 elementos total\nprint(f'dtype    : {M.dtype}')\nprint(f'itemsize : {M.itemsize} bytes/elem')\nprint(f'nbytes   : {M.nbytes} bytes total')\nprint(f'strides  : {M.strides}')   # cuánto avanzar en memoria por dim"),
        Cell("md", "## 4️⃣ `dtype` — memoria vs precisión\n\nDtypes principales (VanderPlas tabla 2-1):\n\n| dtype | bytes | rango |\n|---|---|---|\n| `int8`  | 1 | -128 a 127 |\n| `int16` | 2 | -32k a 32k |\n| `int32` | 4 | ±2.1e9 |\n| `int64` | 8 | ±9.2e18 (default en Linux/macOS, int32 default en Windows < numpy 2.0) |\n| `uint8` | 1 | 0 a 255 (imágenes RGB) |\n| `float32` | 4 | ±3.4e38, ~7 dígitos precisión |\n| `float64` | 8 | ±1.7e308, ~15 dígitos (default) |\n| `bool` | 1 | True/False |\n\n**Elige `float32`** cuando trabajes con redes neuronales en GPU (la mitad de memoria, suficiente precisión para gradientes)."),
        Cell("md", "## 5️⃣ ⚠️ Bug clásico: overflow silencioso\n\nNumPy no levanta excepción cuando un dtype no alcanza — *wrap-around* silencioso:"),
        Cell("code", "# Overflow demo\na = np.array([100, 200, 50], dtype=np.int8)\nprint('original:', a)\nb = a + 200\nprint('+200    :', b, '  ← ¡debería ser [300, 400, 250]!')\nprint('  por qué: int8 va de -128 a 127, los valores hicieron wrap-around')\n\n# Fix: dtype suficiente o promoción explícita\nc = a.astype(np.int32) + 200\nprint('fix     :', c)"),
        Cell("md", "## 6️⃣ Random reproducible — API moderno\n\n```python\n# ❌ legacy (deprecated en favor del nuevo Generator)\nnp.random.seed(42)\nnp.random.rand(5)\n\n# ✅ moderno\nrng = np.random.default_rng(seed=42)\nrng.random(5)\nrng.normal(0, 1, 5)\nrng.integers(0, 10, 5)\n```\n\nVentajas: independiente entre instancias (puedes tener varios rngs), algoritmo más rápido (PCG64), API más limpio."),
        Cell("code", "# Mismo seed → mismo output (reproducibilidad)\nrng_a = np.random.default_rng(seed=42)\nrng_b = np.random.default_rng(seed=42)\nprint(rng_a.normal(0, 1, 5))\nprint(rng_b.normal(0, 1, 5))   # idéntico\nprint('iguales?', np.array_equal(rng_a.normal(0,1,5), rng_b.normal(0,1,5)))"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé por qué ndarray es más rápido que list\n- [ ] Conozco las 6 formas de crear arrays\n- [ ] Sé inspeccionar shape, dtype, ndim, nbytes\n- [ ] Anticipé overflow al elegir dtype\n- [ ] Uso `np.random.default_rng(seed)` no `np.random.seed`"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Memoria list vs ndarray, 6 formas, overflow int8, función `info(arr)`."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 2 §§ 2.1-2.2\n- [Array creation](https://numpy.org/doc/stable/user/basics.creation.html)\n- [Generator API](https://numpy.org/doc/stable/reference/random/generator.html)\n\n➡️ **Siguiente:** [015 — NumPy: ufuncs y vectorización](../015-numpy-ufuncs-y-vectorizacion/README.md)"),
    ],
    definiciones=[
        ("`ndarray`", "Estructura de datos central de NumPy. Bloque contiguo de memoria con dtype fijo + metadata (shape, strides). 50–100× más rápido que list por evitar el overhead de PyObject por elemento y permitir vectorización SIMD."),
        ("`dtype`", "Tipo de elemento del array: `int8/16/32/64`, `uint8` (imágenes RGB), `float32/64`, `bool`, `complex64/128`. Determina memoria por elemento (`itemsize`) y precisión/rango."),
        ("`shape`", "Tupla con tamaño de cada dimensión: `(10,)` 1D, `(3, 4)` matriz, `(2, 3, 4)` tensor 3D. `len(shape)` = `ndim`. `prod(shape)` = `size` (total elementos)."),
        ("`strides`", "Bytes que el array salta para moverse 1 paso en cada dimensión. Permite vistas eficientes sin copiar memoria (transpose, slicing). Detalle interno pero útil para entender por qué algunas operaciones son gratis."),
        ("`Generator` (random)", "API moderno para aleatoriedad: `rng = np.random.default_rng(seed)`. Reemplaza al legacy `np.random.seed()` + funciones globales. Características: PCG64 (mejor algoritmo), múltiples generadores independientes, API consistente."),
        ("Promoción de tipo", "Cuando operas arrays de dtypes distintos, NumPy promueve al más amplio: `int + float = float`, `int8 + int16 = int16`. La regla evita pérdida silenciosa pero puede generar overflow en otros casos (clase: overflow int8)."),
    ],
    errores_comunes=[
        ("`OverflowError` silencioso con int8/uint8", "NumPy no lanza excepción — hace wrap-around: `np.array([200], dtype=uint8) + 100` da `44`. **Fix**: usa dtype más amplio (`int32`/`int64`) o `astype` antes de la operación."),
        ("`np.array([1, 2, 'x'])` queda como `dtype='<U21'`", "NumPy promueve TODO a string para ser homogéneo. **Fix**: separa los tipos o usa pandas (que sí permite columnas heterogéneas)."),
        ("`np.empty(3)` con basura en vez de ceros", "`empty` NO inicializa — más rápido que `zeros` pero contiene lo que había en memoria. **Fix**: usa `np.zeros` si necesitas ceros garantizados."),
        ("Reproduzco un experimento con seed y da resultados distintos", "Estás usando el API legacy (`np.random.seed`) con varias librerías que también lo modifican. **Fix**: usa `np.random.default_rng(seed)` — independiente, no afecta el estado global."),
        ("`np.arange(0.1, 1.0, 0.1)` no incluye `1.0`", "Floats — el último step da `0.9999...` por imprecisión. **Fix**: usa `np.linspace(0.1, 1.0, 10)` que controla N puntos exactos."),
    ],
    faq=[
        ("¿`np.array([1,2,3])` o `np.asarray([1,2,3])`?",
         "`asarray` no copia si ya es ndarray (más eficiente); `array` siempre copia por default. Usa `asarray` cuando aceptas cualquier 'array-like' y no necesitas garantizar copia."),
        ("¿`float32` o `float64`?",
         "Default es `float64` — máxima precisión. **`float32`** cuando trabajas con redes neuronales en GPU (la mitad de memoria, suficiente para gradientes), imágenes, o necesitas duplicar la velocidad de IO."),
        ("¿Cuándo `int32` y cuándo `int64`?",
         "Default depende del OS (int64 Unix/macOS, int32 Windows pre-numpy 2.0). En 2026, NumPy 2+ usa int64 en todas las plataformas. Solo bajes a int32 si memoria es crítica y sabes que tus valores caben."),
        ("¿`np.random.seed(42)` ya no se usa?",
         "Funciona pero está deprecated en favor del nuevo API. Razones: estado global (peligroso), Mersenne Twister (lento), no permite múltiples streams independientes. Usa `default_rng(seed)`."),
        ("¿Por qué `arr.nbytes` no coincide con `sys.getsizeof(arr)`?",
         "`nbytes` cuenta solo los datos (`size * itemsize`). `getsizeof` cuenta también el header del objeto ndarray (~100 bytes). Para arrays grandes la diferencia es despreciable."),
    ],
))


SPECS.append(ClassSpec(
    folder="015-numpy-ufuncs-y-vectorizacion",
    number="015",
    title="NumPy: ufuncs y vectorización",
    duration="75 min",
    source="VanderPlas, **cap. 2**, § 2.3 *Computation on NumPy Arrays: Universal Functions*.",
    objetivo=(
        "Que el alumno **abandone los `for` loops** sobre arrays NumPy y use ufuncs (universal "
        "functions) para operaciones elementwise — la fuente real del speedup. Ufuncs son C "
        "compilado vectorizado; un `for` Python sobre array es lo peor de ambos mundos."
    ),
    resultados=[
        "**Identificar** una ufunc (`np.add`, `np.multiply`, `np.sin`, `np.exp`, `np.log`, comparadores).",
        "**Reemplazar** un `for+append` por una expresión vectorizada y medir el speedup.",
        "**Usar el parámetro `out=`** para escribir el resultado in-place (evita allocar memoria extra).",
        "**Combinar** ufuncs con operadores aritméticos (`+`, `-`, `*`, `/`, `**`).",
        "**Reconocer** las trampas de la vectorización (overflow, NaN propagación, división por cero).",
    ],
    temas=[
        ("¿Qué es una ufunc?", "Función C vectorizada elementwise."),
        ("Ufuncs unarias y binarias", "`np.exp(x)` vs `np.add(x, y)`."),
        ("Operadores → ufuncs", "`a + b` ≡ `np.add(a, b)`."),
        ("`out=` para in-place", "Memoria O(1) extra."),
        ("Trampas: overflow, NaN, inf, división por cero", "NumPy avisa pero no para."),
        ("`np.where(cond, a, b)`", "Ternario vectorizado."),
    ],
    dataset="Sintético: arrays grandes para benchmark. Sin descarga.",
    ejercicios=[
        "**Benchmark.** Calcula `[x*x + 2*x + 1 for x in range(1_000_000)]` vs `arr*arr + 2*arr + 1`. Mide con `%timeit`.",
        "**Logaritmo y exponencial.** Con `np.exp` y `np.log`, verifica que `log(exp(x)) ≈ x` para 1000 valores. Reporta el error máximo.",
        "**In-place vs alloc.** `arr = arr * 2 + 1` vs `np.multiply(arr, 2, out=arr); np.add(arr, 1, out=arr)`. Compara `tracemalloc`.",
        "**`np.where` ternario.** Dado un array de notas, crea otro array con `'aprobado'` si nota >= 4, `'reprobado'` si no.",
        "**Trampa NaN.** Crea `np.array([1, 2, np.nan, 4]).sum()` y `.mean()`. Compara con `np.nansum` y `np.nanmean`.",
    ],
    homework=(
        "Notebook: (a) reescribe 3 loops como expresiones vectorizadas + tabla con `%timeit` (3 N "
        "distintos); (b) demuestra `out=` con `tracemalloc`; (c) usa `np.where` para clasificar "
        "datos; (d) maneja NaN con `nansum/nanmean` y compara con propagación."
    ),
    homework_criterio="Speedup >50× en N=1M. `out=` muestra memoria ≈ 0 extra. NaN-handling correcto.",
    referencias=[
        "VanderPlas, **cap. 2** § 2.3 *Computation on NumPy Arrays*.",
        "[NumPy ufuncs reference](https://numpy.org/doc/stable/reference/ufuncs.html)",
    ],
    siguiente=("016-numpy-agregaciones", "NumPy: agregaciones"),
    cells=[
        Cell("md", "# Clase 015 — NumPy: ufuncs y vectorización\n\n**Parte 0** · VanderPlas cap. 2 § 2.3.\n\n> 🎯 Abandonar `for` sobre arrays. Ufuncs = funciones C vectorizadas elementwise — el speedup real.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport time, tracemalloc\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ ¿Qué es una ufunc?\n\nUna **universal function** es una función NumPy que opera **elementwise** sobre arrays, implementada en C y vectorizada (SIMD cuando posible).\n\n**Unarias** (un input): `np.exp`, `np.log`, `np.sin`, `np.sqrt`, `np.abs`, `np.negative`...\n**Binarias** (dos inputs): `np.add`, `np.multiply`, `np.divide`, `np.power`, `np.maximum`...\n\nLos **operadores** (`+`, `-`, `*`, `/`, `**`, `==`, `<`...) son sintaxis dulce sobre ufuncs."),
        Cell("md", "## 2️⃣ El speedup en vivo"),
        Cell("code", "N = 1_000_000\nlst = list(range(N))\narr = np.arange(N)\n\n# Versión Python\nt0 = time.perf_counter()\nres_py = [x*x + 2*x + 1 for x in lst]\nt1 = time.perf_counter()\n\n# Versión vectorizada\nt2 = time.perf_counter()\nres_np = arr*arr + 2*arr + 1\nt3 = time.perf_counter()\n\nprint(f'Python loop : {(t1-t0)*1000:.1f} ms')\nprint(f'NumPy vec   : {(t3-t2)*1000:.1f} ms')\nprint(f'speedup     : {(t1-t0)/(t3-t2):.0f}×')"),
        Cell("md", "## 3️⃣ Operadores como ufuncs\n\n```python\na + b   ≡  np.add(a, b)\na * b   ≡  np.multiply(a, b)\na ** b  ≡  np.power(a, b)\na == b  ≡  np.equal(a, b)\na > b   ≡  np.greater(a, b)\n-a      ≡  np.negative(a)\n```\n\nEsto significa que `arr*arr + 2*arr + 1` son 4 ufuncs encadenadas — cada una alloca un array temporal. Para ahorrar memoria, usa `out=`:"),
        Cell("code", "# Sin out=: cada operación alloca\nA = rng.random(1_000_000)\ntracemalloc.start()\nresult = A * A + 2*A + 1\n_, peak1 = tracemalloc.get_traced_memory()\ntracemalloc.stop()\nprint(f'sin out= : peak {peak1/1024:.0f} KB')\n\n# Con out=: in-place, sin allocs\nA = rng.random(1_000_000)\ntracemalloc.start()\nnp.multiply(A, A, out=A)\nnp.multiply(2, A, out=A)   # nota: el segundo factor podría ser otro array\nnp.add(A, 1, out=A)\n_, peak2 = tracemalloc.get_traced_memory()\ntracemalloc.stop()\nprint(f'con out= : peak {peak2/1024:.0f} KB')\nprint(f'ratio    : {peak1/max(peak2,1):.1f}×')"),
        Cell("md", "## 4️⃣ Ufuncs trigonométricas, exponenciales y logarítmicas\n\nVanderPlas tabla 2-4:"),
        Cell("code", "x = np.linspace(0, 2*np.pi, 5)\nprint('x       :', x)\nprint('sin(x)  :', np.sin(x))\nprint('cos(x)  :', np.cos(x))\nprint()\nprint('exp(x)  :', np.exp(x[:3]))\nprint('log(...):', np.log(np.exp(x[:3])))   # log(exp(x)) ≈ x\nprint('sqrt    :', np.sqrt([1, 4, 9, 16]))\nprint('abs     :', np.abs([-3, 5, -7]))"),
        Cell("md", "## 5️⃣ `np.where` — ternario vectorizado\n\n```python\nnp.where(cond_array, valor_si_true, valor_si_false)\n```\n\nUtil para clasificar, máscaras, sustituciones:"),
        Cell("code", "notas = np.array([2.8, 4.5, 6.1, 3.2, 7.0, 5.5])\nestado = np.where(notas >= 4, 'aprobado', 'reprobado')\nfor n, e in zip(notas, estado):\n    print(f'{n}: {e}')"),
        Cell("md", "## 6️⃣ ⚠️ Trampas\n\n**Overflow silencioso** (ya visto en clase 014). NumPy no para, sólo wrap-around.\n\n**NaN propagación**: cualquier operación con NaN produce NaN:\n\n```python\nnp.array([1, 2, np.nan, 4]).sum()    # nan\nnp.array([1, 2, np.nan, 4]).mean()   # nan\n```\n\n**Fix**: usa las variantes `nan*`:\n\n```python\nnp.nansum(arr)     # ignora NaN\nnp.nanmean(arr)    # ignora NaN\nnp.nanmedian(arr)\n```\n\n**División por cero**: produce `inf` con warning. Para silenciar (o convertir a NaN), usa `np.errstate`:"),
        Cell("code", "a = np.array([1, 2, np.nan, 4, 5])\nprint(f'sum      : {a.sum()}')           # nan\nprint(f'nansum   : {np.nansum(a)}')      # 12\nprint(f'mean     : {a.mean()}')\nprint(f'nanmean  : {np.nanmean(a)}')\n\nprint()\nwith np.errstate(divide='ignore', invalid='ignore'):\n    res = np.array([1, 0, -1]) / np.array([0, 0, 0])\n    print('1/0, 0/0, -1/0 :', res)   # inf, nan, -inf"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé qué es una ufunc y por qué es rápida\n- [ ] Reescribo `for+append` como expresión vectorizada\n- [ ] Uso `out=` para ahorrar memoria\n- [ ] Conozco `np.where` para ternarios vectorizados\n- [ ] Manejo NaN con `nansum`/`nanmean`"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 3 loops reescritos con benchmark, demo `out=`, `np.where`, manejo NaN."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 2 § 2.3\n- [ufuncs reference](https://numpy.org/doc/stable/reference/ufuncs.html)\n\n➡️ **Siguiente:** [016 — Agregaciones](../016-numpy-agregaciones/README.md)"),
    ],
    definiciones=[
        ("Ufunc (universal function)", "Función NumPy implementada en C que opera **elementwise** y vectorizada (SIMD cuando posible). Características: rápida (10-100× vs Python), broadcasting automático, soporta `out=` para in-place."),
        ("Vectorización", "Operar sobre arrays completos en vez de loops Python: `arr * 2` en vez de `[x*2 for x in arr]`. La operación corre en C compilado sobre memoria contigua, sin overhead del intérprete por elemento."),
        ("In-place (`out=`)", "Escribir el resultado de una ufunc en un array existente, sin allocar memoria nueva: `np.multiply(a, 2, out=a)`. Útil con arrays grandes donde la copia temporal duplicaría la memoria pico."),
        ("Propagación de NaN", "Cualquier operación que tenga `NaN` como input produce `NaN`. `np.array([1, np.nan, 3]).sum()` → `nan`. Para ignorar usa variantes `nan*`: `nansum`, `nanmean`, `nanmedian`."),
        ("`np.where(cond, a, b)`", "Ternario vectorizado: para cada elemento, si `cond` es True usa `a`, si no usa `b`. Equivale a `[a if c else b for c, a, b in zip(cond, a, b)]` pero ~100× más rápido."),
    ],
    errores_comunes=[
        ("`for i in range(len(arr)): arr[i] = ...` es lentísimo", "Loops Python sobre array NumPy = lo peor de ambos mundos. **Fix**: reescribe como expresión vectorizada (`arr = ...`) o usa ufunc explícita."),
        ("RuntimeWarning: divide by zero / invalid value", "NumPy avisa pero no para: `1/0` → `inf`, `0/0` → `nan`. **Fix**: filtra antes (`arr[arr != 0]`) o silencia con `np.errstate(divide='ignore', invalid='ignore')`."),
        ("`out=` con dtype incompatible", "`np.add(int_arr, 0.5, out=int_arr)` falla — float no cabe en int. **Fix**: convierte primero (`arr = arr.astype(float)`) o usa array distinto como destino."),
        ("Resultado de `np.where` no es lo esperado", "Los 3 args se evalúan **completos**: `np.where(arr>0, 1/arr, 0)` calcula `1/arr` para TODOS los elementos (incluso negativos → division por cero). **Fix**: usa `np.where` solo para values planos, no expresiones."),
        ("`arr.sum()` da NaN y no sé por qué", "Hay un NaN escondido en el array. **Fix**: `print(np.isnan(arr).sum())` para contar; usa `np.nansum()` para ignorar."),
    ],
    faq=[
        ("¿Cuánto más rápido es vectorizar?",
         "Típicamente 50-100× para arrays de 1M elementos. Para arrays pequeños (<100), la ganancia es menor o nula (overhead constante). Mide con `%timeit`, no asumas."),
        ("¿`arr + 1` o `np.add(arr, 1)`?",
         "Equivalentes. Operadores son sintaxis dulce sobre ufuncs. Usa `np.add(...)` cuando necesitas `out=` (in-place) o `where=` (mask)."),
        ("¿NumPy aprovecha mi GPU?",
         "**No** — solo CPU. Para GPU: CuPy (drop-in replacement), PyTorch tensors, JAX. NumPy 2 está mejorando vectorización CPU (SIMD wider, BLAS) pero sigue siendo CPU."),
        ("¿Por qué `arr ** 2` es más rápido que `arr * arr`?",
         "Suelen empatar (`**` también es ufunc). Para potencias enteras pequeñas (2, 3), NumPy a veces usa atajos. Mide con `%timeit` en tu caso específico."),
        ("¿`np.where` o boolean mask?",
         "**Mask** (`arr[cond] = valor`) si vas a modificar in-place o filtrar (`arr[arr>0]`). **`np.where(cond, a, b)`** si necesitas un array nuevo con dos valores posibles según condición."),
    ],
))


SPECS.append(ClassSpec(
    folder="016-numpy-agregaciones",
    number="016",
    title="NumPy: agregaciones",
    duration="60 min",
    source="VanderPlas, **cap. 2** § 2.4 *Aggregations: Min, Max, and Everything in Between*.",
    objetivo=(
        "Que el alumno reduzca arrays a estadísticos (sum, mean, std, percentile, min, max) "
        "controlando el `axis` correcto — la fuente del 50% de los bugs de pandas/sklearn cuando "
        "alguien se confunde de eje. También: variantes `nan*` y reducciones acumulativas."
    ),
    resultados=[
        "**Calcular** sum, mean, std, var, median, percentile sobre arrays.",
        "**Controlar el eje** con `axis=0` (a lo largo de filas, da resultado por columna) y `axis=1` (a lo largo de columnas, da por fila).",
        "**Usar variantes `nan*`** (nansum, nanmean, etc.) cuando hay datos faltantes.",
        "**Reducciones acumulativas** con `cumsum` y `cumprod`.",
        "**Encontrar índice** del min/max con `argmin`/`argmax`.",
    ],
    temas=[
        ("Reducciones básicas", "sum, mean, std, var, min, max, median, percentile."),
        ("Eje: el bug más común", "`axis=0` reduce filas (resultado por columna)."),
        ("Variantes NaN-aware", "nansum, nanmean, nanmedian, nanstd."),
        ("Acumulativas", "cumsum, cumprod — útiles para series temporales."),
        ("argmin/argmax", "Posición del extremo."),
        ("`all` y `any`", "Reducciones booleanas."),
    ],
    dataset=(
        "Sintético (matriz aleatoria 100×10 simulando \"10 features × 100 muestras\") generado en "
        "el notebook. Sin descarga."
    ),
    ejercicios=[
        "**Promedio por columna.** Dada matriz 100×4 de ventas (filas=día, cols=tienda), calcula la media por tienda y por día.",
        "**Estadísticos completos.** Para un array de 1000 normales, reporta mean, std, median, p25, p75, min, max.",
        "**Con NaN.** Inserta 50 NaN aleatorios en el array anterior. Compara `mean` (propaga) vs `nanmean`.",
        "**Cumsum.** Genera array de retornos diarios aleatorios. Calcula el precio acumulado con `cumprod(1+r)`.",
        "**Mejor tienda.** Con la matriz del ejercicio 1, usa `argmax(axis=0)` para encontrar el día de mayor venta de cada tienda.",
    ],
    homework=(
        "Notebook con matriz simulada 365 días × 5 tiendas de ventas, reportando: media/std por "
        "tienda, mejor y peor día de cada tienda, cumsum total anual, % de días con NaN simulados "
        "(20 aleatorios) usando variantes nan*."
    ),
    homework_criterio="Eje correcto en todas las agregaciones; valores reproducibles con seed.",
    referencias=[
        "VanderPlas, **cap. 2** § 2.4.",
        "[NumPy statistics functions](https://numpy.org/doc/stable/reference/routines.statistics.html)",
    ],
    siguiente=("017-numpy-broadcasting", "NumPy: broadcasting"),
    cells=[
        Cell("md", "# Clase 016 — NumPy: agregaciones\n\n**Parte 0** · VanderPlas cap. 2 § 2.4.\n\n> 🎯 Reducir arrays a estadísticos con el `axis` correcto — la fuente del 50% de los bugs de orientación.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Reducciones básicas\n\n```python\narr.sum()      arr.mean()     arr.std()     arr.var()\narr.min()      arr.max()      np.median(arr)\nnp.percentile(arr, 25)         np.percentile(arr, [25, 50, 75])\n```\n\nMétodo del array (`arr.sum()`) o función NumPy (`np.sum(arr)`) — equivalentes."),
        Cell("code", "x = rng.normal(0, 1, 1000)\nprint(f'mean   : {x.mean():.4f}')\nprint(f'std    : {x.std():.4f}')\nprint(f'median : {np.median(x):.4f}')\nprint(f'p25,75 : {np.percentile(x, [25, 75])}')\nprint(f'min,max: ({x.min():.2f}, {x.max():.2f})')"),
        Cell("md", "## 2️⃣ El bug del `axis`\n\nDada una matriz `(rows, cols)`:\n\n- `axis=0` → reduce **filas**, deja **una valor por columna**.\n- `axis=1` → reduce **columnas**, deja **un valor por fila**.\n\nMnemónico: \"el axis que pasas es el que **desaparece**\"."),
        Cell("code", "# Matriz 4 filas × 3 columnas\nM = np.array([\n    [1, 2, 3],\n    [4, 5, 6],\n    [7, 8, 9],\n    [10, 11, 12],\n])\nprint(f'M.shape = {M.shape}')\nprint(f'M.sum()         → escalar : {M.sum()}')\nprint(f'M.sum(axis=0)   → por col : {M.sum(axis=0)}  shape {M.sum(axis=0).shape}')\nprint(f'M.sum(axis=1)   → por fila: {M.sum(axis=1)}  shape {M.sum(axis=1).shape}')"),
        Cell("md", "## 3️⃣ Caso típico: ventas día × tienda\n\nMatriz 100 días × 4 tiendas:"),
        Cell("code", "ventas = rng.integers(50, 500, size=(100, 4))\nprint(f'ventas.shape = {ventas.shape}')\n\nprint('\\n— por tienda (resumen vertical, axis=0) —')\nprint(f'media : {ventas.mean(axis=0).round(1)}')\nprint(f'total : {ventas.sum(axis=0)}')\nprint(f'mejor : {ventas.max(axis=0)}')\n\nprint('\\n— por día (resumen horizontal, axis=1) — primeros 5 días —')\nprint(f'media diaria primeros 5 días: {ventas.mean(axis=1)[:5].round(1)}')"),
        Cell("md", "## 4️⃣ Variantes NaN-aware\n\n| Sin NaN | Con NaN |\n|---|---|\n| `sum`, `mean`, `std`, `var` | `nansum`, `nanmean`, `nanstd`, `nanvar` |\n| `min`, `max`, `median` | `nanmin`, `nanmax`, `nanmedian` |\n| `argmin`, `argmax` | `nanargmin`, `nanargmax` |\n| `percentile` | `nanpercentile` |"),
        Cell("code", "datos = rng.normal(0, 1, 100).copy()\nidx_nans = rng.choice(100, 10, replace=False)\ndatos[idx_nans] = np.nan\n\nprint(f'mean (propaga) : {datos.mean()}')\nprint(f'nanmean        : {np.nanmean(datos):.4f}')\nprint(f'nanmedian      : {np.nanmedian(datos):.4f}')\nprint(f'NaN count      : {np.isnan(datos).sum()}')"),
        Cell("md", "## 5️⃣ Acumulativas: `cumsum`, `cumprod`\n\nÚtiles para series temporales — precio acumulado, drawdown, totales corridos:"),
        Cell("code", "# Retornos diarios pequeños\nretornos = rng.normal(0.001, 0.02, 30)\nprint('retornos:', retornos[:5].round(4), '...')\n\n# Precio acumulado partiendo de 100\nprecio = 100 * np.cumprod(1 + retornos)\nprint(f'precio final: {precio[-1]:.2f}')\nprint(f'precio max  : {precio.max():.2f}')\n\n# Suma acumulada\nventas_diarias = rng.integers(50, 200, 30)\nprint(f'\\nventa total acumulada día 30: {ventas_diarias.cumsum()[-1]}')"),
        Cell("md", "## 6️⃣ `argmin` / `argmax` — posición del extremo\n\nNo el **valor**, el **índice**:"),
        Cell("code", "x = rng.normal(0, 1, 10)\nprint('array      :', x.round(2))\nprint(f'max        : {x.max():.4f}')\nprint(f'argmax     : {x.argmax()}  ← índice del max')\nprint(f'verificación: x[{x.argmax()}] = {x[x.argmax()]:.4f}')\n\n# En matriz: por eje\nM = rng.normal(0, 1, (5, 3))\nprint(f'\\nM.argmax(axis=0) → fila del max por columna: {M.argmax(axis=0)}')\nprint(f'M.argmax(axis=1) → col del max por fila    : {M.argmax(axis=1)}')"),
        Cell("md", "## 7️⃣ `all` y `any` — reducciones booleanas\n\n```python\n(arr > 0).all()        # ¿todos > 0?\n(arr > 0).any()        # ¿al menos uno > 0?\n(M > 0).all(axis=1)    # ¿todas las cols positivas en cada fila?\n```"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Conozco sum/mean/std/median/percentile\n- [ ] Sé que `axis=0` reduce filas (resultado por columna)\n- [ ] Uso variantes `nan*` cuando hay NaN\n- [ ] Uso `cumsum`/`cumprod` para series\n- [ ] Uso `argmax`/`argmin` para encontrar posiciones"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Matriz 365×5 de ventas con análisis completo (media/std por tienda, mejor/peor día, cumsum anual, manejo NaN)."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 2 § 2.4\n- [Statistics functions](https://numpy.org/doc/stable/reference/routines.statistics.html)\n\n➡️ **Siguiente:** [017 — Broadcasting](../017-numpy-broadcasting/README.md)"),
    ],
    definiciones=[
        ("Agregación / reducción", "Operación que **colapsa** un array a menos dimensiones: `sum`, `mean`, `std`, `min`, `max`, `argmax`. Sin `axis`, reduce a un escalar; con `axis=N`, elimina la dimensión N."),
        ("`axis=0` vs `axis=1`", "**Regla**: el axis que pasas es el que **desaparece**. En matriz `(filas, cols)`: `axis=0` colapsa filas → un valor por columna; `axis=1` colapsa cols → un valor por fila. Mnemónico inverso al que muchos esperan."),
        ("`argmin` / `argmax`", "Devuelven el **índice** del extremo (no el valor). `arr.argmax()` = posición del máximo; `arr[arr.argmax()]` = valor máximo. Con `axis=` devuelven array de índices por fila/columna."),
        ("Variantes `nan*`", "Versiones que **ignoran NaN** en vez de propagarlo: `nansum`, `nanmean`, `nanstd`, `nanmin`, `nanmax`, `nanmedian`, `nanpercentile`, `nanargmax`. Útiles cuando los datos tienen missing."),
        ("Acumulativas (`cumsum`, `cumprod`)", "No colapsan — devuelven array de igual shape con valores acumulados hasta cada posición. Útiles para series temporales (precio acumulado, drawdown)."),
        ("`percentile` / `quantile`", "Valor por debajo del cual cae el N% de los datos. `np.percentile(arr, 50)` = mediana. `np.percentile(arr, [25, 50, 75])` = cuartiles."),
    ],
    errores_comunes=[
        ("`M.sum(axis=0)` da resultado por columna y esperaba por fila", "Confusión clásica. **Regla**: `axis=0` reduce **filas** (resultado per-column). **Fix**: si querías por fila, usa `axis=1`. Memoriza: \"el axis que pasas desaparece\"."),
        ("`arr.mean()` da NaN aunque solo hay un par de NaN", "Cualquier NaN propaga. **Fix**: `np.nanmean(arr)` o filtra antes (`arr[~np.isnan(arr)]`)."),
        ("`np.argmax(matriz)` devuelve un solo número raro", "Sin `axis`, aplana el array primero y devuelve un índice **lineal**. **Fix**: `argmax(axis=0)` o `axis=1` para obtener índices por dimensión; o `np.unravel_index(argmax, shape)` para coordenadas."),
        ("`np.percentile([1,2,3,4], 50)` da `2.5` no `2`", "Interpolación lineal por default. Si quieres el valor exacto del dataset, usa `interpolation='nearest'` o `quantile` con `method='lower'`."),
        ("`cumsum` de floats acumula error de redondeo en arrays largos", "Sumas múltiples introducen error numérico. **Fix**: si necesitas precisión, `np.cumsum(arr, dtype=np.float64)` o usa pairwise summation (Kahan)."),
    ],
    faq=[
        ("¿`arr.sum()` o `np.sum(arr)`?",
         "Equivalentes. Método del array (`.sum()`) es más legible en cadenas (`arr.clip(0).sum()`). Función (`np.sum`) acepta también listas (no solo ndarray)."),
        ("¿Cómo recuerdo qué axis colapsa cuál?",
         "**El axis que pasas es el que desaparece.** Si shape es `(3, 4)` y haces `sum(axis=0)`, queda `(4,)` — desapareció dim 0. Si `axis=1`, queda `(3,)`."),
        ("¿`std` usa N o N-1?",
         "Default `ddof=0` (divide por N — desviación poblacional). Para desviación muestral (N-1), `arr.std(ddof=1)`. Pandas y scipy.stats usan N-1 por default — cuidado al comparar."),
        ("¿`np.median` ignora NaN?",
         "No — usa `np.nanmedian`. Mismo patrón que `mean`/`nanmean`."),
        ("¿Hay una agregación 'top-3' built-in?",
         "No directa. Usa `np.partition(arr, -3)[-3:]` para los 3 mayores (más rápido que sort completo). Si necesitas ordenados, `.sort()` después."),
    ],
))


SPECS.append(ClassSpec(
    folder="017-numpy-broadcasting",
    number="017",
    title="NumPy: broadcasting",
    duration="75 min",
    source="VanderPlas, **cap. 2** § 2.5 *Computation on Arrays: Broadcasting*.",
    objetivo=(
        "Que el alumno **internalice las reglas de broadcasting** — el mecanismo por el que NumPy "
        "operó arrays de shapes distintos sin copiar datos. Es lo que hace que `M - M.mean(axis=0)` "
        "centrado por columna sea una línea, no un bucle anidado."
    ),
    resultados=[
        "**Recitar las 3 reglas** de broadcasting (alinea por la derecha, dim 1 estira, falla si no es 1 ni igual).",
        "**Predecir** la shape del resultado de una operación entre arrays de shapes distintos.",
        "**Centrar y escalar** matrices por fila/columna sin loops.",
        "**Usar `np.newaxis`** (o `None`) para promover un vector a matriz fila/columna.",
        "**Diagnosticar** un `ValueError: operands could not be broadcast together` leyendo las shapes.",
    ],
    temas=[
        ("Las 3 reglas", "Padding a la derecha, dim 1 estira, error si no coincide."),
        ("Vector + matriz", "Vector como fila o como columna."),
        ("`np.newaxis` / `None`", "Insertar eje de tamaño 1."),
        ("Caso canónico: centrar/escalar", "`X - X.mean(axis=0)` y `(X - μ) / σ`."),
        ("Outer product sin loop", "`a[:, None] * b[None, :]`."),
        ("ValueError común: \"operands could not be broadcast together\"", "Cómo leerlo."),
    ],
    dataset="Sintético: matriz de features 100×5 para estandarización. Sin descarga.",
    ejercicios=[
        "**Predice antes de ejecutar.** Para shapes `(3,)`, `(3,1)`, `(1,3)`, `(2,3,4)` × `(4,)`, predice la shape del resultado. Verifica.",
        "**Estandariza features.** Matriz 100×5 aleatoria. Resta media por columna y divide por std por columna en una línea.",
        "**Outer product.** Vectores `a=[1,2,3]`, `b=[10,20,30,40]`. Calcula la matriz outer (3×4) sin `np.outer`, solo broadcasting.",
        "**Distance matrix.** Dados 5 puntos 2D, construye matriz 5×5 de distancias euclídeas entre pares — sin `cdist`, solo broadcasting.",
        "**Diagnostica error.** Intenta `np.ones((3,4)) + np.ones((4,3))`. Lee el ValueError y explica.",
    ],
    homework=(
        "Notebook que: (a) predice shapes de 4 operaciones broadcasting y verifica; (b) estandariza "
        "una matriz feature por columna en una línea; (c) construye distance matrix de 100 puntos "
        "sin loop; (d) provoca y explica un error de broadcasting."
    ),
    homework_criterio="Las predicciones coinciden. Estandarización: media≈0, std≈1 por columna.",
    referencias=[
        "VanderPlas, **cap. 2** § 2.5 *Broadcasting*.",
        "[NumPy broadcasting docs](https://numpy.org/doc/stable/user/basics.broadcasting.html)",
    ],
    siguiente=("018-numpy-boolean-masks-y-fancy-indexing", "NumPy: boolean masks y fancy indexing"),
    cells=[
        Cell("md", "# Clase 017 — NumPy: broadcasting\n\n**Parte 0** · VanderPlas cap. 2 § 2.5.\n\n> 🎯 El mecanismo por el que NumPy opera arrays de shapes distintos sin copiar datos.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Las 3 reglas de broadcasting\n\n**Regla 1**: si los arrays tienen distinta cantidad de dimensiones, se **rellena con 1s a la izquierda** la shape del menor.\n\n**Regla 2**: si en alguna dim los tamaños difieren y **uno es 1**, ese se **estira** (virtualmente) al otro.\n\n**Regla 3**: si en alguna dim los tamaños difieren y **ninguno es 1**, **error**.\n\nEjemplos:\n```\n(3,4) + (4,)        → (3,4) + (1,4)  → (3,4) + (3,4)  ✅\n(3,4) + (3,1)        → ya alineadas   → (3,4) + (3,4)  ✅\n(3,4) + (3,)        → (3,4) + (1,3)  → (3,4) + (3,3)  ❌ regla 3\n```"),
        Cell("md", "## 2️⃣ Vector + matriz: el caso más común"),
        Cell("code", "M = np.array([[1, 2, 3], [4, 5, 6]])     # (2, 3)\nv = np.array([10, 20, 30])               # (3,)\nprint('M + v (vector como fila):')\nprint(M + v)\nprint()\n\nw = np.array([[100], [200]])             # (2, 1)\nprint('M + w (vector como columna):')\nprint(M + w)"),
        Cell("md", "## 3️⃣ `np.newaxis` (alias `None`) — promover un vector\n\nA veces necesitas decir explícitamente \"este vector es una fila\" o \"es una columna\":"),
        Cell("code", "v = np.array([1, 2, 3])    # (3,)\n\n# Como fila (1, 3)\nfila = v[np.newaxis, :]\nprint(f'fila shape: {fila.shape}')   # (1, 3)\n\n# Como columna (3, 1) — sintaxis equivalente con None\ncol = v[:, None]\nprint(f'col shape : {col.shape}')    # (3, 1)\n\n# Outer product: (3,1) * (1,4) → (3,4)\na = np.array([1, 2, 3])\nb = np.array([10, 20, 30, 40])\nouter = a[:, None] * b[None, :]\nprint(f'\\nouter shape: {outer.shape}')\nprint(outer)"),
        Cell("md", "## 4️⃣ Caso canónico — estandarizar features\n\nMatriz `X` con shape `(n_muestras, n_features)`. Queremos centrar y escalar por feature:\n\n```python\nμ = X.mean(axis=0)     # (n_features,)\nσ = X.std(axis=0)      # (n_features,)\nZ = (X - μ) / σ        # broadcasting: (n,d) - (d,) → (n,d)\n```"),
        Cell("code", "X = rng.normal(loc=[5, 10, 100], scale=[1, 2, 50], size=(100, 3))\nprint(f'X.shape  : {X.shape}')\nprint(f'media    : {X.mean(axis=0).round(2)}')\nprint(f'std      : {X.std(axis=0).round(2)}')\n\n# Estandariza en una línea\nZ = (X - X.mean(axis=0)) / X.std(axis=0)\nprint(f'\\nZ.mean   : {Z.mean(axis=0).round(4)}  (≈ 0)')\nprint(f'Z.std    : {Z.std(axis=0).round(4)}  (≈ 1)')"),
        Cell("md", "## 5️⃣ Distance matrix — sin loop\n\nDados `n` puntos en `d` dimensiones, queremos matriz `n×n` con distancias euclídeas. Usando broadcasting:\n\n```python\ndiff = X[:, None, :] - X[None, :, :]    # (n, 1, d) - (1, n, d) → (n, n, d)\ndist = np.sqrt((diff ** 2).sum(axis=2)) # (n, n)\n```"),
        Cell("code", "puntos = rng.normal(0, 1, (5, 2))   # 5 puntos 2D\ndiff = puntos[:, None, :] - puntos[None, :, :]\nprint(f'diff.shape: {diff.shape}')   # (5, 5, 2)\ndist = np.sqrt((diff ** 2).sum(axis=2))\nprint(f'\\ndist matrix (5x5):')\nprint(dist.round(2))\nprint(f'\\ndiagonal (cada punto consigo): {np.diag(dist)}  (≈ 0)')"),
        Cell("md", "## 6️⃣ Cuando broadcasting falla\n\nEl error típico:\n\n```\nValueError: operands could not be broadcast together with shapes (3,4) (4,3)\n```\n\n**Cómo leerlo**:\n1. Alinea las shapes a la derecha.\n2. En cada columna alineada, debe haber `==` o uno `1`.\n3. Si no, falla.\n\nPara `(3,4)` y `(4,3)`:\n```\n(3, 4)\n(4, 3)\n```\nColumna derecha: 4 vs 3 → distintos y ninguno es 1 → falla."),
        Cell("code", "try:\n    np.ones((3, 4)) + np.ones((4, 3))\nexcept ValueError as e:\n    print(f'ValueError: {e}')\n    print('Lo correcto: transponer uno, o asegurar dims compatibles.')\n    print(f'Con transpose: {(np.ones((3,4)) + np.ones((4,3)).T).shape}')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé las 3 reglas de broadcasting de memoria\n- [ ] Predigo la shape del resultado antes de ejecutar\n- [ ] Estandarizo una matriz por columna en una línea\n- [ ] Uso `[:, None]` para promover a columna\n- [ ] Leo y diagnostico ValueError de broadcasting"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Predicción de shapes, estandarización, distance matrix sin loop, diagnóstico de error."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 2 § 2.5\n- [Broadcasting docs](https://numpy.org/doc/stable/user/basics.broadcasting.html)\n\n➡️ **Siguiente:** [018 — Boolean masks y fancy indexing](../018-numpy-boolean-masks-y-fancy-indexing/README.md)"),
    ],
    definiciones=[
        ("Broadcasting", "Mecanismo por el que NumPy opera arrays de shapes distintos **sin copiar memoria**, estirando virtualmente las dimensiones de tamaño 1. Lo que hace posible `X - X.mean(axis=0)` (centrado por columna) en una línea sin loops."),
        ("Regla 1 — padding por la izquierda", "Si los arrays tienen distinta cantidad de dimensiones, la shape del menor se rellena con `1`s a la izquierda. `(4,)` operado con `(3, 4)` se trata como `(1, 4)` vs `(3, 4)`."),
        ("Regla 2 — estirar dim 1", "En cada dimensión donde los tamaños difieren, si uno es `1` se estira al otro. `(3, 1)` y `(3, 4)` → ambos `(3, 4)` (la primera se estira en eje 1)."),
        ("Regla 3 — fallo", "Si en alguna dimensión los tamaños son distintos y **ninguno es 1**, lanza `ValueError: operands could not be broadcast together`. No hay forma de inferir qué hacer."),
        ("`np.newaxis` (alias `None`)", "Inserta una dimensión de tamaño 1 donde lo pongas. `v[:, None]` convierte vector `(3,)` en columna `(3, 1)`. Crítico para forzar broadcasting en la dirección correcta."),
        ("Outer product vía broadcasting", "`a[:, None] * b[None, :]` produce matriz `(len(a), len(b))` con todos los productos par a par — equivalente a `np.outer(a, b)` pero usando broadcasting puro."),
    ],
    errores_comunes=[
        ("`ValueError: operands could not be broadcast together with shapes (3,4) (4,3)`", "Las shapes alineadas por la derecha no son compatibles. **Fix**: lee el error literal, alinea shapes a la derecha mentalmente, transpone (`.T`) uno o ajusta con `newaxis`."),
        ("Resté `M.mean(axis=0)` y los promedios quedaron MAL", "`mean(axis=0)` devuelve shape `(n_cols,)` — se broadcastea como FILA. Si querías restar por fila, usa `M.mean(axis=1)[:, None]` para que se broadcastee como COLUMNA."),
        ("`a + b` con shapes `(3,)` y `(3,)` da escalar (suma punto)", "**No** — da array `(3,)` elementwise. Producto punto es `np.dot(a, b)` o `a @ b`. Confundir esto es el bug #1 al empezar."),
        ("Memoria explota en una operación 'inocente'", "`X[:, None, :] - X[None, :, :]` produce array `(N, N, D)`. Si N=10000, son 100M × D elementos. **Fix**: usa `scipy.spatial.distance.cdist` o procesa por chunks."),
        ("`a[None] + b` no se broadcastea como espero", "`a[None]` añade dim al inicio. Quizás querías `a[:, None]` (al medio) o `a[None, :]` (explícito). Usa `print(arr.shape)` siempre antes de operar."),
    ],
    faq=[
        ("¿Cómo predigo la shape del resultado?",
         "(1) Alinea las shapes por la derecha. (2) En cada columna alineada: si son iguales o uno es 1, OK; si no, error. (3) Resultado: por dimensión, toma el `max` de las dos."),
        ("¿Broadcasting copia memoria?",
         "**No** — es virtual. NumPy itera con strides 0 en las dims estiradas. Por eso es tan eficiente: cero alloc extra (excepto el array resultado)."),
        ("¿`X - X.mean(0)` o `X - X.mean(0, keepdims=True)`?",
         "Para 2D ambos funcionan (broadcasting alinea). En 3D+, `keepdims=True` preserva la dimensión como `1` y evita confusiones. Recomendado en general."),
        ("¿`np.newaxis` o `None`?",
         "Aliases — `arr[:, None]` y `arr[:, np.newaxis]` son idénticos. `None` es más conciso; muchos prefieren `np.newaxis` por explicitud."),
        ("¿Qué hago si broadcasting no me sirve?",
         "Operaciones que no se ajustan a las reglas: usa `np.einsum` (más expresivo), `np.tensordot`, o reshape explícito. Como último recurso, loop Python — pero busca librería específica antes."),
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
