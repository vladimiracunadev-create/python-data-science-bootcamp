# ❓ Preguntas — Clase 20: Árboles de Decisión y Random Forest

> Preguntas de comprensión, discusión y evaluación.

## 🧠 Preguntas de comprensión

1. ¿Cómo funciona un árbol de decisión? Describe el proceso de dividir los datos en cada nodo usando un ejemplo sencillo (por ejemplo, aprobar o no un préstamo).
2. ¿Qué es la impureza de Gini? ¿Qué valor de Gini indica un nodo perfectamente puro y cuál indica máxima impureza?
3. ¿Qué hace el parámetro `max_depth` en `DecisionTreeClassifier`? ¿Qué problema resuelve limitarlo?
4. ¿Qué es el sobreajuste (overfitting) y cómo puedes detectarlo comparando la accuracy en train vs. test?
5. ¿Qué es el bagging y cómo lo aplica Random Forest internamente para generar diversidad entre árboles?
6. ¿Para qué sirve el atributo `feature_importances_`? ¿Cómo se interpreta un valor de 0.45 para una variable?
7. ¿Por qué generalmente Random Forest supera en accuracy a un solo árbol de decisión?

## 💬 Preguntas de discusión

1. Un árbol con `max_depth=20` tiene 100% de accuracy en train y 62% en test. ¿Qué está pasando? ¿Cómo lo corregirías?
2. ¿Cuándo preferirías usar un solo árbol de decisión en lugar de un Random Forest, a pesar de que RF suele ser más preciso?
3. `feature_importances_` muestra que `ausencias` es la variable más importante para predecir si un estudiante aprueba. ¿Qué decisiones de negocio o pedagógicas podrías tomar con este dato?

## 🧪 Preguntas de código

1. Entrena un `DecisionTreeClassifier` con `max_depth=1` y otro con `max_depth=20` sobre `estudiantes.csv`. Compara la accuracy de ambos en train y test. ¿Cuál sobreajusta?
2. Usa `plot_tree` para visualizar el árbol con `max_depth=3`. Identifica la primera pregunta que hace el árbol (nodo raíz) y explica por qué eligió esa variable.
3. Entrena un `RandomForestClassifier` con `n_estimators=100` y extrae `feature_importances_`. Haz un gráfico de barras horizontal que muestre la importancia de cada variable, ordenado de mayor a menor.

## 🎯 Pregunta integradora

Usando `estudiantes.csv` para predecir si un alumno aprueba o reprueba: entrena tres modelos (árbol con `max_depth=3`, árbol con `max_depth=15`, Random Forest con `n_estimators=100`). Para cada uno, reporta accuracy en train y test. Luego visualiza el árbol del primer modelo e identifica las 3 variables más importantes del Random Forest. Finalmente, explica en palabras simples por qué el Random Forest es más robusto y en qué situación elegirías el árbol pequeño sobre el bosque.
