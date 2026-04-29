# 💻 Guía de código — Clase 01: Fundamentos de Python aplicados a datos

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Variables y tipos de datos

```python
# Una variable guarda un valor con un nombre expresivo.
# Los tipos de dato determinan qué operaciones podemos hacer.

producto = "Mouse"          # str: texto
precio_unitario = 8990      # int: número entero (pesos chilenos)
descuento_pct = 0.10        # float: número decimal (10%)
en_stock = True             # bool: verdadero o falso

# Calculamos el precio con descuento usando las variables anteriores.
precio_final = precio_unitario * (1 - descuento_pct)
print(f"{producto} — Precio final: ${precio_final:,.0f}")
```

**¿Qué hace este bloque?**
Define cuatro variables de distintos tipos y las combina en un cálculo. El f-string formatea el resultado con separadores de miles y sin decimales, lo que lo hace legible como precio en pantalla.

**¿Por qué se escribe así y no de otra forma?**
Usar nombres descriptivos (`precio_unitario` en lugar de `p`) hace que el código se lea como una oración. El f-string con `:,.0f` es más claro que concatenar strings manualmente con `str()`.

**Resultado esperado:**
```
Mouse — Precio final: $8,091
```

---

## Bloque 2: Listas para agrupar valores del mismo tipo

```python
# Una lista agrupa múltiples valores bajo un solo nombre.
ventas_diarias = [45000, 62000, 38000, 71000, 55000]

# Calculamos métricas básicas sin escribir cada valor por separado.
total = sum(ventas_diarias)
promedio = total / len(ventas_diarias)
máximo = max(ventas_diarias)

print(f"Total semana: ${total:,}")
print(f"Promedio diario: ${promedio:,.0f}")
print(f"Mejor día: ${máximo:,}")
```

**¿Qué hace este bloque?**
Agrupa las ventas de cinco días en una lista y calcula el total, promedio y máximo usando funciones integradas de Python (`sum`, `len`, `max`). Ningún valor está "hardcodeado" en los cálculos.

**¿Por qué se escribe así y no de otra forma?**
Si los datos cambian (o si hay 500 días en lugar de 5), el código no necesita modificarse. Las funciones `sum`, `len` y `max` funcionan con cualquier lista numérica.

**Resultado esperado:**
```
Total semana: $271,000
Promedio diario: $54,200
Mejor día: $71,000
```

---

## Bloque 3: Diccionarios para representar registros con campos

```python
# Un diccionario asocia claves (nombres de campo) con valores.
# Es ideal para representar un registro con múltiples atributos.
venta = {
    "producto": "Teclado",
    "unidades": 2,
    "precio_unitario": 15990,
    "descuento_pct": 0.05,
}

# Accedemos a cada campo por su nombre, no por posición.
total_neto = venta["unidades"] * venta["precio_unitario"] * (1 - venta["descuento_pct"])
print(f"Venta de {venta['producto']}: ${total_neto:,.0f}")
```

**¿Qué hace este bloque?**
Crea un registro de venta como diccionario y calcula el total neto accediendo a sus campos por nombre. Este patrón es la base de las filas de un DataFrame en pandas.

**¿Por qué se escribe así y no de otra forma?**
Un diccionario es más seguro que una lista para este caso: si el orden de los campos cambia, el cálculo sigue siendo correcto porque accedemos por clave, no por índice.

**Resultado esperado:**
```
Venta de Teclado: $30,381
```

---

## Bloque 4: Funciones para encapsular lógica reutilizable

```python
# Una función agrupa una operación con nombre propio.
# Parámetros: lo que necesita. Return: lo que devuelve.
def calcular_total_bruto(unidades, precio_unitario):
    """Calcula el ingreso bruto antes de descuentos."""
    return unidades * precio_unitario


# Lista de ventas representada como lista de diccionarios.
ventas = [
    {"producto": "Mouse",   "unidades": 3, "precio_unitario": 8990},
    {"producto": "Teclado", "unidades": 2, "precio_unitario": 15990},
    {"producto": "Monitor", "unidades": 1, "precio_unitario": 89990},
]

# Aplicamos la función a cada registro usando comprensión de listas.
totales = [calcular_total_bruto(v["unidades"], v["precio_unitario"]) for v in ventas]

for venta, total in zip(ventas, totales):
    print(f"{venta['producto']}: ${total:,}")
```

**¿Qué hace este bloque?**
Define una función de cálculo y la aplica a una lista de ventas. `zip` permite iterar en paralelo sobre dos listas (ventas y totales) para imprimir ambos juntos.

**¿Por qué se escribe así y no de otra forma?**
Al encapsular el cálculo en `calcular_total_bruto`, si la lógica cambia (por ejemplo, agregar IVA), solo se modifica en un lugar. Esto evita errores de inconsistencia.

**Resultado esperado:**
```
Mouse: $26,970
Teclado: $31,980
Monitor: $89,990
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `TypeError: can only concatenate str (not "int") to str` | Se intenta unir un string y un número con `+` sin convertir | Usar f-string: `f"Total: {total}"` o convertir explícitamente: `str(total)` |
| `ZeroDivisionError: division by zero` | Se divide entre cero, por ejemplo si una lista está vacía | Verificar `if len(lista) > 0` antes de dividir, o usar `len(lista) or 1` como guardia |
| `KeyError: 'precio'` | La clave buscada no existe en el diccionario (puede estar mal escrita) | Imprimir `dict.keys()` para ver las claves disponibles; usar `.get("precio", 0)` para valor por defecto |
| `NameError: name 'total' is not defined` | La variable se usa antes de ser definida, o está definida dentro de una función y se usa afuera | Revisar el orden de definición; asegurarse de que la función use `return` y no solo `print` |
