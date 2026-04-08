# 📐 Estándar alto y brechas del bootcamp

## Contexto

Este documento aterriza el análisis transversal del portafolio a `python-data-science-bootcamp`.

Repos de referencia directa:

- `gabysql`
- `langgraph-realworld`
- `social-bot-scheduler`
- `problem-driven-systems-lab`
- `rootcause-windows-inspector`
- `rootcause-landing`

## Donde este repo ya esta fuerte

- contenido pedagógico real y no solo demo visual;
- curriculum modular con clases, ejercicios, notebooks y datasets;
- laboratorio interactivo que permite practicar dentro del mismo producto;
- material especifico para entrevista, propuesta y clase de prueba;
- portal del alumno separado del entorno de laboratorio.

## Lo que lo alejaba del estandar alto

Antes de esta pasada, las brechas más claras eran:

1. poca capa stakeholder visible fuera de Markdown;
2. GitHub Pages incompleto y amarrado solo a `main`;
3. sin CI de repo visible;
4. sin workflow de seguridad visible;
5. sin `SECURITY.md` ni `RUNBOOK.md` en la raiz;
6. sin health endpoints para operación y smoke checks;
7. despliegue Docker sin perfil más endurecido;
8. README todavia más cercano a inventario que a producto.

## Lo que se elevo en esta pasada

### Producto y presentación

- se reforzo `site/index.html` como portal real del alumno;
- se agrego `site/product/index.html` como presentación institucional del producto;
- se separo con claridad la superficie para alumnos de la superficie para la institución.
- se elevo la capa visual con iconografia, arquitectura visible y matriz funcional en la vista institucional.

### Arquitectura documental

- se agrego `docs/INDEX.md` como mapa de lectura por audiencia;
- se agrego `docs/CATALOGO_PRODUCTO.md` como fuente de verdad del producto;
- se agrego `docs/ARQUITECTURA_PRODUCTO.md` con diagramas y fronteras del sistema;
- se agrego `docs/GUIA_EVALUACION.md` como ruta ejecutiva para evaluadores;
- se rehizo `README.md` con badges, rutas por perfil, arquitectura y mapa documental.

### Operación y seguridad

- se agregaron `/health` y `/ready`;
- se documentaron `SECURITY.md` y `RUNBOOK.md`;
- se agrego `.env.example`;
- se agrego `.dockerignore`;
- se endurecio Docker con `HEALTHCHECK` y compose de perfil más serio;
- se creo `docker-compose.prod.yml`.

### Validación continua

- se agrego `ci.yml` con lint, tests y build de imagen;
- se agrego `security.yml` con `pip-audit` y `bandit`;
- se corrigio Pages para `master` y `main`.

## Comparacion rápida contra el estandar del portafolio

| Pilar | Estado actual | Nota |
|---|---|---|
| Identidad de producto | mejorado | ya no depende solo del README |
| Rutas por audiencia | alto | indice, guía de evaluación y README alineados |
| Visuales con intencion | alto | Pages ahora tiene dos superficies diferenciadas y arquitectura visible |
| Quickstart reproducible | alto | virtualenv, Docker y compose |
| Runbook operativo | alto | existe base clara en raiz |
| Postura de seguridad | alto para demo local | honesta y acotada |
| Defaults seguros | medio/alto | localhost, headers, health checks |
| CI visible | alto | tests, lint y build |
| Security workflow | medio | buena base, aun se puede profundizar |
| Catálogo/taxonomia | alto | existe fuente de verdad explicita del producto |
| Evidencia de validación | medio/alto | tests y endpoints ya visibles |
| Storytelling comercial | medio/alto | ya existe, pero puede refinarse más |

## Lo que todavia falta para rozar Tier A

1. una politica de releases y versionado más visible;
2. más observabilidad si algun dia el runner se expone fuera del equipo local;
3. una experiencia PDF y HTML todavia más integrada entre presentación, producto y operación;
4. una capa de medicion de uso o progreso si el producto evoluciona a cohortes más grandes;
5. una family adicional de docs HTML públicas si la capa institucional necesita vivir fuera del repo.

## Regla de continuidad

La evolución correcta de este repo no es agregar contenido sin fin.

Es consolidar el paquete que ya aparece en tus mejores repos:

- producto claro;
- honestidad de límites;
- operación reproducible;
- seguridad explicita;
- capa visual para quien no va a leer código;
- crecimiento sin rehacer la base.
