# ❓ Preguntas — Clase 19: Regresión Lineal y Múltiple

> Preguntas de comprensión, discusión y evaluación.

## 🧠 Preguntas de comprensión

1. ¿Qué representa la línea de regresión en un gráfico de dispersión y qué criterio usa sklearn para encontrarla (mínimos cuadrados)?
2. ¿Qué significan los atributos `coef_` e `intercept_` de un modelo `LinearRegression`? ¿Cómo se interpreta cada uno en contexto real?
3. ¿Qué indica un valor de R² cercano a 0? ¿Y uno cercano a 1? ¿Puede R² ser negativo y qué significaría eso?
4. ¿Cuál es la diferencia entre regresión lineal simple y regresión lineal múltiple en términos de variables de entrada?
5. ¿Qué es un residual? ¿Por qué es útil graficarlos para evaluar si un modelo lineal es apropiado?
6. ¿Qué mide el RMSE y en qué unidades se expresa respecto a la variable objetivo?
7. ¿En qué situaciones deberías usar regresión en lugar de clasificación? Da dos ejemplos concretos de cada tipo de problema.

## 💬 Preguntas de discusión

1. Si el R² de tu modelo es 0.45, ¿considerarías que el modelo es útil? ¿Depende del contexto? Da un ejemplo donde 0.45 sea aceptable y otro donde no lo sea.
2. Un colega dice: "mientras más variables independientes agregue al modelo, mejor será el R²". ¿Estás de acuerdo? ¿Qué riesgos trae agregar variables indiscriminadamente?
3. ¿Cómo interpretarías en términos de negocio que el `coef_` de la variable "horas de estudio" sea 2.3 en un modelo que predice calificaciones finales?

## 🧪 Preguntas de código

1. Dado el dataset `ventas_tienda.csv` con columnas `publicidad` y `ventas`, entrena un modelo de regresión lineal y muestra el coeficiente, intercepto y R². Luego predice las ventas para una inversión publicitaria de 500.
2. Crea un gráfico de residuales: calcula `y_pred = model.predict(X_test)`, luego grafica `y_test - y_pred` contra `y_pred`. ¿Qué patrón esperarías ver en un modelo bien ajustado?
3. Usando `estudiantes.csv`, entrena una regresión múltiple con al menos 3 variables (por ejemplo, `horas_estudio`, `ausencias`, `promedio_anterior`) para predecir la calificación final. Calcula el RMSE del modelo en el conjunto de prueba.

## 🎯 Pregunta integradora

Tienes el dataset `ventas_tienda.csv` con columnas: `publicidad_tv`, `publicidad_radio`, `publicidad_redes`, `descuento_porcentaje` y `ventas`. Entrena una regresión múltiple, interpreta el coeficiente de cada variable (¿qué canal de publicidad tiene más impacto por unidad invertida?), calcula R² y RMSE, grafica los residuales y concluye: ¿el modelo es adecuado para predecir ventas? ¿Qué cambios harías para mejorarlo?
