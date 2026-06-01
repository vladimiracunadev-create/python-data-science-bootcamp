<div align="center">

# 📚 Syllabus — Python Data Science Program

### **197 clases · 9 partes · curriculum avanzado y completo**

[![Clases](https://img.shields.io/badge/clases-197-7c5cff?style=for-the-badge)](../classes/README.md)
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

> 🎯 La cobertura de las **Partes 5 (Ingeniería de datos)**, **6 (Recomendadores)** y **8 (Capstones)** se apoya en buenas prácticas comunitarias y documentación oficial de cada herramienta (Spark, Airflow, Surprise, scikit-learn).

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
| 0 | Prerrequisitos: Python + NumPy + pandas + viz + SQL + APIs | 46 | [`parte-0-prerrequisitos/`](../classes/parte-0-prerrequisitos) |
| 1 | Machine Learning clásico | 43 | [`parte-1-machine-learning-clasico/`](../classes/parte-1-machine-learning-clasico) |
| 2 | Deep Learning (Keras, TensorFlow, transformers, RL, despliegue) | 56 | [`parte-2-deep-learning/`](../classes/parte-2-deep-learning) |
| 3 | Estadística inferencial y causal | 13 | [`parte-3-estadistica-inferencial/`](../classes/parte-3-estadistica-inferencial) |
| 4 | MLOps en producción | 14 | [`parte-4-mlops/`](../classes/parte-4-mlops) |
| 5 | Ingeniería de datos | 8 | [`parte-5-ingenieria-de-datos/`](../classes/parte-5-ingenieria-de-datos) |
| 6 | Sistemas de recomendación | 7 | [`parte-6-sistemas-de-recomendacion/`](../classes/parte-6-sistemas-de-recomendacion) |
| 7 | Ética, fairness, privacidad | 6 | [`parte-7-etica-fairness-privacidad/`](../classes/parte-7-etica-fairness-privacidad) |
| 8 | Capstones | 4 | [`parte-8-capstones/`](../classes/parte-8-capstones) |
| | **Total** | **197** | |

## 📊 Estado de implementación

| Componente | Estado |
|---|---|
| Estructura de carpetas (197) | ✅ creada |
| README por clase | ✅ Partes 0 y 1 (89) completos y ampliados · Partes 2-8 stubs |
| `notebook.ipynb` por clase | ✅ Parte 0 (46) ejecutables · ⏳ Partes 1-8 stubs (notebooks pendientes de desarrollo aunque los README estén completos en Parte 1) |
| Contenido pedagógico real | 🟢 Partes 0 y 1 completas (89 clases) · ⏳ 108 clases pendientes (Partes 2-8) |
| Definiciones + Errores comunes + FAQ por clase | 🟢 89/89 en Partes 0-1 (v2.3.0) · ⏳ Partes 2-8 |
| Complementos modernos integrados | 🟢 13 complementos en Partes 0-1 (regex, pytest, Polars, Parquet, async/httpx, validación temporal, FE+MICE, Optuna, model cards, class imbalance, calibración, SHAP/LIME) |
| PDFs y PPTX por clase | ⏳ pendiente (regenerar tras desarrollar contenido) |
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

1. ~~**Parte 0** completa (46 clases) — sin prerrequisitos nadie llega al resto.~~ ✅ completada (v2.1.0, ampliada en v2.2.0, +5 complementos en v2.3.0).
2. ~~**Parte 1** (43 clases) — ML clásico es la base del 70% del trabajo real.~~ ✅ completada (v2.3.0, con 8 complementos modernos integrados).
3. **Parte 3** (13 clases) — siguiente prioridad. La estadística inferencial soporta la evaluación de modelos de Parte 1.
4. **Parte 2** (56 clases) — Deep Learning solo con bases sólidas de Parte 1.
5. **Parte 4** (MLOps) — después de tener al menos un modelo serio entrenado.
6. **Partes 5, 6, 7** en paralelo según prioridad.
7. **Parte 8** (capstones) — al cierre del programa.

## 🧠 Metodología por clase

- Pregunta motivadora (1 min)
- Concepto y metáfora (5–10 min)
- Demo guiada con código documentado (15–20 min)
- Práctica acompañada en notebook (20–30 min)
- Ejercicio individual (15–20 min)
- Quiz de cierre + pregunta integradora (5 min)

## 🧰 Herramientas del programa

Python 3.12+, JupyterLab, NumPy, pandas, matplotlib, seaborn, scikit-learn, XGBoost/LightGBM/CatBoost, scipy, statsmodels, SQL (sqlite/DuckDB/PostgreSQL), MongoDB, Polars, PySpark, TensorFlow/Keras, PyTorch, Hugging Face Transformers, FastAPI, Docker, MLflow, DVC, GitHub Actions, Airflow/Prefect, SHAP, Great Expectations.
