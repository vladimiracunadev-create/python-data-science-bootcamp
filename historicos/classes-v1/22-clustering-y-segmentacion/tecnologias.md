# 🔧 Tecnologías complementarias — Clase 22: Clustering y Segmentación

> Herramientas y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `sklearn.cluster.AgglomerativeClustering` | Clustering jerárquico: construye un dendrograma sin necesitar k a priori | Intermedio |
| `sklearn.cluster.MeanShift` | Encuentra clusters sin especificar k, basado en densidad | Intermedio |
| `scipy.cluster.hierarchy` | Dendrogramas para clustering jerárquico, útil para visualizar relaciones | Intermedio |
| `sklearn.preprocessing.StandardScaler` | Normalización esencial antes de K-Means (sin esto, las variables de mayor escala dominan) | Básico |
| `yellowbrick.cluster.KElbowVisualizer` | Visualización automática del método del codo con más opciones | Intermedio |
| `umap-learn` | Reducción de dimensionalidad no lineal, ideal para visualizar clusters en 2D | Avanzado |

## 🌐 Recursos recomendados

- **Documentación oficial**: https://scikit-learn.org/stable/modules/clustering.html
- **Tutorial recomendado**: "K-Means Clustering in Python — A Practical Guide" — Real Python
- **Concepto clave para buscar**: "customer segmentation RFM analysis" — marco clásico de negocio para segmentar clientes con clustering

## 🚀 Próximos pasos sugeridos

- Aprender clustering jerárquico con dendrogramas para casos donde el número de clusters no está claro
- Estudiar RFM (Recencia, Frecuencia, Monto) como framework de negocio para usar con K-Means
- Explorar UMAP para visualizar clusters en datasets de alta dimensionalidad
- Practicar la interpretación de negocio de clusters: dar nombre y estrategia a cada segmento

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `sklearn.mixture.GaussianMixture` | Clustering probabilístico: cada punto tiene probabilidad de pertenecer a cada cluster | Cuando los clusters se superponen o quieres "suavidad" en las asignaciones |
| `hdbscan` | DBSCAN jerárquico, más robusto y con menos parámetros para ajustar | Cuando DBSCAN da resultados inestables al cambiar eps |
| `Tableau / Power BI` | Visualización interactiva de clusters para presentaciones de negocio | Para comunicar segmentación a equipos no técnicos |
