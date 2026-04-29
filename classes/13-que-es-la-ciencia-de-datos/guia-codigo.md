# 💻 Guía de código — Clase 13: ¿Qué es la Ciencia de Datos?

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Importar las librerías esenciales

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

**¿Qué hace este bloque?**
Cada línea carga una librería externa y le asigna un alias corto:
- `import pandas as pd`: carga pandas con el alias `pd`. Desde aquí, `pd.algo` llama a funciones de pandas.
- `import numpy as np`: carga numpy con el alias `np`. Se usa para cálculos numéricos rápidos sobre arrays.
- `import matplotlib.pyplot as plt`: carga el módulo de graficación con el alias `plt`.

**¿Por qué se escribe así y no de otra forma?**
Los alias `pd`, `np` y `plt` son convenciones universales en la comunidad de ciencia de datos. Todo el mundo las usa igual, lo que hace que el código sea reconocible instantáneamente por cualquier profesional. No es obligatorio usar estos alias, pero sí es una buena práctica seguirlos.

**Resultado esperado:**
No produce salida visible en pantalla. Si no aparece ningún error, significa que las librerías están instaladas correctamente y listas para usar.

---

## Bloque 2: Cargar y explorar un dataset

```python
# Cargar el archivo CSV en un DataFrame
df = pd.read_csv("ventas_tienda.csv")

# Ver el tamaño del dataset
print("Dimensiones:", df.shape)

# Ver las primeras filas
print("\nPrimeras 5 filas:")
df.head()
```

**¿Qué hace este bloque?**
- `pd.read_csv("ventas_tienda.csv")`: lee el archivo CSV y lo convierte en un DataFrame, que es una tabla con filas y columnas.
- `df.shape`: devuelve una tupla `(filas, columnas)` que indica el tamaño total del dataset.
- `df.head()`: muestra las primeras 5 filas del DataFrame de forma visual en el notebook. Se puede pasar un número: `df.head(10)` muestra 10.

**¿Por qué se escribe así y no de otra forma?**
`read_csv` es la función más usada para cargar datos porque el CSV es el formato más común en ciencia de datos. Usar `.head()` al inicio es una práctica clave: antes de analizar cualquier dataset, siempre hay que "echar un vistazo" para entender qué columnas hay y cómo lucen los datos.

**Resultado esperado:**
Una tabla con las primeras 5 filas mostrando columnas como `fecha`, `producto`, `ventas`, `categoría`, entre otras. El `shape` podría ser algo como `(500, 6)`.

---

## Bloque 3: Inspeccionar tipos de datos y estadísticas

```python
# Tipos de datos por columna
print("Tipos de datos:")
print(df.dtypes)

# Resumen estadístico de columnas numéricas
print("\nResumen estadístico:")
df.describe()
```

**¿Qué hace este bloque?**
- `df.dtypes`: muestra el tipo de dato de cada columna: `int64` para enteros, `float64` para decimales, `object` para texto.
- `df.describe()`: calcula automáticamente estadísticas descriptivas para todas las columnas numéricas: conteo, media, desviación estándar, mínimo, cuartiles (25%, 50%, 75%) y máximo.

**¿Por qué se escribe así y no de otra forma?**
Revisar los tipos de datos es fundamental porque muchos errores vienen de tratar números como texto (tipo `object`) o viceversa. `describe()` te da en un solo comando una radiografía estadística del dataset, lo que ayuda a detectar valores atípicos o rangos inesperados antes de cualquier análisis.

**Resultado esperado:**
Una tabla con filas `count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, `max` para cada columna numérica. Por ejemplo, para `ventas` verías su promedio y el rango de valores.

---

## Bloque 4: Identificar valores nulos

```python
# Conteo de valores nulos por columna
print("Valores nulos por columna:")
print(df.isnull().sum())

# Porcentaje de nulos
print("\nPorcentaje de nulos (%):")
print((df.isnull().sum() / len(df) * 100).round(2))
```

**¿Qué hace este bloque?**
- `df.isnull()`: crea una tabla de `True`/`False` donde `True` indica que el valor está vacío o es nulo.
- `.sum()`: suma los `True` (que valen 1) por columna, dando el total de nulos en cada una.
- Dividir entre `len(df)` y multiplicar por 100 convierte el conteo en porcentaje relativo.

**¿Por qué se escribe así y no de otra forma?**
Los datos reales casi siempre tienen valores faltantes. Saber cuántos hay y en qué columnas es el primer paso para decidir cómo tratarlos: ¿eliminar las filas?, ¿rellenar con la media?, ¿dejarlos? Esta exploración inicial corresponde a la fase de "Comprensión de los Datos" en CRISP-DM.

**Resultado esperado:**
```
Valores nulos por columna:
fecha         0
producto      0
ventas        3
categoría     1
dtype: int64

Porcentaje de nulos (%):
fecha        0.00
producto     0.00
ventas       0.60
categoría    0.20
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `ModuleNotFoundError: No module named 'pandas'` | La librería no está instalada en el entorno actual | Ejecutar `pip install pandas` en la terminal y reiniciar el kernel |
| `FileNotFoundError: ventas_tienda.csv` | El archivo no está en la misma carpeta que el notebook | Verificar la ubicación con `import os; print(os.getcwd())` y mover el archivo |
| `UnicodeDecodeError` al leer un CSV | El archivo usa una codificación distinta (ej. latin-1) | Usar `pd.read_csv("archivo.csv", encoding="latin-1")` |
| `df.head` muestra texto en lugar de tabla | Se olvidaron los paréntesis al llamar la función | Escribir `df.head()` con los paréntesis al final |
| Columnas numéricas aparecen como tipo `object` | Los números tienen comas como separador decimal o texto mezclado | Usar `pd.to_numeric(df['columna'], errors='coerce')` para convertirlas |
