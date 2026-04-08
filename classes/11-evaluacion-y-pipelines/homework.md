# Tarea — Clase 11: Evaluación robusta y Pipelines de ML

## Consigna

Construye un Pipeline completo para predecir el **descuento aplicado** (regresión) o la **sucursal con mayor renta** (clasificación) usando `ventas_tienda.csv`.

## Pasos requeridos

1. **Exploración**
   - Identifica columnas numéricas y categóricas.
   - ¿Hay valores nulos? Decide cómo imputarlos dentro del Pipeline.

2. **Pipeline**
   - Usa `ColumnTransformer` para preprocesar por separado numéricas y categóricas.
   - Incluye `SimpleImputer` en la etapa numérica.
   - Incluye el modelo al final del Pipeline.

3. **Evaluación robusta**
   - Aplica validación cruzada con k=5.
   - Reporta media y desviación estándar del score.

4. **Búsqueda de hiperparámetros**
   - Usa `GridSearchCV` con al menos 2 hiperparámetros y 3 valores cada uno.
   - Muestra los mejores parámetros.

5. **Conclusión**
   - ¿El Pipeline mejoró el resultado respecto a la clase anterior?
   - ¿Qué hiperparámetro tuvo más impacto?

## Entrega

Notebook `.ipynb` con todas las celdas ejecutadas, incluyendo la tabla de resultados del GridSearchCV.
