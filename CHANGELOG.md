<div align="center">

# 📝 Changelog

### **Historial de cambios por versión**

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-f59e0b?style=for-the-badge)](https://keepachangelog.com/es/1.0.0/)
[![SemVer](https://img.shields.io/badge/SemVer-2.0.0-3fb950?style=for-the-badge)](https://semver.org/lang/es/)

</div>

> 📌 Todos los cambios notables de este proyecto se documentan aquí.

---

## [v3.8.1] — 2026-07-20 (Las 232 clases embebidas en la app Android)

### Corregido
- **La app Android se instalaba con el catálogo vacío.** `mobile/src/data/classes.js` era un stub `export const CLASSES = []`, así que el APK `v3.8.0` mostraba "0/0 clases" y ninguna tarjeta. Se confirmó extrayendo `assets/index.android.bundle` del APK publicado: 0 referencias al currículo frente al shell de la app presente.
- **`ClassScreen` crasheaba al abrir cualquier clase.** Llamaba a `normalizeLevel`, una función que no existía ni se importaba (`ReferenceError`). Estaba latente porque con el catálogo vacío nunca se llegaba a esa pantalla. Ahora usa `levelColor` del theme, que ya normaliza acentos.
- **Los 232 enlaces a Google Colab daban 404.** `mobile/src/utils/colab.js` apuntaba a la rama `master`; la única rama del remoto es `main`. Mismo fallo en `scripts/generate_release_pdfs.py` y `scripts/rebuild_curriculum.py`, que lo propagaban a los PDFs y notebooks generados.
- **El APK debug no era autónomo.** Con el valor por defecto de `debuggableVariants` (`["debug"]`), Gradle omite el bundle JS y la app instalada muere en "Unable to load script" sin un servidor Metro delante. Ahora `debuggableVariants = []`.

### Añadido
- **`scripts/generate_mobile_curriculum.py`** — genera `mobile/src/data/classes.js` desde `classes/**/README.md` (las 232 clases en 9 partes). El parser ancla las secciones en el **emoji** del encabezado, no en su texto, porque el título varía entre partes (`🗺️ Temas` vs `🗺️ Fases del capstone`, `📂 Dataset / recursos` vs `📂 Recursos`).
- **Navegación jerárquica en la app**: `HomeScreen` lista las 9 partes con progreso → `PartScreen` (nueva) lista las clases de la parte con buscador que ignora acentos → `ClassScreen` muestra el detalle. Una lista plana de 232 elementos era inusable. Nuevo componente `PartCard`.
- **`tests/test_mobile_curriculum.py`** — 20 tests sobre el catálogo embebido: reparto por parte, numeración contigua, campos no vacíos, enlaces de Colab a notebooks existentes, y un test que regenera y compara para detectar deriva respecto del markdown.
- **`.gitignore`**: los binarios de release (`*.apk`, `*.exe`, `*.zip`, `*.aab` bajo `dist_installer/`) quedan fuera del control de versiones. Pesan 140-280 MB y GitHub rechaza cualquier archivo de más de 100 MB, así que commitearlos rompía el push.

### Cambiado
- `mobile/package.json` (1.0.0) y `pyproject.toml` (2.0.0) estaban desincronizados del release; ambos pasan a `3.8.1`. La descripción de `pyproject.toml` seguía diciendo "12 clases".
- Android `versionCode 38 → 39`, `versionName "3.8.0" → "3.8.1"`.
- README, ROADMAP, RECRUITER, `docs/MOBILE_APP.md`, `docs/CATALOGO_PRODUCTO.md`, `docs/ARQUITECTURA_PRODUCTO.md` y `docs/GUIA_EVALUACION.md` dejaban de declarar el contenido móvil como "pendiente migrar".

### Verificado
- APK instalado en emulador Android (API 36): arranca **sin** servidor Metro, se recorre Home → Parte → Clase → Práctica sin crash y el progreso persiste entre pantallas.
- Instalador `.exe` verificado instalando en aislado: 232 clases y 232 notebooks en el payload. ZIP portable: 241 README + 232 notebooks. **Ninguno de los dos artefactos Windows tenía el fallo del catálogo** — leen el árbol `classes/` real que empaqueta PyInstaller.

---

## [v3.8.0] — 2026-06-19 (App Windows nativa con PySide6 — sin web ni localhost)

### Released
- **GitHub Release `v3.8.0`** publicado el 2026-06-19 con 5 assets:
  - `PythonDSProgram_windows_portable_v3.8.0.zip` (274 MB) — app Windows nativa Qt slim (sin PDFs/PPTX embebidos; el viewer los abre desde el repo).
  - `PythonDSProgram_android_v3.8.0_debug.apk` (139 MB) — APK Android debug (Expo SDK 51, versionCode 38).
  - `curso-completo.pdf` (1.9 MB) y `curso-completo.pptx` (2.0 MB) — bundles del currículo entero.
  - `SHA256SUMS_v3.8.0.txt` para verificación de integridad.
- Bundle Windows slim: `program.spec` ya no empaqueta `docs/pdfs/` ni los PDFs/PPTX en `classes/` — los botones "Abrir PDF/PPTX" abren la URL raw de GitHub (`https://github.com/.../raw/main/classes/...`). Bajó de 332 MB → 274 MB en el ZIP.
- Android `mobile/android/app/build.gradle`: bump `versionCode 1 → 38`, `versionName "1.0.0" → "3.8.0"`.
- `app_desktop/curriculum.py`: nuevas funciones `class_pdf_url`, `class_pptx_url`, `class_repo_url`, `open_pdf`, `open_pptx`, `open_url` que abren el archivo local en dev o la URL raw del repo en bundle frozen.

Link al release: https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.8.0

### Cambiado
- **`launcher.py` reescrito**: ya no arranca Flask+pywebview+Edge WebView2. Ahora arranca directo PySide6 (Qt nativo). El ejecutable .exe no levanta servidor HTTP ni renderiza web.
- **NUEVO paquete `app_desktop/`** (8 módulos, ~1000 líneas) — la app Windows nativa:
  - `main_window.py` — QMainWindow con QTreeView de los 9 partes + 232 clases, búsqueda en vivo, tabs README/Notebook, toolbar con "Abrir PDF/PPTX/Carpeta", navegación anterior/siguiente, theme light/dark persistente vía QSettings.
  - `readme_view.py` — QTextBrowser con `setMarkdown()` (rich text Qt **nativo**, no QWebEngineView).
  - `notebook_view.py` — QScrollArea + widgets por celda: markdown en QTextBrowser, code en QTextEdit oscuro monoespaciado, outputs (stdout, image/png base64 → QPixmap, errores en rojo).
  - `curriculum.py` — adapter que reusa `app.notebook_loader` y funciona en dev y en bundle PyInstaller (`sys._MEIPASS`).
  - `styles.py` — QSS light/dark.
- **`program.spec` reescrito**: bundle PyInstaller trae ahora PySide6 + shiboken6, sin pywebview/Flask/torch/sklearn. Empaqueta `classes/` + bundles PDF/PPTX + `app_desktop/`. El .exe queda en ~150-200 MB (vs ~500 MB del bundle anterior con torch).

### Conservado
- El laboratorio Flask + kernel Jupyter (`app/`) sigue como herramienta separada para EJECUTAR código sobre los notebooks (`python -m app.app`). La app desktop nativa es solo viewer; quien necesite ejecución usa el lab Flask.
- `installer/setup.iss` (Inno Setup), `build_windows.bat`, `docs/pdfs/`, `docs/presentaciones/`, todo el currículo.

### Tests
- `tests/test_app_desktop.py` — 6 smoke tests (corren con `QT_QPA_PLATFORM=offscreen`): paquete importable, adapter ve 232 clases, resolver de paths PDF/PPTX/notebook, MainWindow instanciable, NotebookView renderiza una clase real, ReadmeView usa setMarkdown.

### Por qué este cambio
El usuario pidió "app de Windows que no sea web y no levante localhost". El wrapper pywebview seguía dependiendo de Flask + Edge WebView2 (web por dentro). La nueva app PySide6 cumple: widgets Qt nativos, cero HTTP, cero WebView.

---

## [v3.7.0] — 2026-06-18 (35 notebooks faltantes generados · cobertura ejecutable 100%)

### Añadido
- 35 notebooks ejecutables faltantes generados para las "clases dedicadas modernas": Polars (033), Parquet/Arrow/DuckDB (034), async (049), walk-forward (053), target encoding+MICE (055), Optuna (058), Model Cards (060), SMOTE (064), calibración (076), SHAP profundo (087), Ray Tune (106), Lion/Sophia (114), Stochastic Depth (117), PyTorch fundamentos (122), Lightning (123), SAM (133), YOLOv11 (134), Flash Attention+RoPE+GQA (144), CLIP/SigLIP (146), Whisper (147), LoRA (149), DPO (150), vLLM (151), MCP (153), Agentes ReAct (154), LLM eval (155), SDXL/ControlNet (160), ONNX (167), JAX/Flax (173), Effect size (177), BCa bootstrap (184), CUPED (186), DoubleML (189), Synthetic Control (191), PyMC stack (193).
- Cada notebook: 12-16 celdas v3.0, self-contained con datasets sintéticos, seed 42, try/except sobre libs pesadas con fallback CPU-friendly para correr end-to-end en el laboratorio sin GPU.

### Cobertura del currículo
- **232 carpetas de clase · 232 READMEs pedagógicos · 232 notebooks ejecutables**. 🎓 Cobertura 100% real (no solo a nivel de README).
- El laboratorio con kernel Jupyter (Flask + jupyter_client + ipykernel, v3.6.0) puede ahora ejecutar cualquier clase del currículo.

### Arreglado
- `ruff` `I001` en `app/app.py` por imports aliased no agrupables: habilitada `combine-as-imports = true` en `pyproject.toml`. CI estaba en rojo desde v3.6.0 por esto; verde otra vez en commit aaf26a1.

---

## [v3.6.0] — 2026-06-18 (Laboratorio de ejecución Python: kernel Jupyter real)

### Cambiado
- **Reemplazo de `app/execution_engine.py` (exec() puro) por `app/kernel_manager.py`** — backend de ejecución ahora usa `jupyter_client` + `ipykernel` reales (un kernel Jupyter por sesión, no un namespace Python con `exec()`).
- **Nuevo `app/notebook_loader.py`** — el laboratorio lee los `classes/**/notebook.ipynb` reales del currículo en lugar de generar notebooks desde templates.
- **SPA frontend nueva** — `app/templates/index.html` + `app/static/styles.css` + `app/static/lab.js`: árbol del currículo navegable, celdas estilo Jupyter, outputs ricos (HTML, imágenes PNG/JPEG, errores con traceback, streams stdout/stderr), atajos Ctrl/Cmd+Enter (ejecutar) y Shift+Enter (ejecutar y avanzar), toggle theme dark/light.
- **Nuevas rutas API**: `GET /api/curriculum`, `GET /api/notebook/<slug>`, `POST /api/kernel/start`, `POST /api/kernel/<id>/execute`, `POST /api/kernel/<id>/interrupt`, `POST /api/kernel/<id>/restart`, `DELETE /api/kernel/<id>`.
- **Bundle completo** en `requirements.txt` (~2.5 GB) — torch CPU + transformers + sentence-transformers + faiss-cpu + xgboost + statsmodels + fairlearn + lightgbm + etc., para que el lab ejecute cualquier notebook del currículo sin pip-install adicional.

### Conservado
- `app/app.py` (shell Flask), `launcher.py`, instalador Windows + WebView2, `Dockerfile`, CSP estricto, modo local-first.

### Reality check
- **232 carpetas de clase con `README.md` pedagógico** (currículo completo a nivel de contenido).
- **197 clases con `notebook.ipynb` ejecutable**. Las **35 clases dedicadas modernas** (Polars, Optuna, Ray Tune, Lightning, etc.) tienen README pero notebook pendiente — el loader marca `has_notebook: bool` por clase y la UI deshabilita "Ejecutar" cuando es False.

---

## [v3.5.0] — 2026-06-18 (Parte 8 — Capstones completa · 🎓 currículo 232/232 = 100%)

### Añadido

- **Parte 8 — Capstones: 4/4 clases desarrolladas** (229-232) con patrón pedagógico v3.0 completo. Integrador de Partes 0-7 + Huyen *Designing ML Systems* + Hyndman & Athanasopoulos *FPP3* + timm/Lightning + MkDocs Material/Quarto.
  - **229 — Capstone 1: tabular E2E**: dataset sintético churn 10K filas, ColumnTransformer + GradientBoostingClassifier + Optuna 20 trials, MLflow opcional, curvas ROC + calibración, threshold F1, stubs FastAPI/Streamlit/SHAP + Model Card JSON.
  - **230 — Capstone 2: NLP o series**: dos ramas opt-in en README (A: DistilBERT/sentence-transformers/RAG mini; B: forecasting). Notebook implementa rama B completa — serie sintética multi-estacional 3 años, baselines naive + seasonal naive, ETS (statsmodels), Ridge con features lag/rolling, backtesting expanding window 5 folds, intervalos cuantiles, drift KS sobre residuos, stub FastAPI.
  - **231 — Capstone 3: visión transfer learning**: notebook CPU-friendly con dataset sintético 1000 patches 32×32 (círculo/cuadrado/triángulo), baseline LogReg, features HOG manuales, augmentation manual (flip+rotación+jitter), CNN PyTorch opcional con try/except, stubs timm/ONNX/FastAPI base64. README describe stack completo (ConvNeXt/EfficientNetV2/ViT, RandAugment/MixUp/CutMix, AMP, torch.compile).
  - **232 — Portafolio público**: clase final del programa. Notebook generador end-to-end del portafolio (dataclass Project, los 3 capstones llenos, renderers de project page + index + Model Card, validador con gate de calidad, stubs mkdocs.yml + GitHub Actions Pages, outlines de deck 10-15 slides y blog post, checklist 15 ítems, paths de especialización). README sin "siguiente clase" — cierre del programa con links al índice general.

### Cambiado

- ROADMAP v3.4.0 → v3.5.0; Parte 8 marcada `✅ completada`; entrada "🎓 Currículo completo: 232/232 (100%)" agregada.
- README de Parte 8 actualizado (fuente principal + estructura temática con numeración real 229-232 + foco específico por capstone).
- README raíz, badge de versión, estado del producto y mapa del currículo sincronizados a v3.5.0 (232/232 = 100%, "trabajo pendiente" reemplazado por sección "🎓 Programa completo").

### Cobertura del currículo

- **232/232 clases desarrolladas (100%)**. 🎓 Programa completo. Próximo foco del repo (no del currículo): regenerar PDFs/PPTX por bloques, migrar contenido a UI Android, mejoras al laboratorio de ejecución Python.

---

## [v3.4.0] — 2026-06-18 (Parte 7 — Ética, Fairness y Privacidad completa)

### Añadido

- **Parte 7 — Ética, Fairness y Privacidad: 6/6 clases desarrolladas** (223-228) con patrón pedagógico v3.0 completo. Fuente: Barocas/Hardt/Narayanan *Fairness and ML* (fairmlbook.org) + papers fundacionales (Suresh-Guttag 2021, Hardt-Price-Srebro 2016, Chouldechova 2017, Kleinberg-Mullainathan-Raghavan 2017, Dwork-Roth 2014, Abadi 2016, McMahan 2017, Zhu 2019, Pineau 2021, Mitchell 2019, Gebru 2018) + Reglamentos UE 2016/679 (GDPR) y 2024/1689 (AI Act).
  - **223 — Tipos de sesgo y orígenes**: taxonomía Suresh-Guttag (histórico, representación, medición, agregación, evaluación, despliegue) con demos sintéticas y caso Gender Shades.
  - **224 — Métricas de fairness**: demographic parity, equal opportunity, equalized odds, calibration. Impossibility theorem (Kleinberg/Chouldechova) demostrado numéricamente. Tooling: fairlearn/aif360.
  - **225 — Privacidad diferencial**: (ε,δ)-DP, mecanismos Laplace + Gaussiano, composición básica + avanzada, DP-SGD manual sobre regresión lineal, trade-off privacy-utility por ε.
  - **226 — Federated learning**: FedAvg implementado a mano con 10 clientes, simulación non-IID, demo didáctica de gradient leakage, defensas (secure agg, DP-FedAvg).
  - **227 — GDPR + EU AI Act**: bases legales, derechos del titular, Art. 22 decisiones automatizadas, DPIA. AI Act por niveles de riesgo (prohibido/alto/limitado/mínimo) + GPAI. Notebook utilitario con 8 chequeos programáticos de compliance.
  - **228 — Reproducibilidad**: seeds determinismo (Python/NumPy/Torch/sklearn), fuentes de non-determinism (GPU, hash, float assoc), lock files (uv/poetry/pip-compile), versionado de datasets (DVC/Git LFS), manifest con sha256, model cards (Mitchell 2019) y datasheets (Gebru 2018).

### Cambiado

- ROADMAP v3.3.0 → v3.4.0; Parte 7 marcada `✅ completada`.
- README de Parte 7 actualizado (fuente principal completa + estructura temática con numeración real 223-228).
- README raíz, badge de versión, estado del producto y mapa del currículo sincronizados a v3.4.0 (228/232 ≈ 98%).
- Siguiente prioridad: **Parte 8 — Capstones** (4 clases · 229-232).

### Cobertura del currículo

- **228/232 clases desarrolladas** (~98%). Pendientes: P8 (4) = 4 clases restantes (capstones).

---

## [v3.3.0] — 2026-06-17 (Parte 6 — Sistemas de Recomendación completa)

### Añadido

- **Parte 6 — Sistemas de Recomendación: 7/7 clases desarrolladas** (216-222) con patrón pedagógico v3.0 completo. Fuente: Aggarwal *Recommender Systems: The Textbook* + papers fundacionales (Koren 2009, Hu 2008, Burke 2002, Linden 2003).
  - **216 — Filtrado colaborativo user/item-based**: kNN con scipy.sparse, coseno/Pearson/Jaccard, por qué item-based gana en producción (Amazon 2003).
  - **217 — Matrix factorization SVD + ALS**: SVD truncado, ALS implementado a mano, implicit ALS con la lib `implicit` (Hu et al.), embeddings y PCA.
  - **218 — Content-based**: TF-IDF + cosine, sentence-transformers (`all-MiniLM-L6-v2`), FAISS para retrieval <10ms.
  - **219 — Híbridos**: los 7 patrones de Burke, weighted con tuning de α, switching cold-start, LightFM hybrid con features.
  - **220 — Métricas**: implementación desde cero de recall@k, precision@k, MAP@k, NDCG@k, coverage, diversity. Por qué NO usar RMSE en top-N.
  - **221 — Cold-start**: Bayesian shrinkage para popularity, onboarding explícito, novelty boost para items nuevos, epsilon-greedy bandit.
  - **222 — Librerías**: comparativa Surprise/Implicit/LightFM con NDCG@10 + tiempo; decision matrix por caso de uso.

### Cambiado

- ROADMAP v3.2.0 → v3.3.0; Parte 6 marcada `✅ completada`.
- README de Parte 6 actualizado (fuente principal completa + estructura temática + numeración corregida 216-222).
- Siguiente prioridad: **Parte 7 — Ética, Fairness, Privacidad** (6 clases · 223-228).

### Cobertura del currículo

- **222/232 clases desarrolladas** (~96%). Pendientes: P7 (6), P8 (4) = 10 clases restantes.

---

## [v3.2.0] — 2026-06-17 (Parte 5 — Ingeniería de Datos completa)

### Añadido

- **Parte 5 — Ingeniería de Datos: 8/8 clases desarrolladas** (208-215) con patrón pedagógico v3.0 completo. Fuente: Reis & Housley *Fundamentals of Data Engineering* (O'Reilly, 2022) + Kimball & Ross *Data Warehouse Toolkit* (Wiley, 3ª ed.) + docs oficiales del stack moderno.
  - **208 — Airflow + TaskFlow API**: DAGs idempotentes, retries/SLAs, XComs, catchup vs backfill, ETL vs ELT.
  - **209 — Prefect 3 + Dagster**: mismo pipeline con `@flow`/`@task` y con `@asset` SDA; comparativa con Airflow.
  - **210 — PySpark 3.5**: lazy DataFrames, broadcast join, AQE, particionado, salting para skew, Spark UI.
  - **211 — Polars 1.x**: eager vs lazy, streaming engine para datasets > RAM, Arrow zero-copy con DuckDB.
  - **212 — Data warehouses**: DuckDB local (full demo), BigQuery (dry-run + cost guard), Snowflake (cluster keys + time travel).
  - **213 — Streaming Kafka + Kinesis**: KRaft docker-compose, producer/consumer con consumer groups, at-least-once + idempotent dedupe.
  - **214 — Parquet + Avro**: benchmark CSV vs Parquet (snappy/zstd/gzip), row groups + stats, schema evolution backward-compatible.
  - **215 — Modelado dimensional**: star schema con DuckDB, `dim_date` precalculada, SCD Tipo 2 con surrogate keys (demo Alice cambia ciudad), grain decisión.

### Cambiado

- ROADMAP v3.1.0 → v3.2.0; Parte 5 marcada `✅ completada`.
- README de Parte 5 actualizado con estructura temática + numeración correcta (208-215).
- Siguiente prioridad: **Parte 6 — Sistemas de Recomendación** (7 clases · 216-222).

### Cobertura del currículo

- **215/232 clases desarrolladas** (~93%). Pendientes: P6 (7), P7 (6), P8 (4) = 17 clases restantes.

---

## [v3.1.0] — 2026-06-17 (Parte 4 — MLOps completa)

### Añadido

- **Parte 4 — MLOps: 14/14 clases desarrolladas** (194-207) con patrón pedagógico v3.0 completo (Objetivo · Resultados · Temas · Definiciones · Dataset · Ejercicios · Homework verificable · Errores comunes · FAQ · Referencias). Fuente: Huyen *Designing Machine Learning Systems* (O'Reilly) + ecosistema MLOps actual.
  - **194 — Versionado de datos con DVC 3.x**: `dvc.yaml`, remotes, `dvc exp`, lockfile, reproducibilidad point-in-time.
  - **195 — MLflow Tracking + Model Registry**: runs, autolog, registry con stages + aliases (`@champion`/`@challenger`).
  - **196 — Feature stores con Feast 0.40+**: offline/online store, point-in-time joins, materialización, training/serving skew.
  - **197 — CI/CD con GitHub Actions + CML**: workflows lint/test/train, OIDC para AWS, branch protection, CML comment con métricas.
  - **198 — Docker multi-stage**: imagen <500 MB, layer caching, non-root, distroless tradeoffs, digests vs tags.
  - **199 — FastAPI sirviendo modelos**: lifespan, Pydantic v2, sync vs async, batching, healthchecks, Prometheus.
  - **200 — Kubernetes**: 5 manifests mínimos (Deployment/Service/HPA/Ingress/ConfigMap), las 3 probes, rolling update + rollback.
  - **201 — Serverless ML**: Lambda Container Image + Cloud Functions 2nd gen, cold start mitigation, cost calculator vs K8s.
  - **202 — Monitoreo: data/model/concept drift**: PSI/KS/Wasserstein, Evidently AI, NannyML (CBPE), alertas con cooldown.
  - **203 — Reentrenamiento programado**: DAG Prefect/Airflow, champion-challenger, idempotencia, online vs continual training.
  - **204 — Shadow + canary + A/B test**: sticky assignment, auto-rollback por guardrails, sample size pre-calculado, rigor estadístico.
  - **205 — Interpretabilidad en producción**: SHAP TreeExplainer (rápido) vs KernelExplainer, PDP+ICE, LIME, endpoint `/explain`.
  - **206 — Testing de datos**: Great Expectations 1.x, Pandera, integración con DVC/Airflow como gate.
  - **207 — Behavioral tests**: invariance (gender swap), directional (income up), MFT, slice-based — al estilo CheckList (Ribeiro et al., ACL 2020 best paper).

### Cambiado

- ROADMAP, README de Parte 4 sincronizados con v3.1.0; Parte 4 marcada `✅ completada`.
- Siguiente prioridad: **Parte 5 — Ingeniería de datos** (8 clases · 208-215).

### Cobertura del currículo

- **207/232 clases desarrolladas** (~89%). Pendientes: P5 (8), P6 (7), P7 (6), P8 (4) = 25 clases restantes.

---

## [v3.0.0] — 2026-06-04 (BREAKING — gran restructuración del currículo)

### Cambios estructurales (BREAKING)

- **Currículo expandido a 232 clases** (antes 197). Numeración secuencial limpia **001-232** (sin sufijos `a/b/c`).
  - **Partes 0-3 (193 clases) 100 % completas** con patrón pedagógico v2.2.0 y modernización 2024-2026.
  - **35 clases dedicadas** a temas modernos integradas como clases propias (antes eran "complementos" dentro de otras clases).
  - **8 complementos previos convertidos a clases independientes** (validación temporal, FE+MICE, Ray Tune, Lion/Sophia, Stochastic Depth, Flash Attention/RoPE/GQA, BCa bootstrap, stack PyMC v5).

### Añadido

- **Parte 2 — Deep Learning: 75/75 clases desarrolladas** (100-174) con patrón pedagógico completo. Géron 3ª ed. (caps. 10-19) + ecosistema PyTorch + HuggingFace + papers seminales.
  - 19 clases dedicadas modernas: Ray Tune (HPO distribuido), Lion/Sophia/Schedule-Free (optimizadores 2023+), Stochastic Depth/DropPath/LayerDrop, PyTorch + Lightning, SAM/SAM 2, YOLOv11, Flash Attention v2/v3 + RoPE + GQA, CLIP/SigLIP, Whisper, LoRA/QLoRA, DPO/RLHF, vLLM/TGI, MCP (Model Context Protocol), Agentes (ReAct, multi-agent), LLM Evaluation (MMLU, MT-Bench, LLM-as-judge), SDXL + ControlNet, ONNX/ONNX Runtime, JAX/Flax.
- **Parte 3 — Estadística inferencial y causal: 19/19 clases desarrolladas** (175-193). ISLP + Bruce & Bruce + Pearl + Hernán & Robins.
  - 6 clases dedicadas modernas: effect size (Cohen's d/Hedges' g/Cliff's δ con pingouin), BCa bootstrap + APIs scipy modernas, CUPED + sequential testing + always-valid p-values, DoubleML/EconML (ML para causalidad), Synthetic Control Method (pysyncon, SparseSC), stack PyMC v5 + NumPyro + ArviZ.
- **Parte 0 expandida a 49 clases** (antes 46) con 3 clases dedicadas: Polars (DataFrames modernos), Parquet + Arrow + DuckDB, async / httpx / aiohttp.
- **Parte 1 expandida a 50 clases** (antes 43) con 7 clases dedicadas: validación temporal, FE avanzado + MICE, Optuna dedicado, Model Cards y Responsible ML, class imbalance/SMOTE, calibración de probabilidades, SHAP en profundidad.

### Cambiado

- **Numeración global renumerada**: P0=001-049, P1=050-099, P2=100-174, P3=175-193, P4=194-207, P5=208-215, P6=216-222, P7=223-228, P8=229-232.
- **200 carpetas de clase renombradas** con git rename detection preservada.
- **Limpieza de duplicados**: 17 anchors con complementos modernos en versión expansión-2026 pasaron a tener puntero corto a la clase dedicada en lugar de duplicar contenido.
- **Documentación sincronizada**: ROADMAP, README root, RECRUITER, RUNBOOK, 4 README de Parte, classes/README.md, 8 docs en `docs/` (INDEX, syllabus, cronograma, ARQUITECTURA, CATALOGO, GUIA_EVALUACION, MOBILE_APP, despliegue), site/index.html, site/product/index.html, mobile/src/data/classes.js.
- **site/clases regenerado** vía `scripts/generate_site_curriculum.py` (9 partes, 232 fichas HTML).
- **README root**: badges actualizados — v3.0.0, 232 clases, Partes 0-3 al 100 %, Partes 4-8 en desarrollo.

### Versión

- `v2.3.0` → `v3.0.0` (BREAKING por renumeración global; todos los enlaces externos a clases por número quedan invalidados).

---

## [v2.3.0] — 2026-06-01

### Añadido

- **Parte 1 — Machine Learning Clásico: 43/43 clases desarrolladas** ✅. Reemplaza los stubs por contenido completo siguiendo el patrón pedagógico v2.2.0 (Objetivo + Resultados verificables + Temas + Definiciones + Ejercicios + Homework + Errores comunes + FAQ + Referencias). Fuente principal: **Géron** (*Hands-On ML* 3ª ed., caps. 1–9). Total: **5.078 líneas** en los 43 README.
- **Cierre completo del audit de Parte 1: 8/8 complementos modernos integrados** en clases existentes (no se rompió la numeración):
  - Clase 049 → **validación temporal** (`TimeSeriesSplit`, walk-forward, gap).
  - Clase 050 → **feature engineering avanzado** (target encoding con CV out-of-fold, cyclic encoding, los 3 leakages) y **imputación avanzada** (`KNNImputer`, `IterativeImputer`/MICE, `MissingIndicator`).
  - Clase 052 → **HPO moderno** (Optuna con pruners, optimización bayesiana, `HalvingGridSearchCV`).
  - Clase 053 → **Model Cards y documentación responsable** (Mitchell 2018, HF model cards, Datasheets for Datasets, EU AI Act).
  - Clase 056 → **class imbalance** (`class_weight='balanced'`, SMOTE vía `imblearn`, threshold tuning con `precision_recall_curve`, warning anti-leakage).
  - Clase 067 → **calibración de probabilidades** (Platt, isotonic, temperature scaling, `CalibratedClassifierCV`).
  - Clase 077 → **interpretabilidad moderna SHAP/LIME** (`TreeExplainer`, `summary_plot`, `waterfall_plot`, PDP/ICE).
- **5 complementos modernos sumados a Parte 0** (cierran huecos del audit sin tocar el contenido existente):
  - Clase 004 → **testing con pytest** (fixtures, parametrize, qué testear en DS).
  - Clase 011 → **formatos columnares** Parquet/Arrow/Feather + `dtype_backend="pyarrow"`.
  - Clase 022 → **Polars** como alternativa moderna (tabla comparativa con pandas).
  - Clase 030 → **regex con módulo `re`** (metacaracteres, raw strings, regex101).
  - Clase 045 → **httpx + async** (`asyncio.gather`, `Semaphore` para rate limiting, `tenacity`).
- README de Parte 1 actualizado con marca de completitud (✅) y listado explícito de los 7 complementos modernos integrados.

### Cambiado

- README raíz: badge "Parte 0 46/46" reemplazado por badges **Parte 0 ✅** + **Parte 1 43/43 ✅**; versión a v2.3.0; estado a "Partes 2-8 en desarrollo".
- ROADMAP: marcado el ítem de Parte 1 (43 clases) como completado; versión actualizada a v2.3.0.
- `docs/CATALOGO_PRODUCTO.md`: estado del currículo "Partes 0-1 (89 clases) completas y ampliadas".
- `docs/syllabus.md`: tabla de estado de implementación refleja Parte 1 completa.

### Corregido

- Clase 073 (regresión con árboles): el link a "Siguiente clase" mostraba el path como texto visible; ahora usa un texto humano legible.

---

## [v2.2.0] — 2026-05-22

### Añadido

- **Parte 0 ampliada pedagógicamente — 46/46 clases** con tres secciones nuevas:
  - **📖 Definiciones y características** — términos técnicos con explicación + características clave (~230 ítems totales).
  - **⚠️ Errores comunes** — tabla "síntoma/mensaje → causa y cómo arreglar" basada en los bugs más frecuentes de alumnos (~230 ítems).
  - **❓ Preguntas frecuentes** — FAQs auténticas que aparecen al estudiar el tema (~230 ítems).
- Total: **~690 ítems pedagógicos nuevos** sobre los 46 README y notebooks.
- **Framework v2 del generador** (`scripts/build_parte0_classes.py`): el `ClassSpec` ahora acepta `definiciones`, `faq` y `errores_comunes`. Render automático en README (en posición didáctica óptima) y en notebook (3 celdas markdown insertadas antes de Referencias).
- **Skill global `python-version-control`** (`~/.claude/skills/python-version-control/`): audita coherencia de versión Python en cualquier repo (pyproject + Dockerfile + workflows + tox + pre-commit). Reportó y resolvió drift `3.10/3.11/3.12` en este repo.
- **Mejoras de descubribilidad en GitHub Pages**:
  - **Tabla de contenidos automática** al inicio de cada página de clase (anchors a los `H2`).
  - **Badges visuales** (📖 ⚠️ ❓) en la lista de clases de cada parte mostrando qué tiene cada una.
  - **Banner amarillo en `/clases/`** con contador global "X clases ya incluyen Definiciones · Errores · FAQ".
  - **Resumen "X de Y ampliadas"** en cada página de parte.

### Cambiado

- README raíz: badges actualizados (v2.2.0 + badge "Parte 0 46/46 completa" + estado partes 1-8 en desarrollo).
- ROADMAP: Parte 0 marcada explícitamente como ampliada.
- `docs/`: estado general del programa actualizado.

---

## [v2.1.0] — 2026-05-22

### Añadido

- **Parte 0 — Prerrequisitos: contenido pedagógico completo** (46 clases)
  - Setup (001–005): venv/uv/conda, Jupyter, Git, CCDS, VS Code
  - Python idiomático (006–013): tipos, comprehensions, funciones, OOP, pathlib, logging, type hints
  - NumPy (014–021): tipos, ufuncs, agregaciones, broadcasting, masks, sort, linalg, random
  - pandas (022–032): Series/DataFrame, indexing, joins, groupby, pivot, strings, time series, eval/query
  - Visualización (033–040): matplotlib base, subplots, seaborn, mapas folium/plotly
  - SQL + NoSQL + APIs (041–046): SQL básico/avanzado, DuckDB, MongoDB, requests, scraping
- Cada clase: README con objetivo + resultados + 5 ejercicios + homework verificable + referencias a libro fuente
- Cada notebook: 10–18 celdas ejecutables con código real (no stubs)
- `scripts/build_parte0_*.py` — generadores idempotentes por bloque temático
- `scripts/generate_site_curriculum.py` — publica los 197 README como HTML en GitHub Pages bajo `/clases/`
- Workflow `deploy-pages.yml` regenera HTML en cada push a `classes/**/README.md`
- Skill global `python-version-control` para auditar coherencia de versión Python en repos
- Páginas Pages live en https://vladimiracunadev-create.github.io/python-data-science-program/clases/

### Cambiado

- **Alineación Python 3.12** en toda la stack (pyproject `requires-python`, `target-version` ruff, Dockerfile `FROM`, CI matrix, security workflow). El currículo asume y enseña 3.12+; ahora coincide con CI/Docker.
- README raíz y ROADMAP marcan Parte 0 como completa

### Corregido

- Branch policy del environment `github-pages` (residuo de rename `master`→`main`)
- ruff `per-file-ignores` para scripts de generación con `sys.path.insert` entre imports

---

## [v2.0.0-scaffold] — 2026-05-17

Rediseño completo del currículo. Pasa de 31 clases en 13 módulos a **197 clases en 9 partes**, alineado con pauta profesional derivada de *Hands-On ML* (Géron 3ª ed.), *Python Data Science Handbook* (VanderPlas), *Designing ML Systems* (Huyen), *ISLP* (James et al) y *Fairness and ML* (Barocas/Hardt/Narayanan).

### Añadido

- `scripts/generate_v2_curriculum.py` — generador idempotente de los 197 stubs (carpeta + `README.md` + `notebook.ipynb` por clase)
- `classes/parte-{0..8}-*/NNN-tema/` — 197 carpetas de clase organizadas en 9 partes (Prerrequisitos, ML clásico, Deep Learning, Estadística inferencial, MLOps, Ingeniería de datos, Recomendadores, Ética, Capstones)
- `classes/README.md` — índice navegable de las 197 clases
- `historicos/README.md` — explicación de qué se archivó y por qué

### Cambiado

- `app/content_loader.py` — `list_classes()` ahora descubre clases por `rglob("notebook.ipynb")`, soportando anidamiento ilimitado
- `app/app.py` — rutas `/api/class/<path:slug>` y `/downloads/class/<path:slug>/<asset_kind>` aceptan slugs con `/`; nuevo `_valid_class_slug`
- `docs/syllabus.md` — reescrito para reflejar v2 (197 clases, 9 partes, orden recomendado de desarrollo, fuentes)
- `docs/CATALOGO_PRODUCTO.md`, `docs/ARQUITECTURA_PRODUCTO.md`, `docs/INDEX.md` — realineados con v2
- `README.md` — estado v2.0.0-scaffold + lista de migraciones pendientes
- `tests/test_app_endpoints.py` — migrados a slugs v2; quiz/PDF/PPTX en `skip` con razón explícita hasta regenerar assets

### Movido (`git mv`, historial preservado)

- `classes/*` → `historicos/classes-v1/` (las 31 clases v1 con contenido completo se conservan como referencia y fuente de material reutilizable)
- Documentación y scripts asociados al uso institucional original retirados del repositorio público (movidos a archivo personal fuera del repo)

### Pendiente

- Rellenar el contenido pedagógico de los 197 stubs (orden recomendado en `docs/syllabus.md`)
- Migrar `mobile/src/data/classes.js` al currículo v2
- Migrar `site/` al currículo v2
- Regenerar PDFs y PPTX para v2 (los actuales son v1)

---

## [v1.1.0] — 2026-04-28

Expansión del curriculum de 13 a 31 clases. El producto pasa de un curso introductorio a un programa completo de Data Science.

### Añadido

**Curriculum:**
- 18 nuevas clases (13–30) en 10 módulos adicionales: ¿Qué es la Ciencia de Datos?, NumPy, SQL básico, Seaborn, estadística inferencial, feature engineering, regresión lineal, árboles/Random Forest, Gradient Boosting, clustering, PCA, series de tiempo, ajuste de hiperparámetros, NLP, detección de anomalías, ética/sesgo/privacidad, redes neuronales, despliegue con Flask
- Cada nueva clase incluye: README, slides, teoria, ejercicios, homework, notebook, soluciones, preguntas, tecnologias, guia-codigo, PDF guía-explicativa, PPTX presentación
- `preguntas.md`, `tecnologias.md` y `guia-codigo.md` añadidos retroactivamente a clases 00–12

**Datasets:**
- `datasets/comentarios_productos.csv` — 100 reseñas sintéticas en español con etiqueta de sentimiento (Positivo/Negativo/Neutro), para clase 26 (NLP)

**Materiales generados:**
- 31 PDFs guía-explicativa en `docs/pdfs/classes/` y dentro de cada carpeta de clase
- 31 PPTXs presentación en `docs/presentaciones/classes/` y dentro de cada carpeta de clase
- `scripts/generate_class_docs.py` — generación reproducible de PDFs y PPTXs para clases 13–30

**Documentación:**
- `docs/syllabus.md` — currículo completo 31 clases, 13 módulos, perfil de salida actualizado
- `docs/cronograma-referencial.md` — 31 sesiones con modalidades intensiva, estándar y parte-tiempo
- `docs/CATALOGO_PRODUCTO.md` — superficies y artefactos actualizados a 31 clases
- `docs/ARQUITECTURA_PRODUCTO.md` — diagramas y tablas actualizados, tabla de módulos y datasets
- `docs/GUIA_EVALUACION.md` — reescrita con inventario real, walkthrough de 10 min y señales de madurez
- `docs/INDEX.md` — iconos por perfil, territorio 2 renombrado a "proceso de selección histórico"
- `site/index.html` — 31 class cards, stats actualizados
- `README.md`, `RECRUITER.md` — conteos actualizados, sección Android añadida

### Cambiado

- El producto deja de estar orientado exclusivamente a un perfil escolar — ahora cubre el recorrido completo de un Data Scientist, accesible para cualquier edad y nivel de entrada
- Documentación del repositorio reorientada para reflejar su uso como recurso personal y muestra de habilidades

---

## [v1.0.0] — 2026-04-09

Primera versión operativa y publicada como release oficial.

### Añadido

**App de escritorio Windows:**
- `launcher.py` reescrito con pywebview 6.1 — abre una ventana nativa de Windows (Edge WebView2) sin abrir el navegador del sistema
- puerto libre elegido automáticamente (no hardcodeado), elimina conflictos de red
- pantalla de carga animada mientras Flask interno inicia
- página de error en ventana si el servidor no responde en 45 segundos
- `run_program.py` mejorado — detecta puerto ocupado, espera health, abre navegador automáticamente, maneja Ctrl+C

**Build:**
- `program.spec` actualizado con `collect_all('webview')` para bundlear pywebview correctamente
- `console=False` en el spec — elimina la ventana negra de consola al lanzar el .exe
- `build_windows.bat` instala pywebview automáticamente, genera ZIP portable con PowerShell
- favicon SVG inline en `index.html` — elimina 404 en cada carga

**Seguridad:**
- CSP endurecida: eliminada dependencia de Google Fonts CDN externo
- `# nosec B310` y `# nosec B110` justificados en los polling loops de health check
- Bandit: 0 High, 0 Medium, 0 Low en el escaneo completo

**Documentación:**
- `README.md` actualizado — refleja app de escritorio, rutas por perfil, mapa documental completo
- `RUNBOOK.md` actualizado — incluye arranque en modo desktop, smoke checks, variables de entorno
- `SECURITY.md` reescrito — superficies por modo, tabla de protecciones detallada, versiones soportadas
- `docs/BUILD_INSTALLER.md` reescrito — arquitectura actualizada, WebView2 requirement, troubleshooting
- `docs/CATALOGO_PRODUCTO.md` actualizado — corrección de descripción del instalador Windows
- `docs/entorno-interactivo.md` reescrito — describe ambos modos (desktop + dev)
- `docs/ARQUITECTURA_PRODUCTO.md` actualizado — app de escritorio en diagramas
- `docs/INDEX.md` actualizado — incluye nuevos archivos estándar
- `LICENSE` completado con texto MIT completo + clarificaciones sobre componentes
- Creados: `RECRUITER.md`, `CHANGELOG.md`, `CONTRIBUTING.md`, `ROADMAP.md`

**Correcciones:**
- `app/app.py`: `_get_base_dir()` con soporte `sys._MEIPASS` para PyInstaller frozen mode
- `app/templates/index.html`: eliminado Google Fonts (requería conexión a internet)
- `app/static/styles.css`: fuentes del sistema (`Segoe UI, system-ui`) en lugar de Google Fonts

### Artefactos de release

| Artefacto | Tamaño | SHA256 |
|---|---|---|
| `PythonDSProgram_windows_portable_v1.0.0.zip` | 92 MB | `239d2261...` |
| `PythonDSProgram_android_v1.0.0_debug.apk` | 137 MB | `cb69408b...` |

Build: Python 3.12 · PyInstaller 6.19 · pywebview 6.1 · commit `487b229`

---

## [pre-v1.0.0] — 2026-04-08 (scaffolding inicial)

> Versiones de construcción — no publicadas como release. Documentadas aquí por completitud.

### Incluido en la construcción inicial

- Curriculum completo: clase 0 diagnóstica + clases 01–12 con teoría, slides, ejercicios, tarea, notebook y soluciones
- Laboratorio Flask con 10 rutas (clases, notebooks, ejecución, guardado, reset, health, ready)
- Motor de ejecución con sesiones persistentes, timeout, eviction y captura de matplotlib
- 6 notebooks interactivos en JSON para el laboratorio web
- 5 datasets sintéticos (CSV)
- Portal del alumno en `site/` + vista institucional en `site/product/`
- App Android (Expo/React Native) en `mobile/` con scaffold Android nativo
- 3 workflows de CI/CD (tests, security, deploy-pages)
- 4 módulos de tests (pytest)
- Documentación inicial: 19 documentos en `docs/`
- Dockerfile + docker-compose (dev y prod)
- Scripts de build y generación de PDFs

---

[v1.0.0]: https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v1.0.0
