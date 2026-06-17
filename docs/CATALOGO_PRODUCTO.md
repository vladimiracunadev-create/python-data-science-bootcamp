<div align="center">

# 📦 Catálogo del producto

### **Fuente de verdad de superficies, artefactos y reglas de comunicación**

[![Autoridad](https://img.shields.io/badge/prioridad-este%20documento-ef4444?style=for-the-badge)](#-regla-de-prioridad)
[![Estado](https://img.shields.io/badge/release-v3.3.0-2e8b57?style=for-the-badge)](../CHANGELOG.md)

</div>

> ⚠️ Si algún README, landing o presentación contradice este documento, **este tiene prioridad.**
>
> 📌 El currículo tiene **232 clases en 9 partes** (v3.3.0, numeración secuencial 001-232). **Partes 0-6 (222 clases ≈ 96%) están completas y modernizadas** con contenido pedagógico real + Definiciones/Errores/FAQ en cada clase + 35 clases dedicadas a temas 2024-2026 + stack completo MLOps (DVC, MLflow, Feast, K8s, FastAPI, drift, shadow/canary, SHAP, Great Expectations, behavioral tests) + data engineering (Airflow, Prefect/Dagster, PySpark, Polars, DuckDB/BQ/Snowflake, Kafka, Parquet/Avro, star schemas SCD2) + recomendadores (CF, SVD/ALS, content+FAISS, LightFM, métricas top-N, cold-start). **Partes 7-8 (10 clases)** tienen la estructura scaffold y se desarrollan por bloques. Pauta completa en [syllabus.md](syllabus.md), índice navegable en [../classes/README.md](../classes/README.md).

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
| Laboratorio interactivo (`app/`) | núcleo operativo | operativo | docente / estudiante guiado | acceso a las 232 clases (stubs), notebooks editables, ejecución Python en tiempo real, captura de gráficos, guardado local |
| App de escritorio Windows (`launcher.py` + `installer/`) | distribución de escritorio | listo para build | alumno / docente en aula | ventana nativa Edge WebView2 sin navegador, sin Python instalado en el equipo del usuario, Flask interno transparente |
| App Android (`mobile/`) | distribución móvil | **catálogo vacío** | alumno en movimiento | código operativo, pero `mobile/src/data/classes.js` quedó como stub; pendiente cargar entradas del currículo actual |
| Portal del alumno (`site/`) | superficie pública | operativo | alumno | muestra el resumen de 232 clases en 9 partes con tarjeta por parte |
| Vista institucional (`site/product/`) | superficie pública | operativo (mensaje genérico) | institución / evaluador | narrativa del producto, alcance, arquitectura visual |
| Currículo modular (`classes/`) | base pedagógica | **Partes 0-6 (222 ≈ 96%) completas y modernizadas** · Partes 7-8 (10) scaffold | docente / alumno | 232 clases organizadas en 9 partes (numeración secuencial 001-232: Prerrequisitos, ML clásico, Deep Learning, Estadística inferencial y causal, MLOps, Ingeniería de datos, Recomendadores, Ética, Capstones). Partes 0-6 incluyen Definiciones, Errores comunes y FAQ en cada clase, más 35 clases dedicadas a temas 2024-2026 y stack completo de MLOps + data engineering + recomendadores. |
| Kit documental (`docs/`) | capa editorial | operativo | docente / stakeholder | metodología, operación, evaluación, seguridad y arquitectura |
| PDFs (`docs/pdfs/`) | artefacto de apoyo | se regenera por bloque | docente / alumno / evaluador | guías PDF por clase al madurar el contenido |
| Presentaciones (`docs/presentaciones/`) | artefacto de apoyo | se regenera por bloque | docente | decks `.pptx` por clase al madurar el contenido |

---

## 🗂️ Estructura del currículo

| Parte | Tema | Clases |
|---|---|---|
| 0 | Prerrequisitos: Python, NumPy, pandas, visualización, SQL, NoSQL, APIs | 46 |
| 1 | Machine Learning clásico (regresión, clasificación, ensembles, no supervisado) | 43 |
| 2 | Deep Learning (Keras, TensorFlow, CNN, RNN, Transformers, RL, despliegue) | 56 |
| 3 | Estadística inferencial y causal | 13 |
| 4 | MLOps en producción (Docker, CI/CD, MLflow, monitoreo, interpretabilidad) | 14 |
| 5 | Ingeniería de datos (Spark, Airflow, lakehouses, streaming) | 8 |
| 6 | Sistemas de recomendación | 7 |
| 7 | Ética, fairness, privacidad | 6 |
| 8 | Capstones públicos | 4 |
| | **Total** | **232** |

Cada clase vive en `classes/parte-N-slug/NNN-tema-slug/` con `README.md` (ficha) + `notebook.ipynb`. Materiales opcionales (`teoria.md`, `slides.md`, `ejercicios.md`, `homework.md`, `soluciones.ipynb`, `quiz.json`, PDF, PPTX) se añaden conforme cada clase madura.

---

## ⚙️ Funcionalidad real por superficie

| Capacidad | Lab Flask | App Windows | App Android | Portal alumno | Vista institucional |
|---|---|---|---|---|---|
| Ver contenido de las clases | ✅ (stubs) | ✅ (tras rebuild) | ❌ (pendiente) | ❌ (pendiente) | ❌ |
| Ejecutar código Python | ✅ (runner local) | ✅ (runner local) | ↗️ Google Colab | ❌ | ❌ |
| Leer código comentado | ✅ | ✅ | ✅ | ❌ | ❌ |
| Abrir en Colab | ❌ | ❌ | ✅ | ❌ | ❌ |
| Guardar notebooks | ✅ | ✅ | ❌ | ❌ | ❌ |
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
| `docs/pdfs/classes/` | guías imprimibles por clase | se regenera por bloque al madurar el contenido |
| `docs/presentaciones/classes/` | decks de presentación por clase | mismo estado |
| `docs/pdfs/guia-estudio-repositorio.pdf` | ruta de lectura rápida del repo | vigente |
| `docs/pdfs/guia-total-python-data-science.pdf` | guía ampliada de Python con DS | vigente |
| `scripts/generate_class_docs.py` | generación reproducible de PDFs y PPTXs | pendiente adaptar al recorrido anidado |
| `scripts/generate_class_assets.py` | generación de assets por clase | mismo estado |
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

- **el currículo está parcialmente desarrollado**: Partes 0-6 (222 clases ≈ 96%) completas y modernizadas con Definiciones/Errores/FAQ en cada clase + 35 clases dedicadas a temas 2024-2026 + stack MLOps + data engineering + recomendadores; Partes 7-8 (10 clases) son scaffold cuya estructura existe pero el contenido pedagógico debe desarrollarse — no afirmar "232 clases listas para dictar";
- el portal del alumno **no es** todo el producto;
- la vista institucional **no reemplaza** el laboratorio;
- la app Android **no ejecuta Python nativo** — usa Google Colab;
- el instalador Windows es una app de escritorio real — **no abre el navegador del sistema**;
- el runner local **no debe presentarse** como SaaS expuesto a internet.

---

## 🚀 Versión inicial sugerida para primeros pasos

Para una primera implementación acotada, **las Partes 0-6 (222 clases) ya están desarrolladas** (v3.3.0). El próximo bloque a desarrollar es la **Parte 7 — Ética, Fairness, Privacidad** (6 clases, números 223-228). Si se quiere arrancar con un bloque chico ya listo, **Parte 0 — Prerrequisitos** (49 clases, 001-049) está completa:

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
