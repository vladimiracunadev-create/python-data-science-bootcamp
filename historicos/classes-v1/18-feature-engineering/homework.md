# 📝 Tarea — Clase 18
> 📝 Trabajo autónomo para consolidar lo visto y practicar con más calma.

## 🎯 Encargo

Toma el dataset `ventas_tienda.csv` y prepáralo para un modelo de machine learning. El objetivo del modelo será predecir si una venta fue alta o baja (define el umbral que consideres razonable).

Debes completar los siguientes pasos en orden:

1. **Exploración inicial**: revisar tipos, nulos y estadísticas descriptivas.
2. **Variable objetivo**: crear la columna `venta_alta` (1 si `total_venta` supera el umbral elegido, 0 si no). Documenta cuántos 1s y 0s hay.
3. **Variables derivadas**: crear al menos 3 nuevas variables numéricas derivadas de las columnas existentes.
4. **Extracción desde fecha**: crear `mes`, `dia_semana` y `es_fin_semana`.
5. **Codificación categórica**: aplicar `pd.get_dummies` con `drop_first=True` a todas las columnas categóricas relevantes.
6. **Binning**: crear al menos una variable en rangos con `pd.cut` o `pd.qcut`.
7. **Escalado**: aplicar `StandardScaler` a las columnas numéricas más importantes.
8. **Selección**: calcular la correlación de todas las variables con `venta_alta` y seleccionar las 10 más relevantes.
9. **Dataset final**: mostrar el shape del dataset resultante y la lista de columnas seleccionadas.

## 📦 Entregables
- Código o desarrollo ordenado.
- Conclusión breve conectada con evidencia.
- Comentarios que expliquen qué hace y para qué sirve cada bloque importante.

## 🔍 Autoevaluación final
- Entendí la pregunta del módulo.
- Puedo explicar la salida sin leer el código completo.
- Dejé comentarios útiles en los pasos clave.
