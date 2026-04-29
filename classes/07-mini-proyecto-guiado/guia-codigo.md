# 💻 Guía de código — Clase 07: Mini proyecto guiado

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Definir la pregunta y preparar la base de trabajo

```python
import pandas as pd

# Cargamos el dataset de ventas
df = pd.read_csv("datasets/ventas_tienda.csv")

# La pregunta guía todo el proyecto — la escribimos explícitamente
pregunta = "¿Qué categoría concentra mayor ingreso neto en el período?"

# Calculamos el ingreso neto antes de recortar el DataFrame
# unidades * precio_unitario da el total bruto; el descuento reduce ese valor
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

# Recortamos solo las columnas necesarias para responder la pregunta
# .copy() evita el SettingWithCopyWarning al modificar el DataFrame más adelante
columnas = ["fecha", "sucursal", "categoría", "producto", "medio_pago", "total_neto"]
proyecto = df[columnas].copy()

print(pregunta)
print(proyecto.shape)
print(proyecto.head())
```

**¿Qué hace este bloque?** Carga los datos, calcula la métrica principal (`total_neto`) y recorta el DataFrame a las columnas relevantes para la pregunta definida.

**¿Por qué se escribe así y no de otra forma?** Escribir la pregunta como variable de texto fuerza a quien analiza a comprometerse con un objetivo antes de ejecutar código. `copy()` es necesario para evitar que pandas emita advertencias al modificar el DataFrame recortado posteriormente.

**Resultado esperado:**
```
¿Qué categoría concentra mayor ingreso neto en el período?
(1500, 6)
   fecha  sucursal   categoría    producto medio_pago  total_neto
0  2024-01-03  Norte  Electrónica  Laptop     Tarjeta     1260.0
...
```

---

## Bloque 2: Transformaciones de fecha y texto sobre la base del proyecto

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

columnas = ["fecha", "sucursal", "categoría", "producto", "medio_pago", "total_neto"]
proyecto = df[columnas].copy()

# Convertimos fecha a datetime para poder crear columnas derivadas
proyecto["fecha"] = pd.to_datetime(proyecto["fecha"])

# Columnas derivadas que amplían las preguntas posibles
proyecto["mes"]       = proyecto["fecha"].dt.to_period("M").astype(str)
proyecto["dia_semana"] = proyecto["fecha"].dt.day_name()

# Normalizamos texto para evitar duplicados de categoría
proyecto["categoría"] = proyecto["categoría"].str.strip().str.lower()
proyecto["producto"]  = proyecto["producto"].str.strip().str.lower()

# Verificamos el resultado
print(proyecto[["fecha", "mes", "dia_semana", "categoría", "total_neto"]].head())
print("\nCategorías únicas:", proyecto["categoría"].nunique())
```

**¿Qué hace este bloque?** Aplica sobre la base de trabajo las transformaciones de la clase 06: conversión de fechas, creación de columnas derivadas y normalización de texto.

**¿Por qué se escribe así y no de otra forma?** Las transformaciones se hacen sobre `proyecto` (ya recortado), no sobre `df` completo, para mantener el análisis acotado a la pregunta. Normalizar categorías aquí previene que el agrupamiento de la siguiente etapa cuente `"Electrónica"` y `"electronica"` como dos categorías distintas.

**Resultado esperado:**
```
        fecha      mes  dia_semana    categoría  total_neto
0  2024-01-03  2024-01    Wednesday  electrónica      1260.0
...
Categorías únicas: 5
```

---

## Bloque 3: Análisis — ranking de categorías por ingreso neto

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])

columnas = ["fecha", "sucursal", "categoría", "producto", "medio_pago", "total_neto"]
proyecto = df[columnas].copy()
proyecto["categoría"] = proyecto["categoría"].str.strip().str.lower()

# Agrupamos por categoría y sumamos el ingreso neto total
ranking = (
    proyecto
    .groupby("categoría")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
ranking.columns = ["categoría", "ingreso_neto_total"]

# Formateamos el valor para lectura humana
ranking["ingreso_neto_total_fmt"] = ranking["ingreso_neto_total"].apply(
    lambda x: f"${x:,.0f}"
)

print("Ranking de categorías por ingreso neto:")
print(ranking)
```

**¿Qué hace este bloque?** Responde directamente la pregunta del proyecto: agrupa por categoría, suma el ingreso neto y ordena de mayor a menor.

**¿Por qué se escribe así y no de otra forma?** El encadenamiento `.groupby().sum().sort_values().reset_index()` es compacto y produce un DataFrame limpio listo para graficar. `reset_index()` convierte el índice de agrupación en columna regular, necesario para pasarlo a matplotlib.

**Resultado esperado:**
```
Ranking de categorías por ingreso neto:
      categoría  ingreso_neto_total ingreso_neto_total_fmt
0   electrónica          285400.00              $285,400
1    accesorios          198700.00              $198,700
2          ropa          154200.00              $154,200
...
```

---

## Bloque 4: Visualización del resultado del proyecto

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])
proyecto = df[["categoría", "total_neto"]].copy()
proyecto["categoría"] = proyecto["categoría"].str.strip().str.lower()

ranking = (
    proyecto
    .groupby("categoría")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

# Gráfico de barras horizontales: mejor que verticales cuando las etiquetas son largas
fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(ranking["categoría"], ranking["total_neto"], color="steelblue")

# Invertimos el eje Y para que la categoría mayor quede arriba
ax.invert_yaxis()

ax.set_title("Ingreso neto por categoría — Mini proyecto")
ax.set_xlabel("Ingreso neto total ($)")
ax.set_ylabel("Categoría")
ax.grid(axis="x", alpha=0.2)
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?** Convierte el ranking en un gráfico de barras horizontales con el eje invertido para que la categoría de mayor ingreso aparezca en la parte superior.

**¿Por qué se escribe así y no de otra forma?** Las barras horizontales (`barh`) evitan que las etiquetas de categoría se superpongan. `invert_yaxis()` es necesario porque `barh` dibuja de abajo hacia arriba por defecto, lo cual es contraintuitivo para un ranking.

**Resultado esperado:**
```
Gráfico de barras horizontales con las categorías ordenadas
de mayor a menor ingreso neto, donde "electrónica" aparece
en la barra superior más larga.
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `SettingWithCopyWarning` al modificar el DataFrame recortado | Se modificó una vista del DataFrame original sin usar `.copy()` | Agregar `.copy()` al recortar: `proyecto = df[columnas].copy()` |
| El ranking muestra categorías duplicadas (ej. `"Ropa"` y `"ropa"`) | La columna de texto no fue normalizada antes de agrupar | Aplicar `.str.strip().str.lower()` antes del `groupby` |
| `KeyError` al calcular `total_neto` | La columna `descuento_pct` tiene un nombre distinto en el CSV | Verificar con `df.columns.tolist()` antes de operar |
| El gráfico de barras muestra el ranking al revés | `barh` dibuja de abajo hacia arriba por defecto | Agregar `ax.invert_yaxis()` después de crear el gráfico |
| `groupby` produce resultados distintos en cada ejecución | El orden del DataFrame cambia según la lectura del CSV | Siempre usar `.sort_values(ascending=False)` al final del agrupamiento |
