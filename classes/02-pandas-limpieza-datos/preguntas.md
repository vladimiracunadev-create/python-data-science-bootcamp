# ❓ Preguntas de evaluación — Clase 02: Pandas y limpieza de datos

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Qué es un DataFrame en pandas y en qué se diferencia de una lista de diccionarios en Python puro?

2. ¿Por qué el primer paso al recibir un CSV nunca debería ser graficar ni calcular promedios, sino inspeccionarlo? ¿Qué problemas podría pasar por alto si se salta esa etapa?

3. ¿Cuál es la diferencia entre un valor nulo (`NaN`) y un valor vacío (`""`) en una tabla? ¿Por qué es importante distinguirlos?

4. ¿Qué significa "estandarizar" una columna de texto? Da un ejemplo concreto usando la columna `medio_pago` de un dataset de ventas.

5. ¿Cuándo conviene eliminar filas con valores nulos y cuándo conviene imputarlos? ¿Qué criterio usarías para decidir?

## 💻 Preguntas de código

1. ¿Qué información entrega cada una de las tres líneas siguientes y cuál de las tres usarías primero al recibir un CSV desconocido?

```python
print(df.head())
print(df.info())
print(df.isna().sum())
```

2. ¿Cuál es el error en este código y cuál sería el resultado incorrecto que produciría?

```python
df["total"] = df["unidades"] * df["precio"]
df_limpio = df.dropna()
print(df_limpio["total"].sum())
```

3. ¿Qué hace `str.strip()` y por qué es importante aplicarlo antes de filtrar o agrupar por una columna de texto?

```python
df["medio_pago"] = df["medio_pago"].str.strip().str.lower()
```

4. El siguiente código arroja un resultado sorprendente. ¿Por qué y cómo se corrige?

```python
df["precio"] = df["precio"].fillna(0)
promedio = df["precio"].mean()
print("Precio promedio:", promedio)
```

## 🔗 Preguntas integradoras

1. Un colega te entrega un CSV con datos de clientes y te dice "ya está limpio". ¿Qué pasos seguirías de todas formas antes de usarlo en un análisis? ¿Por qué no confiarías ciegamente en esa afirmación?

2. Imagina que la columna `fecha` llegó como texto (`"2024-03-15"`) en lugar de tipo `datetime`. ¿Qué problemas concretos aparecerían si intentas calcular ventas por mes sin corregirlo?

3. ¿Cómo se relaciona la limpieza documentada con la confianza que un equipo puede depositar en los resultados de un análisis? ¿Qué riesgo existe si se limpia sin registrar las decisiones tomadas?
