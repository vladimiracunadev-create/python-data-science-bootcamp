# Parte 1 — Machine Learning Clásico

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-0-prerrequisitos/README.md) · [⏭️ Parte siguiente](../parte-2-deep-learning/README.md)

**48 clases · ~11 semanas · ✅ Contenido completo**

**Fuente principal:** **Géron** ([*Hands-On Machine Learning*, 3ª ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)) — estructura completa de los capítulos 1–9. Para boosting moderno (clase 079): docs oficiales de XGBoost / LightGBM / CatBoost.

Cada clase tiene su `README.md` con objetivo, resultados de aprendizaje verificables, dataset recomendado, 5 ejercicios y homework con criterio de aceptación. Todas las 48 clases incluyen las tres secciones del patrón pedagógico v2.2.0:

- **📖 Definiciones y características** — términos técnicos con explicación y características clave.
- **⚠️ Errores comunes** — tabla de síntomas/mensajes con causa y solución concretas.
- **❓ Preguntas frecuentes** — FAQs auténticas que aparecen al estudiar cada tema.

**📌 Cobertura moderna (audit 2026) — 2 complementos integrados + 5 clases dedicadas:**

Complementos integrados dentro de la clase original:

- Clase 049 → validación temporal (`TimeSeriesSplit`, walk-forward).
- Clase 050 → feature engineering avanzado (target encoding con CV) e imputación avanzada (`KNNImputer`, `IterativeImputer`/MICE).

Clases dedicadas (expansión 2026 con patrón completo + ejercicios + homework propios):

- Clase **052a** → HPO moderno (Optuna, TPE, Hyperband, multi-objective, Ray Tune).
- Clase **053a** → Model Cards y Responsible ML (Mitchell 2018, EU AI Act, NIST AI RMF).
- Clase **056a** → class imbalance (SMOTE, ADASYN, class_weight, threshold tuning, MCC, PR-AUC).
- Clase **067a** → calibración de probabilidades (Platt, isotonic, temperature scaling, ECE, Brier).
- Clase **077a** → SHAP en profundidad (TreeExplainer, KernelExplainer, DeepExplainer, summary/waterfall/dependence).

---

## 🎯 ¿De qué trata esta parte?

El **70 % del trabajo real de un data scientist** ocurre acá: regresión, clasificación, árboles, ensembles, reducción de dimensionalidad y clustering — sobre datos tabulares, con scikit-learn. Es la parte que más empleabilidad da, porque la mayoría de los problemas de negocio se resuelven con un Random Forest o un XGBoost bien evaluado, **no** con una red neuronal.

El recorrido sigue *Hands-On ML* de Géron: arranca con un proyecto end-to-end (CRISP-DM) que atraviesa todo el ciclo (exploración → preparación → modelo → evaluación → tuning → deployment), y luego desmenuza cada familia de modelos con la matemática suficiente para elegir bien hiperparámetros, no solo para usar `.fit()`. Incluye una unidad fuerte de **métricas** (confusion matrix, ROC, precision/recall tradeoff) porque elegir mal la métrica es la causa #1 de modelos que "funcionan en validación y mueren en producción".

## 🧩 Problemas que resuelve

- Plantear un problema de ML desde cero: entender el negocio, definir métrica, dividir train/test sin leakage.
- Construir pipelines completos de preprocesamiento + modelo que se puedan serializar y reusar.
- Elegir entre regresión lineal, logística, SVM, árboles o ensembles con criterio (no por moda).
- Diagnosticar overfitting/underfitting con curvas de aprendizaje y aplicar la regularización correcta.
- Hacer hyperparameter tuning eficiente (Grid Search, Randomized Search) sin sobreajustar al test set.
- Reducir dimensionalidad para visualizar (t-SNE, UMAP) o para acelerar entrenamiento (PCA).
- Detectar anomalías en datasets sin etiquetas (Isolation Forest, LOF, One-Class SVM).

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Llevar un problema tabular nuevo desde dataset crudo hasta modelo evaluado en menos de un día de trabajo.
- Justificar por escrito por qué se eligió un modelo sobre otro (interpretabilidad, datos, métrica, latencia).
- Construir un ensemble (bagging, boosting o stacking) y explicar la mejora sobre el baseline.
- Aplicar correctamente PCA / t-SNE / UMAP para EDA y para preprocesamiento.
- Identificar y corregir las 5 causas más comunes de data leakage.

## 🗺️ Estructura temática

- **Fundamentos y proyecto end-to-end** — clases 047–054 — panorama del ML, desafíos, validación, proyecto completo, CRISP-DM.
- **Clasificación y métricas** — clases 055–060 — MNIST, confusion matrix, precision/recall, ROC, multiclase, análisis de errores.
- **Modelos lineales** — clases 061–067 — regresión lineal, gradient descent, polinomial, learning curves, regularización, logística.
- **SVM** — clases 068–070 — lineal, kernel, regresión.
- **Árboles** — clases 071–073 — entrenamiento, regularización, regresión.
- **Ensembles** — clases 074–080 — voting, bagging, Random Forest, feature importance, boosting (AdaBoost, GBM, XGBoost, LightGBM, CatBoost), stacking.
- **Reducción de dimensionalidad** — clases 081–084 — maldición de la dimensionalidad, PCA, LLE, MDS/Isomap/t-SNE/UMAP/LDA.
- **Clustering y detección de anomalías** — clases 085–089 — K-Means, DBSCAN, jerárquico, GMM, Isolation Forest, LOF.

## 📚 Índice de clases (43)

