<div align="center">

# 📝 Changelog

### **Historial de cambios por versión**

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-f59e0b?style=for-the-badge)](https://keepachangelog.com/es/1.0.0/)
[![SemVer](https://img.shields.io/badge/SemVer-2.0.0-3fb950?style=for-the-badge)](https://semver.org/lang/es/)

</div>

> 📌 Todos los cambios notables de este proyecto se documentan aquí.

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
