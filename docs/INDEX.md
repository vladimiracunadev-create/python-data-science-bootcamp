# Índice de documentación

> Punto de entrada canónico para navegar la documentación del bootcamp por audiencia y objetivo.
>
> **Estado v2:** el currículo creció a 197 clases en 9 partes. Este repositorio nació como muestra de habilidades técnicas y pedagógicas, y hoy se desarrolla como recurso personal de aprendizaje y enseñanza, abierto a cualquier persona.

---

## Territorios de esta documentación

| Territorio | Carpeta / ubicación | Para quién |
|---|---|---|
| Producto del bootcamp | `docs/` (raíz) + archivos raíz (`README`, `RUNBOOK`, `SECURITY`, etc.) | Docentes, alumnos, evaluadores técnicos |
| Currículo vigente (v2) | `classes/` | Alumnos y docentes |
| Currículo histórico (v1) | `historicos/classes-v1/` | Desarrolladores de contenido (fuente de material reutilizable) |
| Notas internas del maintainer | `docs/maintainer/` | Solo el autor |

---

## Archivos raíz del producto

| Archivo | Audiencia | Contenido |
|---|---|---|
| [../README.md](../README.md) | todos | Portada del producto, estado actual v2, rutas por perfil |
| [../RECRUITER.md](../RECRUITER.md) | reclutadores / evaluadores técnicos | Evidencia técnica en 5 minutos, stack, estado real |
| [../CHANGELOG.md](../CHANGELOG.md) | maintainers / contribuidores | Historial de cambios por versión |
| [../CONTRIBUTING.md](../CONTRIBUTING.md) | contribuidores | Cómo contribuir al proyecto |
| [../ROADMAP.md](../ROADMAP.md) | todos | Dirección futura del producto |
| [../RUNBOOK.md](../RUNBOOK.md) | operación | Arranque, smoke checks, incidentes y apagado |
| [../SECURITY.md](../SECURITY.md) | seguridad / todos | Postura de seguridad, riesgos aceptados, hardening |
| [../LICENSE](../LICENSE) | legal | Términos de uso MIT |

---

## Documentos del producto en `docs/`

### Lectura recomendada por perfil

| Perfil | Documento de entrada | Qué obtiene |
|---|---|---|
| Alumno | [student-guide.md](student-guide.md) | Cómo usar los materiales, ruta y expectativas |
| Docente | [instructor-guide.md](instructor-guide.md) | Playbook para impartir el bootcamp |
| Institución / evaluador | [GUIA_EVALUACION.md](GUIA_EVALUACION.md) | Valor del producto, evidencias y límites reales |
| Reclutador técnico | [../RECRUITER.md](../RECRUITER.md) | Evidencia rápida sin lectura extensa |
| Stakeholder técnico | [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) | Capas, flujos, fronteras y evolución |
| Producto / fuente de verdad | [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) | Superficies, artefactos y reglas de comunicación |
| Operación | [../RUNBOOK.md](../RUNBOOK.md) | Arranque, smoke checks, verificación y apagado |
| Seguridad | [../SECURITY.md](../SECURITY.md) | Postura actual, riesgos aceptados y hardening |

### Mapa documental técnico

| Documento | Rol |
|---|---|
| [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) | Fuente de verdad para superficies y artefactos |
| [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) | Arquitectura funcional con diagramas Mermaid |
| [GUIA_EVALUACION.md](GUIA_EVALUACION.md) | Ruta ejecutiva de 10 minutos |
| [BUILD_INSTALLER.md](BUILD_INSTALLER.md) | Cómo generar el instalador .exe para Windows |
| [MOBILE_APP.md](MOBILE_APP.md) | Cómo construir y distribuir la app Android |
| [MIGRACION_AWS.md](MIGRACION_AWS.md) | Plan de migración a cloud (AWS) |
| [entorno-interactivo.md](entorno-interactivo.md) | El laboratorio Flask — modos, API, motor de ejecución |
| [despliegue-seguro-y-operacion.md](despliegue-seguro-y-operacion.md) | CI/CD, Docker y hardening técnico |
| [portal-estudiante-y-app-movil.md](portal-estudiante-y-app-movil.md) | Portal público, laboratorio y app móvil |
| [pdfs/](pdfs/) | Guías explicativas (v1 vigente; v2 se regenera por bloques) |
| [presentaciones/](presentaciones/) | Decks `.pptx` (mismo estado) |

### Documentos pedagógicos

| Documento | Rol |
|---|---|
| [syllabus.md](syllabus.md) | **Currículo v2 completo: 197 clases en 9 partes, pauta avanzada** |
| [../classes/README.md](../classes/README.md) | Índice navegable de las 197 clases con enlaces directos |
| [cronograma-referencial.md](cronograma-referencial.md) | Distribución temporal sugerida |
| [metodologia-docente.md](metodologia-docente.md) | Marco pedagógico del producto |
| [instructor-guide.md](instructor-guide.md) | Playbook para quien imparte el bootcamp |
| [student-guide.md](student-guide.md) | Guía de onboarding del alumno |
| [plan-evaluacion.md](plan-evaluacion.md) | Criterios de evaluación y retroalimentación |
| [herramientas-pedagogicas-de-aula.md](herramientas-pedagogicas-de-aula.md) | Estrategias de mediación y problemas de aula |
| [aula-ia-y-problemas-frecuentes.md](aula-ia-y-problemas-frecuentes.md) | Uso de IA y manejo de dificultades frecuentes |
| [perfil-estudiantes.md](perfil-estudiantes.md) | Perfil de entrada y consideraciones del grupo |

### Regla de lectura rápida (10 minutos)

1. [../README.md](../README.md) — estado v2 y rutas por perfil
2. [../RECRUITER.md](../RECRUITER.md) — evidencia técnica
3. [GUIA_EVALUACION.md](GUIA_EVALUACION.md) — valor y límites
4. [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) — superficies y artefactos
5. [syllabus.md](syllabus.md) — pauta completa de 197 clases

---

## Histórico (`historicos/`)

Material del currículo v1 archivado como referencia y fuente de material reutilizable. **No es la fuente de verdad del producto vigente** — el producto hoy se desarrolla como recurso personal de aprendizaje y mejora del propio producto.

| Carpeta / archivo | Rol |
|---|---|
| [../historicos/classes-v1/](../historicos/classes-v1) | 31 clases del currículo v1 con contenido completo (teoría, ejercicios, soluciones, PDF, PPTX) |
| [../historicos/README.md](../historicos/README.md) | Explicación del archivo |

---

## Notas internas del maintainer

Documentos de autoevaluación y mejora continua. No forman parte del producto público.

| Documento | Rol |
|---|---|
| [maintainer/portfolio-high-standard.md](maintainer/portfolio-high-standard.md) | Análisis transversal del portafolio del autor |
| [maintainer/estandar-alto-gap-bootcamp.md](maintainer/estandar-alto-gap-bootcamp.md) | Brecha entre este repo y el estándar alto personal |
| [maintainer/revision-otros-repos-e-insights.md](maintainer/revision-otros-repos-e-insights.md) | Insights de revisión de otros repositorios |
