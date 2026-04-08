# Python Data Science Bootcamp

Base de capacitacion tecnica para Python y Data Science orientada a clases reales, laboratorios guiados y despliegue progresivo en contexto educativo.

No es solo un repo de materiales. Reune curriculum modular, app interactiva, portal del alumno, documentacion de operacion y una superficie institucional para presentar el producto sin depender solo de Markdown.

## Estado del producto

Este repositorio esta listo para:

- demos locales y entrevistas de producto educativo;
- bootcamps presenciales o guiados por docente;
- publicacion del portal del alumno via GitHub Pages;
- crecimiento posterior hacia una experiencia mas completa, incluyendo app movil.

No esta pensado todavia para exponer el runner a internet abierta sin autenticacion, proxy y hardening adicional.

## Rutas por audiencia

### Alumno

- portal publico: `site/`
- URL esperada: `https://vladimiracunadev-create.github.io/python-data-science-bootcamp/`

### Institucion / stakeholder

- presentacion visual del producto: `site/product/`
- muestra PDF: `docs/pdfs/muestra-producto-para-skillnest.pdf`

### Docente / implementacion

- propuesta inicial: `docs/implementacion-v1-skillnest-san-nicolas.md`
- herramientas de aula: `docs/herramientas-pedagogicas-de-aula.md`
- problemas frecuentes y uso de IA: `docs/aula-ia-y-problemas-frecuentes.md`

### Operacion / repo

- postura de seguridad: `SECURITY.md`
- runbook operativo: `RUNBOOK.md`
- analisis de estandar alto: `docs/portfolio-high-standard.md`
- gap especifico de este repo: `docs/estandar-alto-gap-bootcamp.md`

## Superficies del producto

| Superficie | Rol | Estado |
|---|---|---|
| App Flask (`app/`) | laboratorio interactivo para clases, notebooks y runner | operativa |
| Portal del alumno (`site/`) | enlace oficial y capa publica simple para estudiantes | operativo |
| Vista institucional (`site/product/`) | presentacion del producto para entrevista o evaluacion externa | operativa |
| Material pedagogico (`classes/`, `docs/`) | contenido reusable de clases, metodologia y apoyo | operativo |

## Que incluye hoy

### Curriculum

- 12 clases modulares;
- ejercicios, tareas, notebooks y soluciones;
- datasets sinteticos para practica;
- guias de instructor, metodologia y evaluacion.

### Laboratorio interactivo

- app Flask con visualizacion de clases;
- carga de notebooks base;
- ejecucion de codigo Python en navegador;
- guardado de notebooks de practica;
- endpoints de salud para smoke checks.

### Publicacion y presentacion

- landing publica para estudiantes en GitHub Pages;
- presentacion institucional HTML separada del portal del alumno;
- PDFs listos para preparacion personal y muestra del producto.

## Inicio rapido

### Entorno virtual

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run_bootcamp.py
```

Abrir `http://127.0.0.1:8000`.

### Docker local

```bash
docker compose up --build
```

### Perfil mas endurecido

```bash
docker compose -f docker-compose.prod.yml up -d --build
```

## Validacion

```bash
pytest
pip install ruff
ruff check .
```

Endpoints utiles:

- `GET /health`
- `GET /ready`
- `GET /api/classes`

## CI/CD visible

Este repo ya deja visible una base de validacion continua:

- `.github/workflows/ci.yml`
- `.github/workflows/security.yml`
- `.github/workflows/deploy-pages.yml`

Eso cubre:

- lint;
- tests;
- build de contenedor;
- auditoria basica de dependencias;
- escaneo estatico de seguridad;
- despliegue del portal del alumno a GitHub Pages.

## Seguridad y limites

Protecciones actuales:

- validacion de entradas;
- limites de payload y longitud de codigo;
- timeout por ejecucion;
- eviction de sesiones antiguas;
- headers HTTP de seguridad;
- defaults locales por `127.0.0.1`.

Limites actuales:

- no hay autenticacion integrada;
- no hay sandbox fuerte para codigo no confiable;
- no hay rate limiting de red;
- no hay TLS nativo.

Ver detalle en `SECURITY.md`.

## Estructura principal

```text
app/                  aplicacion Flask y runner
classes/              clases del bootcamp
datasets/             datos de practica
docs/                 metodologia, propuesta, entrevista y PDFs
site/                 portal del alumno + vista institucional
tests/                suite automatizada
SECURITY.md           postura actual y riesgos aceptados
RUNBOOK.md            operacion diaria y smoke checks
```

## Idea fuerza

El valor de este proyecto no depende de competir contra una tecnologia puntual. Su valor esta en traducir herramientas a aprendizaje real, con secuencia pedagogica, criterio docente y una base que puede crecer sin rehacerse desde cero.
