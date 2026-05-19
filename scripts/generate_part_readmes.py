"""Genera README.md raíz para cada parte del currículo.

Cada README contiene:
- Narrativa rica (de qué trata, qué problemas resuelve, resultados de aprendizaje)
- Estructura temática de la parte
- Índice completo de clases con links
- Navegación de regreso al programa y entre partes
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLASSES = ROOT / "classes"

# Metadata por parte: título visible, fuente, narrativa.
PARTS = {
    "parte-0-prerrequisitos": {
        "num": 0,
        "titulo": "Prerrequisitos: Python + NumPy + pandas + visualización + SQL + APIs",
        "fuente": "**VanderPlas** ([*Python Data Science Handbook*](https://jakevdp.github.io/PythonDataScienceHandbook/)) — secuencia y énfasis en NumPy, pandas y matplotlib.",
        "duracion_estimada": "~10–12 semanas a ritmo moderado",
        "trata": (
            "Esta parte construye **toda la base técnica** que el resto del programa da por sentada. "
            "No es \"introducción a Python\" — es el conjunto mínimo de herramientas con las que un data "
            "scientist trabaja a diario: el lenguaje, los entornos reproducibles, el control de versiones, "
            "el stack numérico (NumPy / pandas), la visualización (matplotlib / seaborn / plotly), "
            "el acceso a datos (SQL, NoSQL, APIs, scraping) y la disciplina de proyecto (logging, "
            "type hints, manejo de errores, estructura cookiecutter).\n\n"
            "El recorrido es deliberadamente extenso porque cada laguna acá se convierte en deuda invisible "
            "que aparece después en Parte 1 (ML clásico) y Parte 2 (Deep Learning). Quien complete bien "
            "esta parte puede leer cualquier notebook profesional, reproducirlo, modificarlo y debuggearlo."
        ),
        "resuelve": [
            "Configurar un entorno Python aislado y reproducible (venv / uv / conda) sin colisiones de dependencias.",
            "Manipular datasets tabulares de tamaño medio (cientos de miles de filas) sin caer en bucles ni código lento.",
            "Limpiar, transformar y unir datos sucios usando pandas (faltantes, tipos, formatos, joins, groupby).",
            "Producir gráficos publicables (no solo `df.plot()`) con matplotlib + seaborn, incluyendo mapas geográficos.",
            "Consultar bases relacionales con SQL avanzado (CTEs, window functions) y conectarlas desde Python.",
            "Acceder a datos externos vía APIs REST y, cuando no hay API, mediante web scraping responsable.",
        ],
        "resultados": [
            "Levantar un proyecto nuevo con estructura reproducible, dependencias fijadas y `pre-commit` en menos de 10 minutos.",
            "Escribir código NumPy/pandas vectorizado (sin loops) y justificar por qué es más rápido.",
            "Diseñar visualizaciones efectivas que comuniquen una conclusión, no solo \"que se vean lindas\".",
            "Escribir consultas SQL no triviales (window functions, CTEs recursivas) y traducirlas a pandas y viceversa.",
            "Extraer datos de una API o sitio web y dejarlos listos para análisis, manejando paginación y rate-limiting.",
        ],
        "estructura": [
            ("Setup y reproducibilidad", "clases 001–005 — instalación, Jupyter, Git/GitHub, estructura de proyecto, editor."),
            ("Python para data science", "clases 006–013 — tipos, comprehensions, funciones, OOP, pathlib, logging, type hints."),
            ("NumPy (8 clases)", "clases 014–021 — creación, ufuncs, agregaciones, broadcasting, masks, álgebra lineal, aleatoriedad."),
            ("pandas (11 clases)", "clases 022–032 — Series/DataFrame, indexación, joins, groupby, pivot, strings, series de tiempo."),
            ("Visualización", "clases 033–040 — matplotlib en profundidad, seaborn, visualización geográfica."),
            ("SQL", "clases 041–043 — desde fundamentos a window functions y conexión desde Python."),
            ("Acceso a datos externos", "clases 044–046 — MongoDB, APIs REST, web scraping con BeautifulSoup."),
        ],
        "prev": None,
        "next": "parte-1-machine-learning-clasico",
    },
    "parte-1-machine-learning-clasico": {
        "num": 1,
        "titulo": "Machine Learning Clásico",
        "fuente": "**Géron** ([*Hands-On Machine Learning*, 3ª ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)) — estructura completa de los capítulos 1–9.",
        "duracion_estimada": "~10 semanas",
        "trata": (
            "El **70 % del trabajo real de un data scientist** ocurre acá: regresión, clasificación, árboles, "
            "ensembles, reducción de dimensionalidad y clustering — sobre datos tabulares, con scikit-learn. "
            "Es la parte que más empleabilidad da, porque la mayoría de los problemas de negocio se resuelven "
            "con un Random Forest o un XGBoost bien evaluado, **no** con una red neuronal.\n\n"
            "El recorrido sigue *Hands-On ML* de Géron: arranca con un proyecto end-to-end (CRISP-DM) que "
            "atraviesa todo el ciclo (exploración → preparación → modelo → evaluación → tuning → "
            "deployment), y luego desmenuza cada familia de modelos con la matemática suficiente para "
            "elegir bien hiperparámetros, no solo para usar `.fit()`. Incluye una unidad fuerte de "
            "**métricas** (confusion matrix, ROC, precision/recall tradeoff) porque elegir mal la métrica "
            "es la causa #1 de modelos que \"funcionan en validación y mueren en producción\"."
        ),
        "resuelve": [
            "Plantear un problema de ML desde cero: entender el negocio, definir métrica, dividir train/test sin leakage.",
            "Construir pipelines completos de preprocesamiento + modelo que se puedan serializar y reusar.",
            "Elegir entre regresión lineal, logística, SVM, árboles o ensembles con criterio (no por moda).",
            "Diagnosticar overfitting/underfitting con curvas de aprendizaje y aplicar la regularización correcta.",
            "Hacer hyperparameter tuning eficiente (Grid Search, Randomized Search) sin sobreajustar al test set.",
            "Reducir dimensionalidad para visualizar (t-SNE, UMAP) o para acelerar entrenamiento (PCA).",
            "Detectar anomalías en datasets sin etiquetas (Isolation Forest, LOF, One-Class SVM).",
        ],
        "resultados": [
            "Llevar un problema tabular nuevo desde dataset crudo hasta modelo evaluado en menos de un día de trabajo.",
            "Justificar por escrito por qué se eligió un modelo sobre otro (interpretabilidad, datos, métrica, latencia).",
            "Construir un ensemble (bagging, boosting o stacking) y explicar la mejora sobre el baseline.",
            "Aplicar correctamente PCA / t-SNE / UMAP para EDA y para preprocesamiento.",
            "Identificar y corregir las 5 causas más comunes de data leakage.",
        ],
        "estructura": [
            ("Fundamentos y proyecto end-to-end", "clases 047–054 — panorama del ML, desafíos, validación, proyecto completo, CRISP-DM."),
            ("Clasificación y métricas", "clases 055–060 — MNIST, confusion matrix, precision/recall, ROC, multiclase, análisis de errores."),
            ("Modelos lineales", "clases 061–067 — regresión lineal, gradient descent, polinomial, learning curves, regularización, logística."),
            ("SVM", "clases 068–070 — lineal, kernel, regresión."),
            ("Árboles", "clases 071–073 — entrenamiento, regularización, regresión."),
            ("Ensembles", "clases 074–080 — voting, bagging, Random Forest, feature importance, boosting (AdaBoost, GBM, XGBoost, LightGBM, CatBoost), stacking."),
            ("Reducción de dimensionalidad", "clases 081–084 — maldición de la dimensionalidad, PCA, LLE, MDS/Isomap/t-SNE/UMAP/LDA."),
            ("Clustering y detección de anomalías", "clases 085–089 — K-Means, DBSCAN, jerárquico, GMM, Isolation Forest, LOF."),
        ],
        "prev": "parte-0-prerrequisitos",
        "next": "parte-2-deep-learning",
    },
    "parte-2-deep-learning": {
        "num": 2,
        "titulo": "Deep Learning — Keras, TensorFlow, Transformers, RL y Despliegue",
        "fuente": "**Géron** ([*Hands-On ML*, 3ª ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)) — capítulos 10–19, con incorporación de LLMs modernos, RAG y modelos de difusión.",
        "duracion_estimada": "~13–14 semanas",
        "trata": (
            "La parte **más extensa** del programa. Cubre Deep Learning desde el perceptrón hasta los "
            "modelos generativos modernos (Transformers, LLMs, difusión) y reinforcement learning. "
            "El énfasis está en **entender qué hace cada bloque** (no solo en copiar `model.fit`): por qué "
            "BatchNorm acelera la convergencia, qué hace Adam que no hace SGD, cuándo conviene una CNN "
            "vs una ViT, por qué un Transformer dejó obsoletas a las RNN para secuencias largas.\n\n"
            "Está organizada en bloques: **fundamentos** (MLPs, optimización, regularización), "
            "**ingeniería con TensorFlow/Keras** (custom layers, tf.data, TFRecord), **visión por "
            "computadora** (CNNs y arquitecturas modernas), **secuencias** (RNN, LSTM, atención, "
            "Transformers, LLMs, RAG), **generativos** (autoencoders, VAE, GAN, difusión), "
            "**reinforcement learning** y **despliegue a producción** (TF Serving, Vertex AI, TF Lite, "
            "TensorFlow.js, multi-GPU)."
        ),
        "resuelve": [
            "Entrenar una red neuronal desde cero (MLP) y explicar la matemática del backpropagation.",
            "Diagnosticar y resolver vanishing/exploding gradients con inicialización, BatchNorm y activaciones modernas.",
            "Hacer transfer learning con CNNs preentrenadas para visión o con LLMs para texto.",
            "Construir un pipeline de datos eficiente con tf.data + TFRecord para entrenar sobre datasets que no caben en RAM.",
            "Implementar arquitecturas modernas: ResNet, EfficientNet, ViT, BERT, GPT, modelos de difusión.",
            "Usar Hugging Face Transformers para tareas reales (clasificación, NER, generación, embeddings).",
            "Construir un sistema RAG básico sobre documentos propios.",
            "Desplegar un modelo entrenado a producción (TF Serving + gRPC, Vertex AI, TF Lite móvil, navegador con TF.js).",
        ],
        "resultados": [
            "Entrenar y serializar un modelo de visión que supere baseline en un dataset propio.",
            "Hacer fine-tuning de un Transformer pequeño para clasificación o generación.",
            "Construir un mini-RAG con embeddings + retriever + LLM sobre un corpus de ~1000 documentos.",
            "Servir un modelo entrenado vía API en una GPU y medir su latencia.",
            "Explicar el tradeoff entrenamiento/serving para CNN vs ViT vs LLM para un caso concreto.",
        ],
        "estructura": [
            ("Fundamentos de redes neuronales", "clases 090–095 — perceptrón, MLP, backprop, Keras (Sequential, Functional, Subclassing), Keras Tuner."),
            ("Entrenamiento de redes profundas", "clases 096–104 — gradientes, inicialización, activaciones, normalización, optimizadores, schedules, regularización."),
            ("TensorFlow avanzado", "clases 105–112 — tensores, custom layers/loops, autograph, tf.data, TFRecord, preprocessing layers, TFDS."),
            ("Visión por computadora", "clases 113–117 — convoluciones, pooling, arquitecturas CNN modernas, transfer learning, detección/segmentación."),
            ("Secuencias y NLP", "clases 118–129 — RNN, LSTM, GRU, 1D CNN, char-RNN, sentimiento, encoder-decoder, atención, Transformers, BERT/GPT, Hugging Face, LLMs, RAG."),
            ("Modelos generativos", "clases 130–133 — autoencoders, VAE, GAN, difusión."),
            ("Reinforcement Learning", "clases 134–138 — Gymnasium, policy gradients, MDPs, Q-learning, DQN, PPO/SAC."),
            ("Despliegue y escala", "clases 139–145 — TF Serving, Vertex AI, TF Lite, TensorFlow.js, GPU, tf.distribute, entrenamiento a escala."),
        ],
        "prev": "parte-1-machine-learning-clasico",
        "next": "parte-3-estadistica-inferencial",
    },
    "parte-3-estadistica-inferencial": {
        "num": 3,
        "titulo": "Estadística Inferencial y Causal",
        "fuente": "**ISLP** ([*Statistical Learning with Python*](https://www.statlearning.com/)) — rigor matemático en tests, intervalos y diseño experimental.",
        "duracion_estimada": "~4 semanas (puede intercalarse con Parte 1)",
        "trata": (
            "La parte que separa al data scientist del \"sklearn user\". Cubre **inferencia estadística** "
            "(tests, intervalos, bootstrap), **diseño de experimentos** (A/B testing real, no solo "
            "`p < 0.05`) e **inferencia causal** (DAGs, confounders, instrumentos, DiD, uplift) — "
            "herramientas que se usan a diario para responder preguntas tipo \"¿esto que cambiamos en "
            "el producto realmente movió la métrica?\" o \"¿este coeficiente significa lo que creo que "
            "significa?\".\n\n"
            "Se intercala bien con la Parte 1 porque la mayoría de los problemas de evaluación de "
            "modelos (comparar dos clasificadores, decidir si una mejora es real) son problemas "
            "estadísticos disfrazados. Incluye una introducción a estadística bayesiana con PyMC para "
            "abrir la puerta a inferencia con incertidumbre explícita."
        ),
        "resuelve": [
            "Decidir si una diferencia observada es estadísticamente significativa o ruido.",
            "Diseñar un A/B test con tamaño de muestra y poder estadístico correctos, no a ojo.",
            "Aplicar el test correcto según los supuestos del dato (paramétrico vs no paramétrico, pareado vs independiente).",
            "Corregir comparaciones múltiples (Bonferroni, FDR) para no inflar el falso positivo.",
            "Estimar incertidumbre con bootstrap cuando los supuestos clásicos no aplican.",
            "Identificar confounders en un DAG y elegir la estrategia causal correcta (control, IV, DiD, uplift).",
            "Hacer una inferencia bayesiana básica con MCMC en PyMC.",
        ],
        "resultados": [
            "Diseñar y analizar un A/B test end-to-end, incluyendo poder estadístico y corrección por múltiples métricas.",
            "Aplicar bootstrap para construir intervalos de confianza no paramétricos sobre cualquier estimador.",
            "Dibujar el DAG de un problema de negocio y justificar qué variables controlar.",
            "Implementar un modelo bayesiano simple en PyMC e interpretar el posterior.",
        ],
        "estructura": [
            ("Tests clásicos", "clases 146–151 — distribuciones, t-test, chi-cuadrado, ANOVA, no paramétricos, comparaciones múltiples."),
            ("Estimación e incertidumbre", "clases 152–153 — intervalos de confianza, bootstrap, permutation tests."),
            ("Experimentación y causalidad", "clases 154–157 — A/B testing, diseño experimental, inferencia causal con DAGs, uplift / DiD."),
            ("Inferencia bayesiana", "clase 158 — priors, posterior, MCMC con PyMC."),
        ],
        "prev": "parte-2-deep-learning",
        "next": "parte-4-mlops",
    },
    "parte-4-mlops": {
        "num": 4,
        "titulo": "MLOps — Modelos en Producción",
        "fuente": "**Huyen** ([*Designing Machine Learning Systems*](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/)) — el manual de cabecera para MLOps moderno.",
        "duracion_estimada": "~4–5 semanas",
        "trata": (
            "La parte que convierte un notebook que entrena bien en un **sistema que funciona en "
            "producción 24/7**. Cubre versionado (de datos, modelos y experimentos), packaging "
            "(Docker), serving (FastAPI, Kubernetes, serverless), monitoreo (data drift, model drift) "
            "y los rituales que evitan que el modelo se degrade silenciosamente (reentrenamiento "
            "programado, shadow deployment, canary releases).\n\n"
            "Incluye una unidad fuerte de **interpretabilidad** (SHAP, LIME, PDP, ICE) porque ningún "
            "modelo va a producción sin alguien preguntando \"¿por qué dijo eso?\", y otra de **testing** "
            "(datos con Great Expectations, modelos con tests de invariancia) porque en ML el bug "
            "habitual no es un crash sino un drift silencioso."
        ),
        "resuelve": [
            "Versionar datasets pesados con DVC y modelos/experimentos con MLflow.",
            "Empaquetar un modelo entrenado en un contenedor Docker reproducible.",
            "Servir el modelo como API (FastAPI) y escalar con Kubernetes o serverless.",
            "Detectar data drift y model drift antes de que el negocio reclame.",
            "Hacer despliegues seguros (shadow, canary) para evitar romper producción.",
            "Explicar predicciones individuales y globales con SHAP / LIME / PDP / ICE.",
            "Validar entradas con Great Expectations antes de que lleguen al modelo.",
        ],
        "resultados": [
            "Tomar un modelo entrenado y publicarlo como API monitoreada en producción en menos de un día.",
            "Diseñar un pipeline CI/CD que reentrene y redesplíegue automáticamente cuando llega data nueva.",
            "Configurar alertas de drift que avisen *antes* de que la métrica de negocio caiga.",
            "Generar un reporte de interpretabilidad para stakeholders no técnicos.",
        ],
        "estructura": [
            ("Versionado", "clases 159–161 — DVC para datos, MLflow para modelos/experimentos, Feast como feature store."),
            ("CI/CD y packaging", "clases 162–164 — GitHub Actions para ML, Docker, FastAPI."),
            ("Escala y serving", "clases 165–166 — Kubernetes, serverless (AWS Lambda / GCP Functions)."),
            ("Monitoreo y operación", "clases 167–169 — data/model drift, reentrenamiento programado, shadow/canary."),
            ("Interpretabilidad y testing", "clases 170–172 — SHAP/LIME/PDP/ICE, testing de datos, testing de modelos."),
        ],
        "prev": "parte-3-estadistica-inferencial",
        "next": "parte-5-ingenieria-de-datos",
    },
    "parte-5-ingenieria-de-datos": {
        "num": 5,
        "titulo": "Ingeniería de Datos",
        "fuente": "Complementaria — fundamentos prácticos de data engineering necesarios para alimentar pipelines de ML a escala.",
        "duracion_estimada": "~3 semanas",
        "trata": (
            "La parte que enseña a **mover y transformar datos a escala**, más allá de lo que pandas "
            "aguanta. Cubre orquestación (Airflow, Prefect, Dagster), procesamiento distribuido "
            "(PySpark, Polars), almacenamiento analítico (BigQuery, Snowflake, DuckDB), streaming "
            "(Kafka, Kinesis), formatos columnares (Parquet, Avro) y modelado dimensional "
            "(star/snowflake schemas).\n\n"
            "Es la parte donde el data scientist deja de pedirle datos al equipo de data engineering "
            "y empieza a moverlos él mismo cuando es necesario. No reemplaza a un data engineer "
            "senior, pero sí cubre el 80 % de los casos donde el bottleneck era \"esto no cabe en "
            "memoria\" o \"este pipeline corre 8 horas y falla a la mitad\"."
        ),
        "resuelve": [
            "Orquestar un pipeline de N pasos con dependencias, retries y observabilidad.",
            "Procesar datasets de TBs con PySpark o de GBs con Polars sin cargarlos en RAM.",
            "Consultar un data warehouse moderno (BigQuery, Snowflake, DuckDB local) desde Python.",
            "Consumir un stream de eventos en tiempo real (Kafka / Kinesis).",
            "Elegir el formato de almacenamiento correcto (Parquet vs Avro vs CSV) según el patrón de lectura.",
            "Diseñar un modelo dimensional (star schema) para BI y para features de ML.",
        ],
        "resultados": [
            "Convertir un script `pandas` que tomaba horas en un pipeline Airflow/Prefect con Polars o PySpark.",
            "Migrar un workflow desde CSV a Parquet y medir la mejora en tiempo y espacio.",
            "Diseñar un star schema para un caso de negocio dado.",
        ],
        "estructura": [
            ("Orquestación", "clases 173–174 — Airflow, Prefect, Dagster."),
            ("Procesamiento distribuido y moderno", "clases 175–176 — PySpark, Polars."),
            ("Data warehouses y streaming", "clases 177–178 — BigQuery / Snowflake / DuckDB, Kafka / Kinesis."),
            ("Formatos y modelado", "clases 179–180 — Parquet/Avro, modelado dimensional."),
        ],
        "prev": "parte-4-mlops",
        "next": "parte-6-sistemas-de-recomendacion",
    },
    "parte-6-sistemas-de-recomendacion": {
        "num": 6,
        "titulo": "Sistemas de Recomendación",
        "fuente": "Complementaria — combinación de filtrado colaborativo clásico y enfoques modernos basados en embeddings.",
        "duracion_estimada": "~2–3 semanas",
        "trata": (
            "Una unidad especializada en una de las aplicaciones de ML con más impacto comercial "
            "directo: **recomendar el siguiente producto, video, canción o contenido**. Cubre los dos "
            "enfoques clásicos (filtrado colaborativo y content-based), su unión en sistemas "
            "**híbridos**, y la matemática detrás (factorización de matrices: SVD, ALS).\n\n"
            "También cubre las **métricas correctas** (MAP@k, NDCG, recall@k — no accuracy) y el "
            "problema del **cold-start** (usuarios o items nuevos sin historial), que es donde mueren "
            "la mayoría de los recomendadores en su primer mes en producción. Termina con un tour "
            "por las librerías que se usan en la práctica (LightFM, Implicit, Surprise)."
        ),
        "resuelve": [
            "Construir un recomendador user-based o item-based desde una matriz usuario-item dispersa.",
            "Aplicar factorización de matrices (SVD / ALS) para llegar a recomendaciones escalables.",
            "Combinar señales colaborativas y de contenido en un recomendador híbrido.",
            "Evaluar un recomendador con la métrica correcta (no con accuracy ni RMSE de rating).",
            "Mitigar el cold-start con estrategias basadas en contenido o popularidad.",
        ],
        "resultados": [
            "Entrenar y evaluar un recomendador end-to-end con LightFM o Implicit sobre un dataset real (MovieLens o similar).",
            "Reportar la calidad del recomendador con MAP@k y NDCG, no con accuracy.",
            "Diseñar una estrategia explícita para usuarios y items nuevos.",
        ],
        "estructura": [
            ("Filtrado colaborativo", "clases 181–182 — user-based, item-based, factorización de matrices (SVD, ALS)."),
            ("Content-based e híbridos", "clases 183–184 — content-based, recomendadores híbridos."),
            ("Evaluación y cold-start", "clases 185–186 — métricas MAP@k / NDCG / recall@k, cold-start problem."),
            ("Tooling", "clase 187 — LightFM, Implicit, Surprise."),
        ],
        "prev": "parte-5-ingenieria-de-datos",
        "next": "parte-7-etica-fairness-privacidad",
    },
    "parte-7-etica-fairness-privacidad": {
        "num": 7,
        "titulo": "Ética, Fairness y Privacidad",
        "fuente": "**Barocas / Hardt / Narayanan** ([*Fairness and Machine Learning*](https://fairmlbook.org/)) — el texto de referencia académico para fairness algorítmica.",
        "duracion_estimada": "~2 semanas",
        "trata": (
            "La parte que ningún currículo serio puede omitir en 2026: cómo construir sistemas de ML "
            "que **no discriminen, no filtren datos personales y sean reproducibles**. Cubre los "
            "tipos y orígenes del sesgo algorítmico, las **métricas formales de fairness** "
            "(demographic parity, equalized odds, calibration — y por qué son matemáticamente "
            "incompatibles entre sí), técnicas modernas como **privacidad diferencial** y "
            "**federated learning**, y el marco regulatorio actual (GDPR, AI Act europeo).\n\n"
            "Cierra con una clase sobre **reproducibilidad** (seeds, lock files, versionado de "
            "datasets) que es prerrequisito de cualquier discusión seria sobre fairness: si no se "
            "puede reproducir, no se puede auditar."
        ),
        "resuelve": [
            "Identificar los tipos y fuentes de sesgo en un dataset y en un modelo entrenado.",
            "Medir fairness con las métricas correctas y explicar por qué no se pueden cumplir todas a la vez.",
            "Aplicar privacidad diferencial básica para publicar estadísticas sin filtrar individuos.",
            "Entender cuándo federated learning es la solución correcta (y cuándo es overkill).",
            "Cumplir requisitos básicos de GDPR y AI Act en un proyecto de ML.",
            "Hacer un experimento reproducible bit-a-bit.",
        ],
        "resultados": [
            "Auditar un modelo clasificador por demographic parity y equalized odds, y reportar trade-offs.",
            "Documentar un dataset y un modelo con un datasheet / model card.",
            "Producir un experimento que cualquiera puede reproducir desde el repo en menos de 30 minutos.",
        ],
        "estructura": [
            ("Sesgo y fairness", "clases 188–189 — tipos de sesgo, métricas de fairness."),
            ("Privacidad", "clases 190–191 — privacidad diferencial, federated learning."),
            ("Regulación y reproducibilidad", "clases 192–193 — GDPR / AI Act, reproducibilidad práctica."),
        ],
        "prev": "parte-6-sistemas-de-recomendacion",
        "next": "parte-8-capstones",
    },
    "parte-8-capstones": {
        "num": 8,
        "titulo": "Capstones — Proyectos Integradores",
        "fuente": "Síntesis — el estudiante demuestra dominio integrando todo lo aprendido en tres proyectos completos y un portafolio público.",
        "duracion_estimada": "proyectos largos · ~4–6 semanas",
        "trata": (
            "La parte final del programa, donde no se aprende contenido nuevo: se **integra todo** "
            "en tres proyectos end-to-end y un portafolio público en GitHub Pages. Cada capstone "
            "cubre un dominio distinto (tabular, NLP/series, visión) para forzar al estudiante a "
            "demostrar versatilidad, y todos los proyectos deben llegar hasta el **deployment** "
            "(API, dashboard, app) — no se aceptan notebooks aislados.\n\n"
            "El capstone final (la \"clase 197\") no es código sino **comunicación**: armar un "
            "portafolio público navegable, una presentación de 10 minutos por proyecto y un README "
            "técnico que un reclutador o colega pueda entender. Es el entregable que se usa para "
            "buscar trabajo o para evaluar el programa entero."
        ),
        "resuelve": [
            "Demostrar que se puede llevar un problema desde dataset crudo hasta sistema en producción sin asistencia.",
            "Integrar las tres partes técnicas duras del programa: ML clásico (P1), DL (P2) y MLOps (P4).",
            "Comunicar resultados técnicos a audiencias no técnicas.",
            "Construir un portafolio público creíble para postular a trabajos de data scientist / ML engineer.",
        ],
        "resultados": [
            "Tres proyectos completos publicados en GitHub con README, demo desplegada y documentación reproducible.",
            "Un portafolio público en GitHub Pages que sirva como CV técnico.",
            "Tres presentaciones de 10 minutos (una por capstone) listas para entrevistas.",
        ],
        "estructura": [
            ("Capstone 1 — Tabular", "clase 194 — problema tabular end-to-end (EDA, modelo, API, dashboard)."),
            ("Capstone 2 — NLP o series", "clase 195 — NLP o time-series end-to-end."),
            ("Capstone 3 — Visión", "clase 196 — visión por computadora con transfer learning."),
            ("Portafolio público", "clase 197 — GitHub Pages, presentación, README técnico."),
        ],
        "prev": "parte-7-etica-fairness-privacidad",
        "next": None,
    },
}


def class_human_title(class_dir: Path) -> str:
    """Lee el título de la clase desde su README.md (primera línea con `#`)."""
    readme = class_dir / "README.md"
    if readme.exists():
        with readme.open(encoding="utf-8") as f:
            for line in f:
                m = re.match(r"^#\s+Clase\s+(\d+)\s*[—–-]\s*(.+?)\s*$", line)
                if m:
                    return f"{m.group(1)} — {m.group(2)}"
    # Fallback: slug → texto
    name = class_dir.name
    num, _, rest = name.partition("-")
    return f"{num} — {rest.replace('-', ' ').capitalize()}"


def build_index(part_dir: Path) -> str:
    classes = sorted(d for d in part_dir.iterdir() if d.is_dir() and re.match(r"^\d{3}-", d.name))
    lines = []
    for c in classes:
        title = class_human_title(c)
        lines.append(f"- [{title}]({c.name}/README.md)")
    return "\n".join(lines)


def part_readme(slug: str, meta: dict) -> str:
    part_dir = CLASSES / slug
    n_classes = sum(1 for d in part_dir.iterdir() if d.is_dir() and re.match(r"^\d{3}-", d.name))

    nav_links = ["[⬅️ Volver al programa](../../README.md)", "[📚 Índice completo](../README.md)"]
    if meta["prev"]:
        nav_links.append(f"[⏮️ Parte anterior](../{meta['prev']}/README.md)")
    if meta["next"]:
        nav_links.append(f"[⏭️ Parte siguiente](../{meta['next']}/README.md)")
    nav = " · ".join(nav_links)

    resuelve_md = "\n".join(f"- {x}" for x in meta["resuelve"])
    resultados_md = "\n".join(f"- {x}" for x in meta["resultados"])
    estructura_md = "\n".join(f"- **{titulo}** — {detalle}" for titulo, detalle in meta["estructura"])
    indice_md = build_index(part_dir)

    return f"""# Parte {meta["num"]} — {meta["titulo"]}

> {nav}

**{n_classes} clases** · {meta["duracion_estimada"]}

**Fuente principal:** {meta["fuente"]}

---

## 🎯 ¿De qué trata esta parte?

{meta["trata"]}

## 🧩 Problemas que resuelve

{resuelve_md}

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

{resultados_md}

## 🗺️ Estructura temática

{estructura_md}

## 📚 Índice de clases ({n_classes})

{indice_md}

---

> {nav}
"""


def main() -> None:
    for slug, meta in PARTS.items():
        part_dir = CLASSES / slug
        if not part_dir.exists():
            print(f"SKIP missing: {slug}")
            continue
        readme = part_dir / "README.md"
        readme.write_text(part_readme(slug, meta), encoding="utf-8")
        print(f"wrote {readme.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
