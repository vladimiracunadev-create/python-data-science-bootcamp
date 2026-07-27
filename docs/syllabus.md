<div align="center">

# 📚 Syllabus — Python Data Science Program

### **232 clases · 9 partes · curriculum avanzado y completo**

[![Clases](https://img.shields.io/badge/clases-232-7c5cff?style=for-the-badge)](../classes/README.md)
[![Partes](https://img.shields.io/badge/partes-9-0ea5e9?style=for-the-badge)](#-mapa-curricular-por-partes)
[![Fuentes](https://img.shields.io/badge/fuentes-5%20libros-f59e0b?style=for-the-badge)](#-fuentes-y-pauta)

</div>

> 📖 Pauta derivada de cinco libros referentes — ver [§ Fuentes y pauta](#-fuentes-y-pauta) para qué aporta cada uno.
>
> 🧭 Índice navegable completo: [classes/README.md](../classes/README.md)

---

## 📚 Fuentes y pauta

> Cuando decimos que el currículo está *derivado* de estas fuentes, queremos decir que cada parte del temario se construyó tomando explícitamente la secuencia, los énfasis y las decisiones pedagógicas de uno o más de estos libros. No se copia contenido — se respetan sus criterios técnicos y se adaptan a notebooks, datasets y ejercicios propios.

| 📘 Libro / autor | Aporte concreto al currículo |
|---|---|
| **🧠 Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow** — Aurélien Géron (3ª ed., O'Reilly 2022) | Espina dorsal del programa. Define la secuencia de **Parte 1 (ML clásico)** y **Parte 2 (Deep Learning)**: regresión → clasificación → ensembles → reducción dimensional → clustering → MLP → CNN → RNN → transformers → RL → despliegue. Es la referencia más práctica del mercado. |
| **📊 Python Data Science Handbook** — Jake VanderPlas (O'Reilly, 2ª ed.) | Cubre la **Parte 0 (Prerrequisitos)**: NumPy, pandas, matplotlib, ML clásico introductorio. Su tratamiento de pandas y visualización es el estándar tácito de la comunidad Python para análisis de datos. |
| **🏭 Designing Machine Learning Systems** — Chip Huyen (O'Reilly 2022) | Define la **Parte 4 (MLOps)** y la mentalidad de "ML como sistema de producción": ciclo de vida real, monitoreo, deriva de datos, fairness, observabilidad. Cierra la brecha entre notebook y servicio en vivo. |
| **📈 An Introduction to Statistical Learning, Python edition (ISLP)** — James, Witten, Hastie, Tibshirani (Springer 2023) | Refuerza la **Parte 3 (Estadística inferencial)** y aporta rigor matemático a la **Parte 1**. Es el manual estándar para entender por qué los modelos funcionan, no sólo cómo entrenarlos. |
| **⚖️ Fairness and Machine Learning** — Solon Barocas, Moritz Hardt, Arvind Narayanan (MIT Press 2023) | Funda la **Parte 7 (Ética, fairness, privacidad)**. Plantea el problema de sesgo algorítmico no como anexo moral sino como decisión técnica con métricas, definiciones formales y trade-offs documentables. |

> 🎯 La cobertura de las **Partes 5 (Ingeniería de datos)** y **6 (Recomendadores)** se apoya en buenas prácticas comunitarias y documentación oficial de cada herramienta (Spark, Airflow, Surprise, scikit-learn). La **Parte 8 (Capstones)** integra todo lo anterior y suma fuentes específicas: Huyen (DML Systems), Hyndman & Athanasopoulos (Forecasting Principles & Practice 3ª ed.), timm/Lightning/Albumentations, MkDocs Material/Quarto.

---

## 🎯 Propósito

Llevar a una persona desde cero programación hasta nivel **data scientist / ML engineer empleable** en 2026, con cobertura honesta de:

- Python aplicado a datos (no Python académico)
- Manipulación, SQL, NoSQL, ingesta y escala
- Estadística descriptiva e inferencial, A/B testing, inferencia causal
- Machine Learning clásico completo (sklearn + ensembles modernos)
- Deep Learning end-to-end (Keras + PyTorch + transformers + RAG + difusión)
- MLOps real (Docker, CI/CD, MLflow, monitoreo, fairness)
- Ingeniería de datos mínima (Spark, Airflow, lakehouses)
- Sistemas de recomendación
- Ética, privacidad y reproducibilidad
- Tres capstones públicos en GitHub

## 🚪 Perfil de entrada

Sin requisitos formales. Una persona con cero programación entra por la Parte 0. Una persona con experiencia previa puede saltarse partes específicas validándose contra el `README.md` de cada clase.

## 🎓 Perfil de salida

Capaz de:

1. tomar un dataset desconocido, hacer EDA, decidir un modelo, entrenarlo, evaluarlo y desplegarlo;
2. defender decisiones de modelado con vocabulario estadístico riguroso;
3. operar el ciclo de vida completo MLOps (versionado, CI/CD, monitoreo);
4. construir un portafolio público que cualquier reclutador técnico pueda inspeccionar;
5. trabajar dentro de equipos de datos sin retraining adicional.

---

## 🗂️ Estructura general

| Parte | Tema | Clases | Carpeta |
|---|---|---|---|
| 0 | Prerrequisitos: Python + NumPy + pandas + Polars + Parquet/Arrow/DuckDB + viz + SQL + NoSQL + APIs + async | 49 | [`parte-0-prerrequisitos/`](../classes/parte-0-prerrequisitos) |
| 1 | Machine Learning clásico | 50 | [`parte-1-machine-learning-clasico/`](../classes/parte-1-machine-learning-clasico) |
| 2 | Deep Learning (Keras, PyTorch+Lightning, CNN, transformers, LLMs, multimodal, MCP/agentes, RL, despliegue) | 75 | [`parte-2-deep-learning/`](../classes/parte-2-deep-learning) |
| 3 | Estadística inferencial y causal | 19 | [`parte-3-estadistica-inferencial/`](../classes/parte-3-estadistica-inferencial) |
| 4 | MLOps en producción | 14 | [`parte-4-mlops/`](../classes/parte-4-mlops) |
| 5 | Ingeniería de datos | 8 | [`parte-5-ingenieria-de-datos/`](../classes/parte-5-ingenieria-de-datos) |
| 6 | Sistemas de recomendación | 7 | [`parte-6-sistemas-de-recomendacion/`](../classes/parte-6-sistemas-de-recomendacion) |
| 7 | Ética, fairness, privacidad | 6 | [`parte-7-etica-fairness-privacidad/`](../classes/parte-7-etica-fairness-privacidad) |
| 8 | Capstones | 4 | [`parte-8-capstones/`](../classes/parte-8-capstones) |
| | **Total** | **232** | |

## 📊 Estado de implementación

| Componente | Estado |
|---|---|
| Estructura de carpetas (232) | ✅ creada |
| README por clase | 🎓 **232/232 completos y modernizados** (v3.9.0 · 100%) |
| `notebook.ipynb` por clase | 🎓 **232/232 ejecutables · cobertura 100% real** (v3.9.0) — todas las clases corren en el laboratorio con kernel Jupyter real |
| Contenido pedagógico real | 🎓 **232 READMEs · 232 notebooks ejecutables · 100% real** (v3.9.0) |
| Definiciones + Errores comunes + FAQ por clase | 🎓 **232/232** (v3.9.0 · 100%) |
| Clases dedicadas modernas 2024-2026 | 🟢 **35 clases dedicadas** en Partes 0-3 + stack moderno completo en Partes 4-7 (DVC/MLflow/Feast/K8s/FastAPI/Evidently/NannyML/Prefect/Istio/SHAP/Great Expectations/CheckList; Airflow/Prefect/Dagster/PySpark/Polars/DuckDB/BQ/Snowflake/Kafka/Parquet/Avro/star schema; CF/SVD+ALS/sentence-transformers/FAISS/LightFM/bandits; Suresh-Guttag taxonomía sesgos/DP+EO+calibration+impossibility theorem/privacidad diferencial Laplace+Gauss+DP-SGD/FedAvg+gradient leakage/GDPR+AI Act EU 2024/1689/seeds+lock files+model cards+datasheets) |
| PDFs y PPTX por clase | ✅ **232 PDFs + 232 PPTX por clase + 9 bundles por parte + `curso-completo.pdf`/`.pptx`** (v3.9.0) |
| Quizzes pre/post lección | ⏳ pendiente |
| Datasets temáticos por bloque | ⏳ pendiente |

## 🛠️ Cómo desarrollar una clase

Cada carpeta de clase tiene la misma estructura mínima:

```
classes/parte-N-slug/NNN-tema-slug/
├── README.md       # ficha: objetivo, resultados, temas, prerrequisitos
└── notebook.ipynb  # cuaderno de la clase
```

Materiales opcionales que se pueden añadir conforme una clase madure:

```
├── teoria.md
├── slides.md
├── ejercicios.md
├── homework.md
├── soluciones.ipynb
├── quiz.json
├── tecnologias.md
└── guia-codigo.md
```

## 🛣️ Orden recomendado de desarrollo

1. ~~**Parte 0** completa (49 clases · 001-049) — sin prerrequisitos nadie llega al resto.~~ ✅ completada (v3.0.0, ampliada con Polars, Parquet/Arrow/DuckDB, async/httpx).
2. ~~**Parte 1** (50 clases · 050-099) — ML clásico es la base del 70% del trabajo real.~~ ✅ completada (v3.0.0, con 7 clases dedicadas: Optuna, SHAP, calibración, Model Cards, class imbalance, validación temporal, FE+MICE).
3. ~~**Parte 3** (19 clases · 175-193) — estadística inferencial y causal.~~ ✅ completada (v3.0.0, con 6 clases dedicadas: effect size, BCa, CUPED+sequential, DoubleML, Synthetic Controls, PyMC v5/NumPyro/ArviZ).
4. ~~**Parte 2** (75 clases · 100-174) — Deep Learning con expansión LLM/multimodal completa.~~ ✅ completada (v3.0.0, con 19 clases dedicadas modernas 2024-2026: PyTorch+Lightning, SAM/YOLOv11, Flash Attention, CLIP/Whisper, LoRA/QLoRA/DPO/vLLM, MCP/agentes/eval, SDXL+ControlNet, ONNX, JAX).
5. ~~**Parte 4** (MLOps, 14 clases · 194-207) — después de tener al menos un modelo serio entrenado.~~ ✅ completada (v3.1.0, fuente Huyen — DVC, MLflow, Feast, K8s, FastAPI, drift, shadow/canary, SHAP en producción, Great Expectations, behavioral tests).
6. ~~**Parte 5** (Ingeniería de datos, 8 clases · 208-215).~~ ✅ completada (v3.2.0, fuentes Reis & Housley + Kimball — Airflow, Prefect/Dagster, PySpark, Polars, DuckDB/BQ/Snowflake, Kafka, Parquet/Avro, star schemas).
7. ~~**Parte 6** (Sistemas de recomendación, 7 clases · 216-222).~~ ✅ completada (v3.3.0, fuente Aggarwal + papers fundacionales — CF kNN, SVD/ALS, content+FAISS, LightFM, métricas top-N, cold-start, librerías).
8. ~~**Parte 7** (Ética, fairness, privacidad, 6 clases · 223-228).~~ ✅ completada (v3.4.0, fuentes Barocas/Hardt/Narayanan + Suresh-Guttag 2021 + Hardt-Price-Srebro 2016 + Chouldechova 2017 + Kleinberg 2017 + Dwork-Roth 2014 + Abadi 2016 + McMahan 2017 + Reglamentos UE 2016/679 y 2024/1689 + Pineau 2021 + Mitchell 2019 + Gebru 2018 — Suresh-Guttag taxonomía sesgos, DP/EO/calibration + impossibility theorem, privacidad diferencial (Laplace/Gauss/DP-SGD), federated learning (FedAvg + gradient leakage), GDPR + AI Act EU 2024/1689, reproducibilidad (seeds/lock files/model cards/datasheets)).
9. ~~**Parte 8** (capstones, 4 proyectos · 229-232).~~ ✅ completada (v3.5.0, fuentes Huyen + Hyndman & Athanasopoulos FPP3 + timm/Lightning/Albumentations + MkDocs Material/Quarto + integradores de todas las partes previas — Capstone 1 tabular E2E (ColumnTransformer+GBM+Optuna+MLflow+FastAPI+Streamlit+SHAP+CI), Capstone 2 NLP/series (DistilBERT o forecasting con baselines+SARIMA+backtesting+cuantiles), Capstone 3 visión transfer learning (ConvNeXt/EfficientNetV2/ViT + RandAugment/MixUp/CutMix + ONNX), Portafolio público (MkDocs Material/Quarto + GitHub Pages + demos hosted + deck + CV técnico)).

🎓 **Currículo completo · 232 READMEs · 197 notebooks ejecutables (35 dedicadas modernas con README pero notebook pendiente).** Próximo foco: superficies (regen PDFs/PPTX por clase, migración de contenido a la app Android, mejoras del laboratorio de ejecución Python).

## 🧠 Metodología por clase

- Pregunta motivadora (1 min)
- Concepto y metáfora (5–10 min)
- Demo guiada con código documentado (15–20 min)
- Práctica acompañada en notebook (20–30 min)
- Ejercicio individual (15–20 min)
- Quiz de cierre + pregunta integradora (5 min)

## 🧰 Herramientas del programa

Python 3.12+, JupyterLab, NumPy, pandas, matplotlib, seaborn, scikit-learn, XGBoost/LightGBM/CatBoost, scipy, statsmodels, SQL (sqlite/DuckDB/PostgreSQL), MongoDB, Polars, PySpark, TensorFlow/Keras, PyTorch, Hugging Face Transformers, FastAPI, Docker, MLflow, DVC, GitHub Actions, Airflow/Prefect, SHAP, Great Expectations.
