# Documento Teórico — Clase 01: Fundamentos de Python aplicados a datos

> **Nivel:** Principiante · **Duración estimada de lectura:** 25 minutos

---

## 1. Variables y tipos de datos

Una **variable** es un nombre que apunta a un valor en memoria. Python es dinámico: el tipo se infiere automáticamente.

### 1.1 Tipos fundamentales

| Tipo | Nombre Python | Ejemplo | Uso en Data Science |
|---|---|---|---|
| Entero | `int` | `ventas = 150` | Conteos, cantidades |
| Decimal | `float` | `precio = 9.99` | Precios, porcentajes, métricas |
| Texto | `str` | `ciudad = "Santiago"` | Categorías, etiquetas |
| Booleano | `bool` | `activo = True` | Filtros, condiciones |
| Nulo | `NoneType` | `descuento = None` | Valor faltante |

```python
producto = "Mouse"         # str
precio = 8990              # int
precio_oferta = 7490.50    # float
tiene_stock = True         # bool
proveedor = None           # NoneType — no hay proveedor asignado

print(type(producto))      # <class 'str'>
print(type(precio))        # <class 'int'>
```

### 1.2 Conversión entre tipos

```python
# str → int / float
cantidad_txt = "15"
cantidad = int(cantidad_txt)        # 15
porcentaje = float("0.12")          # 0.12

# int/float → str (para mostrar)
mensaje = "Total: $" + str(precio * cantidad)

# Verificar si es convertible
print("15".isdigit())   # True
print("abc".isdigit())  # False
```

---

## 2. Operadores

### 2.1 Aritméticos

| Operador | Operación | Ejemplo | Resultado |
|---|---|---|---|
| `+` | Suma | `5 + 3` | `8` |
| `-` | Resta | `10 - 4` | `6` |
| `*` | Multiplicación | `3 * 7` | `21` |
| `/` | División | `15 / 4` | `3.75` |
| `//` | División entera | `15 // 4` | `3` |
| `%` | Módulo (resto) | `15 % 4` | `3` |
| `**` | Potencia | `2 ** 8` | `256` |

### 2.2 Comparación

| Operador | Significado | Ejemplo | Resultado |
|---|---|---|---|
| `==` | Igual | `5 == 5` | `True` |
| `!=` | Distinto | `5 != 3` | `True` |
| `>` | Mayor | `10 > 8` | `True` |
| `<` | Menor | `3 < 1` | `False` |
| `>=` | Mayor o igual | `5 >= 5` | `True` |
| `<=` | Menor o igual | `4 <= 3` | `False` |

---

## 3. Estructuras de datos

### 3.1 Listas

Una lista almacena una secuencia ordenada de elementos (pueden ser de distintos tipos).

```python
precios = [8990, 15990, 25990, 3490]

# Acceder por índice (empieza en 0)
print(precios[0])    # 8990
print(precios[-1])   # 3490 (último elemento)

# Slicing
print(precios[1:3])  # [15990, 25990]

# Métodos útiles
precios.append(12000)       # agregar al final
precios.sort()               # ordenar in-place
print(len(precios))          # número de elementos
print(sum(precios))          # suma de todos
print(min(precios))          # mínimo
print(max(precios))          # máximo
```

### 3.2 Diccionarios

Un diccionario almacena pares **clave: valor**. Ideal para representar un registro de datos.

```python
producto = {
    "nombre": "Teclado mecánico",
    "precio": 45990,
    "stock": 23,
    "categoria": "Periféricos",
    "activo": True
}

# Acceder
print(producto["nombre"])         # Teclado mecánico
print(producto.get("iva", 0.19))  # 0.19 (valor por defecto si no existe)

# Modificar
producto["precio"] = 42990
producto["descuento_pct"] = 0.10

# Iterar
for clave, valor in producto.items():
    print(f"  {clave}: {valor}")
```

### 3.3 Comparación de estructuras

| Estructura | Ordenada | Mutable | Duplicados | Ejemplo |
|---|---|---|---|---|
| `list` | ✅ Sí | ✅ Sí | ✅ Permite | `[1, 2, 2, 3]` |
| `tuple` | ✅ Sí | ❌ No | ✅ Permite | `(1, 2, 3)` |
| `set` | ❌ No | ✅ Sí | ❌ No permite | `{1, 2, 3}` |
| `dict` | ✅ Sí (3.7+) | ✅ Sí | Claves únicas | `{"a": 1}` |

---

## 4. Control de flujo

### 4.1 Condicionales

```python
ventas = 450

if ventas >= 500:
    categoria = "Alto rendimiento"
elif ventas >= 300:
    categoria = "Rendimiento medio"
else:
    categoria = "Bajo rendimiento"

print(f"Categoría: {categoria}")
```

