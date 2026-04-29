# 💻 Guía de código — Clase 14: NumPy — Arrays y cálculo vectorizado

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Crear arrays de distintas formas

```python
import numpy as np

# Desde una lista de Python
ventas = np.array([150, 230, 180, 310, 275, 190])

# Matriz de ceros de 3 filas y 4 columnas
matriz_ceros = np.zeros((3, 4))

# Secuencia con paso fijo (como range, pero devuelve un array)
dias = np.arange(1, 31, 1)           # del 1 al 30, paso 1

# N puntos igualmente espaciados entre dos valores
precios_escala = np.linspace(0, 100, 11)  # 11 valores: 0, 10, 20, ..., 100
```

**¿Qué hace este bloque?**
- `np.array([...])`: convierte una lista de Python en un array NumPy. La diferencia es que NumPy almacena todos los elementos del mismo tipo en memoria contigua, lo que hace los cálculos mucho más rápidos.
- `np.zeros((3, 4))`: crea una matriz de 3 filas y 4 columnas rellena de ceros. El argumento es una tupla con la forma deseada.
- `np.arange(inicio, fin, paso)`: funciona como `range()` de Python pero devuelve un array. El valor `fin` no se incluye.
- `np.linspace(inicio, fin, n)`: divide el intervalo en exactamente `n` puntos igualmente distribuidos, incluyendo ambos extremos.

**¿Por qué se escribe así y no de otra forma?**
`linspace` se prefiere cuando necesitas exactamente N puntos (por ejemplo, para graficar una función continua). `arange` se prefiere cuando sabes el paso entre valores. Con listas de Python tendrías que escribir un `for` o una comprensión de lista, lo que es más lento y menos expresivo.

**Resultado esperado:**
```
ventas         → array([150, 230, 180, 310, 275, 190])
matriz_ceros   → array([[0., 0., 0., 0.],
                         [0., 0., 0., 0.],
                         [0., 0., 0., 0.]])
dias           → array([ 1,  2,  3, ..., 30])
precios_escala → array([  0.,  10.,  20., ..., 100.])
```

---

## Bloque 2: Propiedades e indexación

```python
ventas = np.array([150, 230, 180, 310, 275, 190])

# Propiedades del array
print("Forma:", ventas.shape)       # (6,) — 1D con 6 elementos
print("Tipo:", ventas.dtype)        # int64 — enteros de 64 bits
print("Dimensiones:", ventas.ndim)  # 1
print("Total elementos:", ventas.size)  # 6

# Indexación básica (empieza en 0)
print("Primera venta:", ventas[0])    # 150
print("Última venta:", ventas[-1])    # 190

# Slicing: [inicio:fin] — fin NO incluido
print("Ventas del 2 al 4:", ventas[1:4])  # [230, 180, 310]

# Array 2D: indexación con dos índices
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Elemento fila 1, col 2:", matriz[1, 2])  # 6
print("Segunda fila completa:", matriz[1, :])    # [4, 5, 6]
print("Segunda columna:", matriz[:, 1])          # [2, 5, 8]
```

**¿Qué hace este bloque?**
- `.shape`: devuelve la dimensión como tupla. `(6,)` es 1D, `(3, 4)` es 2D con 3 filas y 4 columnas.
- `.dtype`: el tipo de dato de los elementos. `int64` para enteros, `float64` para decimales.
- `ventas[-1]`: los índices negativos cuentan desde el final: -1 es el último, -2 el penúltimo, etc.
- `ventas[1:4]`: extrae una "rebanada" (slice) desde el índice 1 hasta el 3 (el 4 no se incluye).
- `matriz[1, 2]`: en arrays 2D se usan dos índices separados por coma: primero la fila, luego la columna.
- `matriz[:, 1]`: el `:` solo significa "todas" — en este caso, todas las filas, columna 1.

**¿Por qué se escribe así y no de otra forma?**
La notación `[:,1]` es mucho más concisa que un bucle `for`. Entender `axis=0` (filas) y `axis=1` (columnas) es fundamental para trabajar con datos tabulares en NumPy y pandas.

**Resultado esperado:**
```
Forma: (6,)
Tipo: int64
Primera venta: 150
Última venta: 190
Ventas del 2 al 4: [230 180 310]
Elemento fila 1, col 2: 6
Segunda columna: [2 5 8]
```

---

## Bloque 3: Operaciones vectorizadas y estadísticas

```python
ventas = np.array([150, 230, 180, 310, 275, 190])

# Operaciones elemento a elemento — sin necesidad de bucle for
ventas_con_iva = ventas * 1.19
ventas_normalizadas = ventas / ventas.max()

# Funciones estadísticas
print("Promedio:", ventas.mean())
print("Desviación estándar:", ventas.std().round(2))
print("Mínimo:", ventas.min(), "en índice:", ventas.argmin())
print("Máximo:", ventas.max(), "en índice:", ventas.argmax())
print("Suma total:", ventas.sum())
print("Mediana:", np.median(ventas))
print("Percentil 75:", np.percentile(ventas, 75))

# Filtrado booleano — seleccionar elementos por condición
ventas_altas = ventas[ventas > 200]
print("Ventas mayores a 200:", ventas_altas)

# Índices donde se cumple la condición
indices_pico = np.where(ventas > ventas.mean())
print("Índices sobre la media:", indices_pico[0])
```

**¿Qué hace este bloque?**
- `ventas * 1.19`: multiplica TODOS los elementos por 1.19 en una sola operación. No se necesita un `for`.
- `.argmin()` / `.argmax()`: devuelven el *índice* donde está el mínimo/máximo, no el valor en sí.
- `ventas[ventas > 200]`: el filtrado booleano funciona en dos pasos: primero crea una máscara `[False, True, False, True, True, False]`, luego selecciona los elementos donde es `True`.
- `np.where(condicion)`: devuelve los índices donde la condición es verdadera (útil para saber en qué posición están los valores que cumplen la condición).

**¿Por qué se escribe así y no de otra forma?**
Las operaciones vectorizadas son la gran ventaja de NumPy. Un `for` en Python que recorre 1 millón de elementos puede tardar segundos; la misma operación vectorizada en NumPy tarda milisegundos. Para datasets grandes, esta diferencia es crucial.

**Resultado esperado:**
```
Promedio: 222.5
Desviación estándar: 56.07
Mínimo: 150 en índice: 0
Máximo: 310 en índice: 3
Suma total: 1335
Ventas mayores a 200: [230 310 275]
Índices sobre la media: [1 3 4]
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `ValueError: cannot reshape array of size 10 into shape (3,4)` | El número de elementos no coincide con la nueva forma (10 ≠ 3×4=12) | Verificar que `filas × columnas == array.size` antes de hacer `reshape` |
| `IndexError: index 6 is out of bounds for axis 0 with size 6` | Se accedió a un índice que no existe (array va del índice 0 al 5) | El último índice válido siempre es `len(arr) - 1`; usar `-1` para el último |
| `TypeError: ufunc 'add' did not contain a loop` | Se intentó sumar arrays de tipos incompatibles (texto + número) | Verificar `arr.dtype` y convertir con `.astype(float)` si es necesario |
| División entera da resultado inesperado | Dividir dos arrays de tipo `int64` trunca los decimales | Convertir a float primero: `ventas.astype(float) / total` |
| `ValueError: operands could not be broadcast together` | Los `shape` de dos arrays son incompatibles para la operación | Revisar shapes con `.shape` y usar `.reshape()` para hacerlos compatibles |
