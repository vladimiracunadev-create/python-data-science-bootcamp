# 🔧 Tecnologías complementarias — Clase 21: Gradient Boosting

> Herramientas y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `xgboost` | Implementación optimizada de gradient boosting; la más usada en competencias | Intermedio |
| `lightgbm` | Gradient boosting aún más rápido que XGBoost, excelente en datos grandes | Intermedio |
| `catboost` | Gradient boosting de Yandex, maneja variables categóricas automáticamente | Intermedio |
| `sklearn.model_selection.GridSearchCV` | Búsqueda de hiperparámetros óptimos (learning_rate, n_estimators, max_depth) | Intermedio |
| `optuna` | Búsqueda de hiperparámetros bayesiana, más eficiente que GridSearch | Avanzado |
| `sklearn.metrics.classification_report` | Muestra precisión, recall y F1 por clase para evaluar el modelo completo | Básico |

## 🌐 Recursos recomendados

- **Documentación oficial**: https://xgboost.readthedocs.io/en/stable/
- **Tutorial recomendado**: "XGBoost — A Complete Guide" — Machine Learning Mastery (machinelearningmastery.com)
- **Concepto clave para buscar**: "gradient boosting explained step by step" — para entender los residuales como gradientes

## 🚀 Próximos pasos sugeridos

- Aprender a usar `early_stopping_rounds` en XGBoost para detener el entrenamiento automáticamente antes del overfitting
- Explorar LightGBM como alternativa más rápida para datasets con millones de filas
- Estudiar SHAP values con XGBoost para explicar predicciones individuales
- Practicar `cross_val_score` para evaluar GBM de forma más robusta que un solo train/test split

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `lightgbm.LGBMClassifier` | Boosting con hojas en lugar de niveles; muy rápido en datos grandes | Cuando el dataset tiene más de 100k filas |
| `catboost.CatBoostClassifier` | Maneja categorías sin encoding; menos preprocesamiento requerido | Cuando hay muchas variables categóricas con alta cardinalidad |
| `sklearn.ensemble.HistGradientBoostingClassifier` | Versión rápida de GBM nativa en sklearn, similar a LightGBM | Cuando quieres boosting sin instalar librerías extra |
