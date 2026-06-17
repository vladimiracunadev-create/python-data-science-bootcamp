<div align="center">

# 🛣️ Roadmap

### **Dirección futura del Python Data Science Program**

[![Version](https://img.shields.io/badge/release-v3.3.0-2e8b57?style=for-the-badge)](CHANGELOG.md)
[![Estado](https://img.shields.io/badge/contenido-en%20desarrollo-f59e0b?style=for-the-badge)](#-trabajo-cr%C3%ADtico--completar-el-contenido-pedag%C3%B3gico)

</div>

> 🗺️ No es un compromiso de fechas — es un mapa de intención técnica y pedagógica.

---

## 📊 Estado actual — v3.3.0 (junio 2026 — Parte 6 Sistemas de Recomendación completa)

| 🎛️ Superficie | 🚦 Estado |
|---|---|
| 📚 Currículo (**232 clases**, 9 partes, numeración secuencial limpia 001-232) | 🟢 **Partes 0, 1, 2, 3, 4, 5 y 6 (222 clases) completas v3.3** (Definiciones · Errores · FAQ en cada clase + 35 clases dedicadas a temas modernos 2024-2026: Polars/Arrow/DuckDB, async, validación temporal, FE+MICE, Optuna, Model Cards, SMOTE, calibración, SHAP profundo, Ray Tune, Lion/Sophia, Stochastic Depth, PyTorch+Lightning, SAM/YOLOv11, Flash Attention/RoPE/GQA, CLIP/Whisper, LoRA/DPO/vLLM, MCP/Agentes/Eval, SDXL/ControlNet, ONNX, JAX/Flax, effect size, BCa bootstrap, CUPED+sequential, DoubleML, Synthetic Controls, PyMC v5/NumPyro/ArviZ) + **Parte 4 MLOps (14 clases): DVC, MLflow, Feast, GH Actions/CML, Docker multi-stage, FastAPI, Kubernetes, serverless cost calc, drift detection (PSI/KS/Wasserstein/CBPE), retraining (Prefect+champion-challenger), shadow/canary/auto-rollback, SHAP/LIME/PDP/ICE en producción, Great Expectations+Pandera, behavioral tests INV/DIR/MFT/slice** · Partes 5-8 (25 clases) pendientes desarrollo |
| 🧪 Laboratorio Flask | ✅ operativo |
| 🖥️ App de escritorio Windows (pywebview) | 🟡 código operativo · binario pendiente de rebuild |
| 📱 App Android | 🟡 APK debug publicado — pendiente migrar contenido al índice actual |
| 🌐 Portal del alumno | 🟡 en vivo — pendiente migrar al índice actual |
| 🏛️ Vista institucional | ✅ en vivo |
| 📖 Documentación | ✅ alineada con el currículo actual |

---

## 🔥 Trabajo crítico — completar el contenido pedagógico

### 📝 Contenido pedagógico

- [x] **0️⃣ Parte 0 — Prerrequisitos (49 clases · 001-049)** ✅ completada (mayo 2026, ampliada junio 2026 con clases dedicadas), **ampliada con Definiciones, Errores comunes y FAQ por clase** + 3 clases dedicadas modernas (Polars, Parquet/Arrow/DuckDB, async httpx/aiohttp) + 2 complementos integrados (regex, pytest) — VanderPlas + Ramalho + Tanimura + Mitchell + docs oficiales
- [x] **1️⃣ Parte 1 — ML clásico (50 clases · 050-099)** ✅ completada (junio 2026), patrón pedagógico completo + **7 clases dedicadas modernas** (validación temporal, FE avanzado + MICE, Optuna dedicado, Model Cards/Responsible ML, class imbalance + SMOTE, calibración Platt/isotonic, SHAP en profundidad) — Géron 3ª ed., caps. 1–9 + docs XGBoost/LightGBM/CatBoost
- [x] **2️⃣ Parte 2 — Deep Learning (75 clases · 100-174)** ✅ completada (junio 2026), patrón pedagógico completo + **19 clases dedicadas modernas 2024-2026** (Ray Tune, Lion/Sophia, Stochastic Depth, PyTorch+Lightning, SAM/YOLOv11, Flash Attention/RoPE/GQA, CLIP/SigLIP, Whisper, LoRA/QLoRA, DPO/RLHF, vLLM/TGI, MCP, Agentes ReAct, LLM Evaluation, SDXL+ControlNet, ONNX, JAX/Flax) — Géron 3ª ed. caps. 10-19 + papers seminales + HuggingFace + PyTorch ecosystem
- [x] **3️⃣ Parte 3 — Estadística inferencial y causal (19 clases · 175-193)** ✅ completada (junio 2026), patrón pedagógico completo + **6 clases dedicadas modernas** (effect size, BCa bootstrap, CUPED+sequential, DoubleML/EconML, Synthetic Controls, stack PyMC v5/NumPyro/ArviZ) — ISLP + Bruce & Bruce + Pearl + Hernán & Robins
- [x] **4️⃣ Parte 4 — MLOps (14 clases · 194-207)** ✅ completada (junio 2026), patrón pedagógico completo — Huyen *Designing ML Systems* + ecosistema MLOps actual (DVC 3, MLflow 2.x, Feast 0.40+, GH Actions+CML, Docker multi-stage, FastAPI+Pydantic v2, K8s+HPA, Lambda Container/Cloud Functions 2nd gen, Evidently+NannyML, Prefect 3, Istio canary, SHAP TreeExplainer en producción, Great Expectations 1.x+Pandera, behavioral tests al estilo CheckList)
- [x] **5️⃣ Parte 5 — Ingeniería de Datos (8 clases · 208-215)** ✅ completada (junio 2026), patrón pedagógico completo — Reis & Housley *Fundamentals of Data Engineering* + Kimball & Ross *Data Warehouse Toolkit* (Airflow TaskFlow API, Prefect 3 + Dagster assets, PySpark 3.5 broadcast/AQE/skew, Polars 1.x lazy+streaming, BigQuery/Snowflake/DuckDB cost-aware, Kafka KRaft + Kinesis, Parquet/Avro + schema evolution, star/snowflake schemas con SCD 2)
- [x] **6️⃣ Parte 6 — Sistemas de Recomendación (7 clases · 216-222)** ✅ completada (junio 2026), patrón pedagógico completo — Aggarwal *Recommender Systems* + Koren/Bell/Volinsky 2009 + Hu/Koren/Volinsky 2008 + Burke 2002 (user/item-based kNN, SVD+ALS implicit, content-based con sentence-transformers+FAISS, hybrid weighted/switching/LightFM, MAP@k/NDCG@k/coverage/diversity, cold-start con Bayesian shrinkage+bandits, comparativa Surprise/Implicit/LightFM)
- [ ] Desarrollar las 10 clases restantes de las **Partes 7-8 (223-232)** (siguiente prioridad: **7️⃣ Parte 7 — Ética, Fairness, Privacidad · 223-228**)

### 🔄 Superficies pendientes de migración

- [x] 📱 `mobile/src/data/classes.js` — actualizado a v3.0.0 (232 clases), pendiente UI Android para listar
- [x] 🌐 `site/` — regenerado contra el currículo v3.0.0 (`scripts/generate_site_curriculum.py`)
- [ ] 📄 `docs/pdfs/classes/` y `docs/presentaciones/classes/` — regenerar PDFs y PPTX por bloques al madurar el contenido
- [ ] 🔧 Adaptar `scripts/generate_class_docs.py` y `scripts/generate_class_assets.py` para que recorran la estructura anidada del currículo

### ✅ Verificación de calidad pedagógica

- [ ] 🤖 Script de CI que falle si una clase tiene `notebook.ipynb` con menos de N celdas reales
- [ ] 🔗 Script de CI que verifique que cada clase referencia un dataset existente
- [ ] 🧠 Quizzes interactivos pre/post lección como parte del estándar de cada clase

---

## ⏱️ Corto plazo — mejoras al núcleo existente

### 🧪 Laboratorio

- [ ] 📊 Indicador de progreso por clase en el sidebar (con cobertura de las 232 clases)
- [ ] 🌲 Navegación jerárquica (parte → clase) en lugar de lista plana
- [ ] 📥 Soporte para importar notebooks `.ipynb` externos
- [ ] 🌓 Modo oscuro / claro configurable desde la interfaz

### 🖥️ App de escritorio Windows

- [ ] 🎨 Icono personalizado (.ico) para el ejecutable y el instalador
- [ ] 📦 Instalador con soporte explícito a Edge WebView2 Runtime (descarga automática si falta)
- [ ] 🖼️ Modo quiosco (pantalla completa sin barra de menú)
- [ ] 🔏 Versión firmada digitalmente (para eliminar alertas de SmartScreen)

### 🔐 Seguridad y operación

- [ ] 🚦 Rate limiting básico en el motor de ejecución (por sesión)
- [ ] 📋 Log estructurado de ejecuciones para auditoría docente
- [ ] 🎭 Opción de modo demo (sin guardado de notebooks)

---

## 🎯 Mediano plazo — nuevas capacidades

### 🏗️ Plataforma

- [ ] 🔑 Autenticación básica opcional (PIN por clase o por cohorte)
- [ ] 💾 Exportación de notebooks guardados a `.ipynb`
- [ ] 📈 Panel de resumen de progreso por alumno (para el docente) con métricas a nivel de las 9 partes
- [ ] 🌍 Soporte multi-idioma (inglés como segunda lengua de la UI)

### 📱 App Android (post-migración de contenido)

- [ ] 🚀 Publicación en APK release (firmado) para distribución directa
- [ ] 🔄 Seguimiento de progreso con sincronización local
- [ ] 📴 Modo offline completo (sin Google Colab como dependencia para ver código)

---

## 🌠 Largo plazo — evolución del producto

### 👥 Multiusuario y red

- [ ] 🌐 Modo servidor local de aula (múltiples alumnos en la misma red WiFi)
- [ ] 🔐 Autenticación real (OAuth básico) para entornos compartidos
- [ ] 📊 Dashboard de clase para el instructor con estado de alumnos

### 🤖 IA integrada

- [ ] 🦙 Asistente local de consulta pedagógica (vía Ollama/modelo local)
- [ ] 💡 Sugerencias automáticas de corrección en ejercicios
- [ ] ⚡ Generación asistida de nuevos ejercicios por clase a partir del scaffold

### 📦 Distribución

- [ ] 🍎 Paquete de instalación para macOS (usando pywebview con backend cocoa)
- [ ] 🐧 Instalador para Linux (AppImage o .deb)
- [ ] 🐳 Imagen Docker pre-construida publicada en Docker Hub

---

## 🚫 Lo que NO es parte del roadmap

- ❌ conversión a SaaS con hosting externo (sale del scope de herramienta docente local);
- ❌ soporte para múltiples lenguajes de programación en el runner (el foco es Python);
- ❌ integración con LMS (Moodle, Canvas) sin un contrato específico que lo justifique;
- ❌ versión cloud con datos de alumnos en servidor externo sin acuerdo de privacidad.

---

## 💬 Cómo influir en el roadmap

- 📨 abre un issue describiendo la necesidad y el contexto educativo que la justifica;
- 🎯 las mejoras con casos de uso reales (cohortes específicas, problemas documentados) tienen prioridad;
- 🤝 las contribuciones de código son bienvenidas — ver [CONTRIBUTING.md](CONTRIBUTING.md).
