# Clase 230 — Capstone 2: NLP o series de tiempo end-to-end

> Parte: **8 — Capstones** · Fuente: Hyndman & Athanasopoulos, [*Forecasting: Principles and Practice* (3ª ed.)](https://otexts.com/fpp3/) + Hugging Face [NLP course](https://huggingface.co/learn/nlp-course). ⏱️ Duración estimada: **180 min**.
>
> 🎚️ **Nivel:** Avanzado

## 🎯 Objetivo

Entregar un segundo capstone end-to-end eligiendo **una de dos ramas**: (A) **NLP** — clasificación de texto / NER / RAG con transformers y endpoint FastAPI, o (B) **series de tiempo** — forecasting con baselines + modelos modernos, backtesting honesto e intervalos de predicción. En ambas ramas: tracking con MLflow, contenedorización con Docker, reproducibilidad con `uv` lock + seeds, Model Card, y discusión de drift (texto o forecast).

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Elegir entre **NLP** o **series de tiempo** según interés/dominio y justificar la decisión en el README del proyecto.
- Construir un pipeline reproducible con **split honesto** (estratificado en NLP, temporal sin shuffle en series).
- Reportar métricas del dominio: **F1/accuracy + slice analysis** (NLP) o **sMAPE/MASE + pinball loss** (series).
- Servir el modelo en un endpoint **FastAPI** dockerizado, con MLflow tracking del entrenamiento.
- Detectar **drift** (Evidently text drift en NLP; KS sobre residuos en series) y documentarlo en la Model Card.

## 🗺️ Fases del capstone

| # | Fase | Entregable |
|---|---|---|
| 1 | Definición + dataset + Model Card v0 | `README.md` del proyecto con problema, métrica primaria y rama elegida. |
| 2 | EDA específico del dominio | NLP: distribución de longitudes, balance de clases, idioma. Series: STL, ACF/PACF, estacionariedad. |
| 3 | Split honesto + baselines | NLP: TF-IDF + Logistic / clase mayoritaria. Series: naive, seasonal naive, ETS, SARIMA. |
| 4 | Modelo moderno + MLflow tracking | NLP: fine-tune DistilBERT o sentence-transformers / RAG con FAISS. Series: NeuralProphet / Darts / Statsforecast (N-BEATS opcional). |
| 5 | Backtesting + intervalos | NLP: slice analysis (longitud, idioma, clase). Series: expanding window + cuantiles P10/P90. |
| 6 | Empaquetado + endpoint + drift | Docker + FastAPI (`/predict` o `/forecast`) + reporte de drift + Model Card final. |

## 📖 Definiciones y características

- **sMAPE** (symmetric MAPE): `mean(2·|y−ŷ| / (|y|+|ŷ|))`. Acotada en [0, 2], no estalla cuando `y=0` (a diferencia de MAPE).
- **MASE** (Mean Absolute Scaled Error): error escalado por el error del **naive estacional in-sample**. `MASE<1` ⇒ mejor que naive; comparable entre series de distinta escala.
- **Pinball loss** (quantile loss): `max(τ·(y−ŷ), (τ−1)·(y−ŷ))`. Loss correcta para **predicción de cuantiles** (intervalos P10/P90).
- **Backtesting expanding window**: `train[0:T₀] → predict[T₀:T₀+h]`, luego `train[0:T₀+h] → predict[...]`, etc. No re-mezcla; respeta el orden temporal.
- **Slice analysis (NLP)**: medir métricas por subconjunto (longitud del texto, idioma, clase) — un F1 global de 0.92 puede esconder F1=0.40 en textos largos.
- **Fine-tuning ligero**: entrenar solo la cabeza (head) de un transformer pre-entrenado o aplicar **LoRA** (adapters de bajo rango) → 10–100× menos parámetros entrenables.
- **RAG (Retrieval-Augmented Generation)**: embeddings → vector index (FAISS) → recuperar top-k → LLM responde con contexto. Reduce alucinaciones, no requiere fine-tuning.
- **Drift de forecast**: residuos `y−ŷ` cuya distribución cambia en el tiempo — señal de que el modelo necesita re-entrenamiento.

## 📂 Dataset / recursos

- **Rama A — NLP**: IMDB reviews (50K, binario), AG News (120K, 4 clases), o reseñas de Yelp en español. Para RAG: Wikipedia dump pequeño o docs internos.
- **Rama B — Series**: M5 (Walmart, jerárquica), electricity load (UCI), o clima diario (NOAA). Mínimo 2 años con estacionalidad clara.
- Stack común: `uv` (Parte 7), Docker, MLflow, FastAPI, Evidently. NLP extra: `transformers`, `datasets`, `sentence-transformers`, `faiss-cpu`. Series extra: `statsmodels`, `statsforecast`, `darts` o `neuralprophet`.

## 🧪 Ejercicios

1. **Definición**: escribir el problema en 5 líneas (qué se predice, para qué, métrica primaria, baseline aceptable, costo de errar). Elegir rama A o B.
2. **EDA del dominio**: rama A → distribuciones de longitud y balance de clases por idioma; rama B → STL + ACF/PACF + test de estacionariedad ADF.
3. **Baselines**: rama A → TF-IDF + LogisticRegression; rama B → naive + seasonal naive + ETS. Loggear todo a MLflow.
4. **Modelo moderno**: rama A → fine-tune DistilBERT 2 epochs con `transformers.Trainer`; rama B → SARIMA o NeuralProphet con backtesting expanding window 5 folds.
5. **Endpoint + drift**: FastAPI con `/predict` (NLP) o `/forecast?horizon=14` (series), dockerizado. Reporte de drift entre primera y segunda mitad del test (Evidently o KS test manual).

## 📝 Homework verificable

Repositorio con:

1. `README.md` del proyecto con problema, rama elegida (A o B), métrica primaria y resultado.
2. Notebook de EDA + entrenamiento con seeds fijas (42) y MLflow tracking visible (screenshot o `mlruns/` versionado).
3. `Dockerfile` + `compose.yml` que levanten FastAPI + MLflow UI con un solo `docker compose up`.
4. Endpoint funcional: `curl -X POST localhost:8000/predict` (NLP) o `curl localhost:8000/forecast?horizon=14` (series) devuelve JSON válido.
5. **Model Card** (1 página) con métricas globales y por slice/horizonte, datos de entrenamiento, sesgos conocidos, y plan de monitoreo de drift.

**Criterio de aceptación**: el modelo moderno supera al mejor baseline en la métrica primaria (NLP: ≥ +3 puntos de F1; series: MASE < 1.0 y sMAPE menor que seasonal naive), el endpoint responde en <500 ms, y la Model Card identifica al menos un slice/horizonte donde el modelo es débil.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| sMAPE = 200% en algunos puntos | `y=0` con `ŷ>0`. **Fix**: usar sMAPE simétrica `2·|y−ŷ|/(|y|+|ŷ|+ε)`, o cambiar a MASE. |
| Modelo de forecast "perfecto" en test | Hiciste `train_test_split` con `shuffle=True`. **Fix**: split temporal: `train = df[:T₀]`, `test = df[T₀:]`. Nunca shuffle en series. |
| `transformers` no carga pesos en Docker | Falta caché o no hay internet. **Fix**: descargar pesos en build (`RUN python -c "from transformers import ..."`) o montar volumen `~/.cache/huggingface`. |
| F1 global alto pero el cliente reclama | No hiciste slice analysis. **Fix**: reportar F1 por longitud/idioma/clase; un slice débil explica las quejas. |
| Intervalos P10/P90 cubren <50% del test | Modelo subestima la varianza. **Fix**: calibrar con conformal prediction o usar quantile regression con pinball loss directo. |
| `OOM` al fine-tunear DistilBERT en CPU | Batch size demasiado grande. **Fix**: `per_device_train_batch_size=8`, `gradient_accumulation_steps=4`, o usar adapters/LoRA. |

## ❓ Preguntas frecuentes

**❓ ¿NLP o series? ¿Cuál es más fácil?**

Series suele ser más rápido de prototipar (statsforecast entrena SARIMA sobre miles de series en minutos, sin GPU). NLP con transformers requiere GPU para fine-tuning serio, o aceptar fine-tuning lento en CPU con DistilBERT y `max_length=128`.

**❓ ¿Puedo usar GPT-4/Claude vía API en vez de fine-tunear?**

Sí — es válido como baseline en RAG o clasificación zero-shot, pero el capstone pide al menos **un modelo propio entrenado y versionado en MLflow**. La llamada a API puede ser el comparativo.

**❓ ¿Por qué MASE además de sMAPE?**

Porque MASE es **comparable entre series** (escala-invariante vs el naive estacional). Si reportás solo sMAPE, no podés saber si 12% es bueno o malo sin contexto. MASE < 1 ⇒ mejor que naive, en cualquier serie.

**❓ ¿FastAPI o BentoML?**

FastAPI por default (ya cubierto en Parte 4). BentoML si necesitás batch inference automática, model registry integrado, o despliegue a SageMaker/Vertex con menos código.

**❓ ¿La Model Card es realmente necesaria?**

Sí — Mitchell et al. (Google, 2019) la propusieron por una razón: sin ella, nadie sabe qué slices son débiles ni cuándo el modelo se rompe. Es lo primero que un evaluador externo (o auditor) pide.

## 🔗 Referencias

- Hyndman, R., Athanasopoulos, G. *Forecasting: Principles and Practice* (3ª ed., 2021) — https://otexts.com/fpp3/
- Hugging Face NLP course — https://huggingface.co/learn/nlp-course
- Hvitfeldt, E., Silge, J. *Supervised ML for Text Analysis* (2021) — https://smltar.com/ (R, conceptos aplican)
- Statsforecast docs — https://nixtlaverse.nixtla.io/statsforecast/index.html
- Darts (forecasting deep + clásico) — https://unit8co.github.io/darts/
- Mitchell, M. et al. *Model Cards for Model Reporting* (FAT* 2019).

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-230-capstone-2-nlp-o-series-de-tiempo-end-to-end-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-230-capstone-2-nlp-o-series-de-tiempo-end-to-end-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 231 — Capstone 3: visión por computadora con transfer learning](../231-capstone-3-vision-por-computadora-con-transfer-learning/README.md)
