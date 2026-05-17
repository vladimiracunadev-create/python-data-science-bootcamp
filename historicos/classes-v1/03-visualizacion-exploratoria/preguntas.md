# ❓ Preguntas de evaluación — Clase 03: Visualización exploratoria

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Cuál es la diferencia entre una visualización exploratoria y una visualización explicativa? ¿En qué momento del análisis se usa cada una?

2. ¿Por qué es necesario agrupar y resumir los datos antes de graficarlos? ¿Qué problema ocurre si gráficas directamente todas las filas de un dataset de ventas con miles de registros?

3. ¿Cuándo es más adecuado usar un gráfico de barras en lugar de un gráfico de líneas? Da un ejemplo concreto de cada caso usando datos de una tienda.

4. ¿Qué significa que un gráfico "responde una pregunta"? ¿Cómo sabes si el gráfico que creaste es adecuado para la pregunta que te hiciste?

5. ¿Por qué se recomienda ordenar las barras de mayor a menor en un gráfico de categorías? ¿Qué facilita visualmente ese orden?

## 💻 Preguntas de código

1. ¿Qué hace el siguiente bloque paso a paso? ¿Qué pasaría si se omitiera `.sort_values()`?

```python
resumen = (
    df.groupby("categoría")["total_neto"]
    .sum()
    .sort_values(ascending=False)
)
plt.bar(resumen.index, resumen.values)
```

2. ¿Cuál es el error en este código y qué gráfico incorrecto produciría?

```python
df["total_neto"] = df["unidades"] * df["precio_unitario"]
plt.bar(df["categoría"], df["total_neto"])
plt.title("Ventas por categoría")
plt.show()
```

3. ¿Qué hace cada línea de configuración del siguiente bloque? ¿Cuáles omitirías si el gráfico es solo para exploración personal?

```python
plt.figure(figsize=(8, 4))
plt.bar(resumen["categoría"], resumen["total_neto"])
plt.title("Ventas netas por categoría")
plt.ylabel("CLP")
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()
```

4. El siguiente código produce un gráfico pero resulta difícil de leer. ¿Por qué y cómo lo mejorarías?

```python
plt.bar(df["producto"], df["precio_unitario"])
plt.show()
```

## 🔗 Preguntas integradoras

1. Una gerente de ventas te pide "un gráfico que muestre cómo van las ventas". ¿Qué preguntas le harías antes de escribir una sola línea de código? ¿Por qué esas preguntas son necesarias?

2. Tienes un dataset de ventas por sucursal y por mes. ¿Qué tres preguntas exploratorias distintas formularías y qué tipo de gráfico usarías para cada una?

3. ¿Cómo se relaciona la decisión de agrupar los datos (por categoría, por sucursal, por mes) con la pregunta de negocio que intentas responder? ¿Qué riesgo existe si eliges la agrupación incorrecta?
