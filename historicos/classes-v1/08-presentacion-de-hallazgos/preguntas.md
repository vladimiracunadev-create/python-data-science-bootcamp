# ❓ Preguntas de evaluación — Clase 08: Presentación de hallazgos

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Qué diferencia hay entre un hallazgo y una conclusión ejecutiva? ¿Por qué no es suficiente con mostrar el dato?
2. ¿Qué significa "storytelling con datos"? ¿Cuáles son los tres elementos que debe tener una historia de análisis bien construida?
3. ¿Por qué la elección del gráfico afecta el mensaje que se transmite? Da un ejemplo donde un gráfico de línea y uno de barras comunicarían cosas distintas con los mismos datos.
4. ¿Qué es un resumen ejecutivo en el contexto del análisis de datos? ¿A quién va dirigido y qué información debe incluir obligatoriamente?
5. ¿Cómo sabes si tu visualización "sostiene el mensaje"? ¿Qué preguntas te harías antes de incluirla en una presentación?

## 💻 Preguntas de código

1. El siguiente bloque construye un resumen ejecutivo en texto. ¿Qué agregarías para que el hallazgo sea más preciso e incluya el valor numérico concreto?

```python
hallazgo     = "La categoría Accesorios concentra el mayor ingreso neto del período."
evidencia    = "El resumen por categoría la ubica en el primer lugar del ranking."
recomendacion = "Conviene revisar margen, stock y campañas antes de ampliar la oferta."

print(hallazgo)
print(evidencia)
print(recomendacion)
```

2. ¿Qué hace `ax.annotate()` en el siguiente bloque y cuándo es útil en una presentación de hallazgos?

```python
ax.annotate(
    "Pico máximo",
    xy=(pico_x, pico_y),
    xytext=(pico_x + 1, pico_y + 50),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10,
    color="red"
)
```

3. ¿Qué diferencia produce usar `color="tomato"` vs. `color="steelblue"` en el gráfico de la categoría destacada? ¿Qué principio de visualización aplica?

4. ¿Qué produce el siguiente bloque y por qué es útil para presentar hallazgos a una audiencia no técnica?

```python
ranking["porcentaje"] = (ranking["ingreso_neto_total"] / ranking["ingreso_neto_total"].sum() * 100).round(1)
print(ranking[["categoría", "ingreso_neto_total", "porcentaje"]])
```

## 🔗 Preguntas integradoras

1. Tienes el ranking de categorías del mini proyecto de la clase 07. ¿Cómo estructurarías una presentación de 3 diapositivas con ese resultado? ¿Qué va en cada diapositiva?
2. ¿Por qué un análisis técnicamente correcto puede no tener impacto si no se comunica bien? Describe una situación concreta donde esto podría ocurrir en un contexto profesional.
3. ¿Qué cambiarías en un gráfico de barras estándar para que comunique claramente la categoría ganadora sin que el lector tenga que leer todos los valores?
