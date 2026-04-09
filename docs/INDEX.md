# 🧭 Índice de documentación

> Punto de entrada canónico para navegar la documentación del bootcamp por audiencia y objetivo.
>
> Esta documentación tiene tres territorios distintos. Saber en cuál estás evita confusiones.

---

## Territorios de esta documentación

| Territorio | Carpeta / ubicación | Para quién |
|---|---|---|
| Producto del bootcamp | `docs/` (raíz) + archivos raíz (`README`, `RUNBOOK`, `SECURITY`, etc.) | Instituciones, docentes, alumnos, evaluadores técnicos |
| Preparación para entrevista | `docs/entrevista/` | Uso personal del autor en proceso de contratación |
| Notas internas del maintainer | `docs/maintainer/` | Solo el autor, para análisis de portafolio y mejora continua |

---

## Territorio 1: Archivos raíz del producto

Documentos que viven en la raíz del repositorio y forman la capa de entrada principal.

| Archivo | Audiencia | Contenido |
|---|---|---|
| [../README.md](../README.md) | todos | Portada del producto, rutas por perfil, inicio rápido |
| [../RECRUITER.md](../RECRUITER.md) | reclutadores / evaluadores técnicos | Evidencia técnica en 5 minutos, stack, estado real |
| [../CHANGELOG.md](../CHANGELOG.md) | maintainers / contribuidores | Historial de cambios por versión |
| [../CONTRIBUTING.md](../CONTRIBUTING.md) | contribuidores | Cómo contribuir al proyecto |
| [../ROADMAP.md](../ROADMAP.md) | todos | Dirección futura del producto |
| [../RUNBOOK.md](../RUNBOOK.md) | operación | Arranque, smoke checks, incidentes y apagado |
| [../SECURITY.md](../SECURITY.md) | seguridad / todos | Postura de seguridad, riesgos aceptados, hardening |
| [../LICENSE](../LICENSE) | legal | Términos de uso MIT con clarificaciones |

---

## Territorio 1: Documentos del producto en `docs/`

### Lectura recomendada por perfil

| Perfil | Documento de entrada | Qué obtiene |
|---|---|---|
| Institución / evaluador | [GUIA_EVALUACION.md](GUIA_EVALUACION.md) | Valor del producto, evidencias y límites reales |
| Reclutador técnico | [../RECRUITER.md](../RECRUITER.md) | Evidencia rápida sin lectura extensa |
| Stakeholder técnico | [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) | Capas, flujos, fronteras y evolución |
| Producto / fuente de verdad | [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) | Superficies, artefactos y reglas de comunicación |
| Docente / implementación | [herramientas-pedagogicas-de-aula.md](herramientas-pedagogicas-de-aula.md) | Mediación en clase, problemas frecuentes, ritmo |
| Alumno | [student-guide.md](student-guide.md) | Cómo usar los materiales, ruta y expectativas |
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
| [entorno-interactivo.md](entorno-interactivo.md) | El laboratorio Flask — modos, API, motor de ejecución |
| [despliegue-seguro-y-operacion.md](despliegue-seguro-y-operacion.md) | CI/CD, Docker y hardening técnico |
| [portal-estudiante-y-app-movil.md](portal-estudiante-y-app-movil.md) | Portal público, laboratorio y app móvil |
| [pdfs/](pdfs/) | PDFs de entrevista, estudio y guías de clase |
| [presentaciones/](presentaciones/) | Presentaciones `.pptx` listas para exposición |

### Documentos pedagógicos

| Documento | Rol |
|---|---|
| [metodologia-docente.md](metodologia-docente.md) | Marco pedagógico del producto |
| [instructor-guide.md](instructor-guide.md) | Playbook para quien imparte el bootcamp |
| [student-guide.md](student-guide.md) | Guía de onboarding del alumno |
| [plan-evaluacion.md](plan-evaluacion.md) | Criterios de evaluación y retroalimentación |
| [herramientas-pedagogicas-de-aula.md](herramientas-pedagogicas-de-aula.md) | Estrategias de mediación y problemas de aula |
| [aula-ia-y-problemas-frecuentes.md](aula-ia-y-problemas-frecuentes.md) | Uso de IA y manejo de dificultades frecuentes |
| [perfil-estudiantes.md](perfil-estudiantes.md) | Perfil de entrada y consideraciones del grupo |
| [syllabus.md](syllabus.md) | Visión general del programa |
| [cronograma-referencial.md](cronograma-referencial.md) | Distribución temporal de clases |
| [implementacion-v1-skillnest-san-nicolas.md](implementacion-v1-skillnest-san-nicolas.md) | Ruta inicial acotada para contexto escolar |

