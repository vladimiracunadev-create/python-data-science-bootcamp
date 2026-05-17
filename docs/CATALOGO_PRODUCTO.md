# Catálogo del producto

> Fuente de verdad de superficies, artefactos y reglas de comunicación.
> Si algún README, landing o presentación contradice este documento, **este tiene prioridad.**

> **Estado:** v2.0.0-scaffold. El currículo creció de 31 a **197 clases en 9 partes**. La estructura de carpetas y stubs está creada; el contenido pedagógico de cada clase se desarrolla por bloques. Pauta completa en [syllabus.md](syllabus.md), índice navegable en [../classes/README.md](../classes/README.md).

---

## Definiciones

| Término | Significado |
|---|---|
| **Superficie** | Forma concreta en que una audiencia interactúa con el producto |
| **Artefacto** | Archivo o salida reutilizable que apoya la evaluación, presentación u operación |
| **Ruta documental** | Documento canónico que ordena, explica o limita el producto |
| **Evolución** | Capacidad proyectada, pero no operativa hoy como pieza principal |

---

## Matriz canónica de superficies

| Superficie | Tipo | Estado | Audiencia | Qué entrega hoy |
|---|---|---|---|---|
| Laboratorio interactivo (`app/`) | núcleo operativo | operativo | docente / estudiante guiado | acceso a las 197 clases (stubs), notebooks editables, ejecución Python en tiempo real, captura de gráficos, guardado local |
| App de escritorio Windows (`launcher.py` + `installer/`) | distribución de escritorio | listo para build | alumno / docente en aula | ventana nativa Edge WebView2 sin navegador, sin Python instalado en el equipo del usuario, Flask interno transparente |
| App Android (`mobile/`) | distribución móvil | **catálogo vacío** | alumno en movimiento | código operativo, pero `mobile/src/data/classes.js` quedó como stub en la migración; pendiente cargar entradas v2 |
| Portal del alumno (`site/`) | superficie pública | operativo · alineado con v2 | alumno | muestra el resumen de 197 clases en 9 partes con tarjeta por parte |
| Vista institucional (`site/product/`) | superficie pública | operativo (mensaje genérico) | institución / evaluador | narrativa del producto, alcance, arquitectura visual |
| Currículo modular (`classes/`) | base pedagógica | scaffold v2 operativo, contenido en desarrollo | docente / alumno | 197 clases organizadas en 9 partes (Prerrequisitos, ML clásico, Deep Learning, Estadística inferencial, MLOps, Ingeniería de datos, Recomendadores, Ética, Capstones) |
| Currículo v1 archivado (`historicos/classes-v1/`) | referencia | congelado | desarrollador de contenido | 31 clases v1 preservadas como fuente de material reutilizable |
| Kit documental (`docs/`) | capa editorial | operativo | docente / stakeholder | metodología, operación, evaluación, seguridad y arquitectura |
| PDFs (`docs/pdfs/`) | artefacto de apoyo | **vigente solo para v1** | docente / alumno / evaluador | 31 guías v1; se regenerarán por bloques al rellenar contenido v2 |
| Presentaciones (`docs/presentaciones/`) | artefacto de apoyo | **vigente solo para v1** | docente | 31 decks v1; mismo plan de regeneración |

---

## Estructura del currículo v2

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
| | **Total** | **197** |

Cada clase vive en `classes/parte-N-slug/NNN-tema-slug/` con `README.md` (ficha) + `notebook.ipynb`. Materiales opcionales (`teoria.md`, `slides.md`, `ejercicios.md`, `homework.md`, `soluciones.ipynb`, `quiz.json`, PDF, PPTX) se añaden conforme cada clase madura.

---

## Funcionalidad real por superficie

