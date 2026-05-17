# 🏋️ Ejercicios — Clase 23: Reducción de dimensionalidad — PCA

> Completa cada ejercicio en tu notebook. Escribe el código, ejecuta las celdas y responde las preguntas de reflexión.

---

## Ejercicio 1 — Preparar el dataset
**Nivel: Básico**

Carga `estudiantes.csv` y selecciona solo las columnas numéricas.

```python
import pandas as pd
import numpy as np

df = pd.read_csv('datasets/estudiantes.csv')
print(df.shape)
print(df.dtypes)
df.head()
```

**Preguntas de reflexión:**
1. ¿Cuántas columnas numéricas tiene el dataset?
2. ¿Hay correlaciones visibles entre columnas? Usa `df.corr()` para comprobarlo.
3. ¿Cuáles columnas crees que estarán más correlacionadas?

---

## Ejercicio 2 — Escalar antes de PCA
**Nivel: Básico**

```python
from sklearn.preprocessing import StandardScaler

# Seleccionar columnas numéricas
cols_num = df.select_dtypes(include='number').columns.tolist()
X = df[cols_num].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print(f'Columnas usadas: {cols_num}')
print(f'Forma: {X_scaled.shape}')
print(f'Media (debe ser ~0): {X_scaled.mean(axis=0).round(4)}')
print(f'Desv. est. (debe ser ~1): {X_scaled.std(axis=0).round(4)}')
```

**Preguntas de reflexión:**
1. ¿Por qué escalar ANTES de PCA y no después?
2. ¿Qué pasaría si una columna tiene rango 0-1 y otra rango 0-1000?

---

## Ejercicio 3 — Scree Plot: ¿cuántos componentes necesito?
**Nivel: Básico**

Antes de reducir a 2 dimensiones, averigua cuánta información captura cada componente.

```python
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# PCA completo (todos los componentes)
pca_full = PCA()
pca_full.fit(X_scaled)

varianza_acumulada = pca_full.explained_variance_ratio_.cumsum()
n_comp = len(varianza_acumulada)

# Scree Plot
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Individual
axes[0].bar(range(1, n_comp+1), pca_full.explained_variance_ratio_ * 100,
            color='steelblue')
axes[0].set_xlabel('Componente')
axes[0].set_ylabel('Varianza explicada (%)')
axes[0].set_title('Varianza por componente')

# Acumulada
axes[1].plot(range(1, n_comp+1), varianza_acumulada * 100,
             marker='o', color='coral')
axes[1].axhline(y=80, color='green', linestyle='--', label='80%')
axes[1].axhline(y=95, color='red', linestyle='--', label='95%')
axes[1].set_xlabel('Número de componentes')
axes[1].set_ylabel('Varianza acumulada (%)')
axes[1].set_title('Varianza acumulada')
axes[1].legend()

plt.tight_layout()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Cuántos componentes necesitas para explicar el 80% de la varianza?
2. ¿Cuántos para el 95%?
3. ¿Vale la pena quedarse con 2 componentes? ¿Qué porcentaje representan?

---

## Ejercicio 4 — Reducir a 2 dimensiones
**Nivel: Básico**

```python
# Aplicar PCA con 2 componentes
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f'Forma original:  {X_scaled.shape}')
print(f'Forma reducida:  {X_pca.shape}')
print(f'\nVarianza explicada:')
print(f'  PC1: {pca.explained_variance_ratio_[0]*100:.1f}%')
print(f'  PC2: {pca.explained_variance_ratio_[1]*100:.1f}%')
print(f'  Total: {pca.explained_variance_ratio_.sum()*100:.1f}%')
```

**Preguntas de reflexión:**
1. ¿Qué porcentaje de información "perdimos" al reducir?
2. ¿Ese porcentaje de pérdida es aceptable?

---

## Ejercicio 5 — Visualizar en 2D
**Nivel: Básico**

```python
plt.figure(figsize=(8, 6))
plt.scatter(
    X_pca[:, 0], X_pca[:, 1],
    alpha=0.6, edgecolors='k', linewidths=0.3, s=50
)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% varianza)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% varianza)')
plt.title('Estudiantes en espacio 2D (PCA)')
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.tight_layout()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Ves alguna estructura en la nube de puntos? ¿Grupos visibles?
2. ¿Hay outliers (puntos muy alejados del resto)?

---

## Ejercicio 6 — Biplot: variables y muestras juntas
**Nivel: Intermedio**

```python
fig, ax = plt.subplots(figsize=(9, 7))

# Puntos (muestras)
ax.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.4, s=30, color='steelblue')

# Vectores (variables originales)
loadings = pca.components_.T
escala = 2.5

for i, nombre in enumerate(cols_num):
    ax.arrow(0, 0,
             loadings[i, 0] * escala,
             loadings[i, 1] * escala,
             head_width=0.08, head_length=0.04,
             fc='red', ec='darkred', linewidth=1.5)
    ax.text(loadings[i, 0] * escala * 1.15,
            loadings[i, 1] * escala * 1.15,
            nombre, fontsize=9, color='darkred', ha='center')

ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_title('Biplot PCA — Estudiantes')
plt.tight_layout()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Qué variables apuntan en la misma dirección? (están correlacionadas positivamente)
2. ¿Hay alguna variable que apunta en dirección opuesta a las demás?
3. ¿Cuál variable tiene el vector más largo? ¿Qué significa eso?

---

## Ejercicio 7 — PCA + Clustering
**Nivel: Intermedio**

Combina PCA con K-Means del capítulo anterior.

```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Aplicar K-Means en el espacio PCA 2D
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
etiquetas = kmeans.fit_predict(X_pca)

score = silhouette_score(X_pca, etiquetas)
print(f'Silhouette Score (en espacio PCA): {score:.3f}')

# Visualizar
plt.figure(figsize=(9, 6))
colores = ['#2196F3', '#FF5722', '#4CAF50']
for i in range(3):
    mask = etiquetas == i
    plt.scatter(X_pca[mask, 0], X_pca[mask, 1],
                c=colores[i], label=f'Cluster {i}', alpha=0.7, s=50)

centros_pca = kmeans.cluster_centers_
plt.scatter(centros_pca[:, 0], centros_pca[:, 1],
            marker='X', s=250, color='black', zorder=5, label='Centroides')

plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('K-Means en espacio PCA')
plt.legend()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Los clusters se ven claramente separados en el espacio PCA?
2. Compara con el clustering directo (sin PCA) de la clase anterior. ¿Cuál se ve mejor?

---

## Ejercicio 8 — Aplicar al dataset de ventas
**Nivel: Avanzado**

Repite el análisis completo con `ventas_tienda.csv`.

```python
df_v = pd.read_csv('datasets/ventas_tienda.csv')
cols_v = df_v.select_dtypes(include='number').columns.tolist()
X_v = df_v[cols_v].dropna()

# Escalar → PCA → Visualizar
# (escribe el código completo aquí)
```

**Pasos:**
1. Escalar los datos
2. Hacer el Scree Plot para elegir número de componentes
3. Reducir a 2 componentes
4. Graficar el scatter plot 2D
5. Crear el biplot
6. Aplicar K-Means en el espacio PCA

**Entrega:** Un párrafo describiendo qué revelaron los componentes principales sobre el dataset de ventas.
