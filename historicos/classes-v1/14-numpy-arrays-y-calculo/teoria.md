# 🧠 Documento teórico — Clase 14: NumPy - Arrays y cálculo vectorizado

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

NumPy permite operar sobre miles de números a la vez, sin bucles, de forma rápida y clara.

## ❓ Por qué importa este módulo

Python es un lenguaje muy flexible, pero sus listas no están optimizadas para cálculo numérico a gran escala. NumPy resuelve esto con los **arrays**: estructuras que almacenan datos del mismo tipo de forma contigua en memoria, lo que permite aplicar operaciones sobre todos los elementos simultáneamente. Pandas y scikit-learn están construidos sobre NumPy, por lo que entender arrays es entender la base de casi toda la ciencia de datos en Python.

## 📖 ¿Qué es NumPy?

NumPy (Numerical Python) es una biblioteca que proporciona:

1. **El objeto `ndarray`**: un array multidimensional de elementos del mismo tipo
2. **Funciones vectorizadas**: operaciones que se aplican a todo el array sin bucles explícitos
3. **Herramientas matemáticas**: álgebra lineal, generación de números aleatorios, transformadas de Fourier

La ventaja de velocidad viene del hecho de que NumPy está implementado en C, y los datos se almacenan en bloques contiguos de memoria que el procesador puede cargar eficientemente.

## 💻 Bloque de código documentado

### Crear arrays de distintas formas

**Qué hace:** muestra las seis formas más comunes de crear arrays NumPy.

**Para qué sirve:** elegir la forma correcta de crear un array según la situación (desde datos existentes, o generando secuencias/rangos para análisis).

```python
import numpy as np

# Desde una lista de Python — el caso más frecuente al trabajar con datos
precios = np.array([29.99, 45.50, 12.00, 89.99, 34.75])
print(precios)           # [29.99 45.5  12.   89.99 34.75]
print(type(precios))     # <class 'numpy.ndarray'>

# Array de ceros — útil como punto de partida para llenar después
ceros = np.zeros(5)
print(ceros)             # [0. 0. 0. 0. 0.]

# Array de unos — útil como máscara o valor inicial
unos = np.ones(5)
print(unos)              # [1. 1. 1. 1. 1.]

# Rango de enteros — equivalente a range(), pero devuelve un array
rango = np.arange(0, 10, 2)   # desde 0, hasta 10 (excluido), paso 2
print(rango)             # [0 2 4 6 8]

# Valores igualmente espaciados entre dos extremos — útil para gráficas
espacio = np.linspace(0, 1, 5)  # 5 valores entre 0 y 1
print(espacio)           # [0.   0.25 0.5  0.75 1.  ]

# Array 2D (matriz) desde lista de listas
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz.shape)      # (2, 3) — 2 filas, 3 columnas
```

### Propiedades del array

**Qué hace:** consulta las características de un array.

**Para qué sirve:** antes de operar sobre un array, conviene conocer su forma, tipo de dato y tamaño para evitar errores.

```python
import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

print(arr.dtype)   # int64 — tipo de dato de los elementos
print(arr.shape)   # (2, 3) — (filas, columnas)
print(arr.ndim)    # 2 — número de dimensiones
print(arr.size)    # 6 — total de elementos
```

### Operaciones vectorizadas

**Qué hace:** aplica operaciones aritméticas a todos los elementos sin escribir un bucle.

**Para qué sirve:** calcular precios con IVA, normalizar puntuaciones, comparar valores — todo en una sola línea clara y eficiente.

```python
import numpy as np

precios = np.array([29.99, 45.50, 12.00, 89.99, 34.75])

# Aplicar IVA del 16% a todos los precios a la vez
precios_con_iva = precios * 1.16
print(precios_con_iva)   # [34.7884 52.78   13.92   104.3884 40.31]

# Comparar qué precios superan cierto umbral
# El resultado es un array de True/False para cada elemento
mascara = precios > 30
print(mascara)           # [False  True False  True  True]
```

### Funciones estadísticas

**Qué hace:** calcula estadísticas sobre el array completo o por eje (filas/columnas).

**Para qué sirve:** resumir datos numéricos, detectar valores extremos, medir dispersión.

```python
import numpy as np

ventas = np.array([120, 95, 200, 180, 145, 210, 88])

print(np.mean(ventas))    # Promedio: 148.28...
print(np.median(ventas))  # Mediana: 145.0 (el valor central)
print(np.std(ventas))     # Desviación estándar: mide cuánto varían los datos
print(np.min(ventas))     # Mínimo: 88
print(np.max(ventas))     # Máximo: 210
print(np.sum(ventas))     # Suma total: 1038
print(np.argmax(ventas))  # Índice del máximo: 5 (el sexto elemento)
```

### Filtrado con condiciones booleanas (boolean indexing)

**Qué hace:** selecciona solo los elementos que cumplen una condición.

**Para qué sirve:** filtrar datos sin bucles — equivalente a un WHERE en SQL o a df[condición] en pandas.

```python
import numpy as np

ventas = np.array([120, 95, 200, 180, 145, 210, 88])

# Seleccionar solo ventas mayores a 150
ventas_altas = ventas[ventas > 150]
print(ventas_altas)      # [200 180 210]

# Contar cuántas ventas superan el promedio
promedio = np.mean(ventas)
sobre_promedio = np.sum(ventas > promedio)
print(f"Ventas sobre el promedio: {sobre_promedio}")
```

### Reshaping

**Qué hace:** cambia la forma de un array sin alterar sus datos.

**Para qué sirve:** reorganizar datos para que sean compatibles con algoritmos que esperan matrices 2D.

```python
import numpy as np

# Array de 6 elementos
arr = np.arange(1, 7)
print(arr)           # [1 2 3 4 5 6]

# Reorganizar en 2 filas de 3 columnas
matriz = arr.reshape(2, 3)
print(matriz)
# [[1 2 3]
#  [4 5 6]]

# -1 deja que NumPy calcule la dimensión automáticamente
arr_col = arr.reshape(-1, 1)  # columna de 6 filas
print(arr_col.shape)          # (6, 1)
```

## ⚠️ Errores frecuentes a vigilar

- **Mezclar tipos en un array**: NumPy fuerza todos los elementos al mismo tipo; si mezclas enteros y strings, todos se convierten a string silenciosamente
- **Confundir `shape` con `size`**: `shape` devuelve una tupla con las dimensiones; `size` devuelve el total de elementos
- **Olvidar que el slicing no copia**: `b = a[1:4]` crea una *vista* del array original; modificar `b` modifica `a`; usar `b = a[1:4].copy()` para evitarlo
- **Usar `==` para comparar arrays enteros**: devuelve un array de booleanos, no un solo True/False; usar `np.array_equal(a, b)` para comparar dos arrays completamente

## 🔗 Conexión con el siguiente módulo

Ahora que entiendes arrays y cálculo vectorizado, estás listo para la Clase 15: SQL básico con Python. Verás que muchas consultas SQL hacen en una sola línea declarativa lo que en NumPy/pandas requiere varias transformaciones — cada herramienta tiene su lugar ideal.
