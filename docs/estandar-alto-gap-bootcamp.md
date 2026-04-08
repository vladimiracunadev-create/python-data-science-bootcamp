# Estandar alto y brechas del bootcamp

## Contexto

Este documento aterriza el analisis transversal del portafolio a `python-data-science-bootcamp`.

Repos de referencia directa:

- `gabysql`
- `langgraph-realworld`
- `social-bot-scheduler`
- `problem-driven-systems-lab`
- `rootcause-windows-inspector`
- `rootcause-landing`

## Donde este repo ya esta fuerte

- contenido pedagogico real y no solo demo visual;
- curriculum modular con clases, ejercicios, notebooks y datasets;
- laboratorio interactivo que permite practicar dentro del mismo producto;
- material especifico para entrevista, propuesta y clase de prueba;
- portal del alumno separado del entorno de laboratorio.

## Lo que lo alejaba del estandar alto

Antes de esta pasada, las brechas mas claras eran:

1. poca capa stakeholder visible fuera de Markdown;
2. GitHub Pages incompleto y amarrado solo a `main`;
3. sin CI de repo visible;
4. sin workflow de seguridad visible;
5. sin `SECURITY.md` ni `RUNBOOK.md` en la raiz;
6. sin health endpoints para operacion y smoke checks;
7. despliegue Docker sin perfil mas endurecido;
8. README todavia mas cercano a inventario que a producto.

## Lo que se elevo en esta pasada

### Producto y presentacion

- se reforzo `site/index.html` como portal real del alumno;
- se agrego `site/product/index.html` como presentacion institucional del producto;
- se separo con claridad la superficie para alumnos de la superficie para la institucion.

### Operacion y seguridad

- se agregaron `/health` y `/ready`;
- se documentaron `SECURITY.md` y `RUNBOOK.md`;
- se agrego `.env.example`;
- se agrego `.dockerignore`;
- se endurecio Docker con `HEALTHCHECK` y compose de perfil mas serio;
- se creo `docker-compose.prod.yml`.

### Validacion continua

- se agrego `ci.yml` con lint, tests y build de imagen;
- se agrego `security.yml` con `pip-audit` y `bandit`;
- se corrigio Pages para `master` y `main`.

## Comparacion rapida contra el estandar del portafolio

| Pilar | Estado actual | Nota |
|---|---|---|
| Identidad de producto | mejorado | ya no depende solo del README |
| Rutas por audiencia | medio/alto | alumno, institucion, operador, entrevistador |
| Visuales con intencion | mejorado | Pages ahora tiene dos superficies diferenciadas |
| Quickstart reproducible | alto | virtualenv, Docker y compose |
| Runbook operativo | alto | existe base clara en raiz |
| Postura de seguridad | alto para demo local | honesta y acotada |
| Defaults seguros | medio/alto | localhost, headers, health checks |
| CI visible | alto | tests, lint y build |
| Security workflow | medio | buena base, aun se puede profundizar |
| Catalogo/taxonomia | medio | todavia puede unificarse mas |
| Evidencia de validacion | medio/alto | tests y endpoints ya visibles |
| Storytelling comercial | medio/alto | ya existe, pero puede refinarse mas |

## Lo que todavia falta para rozar Tier A

1. una taxonomia canonica que separe con mas claridad demo, portal alumno, laboratorio y futuro movil;
2. una politica de releases y versionado mas visible;
3. mas observabilidad si algun dia el runner se expone fuera del equipo local;
4. una experiencia PDF y HTML todavia mas integrada entre presentacion, producto y operacion;
5. una capa de medicion de uso o progreso si el producto evoluciona a cohortes mas grandes.

## Regla de continuidad

La evolucion correcta de este repo no es agregar contenido sin fin.

Es consolidar el paquete que ya aparece en tus mejores repos:

- producto claro;
- honestidad de limites;
- operacion reproducible;
- seguridad explicita;
- capa visual para quien no va a leer codigo;
- crecimiento sin rehacer la base.
