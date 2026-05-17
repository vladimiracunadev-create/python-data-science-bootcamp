# 🛠️ Tecnologías complementarias — Clase 09: Introducción a machine learning

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| scikit-learn | >= 1.3 | Train/test split y entrenamiento de la regresión lineal |
| pandas | >= 2.0 | Carga del dataset y selección de columnas X e y |
| numpy | >= 1.24 | Operaciones numéricas sobre arrays de predicciones |
| matplotlib | >= 3.7 | Visualizar predicciones vs valores reales con un scatter plot |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| Jupyter Notebook / JupyterLab | Entorno interactivo para ejecutar bloques paso a paso | Durante la clase para mostrar el flujo celda por celda |
| seaborn | Librería de visualización estadística sobre matplotlib | Para graficar la línea de regresión con `regplot` de forma rápida |
| joblib | Serialización de modelos de scikit-learn | Cuando quieres guardar el modelo entrenado para reutilizarlo sin reentrenar |
| yellowbrick | Visualizaciones específicas para ML | Para mostrar residuos y calidad del ajuste de forma visual e inmediata |

## 📚 Recursos para profundizar

- [Documentación oficial de scikit-learn — LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Documentación oficial de scikit-learn — train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
- [Guía de usuario de scikit-learn: Supervised learning](https://scikit-learn.org/stable/supervised_learning.html)
- [Pandas — Selección de columnas y tipos de datos](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Tutorial interactivo de ML con scikit-learn en Kaggle](https://www.kaggle.com/learn/intro-to-machine-learning)

## ⚡ Comandos de instalación

```bash
pip install scikit-learn pandas numpy matplotlib seaborn joblib
```

Para verificar que scikit-learn quedó instalado correctamente:

```bash
python -c "import sklearn; print(sklearn.__version__)"
```