| Capacidad | Lab Flask | App Windows | App Android | Portal alumno | Vista institucional |
|---|---|---|---|---|---|
| Ver contenido de las clases v2 | ✅ (stubs) | ✅ (tras rebuild) | ❌ (pendiente) | ❌ (pendiente) | ❌ |
| Ejecutar código Python | ✅ (runner local) | ✅ (runner local) | ↗️ Google Colab | ❌ | ❌ |
| Leer código comentado | ✅ | ✅ | ✅ (v1) | ❌ | ❌ |
| Abrir en Colab | ❌ | ❌ | ✅ | ❌ | ❌ |
| Guardar notebooks | ✅ | ✅ | ❌ | ❌ | ❌ |
| Seguimiento de progreso | ❌ | ❌ | ✅ (local, v1) | ❌ | ❌ |
| Mostrar producto a terceros | parcial | ❌ | ❌ | parcial | ✅ |
| Operar sin internet | ✅ | ✅ | ✅ (contenido) | ❌ | ❌ |
| Sin Python instalado | ❌ | ✅ | ✅ | ✅ | ✅ |

---

## Artefactos oficiales de apoyo

| Artefacto | Rol | Estado |
|---|---|---|
| `classes/README.md` | índice navegable de las 197 clases v2 | vigente |
| `scripts/generate_v2_curriculum.py` | regeneración idempotente de la estructura de carpetas | vigente |
| `docs/pdfs/classes/clase-NN-*-guia-explicativa.pdf` (×31) | guía imprimible por clase v1 | vigente para v1, regenerable para v2 cuando madure |
| `docs/presentaciones/classes/clase-NN-*-presentacion.pptx` (×31) | deck de presentación v1 | mismo estado |
| `docs/pdfs/guia-estudio-repositorio.pdf` | ruta de lectura rápida del repo | vigente, requiere refresh tras v2 |
| `docs/pdfs/guia-total-python-data-science.pdf` | guía ampliada de Python con DS | vigente |
| `scripts/generate_class_docs.py` | generación reproducible de PDFs y PPTXs (diseñado para v1) | vigente, requiere adaptación a v2 |
| `scripts/generate_class_assets.py` | generación de assets por clase | mismo estado |
| `scripts/generate_extended_study_pdf.py` | regeneración de la guía ampliada | vigente |

---

## Reglas de comunicación

### Lo que sí se puede afirmar

- el repo contiene una pauta de curso completo de Python y Data Science **avanzado** (197 clases en 9 partes);
- la pauta está derivada de referentes profesionales (Géron, VanderPlas, Huyen, ISLP, Barocas/Hardt/Narayanan);
- el laboratorio interactivo es operativo como herramienta local de aula y ya consume la estructura v2;
- existen superficies públicas funcionales para alumno e institución;
- el currículo v1 (31 clases con contenido completo) sigue disponible en `historicos/` como referencia y fuente de material;
- la propuesta puede arrancar acotada (un bloque) y crecer sin rehacer la base.

### Lo que no se debe mezclar

- **el currículo v2 está en scaffold**: la estructura existe pero el contenido de cada clase debe desarrollarse — no afirmar "197 clases listas para dictar";
- el portal del alumno **no es** todo el producto;
- la vista institucional **no reemplaza** el laboratorio;
- los PDFs v1 **no cubren** las clases v2 nuevas;
- la app Android v1 embebida **no refleja** el currículo v2 hasta que se regenere;
- la app Android **no ejecuta Python nativo** — usa Google Colab;
- el instalador Windows es una app de escritorio real — **no abre el navegador del sistema**;
- el runner local **no debe presentarse** como SaaS expuesto a internet.

---

## Versión inicial sugerida para primeros pasos (v2)

Para una primera implementación acotada, desarrollar primero el **Bloque 0 — Prerrequisitos** (46 clases):

1. Setup y herramientas (clases 001–005)
2. Python aplicado a datos (clases 006–013)
3. NumPy completo (clases 014–021)
4. Pandas completo (clases 022–032)
5. Visualización (clases 033–040)
6. SQL y fuentes de datos (clases 041–046)

Con esto un alumno ya puede afrontar cualquier capstone tabular básico. Las partes 1 (ML clásico) y 3 (estadística inferencial) son el siguiente bloque natural.

---

## Regla de prioridad

Si alguna presentación, README o landing contradice esta matriz, **este documento tiene prioridad.**
