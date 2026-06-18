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

- 📚 **currículo modular** (232 clases · 9 partes · v3.4.0 · pauta derivada de Géron 3ª ed., VanderPlas, Huyen, ISLP, Barocas/Hardt/Narayanan + Reis & Housley, Kimball & Ross, Aggarwal + Suresh-Guttag, Hardt-Price-Srebro, Chouldechova, Kleinberg, Dwork-Roth, Abadi, McMahan + papers seminales 2002-2026) — **Partes 0-7 (228 clases ≈ 98%) completas y ampliadas** con Definiciones, Errores comunes y FAQ en cada clase + 35 clases dedicadas a temas modernos 2024-2026 + stack completo de MLOps (DVC, MLflow, Feast, K8s, FastAPI, drift, shadow/canary, SHAP, Great Expectations, behavioral tests) + data engineering (Airflow, PySpark, Polars, DuckDB/BQ/Snowflake, Kafka, Parquet/Avro, star schemas SCD2) + recomendadores (CF, SVD/ALS, content+FAISS, LightFM, métricas top-N, cold-start) + ética/fairness/privacidad (Suresh-Guttag taxonomía sesgos, DP/EO/calibration + impossibility theorem, privacidad diferencial (Laplace/Gauss/DP-SGD), federated learning (FedAvg + gradient leakage), GDPR + AI Act EU 2024/1689, reproducibilidad (seeds/lock files/model cards/datasheets)); Parte 8 (4 capstones) en desarrollo;
- 🧪 **laboratorio interactivo** (Flask + ejecución Python en tiempo real, matplotlib, pandas);
- 🖥️ **app de escritorio nativa para Windows** (pywebview + Edge WebView2, sin navegador);
- 📱 **app Android** (Expo/React Native, contenido embebido + Google Colab) — pendiente migrar contenido al índice actual;
- 🌐 **portal público** (GitHub Pages para alumnos + vista institucional) — pendiente migrar al índice actual;
- 📖 **documentación de producto** organizada por audiencia.

---

## ✅ Estado real en producción

| 🧩 Componente | 🚦 Estado verificado | 🔍 Evidencia |
|---|---|---|
| Backend Flask | ✅ operativo | 10 rutas, tests automatizados, CI en GitHub Actions |
| Ejecución de código Python | ✅ operativo | pandas, matplotlib (gráficos), scikit-learn, timeout 30s |
| 232 clases (228 desarrolladas, 4 scaffold) | ✅ operativo | `/api/classes` → 232 clases, `/api/class/<path:slug>` → HTML |
| 6 notebooks interactivos | ✅ operativo | `/api/notebooks` → 6 templates, ejecución por celda |
| App de escritorio Windows | 🟡 código operativo · binario pendiente | pywebview 6.1 + PyInstaller 6.19, ZIP portable 92MB |
| Instalador Windows | 🟡 pendiente de rebuild | Inno Setup — sin Python requerido en el PC del usuario |
| App Android | 🟡 APK debug | 137MB, Expo/React Native — pendiente migrar contenido |
| Portal del alumno | ✅ en vivo | GitHub Pages — pendiente migrar al índice actual |
| CI/CD | ✅ activo | 3 workflows: tests, security scan, deploy-pages |
| Análisis de seguridad | ✅ limpio | Bandit: 0 High, 0 Medium, 0 Low |

---

## 🧰 Stack técnico

| 🧱 Capa | 🔧 Tecnología |
|---|---|
| 🐍 Backend | Python 3.10–3.12, Flask 3.x |
| 📊 Data Science | pandas 2.x, numpy 1.26+, matplotlib 3.8+, scikit-learn 1.4+ |
| 🖥️ Desktop Windows | pywebview 6.1 (Edge WebView2), PyInstaller 6.19 |
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

- ✅ capacidad de integrar backend Python con experiencia de escritorio nativa (pywebview);
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

## 📬 Contacto

<div align="center">

**Vladimir Acuña**

[![GitHub](https://img.shields.io/badge/GitHub-vladimiracunadev--create-181717?style=for-the-badge&logo=github)](https://github.com/vladimiracunadev-create)

</div>
