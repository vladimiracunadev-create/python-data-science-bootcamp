<div align="center">

# 🎯 Para reclutadores y evaluadores técnicos

### **Evidencia técnica en 5 minutos · Sin lectura extensa**

[![Tiempo](https://img.shields.io/badge/lectura-5%20min-3fb950?style=for-the-badge)](#-c%C3%B3mo-evaluar-en-5-minutos)
[![Estado](https://img.shields.io/badge/CI-passing-3fb950?style=for-the-badge&logo=github-actions&logoColor=white)](https://github.com/vladimiracunadev-create/python-data-science-program/actions)
[![Bandit](https://img.shields.io/badge/Bandit-0%20issues-3fb950?style=for-the-badge)](SECURITY.md)

</div>

---

## 📦 Qué es este repositorio

Un sistema de capacitación en Python y Data Science que integra:

- 📚 **currículo modular** (232 clases · 9 partes · v3.8.0 · pauta derivada de Géron 3ª ed., VanderPlas, Huyen, ISLP, Barocas/Hardt/Narayanan + Reis & Housley, Kimball & Ross, Aggarwal + Suresh-Guttag, Hardt-Price-Srebro, Chouldechova, Kleinberg, Dwork-Roth, Abadi, McMahan + Hyndman & Athanasopoulos FPP3 + timm/Lightning/Albumentations + MkDocs Material/Quarto + papers seminales 2002-2026) — 🎓 **232/232 READMEs · 232/232 notebooks ejecutables · cobertura 100% real** con Definiciones, Errores comunes y FAQ en cada clase + 35 clases dedicadas a temas modernos 2024-2026 + stack completo de MLOps (DVC, MLflow, Feast, K8s, FastAPI, drift, shadow/canary, SHAP, Great Expectations, behavioral tests) + data engineering (Airflow, PySpark, Polars, DuckDB/BQ/Snowflake, Kafka, Parquet/Avro, star schemas SCD2) + recomendadores (CF, SVD/ALS, content+FAISS, LightFM, métricas top-N, cold-start) + ética/fairness/privacidad (Suresh-Guttag taxonomía sesgos, DP/EO/calibration + impossibility theorem, privacidad diferencial (Laplace/Gauss/DP-SGD), federated learning (FedAvg + gradient leakage), GDPR + AI Act EU 2024/1689, reproducibilidad (seeds/lock files/model cards/datasheets)) + **Capstones integradores** (Capstone 1 tabular E2E (ColumnTransformer+GBM+Optuna+MLflow+FastAPI+Streamlit+SHAP+CI), Capstone 2 NLP/series (DistilBERT o forecasting con baselines+SARIMA+backtesting+cuantiles), Capstone 3 visión transfer learning (ConvNeXt/EfficientNetV2/ViT + RandAugment/MixUp/CutMix + ONNX), Portafolio público (MkDocs Material/Quarto + GitHub Pages + demos hosted + deck + CV técnico)); ya no quedan clases pendientes — siguiente foco: superficies (regen PDFs/PPTX, mobile UI, mejoras lab de ejecución Python);
- 🧪 **laboratorio de ejecución Python** (Flask shell + kernel Jupyter real vía `jupyter_client`, lee notebooks reales del currículo, outputs ricos);
- 🖥️ **app de escritorio nativa para Windows** (PySide6 / Qt nativo · v3.8.0 — sin web, sin localhost, sin WebView; widgets Qt puros con QTreeView, QTextBrowser `setMarkdown`, QScrollArea por celda de notebook · diferencial técnico vs el wrapper pywebview anterior);
- 📱 **app Android** (Expo/React Native, contenido embebido + Google Colab) — pendiente migrar contenido al índice actual;
- 🌐 **portal público** (GitHub Pages para alumnos + vista institucional) — pendiente migrar al índice actual;
- 📖 **documentación de producto** organizada por audiencia.

---

## ✅ Estado real en producción

| 🧩 Componente | 🚦 Estado verificado | 🔍 Evidencia |
|---|---|---|
| Backend Flask | ✅ operativo | 10 rutas, tests automatizados, CI en GitHub Actions |
| Ejecución de código Python | ✅ operativo | Jupyter kernel real (`jupyter_client` + `ipykernel`), pandas, matplotlib, scikit-learn, timeout por celda + interrupt/restart |
| 232 clases · 232 notebooks ejecutables (🎓 100% real) | ✅ operativo | `/api/classes` → 232 clases, `/api/class/<path:slug>` → HTML, `/api/curriculum` → 232/232 con `has_notebook: true` |
| 6 notebooks interactivos | ✅ operativo | `/api/notebooks` → 6 templates, ejecución por celda |
| App de escritorio Windows | ✅ binario v3.8.0 publicado en release | PySide6 + PyInstaller — ZIP portable slim de 274 MB, sin Flask, sin localhost, sin Edge WebView2 |
| Instalador Windows | 🟡 Inno Setup pendiente | el ZIP portable ya está publicado en el release v3.8.0; el `.exe` con Inno Setup queda como paso opcional |
| App Android | ✅ APK debug v3.8.0 publicado en release | 139 MB, Expo SDK 51, versionCode 38 — pendiente migrar contenido (`mobile/src/data/classes.js` sigue stub) |
| Portal del alumno | ✅ en vivo | GitHub Pages — pendiente migrar al índice actual |
| CI/CD | ✅ activo | 3 workflows: tests, security scan, deploy-pages |
| Análisis de seguridad | ✅ limpio | Bandit: 0 High, 0 Medium, 0 Low |

---

## 🧰 Stack técnico

| 🧱 Capa | 🔧 Tecnología |
|---|---|
| 🐍 Backend | Python 3.10–3.12, Flask 3.x |
| 📊 Data Science | pandas 2.x, numpy 1.26+, matplotlib 3.8+, scikit-learn 1.4+ |
| 🖥️ Desktop Windows | PySide6 / Qt nativo (sin WebView), PyInstaller 6.19 |
| 📦 Instalador | Inno Setup 6 |
| 📱 Mobile | Expo SDK 51, React Native, Android Gradle |
| 🎨 Frontend | HTML/CSS/JS vanilla (SPA sin framework) |
| 🧪 Tests | pytest 8.x, 4 módulos |
| 🧹 Lint | ruff |
| 🔐 Security | Bandit |
| ⚙️ CI/CD | GitHub Actions (3 workflows) |
| 🚀 Deploy | GitHub Pages |
| 🐳 Contenedores | Docker + Docker Compose (prod variant) |

---

## 💪 Lo que demuestra este proyecto

- ✅ capacidad de construir una app de escritorio Windows verdaderamente nativa (Qt/PySide6: sin WebView, sin localhost, sin Flask de fondo);
- ✅ criterio de seguridad documentado y verificado con análisis estático;
- ✅ diseño pedagógico con separación clara entre contenido, laboratorio y presentación;
- ✅ estructura de producto con documentación organizada por audiencias;
- ✅ flujo de build reproducible desde fuente hasta instalador .exe y APK Android;
- ✅ operación local-first con múltiples modos de despliegue (venv, Docker, exe).

---

## 🚫 Lo que este proyecto no pretende demostrar

- ❌ una plataforma multiusuario SaaS lista para internet abierta;
- ❌ personalización infinita antes de un acuerdo comercial;
- ❌ profundidad total en todas las capas desde la primera versión.

---

## ⏱️ Cómo evaluar en 5 minutos

1. 📥 Clona el repo y ejecuta `python run_program.py` — el navegador abre automáticamente.
2. 🖱️ Haz clic en cualquier clase del sidebar — carga contenido Markdown con quiz.
3. 🐍 Abre una celda del notebook y ejecuta `import pandas as pd; print(pd.__version__)`.
4. 📦 Descarga el ZIP portable del Release y ejecuta `PythonDSProgram.exe` — se abre una ventana nativa.
5. 📖 Revisa [docs/GUIA_EVALUACION.md](docs/GUIA_EVALUACION.md) para la ruta ejecutiva completa.

---

## 📥 Descarga directa de binarios

Release oficial: [**v3.8.0**](https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.8.0) (publicado 2026-06-19).

- 🖥️ [`PythonDSProgram_windows_portable_v3.8.0.zip`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.8.0/PythonDSProgram_windows_portable_v3.8.0.zip) (274 MB) — descomprimir y ejecutar `PythonDSProgram.exe`, ventana Qt nativa sin instalación.
- 📱 [`PythonDSProgram_android_v3.8.0_debug.apk`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.8.0/PythonDSProgram_android_v3.8.0_debug.apk) (139 MB) — instalar directo en Android.
- 📄 [`curso-completo.pdf`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.8.0/curso-completo.pdf) (1.9 MB) y [`curso-completo.pptx`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.8.0/curso-completo.pptx) (2.0 MB) — currículo completo.
- 🔐 [`SHA256SUMS_v3.8.0.txt`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.8.0/SHA256SUMS_v3.8.0.txt) — verificación de integridad.

---

## 📬 Contacto

<div align="center">

**Vladimir Acuña**

[![GitHub](https://img.shields.io/badge/GitHub-vladimiracunadev--create-181717?style=for-the-badge&logo=github)](https://github.com/vladimiracunadev-create)

</div>
