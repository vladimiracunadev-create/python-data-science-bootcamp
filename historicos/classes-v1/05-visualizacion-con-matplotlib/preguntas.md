# ❓ Preguntas de evaluación — Clase 05: Visualización con matplotlib

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Cuál es la diferencia entre usar `plt.plot()` directamente y usar `fig, ax = plt.subplots()`? ¿Por qué la segunda forma da más control?
2. ¿Qué representa el objeto `Figure` y qué representa el objeto `Axes` en matplotlib? ¿Puedes tener varios `Axes` dentro de una sola `Figure`?
3. ¿Para qué sirve `plt.tight_layout()` y cuándo es importante usarlo?
4. ¿Qué impacto tiene un gráfico sin etiquetas en los ejes cuando lo ve alguien que no participó en el análisis?
5. ¿Cuándo conviene rotar las etiquetas del eje X? ¿Qué parámetro se usa para hacerlo?

## 💻 Preguntas de código

1. ¿Qué imprime o muestra el siguiente código? ¿Qué cambiarías para mejorar su legibilidad?
```python
import matplotlib.pyplot as plt
meses = ["Ene", "Feb", "Mar", "Abr"]
valores = [120, 95, 140, 110]
plt.plot(meses, valores)
plt.show()
```

2. El siguiente bloque tiene un error conceptual: ¿cuál es y cómo lo corriges?
```python
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(df["mes"], df["clientes_activos"])
plt.title("Clientes activos por mes")   # ¿Es correcto este uso?
plt.xlabel("Mes")
plt.ylabel("Clientes")
plt.show()
```

3. ¿Qué hace el parámetro `alpha=0.2` en `ax.grid(alpha=0.2)`? ¿Qué pasaría si lo cambias a `alpha=1`?

4. ¿Cómo agregarías una línea horizontal de referencia en el valor 100 al gráfico de clientes activos? Escribe la línea de código correspondiente.

## 🔗 Preguntas integradoras

1. En el dataset `retencion_clientes.csv` tienes la columna `mes` como texto (ej. `"2024-01"`). ¿Qué podrías hacer antes de graficar para que el eje X se vea ordenado cronológicamente y no alfabéticamente?
2. Si tuvieras que mostrar en el mismo gráfico tanto los clientes activos como los clientes perdidos por mes, ¿qué cambios harías al código de esta clase? ¿Qué elementos visuales agregarías para distinguir ambas series?
3. ¿Cómo conecta esta clase con la siguiente, que trabaja con fechas y transformaciones? ¿Qué datos necesitarías transformar para mejorar los gráficos que ya sabes hacer?
