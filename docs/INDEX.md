# 🧭 Índice de documentación

> Punto de entrada canónico para navegar la documentación del bootcamp por audiencia y objetivo.
>
> Esta documentación tiene tres territorios distintos. Saber en cuál estás evita confusiones.

---

## 🗂️ Territorios de esta documentación

| Territorio | Carpeta / ubicación | Para quién |
|---|---|---|
| 📦 Producto del bootcamp | `docs/` (raíz) + archivos raíz (`README`, `RUNBOOK`, `SECURITY`, etc.) | Docentes, alumnos, evaluadores técnicos, cualquier persona interesada |
| 🗂️ Proceso de selección (histórico) | `docs/entrevista/` | Archivo personal del autor — contexto del proceso con Skillnest |
| 🔧 Notas internas del maintainer | `docs/maintainer/` | Solo el autor, para análisis de portafolio y mejora continua |

---

## 📦 Territorio 1: Archivos raíz del producto

| Archivo | Audiencia | Contenido |
|---|---|---|
| [../README.md](../README.md) | todos | Portada del producto, estado actual, rutas por perfil, inicio rápido |
| [../RECRUITER.md](../RECRUITER.md) | reclutadores / evaluadores técnicos | Evidencia técnica en 5 minutos, stack, estado real |
| [../CHANGELOG.md](../CHANGELOG.md) | maintainers / contribuidores | Historial de cambios por versión |
| [../CONTRIBUTING.md](../CONTRIBUTING.md) | contribuidores | Cómo contribuir al proyecto |
| [../ROADMAP.md](../ROADMAP.md) | todos | Dirección futura del producto |
| [../RUNBOOK.md](../RUNBOOK.md) | operación | Arranque, smoke checks, incidentes y apagado |
| [../SECURITY.md](../SECURITY.md) | seguridad / todos | Postura de seguridad, riesgos aceptados, hardening |
| [../LICENSE](../LICENSE) | legal | Términos de uso MIT |

---

## 📂 Territorio 1: Documentos del producto en `docs/`

### 🔎 Lectura recomendada por perfil

| Perfil | Documento de entrada | Qué obtiene |
|---|---|---|
| 🎓 Alumno | [student-guide.md](student-guide.md) | Cómo usar los materiales, ruta y expectativas |
| 👩‍🏫 Docente | [instructor-guide.md](instructor-guide.md) | Playbook para impartir el bootcamp |
| 🏫 Institución / evaluador | [GUIA_EVALUACION.md](GUIA_EVALUACION.md) | Valor del producto, evidencias y límites reales |
| 💼 Reclutador técnico | [../RECRUITER.md](../RECRUITER.md) | Evidencia rápida sin lectura extensa |
| 🏗️ Stakeholder técnico | [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) | Capas, flujos, fronteras y evolución |
| 📦 Producto / fuente de verdad | [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) | Superficies, artefactos y reglas de comunicación |
| ⚙️ Operación | [../RUNBOOK.md](../RUNBOOK.md) | Arranque, smoke checks, verificación y apagado |
| 🔒 Seguridad | [../SECURITY.md](../SECURITY.md) | Postura actual, riesgos aceptados y hardening |

### 🗺️ Mapa documental técnico

| Documento | Rol |
|---|---|
| [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) | Fuente de verdad para superficies y artefactos |
| [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) | Arquitectura funcional con diagramas Mermaid |
| [GUIA_EVALUACION.md](GUIA_EVALUACION.md) | Ruta ejecutiva de 10 minutos |
| [BUILD_INSTALLER.md](BUILD_INSTALLER.md) | Cómo generar el instalador .exe para Windows |
| [MOBILE_APP.md](MOBILE_APP.md) | Cómo construir y distribuir la app Android |
| [entorno-interactivo.md](entorno-interactivo.md) | El laboratorio Flask — modos, API, motor de ejecución |
| [despliegue-seguro-y-operacion.md](despliegue-seguro-y-operacion.md) | CI/CD, Docker y hardening técnico |
| [portal-estudiante-y-app-movil.md](portal-estudiante-y-app-movil.md) | Portal público, laboratorio y app móvil |
| [pdfs/](pdfs/) | 31 guías explicativas por clase + PDFs de estudio |
| [presentaciones/](presentaciones/) | 31 presentaciones `.pptx` listas para exposición |

