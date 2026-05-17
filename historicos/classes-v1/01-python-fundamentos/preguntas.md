# ❓ Preguntas de evaluación — Clase 01: Fundamentos de Python aplicados a datos

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Qué diferencia hay entre una variable de tipo `int` y una de tipo `float` en Python? ¿Cuándo importa esa diferencia en un análisis de datos?
2. ¿Por qué se prefiere una lista sobre variables separadas (`venta1`, `venta2`, `venta3`) cuando se trabaja con muchos valores del mismo tipo?
3. ¿Qué ventaja tiene guardar información de un producto en un diccionario en lugar de en variables sueltas?
4. ¿Qué significa que una función "retorna" un valor? ¿En qué se diferencia de simplemente imprimir el resultado con `print()`?
5. ¿Cuándo conviene usar un bucle `for` y cuándo un `if/else`? Describe un escenario de ventas para cada caso.

## 💻 Preguntas de código

1. ¿Qué imprime el siguiente bloque y por qué?

```python
ventas = [5000, 12000, 8500, 3200]
total = sum(ventas)
promedio = total / len(ventas)
print(f"Promedio: {promedio:.0f}")
```

2. ¿Cuál es el error en este código y cómo se corrige?

```python
def calcular_descuento(precio, pct):
    descuento = precio * pct
    print(descuento)

precio_final = 10000 - calcular_descuento(10000, 0.1)
print(precio_final)
```

3. ¿Qué hace la comprensión de listas del siguiente bloque? Reescríbela como un bucle `for` tradicional.

```python
productos = ["Mouse", "Teclado", "Monitor"]
mayusculas = [p.upper() for p in productos]
```

4. ¿Qué devuelve `ventas["Teclado"]` si `ventas = {"Mouse": 8990, "Teclado": 15990}`? ¿Qué pasaría si buscas una clave que no existe?

## 🔗 Preguntas integradoras

1. En un negocio real, ¿qué tipo de información se podría representar como una lista de diccionarios? Da un ejemplo con al menos 3 campos y explica por qué esa estructura es útil para analizarla después con pandas.
2. ¿Por qué encapsular cálculos en funciones (como `calcular_total_bruto`) mejora la calidad del análisis en comparación con escribir la misma operación en múltiples partes del código?
3. ¿Cómo se conecta lo que aprendiste en esta clase con el trabajo de un analista de datos que recibe una hoja de cálculo con miles de filas? ¿Qué elementos de Python usaría para procesarla antes de cargarla en pandas?
