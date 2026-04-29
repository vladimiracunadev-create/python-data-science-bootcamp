# 💻 Guía de código — Clase 22: Clustering y Segmentación

> Walkthrough del código clave, bloque por bloque.

## Bloque 1: K-Means y método del codo

```python
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("ventas_tienda.csv")
features = ["ticket_promedio", "frecuencia_compra"]
X = df[features]

# IMPORTANTE: normalizar antes de K-Means
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Calcular inercia para distintos valores de k
inercias = []
rango_k = range(1, 9)

for k in rango_k:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inercias.append(km.inertia_)

# Método del codo
plt.figure(figsize=(8, 4))
plt.plot(rango_k, inercias, marker="o", color="steelblue")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Inercia")
plt.title("Método del codo — K-Means")
plt.xticks(rango_k)
plt.tight_layout()
plt.show()
```

**¿Qué hace?** Prueba K-Means con distintos valores de k y grafica la inercia (suma de distancias al centroide más cercano). El codo visual indica el k óptimo.

**¿Por qué así?** Normalizar con `StandardScaler` es obligatorio antes de K-Means: sin esto, una variable en miles (ej: ventas) domina completamente sobre una en unidades (ej: frecuencia).

**Resultado esperado:** Una curva que baja rápido y luego se aplana. El "codo" (donde la curva empieza a ser casi horizontal) indica el k recomendado.

---

## Bloque 2: Silhouette score y selección del k óptimo

```python
from sklearn.metrics import silhouette_score

silhouettes = []
rango_k_sil = range(2, 9)  # silhouette requiere al menos 2 clusters

for k in rango_k_sil:
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    etiquetas = km.fit_predict(X_scaled)
    score = silhouette_score(X_scaled, etiquetas)
    silhouettes.append(score)
    print(f"k={k}: silhouette = {score:.4f}")

plt.figure(figsize=(8, 4))
plt.plot(rango_k_sil, silhouettes, marker="s", color="coral")
plt.xlabel("Número de clusters (k)")
plt.ylabel("Silhouette score")
plt.title("Silhouette score por número de clusters")
plt.xticks(rango_k_sil)
plt.tight_layout()
plt.show()

k_optimo = rango_k_sil[silhouettes.index(max(silhouettes))]
print(f"\nMejor k según silhouette: {k_optimo}")
```

**¿Qué hace?** Calcula el silhouette score para cada k posible. Este score mide qué tan bien separados están los clusters: cerca de 1 es perfecto, cerca de 0 es solapamiento, negativo es asignación incorrecta.

**¿Por qué así?** El método del codo es subjetivo (el "codo" no siempre es claro). Silhouette ofrece un valor numérico que maximizar, lo que hace la elección más objetiva.

**Resultado esperado:** El k con mayor silhouette score es el candidato óptimo. Si coincide con el codo visual, la elección es más confiable.

---

## Bloque 3: Visualizar clusters y DBSCAN

```python
from sklearn.cluster import KMeans, DBSCAN
import numpy as np

# Aplicar K-Means con k óptimo
km_final = KMeans(n_clusters=k_optimo, random_state=42, n_init=10)
df["cluster_kmeans"] = km_final.fit_predict(X_scaled)

# Visualizar K-Means
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
colores = ["#4C72B0", "#DD8452", "#55A868", "#C44E52"]
for cluster in df["cluster_kmeans"].unique():
    mask = df["cluster_kmeans"] == cluster
    plt.scatter(df.loc[mask, "ticket_promedio"],
                df.loc[mask, "frecuencia_compra"],
                label=f"Cluster {cluster}", alpha=0.6,
                color=colores[cluster % len(colores)])
plt.xlabel("Ticket promedio")
plt.ylabel("Frecuencia de compra")
plt.title("Segmentación K-Means")
plt.legend()

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)
df["cluster_dbscan"] = dbscan.fit_predict(X_scaled)

plt.subplot(1, 2, 2)
scatter = plt.scatter(df["ticket_promedio"], df["frecuencia_compra"],
                      c=df["cluster_dbscan"], cmap="tab10", alpha=0.6)
plt.title(f"DBSCAN — clusters: {df['cluster_dbscan'].nunique() - 1} + ruido")
plt.xlabel("Ticket promedio")
plt.colorbar(scatter)

plt.tight_layout()
plt.show()

# Resumen por cluster
print(df.groupby("cluster_kmeans")[features].mean().round(2))
```

**¿Qué hace?** Visualiza los clusters de K-Means con colores distintos y los compara con DBSCAN. El resumen por cluster permite interpretar qué tipo de cliente representa cada grupo.

**¿Por qué así?** DBSCAN usa -1 para los puntos de ruido (outliers). El scatter coloreado con `cmap` hace visualmente inmediata la diferencia entre ambos algoritmos.

**Resultado esperado:** K-Means crea grupos compactos y esféricos; DBSCAN puede encontrar formas irregulares y marcará puntos aislados como ruido. El resumen de medias te dice ej: "Cluster 0 = clientes con ticket alto pero compra poco frecuente".

---

## ⚠️ Errores comunes y cómo resolverlos

| Error | Por qué ocurre | Solución |
|---|---|---|
| Clusters muy desiguales en tamaño (ej: 1 punto vs 499) | Outliers extremos jalan un centroide hacia ellos | Normalizar con `StandardScaler` y remover outliers antes de clustering |
| K-Means da resultados distintos en cada ejecución | Inicialización aleatoria de centroides | Usar `random_state=42` y `n_init=10` para estabilizar |
| DBSCAN marca casi todo como ruido | `eps` muy pequeño para la escala de los datos | Aumentar `eps` o normalizar los datos primero con `StandardScaler` |
| Silhouette score muy bajo para todos los k | Los datos no tienen estructura natural de clusters | Revisar si el problema realmente se presta a clustering; considerar más features |
