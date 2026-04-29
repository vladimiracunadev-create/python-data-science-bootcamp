# 🧪 Ejercicios — Clase 14

> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar

- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.
- Explica qué hace cada transformación relevante y para qué sirve.

## 🧭 Trabajo guiado

### Ejercicio 1: Crear y explorar arrays

Crea los siguientes arrays y para cada uno imprime su `dtype`, `shape`, `ndim` y `size`:

a) Un array con los números `[5, 10, 15, 20, 25, 30]`
b) Un array de 8 ceros
c) Un array con todos los números pares entre 0 y 20 (inclusive) usando `np.arange`
d) Un array de 6 valores igualmente espaciados entre 0 y 100 usando `np.linspace`
e) Una matriz 3×3 con los valores del 1 al 9

Pregunta de reflexión: ¿Por qué el `dtype` del array (a) es `int64` y el de (b) es `float64`?

### Ejercicio 2: Operaciones vectorizadas con datos de ventas

Carga el dataset `ventas_tienda.csv` y extrae las columnas `precio_unitario` y `unidades` como arrays NumPy. Luego:

a) Calcula el total de venta por registro (precio × unidades) usando operación vectorizada — sin bucle
b) Aplica un descuento del 10% a todos los precios unitarios
c) Crea un array booleano que indique qué registros tienen más de 10 unidades vendidas
d) Usando el array booleano anterior, extrae solo los precios de esos registros

```python
import pandas as pd
import numpy as np

df = pd.read_csv("../../datasets/ventas_tienda.csv")

# Extraer columnas como arrays NumPy
# .values convierte una columna de pandas a un array NumPy
precios = df["precio_unitario"].values
unidades = df["unidades"].values

# Tu código aquí
```

### Ejercicio 3: Estadísticas sobre el array de precios

Usando el array `precios` del ejercicio anterior, calcula y muestra:

a) El precio promedio
b) El precio mediano
c) La desviación estándar de los precios
d) El precio mínimo y máximo
e) Cuántos productos tienen un precio por encima del precio promedio

Para el punto (e), exprésalo también como porcentaje del total de registros.

### Ejercicio 4: Reshaping y arrays 2D

a) Crea un array con los números del 1 al 12 usando `np.arange`
b) Reorganízalo en una matriz de 3 filas × 4 columnas
c) Reorganízalo en una matriz de 4 filas × 3 columnas
d) Selecciona la segunda fila completa de la matriz
e) Selecciona la primera columna completa de la matriz
f) Selecciona el elemento en la posición fila 2, columna 1 (índice 0-based)

### Ejercicio 5 (desafío): Normalización de precios

Normaliza el array de precios unitarios para que todos los valores queden entre 0 y 1, usando la fórmula **min-max**:

```
valor_normalizado = (valor - minimo) / (maximo - minimo)
```

Comprueba que el resultado mínimo sea 0.0 y el máximo sea 1.0.

> Esta técnica se usa en machine learning para que variables con diferentes rangos sean comparables.

## ✅ Criterios de autocorrección

- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
- No se usan bucles `for` donde una operación vectorizada es posible.
- El array de totales en el ejercicio 2 tiene la misma longitud que las columnas originales.
