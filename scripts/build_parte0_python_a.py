"""Classes 006-009 — Python core (tipos, comprehensions, funciones, excepciones)."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="006-python-tipos-estructuras-control-de-flujo",
    number="006",
    title="Python: tipos, estructuras, control de flujo",
    duration="120 min",
    source="*Python Tutorial* oficial (caps. 3-5) · *Fluent Python* (Ramalho, 2ª ed.) cap. 1.",
    objetivo=(
        "Refrescar (o instalar) los cimientos de Python que el resto del programa asume: tipos "
        "primitivos, las 4 estructuras built-in (list, tuple, set, dict), control de flujo "
        "(if/for/while), unpacking, truthiness y la diferencia entre mutables e inmutables — "
        "la fuente del 90% de bugs sutiles."
    ),
    resultados=[
        "**Diferenciar** tipos mutables (list, dict, set) vs inmutables (tuple, str, int, frozenset) y predecir el efecto en asignaciones.",
        "**Usar las 4 estructuras** eligiendo bien: list (orden + duplicados), tuple (inmutable, rápida), set (unicidad), dict (lookup O(1)).",
        "**Aplicar unpacking** en for, returns múltiples y `*args`/`**kwargs`.",
        "**Evaluar truthiness** correctamente (`[]`, `{}`, `0`, `''`, `None` son falsy; el resto es truthy).",
        "**Identificar el bug del default mutable** en funciones (`def f(x, lst=[])`) y por qué es trampa.",
    ],
    temas=[
        ("Mutables vs inmutables", "Define qué pasa con `a = b`."),
        ("list, tuple, set, dict — cuándo cada uno", "Complejidad y semántica distintas."),
        ("Iteración: for, enumerate, zip", "Idiomático > C-style."),
        ("Unpacking y starred expressions", "`a, *b, c = [1,2,3,4,5]`."),
        ("Truthiness y operadores `and`/`or`", "Evalúan al objeto, no al booleano."),
        ("Default mutables: el clásico", "`def f(x, lst=[])` comparte la lista entre llamadas."),
    ],
    dataset=(
        "Datos sintéticos pequeños generados en el notebook (lista de diccionarios simulando "
        "estudiantes). No requiere descarga."
    ),
    ejercicios=[
        "**Cuenta palabras.** Dado un texto, devuelve un `dict[str, int]` con frecuencias. Sin usar `Counter`.",
        "**Unique con orden.** Recibe `list[int]`, devuelve la lista de únicos manteniendo el orden de primera aparición.",
        "**Reproduce el bug del default mutable.** Escribe `def add(item, target=[])`, llámala 3 veces con `add('x')`. Observa. Explica por qué y arregla.",
        "**Top-K palabras.** Mismo texto del ejercicio 1, devuelve las 5 más frecuentes ordenadas por frecuencia descendente.",
        "**Grupos por inicial.** Dado `list[str]`, devuelve `dict[str, list[str]]` agrupando por primera letra (case-insensitive).",
    ],
    homework=(
        "Notebook `homework.ipynb` con las 5 funciones de los ejercicios, cada una con: (a) "
        "implementación, (b) 3 casos de prueba (incluyendo edge cases — lista vacía, string vacío), "
        "(c) docstring corto explicando complejidad."
    ),
    homework_criterio="Las 5 funciones pasan sus casos de prueba; los edge cases manejados sin excepción.",
    referencias=[
        "[Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)",
        "Ramalho, *Fluent Python* 2e — cap. 1 *The Python Data Model*.",
        "[Python Tutorial — Control flow](https://docs.python.org/3/tutorial/controlflow.html)",
    ],
    siguiente=("007-comprehensions-y-generadores", "Comprehensions y generadores"),
    cells=[
        Cell("md", "# Clase 006 — Python: tipos, estructuras, control de flujo\n\n**Parte 0** · Python Tutorial oficial + Ramalho cap. 1.\n\n> 🎯 Refrescar cimientos. Las 4 estructuras built-in, mutabilidad, unpacking, truthiness, default mutables.\n\n> ⏱️ ~120 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import sys\nfrom typing import Iterable\nprint('python:', sys.version.split()[0])"),
        Cell("md", "## 1️⃣ Tipos primitivos y mutabilidad\n\n| Tipo | Mutable | Hashable | Uso típico |\n|---|---|---|---|\n| `int`, `float`, `complex` | ❌ | ✅ | aritmética |\n| `bool` | ❌ | ✅ | flags |\n| `str` | ❌ | ✅ | texto |\n| `bytes` | ❌ | ✅ | binario |\n| `bytearray` | ✅ | ❌ | binario mutable |\n| `list` | ✅ | ❌ | secuencia ordenada |\n| `tuple` | ❌ | ✅ (si elementos hashables) | record, return múltiple |\n| `set`, `frozenset` | ✅/❌ | ❌/✅ | unicidad, operaciones de conjunto |\n| `dict` | ✅ | ❌ | mapping key→value, O(1) lookup |\n\n**Regla**: solo los **hashables** pueden ser claves de dict o elementos de set."),
        Cell("code", "# Demostrar mutabilidad: shared reference vs copy\na = [1, 2, 3]\nb = a            # MISMO objeto\nb.append(4)\nprint('a:', a)   # [1, 2, 3, 4]  ← cambió\n\nc = a.copy()     # NUEVO objeto\nc.append(99)\nprint('a:', a)   # sin cambio\nprint('c:', c)"),
        Cell("md", "## 2️⃣ Las 4 estructuras — cuándo cada una\n\n- **list** — orden importa, duplicados OK, append/pop por el final.\n- **tuple** — inmutable, hashable, ideal para *records* y returns múltiples.\n- **set** — unicidad y operaciones (unión, intersección, diferencia) en O(1).\n- **dict** — mapping key→value, lookup O(1), preserva orden de inserción (Python 3.7+)."),
        Cell("code", "# Comparativa práctica\nfrutas = ['manzana', 'pera', 'manzana', 'kiwi']\n\n# Unicidad rápida con set\nprint('únicas:', set(frutas))\n\n# Conteo con dict\nconteo = {}\nfor f in frutas:\n    conteo[f] = conteo.get(f, 0) + 1\nprint('conteo:', conteo)\n\n# Record con tuple (inmutable)\npunto = (3.5, 7.1)\nx, y = punto   # unpacking\nprint(f'x={x}, y={y}')"),
        Cell("md", "## 3️⃣ Unpacking — el superpoder olvidado\n\n```python\na, b, c = [1, 2, 3]              # básico\na, *rest = [1, 2, 3, 4]          # rest = [2, 3, 4]\n*init, last = [1, 2, 3, 4]       # init = [1, 2, 3], last = 4\nfor i, val in enumerate(['a','b','c']):\n    print(i, val)\nfor k, v in {'x': 1, 'y': 2}.items():\n    print(k, v)\n```"),
        Cell("code", "# Unpacking en returns y zip\ndef min_max(xs):\n    return min(xs), max(xs)\n\nlo, hi = min_max([5, 2, 9, 1, 7])\nprint(f'rango: [{lo}, {hi}]')\n\nnombres = ['Ana', 'Bob', 'Cris']\nedades  = [30, 25, 28]\nfor n, e in zip(nombres, edades):\n    print(f'{n} tiene {e} años')"),
        Cell("md", "## 4️⃣ Truthiness — qué es \"falso\"\n\nFalsy: `False`, `None`, `0`, `0.0`, `''`, `[]`, `{}`, `set()`, `range(0)`.\nTodo lo demás es truthy.\n\n**Idioma pythonico**: `if items:` en vez de `if len(items) > 0:`."),
        Cell("code", "for v in [0, '', [], {}, None, False, 'x', [0], {'a':1}]:\n    print(f'{repr(v):>15} → {\"truthy\" if v else \"falsy\"}')"),
        Cell("md", "## 5️⃣ ⚠️ El bug del default mutable\n\n```python\ndef add(item, target=[]):   # ← TRAMPA\n    target.append(item)\n    return target\n\nadd('a')   # ['a']\nadd('b')   # ['a', 'b']  ← ¡compartió la lista!\n```\n\n**Por qué**: el default se evalúa **una sola vez**, al definir la función. Esa lista vive entre llamadas.\n\n**Fix**: usa `None` como sentinel."),
        Cell("code", "# El bug en vivo\ndef add_bug(item, target=[]):\n    target.append(item)\n    return target\n\nprint(add_bug('a'))\nprint(add_bug('b'))   # ¡compartió!\nprint(add_bug('c'))\n\n# Fix\ndef add_ok(item, target=None):\n    if target is None:\n        target = []\n    target.append(item)\n    return target\n\nprint()\nprint(add_ok('a'))\nprint(add_ok('b'))   # cada llamada arranca limpio\nprint(add_ok('c'))"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé qué tipos son mutables y cuáles inmutables\n- [ ] Elijo bien entre list/tuple/set/dict por caso\n- [ ] Uso unpacking en for/return/llamadas\n- [ ] Conozco truthiness y escribo `if items:`\n- [ ] Nunca uso default mutable en funciones"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. 5 funciones (cuenta palabras, unique con orden, bug del default, top-K, agrupar por inicial) con casos de prueba."),
        Cell("md", "## 🔗 Referencias\n\n- [Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html)\n- Ramalho, *Fluent Python* 2e, cap. 1\n\n➡️ **Siguiente:** [007 — Comprehensions y generadores](../007-comprehensions-y-generadores/README.md)"),
    ],
    definiciones=[
        ("Mutable", "Objeto cuyo estado puede modificarse después de crearlo (`list`, `dict`, `set`, `bytearray`). Consecuencia: si dos variables apuntan al mismo objeto mutable, cambiar una cambia la otra (alias)."),
        ("Inmutable", "Objeto que NO se puede modificar; cualquier 'modificación' produce un objeto nuevo (`int`, `float`, `str`, `tuple`, `frozenset`). Característica clave: son **hashables** y pueden ser claves de dict o miembros de set."),
        ("Hashable", "Objeto con `__hash__` definido y constante durante su vida. Los inmutables built-in son hashables; las listas y dicts NO lo son. Es lo que permite el O(1) lookup de set/dict."),
        ("Unpacking", "Sintaxis para asignar múltiples variables desde un iterable (`a, b = (1, 2)` o `a, *resto = [1, 2, 3, 4]`). El `*` captura el resto en una lista. Funciona en for, return, llamadas a funciones (`f(*lista)`, `g(**dict)`)."),
        ("Truthy / Falsy", "Cómo evalúa Python un objeto en contexto booleano (`if x:`). Falsy: `False`, `None`, `0`, `0.0`, `''`, `[]`, `{}`, `set()`. Truthy: todo lo demás (incluso `' '` con espacio, `[0]`, `{None: None}`)."),
    ],
    errores_comunes=[
        ("`TypeError: unhashable type: 'list'`", "Intentaste usar una lista como clave de dict o miembro de set. **Fix**: usa una tupla en su lugar (es inmutable y hashable). `{[1,2]: 'x'}` ❌ → `{(1,2): 'x'}` ✅."),
        ("Modifiqué una lista y otra variable también cambió", "Las dos apuntan al mismo objeto (alias). **Fix**: si querías una copia, usa `list_b = list_a.copy()` o `list_b = list_a[:]` o `list_b = list(list_a)`."),
        ("Función con default `=[]` comparte la lista entre llamadas", "El default se evalúa **una vez** al definir la función. **Fix**: `def f(x, lst=None): lst = lst or []` (o `lst = [] if lst is None else lst`)."),
        ("`KeyError` al acceder a dict que no tiene la key", "`d['x']` lanza KeyError si no existe. **Fix**: usa `d.get('x', default)` o `from collections import defaultdict; d = defaultdict(int)`."),
        ("`if items != None:` en vez de `if items is not None:`", "Para singletons (`None`, `True`, `False`) usa siempre `is` / `is not` — más rápido y semánticamente correcto. `==` puede engañar si el objeto override `__eq__`."),
    ],
    faq=[
        ("¿Cuándo tupla y cuándo lista?",
         "**Tupla** para records heterogéneos de tamaño fijo (`punto = (3.5, 7.1)`, `(nombre, edad)`). **Lista** para colecciones homogéneas que crecen (`temperaturas = [22.1, 22.5, ...]`). Tupla además sirve como clave de dict; lista no."),
        ("¿Set o dict para chequear pertenencia?",
         "Ambos son O(1). Set si solo necesitas saber si está. Dict si además necesitas asociar valor. Una `list` para esto es O(n) — usa set/dict si haces `if x in coleccion` con N grande."),
        ("¿`copy()` me da una copia completa? ¿Y con listas anidadas?",
         "`.copy()` es **shallow**: copia el contenedor pero comparte las referencias internas. Para anidamiento, `import copy; copy.deepcopy(x)` — más lento pero independiente."),
        ("¿Por qué `0.1 + 0.2 != 0.3`?",
         "Floats son IEEE 754 binarios; `0.1` y `0.2` no tienen representación exacta. **Fix**: para igualdad usa `math.isclose(a, b)`. Para precisión decimal financiera, `from decimal import Decimal`."),
        ("¿Qué pasa con dict si insertas la misma clave dos veces?",
         "El segundo valor sobrescribe al primero. El orden de inserción se preserva (Python 3.7+), así que `list(d)` da las keys en el orden en que se insertaron por primera vez."),
    ],
))


SPECS.append(ClassSpec(
    folder="007-comprehensions-y-generadores",
    number="007",
    title="Comprehensions y generadores",
    duration="90 min",
    source="Ramalho, *Fluent Python* 2e — caps. 2 (Sequences) y 17 (Iterators, Generators, Coroutines).",
    objetivo=(
        "Que el alumno escriba código Python idiomático: list/dict/set comprehensions en vez de "
        "for+append, generadores cuando el dataset no cabe en memoria, y entienda la diferencia "
        "fundamental entre **construir una lista** y **producir un iterable perezoso**."
    ),
    resultados=[
        "**Convertir** loops `for+append` a list/dict/set comprehensions sin perder legibilidad.",
        "**Usar generadores** (`yield` y generator expressions) para procesar datos que no caben en RAM.",
        "**Distinguir** `[x for x in xs]` (lista) vs `(x for x in xs)` (generador): memoria y consumo.",
        "**Encadenar** generadores con `itertools` (`chain`, `islice`, `takewhile`, `groupby`).",
        "**Identificar** cuándo NO usar comprehension (lógica compleja, side effects, debug difícil).",
    ],
    temas=[
        ("List comprehension: `[expr for x in xs if cond]`", "Idiomático, eficiente, legible si es simple."),
        ("Dict/set comprehensions", "Mismo patrón, otra estructura."),
        ("Generator expressions: `(expr for x in xs)`", "Perezoso, memoria O(1)."),
        ("Funciones generadoras con `yield`", "Reescribe procesos como streams."),
        ("`itertools` — la caja de herramientas", "`chain`, `islice`, `groupby`, `accumulate`, `combinations`."),
        ("Comprehension vs loop: cuándo NO", "Lógica >2 líneas, side effects, debug."),
    ],
    dataset=(
        "Datos sintéticos: rango grande de números (1M elementos) para mostrar diferencia "
        "memoria lista vs generador. Sin descarga."
    ),
    ejercicios=[
        "**De for a comprehension.** Toma 3 loops `for+append` (cuadrados, filtra pares, mapea a strings) y conviértelos.",
        "**Generador de Fibonacci infinito.** Función con `yield` que produce Fibonacci. Úsala con `itertools.islice` para tomar los primeros 20.",
        "**Memoria: lista vs generador.** Mide RAM (con `tracemalloc`) de `sum([i*i for i in range(10_000_000)])` vs `sum(i*i for i in range(10_000_000))`. Reporta la diferencia.",
        "**Procesa CSV línea por línea.** Lee un archivo grande con `yield` línea por línea, filtra por una condición, cuenta sin cargar todo en memoria.",
        "**Pivot con dict comprehension.** Dada `list[tuple[str, int]]` (nombre, puntaje), construye `dict[str, list[int]]` agrupando puntajes por nombre.",
    ],
    homework=(
        "Notebook que: (1) reescribe 3 loops como comprehensions, (2) implementa generador "
        "Fibonacci con `islice`, (3) comparativa RAM lista vs generador con `tracemalloc` y "
        "tabla de resultados, (4) lee un CSV ≥10k filas con generador y filtra sin cargar entero."
    ),
    homework_criterio="La medición de RAM muestra >100× menos memoria con generador. CSV se procesa sin OOM.",
    referencias=[
        "Ramalho, *Fluent Python* 2e — caps. 2 y 17.",
        "[PEP 202 — List Comprehensions](https://peps.python.org/pep-0202/)",
        "[PEP 255 — Simple Generators](https://peps.python.org/pep-0255/)",
        "[`itertools` docs](https://docs.python.org/3/library/itertools.html)",
    ],
    siguiente=("008-funciones-args-kwargs-lambdas-closures", "Funciones: args, kwargs, lambdas, closures"),
    cells=[
        Cell("md", "# Clase 007 — Comprehensions y generadores\n\n**Parte 0** · Ramalho caps. 2 y 17.\n\n> 🎯 Escribir Python idiomático: comprehensions en vez de for+append; generadores para procesar lo que no cabe en RAM.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import sys, time, tracemalloc\nfrom itertools import chain, islice, groupby, accumulate, takewhile\nprint('python:', sys.version.split()[0])"),
        Cell("md", "## 1️⃣ List comprehension\n\nForma: `[expr for x in iterable if cond]`. Equivale a un `for+append+if`.\n\n```python\n# Idiomático\ncuadrados_pares = [x*x for x in range(10) if x % 2 == 0]\n\n# Equivalente verboso\nresult = []\nfor x in range(10):\n    if x % 2 == 0:\n        result.append(x*x)\n```"),
        Cell("code", "# Tres ejemplos canónicos\ncuadrados = [x*x for x in range(10)]\nprint('cuadrados:', cuadrados)\n\npares = [x for x in range(20) if x % 2 == 0]\nprint('pares:', pares)\n\nmatriz = [[i*j for j in range(4)] for i in range(4)]\nfor fila in matriz:\n    print(fila)"),
        Cell("md", "## 2️⃣ Dict y set comprehensions\n\nMismo patrón, distinta estructura:"),
        Cell("code", "# Dict comprehension\ncuadrados_dict = {x: x*x for x in range(5)}\nprint(cuadrados_dict)\n\n# Set comprehension (unicidad automática)\nletras = {c.lower() for c in 'Hola Mundo' if c.isalpha()}\nprint(letras)\n\n# Invertir un dict\noriginal = {'a': 1, 'b': 2, 'c': 3}\ninvertido = {v: k for k, v in original.items()}\nprint(invertido)"),
        Cell("md", "## 3️⃣ Generator expressions — lazy y O(1) memoria\n\nMismo paréntesis cambiados:\n\n```python\nlista     = [x*x for x in range(1_000_000)]    # construye toda la lista en memoria\ngenerador = (x*x for x in range(1_000_000))    # objeto perezoso, calcula on-demand\n\nsum(lista)      # ya está en RAM\nsum(generador)  # itera y descarta — RAM O(1)\n```"),
        Cell("code", "# Medición real de memoria\ndef midiendo(label, fn):\n    tracemalloc.start()\n    fn()\n    current, peak = tracemalloc.get_traced_memory()\n    tracemalloc.stop()\n    print(f'{label:20s} peak={peak/1024:.1f} KB')\n\nN = 1_000_000\nmidiendo('lista', lambda: sum([x*x for x in range(N)]))\nmidiendo('generador', lambda: sum(x*x for x in range(N)))"),
        Cell("md", "## 4️⃣ Funciones generadoras con `yield`\n\nCualquier función con `yield` se convierte en generador. Cada `yield` pausa y emite un valor; la siguiente iteración resume."),
        Cell("code", "def fibonacci():\n    \"\"\"Generador infinito de Fibonacci.\"\"\"\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\n\n# Toma los primeros 10 sin construir la lista infinita\nprimeros_10 = list(islice(fibonacci(), 10))\nprint(primeros_10)\n\n# Toma mientras sean < 1000\nfibs_chicos = list(takewhile(lambda x: x < 1000, fibonacci()))\nprint(fibs_chicos)"),
        Cell("md", "## 5️⃣ `itertools` — la navaja suiza\n\n- `chain(a, b, c)` — concatena iterables sin allocar lista\n- `islice(it, start, stop, step)` — slicing perezoso\n- `groupby(it, key)` — agrupa elementos *consecutivos* con misma key\n- `accumulate(it, fn)` — suma/producto acumulado\n- `combinations(it, r)` / `permutations(it, r)` — combinatoria"),
        Cell("code", "# Demo: groupby — atención, agrupa CONSECUTIVOS\ndatos = sorted([('a', 1), ('a', 2), ('b', 3), ('a', 4)], key=lambda x: x[0])\nfor k, grupo in groupby(datos, key=lambda x: x[0]):\n    print(k, list(grupo))\n\nprint()\n\n# accumulate: suma acumulada\nprint(list(accumulate([1, 2, 3, 4, 5])))  # [1, 3, 6, 10, 15]"),
        Cell("md", "## 6️⃣ Cuándo NO usar comprehension\n\n- Lógica de más de 2 líneas → for explícito\n- Side effects (`print`, mutación) → for explícito\n- Anidamiento triple → for explícito\n- Cuando el reviewer no la entiende → for explícito\n\nRegla: comprehension es **expresión**, no **statement**. Si necesitas múltiples statements, usa for."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé convertir `for+append` a comprehension\n- [ ] Distingo `[...]` (lista) de `(...)` (generador)\n- [ ] Sé escribir un generador con `yield`\n- [ ] Conozco `chain`, `islice`, `groupby` de itertools\n- [ ] Sé cuándo NO usar comprehension"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Reescribir 3 loops, generador Fibonacci, medir RAM lista vs generador, procesar CSV grande con generador."),
        Cell("md", "## 🔗 Referencias\n\n- Ramalho, *Fluent Python* 2e — caps. 2 y 17\n- [itertools docs](https://docs.python.org/3/library/itertools.html)\n\n➡️ **Siguiente:** [008 — Funciones: args, kwargs, lambdas, closures](../008-funciones-args-kwargs-lambdas-closures/README.md)"),
    ],
    definiciones=[
        ("List comprehension", "Expresión `[expr for x in iterable if cond]` que **construye una lista** completa en memoria. Equivalente idiomático a `for + append + if`. Más rápida y legible *si la expresión es simple*."),
        ("Generator expression", "Lo mismo pero con paréntesis `(expr for x in iterable if cond)`. Devuelve un **generador perezoso**: produce cada valor on-demand, memoria O(1). Solo puedes recorrerlo una vez."),
        ("Iterador", "Objeto con método `__next__()` que devuelve el siguiente valor o lanza `StopIteration`. Es lo que está *detrás* de un for. Características: lazy, single-pass, memoria O(1)."),
        ("Generador", "Función con `yield` (o generator expression) que produce un iterador. Cada `yield` pausa la función y emite un valor; al siguiente next() retoma desde ahí. Mantiene el estado local entre llamadas."),
        ("`itertools`", "Librería stdlib con bloques perezosos componibles: `chain` (concatena), `islice` (slicing perezoso), `groupby` (agrupa consecutivos), `accumulate` (sum/prod corridos), `takewhile`, `combinations`, `product`."),
    ],
    errores_comunes=[
        ("Iteré un generador y la segunda vez está vacío", "Los generadores son **single-pass**. Tras consumir, están agotados. **Fix**: convierte a lista (`list(gen)`) si necesitas recorrer más veces — pierdes memoria O(1)."),
        ("`MemoryError` al hacer `[expensive(x) for x in millones]`", "Construyes lista completa en RAM. **Fix**: usa generator expression `(expensive(x) for x in millones)` y consúmelo perezosamente con `sum()`, `next()`, `for`."),
        ("`itertools.groupby` me agrupa raro", "Solo agrupa **elementos consecutivos** con misma key. Si los datos no están ordenados por la key, primero `sorted(data, key=...)`."),
        ("Generator expression dentro de función falla con `'generator' object is not subscriptable`", "Estás haciendo `gen[0]` — generadores no son indexables. **Fix**: `next(gen)` para el primer valor, o `list(gen)[0]` si necesitas acceso aleatorio."),
        ("List comprehension con `if-else` no funciona como espero", "`if` al final filtra; `if-else` va al principio: `[x if x > 0 else 0 for x in nums]` (clip). NO `[x for x in nums if x > 0 else 0]` (syntax error)."),
    ],
    faq=[
        ("¿Cuándo comprehension y cuándo for clásico?",
         "Comprehension cuando es **una expresión** clara en 1 línea. For clásico cuando hay >2 statements, side effects (print, mutación), o la lógica es más legible explícita."),
        ("¿Generator expression o list?",
         "Generator si el resultado solo se consume una vez y N es grande (RAM importa). List si necesitas recorrer 2+ veces, indexar, o hacer `len()`. Truco: `sum(x*x for x in xs)` evita lista temporal vs `sum([x*x for x in xs])`."),
        ("¿Cuánto más rápido es vs un for tradicional?",
         "~10-30%, no mil veces más. La ganancia real es legibilidad. Si necesitas mil veces, no es comprehension lo que buscas — es numpy/vectorización (clase 015)."),
        ("¿Generador infinito (`while True: yield ...`) es buena idea?",
         "Sí, pero ojo: **nunca** lo conviertas a lista directo (`list(gen)`) — bucle infinito hasta OOM. Acopla con `itertools.islice(gen, N)` para truncar."),
        ("`yield from` vs `yield`?",
         "`yield from sub_iterable` delega: yieldea todos los valores del sub-iterable. Equivale a `for x in sub: yield x` pero más rápido y propaga `send()`/`throw()` correctamente. Útil para componer generadores."),
    ],
))


SPECS.append(ClassSpec(
    folder="008-funciones-args-kwargs-lambdas-closures",
    number="008",
    title="Funciones: args, kwargs, lambdas, closures",
    duration="90 min",
    source="Ramalho, *Fluent Python* 2e — cap. 7 (Functions as First-Class Objects), cap. 9 (Decorators and Closures).",
    objetivo=(
        "Que el alumno use funciones como ciudadanos de primera clase: pasarlas como argumento, "
        "retornarlas, escribir lambdas cuando aportan, y entender closures — la base de los "
        "decoradores que verán más adelante. Sin esto, el código pandas/sklearn parece magia."
    ),
    resultados=[
        "**Definir funciones** con argumentos posicionales, keyword-only, `*args` y `**kwargs`.",
        "**Pasar funciones como argumento** (callbacks: `sorted(xs, key=fn)`, `df.apply(fn)`).",
        "**Usar lambdas** donde son legibles (callbacks cortos) y evitarlas donde no (lógica).",
        "**Explicar y escribir closures** (función que captura variables del scope exterior).",
        "**Anticipar** la diferencia entre `*args` y `*, args` (keyword-only marker).",
    ],
    temas=[
        ("Argumentos: posicional, keyword, default", "Cuatro modos, una sintaxis."),
        ("`*args` y `**kwargs`", "Funciones que aceptan número variable."),
        ("Keyword-only con `*` separador", "`def f(a, *, b)` → b solo nombrado."),
        ("Funciones como objetos", "Asignables, pasables, retornables."),
        ("Lambdas: dónde sí y dónde no", "Callbacks cortos sí; lógica compleja no."),
        ("Closures: capturando scope", "Base mental de los decoradores."),
    ],
    dataset="Datos sintéticos pequeños (lista de dicts simulando ventas). Sin descarga.",
    ejercicios=[
        "**Función con todo.** Define `f(a, b=10, *args, c, **kwargs)`. Llámala de 3 formas distintas que sean válidas. Identifica qué llamadas son inválidas y por qué.",
        "**`sorted` con key.** Dada `list[dict]` de personas, ordena por edad (asc) y por nombre alfabético. Usa lambda primero, luego `operator.itemgetter`.",
        "**Closure contador.** Escribe `make_counter()` que retorna una función que cada vez que se llama incrementa y retorna un contador interno. ¿Por qué funciona?",
        "**Memoización manual.** Implementa un decorador `@memoize` usando closure + dict. Aplícalo a Fibonacci recursivo y mide el speedup con `%timeit`.",
        "**Compose.** Escribe `compose(f, g, h)` que retorna una función equivalente a `lambda x: f(g(h(x)))`.",
    ],
    homework=(
        "Notebook con: (a) implementación y demo de `make_counter` explicando con comentario por "
        "qué el contador persiste; (b) `@memoize` aplicado a Fibonacci recursivo con benchmark "
        "(N=35) antes/después; (c) ordenamiento de `list[dict]` por 2 criterios usando `itemgetter`."
    ),
    homework_criterio="`memoize` reduce Fibonacci(35) de segundos a milisegundos. Counter independiente entre instancias.",
    referencias=[
        "Ramalho, *Fluent Python* 2e — caps. 7 y 9.",
        "[Python docs — More on Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)",
        "[PEP 3102 — Keyword-Only Arguments](https://peps.python.org/pep-3102/)",
    ],
    siguiente=("009-manejo-de-excepciones-y-context-managers", "Manejo de excepciones y context managers"),
    cells=[
        Cell("md", "# Clase 008 — Funciones: args, kwargs, lambdas, closures\n\n**Parte 0** · Ramalho caps. 7 y 9.\n\n> 🎯 Funciones como first-class objects: callbacks, lambdas, closures — base mental de los decoradores.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "from operator import itemgetter, attrgetter\nimport time\nfrom functools import wraps"),
        Cell("md", "## 1️⃣ Argumentos: las 4 formas\n\n```python\ndef f(pos, kw='default', *args, kw_only, **kwargs):\n    ...\n```\n\n- `pos` — posicional o keyword\n- `kw='default'` — posicional o keyword con default\n- `*args` — captura posicionales restantes en tupla\n- `kw_only` — solo se puede pasar nombrado (tras `*args` o `*`)\n- `**kwargs` — captura keyword restantes en dict"),
        Cell("code", "def reportar(nombre, edad=0, *extras, ciudad, **meta):\n    print(f'nombre  : {nombre}')\n    print(f'edad    : {edad}')\n    print(f'extras  : {extras}')\n    print(f'ciudad  : {ciudad}')\n    print(f'meta    : {meta}')\n\nreportar('Ana', 30, 'lectora', 'pianista', ciudad='Madrid', rol='senior', equipo='ML')"),
        Cell("md", "## 2️⃣ Keyword-only con `*` separador\n\n```python\ndef plot(data, *, color='blue', linewidth=1):\n    ...  # color y linewidth SOLO se pueden pasar como kwargs\n\nplot(xs, color='red')      # ✅\nplot(xs, 'red')            # ❌ TypeError\n```\n\n**Por qué útil**: APIs claras. El lector ve `plot(data, color='red', linewidth=2)` y sabe qué hace cada argumento."),
        Cell("md", "## 3️⃣ Funciones como objetos\n\n```python\ndef saludo(nombre):\n    return f'Hola {nombre}'\n\nf = saludo            # asignable\nprint(f('Mundo'))\n\nfns = [str.upper, str.lower, str.title]  # lista de funciones\nfor fn in fns:\n    print(fn('Hola Mundo'))\n```\n\nEsto es lo que hace posible `df.apply(fn)`, `sorted(xs, key=fn)`, `map(fn, xs)`."),
        Cell("code", "# sorted con key — callback en acción\npersonas = [\n    {'nombre': 'Ana', 'edad': 30},\n    {'nombre': 'Bob', 'edad': 25},\n    {'nombre': 'Cris', 'edad': 28},\n]\n\n# Con lambda\npor_edad = sorted(personas, key=lambda p: p['edad'])\nprint('por edad:', por_edad)\n\n# Con itemgetter (más rápido, más legible para casos simples)\npor_nombre = sorted(personas, key=itemgetter('nombre'))\nprint('por nombre:', por_nombre)"),
        Cell("md", "## 4️⃣ Lambdas: dónde sí, dónde no\n\n**Sí**: callback corto, sin nombre relevante:\n```python\nsorted(xs, key=lambda p: p['edad'])\n```\n\n**No**: cuando merece nombre o tiene lógica:\n```python\n# ❌ ilegible\nfn = lambda x: (x*2, x+1) if x > 0 else (0, 0)\n\n# ✅ función con def\ndef escala_y_offset(x):\n    if x > 0:\n        return x*2, x+1\n    return 0, 0\n```"),
        Cell("md", "## 5️⃣ Closures — funciones que recuerdan\n\nUna **closure** es una función que captura variables del scope donde fue definida.\n\n```python\ndef make_counter():\n    count = 0                  # variable local de make_counter\n    def inner():\n        nonlocal count          # le decimos a inner que use la del exterior\n        count += 1\n        return count\n    return inner\n\ncontador = make_counter()\ncontador()  # 1\ncontador()  # 2\ncontador()  # 3\n```\n\n¿Por qué `count` no muere cuando `make_counter` retorna? Porque `inner` lo capturó y mantiene viva la referencia."),
        Cell("code", "def make_counter():\n    count = 0\n    def inner():\n        nonlocal count\n        count += 1\n        return count\n    return inner\n\nc1 = make_counter()\nc2 = make_counter()   # independiente de c1\n\nprint(c1(), c1(), c1())   # 1 2 3\nprint(c2())               # 1 — su propio count"),
        Cell("md", "## 6️⃣ Aplicación: decorador `@memoize` con closure + dict\n\nUn decorador es una función que recibe función y retorna función. Closure + dict = cache.\n\n```python\ndef memoize(fn):\n    cache = {}\n    @wraps(fn)\n    def wrapper(*args):\n        if args not in cache:\n            cache[args] = fn(*args)\n        return cache[args]\n    return wrapper\n```\n\nEl `cache` vive en el closure → cada llamada con los mismos args devuelve resultado precomputado."),
        Cell("code", "def memoize(fn):\n    cache = {}\n    @wraps(fn)\n    def wrapper(*args):\n        if args not in cache:\n            cache[args] = fn(*args)\n        return cache[args]\n    return wrapper\n\n# Fibonacci recursivo: lento sin memoize\ndef fib_lento(n):\n    if n < 2: return n\n    return fib_lento(n-1) + fib_lento(n-2)\n\n@memoize\ndef fib_rapido(n):\n    if n < 2: return n\n    return fib_rapido(n-1) + fib_rapido(n-2)\n\nN = 30\nt0 = time.perf_counter(); fib_lento(N); t1 = time.perf_counter()\nt2 = time.perf_counter(); fib_rapido(N); t3 = time.perf_counter()\nprint(f'lento  : {(t1-t0)*1000:.1f} ms')\nprint(f'rápido : {(t3-t2)*1000:.4f} ms')\nprint(f'speedup: {(t1-t0)/(t3-t2):.0f}x')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Distingo argumentos posicionales, kw, default, *args, **kwargs\n- [ ] Sé pasar una función como argumento (callback)\n- [ ] Uso lambda solo cuando es corto y claro\n- [ ] Entiendo qué es un closure y por qué funciona\n- [ ] Implementé un memoize y vi el speedup"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. `make_counter` explicado, `@memoize` con benchmark Fibonacci, sort por 2 criterios."),
        Cell("md", "## 🔗 Referencias\n\n- Ramalho, *Fluent Python* 2e — caps. 7, 9\n- [PEP 3102 keyword-only](https://peps.python.org/pep-3102/)\n\n➡️ **Siguiente:** [009 — Manejo de excepciones y context managers](../009-manejo-de-excepciones-y-context-managers/README.md)"),
    ],
    definiciones=[
        ("First-class object", "En Python, funciones son ciudadanos de primera clase: se asignan a variables (`f = saludar`), se pasan como argumento (`sorted(xs, key=f)`), se retornan de otras funciones. Esto habilita callbacks, decoradores y closures."),
        ("`*args` / `**kwargs`", "**`*args`** captura argumentos posicionales sobrantes en una **tupla**. **`**kwargs`** captura argumentos nombrados sobrantes en un **dict**. Convención: solo el `*` y `**` importan; los nombres `args`/`kwargs` son convención."),
        ("Keyword-only argument", "Argumento que solo puede pasarse nombrado: declarado después de `*` o `*args` en la signatura. `def f(a, *, b)` obliga a `f(1, b=2)`. Mejora legibilidad en APIs con muchos params."),
        ("Lambda", "Función anónima de UNA expresión: `lambda x: x*2`. Sin nombre, sin docstring, sin múltiples statements. Útil para callbacks cortos (`sorted(xs, key=lambda p: p['edad'])`). Si necesitas más, usa `def`."),
        ("Closure", "Función que **captura variables** del scope donde fue definida y las mantiene vivas aunque ese scope termine. Base mental de los decoradores. Para *modificar* la variable capturada, usa `nonlocal`."),
        ("Decorador", "Función que recibe función y retorna función (típicamente envuelta). Sintaxis: `@dec` antes de `def`. Implementado típicamente con closure + `@functools.wraps` para preservar metadata original."),
    ],
    errores_comunes=[
        ("`UnboundLocalError: local variable 'x' referenced before assignment`", "Asignaste a `x` dentro de la función → Python la trata como local; pero la usaste antes de asignar. **Fix**: si querías la del scope exterior, declara `nonlocal x` (o `global x`)."),
        ("`SyntaxError: positional argument follows keyword argument`", "Llamaste `f(a=1, 2)` — posicionales primero. **Fix**: `f(2, a=1)`."),
        ("`TypeError: f() got multiple values for argument 'x'`", "Pasaste `x` posicional Y nombrado: `f(5, x=10)`. **Fix**: elige uno."),
        ("Mi decorador rompe `help(funcion)`", "Sin `@functools.wraps(fn)`, el wrapper pierde `__name__`, `__doc__`. **Fix**: `from functools import wraps; @wraps(fn) def wrapper(...)`."),
        ("Lambda en loop captura el último valor", "`[lambda: i for i in range(3)]` — todas las lambdas devuelven `2` porque capturan `i` por referencia. **Fix**: `[lambda i=i: i for i in range(3)]` (default args evalúan en defin time)."),
    ],
    faq=[
        ("¿Cuándo `*args, **kwargs` y cuándo argumentos explícitos?",
         "Argumentos explícitos siempre que conozcas la signatura — el IDE te ayuda y el lector entiende. `*args, **kwargs` solo en wrappers genéricos (decoradores, factories) que deben aceptar cualquier llamada."),
        ("¿Lambda o def?",
         "Lambda solo si: (a) cabe en una expresión, (b) la usas inmediatamente (callback), (c) un nombre no aportaría. En todos los demás casos, `def` con nombre — más debuggeable, soporta docstring y type hints."),
        ("¿Closure es lo mismo que decorador?",
         "Decorador suele estar **implementado con** closure, pero closure ≠ decorador. Closure es cualquier función que captura su entorno; decorador es un patrón específico (función → función)."),
        ("¿Por qué necesito `nonlocal` en `make_counter`?",
         "Sin `nonlocal`, `count += 1` dentro de `inner` se interpretaría como variable local nueva y daría UnboundLocalError. `nonlocal` le dice: 'esa variable vive en el scope inmediato exterior, modifícala'."),
        ("¿Cuál es el costo de pasar funciones como argumento?",
         "Mínimo (es solo una referencia). Lo costoso es la **invocación** repetida en bucles tight (cada llamada Python tiene overhead). Para esto, NumPy/Cython/Numba."),
    ],
))


SPECS.append(ClassSpec(
    folder="009-manejo-de-excepciones-y-context-managers",
    number="009",
    title="Manejo de excepciones y context managers",
    duration="75 min",
    source="*Python Tutorial* cap. 8 (Errors and Exceptions) · Ramalho, *Fluent Python* 2e — cap. 18 (Context Managers).",
    objetivo=(
        "Que el alumno maneje excepciones con criterio (sin `except: pass`), construya jerarquías "
        "de excepciones propias cuando aporta, y use context managers (`with`) — tanto los "
        "built-in como propios con `@contextmanager` — para garantizar limpieza de recursos. "
        "Sin esto, el código de carga de datos es una bomba de relojería."
    ),
    resultados=[
        "**Diferenciar** los 3 tipos de errores (Syntax, runtime exceptions, logical) y dónde se manejan.",
        "**Capturar** excepciones específicas (`except ValueError`, no `except:`) y propagar las que no sabes manejar.",
        "**Crear** una excepción propia heredando de la jerarquía estándar (`class DatasetCorruptoError(Exception)`).",
        "**Usar `with`** para archivos, sesiones HTTP, transacciones DB.",
        "**Escribir** un context manager propio con `@contextmanager` (timer, supress, change_dir).",
    ],
    temas=[
        ("Jerarquía de excepciones built-in", "`BaseException` → `Exception` → `ValueError`/`KeyError`/..."),
        ("`try/except/else/finally`", "Cada bloque tiene un rol específico."),
        ("Capturar específico, no genérico", "`except:` esconde bugs."),
        ("Excepciones propias", "Comunican intención en vez de cargar mensajes string."),
        ("Context managers: protocolo `__enter__`/`__exit__`", "Garantiza cleanup."),
        ("`@contextmanager` de `contextlib`", "Crear cms con función + `yield`."),
    ],
    dataset="Archivo temporal generado en el notebook. Sin descarga.",
    ejercicios=[
        "**Captura específica.** Escribe una función `parse_int_safe(s, default=0)` que use try/except solo para `ValueError`. Demuestra que no esconde otros errores (ej. `TypeError` si pasas un dict).",
        "**Excepción propia.** Define `class DatasetCorruptoError(Exception)` con un atributo `linea`. Lanzala desde una función `cargar_csv` cuando una línea no tenga el número correcto de columnas.",
        "**`with` para archivo.** Lee un archivo línea por línea contando palabras. Compara con la versión sin `with` (manual `open/close`) y muestra qué pasa si hay excepción a mitad.",
        "**Context manager propio: timer.** Con `@contextmanager`, escribe `with timer(\"carga\"):` que imprima cuánto duró el bloque.",
        "**Context manager: change_dir.** `with cd(\"/tmp\"):` cambia de directorio al entrar y vuelve al salir — incluso si hay excepción.",
    ],
    homework=(
        "Notebook con: (a) `parse_int_safe` con tests de los 3 casos (válido, inválido, otro tipo); "
        "(b) `DatasetCorruptoError` usada en una función `cargar_csv` que valida #columnas; "
        "(c) decorador-context manager `timer` aplicado a 2 operaciones; (d) `cd` context manager."
    ),
    homework_criterio="Excepciones se capturan solo donde sabes manejarlas. `timer` reporta segundos correctamente.",
    referencias=[
        "[Python Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)",
        "Ramalho, *Fluent Python* 2e — cap. 18 *Context Managers and else Blocks*.",
        "[`contextlib` docs](https://docs.python.org/3/library/contextlib.html)",
    ],
    siguiente=("010-oop-basico-dataclasses-herencia", "OOP básico, dataclasses, herencia"),
    cells=[
        Cell("md", "# Clase 009 — Excepciones y context managers\n\n**Parte 0** · Python Tutorial cap. 8 + Ramalho cap. 18.\n\n> 🎯 Manejo riguroso de errores y garantía de cleanup con `with`.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import os, time, tempfile\nfrom contextlib import contextmanager\nfrom pathlib import Path"),
        Cell("md", "## 1️⃣ Jerarquía de excepciones\n\n```\nBaseException\n├── SystemExit          ← sys.exit()\n├── KeyboardInterrupt   ← Ctrl+C\n└── Exception           ← captura esto, no BaseException\n    ├── ArithmeticError\n    │   └── ZeroDivisionError\n    ├── LookupError\n    │   ├── KeyError\n    │   └── IndexError\n    ├── ValueError\n    ├── TypeError\n    ├── OSError\n    │   └── FileNotFoundError\n    └── ...\n```\n\nCaptura `Exception` o más específico. **NUNCA** captures `BaseException` o uses `except:` solo."),
        Cell("md", "## 2️⃣ `try/except/else/finally`\n\n```python\ntry:\n    valor = riesgoso()\nexcept ValueError as e:\n    log(f'valor inválido: {e}')\n    valor = None\nelse:\n    # Solo si try NO lanzó excepción\n    log('OK')\nfinally:\n    # Siempre, lanzó o no\n    cleanup()\n```\n\n- `try` — código que puede fallar\n- `except` — manejo específico\n- `else` — éxito (raro, pero útil)\n- `finally` — cleanup garantizado (lo que hace `with` automático)"),
        Cell("code", "def parse_int_safe(s, default=0):\n    \"\"\"Convierte a int; default si no es parseable. Otros errores propagan.\"\"\"\n    try:\n        return int(s)\n    except ValueError:\n        return default\n\nprint(parse_int_safe('42'))          # 42\nprint(parse_int_safe('foo'))         # 0\nprint(parse_int_safe('3.14'))        # 0\ntry:\n    parse_int_safe({'a': 1})         # TypeError no es ValueError → propaga\nexcept TypeError as e:\n    print(f'TypeError correcto: {e}')"),
        Cell("md", "## 3️⃣ Capturar específico — por qué\n\n```python\n# ❌ TRAMPA: esconde TODO error, hasta tipo y nombre\ntry:\n    valor = parse(linea)\nexcept:\n    valor = None   # bug silencioso\n\n# ✅ CORRECTO: solo el error que sabes manejar\ntry:\n    valor = parse(linea)\nexcept ValueError as e:\n    log(f'línea inválida {idx}: {e}')\n    valor = None\n```\n\nUn `except:` puede ocultar un `KeyboardInterrupt`, un `NameError` (typo) o un `MemoryError`. Casi nunca es lo que quieres."),
        Cell("md", "## 4️⃣ Excepciones propias\n\nLas excepciones son **comunicación tipada**. En vez de:\n\n```python\nraise Exception('CSV corrupto en línea 42')\n```\n\nDefine tu tipo:\n\n```python\nclass DatasetCorruptoError(Exception):\n    def __init__(self, mensaje, linea):\n        super().__init__(mensaje)\n        self.linea = linea\n\ntry:\n    cargar(path)\nexcept DatasetCorruptoError as e:\n    log(f'línea {e.linea}: {e}')   # ahora caller puede ACTUAR\n```"),
        Cell("code", "class DatasetCorruptoError(Exception):\n    def __init__(self, mensaje, linea):\n        super().__init__(mensaje)\n        self.linea = linea\n\ndef cargar_csv_estricto(lineas, n_cols):\n    for i, linea in enumerate(lineas, start=1):\n        cols = linea.split(',')\n        if len(cols) != n_cols:\n            raise DatasetCorruptoError(f'esperaba {n_cols} cols, vino {len(cols)}', linea=i)\n        yield cols\n\ndatos = ['a,b,c', 'd,e,f', 'g,h']   # última línea corrupta\ntry:\n    list(cargar_csv_estricto(datos, n_cols=3))\nexcept DatasetCorruptoError as e:\n    print(f'Error línea {e.linea}: {e}')"),
        Cell("md", "## 5️⃣ Context managers — `with`\n\n```python\n# Sin with: si parse() falla, el archivo queda abierto\nf = open('data.csv')\ndatos = parse(f)\nf.close()\n\n# Con with: cleanup garantizado, incluso si parse() lanza\nwith open('data.csv') as f:\n    datos = parse(f)\n# aquí f ya está cerrado\n```\n\nProtocolo: el objeto debe tener `__enter__` (entrada) y `__exit__` (salida). `__exit__` recibe info de la excepción si la hubo."),
        Cell("code", "# Demo: with garantiza close incluso con excepción\ntmp = Path(tempfile.mkdtemp()) / 'demo.txt'\ntmp.write_text('linea1\\nlinea2\\nlinea3\\n')\n\nwith open(tmp) as f:\n    for linea in f:\n        print(linea.strip())\nprint('archivo cerrado:', f.closed)"),
        Cell("md", "## 6️⃣ Context manager propio con `@contextmanager`\n\nLa forma corta: una función con `yield`. Antes del yield = `__enter__`. Después = `__exit__`.\n\n```python\nfrom contextlib import contextmanager\n\n@contextmanager\ndef timer(label):\n    t0 = time.perf_counter()\n    yield                       # aquí corre el código del `with`\n    dt = time.perf_counter() - t0\n    print(f'{label}: {dt*1000:.1f} ms')\n\nwith timer('carga'):\n    time.sleep(0.1)\n```"),
        Cell("code", "@contextmanager\ndef timer(label):\n    t0 = time.perf_counter()\n    try:\n        yield\n    finally:\n        dt = time.perf_counter() - t0\n        print(f'{label}: {dt*1000:.1f} ms')\n\nwith timer('operación A'):\n    time.sleep(0.05)\n\nwith timer('operación B'):\n    sum(i*i for i in range(100_000))"),
        Cell("code", "# Context manager práctico: cambiar de directorio temporalmente\n@contextmanager\ndef cd(path):\n    prev = Path.cwd()\n    os.chdir(path)\n    try:\n        yield\n    finally:\n        os.chdir(prev)   # garantizado incluso si hay excepción\n\nprint('antes:', Path.cwd().name)\nwith cd(tempfile.gettempdir()):\n    print('dentro:', Path.cwd().name)\nprint('después:', Path.cwd().name)"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Capturo excepciones específicas, no `except:`\n- [ ] Sé crear una excepción propia con atributos\n- [ ] Uso `with` para archivos y otros recursos\n- [ ] Sé escribir un context manager con `@contextmanager`\n- [ ] Entiendo que `finally` garantiza cleanup"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. `parse_int_safe`, `DatasetCorruptoError`, `timer`, `cd` context manager."),
        Cell("md", "## 🔗 Referencias\n\n- [Python Tutorial — Errors](https://docs.python.org/3/tutorial/errors.html)\n- [contextlib](https://docs.python.org/3/library/contextlib.html)\n- Ramalho, *Fluent Python* 2e, cap. 18\n\n➡️ **Siguiente:** [010 — OOP básico, dataclasses, herencia](../010-oop-basico-dataclasses-herencia/README.md)"),
    ],
    definiciones=[
        ("Excepción", "Objeto que se 'lanza' (`raise`) cuando algo anómalo ocurre. Sube por el stack hasta que un `except` lo captura, o termina el programa. Todas heredan de `BaseException`; las que debes capturar heredan de `Exception`."),
        ("`try/except/else/finally`", "**`try`**: código riesgoso. **`except`**: maneja una excepción específica. **`else`**: corre si `try` no lanzó (raro pero útil). **`finally`**: cleanup garantizado, lanzó o no."),
        ("Jerarquía de excepciones", "`BaseException` → `SystemExit` / `KeyboardInterrupt` / `Exception` → `ValueError` / `TypeError` / `LookupError` (→ `KeyError`, `IndexError`) / `OSError` / `ArithmeticError` (→ `ZeroDivisionError`). Captura siempre la más específica que sepas manejar."),
        ("Excepción propia (custom)", "Subclase de `Exception` (o subclase específica). Permite tipificar errores de tu dominio (`class DatasetCorruptoError(Exception): ...`) en vez de strings. El caller puede `except DatasetCorruptoError` con precisión."),
        ("Context manager", "Objeto con `__enter__` y `__exit__` que se usa con `with`. Garantiza setup/teardown (abrir/cerrar archivo, conectar/desconectar BD, lock/unlock). El `__exit__` corre incluso si hay excepción."),
        ("`@contextmanager`", "Decorador de `contextlib` que convierte una función con `yield` en context manager. Pre-yield = `__enter__`, post-yield = `__exit__`. Mucho más corto que escribir la clase completa."),
    ],
    errores_comunes=[
        ("`except:` o `except Exception:` ciego esconde bugs", "Cualquier error queda silenciado (incluso typos `NameError`). **Fix**: captura el tipo específico (`except ValueError as e`). Si quieres loguear cualquiera, `except Exception as e: log.error(...); raise`."),
        ("`finally` con `return` traga la excepción", "Si `finally` ejecuta `return`, la excepción del `try` desaparece silenciosamente. **Fix**: NO uses `return` en `finally`; sólo cleanup."),
        ("`with open(f) as f, open(g) as g:` falla por sintaxis vieja", "Esa sintaxis requiere Python 3.10+. **Fix**: en versiones viejas usa `contextlib.ExitStack` o `with open(f) as f: with open(g) as g:` anidado."),
        ("Capturé `KeyError` pero el código sigue rompiéndose", "Tu `except` está más arriba del `try`, o el error proviene de otra línea. **Fix**: lee el traceback completo, busca el `KeyError` real y rodea solo esa línea con try."),
        ("Excepción dentro de generator no se captura como espero", "Las excepciones en generators son tricky; `except` rodea el `for`, no el `yield`. **Fix**: lee la sección \"Exceptions in generators\" del PEP 380, o reformula como función normal."),
    ],
    faq=[
        ("¿`except Exception` o `except`?",
         "Casi siempre `except Exception` — más explícito. `except:` desnudo captura también `KeyboardInterrupt` y `SystemExit`, lo cual rompe Ctrl+C y `sys.exit()`."),
        ("¿Cuándo creo una excepción propia?",
         "Cuando el caller necesita **diferenciar** este error de otros. `raise ValueError('CSV corrupto')` obliga al caller a parsear strings; `raise DatasetCorruptoError(linea=42)` le da un tipo y un atributo concreto."),
        ("¿`with` solo para archivos?",
         "No — para CUALQUIER recurso que necesite cleanup. Files (`open`), conexiones DB (`engine.connect()`), locks (`threading.Lock`), sesiones HTTP (`requests.Session`), transacciones (`db.atomic()`), timing (`with timer(...)`)."),
        ("¿Debo capturar y re-lanzar para añadir contexto?",
         "Sí, con `raise ExceptionNueva(...) from e` — preserva el stacktrace original como '`__cause__`'. El log muestra ambos errores en cadena."),
        ("¿`pass` en `except` es siempre malo?",
         "**Casi siempre sí.** Si tienes que silenciar, al menos `log.warning(...)`. Solo OK cuando la excepción es esperada (`except FileNotFoundError: pass` al limpiar archivos opcionales)."),
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
