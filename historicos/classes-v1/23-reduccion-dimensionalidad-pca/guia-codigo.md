# 💻 Guía de código — Clase 23: Reducción de Dimensionalidad y PCA

> Walkthrough del código clave, bloque por bloque.

## Bloque 1: Aplicar PCA y graficar en 2D

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("estudiantes.csv")
features = ["horas_estudio", "ausencias", "promedio_anterior", "edad",
            "participacion", "tareas_entregadas"]
X = df[features]
y = df["aprobado"]  # para colorear

# Paso 1: SIEMPRE normalizar antes de PCA
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Paso 2: Aplicar PCA a 2 componentes para visualización
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f"Varianza explicada por componente: {pca.explained_variance_ratio_}")
print(f"Varianza total explicada (2 componentes): {pca.explained_variance_ratio_.sum():.2%}")

# Paso 3: Visualizar
plt.figure(figsize=(8, 6))
colores = {0: "#DD8452", 1: "#4C72B0"}
for clase in [0, 1]:
    mask = y == clase
    label = "Aprobó" if clase == 1 else "Reprobó"
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1],
                label=label, alpha=0.6, color=colores[clase])
plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]:.1%} varianza)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]:.1%} varianza)")
plt.title("PCA — Estudiantes en 2 componentes principales")
plt.legend()
plt.tight_layout()
plt.show()
```

**¿Qué hace?** Reduce 6 variables a 2 dimensiones preservando la mayor varianza posible, permitiendo visualizar los datos en 2D y ver si las clases se separan.

**¿Por qué así?** `StandardScaler` es obligatorio: si una variable está en miles y otra en unidades, PCA priorizará la de mayor escala, no la más informativa. La normalización pone todas las variables en el mismo plano.

**Resultado esperado:** Un scatter 2D donde idealmente los puntos de "Aprobó" y "Reprobó" forman nubes separadas, indicando que las variables tienen poder discriminativo.

---

## Bloque 2: Scree plot — varianza acumulada por componente

```python
import numpy as np

# PCA completo (tantos componentes como variables)
pca_completo = PCA()
pca_completo.fit(X_scaled)

varianza_acumulada = np.cumsum(pca_completo.explained_variance_ratio_)
n_componentes = range(1, len(varianza_acumulada) + 1)

plt.figure(figsize=(8, 4))
plt.bar(n_componentes, pca_completo.explained_variance_ratio_,
        alpha=0.5, label="Varianza por componente", color="steelblue")
plt.plot(n_componentes, varianza_acumulada,
         marker="o", color="coral", label="Varianza acumulada")
plt.axhline(y=0.90, linestyle="--", color="gray", label="90% umbral")
plt.xlabel("Número de componentes")
plt.ylabel("Proporción de varianza explicada")
plt.title("Scree Plot — Varianza acumulada")
plt.legend()
plt.tight_layout()
plt.show()

# ¿Cuántos componentes para el 90%?
n_90 = np.argmax(varianza_acumulada >= 0.90) + 1
print(f"Componentes para explicar el 90% de la varianza: {n_90}")
```

**¿Qué hace?** Muestra cuánta varianza explica cada componente (barras) y la acumulación progresiva (línea). La línea horizontal al 90% indica cuántos componentes son suficientes.

**¿Por qué así?** El scree plot es la herramienta estándar para elegir cuántos componentes conservar. El criterio del 80-90% de varianza es una regla práctica común.

**Resultado esperado:** Una curva que sube rápido al principio y se aplana. Si con 3-4 componentes de 6 llegas al 90%, puedes reducir la dimensionalidad a la mitad sin perder mucha información.

---

## Bloque 3: Pipeline PCA + clustering

```python
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Pipeline: normalizar → PCA → KMeans
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("pca", PCA(n_components=2)),
    ("kmeans", KMeans(n_clusters=3, random_state=42, n_init=10))
])

etiquetas = pipeline.fit_predict(X)

# Obtener coordenadas PCA para visualizar
X_pca_pipe = pipeline[:-1].transform(X)  # todo excepto el último paso

plt.figure(figsize=(8, 5))
scatter = plt.scatter(X_pca_pipe[:, 0], X_pca_pipe[:, 1],
                      c=etiquetas, cmap="tab10", alpha=0.7)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("Clusters K-Means sobre espacio PCA")
plt.colorbar(scatter, label="Cluster")
plt.tight_layout()
plt.show()

# Silhouette sobre el espacio PCA
sil = silhouette_score(X_pca_pipe, etiquetas)
print(f"Silhouette score (PCA + KMeans): {sil:.4f}")
```

**¿Qué hace?** Combina preprocesamiento, reducción y clustering en un pipeline limpio y reproducible. Visualiza los clusters directamente en el espacio de 2 componentes principales.

**¿Por qué así?** El Pipeline de sklearn garantiza que el scaler y el PCA se ajustan solo con los datos de entrenamiento, evitando data leakage. Es la forma correcta de encadenar transformaciones en producción.

**Resultado esperado:** Un scatter 2D con 3 grupos de colores distintos. El silhouette score debería ser razonablemente alto si los datos tienen estructura natural.

---

## ⚠️ Errores comunes y cómo resolverlos

| Error | Por qué ocurre | Solución |
|---|---|---|
| PCA da componentes que no explican casi nada | No se normalizaron los datos; una variable domina por escala | Aplicar `StandardScaler` antes de `PCA` siempre |
| `explained_variance_ratio_` no suma 1 | Se usó `n_components` menor al número de variables | Usar `PCA()` sin argumentos para el scree plot completo |
| El scatter PCA no muestra separación entre clases | Las variables numéricas usadas no discriminan bien la variable objetivo | Revisar correlaciones; quizás la separación no es lineal (probar t-SNE) |
| Error al usar `pipeline[:-1].transform(X)` | Versión antigua de sklearn que no soporta slicing de pipelines | Usar `Pipeline(pipeline.steps[:-1]).transform(X)` como alternativa |
