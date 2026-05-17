# 📘 Clase 14: NumPy - Arrays y cálculo vectorizado

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo

Aprender a usar NumPy para crear y manipular arrays numéricos, y entender por qué el cálculo vectorizado es mucho más eficiente que usar bucles de Python. El estudiante podrá extraer columnas de un dataset real como arrays y aplicar operaciones estadísticas y transformaciones sin escribir un solo `for`.

## ⏱️ Duración sugerida

90 minutos

## 📦 Dataset base

- `datasets/ventas_tienda.csv`

## ✅ Resultados esperados

Al finalizar, el estudiante podrá:

- Crear arrays NumPy de distintas formas (desde listas, con zeros/ones, con arange/linspace)
- Consultar las propiedades de un array: shape, dtype, ndim, size
- Indexar y hacer slicing en arrays unidimensionales y bidimensionales
- Aplicar operaciones vectorizadas: suma, multiplicación, comparación sin bucles
- Calcular estadísticas sobre un array: media, desviación estándar, mínimo, máximo, suma, mediana
- Filtrar un array usando condiciones booleanas
- Extraer una columna de un CSV como array NumPy y operarla

## 🧭 Temas clave

- Qué es NumPy y por qué es más rápido que las listas de Python
- Creación de arrays: `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`
- Propiedades del array: `dtype`, `shape`, `ndim`, `size`
- Indexado y slicing (misma sintaxis que listas, pero sobre arrays multidimensionales)
- Operaciones vectorizadas: aritmética y comparaciones elemento a elemento
- Funciones estadísticas: `np.mean`, `np.std`, `np.min`, `np.max`, `np.sum`, `np.median`
- Filtrado de arrays con condiciones booleanas (boolean indexing)
- Reshaping de arrays
- Por qué pandas usa NumPy internamente

## 🧰 Materiales del módulo

- `README.md`
- `slides.md`
- `teoria.md`
- `ejercicios.md`
- `homework.md`
- `notebook.ipynb`
- `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase

- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.
- Antes de pasar al siguiente paso, verifica que entiendes la salida.

## 💡 Idea central

NumPy permite operar sobre miles de números a la vez, sin bucles, de forma rápida y clara.

## 👩‍🏫 Nota para el docente

Demuestra en vivo la diferencia de velocidad entre sumar 1,000,000 de números con un bucle de Python versus con NumPy. El resultado visual (tiempo de ejecución) impacta más que cualquier explicación. Luego conecta: "pandas trabaja sobre columnas que internamente son arrays NumPy — por eso pandas también es rápido".
