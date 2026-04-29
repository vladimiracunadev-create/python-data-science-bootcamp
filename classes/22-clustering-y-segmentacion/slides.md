# 🎞️ Slides — Clase 22: Clustering y segmentación

---

## Diapositiva 1 — Título
# Clustering y segmentación
### ¿Cómo encuentra el algoritmo grupos en los datos sin que nadie le diga cuáles son?

---

## Diapositiva 2 — La pregunta clave
## ¿Qué pasa cuando no tienes etiquetas?
- En clasificación sabemos: "este correo ES spam, este NO es spam"
- ¿Y si nadie nos dijo qué es qué?
- **Aprendizaje no supervisado**: el algoritmo descubre la estructura por sí solo
- No predice una categoría conocida → **descubre categorías desconocidas**

---

## Diapositiva 3 — La analogía de los M&Ms
## Imagina que tienes un bolsa de M&Ms mezclados
- Te piden ordenarlos sin decirte el criterio
- Probablemente los agrupes por **color**
- Quizás también por **tamaño**
- Eso es exactamente lo que hace K-Means:
  - Busca grupos donde los elementos se parezcan entre sí
  - Y sean distintos de los otros grupos

---

## Diapositiva 4 — ¿Qué es el Clustering?
## Clustering = agrupar sin etiquetas
- Se buscan **grupos naturales** (clusters) en los datos
- Los puntos dentro de un cluster son **similares entre sí**
- Los puntos de distintos clusters son **diferentes entre sí**
- Aplicaciones reales:
  - Segmentación de clientes (¿quiénes compran igual?)
  - Agrupación de productos similares
  - Detección de grupos de estudiantes con rendimiento parecido

---

## Diapositiva 5 — K-Means paso a paso
## Cómo funciona K-Means
1. **Elegimos K** (número de grupos que queremos)
2. Colocamos K centros al azar
3. Cada punto se asigna al centro más cercano
4. Los centros se mueven al promedio de su grupo
5. Repetimos 3 y 4 hasta que los centros no se muevan más

> Es como si el algoritmo reorganizara los M&Ms una y otra vez hasta que cada pila sea lo más compacta posible.

---

## Diapositiva 6 — K-Means en código
## sklearn lo hace en 3 líneas
```python
from sklearn.cluster import KMeans

modelo = KMeans(n_clusters=3, random_state=42)
modelo.fit(X)

etiquetas = modelo.labels_          # grupo de cada punto
centros   = modelo.cluster_centers_ # coordenadas de los centros
```

---

## Diapositiva 7 — ¿Cuántos grupos elijo? El Método del Codo
## El problema: K-Means necesita que tú elijas K
- Si K es muy pequeño: grupos muy mezclados (mala separación)
- Si K es muy grande: demasiados grupos, sin sentido
- **Solución: Método del Codo**
  - Probamos K = 1, 2, 3, ... 10
  - Medimos la **inercia** (suma de distancias al centro)
  - Graficamos: donde la curva "dobla" es el K ideal

---

## Diapositiva 8 — Silhouette Score
## ¿Qué tan bueno es mi clustering?
- El **Silhouette Score** mide qué tan bien separados están los grupos
- Va de **-1 a +1**:
  - Cerca de **+1** → clusters bien definidos ✅
  - Cerca de **0** → grupos solapados ⚠️
  - Cerca de **-1** → puntos en el grupo equivocado ❌
```python
from sklearn.metrics import silhouette_score
score = silhouette_score(X, etiquetas)
```

---

## Diapositiva 9 — DBSCAN: cuando los grupos tienen formas raras
## K-Means solo funciona bien con grupos "redondos"
- Si los grupos tienen formas irregulares, K-Means falla
- **DBSCAN** (Density-Based Spatial Clustering)
  - Encuentra clusters de cualquier forma
  - Detecta puntos de **ruido** (outliers) → los marca con -1
  - No necesita que elijas K

---

## Diapositiva 10 — Visualización de clusters
## Ver los grupos en un gráfico
```python
import matplotlib.pyplot as plt

plt.scatter(X['col1'], X['col2'], c=etiquetas, cmap='viridis')
plt.scatter(centros[:, 0], centros[:, 1],
            marker='X', s=200, color='red', label='Centros')
plt.legend()
plt.title('Clusters K-Means')
plt.show()
```
- El color de cada punto indica su cluster
- Las X rojas son los centros

---

## Diapositiva 11 — Interpretación de negocio
## Los clusters deben tener significado
| Cluster | Característica principal | Nombre propuesto |
|---------|--------------------------|------------------|
| 0       | Ventas altas, precio bajo | "Masivo económico" |
| 1       | Ventas bajas, precio alto | "Premium exclusivo" |
| 2       | Ventas medias, precio medio | "Estándar regular" |

> Nombrar los clusters convierte el análisis técnico en decisiones de negocio.

---

## Diapositiva 12 — Resumen
## Lo que aprendimos hoy
- El clustering agrupa datos **sin etiquetas**
- **K-Means** asigna puntos a centros y los mueve iterativamente
- El **Método del Codo** nos ayuda a elegir K
- El **Silhouette Score** mide la calidad del clustering
- **DBSCAN** maneja formas irregulares y ruido
- Siempre hay que **interpretar** qué significa cada grupo

---

## Diapositiva 13 — Tarea para casa
## Homework — Clase 22
- Aplica K-Means al dataset `estudiantes.csv`
- Usa las columnas numéricas de desempeño
- Elige K con el Método del Codo
- Nombra cada grupo según sus características
- Entrega: notebook con visualización y tabla interpretativa
