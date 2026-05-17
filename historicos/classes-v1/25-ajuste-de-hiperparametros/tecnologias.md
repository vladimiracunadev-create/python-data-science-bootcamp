# 🔧 Tecnologías complementarias — Clase 25: Ajuste de Hiperparámetros

> Herramientas y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `scikit-learn` (GridSearchCV) | Búsqueda exhaustiva de hiperparámetros con validación cruzada | Principiante |
| `scikit-learn` (RandomizedSearchCV) | Búsqueda aleatoria eficiente en espacios grandes de hiperparámetros | Principiante |
| `Optuna` | Optimización bayesiana de hiperparámetros, muy eficiente y popular | Intermedio |
| `Hyperopt` | Búsqueda basada en algoritmos TPE (Tree-structured Parzen Estimator) | Intermedio |
| `Ray Tune` | Ajuste de hiperparámetros distribuido para modelos grandes | Avanzado |
| `Keras Tuner` | Optimización automática de hiperparámetros para redes neuronales con Keras | Intermedio |

## 🌐 Recursos recomendados

- **Documentación oficial**: https://scikit-learn.org/stable/modules/grid_search.html
- **Tutorial recomendado**: "Hyperparameter Tuning the Random Forest in Python" en Towards Data Science
- **Concepto clave para buscar**: "Bayesian optimization hyperparameters machine learning"

## 🚀 Próximos pasos sugeridos

- Explorar `Optuna` para optimización bayesiana, que es mucho más inteligente que búsqueda aleatoria
- Aprender a usar `HalvingGridSearchCV` de scikit-learn, que descarta combinaciones malas rápidamente
- Combinar el ajuste de hiperparámetros con `Pipeline` para evitar fuga de datos en el preprocesamiento
- Estudiar el concepto de "early stopping" para detener el entrenamiento cuando deja de mejorar

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `Optuna` | Framework moderno de optimización automática con visualizaciones integradas | Cuando GridSearch es demasiado lento o el espacio es continuo |
| `mlflow` | Registra experimentos, parámetros y métricas de cada prueba | Cuando necesitas comparar muchos experimentos y guardar historial |
| `Weights & Biases (wandb)` | Plataforma de seguimiento de experimentos en la nube con dashboards | Proyectos de equipo donde varios experimentan al mismo tiempo |
