# Parte 1 — Machine Learning Clásico

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-0-prerrequisitos/README.md) · [⏭️ Parte siguiente](../parte-2-deep-learning/README.md)

**50 clases** · ~11 semanas · ✅ Contenido completo

**Fuente principal:** **Géron** ([*Hands-On Machine Learning*, 3ª ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)) — estructura completa de los capítulos 1–9. Para boosting moderno (clase 088): docs oficiales de XGBoost / LightGBM / CatBoost.

Cada clase tiene su `README.md` con objetivo, resultados de aprendizaje verificables, dataset recomendado, 5 ejercicios y homework con criterio de aceptación. Todas las 50 clases incluyen las tres secciones del patrón pedagógico v2.2.0:

- **📖 Definiciones y características** — términos técnicos con explicación y características clave.
- **⚠️ Errores comunes** — tabla de síntomas/mensajes con causa y solución concretas.
- **❓ Preguntas frecuentes** — FAQs auténticas que aparecen al estudiar cada tema.

**📌 Cobertura moderna (audit 2026) — 7 clases dedicadas:**

Todos los temas modernos antes vivían como "complementos" dentro de clases originales; con la expansión 2026 cada uno es su clase propia con patrón completo + ejercicios + homework:

- Clase **053** → Validación temporal: TimeSeriesSplit, walk-forward, blocking.
- Clase **055** → Feature Engineering avanzado: target encoding (CV) + MICE imputation.
- Clase **058** → Optuna y HPO bayesiano dedicado (TPE, Hyperband, multi-objective).
- Clase **060** → Model Cards y Responsible ML (Mitchell 2018, EU AI Act, NIST AI RMF).
- Clase **064** → Class imbalance: SMOTE, ADASYN, class_weight, threshold tuning (PR-AUC, MCC).
- Clase **076** → Calibración de probabilidades (Platt, isotonic, temperature scaling, ECE, Brier).
- Clase **087** → SHAP en profundidad (TreeExplainer, KernelExplainer, DeepExplainer).

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

- **Fundamentos y proyecto end-to-end** — clases 050–061 — panorama del ML, desafíos, validación, proyecto completo, CRISP-DM.
- **Clasificación y métricas** — clases 062–068 — MNIST, confusion matrix, precision/recall, ROC, multiclase, análisis de errores.
- **Modelos lineales** — clases 069–076 — regresión lineal, gradient descent, polinomial, learning curves, regularización, logística.
- **SVM** — clases 077–079 — lineal, kernel, regresión.
- **Árboles** — clases 080–082 — entrenamiento, regularización, regresión.
- **Ensembles** — clases 083–090 — voting, bagging, Random Forest, feature importance, boosting (AdaBoost, GBM, XGBoost, LightGBM, CatBoost), stacking.
- **Reducción de dimensionalidad** — clases 091–094 — maldición de la dimensionalidad, PCA, LLE, MDS/Isomap/t-SNE/UMAP/LDA.
- **Clustering y detección de anomalías** — clases 095–099 — K-Means, DBSCAN, jerárquico, GMM, Isolation Forest, LOF.

## 📚 Índice de clases (50)

