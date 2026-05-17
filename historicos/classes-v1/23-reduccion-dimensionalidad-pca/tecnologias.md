# 🔧 Tecnologías complementarias — Clase 23: Reducción de Dimensionalidad y PCA

> Herramientas y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `sklearn.decomposition.TruncatedSVD` | PCA para matrices dispersas (sparse), útil en NLP | Avanzado |
| `sklearn.manifold.TSNE` | Reducción no lineal, excelente para visualizar clusters complejos en 2D | Intermedio |
| `umap-learn` | Reducción no lineal más rápida que t-SNE, preserva estructura global y local | Avanzado |
| `sklearn.decomposition.NMF` | Factorización matricial no negativa, útil para datos de texto o imágenes | Avanzado |
| `seaborn.pairplot` | Visualiza relaciones entre todas las variables antes de decidir si aplicar PCA | Básico |
| `sklearn.pipeline.Pipeline` | Encadena StandardScaler + PCA + modelo en un solo objeto reutilizable | Intermedio |

## 🌐 Recursos recomendados

- **Documentación oficial**: https://scikit-learn.org/stable/modules/decomposition.html#pca
- **Tutorial recomendado**: "PCA using Python (scikit-learn)" — Towards Data Science (buscar en Medium/TDS)
- **Concepto clave para buscar**: "principal component analysis intuition" — para entender vectores propios sin matemáticas avanzadas

## 🚀 Próximos pasos sugeridos

- Explorar t-SNE y UMAP como alternativas no lineales a PCA para visualización de clusters
- Aprender a usar PCA dentro de un Pipeline de sklearn para evitar data leakage al aplicarlo en cross-validation
- Estudiar PCA incremental (`IncrementalPCA`) para datasets que no caben en memoria
- Practicar biplots interactivos con `plotly` para explorar datasets de alta dimensionalidad

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `sklearn.manifold.TSNE` | Visualización 2D de alta calidad preservando vecindades locales | Para explorar clusters en datos de texto, imágenes o genómica |
| `umap.UMAP` | Más rápido que t-SNE y escala mejor a datasets grandes | Cuando t-SNE tarda demasiado o necesitas embeddings para downstream tasks |
| `factor_analyzer` | Análisis factorial (variante de PCA con interpretación estadística) | Cuando necesitas comunalidades y cargas factoriales para investigación |
