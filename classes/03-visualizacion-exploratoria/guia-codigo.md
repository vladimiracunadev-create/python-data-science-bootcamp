# 💻 Guía de código — Clase 03: Visualización exploratoria

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Calcular la métrica base antes de graficar

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset ya limpio (resultado de la clase 02).
df = pd.read_csv("datasets/ventas_tienda.csv", encoding="utf-8")

# Calculamos la venta neta por fila: unidades × precio × (1 - descuento).
# Esta columna es la métrica real de interés; sin ella solo tenemos unidades brutas.
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

print("Columnas disponibles:", df.columns.tolist())
print(df[["producto", "categoría", "total_neto"]].head())
```

**¿Qué hace este bloque?**
Carga el CSV y crea la columna `total_neto`, que representa el ingreso real después de aplicar el descuento. Esta columna es la que después se agrupará y graficará. Sin este paso, cualquier visualización mostraría cantidades sin contexto económico.

**¿Por qué se escribe así y no de otra forma?**
Crear la métrica antes de agrupar es la secuencia correcta: primero calculamos qué queremos medir, luego lo resumimos por categoría. Si se intentara calcular el total neto después del `groupby`, se perdería la posibilidad de aplicar la fórmula fila por fila.

**Resultado esperado:**
```
Columnas disponibles: ['producto', 'categoría', 'unidades', 'precio_unitario', 'descuento_pct', 'total_neto']
   producto  categoría  total_neto
0     Mouse  Periféricos     24273.0
1   Teclado  Periféricos     30381.0
```

---

## Bloque 2: Agrupar y ordenar el resumen por categoría

```python
# groupby agrupa todas las filas que comparten la misma categoría.
# .sum() suma los totales netos de cada grupo.
# sort_values ordena de mayor a menor para que el gráfico sea más legible.
resumen = (
    df.groupby("categoría", as_index=False)["total_neto"]
    .sum()
    .sort_values("total_neto", ascending=False)
)

print(resumen)
```

**¿Qué hace este bloque?**
Colapsa las filas individuales de ventas en un resumen de una fila por categoría, sumando todos los totales netos de cada grupo. El resultado es una tabla pequeña y manejable, lista para graficar.

**¿Por qué se escribe así y no de otra forma?**
`as_index=False` mantiene `categoría` como columna normal en lugar de convertirla en índice, lo que facilita trabajar con el resultado. Ordenar antes de graficar evita que el docente o el analista tenga que interpretar barras en orden aleatorio, que es cognitivamente más difícil.

**Resultado esperado:**
```
       categoría    total_neto
2        Monitores  18450000.0
0        Periféricos  9320000.0
1        Accesorios   4150000.0
```

---

## Bloque 3: Crear el gráfico de barras con configuración básica

```python
# figure() define el tamaño del gráfico en pulgadas (ancho, alto).
plt.figure(figsize=(8, 4))

# bar() recibe las categorías (eje x) y los valores (eje y).
plt.bar(resumen["categoría"], resumen["total_neto"], color="steelblue")

# Etiquetas y título hacen el gráfico autoexplicativo.
plt.title("Ventas netas por categoría")
plt.ylabel("CLP")
plt.xlabel("Categoría")

# rotation=20 evita que las etiquetas largas se superpongan.
plt.xticks(rotation=20, ha="right")

# tight_layout ajusta los márgenes automáticamente para que nada se corte.
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?**
Genera el gráfico de barras a partir del resumen. Cada llamada de configuración (`title`, `ylabel`, `xticks`, `tight_layout`) responde a un problema concreto de legibilidad.

**¿Por qué se escribe así y no de otra forma?**
En exploración rápida se puede omitir título y etiquetas, pero en un análisis que se comparte con otras personas esas líneas son obligatorias. `tight_layout()` es especialmente importante: sin él, las etiquetas del eje x suelen quedar cortadas al exportar la imagen.

**Resultado esperado:**
```
[Gráfico de barras horizontales con Monitores como la barra más alta,
seguido de Periféricos y Accesorios, ordenadas de mayor a menor]
```

---

## Bloque 4: Comparar dos dimensiones — ventas por sucursal y categoría

```python
# Pregunta exploratoria: ¿qué categoría vende más en cada sucursal?
# Agrupamos por dos columnas simultáneamente.
resumen2 = (
    df.groupby(["sucursal", "categoría"], as_index=False)["total_neto"]
    .sum()
)

# Graficamos solo la sucursal "Norte" para no saturar el gráfico.
norte = resumen2[resumen2["sucursal"] == "Norte"].sort_values("total_neto", ascending=False)

plt.figure(figsize=(7, 4))
plt.bar(norte["categoría"], norte["total_neto"], color="coral")
plt.title("Ventas netas por categoría — Sucursal Norte")
plt.ylabel("CLP")
plt.xticks(rotation=15, ha="right")
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?**
Introduce un `groupby` con dos columnas para cruzar sucursal y categoría. Luego filtra una sola sucursal para crear un gráfico manejable. Este patrón (agrupar, filtrar, graficar) se repite en la mayoría de los análisis exploratorios reales.

**¿Por qué se escribe así y no de otra forma?**
Graficar todas las sucursas a la vez en un solo gráfico de barras produce un resultado ilegible. El patrón correcto es filtrar primero y, si es necesario comparar sucursales, usar subgráficos (`plt.subplots`) o una librería como seaborn con `hue`.

**Resultado esperado:**
```
[Gráfico de barras para la Sucursal Norte mostrando las categorías
ordenadas de mayor a menor venta neta]
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| El gráfico muestra una barra por cada fila en lugar de por categoría | Se graficó el DataFrame completo sin agrupar previamente | Aplicar `groupby().sum()` antes de llamar a `plt.bar()` |
| Las etiquetas del eje x se superponen | Las cadenas de texto son largas y el gráfico es estrecho | Agregar `plt.xticks(rotation=45, ha="right")` o aumentar `figsize` |
| `ValueError: x and y must have same first dimensión` | Las series pasadas a `plt.bar()` tienen longitudes distintas | Verificar que `resumen["categoría"]` y `resumen["total_neto"]` provienen del mismo DataFrame y tienen el mismo número de filas |
| El gráfico aparece vacío o en blanco | Se llamó a `plt.show()` antes de configurar el gráfico, o en un contexto donde el backend no soporta ventanas | En Jupyter usar `%matplotlib inline` al inicio del notebook; en scripts verificar que `plt.show()` esté al final |