### 📖 Documentos pedagógicos

| Documento | Rol |
|---|---|
| [syllabus.md](syllabus.md) | Currículo completo: 31 clases, 13 módulos, perfil de salida |
| [cronograma-referencial.md](cronograma-referencial.md) | Distribución temporal: modalidades intensiva, estándar y parte-tiempo |
| [metodologia-docente.md](metodologia-docente.md) | Marco pedagógico del producto |
| [instructor-guide.md](instructor-guide.md) | Playbook para quien imparte el bootcamp |
| [student-guide.md](student-guide.md) | Guía de onboarding del alumno |
| [plan-evaluacion.md](plan-evaluacion.md) | Criterios de evaluación y retroalimentación |
| [herramientas-pedagogicas-de-aula.md](herramientas-pedagogicas-de-aula.md) | Estrategias de mediación y problemas de aula |
| [aula-ia-y-problemas-frecuentes.md](aula-ia-y-problemas-frecuentes.md) | Uso de IA y manejo de dificultades frecuentes |
| [perfil-estudiantes.md](perfil-estudiantes.md) | Perfil de entrada y consideraciones del grupo |

### ⚡ Regla de lectura rápida (10 minutos)

1. [../README.md](../README.md)
2. [../RECRUITER.md](../RECRUITER.md)
3. [GUIA_EVALUACION.md](GUIA_EVALUACION.md)
4. [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md)
5. [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md)

---

## 🗂️ Territorio 2: Proceso de selección (histórico)

Documentos generados durante el proceso de selección con Skillnest. Se conservan como referencia histórica y como evidencia del proceso pedagógico. **El producto ya superó esa etapa** — ahora se desarrolla como recurso personal de aprendizaje y enseñanza, abierto a cualquier persona.

| Documento | Rol |
|---|---|
| [entrevista/muestra-producto-para-skillnest.md](entrevista/muestra-producto-para-skillnest.md) | Muestra del producto y enfoque docente |
| [entrevista/preguntas-para-hacer-en-entrevista.md](entrevista/preguntas-para-hacer-en-entrevista.md) | Preguntas para aclarar alcance, condiciones y riesgos |
| [entrevista/guia-estudio-repositorio.md](entrevista/guia-estudio-repositorio.md) | Guía maestra para estudiar el repositorio a profundidad |
| [entrevista/guia-total-python-data-science.md](entrevista/guia-total-python-data-science.md) | Mapa completo de Python con Data Science apoyado en fuentes oficiales |
| [entrevista/entrevista-skillnest-preparacion.md](entrevista/entrevista-skillnest-preparacion.md) | Notas personales de pitch, Q&A y límites |
| [entrevista/desafio-tecnico-preparacion.md](entrevista/desafio-tecnico-preparacion.md) | Notas de estudio para desafío técnico |
| [pdfs/](pdfs/) | PDFs generados como artefactos del proceso |

---

## 🔧 Territorio 3: Notas internas del maintainer

Documentos de autoevaluación y mejora continua. No forman parte del producto público.

| Documento | Rol |
|---|---|
| [maintainer/portfolio-high-standard.md](maintainer/portfolio-high-standard.md) | Análisis transversal del portafolio del autor |
| [maintainer/estandar-alto-gap-bootcamp.md](maintainer/estandar-alto-gap-bootcamp.md) | Brecha entre este repo y el estándar alto personal |
| [maintainer/revision-otros-repos-e-insights.md](maintainer/revision-otros-repos-e-insights.md) | Insights de revisión de otros repositorios |
