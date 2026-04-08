# 📝 Tarea â€” Clase 10: Modelos Supervisados â€” ClasificaciÃ³n

> 📝 Trabajo autonomo para consolidar lo visto y practicar con mas calma.


## 🎯 Consigna

Usando `datasets/estudiantes.csv`, construye un clasificador que prediga si un estudiante **aprueba o reprueba** (nota final â‰¥ 60 = aprueba).

## ✅ Pasos requeridos

1. **PreparaciÃ³n**
   - Crea la columna target: `aprobado = (nota_final >= 60).astype(int)`
   - Selecciona al menos 3 features relevantes.
   - Divide en train/test 80/20.

2. **Modelado**
   - Entrena un `DecisionTreeClassifier(max_depth=4)`.
   - Entrena un `LogisticRegression()`.

3. **EvaluaciÃ³n**
   - Genera el `classification_report` para ambos.
   - Muestra la matriz de confusiÃ³n para el mejor modelo.

4. **AnÃ¡lisis**
   - Â¿QuÃ© modelo detecta mejor a los estudiantes en riesgo?
   - Â¿QuÃ© variable tiene mayor importancia? (`model.feature_importances_`)

5. **ReflexiÃ³n**
   - Â¿QuÃ© consecuencias tendrÃ­a un falso negativo en este contexto? (un estudiante en riesgo que no fue detectado)

## 📦 Entrega

Notebook `.ipynb` con todas las celdas ejecutadas y al menos un pÃ¡rrafo de conclusiones.
