# 📝 Tarea — Clase 21

> 📝 Trabajo autónomo para consolidar lo visto y practicar con más calma.

## 🎯 Encargo

Aplica los cuatro clasificadores vistos en clase (Regresión Logística, Árbol, Random Forest y Gradient Boosting) sobre el dataset `retencion_clientes.csv`. El objetivo es predecir si un cliente abandonará el servicio (`churn`). Documenta cada paso, compara los resultados y argumenta cuál modelo recomendarías para producción.

## 📦 Entregables

- Notebook limpio con todos los pasos: carga, exploración mínima, entrenamiento, evaluación.
- Tabla comparativa de accuracy (y si puedes, F1-score) de los cuatro modelos en el conjunto de test.
- Un párrafo de conclusión que responda: ¿cuál modelo recomendarías y por qué? ¿Hay algún trade-off entre precisión e interpretabilidad que valga la pena considerar?
- Al menos un gráfico: puede ser la importancia de variables del bosque o del GBM, o un gráfico de learning_rate vs accuracy.

## 🔍 Autoevaluación final

- Entendí la diferencia conceptual entre bagging y boosting.
- Puedo explicar para qué sirve el `learning_rate` con una analogía propia.
- Sé cómo comparar modelos de forma justa (mismo split, mismo dataset).
- Identifiqué cuál modelo funciona mejor en este problema y puedo justificarlo.
- Dejé comentarios útiles en los pasos clave del notebook.
