# Tarea — Clase 09: Introducción al Machine Learning

## Consigna

Usando el dataset `datasets/estudiantes.csv`, construye un modelo de regresión que prediga la **nota final** de cada estudiante.

## Pasos requeridos

1. **Exploración inicial**
   - ¿Cuántos estudiantes hay? ¿Cuántas variables?
   - ¿Hay valores nulos? ¿Cómo los manejarás?
   - Visualiza la distribución de la variable objetivo.

2. **Selección de features**
   - Elige al menos 2 variables predictoras y justifica tu elección.
   - Excluye variables que causarían data leakage.

3. **Modelado**
   - Divide en train/test (80/20) con `random_state=42`.
   - Entrena una `LinearRegression`.
   - Calcula MAE y RMSE.

4. **Comparación con línea base**
   - Compara tu modelo contra predecir siempre el promedio.

5. **Conclusión**
   - ¿Qué variable tiene mayor influencia? (Revisa `model.coef_`)
   - ¿Qué mejorarías si tuvieras más datos?

## Entrega

Notebook `.ipynb` con resultados visibles (celdas ejecutadas). Máximo 2 páginas de análisis en texto.
