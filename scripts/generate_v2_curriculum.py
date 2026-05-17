"""Genera la estructura de carpetas del currículo v2 (197 contenidos).

Cada contenido es una carpeta con README.md y notebook.ipynb stub.
Layout: classes/parte-N-slug/NNN-tema-slug/
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "classes"

CURRICULUM: list[tuple[str, list[str]]] = [
    ("0-prerrequisitos", [
        "Instalación de Python 3.12+ y entornos virtuales (venv, uv, conda)",
        "Jupyter y JupyterLab: kernels, magics, debugging, profiling",
        "Git y GitHub para data scientists",
        "Estructura reproducible de proyecto (cookiecutter-data-science)",
        "VS Code / Cursor para Python y Jupyter",
        "Python: tipos, estructuras, control de flujo",
        "Comprehensions y generadores",
        "Funciones, args, kwargs, lambdas, closures",
        "Manejo de excepciones y context managers",
        "OOP básico, dataclasses, herencia",
        "pathlib, lectura y escritura de archivos",
        "Logging",
        "Type hints y mypy",
        "NumPy: tipos, creación, atributos",
        "NumPy: ufuncs y vectorización",
        "NumPy: agregaciones",
        "NumPy: broadcasting",
        "NumPy: boolean masks y fancy indexing",
        "NumPy: ordenamiento y búsqueda",
        "NumPy: álgebra lineal con numpy.linalg",
        "NumPy: aleatoriedad y semillas",
        "Pandas: Series y DataFrame",
        "Pandas: indexación (loc, iloc, at, iat)",
        "Pandas: operaciones y alineación",
        "Pandas: datos faltantes",
        "Pandas: MultiIndex",
        "Pandas: concat, merge, join",
        "Pandas: groupby (split-apply-combine)",
        "Pandas: pivot tables y crosstab",
        "Pandas: operaciones vectorizadas sobre strings",
        "Pandas: series de tiempo, resampling, rolling",
        "Pandas: eval y query",
        "Matplotlib: anatomía figura/axes",
        "Matplotlib: line, scatter, bar, histogram, boxplot",
        "Matplotlib: subplots y gridspec",
        "Matplotlib: legends, colorbars, ticks, anotaciones",
        "Matplotlib: stylesheets",
        "Matplotlib: 3D plotting",
        "Seaborn: distribuciones, relaciones, categóricas, facetas",
        "Visualización geográfica (Plotly / folium)",
        "SQL fundamental: SELECT, WHERE, JOIN, GROUP BY, HAVING",
        "SQL avanzado: CTEs, window functions, subqueries correlacionadas",
        "SQL desde Python: sqlite3, SQLAlchemy, DuckDB",
        "NoSQL: MongoDB con pymongo",
        "APIs REST con requests",
        "Web scraping con BeautifulSoup",
    ]),
    ("1-machine-learning-clasico", [
        "Panorama del ML: tipos, batch vs online, instance vs model-based",
        "Desafíos del ML: overfitting, underfitting, datos insuficientes",
        "Testing, validación, hyperparameter tuning, no free lunch theorem",
        "Proyecto end-to-end: visión, datos, exploración, preparación",
        "Selección y entrenamiento de modelo",
        "Fine-tuning (Grid Search, Randomized Search)",
        "Launch, monitoreo y mantenimiento",
        "CRISP-DM como framework metodológico",
        "Clasificación binaria con MNIST",
        "Métricas: confusion matrix, precision, recall, F1",
        "Precision/recall tradeoff",
        "Curva ROC y AUC",
        "Clasificación multiclase, multilabel, multioutput",
        "Análisis de errores",
        "Regresión lineal: ecuación normal vs Gradient Descent",
        "Gradient Descent: batch, stochastic, mini-batch",
        "Regresión polinomial",
        "Curvas de aprendizaje (bias/variance)",
        "Regularización: Ridge, Lasso, Elastic Net",
        "Early stopping",
        "Regresión logística (binaria y softmax)",
        "SVM lineal",
        "SVM no lineal (kernel polinomial, RBF)",
        "SVM para regresión",
        "Árboles de decisión: entrenamiento, visualización, CART",
        "Regularización de árboles",
        "Regresión con árboles",
        "Voting classifiers (hard/soft)",
        "Bagging y Pasting",
        "Random Forests y Extra-Trees",
        "Feature importance",
        "Boosting: AdaBoost, Gradient Boosting",
        "XGBoost, LightGBM, CatBoost",
        "Stacking",
        "Maldición de la dimensionalidad",
        "PCA: proyección, varianza explicada, incremental, randomized, kernel",
        "LLE",
        "MDS, Isomap, t-SNE, UMAP, LDA",
        "Clustering K-Means (selección de k, mini-batch)",
        "DBSCAN",
        "Clustering: agglomerative, BIRCH, mean-shift, affinity propagation, spectral",
        "Gaussian Mixture Models",
        "Detección de anomalías: Isolation Forest, LOF, One-Class SVM",
    ]),
    ("2-deep-learning", [
        "Perceptrón, MLP y backpropagation",
        "Regresión y clasificación con MLP",
        "Keras Sequential API",
        "Keras Functional API y Subclassing",
        "Callbacks, TensorBoard, guardar/restaurar modelos",
        "Keras Tuner",
        "Vanishing/exploding gradients",
        "Inicialización (Glorot, He)",
        "Activaciones: ReLU, ELU, GELU, Swish, Mish",
        "Batch Normalization, Layer Normalization",
        "Gradient clipping",
        "Transfer learning, unsupervised pretraining",
        "Optimizadores: Momentum, Nesterov, AdaGrad, RMSProp, Adam, AdamW",
        "Learning rate scheduling",
        "Regularización: L1/L2, dropout, max-norm, MC dropout",
        "TensorFlow: tensores, variables, operaciones",
        "Losses, métricas, capas, modelos custom",
        "Funciones y grafos (autograph)",
        "Custom training loops",
        "tf.data API",
        "TFRecord",
        "Keras preprocessing layers",
        "TensorFlow Datasets (TFDS)",
        "Capas convolucionales, filtros, feature maps",
        "Pooling",
        "Arquitecturas CNN: LeNet, AlexNet, VGG, GoogLeNet, ResNet, Xception, SENet, EfficientNet",
        "Transfer learning con CNNs preentrenadas",
        "Localización, detección (YOLO, Faster R-CNN), segmentación semántica",
        "RNNs: neuronas recurrentes, BPTT",
        "Forecasting de series con RNN",
        "LSTM, GRU",
        "1D CNNs y WaveNet",
        "Generación de texto char-RNN",
        "Análisis de sentimiento",
        "Encoder-Decoder para traducción",
        "Mecanismos de atención",
        "Transformers: arquitectura, BERT, GPT",
        "Hugging Face Transformers (uso práctico)",
        "LLMs aplicados: fine-tuning, prompting",
        "RAG básico y embeddings",
        "Autoencoders: undercomplete, stacked, denoising, sparse",
        "Variational Autoencoders (VAE)",
        "GANs: DCGAN, Progressive GAN, StyleGAN",
        "Modelos de difusión (DDPM, score-based)",
        "RL: aprendizaje por recompensa, OpenAI Gymnasium",
        "Policy gradients",
        "Markov Decision Processes",
        "TD Learning, Q-Learning, Deep Q-Networks",
        "RL moderno: A3C, PPO, SAC (vista general)",
        "TF Serving + gRPC",
        "Despliegue en Vertex AI",
        "TF Lite (mobile/embedded)",
        "TensorFlow.js (navegador)",
        "Aceleración con GPU",
        "Entrenamiento multi-dispositivo, tf.distribute",
        "Entrenamiento a escala con Vertex AI",
    ]),
    ("3-estadistica-inferencial", [
        "Distribuciones: normal, binomial, Poisson, exponencial",
        "Test t (una muestra, dos muestras, pareado)",
        "Test chi-cuadrado de independencia y bondad de ajuste",
        "ANOVA (one-way, two-way)",
        "Tests no paramétricos: Mann-Whitney, Wilcoxon, Kruskal-Wallis",
        "Corrección de comparaciones múltiples (Bonferroni, FDR)",
        "Intervalos de confianza",
        "Bootstrap y permutation tests",
        "A/B testing: tamaño de muestra, poder estadístico",
        "Diseño experimental",
        "Inferencia causal: DAGs, confounders, instrumentos",
        "Uplift modeling, DiD (difference-in-differences)",
        "Bayes intro: priors, posterior, MCMC con PyMC",
    ]),
    ("4-mlops", [
        "Versionado de datos con DVC",
        "Versionado de modelos y experimentos con MLflow",
        "Feature stores (Feast)",
        "CI/CD para ML con GitHub Actions",
        "Docker para empaquetar modelos",
        "APIs con FastAPI sirviendo modelos",
        "Kubernetes para servir modelos a escala",
        "Serverless ML: AWS Lambda, GCP Cloud Functions",
        "Monitoreo: data drift, model drift, alertas",
        "Reentrenamiento programado",
        "Shadow deployment y canary releases",
        "Interpretabilidad: SHAP, LIME, PDP, ICE",
        "Testing de datos: Great Expectations, Deequ",
        "Testing de modelos: invariance, behavioral tests",
    ]),
    ("5-ingenieria-de-datos", [
        "Pipelines ETL/ELT con Airflow",
        "Pipelines con Prefect o Dagster",
        "PySpark para datasets grandes",
        "Polars como alternativa moderna",
        "Data warehouses: BigQuery, Snowflake, DuckDB",
        "Streaming intro: Kafka, Kinesis",
        "Formatos columnares: Parquet, Avro",
        "Modelado dimensional (star/snowflake schemas)",
    ]),
    ("6-sistemas-de-recomendacion", [
        "Filtrado colaborativo user-based e item-based",
        "Factorización de matrices: SVD, ALS",
        "Content-based filtering",
        "Recomendadores híbridos",
        "Métricas: MAP@k, NDCG, recall@k",
        "Cold-start problem",
        "Librerías: LightFM, Implicit, Surprise",
    ]),
    ("7-etica-fairness-privacidad", [
        "Tipos de sesgo algorítmico y orígenes",
        "Métricas de fairness: demographic parity, equalized odds, calibration",
        "Privacidad diferencial (intro)",
        "Federated learning (intro)",
        "GDPR y AI Act (EU)",
        "Reproducibilidad: seeds, lock files, versionado de datasets",
    ]),
    ("8-capstones", [
        "Capstone 1: problema tabular end-to-end (EDA, modelo, API, dashboard)",
        "Capstone 2: NLP o series de tiempo end-to-end",
        "Capstone 3: visión por computadora con transfer learning",
        "Portafolio público en GitHub Pages y presentación",
    ]),
]


def slugify(text: str) -> str:
    text = text.lower()
    replacements = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "ñ": "n",
        "ü": "u",
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    # Limitar largo del slug para que las rutas en Windows no exploten
    if len(text) > 70:
        text = text[:70].rstrip("-")
    return text


def make_notebook(titulo: str) -> dict:
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [f"# {titulo}\n", "\n", "> Notebook stub generado automáticamente. Reemplazar con contenido real."],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Objetivo\n", "\n", "Describir aquí el objetivo concreto de la clase."],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Setup"],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# Imports y configuración inicial\n"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Desarrollo\n", "\n", "Bloques de código documentados (qué hace / para qué sirve)."],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": ["# TODO: implementar\n"],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Ejercicio guiado\n", "\n", "Consigna de práctica para el alumno."],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": ["## Conclusiones\n", "\n", "Lo que el alumno debe poder explicar al cerrar."],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.12"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def make_readme(numero: int, parte: str, titulo: str) -> str:
    return f"""# Clase {numero:03d} — {titulo}

