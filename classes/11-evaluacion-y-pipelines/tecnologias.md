# 🛠️ Tecnologías complementarias — Clase 11: Evaluación y pipelines

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| scikit-learn | >= 1.3 | Pipeline, StandardScaler, LogisticRegression, cross_val_score |
| pandas | >= 2.0 | Preparación del dataset y construcción de la etiqueta supervisada |
| numpy | >= 1.24 | Cómputo de la media y desviación estándar de los scores de validación cruzada |
| matplotlib | >= 3.7 | Visualizar la distribución de scores entre folds |
| seaborn | >= 0.12 | Graficar la matriz de confusión resultante del pipeline |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `sklearn.pipeline.Pipeline` | Encadena pasos de preprocesamiento y modelo en un único objeto | Siempre que haya al menos un paso de transformación antes del modelo |
| `sklearn.model_selection.GridSearchCV` | Búsqueda de hiperparámetros dentro de un pipeline | Cuando quieres optimizar parámetros del modelo sin introducir leakage |
| `sklearn.preprocessing.SimpleImputer` | Imputa valores nulos antes del modelo | Cuando el dataset tiene columnas con NaN que deben tratarse dentro del pipeline |
| `sklearn.preprocessing.OneHotEncoder` | Codifica variables categóricas | Cuando el dataset incluye columnas de texto que el modelo no puede procesar directamente |
| `sklearn.compose.ColumnTransformer` | Aplica transformaciones distintas a columnas distintas | Cuando hay columnas numéricas y categóricas que necesitan preprocesamiento diferente |
| mlflow | Rastreo de experimentos y métricas por versión de modelo | Para proyectos donde se quiere comparar múltiples pipelines y hiperparámetros |

## 📚 Recursos para profundizar

- [Documentación oficial — Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html)
- [Documentación oficial — cross_val_score](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html)
- [Guía de scikit-learn: Pipelines y preprocesamiento](https://scikit-learn.org/stable/modules/compose.html)
- [Artículo: What is data leakage in ML?](https://machinelearningmastery.com/data-leakage-machine-learning/)
- [Documentación oficial — GridSearchCV](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html)

## ⚡ Comandos de instalación

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

Para instalar mlflow si se quiere rastrear experimentos:

```bash
pip install mlflow
```

Para verificar que el módulo de pipelines está disponible:

```bash
python -c "from sklearn.pipeline import Pipeline; print('Pipeline disponible')"
```
