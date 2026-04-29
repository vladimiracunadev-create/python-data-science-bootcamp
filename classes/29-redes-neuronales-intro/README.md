# 📘 Clase 29: Introducción a redes neuronales

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Entender qué es una red neuronal, cómo aprende y cuándo usarla. Al terminar esta clase, el estudiante podrá construir y evaluar su primera red neuronal usando scikit-learn, comparar su rendimiento contra modelos de árbol, y entender conceptualmente cómo funcionan frameworks más avanzados como Keras y TensorFlow.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/estudiantes.csv`
- `datasets/ventas_tienda.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Explicar qué es una neurona artificial y cómo se conectan en capas, entrenar un MLPClassifier de scikit-learn con distintas configuraciones, comparar el rendimiento de MLP vs Decisión Tree vs Random Forest en el mismo dataset

## 🧭 Temas clave
- Neurona artificial: pesos, bias, función de activación
- Funciones de activación: sigmoid y ReLU
- Capas ocultas y redes profundas
- Forward pass y backward pass (backpropagation)
- MLPClassifier de scikit-learn
- Cuándo usar redes neuronales vs modelos de árbol

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.

## 💡 Idea central
Una red neuronal aprende representaciones progresivamente más complejas de los datos, pasando la información por capas de transformación.

## 👩‍🏫 Nota para el docente
Usa la analogía del procesamiento fotográfico: aplicar un filtro, luego otro, luego otro — cada capa detecta patrones más complejos que la anterior. Dibuja en la pizarra una red simple de 3 capas antes de pasar al código. El objetivo no es que los estudiantes implementen backpropagation desde cero, sino que entiendan cuándo y cómo usar MLPClassifier.
