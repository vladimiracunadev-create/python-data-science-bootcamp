# ❓ Preguntas de evaluación — Clase 07: Mini proyecto guiado

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Por qué es importante formular una pregunta concreta antes de comenzar a analizar datos? ¿Qué problemas genera empezar sin una pregunta definida?
2. ¿Qué significa "recortar" un DataFrame para armar la base de trabajo de un proyecto? ¿Por qué no se trabaja siempre con todas las columnas disponibles?
3. ¿Cuál es la secuencia lógica de un mini proyecto de análisis de datos? Describe los pasos desde la pregunta hasta la conclusión.
4. ¿Qué diferencia hay entre explorar datos libremente y seguir una secuencia de análisis orientada a una pregunta? ¿Cuáles son las ventajas de cada enfoque?
5. ¿Por qué se dice que el proyecto "ordena técnicas sueltas dentro de un proceso con sentido"? Da un ejemplo con las técnicas vistas en las clases anteriores.

## 💻 Preguntas de código

1. El siguiente bloque define la pregunta de análisis y recorta el DataFrame. ¿Qué hace `.copy()` y por qué es importante usarlo aquí?

```python
columnas = ["fecha", "sucursal", "categoría", "producto", "medio_pago", "total_neto"]
proyecto = df[columnas].copy()
```

2. ¿Qué calcula la siguiente línea y qué tipo de dato devuelve? ¿Cuándo podría dar un resultado incorrecto si no se hicieron las transformaciones previas?

```python
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])
```

3. ¿Qué produce este bloque y para qué sirve dentro de un proyecto guiado?

```python
resumen = proyecto.groupby("categoría")["total_neto"].sum().sort_values(ascending=False)
print(resumen)
```

4. Identifica qué paso del pipeline falta en la siguiente secuencia y explica por qué es necesario:

```python
df = pd.read_csv("datasets/ventas_tienda.csv")
# ¿Qué falta aquí antes de crear total_neto?
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])
proyecto = df[["fecha", "categoría", "total_neto"]].copy()
```

## 🔗 Preguntas integradoras

1. ¿Cómo usarías en este mini proyecto las transformaciones de texto y fechas de la clase 06? ¿En qué parte del pipeline encajan?
2. Si la pregunta del proyecto fuera "¿En qué día de la semana se concentran las ventas más altas?", ¿qué columnas necesitarías crear antes de agrupar los datos? ¿Qué gráfico usarías para comunicar el resultado?
3. Al finalizar el análisis, tienes un ranking de categorías por ingreso neto. ¿Cómo convertirías ese resultado en un hallazgo comunicable para la clase 08? ¿Qué agregarías al DataFrame o al gráfico para que el mensaje sea claro?
