# 🏗️ Arquitectura del producto

> Vista de alto nivel del programa, sus superficies, límites operativos y la relación entre contenido, laboratorio y publicación.

---

## 🔭 Visión general

El producto se organiza en tres capas coordinadas:

- una **capa pedagógica reusable** (`classes/`, `datasets/`) — **197 clases en 9 partes** (currículo v2 scaffold); el currículo v1 con 31 clases completas vive en `historicos/classes-v1/`;
- una **capa operativa local** para el laboratorio (`app/`, `launcher.py`, `mobile/`);
- una **capa pública** para alumnos e institución (`site/`, GitHub Pages).

---

## 🗺️ Mapa de alto nivel

```mermaid
graph LR
    INST["🏫 Institución / evaluador"] --> PRODUCT["Vista institucional\nsite/product/"]
    ALUM["🎓 Alumno"] --> PORTAL["Portal del alumno\nsite/"]
    ALUM --> MOBILE["📱 App Android\nmobile/"]
    DOC["👩‍🏫 Docente"] --> LAB["🧪 Laboratorio local\napp/"]
    DOC --> WIN["🖥️ App escritorio Windows\nPythonDSProgram.exe"]

    PRODUCT --> DOCS["📚 Documentación canónica\ndocs/"]
    PORTAL --> DOCS
    WIN --> LAB
    MOBILE --> CLASSES["📂 Clases y materiales\nclasses/ — 197 clases · 9 partes (v2)"]
    MOBILE --> COLAB["☁️ Google Colab\n(ejecución externa)"]
    LAB --> CLASSES
    LAB --> NOTEBOOKS["📓 Notebooks base\napp/notebooks/"]
    LAB --> SAVED["💾 Notebooks guardados\napp/saved_notebooks/"]
    LAB --> DATA["🗃️ Datasets\ndatasets/ — 6 CSV sintéticos"]
    LAB --> HIST["🗄️ Currículo v1 archivado\nhistoricos/classes-v1/"]
    DOCS --> PDFS["📄 PDFs de apoyo\ndocs/pdfs/ — 31 guías v1 + estudios"]
    DOCS --> PPTX["📊 Presentaciones\ndocs/presentaciones/ — 31 PPTXs v1"]
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
    LOADER --> CLASSES["classes/\n197 clases v2 (rglob notebook.ipynb)"]
    NBAPI --> TEMPLATES["app/notebooks/\ntemplates JSON precargados"]
    EXECAPI --> ENGINE["execution_engine.py\ntimeout 30s · max 100 sesiones"]
    ENGINE --> SESSION["Sesión en memoria\nnamespace Python persistente"]
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

### `app/` — Laboratorio Flask

- renderiza la experiencia local de clase con acceso a las **197 clases v2** (descubrimiento por `rglob("notebook.ipynb")`);
- sirve endpoints de clases, notebooks y ejecución (`/api/class/<path:slug>`, `/api/notebook/`, `/api/execute`);
- agrega headers de seguridad y endpoints de salud (`/health`, `/ready`);
- mantiene el motor de ejecución con sesiones, timeout (30 s) y captura de salida.

### `launcher.py` — Ventana nativa Windows

- abre una ventana Edge WebView2 sin navegador del sistema;
- gestiona el ciclo de vida de Flask (arranque, healthcheck, apagado);
- elige un puerto libre automáticamente para evitar conflictos.

### `classes/` — Currículo modular (v2)

Concentra el contenido de las **197 clases** en 9 partes. Pauta derivada de Géron (Hands-On ML 3ª ed.), VanderPlas, Huyen, ISLP y Barocas/Hardt/Narayanan.

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

Layout por clase: `classes/parte-N-slug/NNN-tema-slug/` con `README.md` (ficha) + `notebook.ipynb` (stub). Materiales opcionales (`teoria.md`, `slides.md`, `ejercicios.md`, `homework.md`, `soluciones.ipynb`, `quiz.json`, PDF, PPTX) se añaden cuando una clase madura.

### `historicos/classes-v1/` — Currículo v1 archivado

Las 31 clases del currículo v1 con contenido completo (teoría, ejercicios, soluciones, PDF, PPTX). Congelado, se conserva como referencia y fuente de material reutilizable al rellenar los stubs v2.

### `app/notebooks/` — Labs interactivos

- templates JSON con celdas editables y ejecutables;
- desde Python básico hasta ML con pipelines;
- se guardan en `app/saved_notebooks/` con nombre y fecha.

### `mobile/` — App Android

- Expo/React Native con contenido del currículo v1 (31 clases) embebido — **pendiente migración a v2**;
- integración con Google Colab para ejecución de código;
- seguimiento de progreso local con AsyncStorage.

### `datasets/` — Datos sintéticos

| Dataset | Uso principal |
|---|---|
| ventas_tienda.csv | clases 01–05 · 07 · 09 · 11 |
| retencion_clientes.csv | clases 03 · 08 · 10 |
| soporte_tickets.csv | clases 02 · 06 |
| transporte.csv | clases 04 · 06 |
| estudiantes.csv | clases 04 · 09 · 10 |
| comentarios_productos.csv | clase 26 (NLP) |

### `site/` — Portales públicos

- `site/`: portal del alumno desplegado en GitHub Pages;
- `site/product/`: vista institucional con narrativa de producto;
- evita que la única entrada pública sea un README técnico.

### `docs/` — Documentación canónica

- ordena la narrativa de producto por audiencias;
- separa operación, seguridad, pedagogía y evaluación;
- **31 PDFs guía-explicativa v1** en `docs/pdfs/classes/` (regenerables por bloques al desarrollar v2);
- **31 PPTXs presentación v1** en `docs/presentaciones/classes/` (mismo plan);
- notas del maintainer en `docs/maintainer/`.

### `scripts/` — Automatización

| Script | Función |
|---|---|
| `generate_v2_curriculum.py` | **(v2)** genera la estructura de carpetas + stubs de las 197 clases |
| `generate_class_docs.py` | genera PDFs y PPTXs (diseñado para v1, requiere adaptación a v2) |
| `generate_class_assets.py` | genera assets por clase (mismo estado) |
| `generate_interview_pdfs.py` | regenera PDFs de entrevista (histórico) |
| `generate_extended_study_pdf.py` | regenera guía ampliada de estudio |
| `generar_pdf_documento.py` | generación genérica de PDFs |
| `rebuild_curriculum.py` | reconstruye estructura del curriculum v1 (histórico) |

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
- se acepta que la ruta móvil tiene APK debug como v1.0.0 — producción es roadmap.

---

## 🛣️ Camino de evolución

Ver [ROADMAP.md](../ROADMAP.md) para el detalle completo. Las mejoras naturales de la arquitectura son:

1. autenticación básica para modo servidor local de aula;
2. observabilidad mayor si el laboratorio evoluciona a multiusuario;
3. app de escritorio para macOS y Linux (pywebview soporta ambas plataformas);
4. panel de progreso del alumno visible al instructor;
5. build de producción firmado para la app Android.
