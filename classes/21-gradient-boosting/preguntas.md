# ❓ Preguntas — Clase 21: Gradient Boosting

> Preguntas de comprensión, discusión y evaluación.

## 🧠 Preguntas de comprensión

1. ¿Qué significa que boosting sea "secuencial" y en qué se diferencia de bagging (Random Forest)?
2. ¿Cómo "corrige errores" cada árbol nuevo en Gradient Boosting? ¿Qué aprende a predecir cada árbol adicional?
3. ¿Qué efecto tiene un `learning_rate` muy alto en el entrenamiento? ¿Y uno demasiado bajo?
4. ¿Cuál es la diferencia técnica principal entre `GradientBoostingClassifier` de sklearn y `XGBClassifier` de XGBoost?
5. ¿Por qué Gradient Boosting tiende a superar a Random Forest en muchos benchmarks y competencias de datos?
6. ¿En qué tipo de datasets Gradient Boosting puede ser una mala elección? ¿Cuándo preferirías Random Forest?
7. ¿Qué parámetro controla cuántos árboles se construyen en GBM y cómo interactúa con el `learning_rate`?

## 💬 Preguntas de discusión

1. Si entrenas un GBM con `learning_rate=0.5` y obtienes overfitting, ¿qué combinación de hiperparámetros probarías para solucionarlo? Argumenta tu elección.
2. Comparas 4 modelos (Regresión Logística, Árbol de Decisión, Random Forest, GBM) y el GBM gana en accuracy pero tarda 10x más en entrenar. ¿En qué contextos vale la pena ese costo? ¿Cuándo no?
3. XGBoost ganó muchas competencias de Kaggle entre 2014 y 2018. ¿Por qué crees que sigue siendo una herramienta relevante hoy aunque existan redes neuronales más poderosas?

## 🧪 Preguntas de código

1. Entrena un `GradientBoostingClassifier` con `learning_rate=0.01`, `n_estimators=500` y otro con `learning_rate=0.5`, `n_estimators=50`. Compara accuracy en test. ¿Cuál funciona mejor?
2. Entrena los 4 modelos de la clase (LogReg, DecisionTree, RandomForest, GradientBoosting) sobre `estudiantes.csv` y crea un gráfico de barras comparando su accuracy en el conjunto de prueba.
3. Usa `XGBClassifier` sobre `retencion_clientes.csv` para predecir si un cliente se dará de baja. Muestra las 5 variables más importantes usando `xgb.plot_importance()`.

## 🎯 Pregunta integradora

Con el dataset `retencion_clientes.csv`, entrena los 4 modelos comparados en clase. Para cada modelo: calcula accuracy, precisión, recall y F1-score (usa `classification_report`). Dado que el objetivo de negocio es identificar clientes que van a irse antes de que ocurra (recall alto es crítico), ¿qué modelo elegirías y por qué? ¿Qué hiperparámetros del GBM o XGBoost ajustarías para mejorar el recall sin sacrificar demasiado la precisión?