- [050 — Panorama del ML: tipos, batch vs online, instance vs model-based](050-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based/README.md)
- [051 — Desafíos del ML: overfitting, underfitting, datos insuficientes](051-desafios-del-ml-overfitting-underfitting-datos-insuficientes/README.md)
- [052 — Testing, validación, hyperparameter tuning, no free lunch theorem](052-testing-validacion-hyperparameter-tuning-no-free-lunch-theorem/README.md)
- [053 — Validación temporal: TimeSeriesSplit, walk-forward, blocking](053-validacion-temporal-timeseries-walk-forward/README.md)
- [054 — Proyecto end-to-end: visión, datos, exploración, preparación](054-proyecto-end-to-end-vision-datos-exploracion-preparacion/README.md)
- [055 — Feature Engineering avanzado: target encoding + MICE imputation](055-feature-engineering-avanzado-target-encoding-mice/README.md)
- [056 — Selección y entrenamiento de modelo](056-seleccion-y-entrenamiento-de-modelo/README.md)
- [057 — Fine-tuning: grid search y randomized search](057-fine-tuning-grid-search-randomized-search/README.md)
- [058 — Optuna y HPO bayesiano dedicado](058-optuna-bayesian-hpo-dedicado/README.md)
- [059 — Launch, monitoreo y mantenimiento de modelos](059-launch-monitoreo-y-mantenimiento/README.md)
- [060 — Model Cards y Responsible ML](060-model-cards-y-responsible-ml/README.md)
- [061 — CRISP-DM como framework metodológico](061-crisp-dm-como-framework-metodologico/README.md)
- [062 — Clasificación binaria con MNIST](062-clasificacion-binaria-con-mnist/README.md)
- [063 — Métricas: confusion matrix, precision, recall, F1](063-metricas-confusion-matrix-precision-recall-f1/README.md)
- [064 — Class imbalance: SMOTE, ADASYN, class_weight, threshold tuning](064-class-imbalance-smote-adasyn-class-weight/README.md)
- [065 — Precision/Recall tradeoff](065-precision-recall-tradeoff/README.md)
- [066 — Curva ROC y AUC](066-curva-roc-y-auc/README.md)
- [067 — Clasificación multiclase, multilabel, multioutput](067-clasificacion-multiclase-multilabel-multioutput/README.md)
- [068 — Análisis de errores](068-analisis-de-errores/README.md)
- [069 — Regresión lineal: ecuación normal vs gradient descent](069-regresion-lineal-ecuacion-normal-vs-gradient-descent/README.md)
- [070 — Gradient Descent: batch, stochastic, mini-batch](070-gradient-descent-batch-stochastic-mini-batch/README.md)
- [071 — Regresión polinomial](071-regresion-polinomial/README.md)
- [072 — Curvas de aprendizaje y bias-variance tradeoff](072-curvas-de-aprendizaje-bias-variance/README.md)
- [073 — Regularización: Ridge, Lasso, Elastic Net](073-regularizacion-ridge-lasso-elastic-net/README.md)
- [074 — Early stopping](074-early-stopping/README.md)
- [075 — Regresión logística binaria y softmax](075-regresion-logistica-binaria-y-softmax/README.md)
- [076 — Calibración de probabilidades: Platt, isotonic, temperature scaling](076-calibracion-de-probabilidades-platt-isotonic/README.md)
- [077 — SVM lineal](077-svm-lineal/README.md)
- [078 — SVM no lineal: kernel polinomial y RBF](078-svm-no-lineal-kernel-polinomial-rbf/README.md)
- [079 — SVM para regresión (SVR)](079-svm-para-regresion/README.md)
- [080 — Árboles de decisión: entrenamiento, visualización, CART](080-arboles-de-decision-entrenamiento-visualizacion-cart/README.md)
- [081 — Regularización de árboles](081-regularizacion-de-arboles/README.md)
- [082 — Regresión con árboles](082-regresion-con-arboles/README.md)
- [083 — Voting classifiers: hard y soft](083-voting-classifiers-hard-soft/README.md)
- [084 — Bagging y pasting](084-bagging-y-pasting/README.md)
- [085 — Random Forests y Extra Trees](085-random-forests-y-extra-trees/README.md)
- [086 — Feature importance](086-feature-importance/README.md)
- [087 — SHAP en profundidad: TreeExplainer, KernelExplainer, DeepExplainer](087-shap-en-profundidad-treeexplainer-deepexplainer/README.md)
- [088 — Boosting: AdaBoost y Gradient Boosting](088-boosting-adaboost-gradient-boosting/README.md)
- [089 — XGBoost, LightGBM y CatBoost](089-xgboost-lightgbm-catboost/README.md)
- [090 — Stacking (stacked generalization)](090-stacking/README.md)
- [091 — La maldición de la dimensionalidad](091-maldicion-de-la-dimensionalidad/README.md)
- [092 — PCA: proyección, varianza explicada, incremental, randomized, kernel](092-pca-proyeccion-varianza-explicada-incremental-randomized-kernel/README.md)
- [093 — LLE (Locally Linear Embedding)](093-lle/README.md)
- [094 — MDS, Isomap, t-SNE, UMAP, LDA](094-mds-isomap-t-sne-umap-lda/README.md)
- [095 — Clustering K-Means: selección de K, MiniBatch](095-clustering-k-means-seleccion-de-k-mini-batch/README.md)
- [096 — DBSCAN](096-dbscan/README.md)
- [097 — Agglomerative, BIRCH, Mean Shift, Affinity Propagation, Spectral](097-clustering-agglomerative-birch-mean-shift-affinity-propagation-spectra/README.md)
- [098 — Gaussian Mixture Models](098-gaussian-mixture-models/README.md)
- [099 — Detección de anomalías: Isolation Forest, LOF, One-Class SVM](099-deteccion-de-anomalias-isolation-forest-lof-one-class-svm/README.md)

## 📥 Material descargable — parte completa

Materiales consolidados con TODAS las clases de esta parte (útiles para revisar offline o imprimir el bloque entero):

- 📄 [Guía PDF — parte completa](../../docs/pdfs/parts/parte-1-machine-learning-clasico-completa.pdf) — todas las clases concatenadas con headings demoteados.
- 🎞️ [Presentación PPTX — parte completa](../../docs/presentaciones/parts/parte-1-machine-learning-clasico-completa.pptx) — portada + TOC + slides de cada clase.

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-0-prerrequisitos/README.md) · [⏭️ Parte siguiente](../parte-2-deep-learning/README.md)
