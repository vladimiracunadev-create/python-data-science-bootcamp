# 📖 Teoría — Clase 22: Clustering y segmentación

---

## 1. Aprendizaje supervisado vs. no supervisado

Hasta ahora hemos trabajado con aprendizaje **supervisado**: teníamos un conjunto de datos donde cada fila tenía una etiqueta (por ejemplo, si un correo es spam o no, si un estudiante aprobará o no). El modelo aprendía de esos ejemplos con respuesta conocida.

Pero en la vida real, la mayoría de los datos **no vienen con etiquetas**. Imagina que tienes millones de registros de compras de clientes. Nadie te dijo cuáles son los "tipos" de cliente — de hecho, quizás ni siquiera sabes cuántos tipos existen. Ahí es donde entra el aprendizaje **no supervisado**.

> **Aprendizaje no supervisado**: el algoritmo encuentra patrones, estructuras o grupos en los datos sin que le hayamos dado respuestas correctas de antemano.

---

## 2. ¿Qué es el clustering?

El **clustering** (o agrupamiento) es la tarea de encontrar grupos naturales en los datos. Los puntos dentro de un mismo grupo deben ser **muy similares entre sí**, y los puntos de grupos distintos deben ser **muy diferentes**.

Piénsalo así: si tuvieras que ordenar una biblioteca sin ninguna instrucción, probablemente agruparías los libros por tema, por autor o por tamaño. Eso es clustering: encontrar el criterio de agrupación a partir de los propios datos.

### Aplicaciones reales del clustering:
- **Segmentación de clientes**: ¿qué grupos de compradores tienen comportamientos similares?
- **Agrupación de noticias**: ¿cuáles hablan del mismo tema sin que nadie las haya etiquetado?
- **Medicina**: ¿hay subtipos de pacientes con perfiles similares?
- **Marketing**: ¿qué productos se compran juntos?

---

## 3. K-Means: el algoritmo más popular

**K-Means** es el algoritmo de clustering más utilizado. La K en su nombre representa el número de grupos que queremos encontrar. Es un parámetro que nosotros elegimos.

### ¿Cómo funciona K-Means?

El algoritmo sigue estos pasos (repite hasta converger):

1. **Inicialización**: coloca K "centros" (centroides) en posiciones al azar dentro del espacio de datos.
2. **Asignación**: cada punto de los datos se asigna al centroide más cercano. Distancia = distancia euclidiana (la misma que usarías con regla y papel).
3. **Actualización**: cada centroide se mueve al **promedio** de todos los puntos que tiene asignados.
4. **Convergencia**: se repiten los pasos 2 y 3 hasta que los centroides dejen de moverse (o el cambio sea muy pequeño).

### Visualización mental:
Imagina 20 personas en un parque. Pones 3 banderas (K=3). Cada persona camina hacia la bandera más cercana. Luego cada bandera se mueve al centro de las personas que la rodearon. Las personas vuelven a elegir la bandera más cercana. Repites hasta que nadie cambia de bandera.

### K-Means en sklearn:
```python
from sklearn.cluster import KMeans
import pandas as pd

# Preparar datos numéricos
X = df[['columna1', 'columna2']]

# Crear y entrenar el modelo
modelo = KMeans(n_clusters=3, random_state=42)
modelo.fit(X)

# Obtener resultados
df['cluster'] = modelo.labels_          # etiqueta de cluster para cada fila
centros = modelo.cluster_centers_       # coordenadas de los 3 centroides
inercia = modelo.inertia_               # suma de distancias al cuadrado
```

### Parámetros importantes:
- `n_clusters`: cuántos grupos queremos (el famoso K)
- `random_state`: semilla para reproducibilidad (mismo número = mismo resultado)
- `n_init`: cuántas veces reiniciar con centroides distintos (default=10, elige el mejor)

---

## 4. ¿Cómo elegir K? El Método del Codo

K-Means necesita que nosotros elijamos K. ¿Cómo sabemos cuántos grupos tiene sentido?

La **inercia** es la suma de las distancias al cuadrado de cada punto a su centroide. Cuanto menor la inercia, más compactos son los clusters.

- Con K=1 (un solo cluster), la inercia es máxima
- Con K=N (tantos clusters como puntos), la inercia es 0
- En algún punto intermedio, añadir más clusters deja de mejorar mucho la inercia

El **Método del Codo (Elbow Method)** consiste en graficar la inercia para distintos valores de K y buscar el punto donde la curva "dobla" — ese es el K óptimo.

