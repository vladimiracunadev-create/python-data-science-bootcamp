# 🛠️ Tecnologías complementarias — Clase 12: Proyecto final y cierre

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| scikit-learn | >= 1.3 | Pipeline completo: imputación, escalado, modelo y evaluación con validación cruzada |
| pandas | >= 2.0 | Carga, limpieza, EDA y construcción de variables del proyecto final |
| numpy | >= 1.24 | Cómputo numérico sobre columnas y métricas |
| matplotlib | >= 3.7 | Gráficos de EDA, distribución de variables e importancia de features |
| seaborn | >= 0.12 | Heatmap de correlaciones, matriz de confusión y distribuciones |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `sklearn.pipeline.Pipeline` | Encadena limpieza, escalado y modelo en un único objeto reproducible | Siempre, para evitar leakage en el proyecto final |
| `sklearn.compose.ColumnTransformer` | Aplica transformaciones distintas a columnas numéricas y categóricas | Cuando el dataset del proyecto tiene ambos tipos de columnas |
| `sklearn.preprocessing.SimpleImputer` | Imputa valores nulos con media, mediana o moda | Para manejar valores faltantes dentro del pipeline |
| `joblib` | Guarda el pipeline entrenado en disco | Para reutilizar el modelo sin reentrenar |
| `sklearn.inspection.permutation_importance` | Calcula la importancia de variables por permutación | Para comunicar qué variables son más relevantes en el modelo |
| Jupyter Notebook | Entorno de presentación del proyecto final | Para mostrar el flujo completo: pregunta → datos → análisis → modelo → conclusión |
| nbconvert | Convierte el notebook a HTML o PDF | Para compartir el proyecto final con personas que no tienen Python instalado |

## 📚 Recursos para profundizar

- [Documentación oficial — Pipeline y ColumnTransformer](https://scikit-learn.org/stable/modules/compose.html)
- [Documentación oficial — Feature importance](https://scikit-learn.org/stable/modules/permutation_importance.html)
- [Guía de scikit-learn: Choosing the right estimator](https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)
- [Documentación de nbconvert — exportar notebooks](https://nbconvert.readthedocs.io/en/latest/)
- [Tutorial Kaggle: Data Cleaning](https://www.kaggle.com/learn/data-cleaning)
- [Artículo: How to present ML results to non-technical stakeholders](https://towardsdatascience.com/how-to-communicate-machine-learning-results-to-non-technical-stakeholders-5b6e2a3c8e2e)

## ⚡ Comandos de instalación

```bash
pip install scikit-learn pandas numpy matplotlib seaborn joblib
```

Para exportar el notebook final a HTML:

```bash
pip install nbconvert
jupyter nbconvert --to html notebook.ipynb
```

Para verificar que todas las librerías están listas antes de la presentación:

```bash
python -c "import sklearn, pandas, numpy, matplotlib, seaborn, joblib; print('Todo listo')"
```