> Parte: **{parte}**
> Estado: **stub** (pendiente desarrollar contenido).

## Objetivo

Describir el resultado de aprendizaje concreto de esta clase.

## Resultados esperados

Al finalizar, el estudiante podrá:

- (resultado 1)
- (resultado 2)
- (resultado 3)

## Temas clave

- (subtema 1)
- (subtema 2)
- (subtema 3)

## Materiales

- `README.md` — esta ficha
- `notebook.ipynb` — cuaderno de la clase

## Prerrequisitos

Ver índice general en `classes/README.md` para dependencias entre clases.
"""


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)

    contador_global = 0
    indice_lineas: list[str] = ["# Índice del currículo v2\n", "\n",
                                 "Total: 197 clases en 9 partes.\n", "\n"]

    for parte_slug, temas in CURRICULUM:
        parte_dir = ROOT / f"parte-{parte_slug}"
        parte_dir.mkdir(parents=True, exist_ok=True)
        indice_lineas.append(f"\n## Parte {parte_slug}\n\n")

        for tema in temas:
            contador_global += 1
            tema_slug = slugify(tema)
            carpeta = parte_dir / f"{contador_global:03d}-{tema_slug}"
            carpeta.mkdir(parents=True, exist_ok=True)

            (carpeta / "README.md").write_text(
                make_readme(contador_global, parte_slug, tema),
                encoding="utf-8",
            )
            (carpeta / "notebook.ipynb").write_text(
                json.dumps(make_notebook(tema), ensure_ascii=False, indent=1),
                encoding="utf-8",
            )

            ruta_rel = carpeta.relative_to(ROOT).as_posix()
            indice_lineas.append(f"- [{contador_global:03d} — {tema}]({ruta_rel}/README.md)\n")

    (ROOT / "README.md").write_text("".join(indice_lineas), encoding="utf-8")
    print(f"Generadas {contador_global} clases en {ROOT}")


if __name__ == "__main__":
    main()
