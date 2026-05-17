# 💻 Guía de código — Clase 04: Estadística descriptiva

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Cargar los datos y calcular medidas de tendencia central

```python
import pandas as pd

# Cargamos el dataset de estudiantes con columnas de asistencia y nota.
df = pd.read_csv("datasets/estudiantes.csv", encoding="utf-8")

# Seleccionamos la columna de interés como una Serie.
asistencia = df["asistencia_pct"]

# Calculamos las tres medidas de tendencia central más importantes.
media    = asistencia.mean()
mediana  = asistencia.median()
moda     = asistencia.mode()[0]  # mode() devuelve una Serie; tomamos el primer valor.

print(f"Media:   {media:.1f}%")
print(f"Mediana: {mediana:.1f}%")
print(f"Moda:    {moda:.1f}%")
```

**¿Qué hace este bloque?**
Carga el dataset y calcula las tres medidas de tendencia central de la columna `asistencia_pct`. Imprime los tres valores formateados con un decimal para facilitar la comparación directa entre ellos.

**¿Por qué se escribe así y no de otra forma?**
Calcular las tres medidas juntas y compararlas en pantalla es la práctica correcta: si media y mediana difieren significativamente, hay valores extremos que están "tirando" la media. Calcular solo la media sin la mediana puede llevar a conclusiones incorrectas sobre el grupo.

**Resultado esperado:**
```
Media:   81.3%
Mediana: 85.0%
Moda:    90.0%
```

---

## Bloque 2: Medir la dispersión — desviación estándar y rango

```python
# La desviación estándar mide qué tan dispersos están los valores alrededor de la media.
# Un valor alto indica que el grupo es muy heterogéneo.
desviacion = asistencia.std()

# El rango es la distancia entre el valor mínimo y el máximo.
# Útil para detectar valores extremos, aunque no dice nada sobre la distribución intermedia.
rango = asistencia.max() - asistencia.min()

print(f"Desviación estándar: {desviacion:.1f}%")
print(f"Rango:               {rango:.1f}%")
print(f"Mínimo:              {asistencia.min():.1f}%")
print(f"Máximo:              {asistencia.max():.1f}%")
```

**¿Qué hace este bloque?**
Calcula la desviación estándar y el rango para medir cuánto varían los valores de asistencia entre estudiantes. Una desviación alta combinada con un rango amplio sugiere que hay estudiantes con situaciones muy distintas dentro del mismo grupo.

**¿Por qué se escribe así y no de otra forma?**
La desviación estándar y el rango se complementan: el rango muestra los extremos, la desviación estándar muestra la dispersión típica. Presentar solo uno de los dos puede dar una imagen incompleta. Por ejemplo, un rango de 80 puntos puede deberse a un único valor atípico, mientras que la desviación estándar revela si ese caso es aislado o generalizado.

**Resultado esperado:**
```
Desviación estándar: 14.2%
Rango:               65.0%
Mínimo:              25.0%
Máximo:              90.0%
```

---

## Bloque 3: Resumen completo con describe()

```python
# describe() entrega en una sola llamada las medidas más relevantes.
# count: cuántos valores no nulos hay (útil para detectar faltantes)
# mean: media
# std: desviación estándar
# min / max: valores extremos
# 25%, 50%, 75%: percentiles (el 50% equivale a la mediana)
resumen = asistencia.describe().round(1)
print(resumen)
```

**¿Qué hace este bloque?**
Genera un resumen estadístico completo de la columna de asistencia en una sola línea. El método `describe()` es la primera herramienta de exploración numérica en cualquier análisis.

**¿Por qué se escribe así y no de otra forma?**
`describe()` es más eficiente que calcular cada medida por separado durante la exploración inicial. El `.round(1)` mejora la legibilidad al reducir decimales innecesarios. En un análisis formal, después de este paso se calculan medidas específicas con más detalle si es necesario.

**Resultado esperado:**
```
count     35.0
mean      81.3
std       14.2
min       25.0
25%       75.0
50%       85.0
75%       90.0
max       90.0
Name: asistencia_pct, dtype: float64
```

---

## Bloque 4: Comparar estadísticas entre grupos con groupby

```python
# Agrupamos por sección para comparar el rendimiento de distintos grupos.
# agg() permite calcular varias métricas al mismo tiempo con nombres explícitos.
resumen_por_seccion = (
    df.groupby("sección")["asistencia_pct"]
    .agg(
        media=("mean"),
        mediana=("median"),
        desviacion=("std"),
        n_estudiantes=("count"),
    )
    .round(1)
)

print("Asistencia por sección:")
print(resumen_por_seccion)
```

**¿Qué hace este bloque?**
Calcula la media, mediana, desviación estándar y número de estudiantes de la columna `asistencia_pct` para cada sección del curso. El resultado es una tabla que permite comparar grupos de forma directa.

**¿Por qué se escribe así y no de otra forma?**
Usar `agg()` con nombres explícitos produce una tabla limpia con columnas descriptivas, en lugar de una con nombres genéricos como `<lambda>`. Esto hace que el resultado sea fácil de leer y de presentar. El patrón `groupby + agg` es el más común en análisis descriptivo por segmento en contextos reales.

**Resultado esperado:**
```
Asistencia por sección:
         media  mediana  desviacion  n_estudiantes
sección
A         84.2     87.0        11.5           18.0
B         77.8     81.0        17.4           17.0
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| La media es mucho más baja de lo esperado | Se imputaron nulos con 0 antes de calcular (`fillna(0)`), lo que baja artificialmente el promedio | Calcular la media antes de imputar, o excluir los nulos con `dropna()` si el análisis lo permite |
| `mode()` devuelve varios valores y causa error al acceder con `[0]` | El dataset tiene varios valores igualmente frecuentes (empate de moda) | Usar `mode()[0]` para tomar el primero, o verificar si hay empate con `len(asistencia.mode()) > 1` |
| `agg()` produce un error de sintaxis | La sintaxis de `agg()` con nombres usando tuplas cambió entre versiones de pandas | Usar la forma `agg(media=("columna", "mean"))` con paréntesis, válida en pandas 0.25+ |
| `describe()` excluye columnas de texto | Por defecto, `describe()` solo analiza columnas numéricas | Usar `df.describe(include="all")` para incluir columnas de tipo objeto (texto) |
