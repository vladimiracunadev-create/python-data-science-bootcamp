# Syllabus — Bootcamp Python para Data Science (v2)

> **197 clases · 9 partes · curriculum avanzado y completo**
>
> Fuente: pauta derivada de *Hands-On Machine Learning* (Géron, 3ª ed.) + *Python Data Science Handbook* (VanderPlas) + *Designing ML Systems* (Huyen) + *ISLP* (James et al) + *Fairness and Machine Learning* (Barocas/Hardt/Narayanan).
>
> Índice navegable completo: [classes/README.md](../classes/README.md)

---

## Propósito

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

## Perfil de entrada

Sin requisitos formales. Una persona con cero programación entra por la Parte 0. Una persona con experiencia previa puede saltarse partes específicas validándose contra el `README.md` de cada clase.

## Perfil de salida

Capaz de:

1. tomar un dataset desconocido, hacer EDA, decidir un modelo, entrenarlo, evaluarlo y desplegarlo;
2. defender decisiones de modelado con vocabulario estadístico riguroso;
3. operar el ciclo de vida completo MLOps (versionado, CI/CD, monitoreo);
4. construir un portafolio público que cualquier reclutador técnico pueda inspeccionar;
5. trabajar dentro de equipos de datos sin retraining adicional.

---

## Estructura general

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

## Estado de implementación

| Componente | Estado |
|---|---|
| Estructura de carpetas (197) | ✅ creada |
| README por clase | ✅ stub generado |
| `notebook.ipynb` por clase | ✅ stub generado |
| Contenido pedagógico real | ⏳ pendiente (197 clases por desarrollar) |
| PDFs y PPTX por clase | ⏳ pendiente (regenerar tras desarrollar) |
| Quizzes pre/post lección | ⏳ pendiente |
| Datasets temáticos por bloque | ⏳ pendiente |

El currículo anterior (v1, 31 clases) se conserva en [`historicos/classes-v1/`](../historicos/classes-v1) como referencia y fuente de material reutilizable.

## Cómo desarrollar una clase

Cada carpeta de clase tiene la misma estructura mínima:

```
classes/parte-N-slug/NNN-tema-slug/
├── README.md       # ficha: objetivo, resultados, temas, prerrequisitos
└── notebook.ipynb  # cuaderno de la clase
```

Materiales opcionales que se pueden añadir conforme una clase madure (replicando el estándar de v1):

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

## Orden recomendado de desarrollo

1. **Parte 0** completa (46 clases) — sin prerrequisitos nadie llega al resto.
2. **Parte 1** (43 clases) — ML clásico es la base del 70% del trabajo real.
3. **Parte 3** intercalada con Parte 1 — la estadística inferencial soporta la evaluación de modelos.
4. **Parte 2** (56 clases) — Deep Learning solo con bases sólidas de Parte 1.
5. **Parte 4** (MLOps) — después de tener al menos un modelo serio entrenado.
6. **Partes 5, 6, 7** en paralelo según prioridad.
7. **Parte 8** (capstones) — al cierre del programa.

## Metodología por clase

- Pregunta motivadora (1 min)
- Concepto y metáfora (5–10 min)
- Demo guiada con código documentado (15–20 min)
- Práctica acompañada en notebook (20–30 min)
- Ejercicio individual (15–20 min)
- Quiz de cierre + pregunta integradora (5 min)

## Herramientas del programa

Python 3.12+, JupyterLab, NumPy, pandas, matplotlib, seaborn, scikit-learn, XGBoost/LightGBM/CatBoost, scipy, statsmodels, SQL (sqlite/DuckDB/PostgreSQL), MongoDB, Polars, PySpark, TensorFlow/Keras, PyTorch, Hugging Face Transformers, FastAPI, Docker, MLflow, DVC, GitHub Actions, Airflow/Prefect, SHAP, Great Expectations.
