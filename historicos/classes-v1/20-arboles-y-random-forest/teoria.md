# 🧠 Documento teórico — Clase 20: Árboles de decisión y Random Forest

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

Un Random Forest combina muchos árboles de decisión para dar respuestas más confiables que cualquier árbol solo.

## ❓ Por qué importa este módulo

Los árboles de decisión son uno de los modelos más interpretables del machine learning. El Random Forest extiende esa idea para ganar en precisión sin perder demasiada transparencia. Juntos son la base conceptual de los algoritmos de boosting que veremos en la Clase 21.

## 📖 Conceptos clave

### Árbol de decisión como diagrama de flujo
Un árbol de decisión es una secuencia de preguntas de sí/no sobre los datos:

```
¿asistencia_pct > 80?
  Sí → ¿evaluacion_python > 70?
         Sí → Aprobado
         No → En Riesgo
  No → En Riesgo
```

Cada pregunta es un **nodo**. Las respuestas finales son las **hojas**.

### Impureza de Gini y ganancia de información
El árbol elige cada pregunta buscando la que mejor separa las clases:
- **Impureza de Gini = 0**: todos los elementos en ese nodo son de la misma clase (perfecto).
- **Impureza de Gini = 0.5**: el nodo tiene exactamente 50% de cada clase (máxima confusión).

La pregunta que más reduce la impureza se elige primero. Esto es la **ganancia de información**.

**Analogía accesible:** imagina que quieres separar manzanas de naranjas. La primera pregunta que eliges es la que deja menos fruta mezclada en cada caja.

### Sobreajuste (overfitting)
Un árbol sin restricciones puede crecer hasta tener una hoja por cada dato de entrenamiento. Eso le permite memorizar perfectamente el conjunto de entrenamiento, pero falla con datos nuevos.

- **Solución principal:** limitar `max_depth` (la profundidad máxima del árbol).
- Árbol con `max_depth=2` → muy general, puede subajustar.
- Árbol con `max_depth=20` → muy específico, sobreajusta.
- El valor ideal se busca probando varios y comparando en el conjunto de test.

### Random Forest — "muchos árboles, votación democrática"
1. Se construyen `n_estimators` árboles, cada uno entrenado con una muestra aleatoria de los datos (con reemplazo, técnica llamada **bagging**).
2. Cada árbol también usa un subconjunto aleatorio de variables en cada nodo.
3. Para clasificar un nuevo dato, cada árbol vota y gana la clase más votada.

**Analogía:** en lugar de preguntarle a una sola persona experta, preguntas a 100 personas con conocimiento distinto. La respuesta del grupo suele ser más acertada que la de cualquier individuo.

### Importancia de variables
El Random Forest calcula cuánto redujo la impureza cada variable a lo largo de todos los árboles. Las variables con mayor importancia son las más "preguntadas" por el bosque.

## 💻 Bloque de código documentado

### DecisionTreeClassifier básico

**Qué hace:** crear etiqueta → entrenar árbol → evaluar → visualizar

**Para qué sirve:** mostrar el flujo completo de clasificación con un modelo interpretable.

```python
# Qué hace: entrenar un árbol de decisión para clasificar estudiantes como Aprobado / En Riesgo.
# Para qué sirve: introducir DecisionTreeClassifier con un ejemplo real y visualizable.
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/estudiantes.csv")
df["estado"] = ((df["evaluacion_python"] >= 60) & (df["asistencia_pct"] >= 70)).astype(int)

X = df[["asistencia_pct", "evaluacion_python", "evaluacion_pandas"]]
y = df["estado"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

árbol = DecisionTreeClassifier(max_depth=3, random_state=42)
árbol.fit(X_train, y_train)
print("Accuracy árbol:", round(árbol.score(X_test, y_test), 3))

fig, ax = plt.subplots(figsize=(12, 5))
plot_tree(árbol, feature_names=X.columns, class_names=["En Riesgo", "Aprobado"],
          filled=True, ax=ax, fontsize=9)
plt.tight_layout()
plt.show()
```

### RandomForestClassifier con importancia de variables

```python
# Qué hace: entrenar un bosque y graficar la importancia de cada variable.
# Para qué sirve: comparar precisión árbol vs bosque y ver qué variables importan más.
from sklearn.ensemble import RandomForestClassifier
import numpy as np

bosque = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
bosque.fit(X_train, y_train)
print("Accuracy bosque:", round(bosque.score(X_test, y_test), 3))

importancias = pd.Series(bosque.feature_importances_, index=X.columns).sort_values()
importancias.plot(kind="barh", color="forestgreen")
plt.title("Importancia de variables — Random Forest")
plt.tight_layout()
plt.show()
```

## ⚠️ Errores frecuentes a vigilar

- Comparar accuracy solo en el conjunto de entrenamiento (siempre evaluar en test).
- Usar `max_depth` muy alto sin notar que el accuracy de test baja.
- Olvidar que `feature_importances_` suma 1: es una proporción, no un porcentaje absoluto.

## 🔗 Conexión con el siguiente módulo

La clase 21 introduce Gradient Boosting, donde los árboles se construyen en serie y cada uno aprende de los errores del anterior, logrando aún mayor precisión en datos tabulares.
