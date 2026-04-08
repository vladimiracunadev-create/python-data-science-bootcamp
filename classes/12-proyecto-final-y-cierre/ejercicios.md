# Checklist de entregables — Proyecto Final

## Dataset elegido

Indica cuál dataset usarás y el problema que resolverás:

- **Dataset:** _______________
- **Pregunta de negocio:** _______________
- **Tipo de problema:** Regresión / Clasificación

---

## Checklist de análisis exploratorio

- [ ] Dimensiones del dataset (`df.shape`)
- [ ] Tipos de datos (`df.dtypes`)
- [ ] Estadísticas descriptivas (`df.describe()`)
- [ ] Cantidad y porcentaje de valores nulos
- [ ] Distribución de la variable objetivo (histograma)
- [ ] Al menos una visualización de correlación (heatmap o scatterplot)
- [ ] Identificación de outliers (boxplot)

## Checklist de limpieza

- [ ] Valores nulos imputados o eliminados (con justificación)
- [ ] Tipos de datos corregidos si es necesario
- [ ] Variables nuevas creadas si agregan valor

## Checklist de modelado

- [ ] Train/test split (80/20, `random_state=42`)
- [ ] Pipeline con preprocesamiento + modelo
- [ ] Al menos 2 modelos comparados
- [ ] Métricas de evaluación reportadas
- [ ] El modelo supera la línea base

## Checklist de presentación

- [ ] Título claro del análisis
- [ ] Al menos 3 gráficos comunicativos (con título y etiquetas)
- [ ] Conclusiones en lenguaje de negocio (sin jerga técnica)
- [ ] Limitaciones explicitadas
- [ ] Recomendaciones concretas para el negocio

---

## Formato de entrega

- Notebook `.ipynb` con todas las celdas ejecutadas
- Todas las visualizaciones visibles
- Máximo 15 minutos de presentación oral
