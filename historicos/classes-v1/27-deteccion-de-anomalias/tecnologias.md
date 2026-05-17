# 🔧 Tecnologías complementarias — Clase 27: Detección de Anomalías

> Herramientas, librerías y recursos para ampliar lo visto en clase.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel |
|---|---|---|
| `scikit-learn` (IsolationForest) | Detección de anomalías basada en árboles de aislamiento | Básico |
| `scikit-learn` (LocalOutlierFactor) | Detección basada en densidad local de vecinos | Básico |
| `PyOD` | Librería especializada con 40+ algoritmos de detección de outliers | Intermedio |
| `statsmodels` | Métodos estadísticos: pruebas de hipótesis, Grubbs test, etc. | Intermedio |
| `scipy.stats` | Z-score, distribuciones estadísticas, pruebas de normalidad | Básico |
| `ADTK` | Detección de anomalías específicamente en series temporales | Intermedio |
| `alibi-detect` | Framework de detección de anomalías y drift para ML en producción | Avanzado |
| `River` | Machine learning online para detectar anomalías en tiempo real en streams | Avanzado |

## 🌐 Recursos recomendados

- **Documentación de IsolationForest**: https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html — parámetros clave como `contamination` y `n_estimators`.
- **PyOD documentation**: https://pyod.readthedocs.io/en/latest/ — referencia del toolkit más completo para anomaly detection en Python.
- **Anomaly Detection Learning Resources**: https://github.com/yzhao062/anomaly-detection-resources — recopilación de papers, tutoriales y datasets.
- **Tutorial práctico de detección de fraude**: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud — dataset clásico de fraude bancario con notebooks de la comunidad.
- **Artículo: Comparison of Anomaly Detection Methods**: buscar en Papers With Code las comparaciones actualizadas de algoritmos.

## 🚀 Próximos pasos

- Explorar **PyOD** para acceder a algoritmos más especializados como COPOD, ECOD o HBOS con la misma interfaz de sklearn.
- Aprender detección de anomalías en **series temporales** con ADTK: patrones estacionales, cambios de tendencia, picos repentinos.
- Investigar **Autoencoders** para detección de anomalías en datos de alta dimensionalidad (imágenes, logs de sistemas).
- Practicar con el **dataset de fraude de tarjetas de crédito** de Kaggle: problema real con 99.8% de transacciones normales.
- Explorar cómo combinar múltiples detectores (**ensemble de anomalías**) para reducir falsos positivos.

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `PyOD` | Colección unificada de 40+ algoritmos de detección de outliers | Cuando quieres comparar muchos métodos rápidamente |
| `Azure Anomaly Detector` | API en la nube para detección de anomalías en series temporales | Aplicaciones en producción sin infraestructura propia |
| `Elastic (ELK Stack)` | Detección de anomalías en logs de sistemas en tiempo real | Monitoreo de infraestructura IT y ciberseguridad |
| `Prophet` (Meta) | Forecasting de series temporales con detección implícita de outliers | Datos con estacionalidad conocida (ventas, tráfico web) |
| `Grafana + alertas` | Visualización y alertas automáticas cuando métricas superan umbrales | Monitoreo operacional en tiempo real |