```python
import matplotlib.pyplot as plt

inercias = []
valores_k = range(1, 11)

for k in valores_k:
    modelo = KMeans(n_clusters=k, random_state=42)
    modelo.fit(X)
    inercias.append(modelo.inertia_)

plt.plot(valores_k, inercias, marker='o')
plt.xlabel('Número de clusters (K)')
plt.ylabel('Inercia')
plt.title('Método del Codo')
plt.show()
```

> El "codo" no siempre es muy pronunciado. Es una guía, no una regla exacta. Combínalo con el Silhouette Score y con el sentido común del dominio.

---

## 5. Silhouette Score: medir la calidad del clustering

El **Silhouette Score** mide qué tan bien está asignado cada punto a su cluster:
- Compara la distancia promedio del punto a los demás puntos de su cluster (cohesión)
- vs. la distancia promedio al cluster vecino más cercano (separación)

**Rango: -1 a +1**
- **+1**: el punto está muy bien asignado (lejos de los demás clusters)
- **0**: el punto está en el borde entre dos clusters
- **-1**: el punto probablemente está en el cluster equivocado

```python
from sklearn.metrics import silhouette_score

score = silhouette_score(X, modelo.labels_)
print(f"Silhouette Score: {score:.3f}")
```

Un score mayor a 0.5 generalmente indica clusters bien definidos.

---

## 6. DBSCAN: clusters de cualquier forma

K-Means tiene una limitación importante: asume que los clusters son **esféricos** (redondeados). Si los datos tienen formas curvas, en L, en espiral, etc., K-Means fallará.

**DBSCAN** (Density-Based Spatial Clustering of Applications with Noise) es un algoritmo alternativo que:
- Encuentra clusters de **cualquier forma**
- Detecta automáticamente **outliers** (ruido) — los marca con etiqueta -1
- **No necesita que especifiques K**

Sus parámetros clave son:
- `eps`: radio máximo de vecindad para considerar puntos como vecinos
- `min_samples`: mínimo de puntos en una vecindad para formar un cluster

```python
from sklearn.cluster import DBSCAN

modelo_db = DBSCAN(eps=0.5, min_samples=5)
modelo_db.fit(X)
df['cluster_db'] = modelo_db.labels_  # -1 = outlier
```

---

## 7. Visualizar clusters

La visualización es clave para entender e interpretar los resultados:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))

scatter = ax.scatter(
    X['columna1'], X['columna2'],
    c=df['cluster'],
    cmap='tab10',
    alpha=0.7,
    edgecolors='k',
    linewidths=0.3
)

# Marcar los centroides
ax.scatter(
    centros[:, 0], centros[:, 1],
    marker='X', s=300,
    c='red', zorder=5,
    label='Centroides'
)

ax.set_xlabel('Columna 1')
ax.set_ylabel('Columna 2')
ax.set_title('Clusters K-Means')
ax.legend()
plt.colorbar(scatter, ax=ax, label='Cluster')
plt.show()
```

---

## 8. Interpretar los clusters: de números a negocio

El paso más importante no es técnico sino conceptual: **¿qué significa cada cluster?**

Después de crear los clusters, calcula el promedio de cada variable para cada grupo:

```python
perfil = df.groupby('cluster')[['columna1', 'columna2', 'columna3']].mean()
print(perfil)
```

Luego, dale un nombre descriptivo a cada grupo:
- Cluster 0: "Estudiantes con alto rendimiento en matemáticas"
- Cluster 1: "Estudiantes con bajo rendimiento general"
- Cluster 2: "Estudiantes con rendimiento equilibrado"

> Un buen análisis de clustering siempre termina con una historia: "Encontramos X tipos de [clientes/estudiantes/productos] con estas características..."

---

## 9. Limitaciones del clustering

- K-Means es sensible a **outliers extremos** (los jalan los centroides)
- K-Means asume clusters **esféricos y de tamaño similar**
- El resultado puede variar según la **inicialización** aleatoria
- No hay una respuesta "correcta" — múltiples agrupaciones pueden ser válidas
- Escalar las variables con `StandardScaler` es **muy recomendado** antes de K-Means

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

---

## Resumen de conceptos

| Concepto | Qué es |
|----------|--------|
| Clustering | Agrupar datos similares sin etiquetas |
| K-Means | Asigna puntos al centroide más cercano, iterativamente |
| Inercia | Suma de distancias al cuadrado al centroide |
| Método del Codo | Gráfica inercia vs K para elegir el mejor K |
| Silhouette Score | Mide qué tan bien separados están los clusters (-1 a +1) |
| DBSCAN | Clustering basado en densidad, detecta ruido |
| Centroide | Punto promedio de un cluster |
