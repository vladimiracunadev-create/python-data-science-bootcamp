# ❓ Preguntas de evaluación — Clase 06: Texto, fechas y transformaciones

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Por qué pandas no reconoce automáticamente una columna de fechas al leer un CSV? ¿Qué pasos hay que dar para que la columna sea tratada como fecha real?
2. ¿Cuál es la diferencia entre `df["fecha"].dt.month` y `df["fecha"].dt.to_period("M")`? ¿En qué situación usarías cada uno?
3. ¿Qué problema concreto resuelve `str.strip().str.lower()` al normalizar texto? Pon un ejemplo de dato que causaría duplicados si no se normaliza.
4. ¿Qué significa crear una "columna derivada"? ¿Por qué es preferible crearla en lugar de modificar la columna original?
5. ¿Qué ventaja tiene guardar el resultado de una transformación en una nueva columna del DataFrame en lugar de imprimirlo y descartarlo?

## 💻 Preguntas de código

1. ¿Qué hace exactamente este bloque y qué imprime al final?
```python
import pandas as pd
df = pd.read_csv("datasets/ventas_tienda.csv")
df["fecha"] = pd.to_datetime(df["fecha"])
df["mes"] = df["fecha"].dt.to_period("M").astype(str)
print(df["mes"].value_counts().head(3))
```

2. El siguiente código intenta obtener el día de la semana pero produce un error. ¿Cuál es el problema y cómo se soluciona?
```python
df["dia_semana"] = df["fecha"].day_name()   # ¿Qué falta aquí?
```

3. ¿Qué devuelve `df["producto"].str.strip().str.lower().nunique()` si antes había productos con nombres como `"Laptop"`, `" laptop"`, `"LAPTOP"`?

4. Escribe el código necesario para crear una columna `"trimestre"` a partir de la columna `"fecha"` ya convertida a datetime.

## 🔗 Preguntas integradoras

1. Si quisieras hacer un gráfico de barras con el total de ventas por día de la semana, ¿qué columnas necesitarías crear con las técnicas de esta clase antes de poder graficar?
2. ¿Cómo se conectan las transformaciones de esta clase con el mini proyecto guiado de la clase 07? ¿Qué pasa si el proyecto comienza sin limpiar texto ni convertir fechas?
3. Tienes una columna `"ciudad"` con valores como `"Lima"`, `" lima"`, `"LIMA"`, `"Lima "`. ¿Qué transformación aplicarías y qué resultado obtendrías? ¿Cuántos valores únicos habría antes y después?
