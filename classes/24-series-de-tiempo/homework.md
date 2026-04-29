# 🏠 Homework — Clase 24: Series de tiempo — datos temporales

> Entrega tu notebook con todas las celdas ejecutadas y celdas Markdown explicativas en cada sección.

---

## Contexto del problema

La tienda quiere un informe mensual de ventas que responda tres preguntas:
1. ¿Cómo han evolucionado las ventas en el tiempo? (tendencia)
2. ¿Hay meses del año que siempre venden más o menos? (estacionalidad)
3. ¿Cuánto esperamos vender el próximo mes? (pronóstico)

Tu tarea es construir ese informe con Python usando el dataset `ventas_tienda.csv`.

---

## Parte 1 — Preparación y exploración temporal (2 puntos)

1. Carga `datasets/ventas_tienda.csv`
2. Identifica la columna de fecha, conviértela con `pd.to_datetime()` y ponla como índice
3. Responde en Markdown:
   - ¿Qué rango de fechas cubre el dataset?
   - ¿Cuántos meses distintos hay?
   - ¿Hay algún mes sin datos?
4. Crea una tabla resumen:

```python
resumen = df.resample('M').agg({col_ventas: ['sum', 'mean', 'max', 'count']})
```

---

## Parte 2 — Visualización de la serie de tiempo (3 puntos)

1. gráfica las ventas diarias (o en la frecuencia disponible) con matplotlib
2. Superpón encima el promedio móvil de 7 días Y el de 30 días con colores distintos
3. El gráfico debe tener:
   - Título descriptivo
   - Ejes etiquetados con unidades
   - Leyenda clara
   - Fechas en el eje X legibles (usa `plt.xticks(rotation=45)`)
4. (Bonus) Agrega una banda de confianza con `fill_between` entre la media - desv y la media + desv

**Criterio de calidad:** ¿El gráfico se puede incluir en un informe ejecutivo sin modificaciones?

---

## Parte 3 — Tendencia y comparación mensual (2 puntos)

1. Agrega las ventas por mes con `resample('M').sum()`
2. Crea dos gráficos en una figura (subplots):
   - **Gráfico 1**: ventas mensuales como barras + línea de tendencia
   - **Gráfico 2**: promedio por mes del año (ej: todos los eneros, todos los febreros) para ver estacionalidad
   
```python
# Promedio por mes del año (para ver estacionalidad)
df['mes_num'] = df.index.month
promedio_por_mes = df.groupby('mes_num')[col_ventas].mean()
promedio_por_mes.index = ['Ene','Feb','Mar','Abr','May','Jun',
                           'Jul','Ago','Sep','Oct','Nov','Dic'][:len(promedio_por_mes)]
```

3. Escribe en Markdown:
   - ¿Cuáles son los 3 meses con mayores ventas?
   - ¿Hay evidencia de estacionalidad?

---

## Parte 4 — Descomposición y pronóstico (2 puntos)

1. Aplica `seasonal_decompose` a las ventas mensuales
2. Interpreta en Markdown cada uno de los 4 componentes del gráfico:
   - Observado
   - Tendencia
   - Estacional
   - Residuo
3. Calcula tres pronósticos para el siguiente mes:
   - Naive (último valor)
   - Media móvil de los últimos 3 meses
   - Seasonal naive (mismo mes del año anterior, si hay suficientes datos)
4. Elige cuál usarías y justifica

---

## Parte 5 — Conclusión ejecutiva (1 punto)

Escribe un párrafo de 6-8 oraciones como si fueras el analista de datos explicándole los hallazgos al gerente de la tienda. Incluye:
- El comportamiento general de las ventas (tendencia)
- Si hay meses con mejor desempeño (estacionalidad)
- Tu pronóstico para el mes siguiente y por qué
- Una recomendación de negocio basada en el análisis

---

## Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Fechas correctamente procesadas y tabla resumen | 2 |
| Gráfico de serie + promedios móviles profesional | 3 |
| Análisis de tendencia + gráfico de estacionalidad | 2 |
| Descomposición + 3 pronósticos con justificación | 2 |
| Conclusión ejecutiva | 1 |
| **Total** | **10** |

---

## Bonus (punto extra)

Repite el análisis con `retencion_clientes.csv`. Compara la tendencia de retención con la tendencia de ventas. ¿Hay correlación? ¿Cuándo las ventas suben, ¿la retención también sube?

---

## Entrega

- Archivo: `homework_clase24_tunombre.ipynb`
- Todas las celdas ejecutadas sin errores
- Mínimo 4 celdas Markdown explicativas
- Los gráficos deben verse bien y tener título y ejes