**Condicional en una línea (ternario):**

```python
estado = "activo" if ventas > 0 else "inactivo"
```

### 4.2 Bucle `for`

```python
ventas_por_sucursal = {
    "Norte": 345000,
    "Sur": 289000,
    "Centro": 512000,
    "Oriente": 198000
}

total = 0
for sucursal, monto in ventas_por_sucursal.items():
    total += monto
    print(f"{sucursal}: ${monto:,}")

print(f"\nTotal: ${total:,}")
print(f"Promedio: ${total / len(ventas_por_sucursal):,.0f}")
```

### 4.3 Bucle `while`

```python
intentos = 0
limite = 5

while intentos < limite:
    print(f"Intento {intentos + 1}")
    intentos += 1
```

### 4.4 List comprehensions

Forma concisa de crear listas a partir de otras:

```python
precios = [8990, 15990, 25990, 3490]

# Calcular precios con IVA (19%)
precios_con_iva = [p * 1.19 for p in precios]

# Filtrar solo precios mayores a 10.000
precios_altos = [p for p in precios if p > 10000]

# Combinar filtro y transformación
precios_altos_con_iva = [p * 1.19 for p in precios if p > 10000]
```

---

## 5. Funciones

Una función encapsula lógica reutilizable. En Data Science, las funciones son esenciales para aplicar transformaciones a múltiples columnas o filas.

### 5.1 Sintaxis básica

```python
def calcular_total_neto(unidades, precio_unitario, descuento_pct=0.0):
    """
    Calcula el total neto de una venta.
    
    Args:
        unidades (int): cantidad vendida
        precio_unitario (float): precio sin descuento
        descuento_pct (float): porcentaje de descuento (0.0–1.0)
    
    Returns:
        float: total después de aplicar descuento
    """
    total_bruto = unidades * precio_unitario
    total_neto = total_bruto * (1 - descuento_pct)
    return total_neto

# Llamadas
print(calcular_total_neto(3, 8990))          # sin descuento
print(calcular_total_neto(3, 8990, 0.10))    # con 10% descuento
print(calcular_total_neto(descuento_pct=0.15, unidades=5, precio_unitario=12000))
```

### 5.2 Funciones que retornan múltiples valores

```python
def resumen_ventas(lista_montos):
    return {
        "total": sum(lista_montos),
        "promedio": sum(lista_montos) / len(lista_montos),
        "maximo": max(lista_montos),
        "minimo": min(lista_montos),
        "n": len(lista_montos)
    }

ventas = [45000, 67000, 32000, 89000, 55000]
res = resumen_ventas(ventas)
print(f"Total: ${res['total']:,}")
print(f"Promedio: ${res['promedio']:,.0f}")
```

---

## 6. Formateo de cadenas

```python
nombre = "Santiago"
ventas = 1234567.89

# f-strings (recomendado desde Python 3.6)
print(f"Ciudad: {nombre}")
print(f"Ventas: ${ventas:,.2f}")        # separador de miles y 2 decimales
print(f"Porcentaje: {0.1234:.1%}")      # formato porcentaje
print(f"{'Producto':20} {'Precio':>10}")  # alineación

# Tabla formateada
datos = [("Mouse", 8990), ("Teclado", 15990), ("Webcam", 25990)]
print(f"\n{'Producto':<15} {'Precio':>10}")
print("-" * 26)
for nombre, precio in datos:
    print(f"{nombre:<15} ${precio:>9,}")
```

---

## 7. Errores frecuentes para principiantes

| Error | Causa | Solución |
|---|---|---|
| `NameError: name 'x' is not defined` | Variable no definida o con typo | Verificar nombre y scope |
| `IndexError: list index out of range` | Índice fuera del rango de la lista | Verificar `len()` antes de acceder |
| `KeyError: 'columna'` | Clave no existe en el diccionario | Usar `.get(clave, default)` |
| `TypeError: unsupported operand type(s)` | Operación entre tipos incompatibles | Convertir tipos antes |
| `IndentationError` | Indentación incorrecta | Python usa 4 espacios por nivel |
| `ZeroDivisionError` | División por cero | Verificar denominador antes de dividir |

---

## 8. Resumen rápido

```
✅ Variables → nombres para valores en memoria
✅ Tipos → int, float, str, bool, None
✅ Listas → colecciones ordenadas y mutables
✅ Diccionarios → pares clave:valor
✅ if/elif/else → decisiones
✅ for → iterar sobre colecciones
✅ Funciones → código reutilizable y organizado
✅ f-strings → formateo moderno de texto
```