- [047 — Panorama del ML: tipos, batch vs online, instance vs model-based](047-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based/README.md)
- [048 — Desafíos del ML: overfitting, underfitting, datos insuficientes](048-desafios-del-ml-overfitting-underfitting-datos-insuficientes/README.md)
- [049 — Testing, validación, hyperparameter tuning, no free lunch theorem](049-testing-validacion-hyperparameter-tuning-no-free-lunch-theorem/README.md)
- [050 — Proyecto end-to-end: visión, datos, exploración, preparación](050-proyecto-end-to-end-vision-datos-exploracion-preparacion/README.md)
- [051 — Selección y entrenamiento de modelo](051-seleccion-y-entrenamiento-de-modelo/README.md)
- [052 — Fine-tuning (Grid Search, Randomized Search)](052-fine-tuning-grid-search-randomized-search/README.md)
- [052a — Optuna y HPO bayesiano dedicado](052a-optuna-bayesian-hpo-dedicado/README.md) 🆕
- [053 — Launch, monitoreo y mantenimiento](053-launch-monitoreo-y-mantenimiento/README.md)
- [053a — Model Cards y Responsible ML](053a-model-cards-y-responsible-ml/README.md) 🆕
- [054 — CRISP-DM como framework metodológico](054-crisp-dm-como-framework-metodologico/README.md)
- [055 — Clasificación binaria con MNIST](055-clasificacion-binaria-con-mnist/README.md)
- [056 — Métricas: confusion matrix, precision, recall, F1](056-metricas-confusion-matrix-precision-recall-f1/README.md)
- [056a — Class imbalance: SMOTE, ADASYN, class_weight, threshold tuning](056a-class-imbalance-smote-adasyn-class-weight/README.md) 🆕
- [057 — Precision/recall tradeoff](057-precision-recall-tradeoff/README.md)
- [058 — Curva ROC y AUC](058-curva-roc-y-auc/README.md)
- [059 — Clasificación multiclase, multilabel, multioutput](059-clasificacion-multiclase-multilabel-multioutput/README.md)
- [060 — Análisis de errores](060-analisis-de-errores/README.md)
- [061 — Regresión lineal: ecuación normal vs Gradient Descent](061-regresion-lineal-ecuacion-normal-vs-gradient-descent/README.md)
- [062 — Gradient Descent: batch, stochastic, mini-batch](062-gradient-descent-batch-stochastic-mini-batch/README.md)
- [063 — Regresión polinomial](063-regresion-polinomial/README.md)
- [064 — Curvas de aprendizaje (bias/variance)](064-curvas-de-aprendizaje-bias-variance/README.md)
- [065 — Regularización: Ridge, Lasso, Elastic Net](065-regularizacion-ridge-lasso-elastic-net/README.md)
- [066 — Early stopping](066-early-stopping/README.md)
- [067 — Regresión logística (binaria y softmax)](067-regresion-logistica-binaria-y-softmax/README.md)
- [067a — Calibración de probabilidades: Platt, isotonic, temperature scaling](067a-calibracion-de-probabilidades-platt-isotonic/README.md) 🆕
- [068 — SVM lineal](068-svm-lineal/README.md)
- [069 — SVM no lineal (kernel polinomial, RBF)](069-svm-no-lineal-kernel-polinomial-rbf/README.md)
- [070 — SVM para regresión](070-svm-para-regresion/README.md)
- [071 — Árboles de decisión: entrenamiento, visualización, CART](071-arboles-de-decision-entrenamiento-visualizacion-cart/README.md)
- [072 — Regularización de árboles](072-regularizacion-de-arboles/README.md)
- [073 — Regresión con árboles](073-regresion-con-arboles/README.md)
- [074 — Voting classifiers (hard/soft)](074-voting-classifiers-hard-soft/README.md)
- [075 — Bagging y Pasting](075-bagging-y-pasting/README.md)
- [076 — Random Forests y Extra-Trees](076-random-forests-y-extra-trees/README.md)
- [077 — Feature importance](077-feature-importance/README.md)
- [077a — SHAP en profundidad: TreeExplainer, KernelExplainer, DeepExplainer](077a-shap-en-profundidad-treeexplainer-deepexplainer/README.md) 🆕
- [078 — Boosting: AdaBoost, Gradient Boosting](078-boosting-adaboost-gradient-boosting/README.md)
- [079 — XGBoost, LightGBM, CatBoost](079-xgboost-lightgbm-catboost/README.md)
- [080 — Stacking](080-stacking/README.md)
- [081 — Maldición de la dimensionalidad](081-maldicion-de-la-dimensionalidad/README.md)
- [082 — PCA: proyección, varianza explicada, incremental, randomized, kernel](082-pca-proyeccion-varianza-explicada-incremental-randomized-kernel/README.md)
- [083 — LLE](083-lle/README.md)
- [084 — MDS, Isomap, t-SNE, UMAP, LDA](084-mds-isomap-t-sne-umap-lda/README.md)
- [085 — Clustering K-Means (selección de k, mini-batch)](085-clustering-k-means-seleccion-de-k-mini-batch/README.md)
- [086 — DBSCAN](086-dbscan/README.md)
- [087 — Clustering: agglomerative, BIRCH, mean-shift, affinity propagation, spectral](087-clustering-agglomerative-birch-mean-shift-affinity-propagation-spectra/README.md)
- [088 — Gaussian Mixture Models](088-gaussian-mixture-models/README.md)
- [089 — Detección de anomalías: Isolation Forest, LOF, One-Class SVM](089-deteccion-de-anomalias-isolation-forest-lof-one-class-svm/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-0-prerrequisitos/README.md) · [⏭️ Parte siguiente](../parte-2-deep-learning/README.md)
