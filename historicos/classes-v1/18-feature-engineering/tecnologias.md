# 🔧 Tecnologías complementarias — Clase 18: Feature Engineering — crear mejores variables

> Herramientas, librerías y recursos para ampliar lo aprendido.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel sugerido |
|---|---|---|
| `pandas` | Creación de features derivadas, encoding con `get_dummies`/`map`, binning con `cut`/`qcut` | Básico |
| `scikit-learn` (preprocessing) | `StandardScaler`, `MinMaxScaler`, `OneHotEncoder`, `LabelEncoder` en forma de objetos | Básico |
| `scikit-learn` (feature_selection) | `SelectKBest`, `RFE`, `VarianceThreshold` para seleccionar las features más útiles | Intermedio |
| `category_encoders` | Encodings avanzados: Target Encoding, Binary Encoding, Helmert para alta cardinalidad | Intermedio |
| `scipy.stats` | Transformaciones de distribución (Box-Cox, Yeo-Johnson) para acercar datos a la normalidad | Intermedio |
| `imbalanced-learn` | SMOTE y técnicas para manejar clases desbalanceadas al crear features sintéticas | Intermedio |
| `featuretools` | Generación automática de features relacionales entre múltiples tablas | Avanzado |
| `tsfresh` | Extracción automática de cientos de features estadísticas de series de tiempo | Avanzado |
| `sklearn.impute` | `SimpleImputer`, `KNNImputer` para rellenar valores faltantes antes del modelado | Básico |

## 🌐 Recursos recomendados

- **Documentación oficial**: scikit-learn preprocessing — [scikit-learn.org/stable/modules/preprocessing.html](https://scikit-learn.org/stable/modules/preprocessing.html) — guía completa de todas las transformaciones disponibles con ejemplos de código
- **Tutorial recomendado**: Kaggle Learn — curso gratuito "Feature Engineering" con notebooks descargables y ejercicios sobre datasets reales de competencias
- **Concepto clave para buscar**: "data leakage machine learning" / "data leakage feature engineering" — uno de los errores más peligrosos y comunes al preprocesar datos, y el más difícil de detectar

## 🚀 Próximos pasos sugeridos

- Aprender `Pipeline` y `ColumnTransformer` de scikit-learn para encadenar transformaciones de forma reproducible, ordenada y sin data leakage entre entrenamiento y prueba
- Estudiar Target Encoding de la librería `category_encoders` para variables categóricas con alta cardinalidad (muchas categorías únicas)
- Explorar la extracción de features desde texto: TF-IDF y embeddings con `sklearn.feature_extraction.text`
- Investigar cómo tratar datos desbalanceados con SMOTE (Synthetic Minority Over-sampling Technique) de `imbalanced-learn`

## 🧰 Herramientas alternativas

| Herramienta | Descripción breve | Cuándo conviene usarla |
|---|---|---|
| AutoML (H2O, AutoSklearn) | Automatiza feature engineering y selección de modelos | Exploración rápida o cuando el tiempo es limitado y se necesita una línea base |
| Featuretools | Genera features automáticamente entre tablas relacionadas usando "deep feature synthesis" | Datasets con múltiples tablas con relaciones (similar a una base de datos relacional) |
| dbt (data build tool) | Feature engineering en SQL para data warehouses | En entornos de producción donde los datos viven en BigQuery, Snowflake o Redshift |
| RAPIDS cuDF | Feature engineering en GPU para grandes volúmenes de datos con API similar a pandas | Cuando el dataset tiene millones de filas y hay GPU disponible para acelerar el procesamiento |
