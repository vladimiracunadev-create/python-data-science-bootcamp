<div align="center">

# 🏗️ Arquitectura del producto

### **Vista funcional con diagramas Mermaid de las superficies, capas y fronteras**

[![Capas](https://img.shields.io/badge/capas-3-7c5cff?style=for-the-badge)](#-visi%C3%B3n-general)
[![Diagramas](https://img.shields.io/badge/diagramas-Mermaid-ec4899?style=for-the-badge&logo=mermaid)](#%EF%B8%8F-mapa-de-alto-nivel)
[![Local-first](https://img.shields.io/badge/postura-local--first-3fb950?style=for-the-badge)](#%EF%B8%8F-fronteras-importantes)

</div>

> 🗺️ Vista de alto nivel del programa, sus superficies, límites operativos y la relación entre contenido, laboratorio y publicación.

---

## 🔭 Visión general

El producto se organiza en tres capas coordinadas:

- una **capa pedagógica reusable** (`classes/`, `datasets/`) — **232 clases en 9 partes** (v3.8.0, numeración secuencial 001-232; 🎓 **232/232 clases · 232/232 notebooks ejecutables · cobertura 100% real** — el lab con kernel Jupyter ejecuta el 100% del currículo, modernizado 2024-2026 + 35 clases dedicadas a temas modernos + stack completo MLOps + data engineering + recomendadores + ética/fairness/privacidad + 4 capstones integradores tabular/NLP-series/visión/portafolio);
- una **capa operativa local** dividida en dos superficies independientes:
  - **App Windows nativa (PySide6)** — `launcher.py` + `app_desktop/` (Qt puro, sin web, sin localhost, sin WebView); es solo viewer del currículo (READMEs + notebooks con outputs renderizados).
  - **Laboratorio de ejecución Python (Flask + Jupyter kernel)** — `app/` (`python -m app.app`); herramienta separada para EJECUTAR código sobre los notebooks reales del currículo.
  - **App Android** (`mobile/`).
- una **capa pública** para alumnos e institución (`site/`, GitHub Pages).

---

## 🗺️ Mapa de alto nivel

```mermaid
graph LR
    INST["🏫 Institución / evaluador"] --> PRODUCT["Vista institucional\nsite/product/"]
    ALUM["🎓 Alumno"] --> PORTAL["Portal del alumno\nsite/"]
    ALUM --> MOBILE["📱 App Android\nmobile/"]
    DOC["👩‍🏫 Docente"] --> LAB["🧪 Lab ejecución Python\napp/ (Flask + Jupyter kernel)"]
    DOC --> WIN["🖥️ App escritorio Windows\nPythonDSProgram.exe"]

    PRODUCT --> DOCS["📚 Documentación canónica\ndocs/"]
    PORTAL --> DOCS
    WIN --> LAB
    MOBILE --> CLASSES["📂 Clases y materiales\nclasses/ — 232 clases · 9 partes"]
    MOBILE --> COLAB["☁️ Google Colab\n(ejecución externa)"]
    LAB --> CLASSES
    LAB --> NOTEBOOKS["📓 Notebooks base\napp/notebooks/"]
    LAB --> SAVED["💾 Notebooks guardados\napp/saved_notebooks/"]
    LAB --> DATA["🗃️ Datasets\ndatasets/ — 6 CSV sintéticos"]
    DOCS --> PDFS["📄 PDFs de apoyo\ndocs/pdfs/"]
    DOCS --> PPTX["📊 Presentaciones\ndocs/presentaciones/"]
```

---

## 🔬 Flujo funcional del laboratorio

```mermaid
graph TD
    USER["👩‍💻 Docente o estudiante guiado"] --> UI["Interfaz web\nindex.html + app.js"]
    UI --> CLASSAPI["GET /api/class/slug"]
    UI --> NBAPI["GET /api/notebook/id"]
    UI --> EXECAPI["POST /api/execute"]
    UI --> SAVEAPI["POST /api/notebook/save"]
    UI --> RESETAPI["POST /api/reset"]

    CLASSAPI --> LOADER["content_loader.py\n_safe_resolve + markdown"]
    LOADER --> CLASSES["classes/\n232 clases (rglob notebook.ipynb)"]
    NBAPI --> TEMPLATES["app/notebooks/\ntemplates JSON precargados"]
    EXECAPI --> ENGINE["kernel_manager.py\njupyter_client + ipykernel"]
    ENGINE --> SESSION["Kernel Jupyter por sesión\n(interrupt / restart)"]
    ENGINE --> FIGS["PNG base64\n(matplotlib inline)"]
    SAVEAPI --> SAVED["saved_notebooks/\nJSON del alumno"]
```

---

## 🖥️ Flujo de la app de escritorio Windows

```mermaid
graph TD
    EXE["PythonDSProgram.exe\nPyInstaller bundle"] --> LAUNCHER["launcher.py"]
    LAUNCHER --> PORT["_find_free_port()\npuerto efímero en loopback"]
    LAUNCHER --> FLASK["Flask daemon thread\napp.app"]
    LAUNCHER --> WV["pywebview\nEdge WebView2"]
    FLASK --> HEALTH["/health polling\n_wait_for_server()"]
    HEALTH --> LOAD["window.load_url()\nCarga la app en ventana nativa"]
    WV --> WIN["🖥️ Ventana nativa Windows\nsin navegador externo"]
```

---

## 🚀 Publicación y despliegue

```mermaid
graph LR
    REPO["📦 Repositorio GitHub\nmaster"] --> CI["⚙️ ci.yml\ntests + lint + docker"]
    REPO --> SEC["🔒 security.yml\nBandit + dep audit"]
    REPO --> PAGES["🌐 deploy-pages.yml\npush a master"]
    PAGES --> SITE["site/ publicado\nGitHub Pages"]

    LOCAL["💻 Máquina del docente"] --> VENV["python run_program.py\ndev mode"]
    LOCAL --> DOCKER["🐳 docker compose\ncontenedor"]
    LOCAL --> WINAPP["🖥️ PythonDSProgram.exe\napp de escritorio"]
    VENV --> LAB["app/ en localhost:8000"]
    DOCKER --> LAB
    WINAPP --> LAB
```

---

## 🧩 Componentes y responsabilidades

### `app/` — Laboratorio de ejecución Python (Flask shell + kernel Jupyter)

- **Flask shell** (`app/app.py`) sirve la SPA (`app/templates/index.html`) y enruta las API REST;
- **`app/kernel_manager.py`** gestiona kernels Jupyter reales vía `jupyter_client` + `ipykernel` (un kernel por sesión — soporta `execute`, `interrupt`, `restart`);
- **`app/notebook_loader.py`** descubre y lee los `classes/**/notebook.ipynb` reales del currículo (no genera notebooks desde templates) y marca `has_notebook: bool` por clase;
- rutas API: `/api/curriculum`, `/api/notebook/<slug>`, `/api/kernel/start`, `/api/kernel/<id>/execute`, `/api/kernel/<id>/interrupt`, `/api/kernel/<id>/restart`, `DELETE /api/kernel/<id>`;
- headers de seguridad (CSP estricto) + endpoints de salud (`/health`, `/ready`).

### `launcher.py` — Ventana nativa Windows

- abre una ventana Edge WebView2 sin navegador del sistema;
- gestiona el ciclo de vida de Flask (arranque, healthcheck, apagado);
- elige un puerto libre automáticamente para evitar conflictos.

### `classes/` — Currículo modular

Concentra el contenido de las **232 clases** en 9 partes (v3.7.0, numeración secuencial 001-232 — 🎓 **232 READMEs pedagógicos · 232 notebooks ejecutables · cobertura 100% real**, todas las clases corren en el laboratorio con kernel Jupyter). Pauta derivada de Géron (Hands-On ML 3ª ed.), VanderPlas, Huyen (Designing ML Systems), ISLP, Barocas/Hardt/Narayanan + Reis & Housley (Data Engineering), Kimball & Ross (Data Warehouse Toolkit), Aggarwal (Recommender Systems) + Suresh-Guttag 2021 (taxonomía sesgos), Hardt-Price-Srebro 2016 (equalized odds), Chouldechova 2017, Kleinberg 2017 (impossibility theorem), Dwork-Roth 2014 (privacidad diferencial), Abadi 2016 (DP-SGD), McMahan 2017 (FedAvg), Reglamentos UE 2016/679 y 2024/1689, Pineau 2021 (reproducibilidad), Mitchell 2019 (model cards), Gebru 2018 (datasheets) + **Capstones (P8)**: Hyndman & Athanasopoulos (Forecasting Principles & Practice 3ª ed.), timm/Lightning/Albumentations (visión transfer learning), MkDocs Material/Quarto (portafolio público) + papers seminales 2002-2026 (Flash Attention, LoRA, DPO, ControlNet, MCP, DoubleML, Synthetic Controls, Koren/Hu para MF, Burke para hybrids, CheckList para behavioral tests).

| Parte | Tema | Clases |
|---|---|---|
| 0 | Prerrequisitos: Python, NumPy, pandas, viz, SQL, NoSQL, APIs | 46 |
| 1 | Machine Learning clásico | 43 |
| 2 | Deep Learning (Keras, TF, CNN, RNN, Transformers, RL, despliegue) | 56 |
| 3 | Estadística inferencial y causal | 13 |
| 4 | MLOps en producción | 14 |
| 5 | Ingeniería de datos | 8 |
| 6 | Sistemas de recomendación | 7 |
| 7 | Ética, fairness, privacidad | 6 |
| 8 | Capstones | 4 |

Layout por clase: `classes/parte-N-slug/NNN-tema-slug/` con `README.md` (ficha pedagógica) + `notebook.ipynb` (ejecutable). En Parte 0 (clases maduras) el README incluye además **📖 Definiciones**, **⚠️ Errores comunes** y **❓ FAQ**. Materiales opcionales (`teoria.md`, `slides.md`, `ejercicios.md`, `homework.md`, `soluciones.ipynb`, `quiz.json`, PDF, PPTX) se añaden cuando una clase madura.

### `app/notebooks/` — Labs interactivos

- templates JSON con celdas editables y ejecutables;
- desde Python básico hasta ML con pipelines;
- se guardan en `app/saved_notebooks/` con nombre y fecha.

### `mobile/` — App Android

- Expo/React Native — **pendiente migrar el contenido embebido al índice actual**;
- integración con Google Colab para ejecución de código;
- seguimiento de progreso local con AsyncStorage.

### `datasets/` — Datos sintéticos

| Dataset | Descripción |
|---|---|
| ventas_tienda.csv | Ventas multitienda con categorías y medios de pago |
| retencion_clientes.csv | Serie mensual de altas, bajas e ingresos |
| soporte_tickets.csv | Tickets por categoría, prioridad y canal |
| transporte.csv | Viajes con origen, destino y retrasos |
| estudiantes.csv | Registro académico con asistencia y evaluaciones |
| comentarios_productos.csv | Reseñas en español con etiqueta de sentimiento |

La asignación dataset → clase se hace al desarrollar el contenido pedagógico de cada clase.

### `site/` — Portales públicos

- `site/`: portal del alumno desplegado en GitHub Pages;
- `site/product/`: vista institucional con narrativa de producto;
- evita que la única entrada pública sea un README técnico.

### `docs/` — Documentación canónica

- ordena la narrativa de producto por audiencias;
- separa operación, seguridad, pedagogía y evaluación;
- PDFs y PPTX por clase en `docs/pdfs/classes/` y `docs/presentaciones/classes/` (se regeneran por bloques al madurar el contenido de cada parte);
- notas del maintainer en `docs/maintainer/`.

### `scripts/` — Automatización

| Script | Función |
|---|---|
| `generate_v2_curriculum.py` | genera la estructura de carpetas + stubs de las 232 clases (idempotente) |
| `generate_class_docs.py` | genera PDFs y PPTXs por clase (pendiente adaptar al recorrido anidado) |
| `generate_class_assets.py` | genera assets por clase (mismo estado) |
| `generate_interview_pdfs.py` | regenera PDFs de entrevista |
| `generate_extended_study_pdf.py` | regenera guía ampliada de estudio |
| `generar_pdf_documento.py` | generación genérica de PDFs |

---

## ⚖️ Fronteras importantes

| Frontera | Decisión actual | Motivo |
|---|---|---|
| Portal público vs runner | separados | el alumno no necesita exposición directa al runner |
| Vista institucional vs README | separados pero coherentes | una superficie vende la idea, la otra documenta el repo |
| Laboratorio vs internet abierta | local-first | el runner no está endurecido para exposición externa |
| PDFs vs docs canónicas | PDFs son derivados | la fuente de verdad vive en el repo, no en binarios |
| App de escritorio vs browser | pywebview (Edge WebView2) | evita dependencia del navegador instalado |
| Android vs ejecución nativa | Google Colab como backend | mantiene el APK liviano, sin runtime Python en el dispositivo |

---

## 🧠 Trade-offs conscientes

- se privilegia **claridad pedagógica** por sobre multiusuario endurecido;
- se privilegia **operación local segura** por sobre exposición rápida a internet;
- se privilegia **separación de audiencias** por sobre una sola portada gigantesca;
- se usa pywebview (Edge WebView2) en lugar de Electron para mantener bundle liviano;
- se acepta que la ruta móvil tiene APK debug — producción es roadmap.

---

## 🛣️ Camino de evolución

Ver [ROADMAP.md](../ROADMAP.md) para el detalle completo. Las mejoras naturales de la arquitectura son:

1. autenticación básica para modo servidor local de aula;
2. observabilidad mayor si el laboratorio evoluciona a multiusuario;
3. app de escritorio para macOS y Linux (pywebview soporta ambas plataformas);
4. panel de progreso del alumno visible al instructor;
5. build de producción firmado para la app Android.
