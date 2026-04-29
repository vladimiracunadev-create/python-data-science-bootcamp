# ❓ Preguntas de evaluación — Clase 04: Estadística descriptiva

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Cuál es la diferencia entre la media y la mediana? ¿En qué tipo de distribución de datos divergen más y por qué?

2. ¿Qué información aporta la desviación estándar que no aporta la media sola? Da un ejemplo concreto usando porcentajes de asistencia de estudiantes.

3. ¿Por qué se dice que "la estadística descriptiva resume poblaciones"? ¿Qué se pierde al resumir y cómo se compensa esa pérdida?

4. ¿Qué es un valor atípico (outlier) y cómo puede afectar la media de un conjunto de datos? ¿La mediana tiene el mismo problema? Justifica tu respuesta.

5. ¿Cuándo conviene usar `describe()` de pandas en lugar de calcular cada medida por separado? ¿Qué columnas del resultado de `describe()` son más útiles para detectar problemas de calidad en los datos?

## 💻 Preguntas de código

1. ¿Qué imprime el siguiente bloque y qué conclusión puedes sacar de la diferencia entre los dos valores?

```python
asistencia = pd.Series([95, 92, 88, 45, 91, 90, 87, 93, 96, 10])
print("Media:", asistencia.mean().round(1))
print("Mediana:", asistencia.median())
```

2. ¿Cuál es el error conceptual en este código, aunque no produzca un error de Python?

```python
df["nota_promedio"] = df["nota"].fillna(0)
media = df["nota_promedio"].mean()
print("Nota promedio del curso:", media)
```

3. ¿Qué devuelve `describe()` y qué significa cada fila del resultado? Identifica cuál de ellas indica dispersión.

```python
resumen = df["asistencia_pct"].describe()
print(resumen)
```

4. ¿Qué hace el siguiente bloque y para qué sirve el resultado en un contexto pedagógico?

```python
grupos = df.groupby("sección")["nota"].agg(["mean", "median", "std"])
print(grupos)
```

## 🔗 Preguntas integradoras

1. El director de un colegio informa que "el promedio de notas del curso es 6.0 sobre 7.0". ¿Qué otras medidas pedirías antes de concluir que el curso le está yendo bien? ¿Por qué el promedio solo puede ser engañoso?

2. Una analista de datos reporta que "la desviación estándar de los salarios del equipo es $800.000". Sin saber la media, ¿puedes interpretar si eso es mucho o poco? ¿Qué medida adicional necesitas y por qué?

3. ¿Cómo se relaciona lo aprendido en esta clase con la clase 05 (visualización con matplotlib)? ¿Qué tipos de gráfico son especialmente útiles para representar la distribución y la dispersión de una variable numérica?
