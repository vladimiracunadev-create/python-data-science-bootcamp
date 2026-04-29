# 🧪 Ejercicios — Clase 21

> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar

- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.
- Explica qué hace cada transformación relevante y para qué sirve.

## 🧭 Trabajo guiado

### Ejercicio 1 — GradientBoostingClassifier básico
1. Carga `datasets/estudiantes.csv` y crea la etiqueta `estado` (Aprobado / En Riesgo).
2. Entrena un `GradientBoostingClassifier` con `n_estimators=100`, `learning_rate=0.1`, `max_depth=3`.
3. Imprime el accuracy en train y en test.
4. En una frase: ¿qué hace diferente este modelo respecto a un Random Forest?

### Ejercicio 2 — Efecto del learning_rate
1. Entrena tres modelos GBM con `learning_rate` de 0.01, 0.1 y 0.5 (mismo `n_estimators=100`).
2. Imprime el accuracy en test de cada uno.
3. Explica qué pasa cuando el learning_rate es demasiado alto o demasiado bajo.

### Ejercicio 3 — Comparación de 4 modelos
1. Entrena los cuatro modelos: `LogisticRegression`, `DecisionTreeClassifier`, `RandomForestClassifier`, `GradientBoostingClassifier`.
2. Imprime o muestra en una tabla el accuracy en test de cada uno.
3. ¿Cuál es el mejor? ¿Qué modelo eliminarías primero si tuvieras que simplificar?

### Ejercicio 4 — XGBoost (si está instalado)
1. Importa `xgboost as xgb` y crea un `XGBClassifier` con los mismos parámetros que el GBM del Ejercicio 1.
2. Entrena y evalúa. ¿El accuracy es similar al de sklearn GBM?
3. Escribe una diferencia entre sklearn GBM y XGBoost según lo que leíste en la teoría.

### Ejercicio 5 — Reflexión final
Responde con tus palabras (2-3 oraciones):
- ¿En qué tipo de problema usarías Gradient Boosting en lugar de Regresión Logística?
- ¿Qué harías si el modelo GBM tuviera accuracy de 0.99 en train y 0.65 en test?

## ✅ Criterios de autocorrección

- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
- Puedes explicar la diferencia entre boosting y bagging con una analogía propia.
