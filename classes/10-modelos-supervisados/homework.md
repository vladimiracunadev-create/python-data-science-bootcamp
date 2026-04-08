# Tarea — Clase 10: Modelos Supervisados — Clasificación

## Consigna

Usando `datasets/estudiantes.csv`, construye un clasificador que prediga si un estudiante **aprueba o reprueba** (nota final ≥ 60 = aprueba).

## Pasos requeridos

1. **Preparación**
   - Crea la columna target: `aprobado = (nota_final >= 60).astype(int)`
   - Selecciona al menos 3 features relevantes.
   - Divide en train/test 80/20.

2. **Modelado**
   - Entrena un `DecisionTreeClassifier(max_depth=4)`.
   - Entrena un `LogisticRegression()`.

3. **Evaluación**
   - Genera el `classification_report` para ambos.
   - Muestra la matriz de confusión para el mejor modelo.

4. **Análisis**
   - ¿Qué modelo detecta mejor a los estudiantes en riesgo?
   - ¿Qué variable tiene mayor importancia? (`model.feature_importances_`)

5. **Reflexión**
   - ¿Qué consecuencias tendría un falso negativo en este contexto? (un estudiante en riesgo que no fue detectado)

## Entrega

Notebook `.ipynb` con todas las celdas ejecutadas y al menos un párrafo de conclusiones.
