# 📝 Tarea â€” Clase 09: IntroducciÃ³n al Machine Learning

> 📝 Trabajo autonomo para consolidar lo visto y practicar con mas calma.


## 🎯 Consigna

Usando el dataset `datasets/estudiantes.csv`, construye un modelo de regresiÃ³n que prediga la **nota final** de cada estudiante.

## ✅ Pasos requeridos

1. **ExploraciÃ³n inicial**
   - Â¿CuÃ¡ntos estudiantes hay? Â¿CuÃ¡ntas variables?
   - Â¿Hay valores nulos? Â¿CÃ³mo los manejarÃ¡s?
   - Visualiza la distribuciÃ³n de la variable objetivo.

2. **SelecciÃ³n de features**
   - Elige al menos 2 variables predictoras y justifica tu elecciÃ³n.
   - Excluye variables que causarÃ­an data leakage.

3. **Modelado**
   - Divide en train/test (80/20) con `random_state=42`.
   - Entrena una `LinearRegression`.
   - Calcula MAE y RMSE.

4. **ComparaciÃ³n con lÃ­nea base**
   - Compara tu modelo contra predecir siempre el promedio.

5. **ConclusiÃ³n**
   - Â¿QuÃ© variable tiene mayor influencia? (Revisa `model.coef_`)
   - Â¿QuÃ© mejorarÃ­as si tuvieras mÃ¡s datos?

## 📦 Entrega

Notebook `.ipynb` con resultados visibles (celdas ejecutadas). MÃ¡ximo 2 pÃ¡ginas de anÃ¡lisis en texto.
