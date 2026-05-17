# 📘 Clase 20: Árboles de decisión y Random Forest

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Entender cómo un árbol de decisión hace preguntas de sí/no para clasificar datos, controlar el sobreajuste con `max_depth`, y mejorar la precisión combinando muchos árboles en un Random Forest.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/estudiantes.csv`
- `datasets/ventas_tienda.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Explicar cómo un árbol de decisión divide los datos en nodos y hojas.
- Controlar el sobreajuste ajustando `max_depth`.
- Entrenar un Random Forest y leer la importancia de cada variable.

## 🧭 Temas clave
- Árbol de decisión (DecisionTreeClassifier)
- Profundidad, hojas y nodos
- Impureza de Gini y ganancia de información
- Sobreajuste y `max_depth`
- Random Forest (bagging)
- Importancia de variables

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.

## 💡 Idea central
Un Random Forest combina muchos árboles de decisión para dar respuestas más confiables que cualquier árbol solo.

## 👩‍🏫 Nota para el docente
Dibuja en la pizarra un árbol de tres preguntas (¿asistencia > 80%? → ¿nota Python > 70%?) antes de mostrar código. La metáfora del "jurado de mil personas" es muy efectiva para explicar el Random Forest a cualquier edad.
