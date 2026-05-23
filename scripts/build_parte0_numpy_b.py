"""Classes 018-021 — NumPy B: masks/fancy indexing, sort, linalg, random."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="018-numpy-boolean-masks-y-fancy-indexing",
    number="018",
    title="NumPy: boolean masks y fancy indexing",
    duration="75 min",
    source="VanderPlas, **cap. 2**, §§ 2.6–2.7 *Comparisons, Masks, and Boolean Logic* + *Fancy Indexing*.",
    objetivo=(
        "Que el alumno seleccione, filtre y modifique sub-arrays de tres formas: slicing (visto), "
        "máscaras booleanas (`arr[arr > 0]`) y fancy indexing (`arr[[0, 3, 5]]`). Saber cuál "
        "devuelve **vista** vs **copia** y cuándo cada uno es la herramienta correcta."
    ),
    resultados=[
        "**Filtrar** elementos con máscaras booleanas: `arr[arr > 0]`, `arr[(a > 0) & (a < 10)]`.",
        "**Combinar máscaras** con `&`, `|`, `~` — NO con `and`/`or` (no vectorizan).",
        "**Seleccionar por índices** con fancy indexing: `arr[[0, 3, 5]]` o `arr[idx_array]`.",
        "**Modificar in-place** con máscara: `arr[arr < 0] = 0` (clipping).",
        "**Diferenciar vista vs copia**: slicing es vista; fancy indexing y máscara son copia.",
    ],
    temas=[
        ("Comparaciones elementwise → arrays bool", "`arr > 0` no devuelve un bool, devuelve un array de bools."),
        ("`np.count_nonzero`, `np.sum` sobre bool", "Cuenta cuántos True."),
        ("Combinar máscaras con `&`, `|`, `~`", "Operadores bitwise — no `and`/`or`."),
        ("Fancy indexing con array de índices", "Selección no contigua."),
        ("Vista vs copia", "Slicing = vista; mask/fancy = copia."),
        ("`np.where(cond)` (sin alternativas)", "Devuelve índices donde se cumple."),
    ],
    dataset="Sintético: array de precipitación diaria (365 valores). Sin descarga.",
    ejercicios=[
        "**Cuenta días lluviosos.** Dado array de 365 días con precipitación (mm), cuenta cuántos tuvieron >5mm.",
        "**Estadísticos por máscara.** Calcula precipitación media solo en días lluviosos (>0mm).",
        "**AND/OR combinados.** Días entre 1 y 10 mm. Días <1 o >50 mm.",
        "**Clipping.** Reemplaza valores negativos por 0 in-place (`arr[arr < 0] = 0`).",
        "**Vista vs copia.** Demuestra con un experimento que `arr[:5]` modifica el original pero `arr[arr > 0]` no.",
    ],
    homework=(
        "Notebook con array sintético de 365 días de precipitación generado con seed. Calcula: "
        "(a) días lluviosos y su media, (b) días extremos (>50mm), (c) demo de vista vs copia, "
        "(d) clipping in-place, (e) índices del top 10 días más lluviosos con `argsort`."
    ),
    homework_criterio="Resultados reproducibles. Demo vista/copia muestra comportamiento opuesto.",
    referencias=[
        "VanderPlas, **cap. 2** §§ 2.6, 2.7.",
        "[NumPy indexing user guide](https://numpy.org/doc/stable/user/basics.indexing.html)",
    ],
    siguiente=("019-numpy-ordenamiento-y-busqueda", "NumPy: ordenamiento y búsqueda"),
    cells=[
        Cell("md", "# Clase 018 — Boolean masks y fancy indexing\n\n**Parte 0** · VanderPlas cap. 2 §§ 2.6-2.7.\n\n> 🎯 Filtrar, seleccionar y modificar sub-arrays. Vista vs copia.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ Comparaciones → array booleano\n\nUn comparador (`>`, `<`, `==`, `!=`) **no devuelve un bool sino un array de bools**:"),
        Cell("code", "arr = np.array([1, 5, 2, 8, 3, 7])\nmask = arr > 3\nprint('array:', arr)\nprint('mask :', mask)        # bool array, mismo shape\nprint('count:', mask.sum())  # cuenta True (los True valen 1)"),
        Cell("md", "## 2️⃣ Máscara booleana — filtrado\n\n`arr[mask]` devuelve solo los elementos donde la máscara es True:"),
        Cell("code", "# Lluvia diaria simulada (365 días)\nlluvia = rng.gamma(shape=1.5, scale=3, size=365)\n# Convierte 60% de los días en \"secos\" (0)\nlluvia[rng.random(365) < 0.6] = 0\n\nprint(f'total días     : {len(lluvia)}')\nprint(f'días lluviosos : {(lluvia > 0).sum()}')\nprint(f'días >5mm      : {(lluvia > 5).sum()}')\nprint(f'media (todos)  : {lluvia.mean():.2f} mm')\nprint(f'media (lluvi.) : {lluvia[lluvia > 0].mean():.2f} mm')"),
        Cell("md", "## 3️⃣ Combinar máscaras: `&`, `|`, `~`\n\n⚠️ **NUNCA uses `and`/`or` con arrays** — son escalares. Usa los **bitwise** `&`, `|`, `~` (con paréntesis por precedencia):"),
        Cell("code", "# Lluvia ligera: 1mm <= x <= 10mm\nligeros = lluvia[(lluvia >= 1) & (lluvia <= 10)]\nprint(f'días lluvia ligera (1-10mm): {len(ligeros)}')\n\n# Lluvia ausente o extrema\nraro = lluvia[(lluvia < 1) | (lluvia > 30)]\nprint(f'días sin lluvia o extremos : {len(raro)}')\n\n# Negación: días sin lluvia\nsecos = lluvia[~(lluvia > 0)]\nprint(f'días secos                  : {len(secos)}')"),
        Cell("md", "## 4️⃣ Fancy indexing — selección por índices\n\nPasas un **array de índices** en vez de un slice:"),
        Cell("code", "x = np.arange(10, 100, 10)\nprint('x:', x)\n\nidx = [0, 3, 5, 8]\nprint('x[idx]:', x[idx])    # selecciona esos índices\n\n# En matriz: idx por eje\nM = np.arange(20).reshape(4, 5)\nprint('\\nM:')\nprint(M)\nprint('\\nfilas 0 y 2, todas las columnas:')\nprint(M[[0, 2], :])\nprint('\\nfilas [0,1,2] con columnas [3,1,4] (pares):')\nprint(M[[0, 1, 2], [3, 1, 4]])   # M[0,3], M[1,1], M[2,4]"),
        Cell("md", "## 5️⃣ Modificación in-place — clipping\n\n```python\narr[arr < 0] = 0       # reemplaza negativos por 0\narr[mask] = nuevo_val  # actualización masiva\n```"),
        Cell("code", "# Ejemplo: clipping de valores extremos\nvalores = rng.normal(0, 5, 20).round(2)\nprint(f'originales: {valores}')\n\n# Clip a [-3, 3]\nvalores[valores < -3] = -3\nvalores[valores > 3] = 3\nprint(f'clipped   : {valores}')\n\n# Equivalente con np.clip\nvalores2 = rng.normal(0, 5, 20)\nnp.clip(valores2, -3, 3, out=valores2)"),
        Cell("md", "## 6️⃣ ⚠️ Vista vs copia\n\n- **Slicing** (`arr[:5]`, `arr[1:8:2]`) → **vista**. Modificarla modifica el original.\n- **Máscara booleana** (`arr[mask]`) → **copia**. Modificarla NO afecta al original.\n- **Fancy indexing** (`arr[[0,3,5]]`) → **copia**.\n\nEsto es fuente clásica de bugs."),
        Cell("code", "arr = np.arange(10)\nprint(f'original: {arr}')\n\n# Slicing: vista — modifica el original\nvista = arr[:5]\nvista[0] = 999\nprint(f'tras vista[0]=999: {arr}  ← cambió!')\n\n# Mask: copia — NO modifica\narr = np.arange(10)\nmasked = arr[arr > 3]\nmasked[0] = -1\nprint(f'tras masked[0]=-1: {arr}  ← sin cambios')"),
        Cell("md", "## 7️⃣ `np.where(cond)` sin alternativas — índices donde se cumple"),
        Cell("code", "x = np.array([5, 12, 3, 8, 20, 1])\nidx = np.where(x > 5)\nprint(f'índices donde >5: {idx}')   # tupla con array de índices\nprint(f'valores         : {x[idx]}')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Filtro con `arr[arr > 0]`\n- [ ] Combino con `&`, `|`, `~` (paréntesis)\n- [ ] Sé que mask/fancy = copia, slicing = vista\n- [ ] Modifico in-place con `arr[mask] = valor`\n- [ ] Uso `np.where(cond)` para obtener índices"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Análisis de precipitación con máscaras, fancy indexing y demo vista/copia."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 2 §§ 2.6-2.7\n- [Indexing](https://numpy.org/doc/stable/user/basics.indexing.html)\n\n➡️ **Siguiente:** [019 — Ordenamiento y búsqueda](../019-numpy-ordenamiento-y-busqueda/README.md)"),
    ],
    definiciones=[
        ("Boolean mask", "Array de bools del mismo shape que el original. `arr[mask]` extrae solo los elementos donde mask es True. Devuelve un nuevo array (copia, no vista)."),
        ("Fancy indexing", "Indexar con array de **enteros** (índices arbitrarios, posiblemente no contiguos). `arr[[0, 3, 5]]` selecciona esas 3 posiciones. Devuelve copia."),
        ("Vista (view) vs copia (copy)", "**Slicing** (`arr[:5]`) → vista (mismo storage, mutarla muta el original). **Mask / fancy** → copia (storage independiente). Fuente del 70% de los bugs sutiles."),
        ("Operadores bitwise vs lógicos", "Para combinar masks: `&`, `|`, `~` (bitwise, vectorizados, elementwise). **NO uses `and`, `or`, `not`** — son escalares Python y dan `ValueError: truth value of an array is ambiguous`."),
        ("`np.where(cond)` 1-arg", "Sin alternativas, devuelve **tupla de arrays de índices** donde se cumple la condición. Diferente a `np.where(cond, a, b)` (ternario)."),
    ],
    errores_comunes=[
        ("`ValueError: The truth value of an array with more than one element is ambiguous`", "Usaste `and`/`or`/`not` con arrays. **Fix**: `&`/`|`/`~` con paréntesis: `(a > 0) & (a < 10)` (los paréntesis son obligatorios por precedencia)."),
        ("Modifico `arr[mask]` y el original no cambia", "Mask devuelve **copia**. **Fix**: para modificar in-place, asigna a `arr[mask] = nuevo_valor` (no `arr[mask].do_something()`)."),
        ("`arr[idx1, idx2]` con fancy indexing me da algo raro", "Si `idx1` e `idx2` son arrays del mismo length, NumPy hace pair-wise: `arr[idx1[i], idx2[i]]` para cada i. Para 'todas las filas idx1 con todas las cols idx2', usa `arr[np.ix_(idx1, idx2)]` o `arr[idx1][:, idx2]`."),
        ("Slice modifica el original sin querer", "`subset = arr[:10]; subset[0] = 99` modifica `arr`. **Fix**: `subset = arr[:10].copy()` si querías independencia."),
        ("Mask con shape distinto al array", "Lanza `IndexError: boolean index did not match indexed array`. **Fix**: asegúrate que la mask tiene el mismo shape (`arr.shape == mask.shape`)."),
    ],
    faq=[
        ("¿Mask o fancy indexing?",
         "**Mask** cuando la selección viene de una condición sobre los valores (`arr[arr > 0]`). **Fancy** cuando ya tienes los índices específicos (de un `argsort`, por ejemplo, o de business logic)."),
        ("¿Cómo modifico múltiples elementos con mask?",
         "`arr[arr < 0] = 0` (clipping). Funciona para asignar escalar a todos los True, o array del mismo tamaño que la cantidad de Trues: `arr[arr < 0] = -arr[arr < 0]` (abs solo donde negativo)."),
        ("¿`arr[idx]` con `idx` como booleano o entero?",
         "NumPy distingue: bool array del mismo shape → mask; int array → fancy indexing. Lista Python de bools también funciona, pero ojo con `[0, 1, 0, 1]` que puede interpretarse como ints (índices 0 y 1) o bools — usa `np.array(...)` explícito si hay duda."),
        ("¿`np.where(cond)` o `np.nonzero(cond)`?",
         "Idénticos cuando `where` se llama con un solo argumento. `nonzero` es más explícito del intent (\"dónde NO es 0/False\")."),
        ("¿Cómo combino mask con `np.where` ternario?",
         "`np.where(cond, valor_si_true, valor_si_false)` — ternario vectorizado. La diferencia con `arr[cond] = X`: where construye array nuevo; mask + asignación modifica in-place."),
    ],
))


SPECS.append(ClassSpec(
    folder="019-numpy-ordenamiento-y-busqueda",
    number="019",
    title="NumPy: ordenamiento y búsqueda",
    duration="60 min",
    source="VanderPlas, **cap. 2** § 2.8 *Sorting Arrays* · NumPy sorting reference.",
    objetivo=(
        "Que el alumno ordene arrays con criterio: `sort` vs `argsort`, ordenamiento por eje, "
        "partial sort con `partition`, y búsqueda binaria con `searchsorted`. Útil para top-K, "
        "rankings, alineación de series."
    ),
    resultados=[
        "**Ordenar** con `np.sort(arr)` (devuelve copia) y `arr.sort()` (in-place).",
        "**Obtener índices del orden** con `argsort` — base de top-K y rankings.",
        "**Ordenar por eje** en matrices con `axis=0` o `axis=1`.",
        "**Top-K eficiente** con `np.partition` (no ordena completo, solo separa).",
        "**Búsqueda binaria** con `np.searchsorted` en arrays ordenados (O(log n)).",
    ],
    temas=[
        ("`np.sort` vs `arr.sort()`", "Copia vs in-place."),
        ("`argsort`: el truco del top-K", "Índices que ordenarían el array."),
        ("Ordenamiento por eje", "Por fila o por columna."),
        ("`np.partition` para top-K", "Más rápido que sort completo."),
        ("`np.searchsorted` — binaria O(log n)", "Inserción en array ordenado."),
        ("`np.unique`", "Únicos + opcionalmente cuentas."),
    ],
    dataset="Sintético: puntajes de 1M estudiantes. Sin descarga.",
    ejercicios=[
        "**Top-10.** Dado array de 1M puntajes, obtén los 10 más altos. Compara `np.sort()[-10:]` vs `np.partition`.",
        "**Ranking.** Con `argsort`, asigna a cada estudiante su ranking (1 = mejor).",
        "**Ordena matriz por columna.** Matriz 10×5; ordena cada columna por su valor.",
        "**Mediana por bisect.** Implementa una función que dado un valor `v` y un array ordenado, devuelve su posición percentil usando `searchsorted`.",
        "**`np.unique` con cuentas.** Dado array de categorías, obtén valores únicos y sus frecuencias.",
    ],
    homework=(
        "Notebook con array de 100k puntajes: (a) top-100 con `partition` y benchmark vs sort completo; "
        "(b) ranking con `argsort.argsort()`; (c) percentil de un valor dado con `searchsorted`; "
        "(d) `unique` con `return_counts` y barplot top-10 categorías."
    ),
    homework_criterio="`partition` >10× más rápido que sort completo para N=100k y K=100.",
    referencias=[
        "VanderPlas, **cap. 2** § 2.8.",
        "[NumPy sorting reference](https://numpy.org/doc/stable/reference/routines.sort.html)",
    ],
    siguiente=("020-numpy-algebra-lineal-con-numpy-linalg", "NumPy: álgebra lineal con numpy.linalg"),
    cells=[
        Cell("md", "# Clase 019 — Ordenamiento y búsqueda\n\n**Parte 0** · VanderPlas cap. 2 § 2.8.\n\n> 🎯 sort vs argsort, top-K con partition, búsqueda binaria con searchsorted.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport time\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ `np.sort` vs `arr.sort()`\n\n- `np.sort(arr)` → **devuelve copia** ordenada\n- `arr.sort()` → ordena **in-place**, devuelve None"),
        Cell("code", "arr = rng.integers(0, 100, 10)\nprint(f'original   : {arr}')\nprint(f'np.sort    : {np.sort(arr)}')\nprint(f'original   : {arr}  ← sin cambios')\n\narr.sort()\nprint(f'tras .sort(): {arr}  ← mutado in-place')"),
        Cell("md", "## 2️⃣ `argsort` — el truco del top-K\n\n`argsort` devuelve los **índices que ordenarían** el array. Aplicarlos al array original devuelve ordenado:\n\n```python\nidx = arr.argsort()\nordenado = arr[idx]\n```\n\nPara top-K (los K más grandes): `arr[arr.argsort()][-K:]`."),
        Cell("code", "puntajes = rng.integers(0, 1000, 20)\nprint(f'puntajes: {puntajes}')\n\nidx_orden = puntajes.argsort()\nprint(f'top-5    : {puntajes[idx_orden[-5:]]}')\nprint(f'bottom-5 : {puntajes[idx_orden[:5]]}')"),
        Cell("md", "## 3️⃣ Ranking — argsort de argsort\n\nPara obtener el **ranking** (posición 1..N de cada elemento):"),
        Cell("code", "ranking = puntajes.argsort().argsort() + 1   # +1 para 1-indexed\nfor p, r in zip(puntajes, ranking):\n    print(f'puntaje={p:4d}  ranking={r}')"),
        Cell("md", "## 4️⃣ Ordenamiento por eje en matrices"),
        Cell("code", "M = rng.integers(0, 100, (4, 5))\nprint('Original:')\nprint(M)\n\nprint('\\nOrdenado por filas (axis=1):')\nprint(np.sort(M, axis=1))\n\nprint('\\nOrdenado por columnas (axis=0):')\nprint(np.sort(M, axis=0))"),
        Cell("md", "## 5️⃣ `np.partition` — top-K más rápido\n\nSi solo quieres los K más chicos/grandes, **no necesitas ordenar todo el array**. `partition(arr, K)` deja los K menores en las primeras K posiciones (no necesariamente ordenados entre sí), y el resto después.\n\nComplejidad: O(n) vs O(n log n) del sort completo."),
        Cell("code", "N = 1_000_000\nK = 100\ndatos = rng.normal(0, 1, N)\n\n# Sort completo\nt0 = time.perf_counter()\ntop_sort = np.sort(datos)[-K:]\nt1 = time.perf_counter()\n\n# Partition\nt2 = time.perf_counter()\ntop_part = np.partition(datos, -K)[-K:]\ntop_part.sort()   # opcional: ordenar solo esos K\nt3 = time.perf_counter()\n\nprint(f'sort completo : {(t1-t0)*1000:.1f} ms')\nprint(f'partition     : {(t3-t2)*1000:.1f} ms')\nprint(f'speedup       : {(t1-t0)/(t3-t2):.1f}×')\nprint(f'mismo top?    : {np.array_equal(np.sort(top_sort), np.sort(top_part))}')"),
        Cell("md", "## 6️⃣ `np.searchsorted` — búsqueda binaria O(log n)\n\nEn un array ordenado, encuentra el índice donde insertar un valor para mantenerlo ordenado:"),
        Cell("code", "ordenado = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])\n\n# Dónde se insertaría 35\nprint(np.searchsorted(ordenado, 35))    # 3\n\n# Batch: múltiples valores\nprint(np.searchsorted(ordenado, [5, 35, 75, 100]))"),
        Cell("md", "**Uso: calcular percentil de un valor**:\n\n```python\nrank = np.searchsorted(arr_ordenado, valor)\npercentil = 100 * rank / len(arr_ordenado)\n```"),
        Cell("code", "# Percentil de un puntaje en una distribución\npuntajes = np.sort(rng.normal(70, 10, 10_000))\nmi_puntaje = 85\nrank = np.searchsorted(puntajes, mi_puntaje)\npercentil = 100 * rank / len(puntajes)\nprint(f'puntaje {mi_puntaje} → percentil {percentil:.1f}')"),
        Cell("md", "## 7️⃣ `np.unique` — únicos y cuentas"),
        Cell("code", "categorias = rng.choice(['A', 'B', 'C', 'D'], size=1000, p=[0.5, 0.3, 0.15, 0.05])\nvalores, cuentas = np.unique(categorias, return_counts=True)\nfor v, c in zip(valores, cuentas):\n    print(f'{v}: {c:4d}  ({100*c/len(categorias):.1f}%)')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Distingo `np.sort()` (copia) de `arr.sort()` (in-place)\n- [ ] Sé usar `argsort` para top-K y rankings\n- [ ] Ordeno matrices por axis\n- [ ] Uso `partition` cuando solo necesito top-K\n- [ ] Sé que `searchsorted` es O(log n)"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Top-100 con benchmark partition vs sort, ranking, percentil con searchsorted, unique."),
        Cell("md", "## 🔗 Referencias\n\n- VanderPlas cap. 2 § 2.8\n- [Sorting reference](https://numpy.org/doc/stable/reference/routines.sort.html)\n\n➡️ **Siguiente:** [020 — Álgebra lineal](../020-numpy-algebra-lineal-con-numpy-linalg/README.md)"),
    ],
    definiciones=[
        ("`np.sort` vs `arr.sort()`", "**`np.sort(arr)`** devuelve copia ordenada (no muta). **`arr.sort()`** ordena in-place y retorna None. Mismo patrón que `sorted(list)` vs `list.sort()`."),
        ("`argsort`", "Devuelve los **índices** que ordenarían el array. `idx = arr.argsort(); ordenado = arr[idx]`. Base de top-K, rankings, alineación entre arrays correlacionados."),
        ("`np.partition`", "Quick-select O(n): garantiza que los K menores quedan en las primeras K posiciones (no necesariamente ordenados entre sí), el resto después. Mucho más rápido que sort completo cuando solo necesitas top-K."),
        ("`np.searchsorted`", "Búsqueda binaria O(log n) en array ordenado. Devuelve el índice donde insertar un valor para mantener orden. Útil para calcular percentiles, bucketing."),
        ("`np.unique`", "Devuelve únicos ordenados. Con `return_counts=True` devuelve también las frecuencias — alternativa rápida a `Counter` para datos numéricos."),
    ],
    errores_comunes=[
        ("Ordeno con `arr.sort()` y la variable queda en `None`", "`sort()` es in-place — modifica `arr` y retorna `None`. **Fix**: `ordenado = np.sort(arr)` (con `np.sort`)."),
        ("Top-K con `sort()[-K:]` es lento para N grande, K chico", "Sort completo es O(N log N). **Fix**: `np.partition(arr, -K)[-K:]` es O(N). Acopla con `.sort()` si necesitas los K ordenados internamente."),
        ("`argsort` da resultado raro con matriz", "Sin `axis`, ordena cada fila/columna independiente según `axis=-1` por default. Para ordenar matriz completa por una columna, usa `arr[arr[:, col].argsort()]`."),
        ("`np.searchsorted` da índice fuera del array", "Si el valor es mayor que todos, devuelve `len(arr)`. Es el comportamiento correcto (\"insertar al final\"). **Fix**: clipea con `np.clip(idx, 0, len(arr)-1)` si vas a indexar."),
        ("`np.unique(arr_2d)` aplana el array", "Por default, `unique` trabaja sobre array aplanado. Para únicos por fila/columna: `unique(arr, axis=0)`."),
    ],
    faq=[
        ("¿Cuándo `argsort` y cuándo `sort`?",
         "Si solo necesitas los valores ordenados, `sort`. Si necesitas el orden para **aplicarlo a otros arrays correlacionados** (ej: ordenar `nombres` por `puntajes`), `argsort` te da los índices."),
        ("¿`partition` o `heapq.nlargest`?",
         "`partition` para arrays NumPy (vectorizado, C). `heapq.nlargest(K, lst)` para listas Python. Para K muy pequeño (3-5) sobre N grande, similares; partition gana en arrays grandes."),
        ("¿Cómo ordeno por múltiples claves (lexicográfico)?",
         "`np.lexsort([clave_secundaria, clave_principal])` — devuelve índices. Atención: el orden es **al revés** (último argumento = key primaria)."),
        ("¿`np.unique` preserva el orden de primera aparición?",
         "**No** — siempre ordena. Para preservar orden de aparición: `_, idx = np.unique(arr, return_index=True); arr[np.sort(idx)]`."),
        ("¿Existe equivalente a SQL `ORDER BY x DESC`?",
         "`arr[arr.argsort()][::-1]` o `arr[arr.argsort()[::-1]]`. NumPy no tiene flag `reverse=` como `sorted()` Python — invierte tú."),
    ],
))


SPECS.append(ClassSpec(
    folder="020-numpy-algebra-lineal-con-numpy-linalg",
    number="020",
    title="NumPy: álgebra lineal con numpy.linalg",
    duration="90 min",
    source="VanderPlas, **cap. 2** § 2.9 *Structured Arrays* (referencia) · *Numerical Linear Algebra* (Trefethen & Bau).",
    objetivo=(
        "Que el alumno opere con vectores y matrices al nivel necesario para entender ML: producto "
        "punto, multiplicación matricial, inversa, sistema de ecuaciones (`solve`), descomposiciones "
        "(SVD, eigen). Saber **cuándo no usar la inversa** (lentitud + inestabilidad numérica)."
    ),
    resultados=[
        "**Multiplicar** vectores y matrices con `@` (operador moderno) y `np.dot`.",
        "**Resolver** sistemas `Ax = b` con `np.linalg.solve` (NO con `inv(A) @ b`).",
        "**Calcular** norma, determinante, rango, traza.",
        "**Computar** SVD con `np.linalg.svd` y entender qué retorna.",
        "**Calcular eigenvalores/eigenvectores** con `np.linalg.eig` / `eigh` (simétrica).",
    ],
    temas=[
        ("`@` operador (PEP 465): multiplicación matricial", "Reemplaza `np.matmul`."),
        ("Producto punto vs producto matricial", "Vector·vector vs matriz·matriz."),
        ("Resolver sistemas: `solve` vs `inv`", "Por qué NUNCA usar `inv`."),
        ("Norma, det, rank, trace", "Diagnóstico estructural de matrices."),
        ("SVD — la factorización universal", "Base de PCA, regresión lineal, recomendadores."),
        ("Eigen", "Base de PCA conceptual."),
    ],
    dataset="Sintético: matrices y vectores para los ejercicios. Sin descarga.",
    ejercicios=[
        "**Producto punto.** Dados dos vectores 100-dim aleatorios, calcula `np.dot(a, b)` y verifica que coincide con `sum(a*b)`.",
        "**Multiplicación matricial.** `(50, 30) @ (30, 20)` → `(50, 20)`. Verifica shapes y un elemento manualmente.",
        "**Resuelve sistema.** Genera `A = (5,5)` aleatoria, `b = (5,)`, resuelve `Ax = b` con `solve`. Verifica `A @ x ≈ b`.",
        "**Inv vs solve benchmark.** Para `A (1000,1000)` y `b (1000,)`, mide tiempo de `inv(A) @ b` vs `solve(A, b)`. Reporta speedup.",
        "**SVD de matriz baja rank.** Crea `M = u @ v.T` (rank 1). Calcula SVD y observa que solo el primer valor singular es no-cero.",
    ],
    homework=(
        "Notebook que: (a) compara `inv(A) @ b` vs `solve(A, b)` en tiempo Y precisión "
        "(`np.allclose`); (b) implementa regresión lineal cerrada `β = (XᵀX)⁻¹ Xᵀy` y luego con "
        "`solve`; (c) calcula SVD de una matriz y verifica `M = U @ diag(s) @ Vt`; (d) eigen de "
        "matriz de covarianza."
    ),
    homework_criterio="`solve` más rápido y más preciso que `inv`. SVD reconstruye la matriz dentro de tolerancia.",
    referencias=[
        "VanderPlas cap. 2 (overview NumPy).",
        "[`numpy.linalg` reference](https://numpy.org/doc/stable/reference/routines.linalg.html)",
        "[PEP 465 — `@` operator](https://peps.python.org/pep-0465/)",
        "Trefethen & Bau, *Numerical Linear Algebra* (1997) — fondo matemático.",
    ],
    siguiente=("021-numpy-aleatoriedad-y-semillas", "NumPy: aleatoriedad y semillas"),
    cells=[
        Cell("md", "# Clase 020 — Álgebra lineal\n\n**Parte 0** · `numpy.linalg`.\n\n> 🎯 Operar con vectores y matrices al nivel necesario para ML. Por qué NUNCA usar `inv`.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport time\nrng = np.random.default_rng(42)"),
        Cell("md", "## 1️⃣ El operador `@` (PEP 465)\n\nDesde Python 3.5, `@` es el operador estándar para **multiplicación matricial** (no elementwise, que es `*`).\n\n```python\nC = A @ B           # multiplicación matricial\nC = A.dot(B)        # equivalente, sintaxis vieja\nC = np.matmul(A, B) # equivalente, función explícita\nC = A * B           # ¡elementwise! distinto\n```"),
        Cell("code", "A = np.array([[1, 2], [3, 4]])\nB = np.array([[5, 6], [7, 8]])\n\nprint('A @ B (matricial):')\nprint(A @ B)\nprint('\\nA * B (elementwise):')\nprint(A * B)"),
        Cell("md", "## 2️⃣ Producto punto vector·vector"),
        Cell("code", "a = rng.normal(0, 1, 100)\nb = rng.normal(0, 1, 100)\n\nprint(f'a @ b        : {a @ b:.4f}')\nprint(f'np.dot(a, b) : {np.dot(a, b):.4f}')\nprint(f'sum(a*b)     : {(a*b).sum():.4f}  ← lo mismo')"),
        Cell("md", "## 3️⃣ Resolver `Ax = b`: `solve` vs `inv`\n\n**REGLA**: para resolver `Ax = b`, usa `np.linalg.solve(A, b)`, **NUNCA** `np.linalg.inv(A) @ b`.\n\n**Por qué**:\n- `inv` calcula la inversa completa (O(n³) caro)\n- `solve` usa descomposición LU (O(n³) pero con constante menor)\n- `inv` es **numéricamente inestable** (amplifica errores)\n- `solve` no construye la inversa, evita ese error"),
        Cell("code", "N = 500\nA = rng.normal(0, 1, (N, N))\nb = rng.normal(0, 1, N)\n\nt0 = time.perf_counter(); x_inv = np.linalg.inv(A) @ b; t1 = time.perf_counter()\nt2 = time.perf_counter(); x_solve = np.linalg.solve(A, b); t3 = time.perf_counter()\n\nprint(f'inv(A) @ b : {(t1-t0)*1000:.1f} ms')\nprint(f'solve(A,b) : {(t3-t2)*1000:.1f} ms')\nprint(f'speedup    : {(t1-t0)/(t3-t2):.1f}×')\n\n# Precisión: residual ||Ax - b||\nprint(f'\\nresidual inv  : {np.linalg.norm(A @ x_inv - b):.2e}')\nprint(f'residual solve: {np.linalg.norm(A @ x_solve - b):.2e}')"),
        Cell("md", "## 4️⃣ Diagnóstico estructural\n\n```python\nnp.linalg.norm(v)         # norma L2\nnp.linalg.det(A)          # determinante (cuidado: 0 ⇒ singular)\nnp.linalg.matrix_rank(A)  # rango\nnp.trace(A)               # traza (suma diagonal)\nnp.linalg.cond(A)         # número de condición (estabilidad)\n```\n\n**`cond(A)` grande (>1e10) ⇒ matriz mal condicionada ⇒ `solve` perderá precisión**."),
        Cell("code", "v = np.array([3, 4])\nprint(f'norma L2 [3,4]: {np.linalg.norm(v)}  (= 5)')\n\nM = np.array([[2, 1], [1, 3]])\nprint(f'\\nM = {M.tolist()}')\nprint(f'det      : {np.linalg.det(M):.4f}')\nprint(f'rank     : {np.linalg.matrix_rank(M)}')\nprint(f'trace    : {np.trace(M)}')\nprint(f'cond     : {np.linalg.cond(M):.2f}')\n\n# Matriz singular\nS = np.array([[1, 2], [2, 4]])\nprint(f'\\nMatriz singular:')\nprint(f'det      : {np.linalg.det(S):.4f}')\nprint(f'rank     : {np.linalg.matrix_rank(S)}  (no es 2)')"),
        Cell("md", "## 5️⃣ SVD — la descomposición universal\n\n**Singular Value Decomposition**: cualquier matriz `M (m,n)` se descompone como:\n\n```\nM = U · Σ · Vᵀ\n```\n\n- `U (m, m)` — vectores singulares izquierdos (ortonormales)\n- `Σ (m, n)` — diagonal de **valores singulares** (decrecientes ≥ 0)\n- `Vᵀ (n, n)` — vectores singulares derechos (ortonormales)\n\n**Aplicaciones**: PCA, recomendadores (matriz factorization), compresión de imágenes, pseudo-inversa."),
        Cell("code", "M = rng.normal(0, 1, (6, 4))\nU, s, Vt = np.linalg.svd(M, full_matrices=False)\n\nprint(f'M.shape  : {M.shape}')\nprint(f'U.shape  : {U.shape}')\nprint(f's        : {s.round(3)}  ← valores singulares decrecientes')\nprint(f'Vt.shape : {Vt.shape}')\n\n# Reconstrucción: M = U @ diag(s) @ Vt\nM_reconstruido = U @ np.diag(s) @ Vt\nprint(f'\\nreconstrucción OK: {np.allclose(M, M_reconstruido)}')"),
        Cell("md", "## 6️⃣ Eigenvalores y eigenvectores\n\nPara matriz cuadrada `A`, `A v = λ v` donde `λ` es eigenvalor y `v` eigenvector.\n\n**Base conceptual de PCA**: los eigenvectores de la matriz de covarianza son las direcciones de máxima varianza."),
        Cell("code", "# Matriz de covarianza simulada (simétrica positiva semi-definida)\nX = rng.normal(0, 1, (100, 3))\nC = np.cov(X.T)   # (3, 3)\n\n# Para matrices simétricas, usa eigh (más rápido, garantiza eigenvalores reales)\neigvals, eigvecs = np.linalg.eigh(C)\nprint(f'eigvalues (asc): {eigvals.round(4)}')\nprint(f'\\neigvectors (columnas):')\nprint(eigvecs.round(3))\n\n# La varianza total = suma de eigenvalores\nprint(f'\\ntraza(C)        : {np.trace(C):.4f}')\nprint(f'sum(eigenvalues): {eigvals.sum():.4f}  ← igual')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Uso `@` para mult matricial, `*` para elementwise\n- [ ] NUNCA uso `inv(A) @ b`, siempre `solve(A, b)`\n- [ ] Sé qué retorna SVD y verifico la reconstrucción\n- [ ] Uso `eigh` para matrices simétricas\n- [ ] Conozco `norm`, `det`, `rank`, `cond`"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. inv vs solve benchmark, regresión lineal cerrada, SVD, eigen de covarianza."),
        Cell("md", "## 🔗 Referencias\n\n- [`numpy.linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html)\n- [PEP 465 — `@` operator](https://peps.python.org/pep-0465/)\n\n➡️ **Siguiente:** [021 — Aleatoriedad y semillas](../021-numpy-aleatoriedad-y-semillas/README.md)"),
    ],
    definiciones=[
        ("Operador `@`", "Multiplicación matricial (PEP 465). `A @ B` ≡ `np.matmul(A, B)` ≡ `A.dot(B)`. NO confundir con `*` (elementwise). Disponible Python 3.5+."),
        ("Producto punto vs producto matricial", "**Punto** (vector·vector → escalar): `a @ b` = `sum(a*b)`. **Matricial** (matriz @ matriz → matriz): regla \"fila por columna\". Shapes: `(m,n) @ (n,p) → (m,p)`."),
        ("`np.linalg.solve(A, b)`", "Resuelve `Ax = b` usando descomposición LU. **Siempre preferible a `inv(A) @ b`**: más rápido (no construye inversa), más estable numéricamente, menos memoria."),
        ("SVD (Singular Value Decomposition)", "Descomposición universal: `M = U·Σ·Vᵀ`. U y V son ortogonales; Σ diagonal con valores singulares decrecientes ≥ 0. Base de PCA, recomendadores (matrix factorization), compresión, pseudo-inversa."),
        ("Eigen (eigenvalues/eigenvectors)", "Para `A` cuadrada, `A v = λ v`. `eig` general; `eigh` para matrices simétricas (más rápido, garantiza eigenvalores reales). Base de PCA conceptual."),
        ("Número de condición (`cond`)", "Ratio entre el valor singular más grande y el más pequeño. Mide sensibilidad de la solución a perturbaciones. `cond > 1e10` ⇒ matriz mal condicionada, `solve` perderá precisión."),
    ],
    errores_comunes=[
        ("`A @ B` falla con `ValueError: shapes ... not aligned`", "Las dimensiones internas no coinciden: `(m,n) @ (k,p)` requiere `n == k`. **Fix**: revisa shapes, transpone si necesario (`A @ B.T`)."),
        ("Implementé `inv(A) @ b` y los resultados son raros", "`inv` es inestable numéricamente para matrices grandes/mal-condicionadas. **Fix**: usa `np.linalg.solve(A, b)` — más rápido y más preciso."),
        ("`np.linalg.solve` lanza `LinAlgError: Singular matrix`", "`det(A) ≈ 0` — el sistema no tiene solución única. **Fix**: si esperabas el caso, usa `np.linalg.lstsq(A, b)` (least squares para sistemas singulares/sobredeterminados)."),
        ("`A * B` da resultado raro y esperaba `A @ B`", "Operador `*` es elementwise (Hadamard product). **Fix**: `A @ B` para multiplicación matricial."),
        ("SVD devuelve `Vt` no `V`", "Por convención NumPy devuelve `V^T` (transpuesta), no `V`. Para reconstruir: `M = U @ diag(s) @ Vt`. Si necesitas `V`: `Vt.T`."),
    ],
    faq=[
        ("¿`@`, `np.matmul`, o `np.dot`?",
         "Para matriz×matriz son equivalentes — `@` es el más legible. `np.dot` tiene comportamiento distinto para arrays >2D (no broadcasting); `@` y `matmul` sí. Usa `@` siempre que puedas."),
        ("¿`eig` o `eigh`?",
         "**`eigh`** si la matriz es simétrica (covarianza, kernel matrices, métrica de distancias). Más rápido, garantiza eigenvalores reales. **`eig`** para matrices generales (no simétricas) — puede dar valores complejos."),
        ("¿Por qué `np.linalg.det` para chequear singularidad es mala idea?",
         "El determinante es 0 o no-0 sin gradiente útil — para matrices grandes, det puede ser tan chico/grande que cause underflow/overflow numérico. Mejor: `np.linalg.cond(A)` — si > 1e10, problemática."),
        ("¿Cuándo necesito BLAS/LAPACK?",
         "NumPy ya los usa por debajo (vía OpenBLAS o MKL). Si tu `np.linalg.solve` parece lento, instala MKL (`pip install mkl`) o usa la build de conda con `mkl`."),
        ("¿GPU para álgebra lineal?",
         "**CuPy** (drop-in replacement de NumPy con CUDA), **PyTorch tensors** (`.to('cuda')`), o **JAX**. Para matrices >1000×1000 la GPU vale la pena."),
    ],
))


SPECS.append(ClassSpec(
    folder="021-numpy-aleatoriedad-y-semillas",
    number="021",
    title="NumPy: aleatoriedad y semillas",
    duration="60 min",
    source="*Numerical Recipes* cap. 7 (Random Numbers) · NumPy `random.Generator` docs.",
    objetivo=(
        "Que el alumno genere números aleatorios **reproduciblemente** con el API moderno "
        "(`np.random.default_rng(seed)`), use las distribuciones más comunes (uniforme, normal, "
        "Bernoulli, Poisson, exponencial), y entienda por qué la reproducibilidad es no-negociable "
        "en ciencia de datos."
    ),
    resultados=[
        "**Crear un `Generator`** con `np.random.default_rng(seed)` y usarlo para reproducibilidad.",
        "**Generar muestras** de uniforme, normal, integers, binomial, Poisson, exponencial.",
        "**Permutar y muestrear** sin/con reemplazo con `permutation` y `choice`.",
        "**Reproducir** un experimento exactamente con el mismo seed.",
        "**Saber por qué** `np.random.seed()` (API legacy) es deprecated en favor de `Generator`.",
    ],
    temas=[
        ("`np.random.default_rng(seed)`", "El API moderno (Generator-based, PCG64)."),
        ("Distribuciones continuas: uniform, normal, exponential, gamma, beta", "Las más usadas en simulación."),
        ("Distribuciones discretas: integers, binomial, poisson", "Conteos y procesos."),
        ("`permutation` y `choice`", "Mezclar y muestrear."),
        ("Reproducibilidad: por qué importa", "Misma cosa con mismo seed."),
        ("Múltiples generadores independientes", "Evita interferencia entre experimentos."),
    ],
    dataset="Sintético: simulación Monte Carlo. Sin descarga.",
    ejercicios=[
        "**Reproducibilidad.** Crea 2 rngs con `seed=42`, genera 1000 normales con cada uno. Verifica que son idénticos.",
        "**Distribuciones.** Genera 10000 muestras de: uniforme [0,1], normal(5,2), exponential(λ=1/3), poisson(λ=4). Calcula media y std empírica y compara con teórica.",
        "**Monte Carlo de π.** Estima π lanzando puntos en un cuadrado 2×2 y contando cuántos caen dentro del círculo unitario. Compara con π real.",
        "**Bootstrap.** Dado un sample de 30 valores, estima la distribución de la media por bootstrap (1000 resamples con reemplazo).",
        "**Permutación.** Mezcla un array de 100 elementos con `permutation`. Verifica que es la misma cuando usas el mismo seed.",
    ],
    homework=(
        "Notebook con: (a) Monte Carlo de π con N=10k, 100k, 1M reportando error; (b) bootstrap de "
        "la media de un sample (95% CI vs CLT); (c) demo de reproducibilidad con dos rngs; "
        "(d) tabla comparando momento empírico vs teórico para 4 distribuciones."
    ),
    homework_criterio="MC converge a π. Bootstrap CI similar al CLT. Reproducibilidad exacta.",
    referencias=[
        "[NumPy `random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html)",
        "[NEP 19 — Random number generator policy](https://numpy.org/neps/nep-0019-rng-policy.html)",
        "Press et al., *Numerical Recipes* 3e — cap. 7 *Random Numbers*.",
    ],
    siguiente=("022-pandas-series-y-dataframe", "Pandas: Series y DataFrame"),
    cells=[
        Cell("md", "# Clase 021 — Aleatoriedad y semillas\n\n**Parte 0** · NumPy `random.Generator`.\n\n> 🎯 Aleatoriedad reproducible con el API moderno. Distribuciones, permutación, Monte Carlo.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import numpy as np\nimport math\nrng = np.random.default_rng(seed=42)"),
        Cell("md", "## 1️⃣ API moderno vs legacy\n\n```python\n# ❌ legacy (deprecated)\nnp.random.seed(42)\nnp.random.normal(0, 1, 100)\n\n# ✅ moderno (recomendado)\nrng = np.random.default_rng(seed=42)\nrng.normal(0, 1, 100)\n```\n\n**Ventajas del Generator**:\n- Algoritmo más rápido (PCG64 vs Mersenne Twister)\n- Múltiples generadores independientes (no estado global)\n- API más limpio y consistente\n- Mejor calidad estadística"),
        Cell("md", "## 2️⃣ Reproducibilidad\n\nMismo seed → exactamente los mismos números, siempre, en cualquier máquina:"),
        Cell("code", "rng_a = np.random.default_rng(seed=42)\nrng_b = np.random.default_rng(seed=42)\n\na = rng_a.normal(0, 1, 5)\nb = rng_b.normal(0, 1, 5)\nprint(f'a: {a}')\nprint(f'b: {b}')\nprint(f'iguales? {np.array_equal(a, b)}')"),
        Cell("md", "## 3️⃣ Distribuciones más usadas\n\n| Método | Distribución | Param típicos |\n|---|---|---|\n| `rng.random(n)` | Uniforme [0, 1) | — |\n| `rng.uniform(lo, hi, n)` | Uniforme [lo, hi) | lo, hi |\n| `rng.normal(μ, σ, n)` | Normal | media, std |\n| `rng.standard_normal(n)` | Normal(0,1) | — |\n| `rng.integers(lo, hi, n)` | Uniforme discreto [lo, hi) | lo, hi |\n| `rng.binomial(n, p, size)` | Binomial | n trials, p éxito |\n| `rng.poisson(λ, size)` | Poisson | tasa |\n| `rng.exponential(scale, size)` | Exponencial | scale = 1/λ |\n| `rng.gamma(shape, scale, size)` | Gamma | shape, scale |\n| `rng.beta(a, b, size)` | Beta | a, b |"),
        Cell("code", "N = 100_000\nrng = np.random.default_rng(42)\n\n# Comparar empírico vs teórico\nmuestras = {\n    'uniform(0,1)'    : (rng.random(N),           0.5, math.sqrt(1/12)),\n    'normal(5,2)'     : (rng.normal(5, 2, N),     5,   2),\n    'exponential(3)'  : (rng.exponential(3, N),   3,   3),\n    'poisson(4)'      : (rng.poisson(4, N),       4,   math.sqrt(4)),\n}\n\nprint(f'{\"distribución\":20s} {\"μ_emp\":>8s} {\"μ_teo\":>8s} {\"σ_emp\":>8s} {\"σ_teo\":>8s}')\nfor nombre, (x, mu_t, sd_t) in muestras.items():\n    print(f'{nombre:20s} {x.mean():8.3f} {mu_t:8.3f} {x.std():8.3f} {sd_t:8.3f}')"),
        Cell("md", "## 4️⃣ `choice` y `permutation`\n\n```python\nrng.choice(arr, size, replace=False, p=probabilidades)\nrng.permutation(arr)   # mezcla, devuelve copia\nrng.shuffle(arr)       # mezcla in-place\n```"),
        Cell("code", "rng = np.random.default_rng(42)\nopciones = ['A', 'B', 'C', 'D']\n\n# Muestreo con probabilidades distintas\nmuestra = rng.choice(opciones, size=20, p=[0.5, 0.3, 0.15, 0.05])\nvals, cnts = np.unique(muestra, return_counts=True)\nfor v, c in zip(vals, cnts):\n    print(f'{v}: {c}')\n\n# Permutación reproducible\nrng2 = np.random.default_rng(42)\nrng3 = np.random.default_rng(42)\nprint(f'\\nperm1: {rng2.permutation([1,2,3,4,5])}')\nprint(f'perm2: {rng3.permutation([1,2,3,4,5])}  ← idéntica')"),
        Cell("md", "## 5️⃣ Monte Carlo de π\n\nLanzas puntos al azar en `[-1, 1] × [-1, 1]`. Razón \"dentro del círculo unitario\" / \"total\" tiende a `π/4`."),
        Cell("code", "for N in [1_000, 100_000, 10_000_000]:\n    rng = np.random.default_rng(42)\n    pts = rng.uniform(-1, 1, size=(N, 2))\n    dentro = (pts[:, 0]**2 + pts[:, 1]**2 <= 1).sum()\n    pi_est = 4 * dentro / N\n    error = abs(pi_est - math.pi)\n    print(f'N={N:>10,}  π≈{pi_est:.6f}  error={error:.6f}')"),
        Cell("md", "## 6️⃣ Bootstrap — distribución de un estadístico\n\nResampleas con reemplazo del sample original y recalculas el estadístico — obtienes una distribución del estimador sin asumir CLT."),
        Cell("code", "# Sample observado\nrng = np.random.default_rng(42)\nsample = rng.normal(50, 10, 30)\nprint(f'sample mean : {sample.mean():.2f}')\n\n# Bootstrap: 10000 resamples\nB = 10_000\nbootstrap_means = np.array([\n    rng.choice(sample, size=len(sample), replace=True).mean()\n    for _ in range(B)\n])\n\nprint(f'boot mean   : {bootstrap_means.mean():.2f}')\nprint(f'boot std    : {bootstrap_means.std():.2f}  (= SE de la media)')\nprint(f'95% CI boot : [{np.percentile(bootstrap_means, 2.5):.2f}, {np.percentile(bootstrap_means, 97.5):.2f}]')"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Uso `np.random.default_rng(seed)` no `np.random.seed`\n- [ ] Sé generar normal, uniform, integers, binomial, poisson\n- [ ] Mismo seed → mismo output reproducible\n- [ ] Sé usar `choice` para muestreo con/sin reemplazo\n- [ ] Implementé Monte Carlo y bootstrap"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Monte Carlo de π, bootstrap CI, reproducibilidad, momentos empíricos vs teóricos."),
        Cell("md", "## 🔗 Referencias\n\n- [`random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html)\n- [NEP 19 RNG policy](https://numpy.org/neps/nep-0019-rng-policy.html)\n\n➡️ **Siguiente:** [022 — Pandas: Series y DataFrame](../022-pandas-series-y-dataframe/README.md)"),
    ],
    definiciones=[
        ("Generador pseudoaleatorio (PRNG)", "Algoritmo determinístico que produce secuencia que *parece* aleatoria. Con la misma semilla (seed) produce la misma secuencia → **reproducible**. NumPy 2026 usa PCG64 por default."),
        ("Seed (semilla)", "Estado inicial del PRNG. Mismo seed → misma secuencia, siempre, en cualquier máquina. Es la base de la reproducibilidad científica."),
        ("`np.random.default_rng(seed)`", "API moderno (NumPy 1.17+). Devuelve `Generator` independiente — no toca estado global, múltiples generadores no se interfieren. Reemplaza a `np.random.seed()` + funciones globales (deprecated)."),
        ("Distribuciones continuas comunes", "`uniform(lo, hi)`, `normal(μ, σ)`, `exponential(scale)`, `gamma(shape, scale)`, `beta(a, b)`. Cada una con parámetros que controlan ubicación y dispersión."),
        ("Distribuciones discretas", "`integers(lo, hi)` (uniforme discreto), `binomial(n, p)` (éxitos en n trials), `poisson(λ)` (eventos en intervalo)."),
        ("Bootstrap", "Técnica: resampleas con reemplazo del sample original B veces, recalculas el estadístico → obtienes distribución empírica del estimador. Sin asumir CLT ni normalidad."),
    ],
    errores_comunes=[
        ("Pongo seed pero el resultado cambia entre corridas", "Probablemente otra librería (sklearn, pytorch) usa su propio PRNG. **Fix**: setea seed en cada lib que uses, o pasa el `rng` explícito a funciones que lo acepten."),
        ("`np.random.seed(42)` no funciona como antes", "Está deprecated en favor de `default_rng`. Aún funciona pero NumPy 2+ puede romperlo. **Fix**: migra a `rng = np.random.default_rng(42); rng.normal(...)`."),
        ("`rng.choice(arr, size=N, replace=False)` falla con `ValueError: Cannot take a larger sample than population when 'replace=False'`", "Pediste más muestras únicas que elementos disponibles. **Fix**: aumenta `arr` o usa `replace=True`."),
        ("Genero millones de números 'aleatorios' y mi laptop muere", "Estás materializando lista en RAM. **Fix**: si solo agregas (sum, mean), procesa por chunks: `for _ in range(K): chunk = rng.normal(0,1,N); acc += chunk.sum()`."),
        ("Bootstrap CI parece muy estrecho", "Pocos resamples (B). **Fix**: usa B ≥ 1000 para CI 95%, B ≥ 10000 para colas 99%. El costo es lineal en B."),
    ],
    faq=[
        ("¿Por qué un generador independiente y no el global?",
         "(1) **No interfiere** con libs que también usan random global. (2) **Múltiples experimentos** simultáneos sin conflicto. (3) **API más limpia**. (4) Algoritmo más rápido (PCG64). El legacy es solo por compatibilidad."),
        ("¿Mismo seed da mismos números en Linux/Windows/Mac?",
         "**Sí** — PCG64 es determinístico cross-platform. La única diferencia podría venir de orden de operaciones float (paralelismo), pero `default_rng` es single-threaded."),
        ("¿Qué seed elegir?",
         "Cualquier entero. **42** es convención (Hitchhiker's Guide). **0** funciona pero genera secuencias 'menos aleatorias' en los primeros bits con algunos PRNG (no PCG64). Lo importante es **registrarlo** para reproducir."),
        ("¿Bootstrap mejor que t-test?",
         "Diferente caso. **t-test**: asume normalidad, da p-valor analítico. **Bootstrap**: sin asunción, da distribución empírica de cualquier estadístico (media, mediana, ratio). Para datos no-normales o estadísticos complejos, bootstrap gana."),
        ("¿Cuántas muestras necesito para Monte Carlo?",
         "El error decrece como `1/√N`. Para 1 decimal de precisión: N ≈ 100. Para 2 decimales: N ≈ 10k. Para 3: N ≈ 1M. Verifica convergencia haciendo N=100, 1k, 10k, 100k y mirando que el resultado se estabilice."),
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
