# ❓ Preguntas — Clase 25: Ajuste de Hiperparámetros

> Preguntas de comprensión, discusión y evaluación.

## 🧠 Preguntas de comprensión

1. ¿Cuál es la diferencia entre un parámetro y un hiperparámetro? Da un ejemplo de cada uno en un árbol de decisión.
2. ¿Por qué no podemos aprender los hiperparámetros directamente desde los datos durante el entrenamiento?
3. ¿Qué hace `GridSearchCV` internamente cuando recibe un `param_grid` con 3 valores para un hiperparámetro y 4 para otro?
4. ¿Qué significa el parámetro `cv=5` dentro de `GridSearchCV`? ¿Cuántos modelos se entrenan en total si `param_grid` tiene 12 combinaciones?
5. ¿Cuándo es preferible usar `RandomizedSearchCV` en lugar de `GridSearchCV`?
6. ¿Qué representan `best_params_` y `best_score_` después de ajustar un `GridSearchCV`?
7. ¿Qué diferencia hay entre una `learning_curve` y una `validation_curve`?

## 💬 Preguntas de discusión

1. Imagina que tu modelo tiene 5 hiperparámetros con 10 valores posibles cada uno. ¿Sería práctico usar `GridSearchCV`? ¿Qué harías en cambio?
2. Un compañero dice "encontré los mejores hiperparámetros, así que mi modelo es perfecto". ¿Qué riesgos no está considerando?
3. ¿Por qué crees que la analogía del horno (temperatura, tiempo, posición) sirve para explicar los hiperparámetros? ¿Puedes pensar en otra analogía cotidiana?

## 🧪 Preguntas de código

1. Escribe el `param_grid` para buscar `max_depth` entre 3, 5 y 10, y `n_estimators` entre 50, 100 y 200 en un `RandomForestClassifier`.
2. ¿Qué código usarías para ver los mejores parámetros encontrados y el mejor puntaje de validación cruzada después de correr un `GridSearchCV`?
3. Si tienes un `GridSearchCV` llamado `gs`, ¿cómo harías predicciones con el mejor modelo encontrado sin tener que extraerlo manualmente?

## 🎯 Pregunta integradora

Tienes el dataset `estudiantes.csv` y quieres predecir si un estudiante aprobará el examen final. Diseña una estrategia completa de ajuste de hiperparámetros: elige el modelo base, define el `param_grid` con al menos 3 hiperparámetros, justifica si usarías `GridSearchCV` o `RandomizedSearchCV`, explica cómo interpretarías la `learning_curve` resultante y describe qué harías si el mejor modelo sigue mostrando sobreajuste.
