# 🔧 Tecnologías complementarias — Clase 20: Árboles de Decisión y Random Forest

> Herramientas y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `sklearn.tree.export_text` | Exportar el árbol como texto ASCII para inspección rápida sin gráfico | Básico |
| `sklearn.ensemble.ExtraTreesClassifier` | Variante de RF con splits aleatorios: más rápido, a veces más preciso | Intermedio |
| `dtreeviz` | Visualizaciones de árboles mucho más detalladas y explicativas que `plot_tree` | Intermedio |
| `shap` | Explica las predicciones de Random Forest modelo por modelo y muestra contribución de cada feature | Avanzado |
| `sklearn.inspection.permutation_importance` | Alternativa más robusta a `feature_importances_` basada en permutaciones | Intermedio |
| `imblearn.ensemble.BalancedRandomForestClassifier` | RF que maneja clases desbalanceadas automáticamente | Intermedio |

## 🌐 Recursos recomendados

- **Documentación oficial**: https://scikit-learn.org/stable/modules/ensemble.html#forests-of-randomized-trees
- **Tutorial recomendado**: "Random Forest in Python" — Towards Data Science (buscar en Medium/TDS)
- **Concepto clave para buscar**: "bias-variance tradeoff decision trees" — para entender por qué árboles profundos sobreajustan

## 🚀 Próximos pasos sugeridos

- Explorar `GridSearchCV` para encontrar el mejor `max_depth` y `n_estimators` automáticamente
- Aprender sobre `ExtraTreesClassifier` como alternativa más rápida al Random Forest
- Estudiar SHAP values para explicar predicciones individuales del modelo
- Probar Random Forest para regresión con `RandomForestRegressor`

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `LightGBM.LGBMClassifier` | Implementación de boosting basada en árboles, muy rápida | Cuando el dataset es grande y el tiempo de entrenamiento importa |
| `sklearn.ensemble.BaggingClassifier` | Bagging genérico: puedes aplicarlo a cualquier estimador base | Para entender el concepto de bagging con cualquier modelo |
| `Graphviz` + `export_graphviz` | Exportar árboles a formato visual profesional para presentaciones | Para presentar árboles de decisión a stakeholders |
