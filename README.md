# 🧭 Python Data Science Program

[![CI](https://github.com/vladimiracunadev-create/python-data-science-program/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/python-data-science-program/actions/workflows/ci.yml)
[![Security](https://github.com/vladimiracunadev-create/python-data-science-program/actions/workflows/security.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/python-data-science-program/actions/workflows/security.yml)
[![Pages](https://github.com/vladimiracunadev-create/python-data-science-program/actions/workflows/deploy-pages.yml/badge.svg?branch=main)](https://github.com/vladimiracunadev-create/python-data-science-program/actions/workflows/deploy-pages.yml)
![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-informational.svg)
![Version](https://img.shields.io/badge/release-v2.0.0--scaffold-2e8b57.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

Curso completo de Python y Data Science — desde fundamentos hasta despliegue de modelos en producción.

> **197 clases · 9 partes · pauta avanzada y completa**
>
> Índice navegable: [classes/README.md](classes/README.md) · Syllabus: [docs/syllabus.md](docs/syllabus.md)

Integra currículo modular extenso, laboratorio interactivo local, portal del alumno, app de escritorio nativa para Windows y app Android. La pauta se deriva de *Hands-On Machine Learning* (Géron, 3ª ed.), *Python Data Science Handbook* (VanderPlas), *Designing ML Systems* (Huyen), *ISLP* (James et al) y *Fairness and ML* (Barocas/Hardt/Narayanan).

> **Origen y orientación del proyecto:** este repositorio nació como **muestra de habilidades técnicas y pedagógicas**, y hoy se desarrolla como **recurso personal de aprendizaje, enseñanza y mejora continua del propio producto**. Es público y abierto a cualquier persona que quiera aprender, enseñar o contribuir.

---

## Estado actual del producto

> **Versión:** v2.0.0-scaffold
> **Clases:** 197 en 9 partes (Prerrequisitos, ML clásico, Deep Learning, Estadística inferencial, MLOps, Ingeniería de datos, Recomendadores, Ética, Capstones)
> **Estructura:** carpetas y stubs de `README.md` + `notebook.ipynb` generados para las 197 clases
> **Contenido pedagógico:** ⏳ en desarrollo — los stubs se rellenan por bloques siguiendo el orden de `docs/syllabus.md`
> **Laboratorio:** Flask local con ejecución Python en tiempo real, captura de gráficos y guardado de notebooks
> **Distribución:** app de escritorio Windows (Edge WebView2, sin navegador) + app Android (Expo/React Native)
> **Postura:** local-first — no internet abierta sin capas adicionales

### Trabajo pendiente

- Rellenar contenido pedagógico de las 197 clases (orden recomendado en `docs/syllabus.md` y `ROADMAP.md`)
- Migrar el contenido embebido del mobile (`mobile/src/data/classes.js`) a la estructura actual
- Migrar el portal `site/` al índice actual
- Generar PDFs y PPTX por bloque al madurar el contenido de cada parte

---

## Rutas recomendadas según perfil

| Perfil | Documento de entrada | Qué mirar primero |
|---|---|---|
| Institución / evaluador | [docs/GUIA_EVALUACION.md](docs/GUIA_EVALUACION.md) | valor, evidencia y límites reales |
| Reclutador técnico | [RECRUITER.md](RECRUITER.md) | evidencia técnica rápida en 5 minutos |
| Stakeholder técnico | [docs/ARQUITECTURA_PRODUCTO.md](docs/ARQUITECTURA_PRODUCTO.md) | capas, flujos y fronteras |
| Producto / maintainer | [docs/CATALOGO_PRODUCTO.md](docs/CATALOGO_PRODUCTO.md) | superficies, artefactos y reglas de comunicación |
| Docente | [docs/herramientas-pedagogicas-de-aula.md](docs/herramientas-pedagogicas-de-aula.md) | mediación, problemas de aula y ritmo |
| Alumno | [docs/student-guide.md](docs/student-guide.md) | uso del curso y expectativas |
| Operación | [RUNBOOK.md](RUNBOOK.md) | arranque, smoke checks y apagado |
| Seguridad | [SECURITY.md](SECURITY.md) | postura actual y riesgos aceptados |

Si no sabes por donde entrar, usa [docs/INDEX.md](docs/INDEX.md).

---

## Cómo leer este repo según tiempo disponible

| Tiempo | Secuencia recomendada | Resultado esperado |
|---|---|---|
| 5 minutos | `README` → `RECRUITER.md` | evidencia rápida de qué funciona hoy |
| 15 minutos | `README` → `docs/GUIA_EVALUACION.md` → `docs/CATALOGO_PRODUCTO.md` | entender superficies, arquitectura y criterio de operación |
| 30 minutos | secuencia anterior + `docs/syllabus.md` + `docs/ARQUITECTURA_PRODUCTO.md` | entender el currículo completo, capas y growth path |

La documentación está pensada como sistema, no como inventario de archivos.

---

## Superficies del producto

| Superficie | Rol | Estado |
|---|---|---|
| Laboratorio interactivo (`app/`) | entorno local de clase — notebooks, runner, ejecución Python | operativo |
| Portal del alumno (`site/`) | punto de entrada oficial para estudiantes | operativo |
| Vista institucional (`site/product/`) | presentación visual del producto | operativa |
| Currículo modular (`classes/`) | 197 clases en 9 partes: Prerrequisitos, ML clásico, Deep Learning, Estadística inferencial, MLOps, Ingeniería de datos, Recomendadores, Ética, Capstones | scaffold operativo · contenido en desarrollo |
| App de escritorio Windows (`launcher.py` + `program.spec` + `installer/`) | ventana nativa con Edge WebView2 — sin navegador, sin Python en el PC del alumno | código operativo · binario pendiente de build |
| App Android (`mobile/`) | Expo/React Native con integración Google Colab | código operativo · contenido pendiente de migración al índice actual |
| PDFs (`docs/pdfs/`) | guías por clase | se regeneran por bloques al madurar el contenido |
| Presentaciones (`docs/presentaciones/`) | decks `.pptx` por clase | se regeneran por bloques al madurar el contenido |

La fuente de verdad de esta taxonomía vive en [docs/CATALOGO_PRODUCTO.md](docs/CATALOGO_PRODUCTO.md).

---

## Materiales listos para usar

### Currículo (197 clases)

- Índice navegable: [classes/README.md](classes/README.md)
- Pauta completa: [docs/syllabus.md](docs/syllabus.md)
- Cada clase: `README.md` (ficha) + `notebook.ipynb` (stub). Los materiales PDF/PPTX se regeneran por bloque al madurar el contenido.


### 📄 PDFs de estudio adicionales

PDFs listos para imprimir o compartir. Viven en `docs/pdfs/` y son independientes del flujo de clases.

| Documento | Descripción |
|---|---|
| [guia-estudio-repositorio.pdf](docs/pdfs/guia-estudio-repositorio.pdf) | Ruta de lectura rápida del repo para evaluador o reclutador |
| [guia-total-python-data-science.pdf](docs/pdfs/guia-total-python-data-science.pdf) | Guía ampliada de Python con Data Science investigada con fuentes oficiales |

---

## Arquitectura en una mirada

```mermaid
graph LR
    INST["Institución"] --> PRODUCT["site/product/\nVista institucional"]
    ALUM["Alumno"] --> PORTAL["site/\nPortal del alumno"]
    ALUM --> MOBILE["mobile/\nApp Android"]
    DOC["Docente"] --> LAB["app/\nLaboratorio Flask"]
    DOC --> WIN["PythonDSProgram.exe\nApp de escritorio Windows"]

    PRODUCT --> DOCS["docs/\nDocumentación canónica"]
    PORTAL --> DOCS
    MOBILE --> CLASSES["classes/\n197 clases · 9 partes"]
    MOBILE --> COLAB["Google Colab\n(ejecución de código)"]
    LAB --> CLASSES
    LAB --> DATA["datasets/\n6 CSV sintéticos"]
    LAB --> NOTEBOOKS["app/notebooks/\n6 labs interactivos"]
    LAB --> SAVED["app/saved_notebooks/\nTrabajo del alumno"]
    WIN --> LAB
```

La arquitectura completa, con flujos y fronteras, está en [docs/ARQUITECTURA_PRODUCTO.md](docs/ARQUITECTURA_PRODUCTO.md).

---

## Capacidades actuales

### Currículo y pedagogía

- **Currículo (scaffold):** 197 clases en 9 partes — Prerrequisitos (46), ML clásico (43), Deep Learning (56), Estadística inferencial (13), MLOps (14), Ingeniería de datos (8), Recomendadores (7), Ética (6), Capstones (4);
- pauta derivada de **Hands-On ML** (Géron 3ª ed.), **Python Data Science Handbook** (VanderPlas), **Designing ML Systems** (Huyen), **ISLP** (James et al), **Fairness and ML** (Barocas/Hardt/Narayanan);
- cada clase: `README.md` (ficha) + `notebook.ipynb` (stub); materiales adicionales se agregan al madurar;
- **6 datasets** sintéticos: ventas_tienda, retencion_clientes, soporte_tickets, transporte, estudiantes, comentarios_productos;
- guías de instructor, metodología, criterios de evaluación y ética de datos.

### 🧪 Laboratorio interactivo

- app Flask con acceso a las 197 clases desde interfaz web (descubrimiento automático por anidamiento);
- notebooks interactivos precargados con celdas editables y ejecutables;
- ejecución de código Python por celdas con persistencia de sesión;
- captura de gráficos matplotlib como PNG inline;
- guardado de notebooks en JSON local (`app/saved_notebooks/`);
- endpoints `GET /health` y `GET /ready` para healthchecks.

### App de escritorio Windows

- ventana nativa con Edge WebView2 — **sin abrir el navegador del sistema**;
- Flask corre internamente en un puerto libre elegido automáticamente;
- pantalla de carga animada mientras el entorno inicia;
- portable (ZIP) + instalador (Inno Setup) disponibles;
- sin dependencias en el PC del usuario final.

### App Android

- Expo/React Native (pendiente migrar el contenido embebido al índice actual);
- integración con Google Colab para ejecución de código sin Python local;
- seguimiento de progreso local con AsyncStorage;
- APK debug disponible — producción en roadmap.

### 📊 Presentación y distribución de materiales

- PDFs y PPTX por clase se generan en `docs/pdfs/classes/` y `docs/presentaciones/classes/` por bloques al madurar el contenido pedagógico de cada parte;
- landing pública para alumnos en GitHub Pages (`site/`);
- vista institucional HTML con narrativa de producto (`site/product/`);
- PDFs adicionales de estudio en `docs/pdfs/`.

---

## Inicio rápido

### Opción A — app de escritorio Windows (usuarios finales)

El binario distribuible se reconstruye cuando el contenido alcance un primer hito publicable. Mientras tanto, usa el modo desarrollo (Opción B) o la imagen Docker (Opción C/D) para correr el laboratorio local. Ver [docs/BUILD_INSTALLER.md](docs/BUILD_INSTALLER.md) para construir el `.exe` desde fuente.

Requiere (al usar el binario): Edge WebView2 Runtime (preinstalado en Windows 10 v2004+ y Windows 11).

### Opción B — modo desarrollo (entorno virtual)

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
pip install -r requirements.txt
python run_program.py
```

Abre automáticamente `http://127.0.0.1:8000` en el navegador.

### Opción C — Docker local

```bash
docker compose up --build
```

### Opción D — Docker endurecido

```bash
docker compose -f docker-compose.prod.yml up -d --build
```

---

## Build de distribución

```bash
# Instala dependencias de build
pip install pywebview pyinstaller

# Genera bundle + ZIP portable + instalador (requiere Inno Setup 6)
build_windows.bat
```

Ver [docs/BUILD_INSTALLER.md](docs/BUILD_INSTALLER.md) para instrucciones completas.

---

## Validación y CI/CD

```bash
pytest                   # suite completa
ruff check .             # lint
python -m bandit -r app  # seguridad estática
```

Workflows activos:

| Workflow | Qué cubre |
|---|---|
| [ci.yml](.github/workflows/ci.yml) | tests, lint, build de contenedor |
| [security.yml](.github/workflows/security.yml) | auditoría de dependencias, SAST |
| [deploy-pages.yml](.github/workflows/deploy-pages.yml) | despliegue de `site/` a GitHub Pages |

---

## Seguridad y límites

**Protecciones activas:**

- validación de slugs e identificadores (regex, evita path traversal);
- límite de payload por request (1 MB);
- límite de longitud de código (20 KB);
- timeout de ejecución por celda (30 s) + reinicio de sesión;
- eviction de sesiones antiguas (100 sesiones máx, TTL 1 hora);
- CSP estricto sin dependencias CDN externas;
- defaults de arranque a `127.0.0.1`;
- nosec justificado para falsos positivos de Bandit en polling loops.

**Límites conocidos:**

- no hay autenticación integrada;
- no hay sandbox fuerte para código no confiable;
- no hay rate limiting de red;
- no hay TLS nativo;
- el runner es para uso local en aula, no para internet abierta.

Ver [SECURITY.md](SECURITY.md) para detalle completo.

---

## Mapa documental

| Documento | Rol |
|---|---|
| [RECRUITER.md](RECRUITER.md) | evidencia técnica rápida para evaluadores |
| [CHANGELOG.md](CHANGELOG.md) | historial de cambios por versión |
| [CONTRIBUTING.md](CONTRIBUTING.md) | cómo contribuir al proyecto |
| [ROADMAP.md](ROADMAP.md) | dirección futura del producto |
| [RUNBOOK.md](RUNBOOK.md) | operación diaria |
| [SECURITY.md](SECURITY.md) | postura de seguridad y límites |
| [docs/INDEX.md](docs/INDEX.md) | índice completo por audiencia y objetivo |
| [docs/CATALOGO_PRODUCTO.md](docs/CATALOGO_PRODUCTO.md) | fuente de verdad de superficies y artefactos |
| [docs/ARQUITECTURA_PRODUCTO.md](docs/ARQUITECTURA_PRODUCTO.md) | arquitectura funcional con diagramas |
| [docs/GUIA_EVALUACION.md](docs/GUIA_EVALUACION.md) | ruta ejecutiva de 10 minutos |
| [docs/BUILD_INSTALLER.md](docs/BUILD_INSTALLER.md) | cómo generar el instalador Windows |
| [docs/MOBILE_APP.md](docs/MOBILE_APP.md) | cómo construir y distribuir la app Android |
| [docs/entorno-interactivo.md](docs/entorno-interactivo.md) | el laboratorio Flask y su funcionamiento |
| [docs/metodologia-docente.md](docs/metodologia-docente.md) | marco pedagógico del producto |
| [docs/instructor-guide.md](docs/instructor-guide.md) | playbook de ejecución docente |
| [docs/student-guide.md](docs/student-guide.md) | guía de onboarding del alumno |
| [docs/despliegue-seguro-y-operacion.md](docs/despliegue-seguro-y-operacion.md) | CI/CD, Docker y hardening |
| [docs/MIGRACION_AWS.md](docs/MIGRACION_AWS.md) | migración a la nube AWS — arquitectura, costos y paso a paso |

> Las notas internas del maintainer viven en `docs/maintainer/`.

---

## Lo que este repo sí es

- una base seria de capacitación técnica en Python y Data Science;
- un sistema que integra contenido, práctica interactiva y presentación;
- una app de escritorio nativa para distribución en aula sin configuración;
- una muestra de criterio pedagógico, operacional y de seguridad;
- una propuesta que puede empezar acotada y crecer sin rehacerse.

## Lo que este repo no vende

- una plataforma multiusuario endurecida para internet abierta;
- una app móvil ya en producción (el código existe pero el APK distribuible se reconstruye con el contenido actual);
- una promesa de personalización infinita antes de cerrar condiciones;
- profundidad total en todas las direcciones desde la primera versión.

---

## Idea fuerza

El valor de este proyecto no depende de competir contra una tecnología puntual. Su valor está en traducir herramientas a aprendizaje real, con secuencia pedagógica, criterio docente, operación responsable y una base documental que permite evaluarlo como producto.
