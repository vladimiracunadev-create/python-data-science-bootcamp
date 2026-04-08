# Python Data Science Bootcamp

Repositorio completo de un **bootcamp de Python para Data Science** de 12 clases, con entorno interactivo local, materiales pedagógicos detallados, datasets listos para usar y modelos de Machine Learning.

---

## ¿Qué incluye?

### 12 Clases completas

Cada clase incluye: README con objetivos, slides/pauta, ejercicios (3 niveles), tarea, notebook ejecutable, soluciones y **documento teórico completo con tablas y ejemplos** (base para PDF).

| # | Clase | Herramientas |
|---|---|---|
| 01 | Fundamentos de Python aplicados a datos | Python básico |
| 02 | Pandas y limpieza de datos | pandas |
| 03 | Visualización exploratoria | matplotlib |
| 04 | Estadística descriptiva | pandas, statistics |
| 05 | Visualización avanzada con Matplotlib | matplotlib |
| 06 | Texto, fechas y transformaciones | pandas, re |
| 07 | Mini proyecto guiado | Integrador |
| 08 | Presentación de hallazgos | Storytelling |
| 09 | Introducción al Machine Learning | scikit-learn |
| 10 | Modelos supervisados — Clasificación | scikit-learn |
| 11 | Evaluación robusta y Pipelines de ML | scikit-learn |
| 12 | Proyecto final y cierre | Integrador |

### App interactiva local

Entorno tipo Colab/Jupyter integrado con el contenido del bootcamp. Sin necesidad de instalar Jupyter.

- Ejecución de código Python en el navegador
- Auto-guardado de notebooks (30 s de inactividad)
- `Ctrl+Enter` para ejecutar celdas
- Captura de gráficos matplotlib, print y errores
- Indicador visual de ejecución en progreso

### Generador de PDFs

```bash
python scripts/generar_pdfs.py          # genera PDF de todas las clases
python scripts/generar_pdfs.py --clase 09   # solo clase 9
```

PDFs profesionales con portada, tablas formateadas, bloques de código y colores del bootcamp. Guardados en `docs/pdfs/`.

---

## Inicio rápido

### Opción 1: Entorno virtual (recomendado)

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_bootcamp.py
```

Luego abrir [http://localhost:8000](http://localhost:8000)

### Opción 2: Docker

```bash
docker compose up --build
```

### Opción 3: Make

```bash
make install && make run
```

---

## Estructura del repositorio

```
python-data-science-bootcamp/
├── classes/                  ← 12 clases con todos sus materiales
│   ├── 01-python-fundamentos/
│   │   ├── README.md         ← objetivos, duración, resultados esperados
│   │   ├── slides.md         ← pauta de la clase para el docente
│   │   ├── ejercicios.md     ← ejercicios en 3 niveles
│   │   ├── homework.md       ← tarea para casa
│   │   ├── notebook.ipynb    ← notebook ejecutable
│   │   ├── soluciones.ipynb  ← soluciones comentadas
│   │   └── teoria.md         ← documento teórico completo (base PDF)
│   └── ...
├── datasets/
│   ├── README.md             ← diccionario de datos
│   ├── ventas_tienda.csv
│   ├── retencion_clientes.csv
│   ├── soporte_tickets.csv
│   ├── transporte.csv
│   └── estudiantes.csv
├── app/                      ← aplicación Flask interactiva
│   ├── app.py
│   ├── execution_engine.py   ← ejecución con timeout y evicción de sesiones
│   ├── content_loader.py     ← carga de clases y notebooks con validación
│   ├── notebooks/            ← plantillas de notebooks interactivos
│   ├── templates/index.html
│   └── static/               ← CSS y JS del frontend
├── docs/
│   ├── pdfs/                 ← PDFs generados por clase
│   ├── syllabus.md
│   ├── metodologia-docente.md
│   ├── instructor-guide.md
│   └── ...
├── scripts/
│   └── generar_pdfs.py       ← generador de PDFs desde teoria.md
├── src/
│   ├── utils.py
│   └── data_checks.py
├── tests/                    ← suite de tests (cobertura ~70%)
├── mini_project/
├── examples/
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── pyproject.toml
└── requirements.txt
```

---

## Tests

```bash
pytest                          # ejecutar todos los tests
pytest -v                       # con detalle
pytest --cov=app --cov=src      # con cobertura
```

La suite cubre: endpoints de la app, motor de ejecución, utilidades de datos y validaciones.

---

## Seguridad

El entorno de ejecución está diseñado para **uso local y docente**:

- Timeout de 30 segundos por ejecución (evita bucles infinitos)
- Evicción automática de sesiones (máx. 100 sesiones activas, TTL 1 hora)
- Validación de tamaño de payload y longitud de código
- Protección contra path traversal en carga de archivos
- **No exponer a internet sin autenticación adicional**

---

## Metodología pedagógica

- Clases de 90 minutos con estructura: **mostrar → practicar → reflexionar**
- Ejercicios en 3 niveles: guiados, independientes y desafíos opcionales
- Datasets con contexto empresarial chileno (ventas, soporte, transporte)
- Documento teórico completo por clase (con tablas, código y ejemplos)
- Evaluación continua con rúbricas explícitas

Ver `docs/metodologia-docente.md` para el enfoque pedagógico completo.

---

## Materiales de presentacion

- `docs/entrevista-skillnest-presentacion-v2.md`
- `docs/demo-capacitaciones-escalable.md`
- `docs/aula-ia-y-problemas-frecuentes.md`
- `docs/entrevista-skillnest-preparacion.md`
- `docs/implementacion-v1-skillnest-san-nicolas.md`
- `docs/proceso-seleccion-skillnest.md`
- `docs/desafio-tecnico-preparacion.md`
- `docs/herramientas-pedagogicas-de-aula.md`
- `docs/despliegue-seguro-y-operacion.md`
- `docs/portal-estudiante-y-app-movil.md`

---

## Portal del Alumno

- Landing publica en GitHub Pages: `site/`
- Workflow de publicacion: `.github/workflows/deploy-pages.yml`
- URL esperada: `https://vladimiracunadev-create.github.io/python-data-science-bootcamp/`

---

## Licencia

MIT — libre uso educativo y comercial con atribución.
