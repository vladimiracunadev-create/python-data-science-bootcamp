# 📘 Clase 21: Gradient Boosting — modelos potentes

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Comprender cómo el Gradient Boosting construye árboles de forma secuencial donde cada uno corrige los errores del anterior, conocer sus parámetros clave, y comparar su desempeño contra modelos anteriores (Regresión Logística, Árbol, Random Forest).

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/retencion_clientes.csv`
- `datasets/estudiantes.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Explicar la diferencia conceptual entre bagging (Random Forest) y boosting (Gradient Boosting).
- Entrenar un `GradientBoostingClassifier` y ajustar `n_estimators`, `learning_rate` y `max_depth`.
- Comparar cuatro clasificadores en la misma tarea y elegir el mejor con criterio.

## 🧭 Temas clave
- Boosting secuencial vs bagging paralelo
- GradientBoostingClassifier (sklearn)
- Parámetros: n_estimators, learning_rate, max_depth
- XGBoost básico (XGBClassifier)
- Comparación de modelos: LogisticRegression, DecisionTree, RandomForest, GradientBoosting

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.

## 💡 Idea central
El Gradient Boosting construye cada árbol para corregir los errores del anterior, logrando una de las mayores precisiones disponibles para datos tabulares.

## 👩‍🏫 Nota para el docente
La metáfora del "estudiante que revisa sus errores del examen anterior" es muy efectiva. Énfasis especial en `learning_rate`: pídeles que imaginen cuánto avanzar por paso al bajar una colina; muy rápido (learning_rate alto) y te caes; muy despacio (learning_rate bajo) y tardas mucho. También menciona que GBM domina las competencias de Kaggle con datos tabulares.
