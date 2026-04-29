# 🧪 Ejercicios — Clase 20

> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar

- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.
- Explica qué hace cada transformación relevante y para qué sirve.

## 🧭 Trabajo guiado

### Ejercicio 1 — Árbol básico
1. Carga `datasets/estudiantes.csv`.
2. Crea la etiqueta `estado`: 1 si `evaluacion_python >= 60` Y `asistencia_pct >= 70`, de lo contrario 0.
3. Entrena un `DecisionTreeClassifier` con `max_depth=3`.
4. Imprime el accuracy en train y en test. ¿Hay diferencia grande? ¿Qué indica eso?

### Ejercicio 2 — Visualizar el árbol
1. Usa `plot_tree` para graficar el árbol entrenado en el ejercicio anterior.
2. Identifica cuál es el primer nodo (la pregunta más importante).
3. Escribe con tus palabras qué condición separa mejor a los estudiantes.

### Ejercicio 3 — Sobreajuste con max_depth
1. Entrena tres árboles: `max_depth=1`, `max_depth=5`, `max_depth=None` (sin límite).
2. Para cada uno imprime el accuracy en train y en test.
3. Explica en una frase qué está pasando con el árbol sin límite.

### Ejercicio 4 — Random Forest
1. Entrena un `RandomForestClassifier` con `n_estimators=100` y `max_depth=5`.
2. Compara su accuracy con el mejor árbol simple del ejercicio anterior.
3. Grafica la importancia de variables. ¿Cuál variable parece más útil para predecir el estado?

### Ejercicio 5 — Predicción individual
1. Crea un DataFrame con tres estudiantes hipotéticos con distintos niveles de asistencia y notas.
2. Usa el bosque entrenado para predecir su estado (0 o 1).
3. Usa `predict_proba()` para ver la confianza del modelo en cada predicción.

## ✅ Criterios de autocorrección

- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
- Puedes explicar por qué el bosque suele ganar al árbol individual.
