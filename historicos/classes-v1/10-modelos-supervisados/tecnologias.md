# 🛠️ Tecnologías complementarias — Clase 10: Modelos supervisados

> Herramientas y librerías que complementan o extienden lo visto en esta clase.

## 📦 Librerías principales usadas en esta clase

| Librería | Versión recomendada | Para qué se usa en esta clase |
|---|---|---|
| scikit-learn | >= 1.3 | Entrenar `DecisionTreeClassifier` y calcular métricas de clasificación |
| pandas | >= 2.0 | Crear la etiqueta supervisada `alto_desempeno` y manipular el dataset |
| numpy | >= 1.24 | Cómputo de arrays al calcular métricas y predicciones |
| matplotlib | >= 3.7 | Visualizar el árbol de decisión y la distribución de clases |
| seaborn | >= 0.12 | Graficar la matriz de confusión con `heatmap` |

## 🔗 Herramientas complementarias

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `sklearn.tree.plot_tree` | Función de scikit-learn para visualizar el árbol entrenado | Cuando quieres mostrar las reglas del árbol de forma gráfica |
| `sklearn.metrics.ConfusionMatrixDisplay` | Display nativo de scikit-learn para la matriz de confusión | Para mostrar visualmente los verdaderos/falsos positivos y negativos |
| `sklearn.neighbors.KNeighborsClassifier` | Clasificador alternativo basado en vecinos | Para comparar con el árbol y discutir ventajas de cada enfoque |
| `sklearn.linear_model.LogisticRegression` | Clasificador lineal interpretable | Como línea base para comparar antes de usar modelos más complejos |
| Graphviz | Herramienta externa para exportar el árbol como imagen de alta calidad | Cuando necesitas incluir el árbol en un informe o presentación |

## 📚 Recursos para profundizar

- [Documentación oficial — DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [Documentación oficial — classification_report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html)
- [Guía de métricas de clasificación en scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics)
- [Tutorial interactivo de Kaggle: Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning)
- [Artículo: Precisión vs Recall — cuándo usar cada uno](https://developers.google.com/machine-learning/crash-course/classification/precisión-and-recall)

## ⚡ Comandos de instalación

```bash
pip install scikit-learn pandas numpy matplotlib seaborn
```

Para instalar Graphviz (visualización de árboles de alta calidad):

```bash
pip install graphviz
# En Windows también instalar el binario desde https://graphviz.org/download/
```

Para verificar la instalación:

```bash
python -c "from sklearn.tree import DecisionTreeClassifier; print('OK')"
```
