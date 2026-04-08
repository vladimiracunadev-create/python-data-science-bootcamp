# 📝 Tarea â€” Clase 11: EvaluaciÃ³n robusta y Pipelines de ML

> 📝 Trabajo autonomo para consolidar lo visto y practicar con mas calma.


## 🎯 Consigna

Construye un Pipeline completo para predecir el **descuento aplicado** (regresiÃ³n) o la **sucursal con mayor renta** (clasificaciÃ³n) usando `ventas_tienda.csv`.

## ✅ Pasos requeridos

1. **ExploraciÃ³n**
   - Identifica columnas numÃ©ricas y categÃ³ricas.
   - Â¿Hay valores nulos? Decide cÃ³mo imputarlos dentro del Pipeline.

2. **Pipeline**
   - Usa `ColumnTransformer` para preprocesar por separado numÃ©ricas y categÃ³ricas.
   - Incluye `SimpleImputer` en la etapa numÃ©rica.
   - Incluye el modelo al final del Pipeline.

3. **EvaluaciÃ³n robusta**
   - Aplica validaciÃ³n cruzada con k=5.
   - Reporta media y desviaciÃ³n estÃ¡ndar del score.

4. **BÃºsqueda de hiperparÃ¡metros**
   - Usa `GridSearchCV` con al menos 2 hiperparÃ¡metros y 3 valores cada uno.
   - Muestra los mejores parÃ¡metros.

5. **ConclusiÃ³n**
   - Â¿El Pipeline mejorÃ³ el resultado respecto a la clase anterior?
   - Â¿QuÃ© hiperparÃ¡metro tuvo mÃ¡s impacto?

## 📦 Entrega

Notebook `.ipynb` con todas las celdas ejecutadas, incluyendo la tabla de resultados del GridSearchCV.
