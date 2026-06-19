<div align="center">

# 📦 Catálogo del producto

### **Fuente de verdad de superficies, artefactos y reglas de comunicación**

[![Autoridad](https://img.shields.io/badge/prioridad-este%20documento-ef4444?style=for-the-badge)](#-regla-de-prioridad)
[![Estado](https://img.shields.io/badge/release-v3.8.0-2e8b57?style=for-the-badge)](../CHANGELOG.md)

</div>

> ⚠️ Si algún README, landing o presentación contradice este documento, **este tiene prioridad.**
>
> 📌 El currículo tiene **232 clases en 9 partes** (v3.8.0, numeración secuencial 001-232). 🎓 **232/232 clases · 232/232 notebooks ejecutables · cobertura 100% real** — todas las partes están desarrolladas con contenido pedagógico real + notebook ejecutable corriendo en el laboratorio con kernel Jupyter + Definiciones/Errores/FAQ en cada clase + 35 clases dedicadas a temas 2024-2026 + stack completo MLOps (DVC, MLflow, Feast, K8s, FastAPI, drift, shadow/canary, SHAP, Great Expectations, behavioral tests) + data engineering (Airflow, Prefect/Dagster, PySpark, Polars, DuckDB/BQ/Snowflake, Kafka, Parquet/Avro, star schemas SCD2) + recomendadores (CF, SVD/ALS, content+FAISS, LightFM, métricas top-N, cold-start) + ética/fairness/privacidad (Suresh-Guttag taxonomía sesgos, DP/EO/calibration + impossibility theorem, privacidad diferencial (Laplace/Gauss/DP-SGD), federated learning (FedAvg + gradient leakage), GDPR + AI Act EU 2024/1689, reproducibilidad (seeds/lock files/model cards/datasheets)) + **Capstones integradores (P8)** — Capstone 1 tabular E2E (ColumnTransformer+GBM+Optuna+MLflow+FastAPI+Streamlit+SHAP+CI), Capstone 2 NLP/series (DistilBERT o forecasting con baselines+SARIMA+backtesting+cuantiles), Capstone 3 visión transfer learning (ConvNeXt/EfficientNetV2/ViT + RandAugment/MixUp/CutMix + ONNX), Portafolio público (MkDocs Material/Quarto + GitHub Pages + demos hosted + deck + CV técnico). Ya no quedan clases pendientes — **siguiente foco: superficies**. Pauta completa en [syllabus.md](syllabus.md), índice navegable en [../classes/README.md](../classes/README.md).

---

## 📖 Definiciones

| Término | Significado |
|---|---|
| **Superficie** | Forma concreta en que una audiencia interactúa con el producto |
| **Artefacto** | Archivo o salida reutilizable que apoya la evaluación, presentación u operación |
| **Ruta documental** | Documento canónico que ordena, explica o limita el producto |
| **Evolución** | Capacidad proyectada, pero no operativa hoy como pieza principal |

---

## 🎛️ Matriz canónica de superficies

| Superficie | Tipo | Estado | Audiencia | Qué entrega hoy |
|---|---|---|---|---|
| Laboratorio de ejecución Python (`app/`) | núcleo operativo | operativo | docente / estudiante guiado | Flask shell + kernel Jupyter real (`jupyter_client`), lee notebooks reales del currículo, outputs ricos (HTML/imágenes/errores), 🎓 232/232 notebooks ejecutables (cobertura 100%) |
| App de escritorio Windows (`launcher.py` + `app_desktop/` + `installer/`) | distribución de escritorio | ✅ [**binario publicado en release v3.8.0**](https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.8.0) (ZIP portable slim, 274 MB) | alumno / docente en aula | **app Qt nativa con PySide6 — sin web, sin localhost, sin WebView, sin Flask de fondo**; QTreeView con los 9 partes + 232 clases, QTextBrowser `setMarkdown` para los READMEs, render por celda para los notebooks (outputs PNG base64 → QPixmap). Sin Python instalado en el equipo del usuario. Bundle slim: PDFs/PPTX no van empaquetados — el viewer abre la URL raw de GitHub cuando el archivo local no existe. |
| App Android (`mobile/`) | distribución móvil | ✅ [**APK debug publicado en release v3.8.0**](https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.8.0) (139 MB · versionCode 38) · **catálogo vacío** | alumno en movimiento | código operativo, pero `mobile/src/data/classes.js` quedó como stub; pendiente cargar entradas del currículo actual |
| Portal del alumno (`site/`) | superficie pública | operativo | alumno | muestra el resumen de 232 clases en 9 partes con tarjeta por parte |
| Vista institucional (`site/product/`) | superficie pública | operativo (mensaje genérico) | institución / evaluador | narrativa del producto, alcance, arquitectura visual |
| Currículo modular (`classes/`) | base pedagógica | 🎓 **232/232 README + 232/232 notebooks ejecutables (100% real)** | docente / alumno | 232 clases organizadas en 9 partes (numeración secuencial 001-232: Prerrequisitos, ML clásico, Deep Learning, Estadística inferencial y causal, MLOps, Ingeniería de datos, Recomendadores, Ética, Capstones). Todas las clases incluyen Definiciones, Errores comunes y FAQ, más 35 clases dedicadas a temas 2024-2026 y stack completo de MLOps + data engineering + recomendadores + ética/fairness/privacidad + capstones integradores (tabular E2E, NLP/series, visión transfer learning, portafolio público). |
| Kit documental (`docs/`) | capa editorial | operativo | docente / stakeholder | metodología, operación, evaluación, seguridad y arquitectura |
| PDFs (`docs/pdfs/`) | artefacto de apoyo | ✅ generados | docente / alumno / evaluador | 232 PDFs por clase + 9 PDFs por parte + `curso-completo.pdf` (1.9 MB) |
| Presentaciones (`docs/presentaciones/`) | artefacto de apoyo | ✅ generados | docente | 232 PPTX por clase + 9 PPTX por parte + `curso-completo.pptx` (2.0 MB) |

---

## 🗂️ Estructura del currículo

| Parte | Tema | Clases |
|---|---|---|
| 0 | Prerrequisitos: Python, NumPy, pandas, Polars, Parquet/Arrow/DuckDB, viz, SQL, NoSQL, APIs, async | 49 (001-049) |
| 1 | Machine Learning clásico (regresión, clasificación, ensembles, no supervisado, Optuna, SHAP, calibración, Model Cards) | 50 (050-099) |
| 2 | Deep Learning (Keras + PyTorch + Lightning, CNN/SAM/YOLO, Transformers + Flash/RoPE/GQA, LLMs LoRA/DPO/vLLM, multimodal CLIP/Whisper, MCP/agentes, SDXL+ControlNet, RL, ONNX/JAX, despliegue) | 75 (100-174) |
| 3 | Estadística inferencial y causal (DoubleML, Synthetic Controls, CUPED, PyMC v5) | 19 (175-193) |
| 4 | MLOps en producción (DVC, MLflow, Feast, Docker, K8s, FastAPI, drift, shadow/canary, SHAP, Great Expectations, behavioral tests) | 14 (194-207) |
| 5 | Ingeniería de datos (Airflow, Prefect/Dagster, PySpark, Polars, DuckDB/BQ/Snowflake, Kafka, Parquet/Avro, star schemas SCD2) | 8 (208-215) |
| 6 | Sistemas de recomendación | 7 (216-222) |
| 7 | Ética, fairness, privacidad | 6 (223-228) |
| 8 | Capstones públicos | 4 (229-232) |
| | **Total** | **232** |

Cada clase vive en `classes/parte-N-slug/NNN-tema-slug/` con `README.md` pedagógico (Definiciones · Errores comunes · FAQ · referencias) + `notebook.ipynb` ejecutable v3.0 + `clase-NNN-...-guia-explicativa.pdf` + `clase-NNN-...-presentacion.pptx`. Las 232 clases están desarrolladas; no quedan stubs.

---

## ⚙️ Funcionalidad real por superficie

| Capacidad | Lab ejecución Python | App Windows | App Android | Portal alumno | Vista institucional |
|---|---|---|---|---|---|
| Ver contenido de las clases | ✅ (READMEs renderizados) | ✅ (Qt nativo, READMEs + notebooks) | ❌ (catálogo pendiente) | ✅ (resumen por parte) | ❌ |
| Ejecutar código Python | ✅ (runner local, kernel Jupyter) | ❌ (viewer puro, sin kernel) | ↗️ Google Colab | ❌ | ❌ |
| Leer código comentado | ✅ | ✅ | ✅ | ❌ | ❌ |
| Abrir en Colab | ❌ | ❌ | ✅ | ❌ | ❌ |
| Guardar notebooks | ✅ | ❌ (viewer puro) | ❌ | ❌ | ❌ |
| Seguimiento de progreso | ❌ | ❌ | ✅ (local) | ❌ | ❌ |
| Mostrar producto a terceros | parcial | ❌ | ❌ | parcial | ✅ |
| Operar sin internet | ✅ | ✅ | ✅ (contenido) | ❌ | ❌ |
| Sin Python instalado | ❌ | ✅ | ✅ | ✅ | ✅ |

---

## 🎨 Artefactos oficiales de apoyo

| Artefacto | Rol | Estado |
|---|---|---|
| `classes/README.md` | índice navegable de las 232 clases | vigente |
| `scripts/generate_v2_curriculum.py` | regeneración idempotente de la estructura de carpetas | vigente |
| `docs/pdfs/classes/` y `docs/pdfs/parts/` | 232 guías imprimibles por clase + 9 bundles por parte | ✅ generadas |
| `docs/pdfs/curso-completo.pdf` | currículo completo unificado (1.9 MB) | ✅ generado |
| `docs/presentaciones/classes/` y `docs/presentaciones/parts/` | 232 decks por clase + 9 bundles por parte | ✅ generados |
| `docs/presentaciones/curso-completo.pptx` | currículo completo unificado (2.0 MB) | ✅ generado |
| `docs/pdfs/guia-estudio-repositorio.pdf` | ruta de lectura rápida del repo | vigente |
| `docs/pdfs/guia-total-python-data-science.pdf` | guía ampliada de Python con DS | vigente |
| `scripts/generate_class_assets_v3.py` | regenerador idempotente del PDF + PPTX por clase | vigente |
| `scripts/generate_part_bundles.py` | regenerador de bundles por parte + unificado | vigente |
| `scripts/generate_extended_study_pdf.py` | regeneración de la guía ampliada | vigente |

---

## 📣 Reglas de comunicación

### Lo que sí se puede afirmar

- el repo contiene una pauta de curso completo de Python y Data Science **avanzado** (232 clases en 9 partes);
- la pauta está derivada de referentes profesionales (Géron, VanderPlas, Huyen, ISLP, Barocas/Hardt/Narayanan);
- el laboratorio interactivo es operativo como herramienta local de aula y consume la estructura del currículo;
- existen superficies públicas funcionales para alumno e institución;
- la propuesta puede arrancar acotada (un bloque) y crecer sin rehacer la base.

### Lo que no se debe mezclar

- **el currículo está completo a nivel de contenido pedagógico (🎓 232/232 README + 232/232 notebooks ejecutables · 232/232 PDFs · 232/232 PPTX · 100% real)** con Definiciones/Errores/FAQ en cada clase + 35 clases dedicadas a temas 2024-2026 + stack MLOps + data engineering + recomendadores + ética/fairness/privacidad + 4 capstones integradores; lo único pendiente para "llave en mano" es migrar el catálogo a la UI de la app Android;
- el portal del alumno **no es** todo el producto;
- la vista institucional **no reemplaza** el laboratorio;
- la app Android **no ejecuta Python nativo** — usa Google Colab;
- la app Windows es una app de escritorio Qt nativa real — **no abre el navegador del sistema, no usa WebView, no levanta Flask, no abre ningún puerto local**;
- el runner local **no debe presentarse** como SaaS expuesto a internet.

---

## 🚀 Siguiente paso (post-v3.8.0)

🎓 **El currículo está 100% real (v3.8.0: 232/232 README + 232/232 notebooks ejecutables + 232/232 PDFs + 232/232 PPTX).** El release v3.8.0 ya publicó el binario Windows nativo (PySide6) y el APK Android debug. Lo que queda:

1. cargar el contenido en la **app Android** (`mobile/src/data/classes.js` sigue stub vacío) y rebuild del APK para que la UI muestre las 232 clases;
2. firmar el binario Windows y opcionalmente generar el instalador Inno Setup (el `.iss` ya existe);
3. mejoras incrementales al laboratorio de ejecución Python (navegación jerárquica, modo oscuro configurable, etc.).

Para una primera implementación acotada por aula, **Parte 0 — Prerrequisitos** (49 clases, 001-049) sigue siendo el punto de entrada natural:

1. Setup y herramientas (clases 001–005)
2. Python aplicado a datos (clases 006–013)
3. NumPy completo (clases 014–021)
4. Pandas completo (clases 022–032) + Polars + Parquet/Arrow/DuckDB (033–034)
5. Visualización (clases 035–042)
6. SQL y fuentes de datos (clases 043–048) + async/httpx (049)

Con esto un alumno ya puede afrontar cualquier capstone tabular básico. Las partes 1 (ML clásico) y 3 (estadística inferencial) son el siguiente bloque natural.

---

## ⚖️ Regla de prioridad

Si alguna presentación, README o landing contradice esta matriz, **este documento tiene prioridad.**
