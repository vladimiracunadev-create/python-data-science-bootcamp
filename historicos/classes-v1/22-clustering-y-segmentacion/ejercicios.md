# 🏋️ Ejercicios — Clase 22: Clustering y segmentación

> Completa cada ejercicio en tu notebook. Escribe el código, ejecuta las celdas y responde las preguntas de reflexión.

---

## Ejercicio 1 — Carga y exploración inicial
**Nivel: Básico**

Carga el dataset `ventas_tienda.csv` y explóralo.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/ventas_tienda.csv')
print(df.shape)
print(df.head())
print(df.dtypes)
print(df.describe())
```

**Preguntas de reflexión:**
1. ¿Cuántas filas y columnas tiene el dataset?
2. ¿Qué columnas numéricas podrían ser útiles para clustering?
3. ¿Hay valores nulos? Si los hay, ¿cómo los manejarías?

---

## Ejercicio 2 — Preparar los datos para K-Means
**Nivel: Básico**

Selecciona dos columnas numéricas y escálalas con `StandardScaler`.

```python
from sklearn.preprocessing import StandardScaler

# Selecciona las columnas que usarás
columnas = ['columna1', 'columna2']  # reemplaza con las columnas reales
X = df[columnas].dropna()

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("Media antes:", X.mean().values)
print("Media después:", X_scaled.mean().round(3))
print("Desv. estándar después:", X_scaled.std().round(3))
```

**Preguntas de reflexión:**
1. ¿Por qué es importante escalar antes de K-Means?
2. ¿Qué pasaría si una columna tiene rango 0-100 y otra rango 0-1,000,000?

---

## Ejercicio 3 — Aplicar K-Means con K=3
**Nivel: Básico**

Aplica K-Means con 3 clusters y visualiza los resultados.

```python
from sklearn.cluster import KMeans
import numpy as np

# Entrenar el modelo
modelo = KMeans(n_clusters=3, random_state=42)
modelo.fit(X_scaled)

# Agregar la etiqueta al dataframe original
X_con_clusters = X.copy()
X_con_clusters['cluster'] = modelo.labels_

# Visualizar
plt.figure(figsize=(8, 6))
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 1],
    c=modelo.labels_, cmap='tab10', alpha=0.7
)
plt.scatter(
    modelo.cluster_centers_[:, 0],
    modelo.cluster_centers_[:, 1],
    marker='X', s=200, color='red', label='Centroides'
)
plt.xlabel(columnas[0])
plt.ylabel(columnas[1])
plt.title('K-Means con K=3')
plt.legend()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Los clusters se ven bien separados o hay superposición?
2. ¿Cuántos puntos tiene cada cluster? (usa `X_con_clusters['cluster'].value_counts()`)

---

## Ejercicio 4 — Método del Codo
**Nivel: Intermedio**

Determina el número óptimo de clusters usando la inercia.

```python
inercias = []
valores_k = range(1, 11)

for k in valores_k:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inercias.append(km.inertia_)

plt.figure(figsize=(8, 4))
plt.plot(valores_k, inercias, marker='o', color='steelblue')
plt.xlabel('Número de clusters (K)')
plt.ylabel('Inercia')
plt.title('Método del Codo — Inercia vs K')
plt.xticks(valores_k)
plt.grid(alpha=0.3)
plt.show()
```

**Preguntas de reflexión:**
1. ¿En qué valor de K ves el "codo" de la curva?
2. ¿Coincide con K=3 o sugerirías otro valor?
3. ¿Qué significa que la inercia baje poco al agregar más clusters?

---

## Ejercicio 5 — Silhouette Score
**Nivel: Intermedio**

Calcula el Silhouette Score para K=2, 3, 4 y 5.

```python
from sklearn.metrics import silhouette_score

scores = {}
for k in range(2, 6):
    km = KMeans(n_clusters=k, random_state=42)
    labels = km.fit_predict(X_scaled)
    scores[k] = silhouette_score(X_scaled, labels)
    print(f"K={k}: Silhouette Score = {scores[k]:.3f}")

# Graficar
plt.figure(figsize=(6, 4))
plt.bar(list(scores.keys()), list(scores.values()), color='coral')
plt.xlabel('K')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score por número de clusters')
plt.show()
```

**Preguntas de reflexión:**
1. ¿Qué valor de K tiene el mayor Silhouette Score?
2. ¿Coincide la recomendación del Silhouette con la del Método del Codo?
3. Un score de 0.45 — ¿es bueno o malo? ¿Qué significa?

---

## Ejercicio 6 — Perfil de los clusters
**Nivel: Intermedio**

Interpreta qué representa cada cluster calculando sus promedios.

```python
# Unir etiquetas con datos originales
X_con_clusters = X.copy()
X_con_clusters['cluster'] = modelo.labels_

# Perfil promedio por cluster
perfil = X_con_clusters.groupby('cluster').mean().round(2)
print("Perfil promedio por cluster:")
print(perfil)

# Cantidad de registros por cluster
conteo = X_con_clusters['cluster'].value_counts().sort_index()
print("\nConteo por cluster:")
print(conteo)
```

**Tarea:** Basándote en los valores promedio, ponle un nombre descriptivo a cada cluster.

| Cluster | Nombre propuesto | Justificación |
|---------|-----------------|---------------|
| 0       |                 |               |
| 1       |                 |               |
| 2       |                 |               |

---

## Ejercicio 7 — DBSCAN (exploración)
**Nivel: Avanzado**

Aplica DBSCAN al mismo dataset y compara con K-Means.

```python
from sklearn.cluster import DBSCAN

db = DBSCAN(eps=0.5, min_samples=5)
db.fit(X_scaled)

n_clusters_db = len(set(db.labels_)) - (1 if -1 in db.labels_ else 0)
n_ruido = list(db.labels_).count(-1)

print(f"Clusters encontrados: {n_clusters_db}")
print(f"Puntos de ruido (outliers): {n_ruido}")

plt.figure(figsize=(8, 6))
plt.scatter(
    X_scaled[:, 0], X_scaled[:, 1],
    c=db.labels_, cmap='tab10', alpha=0.7
)
plt.title(f'DBSCAN — {n_clusters_db} clusters, {n_ruido} outliers')
plt.xlabel(columnas[0])
plt.ylabel(columnas[1])
plt.show()
```

**Preguntas de reflexión:**
1. ¿DBSCAN encontró el mismo número de clusters que K-Means?
2. ¿Hay muchos outliers? ¿Qué representan en el contexto del dataset?
3. Cambia `eps` a 0.3 y a 1.0. ¿Cómo cambian los resultados?

---

## Ejercicio 8 — Dataset de estudiantes
**Nivel: Avanzado**

Repite el análisis completo con `estudiantes.csv`.

```python
df_est = pd.read_csv('datasets/estudiantes.csv')
print(df_est.head())
print(df_est.describe())
```

**Pasos a seguir:**
1. Selecciona columnas numéricas de desempeño académico
2. Escala con StandardScaler
3. Aplica el Método del Codo para elegir K
4. Entrena K-Means con el K elegido
5. Visualiza los clusters
6. Calcula el perfil de cada cluster
7. Nombra cada cluster (por ejemplo: "alto rendimiento", "rendimiento bajo", "en progreso")

**Entrega:** Un párrafo describiendo los segmentos encontrados y su posible aplicación pedagógica.
