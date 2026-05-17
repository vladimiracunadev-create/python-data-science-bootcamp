# 💻 Guía de código — Clase 20: Árboles de Decisión y Random Forest

> Walkthrough del código clave, bloque por bloque.

## Bloque 1: Árbol de decisión y demostración de sobreajuste

```python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("estudiantes.csv")
features = ["horas_estudio", "ausencias", "promedio_anterior", "edad"]
X = df[features]
y = df["aprobado"]  # 1 = aprobó, 0 = reprobó

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Árbol superficial: generaliza bien
arbol_simple = DecisionTreeClassifier(max_depth=3, random_state=42)
arbol_simple.fit(X_train, y_train)
print("Árbol max_depth=3:")
print(f"  Train accuracy: {arbol_simple.score(X_train, y_train):.4f}")
print(f"  Test  accuracy: {arbol_simple.score(X_test, y_test):.4f}")

# Árbol profundo: memoriza el entrenamiento
arbol_profundo = DecisionTreeClassifier(max_depth=20, random_state=42)
arbol_profundo.fit(X_train, y_train)
print("\nÁrbol max_depth=20:")
print(f"  Train accuracy: {arbol_profundo.score(X_train, y_train):.4f}")
print(f"  Test  accuracy: {arbol_profundo.score(X_test, y_test):.4f}")
```

**¿Qué hace?** Compara dos árboles con distinta profundidad para mostrar el efecto del sobreajuste: el árbol profundo "memoriza" los datos de entrenamiento pero falla con datos nuevos.

**¿Por qué así?** `max_depth` controla cuántas preguntas puede hacer el árbol. Sin límite, el árbol crea una regla para cada ejemplo del entrenamiento (overfitting perfecto).

**Resultado esperado:** El árbol `max_depth=20` tendrá ~99% en train pero mucho menos en test. El `max_depth=3` tendrá valores más parecidos entre train y test.

---

## Bloque 2: Visualizar el árbol de decisión

```python
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(16, 6))
plot_tree(
    arbol_simple,
    feature_names=features,
    class_names=["Reprobó", "Aprobó"],
    filled=True,       # colores por clase mayoritaria
    rounded=True,      # nodos redondeados
    fontsize=10
)
plt.title("Árbol de Decisión — max_depth=3")
plt.tight_layout()
plt.show()
```

**¿Qué hace?** Dibuja el árbol completo mostrando en cada nodo: la pregunta (feature y umbral), la impureza de Gini, el número de muestras y la clase predicha.

**¿Por qué así?** `filled=True` colorea cada nodo según la clase mayoritaria, haciendo muy visual qué regiones del espacio de datos llevan a cada predicción.

**Resultado esperado:** Un árbol con hasta 3 niveles de profundidad. El nodo raíz muestra la variable más informativa (menor Gini tras el split).

---

## Bloque 3: Random Forest y feature importances

```python
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Entrenar Random Forest
rf = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
rf.fit(X_train, y_train)

print(f"Random Forest — Test accuracy: {rf.score(X_test, y_test):.4f}")

# Extraer y graficar importancia de variables
importancias = rf.feature_importances_
índices = np.argsort(importancias)  # ordenar de menor a mayor

plt.figure(figsize=(8, 4))
plt.barh(
    [features[i] for i in índices],
    importancias[índices],
    color="steelblue"
)
plt.xlabel("Importancia (Gini promedio)")
plt.title("Importancia de variables — Random Forest")
plt.tight_layout()
plt.show()
```

**¿Qué hace?** Entrena 100 árboles sobre muestras bootstrap distintas y promedia sus predicciones. `feature_importances_` muestra qué variables redujeron más la impureza en promedio a lo largo de todos los árboles.

**¿Por qué así?** `n_estimators=100` es un buen punto de partida: suficientes árboles para estabilizar la predicción sin ser excesivamente lento. Más árboles = más robusto pero más costoso.

**Resultado esperado:** La accuracy del RF debería superar a la del árbol simple. El gráfico mostrará qué variable (ej: `ausencias` o `horas_estudio`) es la más predictiva.

---

## ⚠️ Errores comunes y cómo resolverlos

| Error | Por qué ocurre | Solución |
|---|---|---|
| Alta accuracy en train, baja en test con árbol | Árbol demasiado profundo (overfitting) | Reducir `max_depth` (probar 3, 5, 7) o usar `min_samples_leaf` |
| `plot_tree` genera una imagen ilegible | El árbol tiene demasiados nodos para mostrar | Limitar `max_depth=3` o `max_depth=4` solo para la visualización |
| `feature_importances_` da 0 a todas las variables | La variable objetivo está entre los features (data leakage) | Verificar que `y` no esté incluida en `X` |
| Random Forest tarda mucho en entrenar | Demasiados estimadores o dataset muy grande | Reducir `n_estimators` a 50 o usar `n_jobs=-1` para paralelizar |