### Regla de lectura rápida (10 minutos)

1. [../README.md](../README.md)
2. [../RECRUITER.md](../RECRUITER.md)
3. [GUIA_EVALUACION.md](GUIA_EVALUACION.md)
4. [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md)
5. [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md)

---

## Territorio 2: Preparación para entrevista

Documentos de uso personal para el proceso de selección con Skillnest / Colegio San Nicolás de Maipú. No son parte del producto en sí: son instrumentos de preparación, pitch y venta.

> Entrevista: jueves 9 de abril de 2026, 15:30.

| Documento | Rol |
|---|---|
| [entrevista/entrevista-skillnest-preparacion.md](entrevista/entrevista-skillnest-preparacion.md) | Preparación personal: pitch, Q&A, límites sanos |
| [entrevista/preparacion-entrevista-imprimible.md](entrevista/preparacion-entrevista-imprimible.md) | Versión para imprimir o leer antes de entrar |
| [entrevista/desafio-tecnico-preparacion.md](entrevista/desafio-tecnico-preparacion.md) | Dominios técnicos a repasar para el desafío |
| [entrevista/proceso-seleccion-skillnest.md](entrevista/proceso-seleccion-skillnest.md) | Contexto del proceso y sus etapas |
| [entrevista/entrevista-skillnest-presentacion-v2.md](entrevista/entrevista-skillnest-presentacion-v2.md) | Guion de presentación (versión final) |
| [entrevista/entrevista-skillnest-presentacion.md](entrevista/entrevista-skillnest-presentacion.md) | Guion de presentación (versión anterior) |
| [entrevista/muestra-producto-para-skillnest.md](entrevista/muestra-producto-para-skillnest.md) | Muestra escrita del producto para el evaluador |
| [entrevista/preguntas-para-hacer-en-entrevista.md](entrevista/preguntas-para-hacer-en-entrevista.md) | Preguntas clave para aclarar alcance y condiciones |
| [entrevista/guia-estudio-repositorio.md](entrevista/guia-estudio-repositorio.md) | Guía de estudio con comandos, teoría y práctica |
| [entrevista/reunion-pitch.md](entrevista/reunion-pitch.md) | Pitch para la reunión |
| [entrevista/demo-reunion-jueves.md](entrevista/demo-reunion-jueves.md) | Demo específica para la reunión del jueves |
| [entrevista/demo-capacitaciones-escalable.md](entrevista/demo-capacitaciones-escalable.md) | Demo del modelo de capacitaciones escalable |
| [entrevista/valor-diferencial.md](entrevista/valor-diferencial.md) | Diferenciadores para el contexto escolar |
| [entrevista/rubrica-clase-prueba.md](entrevista/rubrica-clase-prueba.md) | Rúbrica para clase de prueba |
| [entrevista/clase-prueba-sugerida.md](entrevista/clase-prueba-sugerida.md) | Clase de prueba sugerida |
| [pdfs/](pdfs/) | PDFs generados para imprimir, estudiar o compartir en reunión |

---

## Territorio 3: Notas internas del maintainer

Documentos de autoevaluación y mejora continua. No forman parte del producto ni de la propuesta al colegio.

| Documento | Rol |
|---|---|
| [maintainer/portfolio-high-standard.md](maintainer/portfolio-high-standard.md) | Análisis transversal del portafolio del autor |
| [maintainer/estandar-alto-gap-bootcamp.md](maintainer/estandar-alto-gap-bootcamp.md) | Brecha entre este repo y el estándar alto personal |
| [maintainer/revision-otros-repos-e-insights.md](maintainer/revision-otros-repos-e-insights.md) | Insights de revisión de otros repositorios |
