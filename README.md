# Python Data Science Bootcamp Demo

Repositorio demostrativo orientado a la enseñanza de **Python para Data Science**, preparado como muestra de trabajo docente y de diseño de bootcamp.
Incluye planificación pedagógica, clases modelo, notebooks prácticos, ejercicios, evaluación, datasets y un **entorno interactivo local en Python** para practicar desde el mismo proyecto.

## Propósito

Este repositorio busca demostrar una forma de enseñar Python para análisis de datos que sea:

- clara para estudiantes principiantes o en transición;
- práctica y orientada a problemas reales;
- simple de ejecutar en un entorno local;
- flexible para adaptarse a distintos ritmos de aprendizaje;
- reutilizable como base para un bootcamp presencial o híbrido.

## Qué contiene

- **docs/**: syllabus, metodología, evaluación, perfil de estudiantes, guía docente y guía de estudiantes.
- **classes/**: clases estructuradas con objetivos, pauta, notebook, ejercicios y tarea.
- **datasets/**: datos de ejemplo simples y explicables en sala.
- **examples/**: notebook y scripts de demostración rápida.
- **mini_project/**: desafío integrador con rúbrica.
- **src/**: utilidades auxiliares para validar datos y apoyar actividades.
- **app/**: entorno interactivo con vista de clases, cuaderno por celdas y runner de código.
- **tests/**: pruebas simples para verificar que el entorno y los materiales funcionen.

## Ruta recomendada para una revisión rápida

1. Leer `docs/syllabus.md`
2. Revisar `docs/metodologia-docente.md`
3. Abrir `classes/01-python-fundamentos/notebook.ipynb`
4. Revisar `classes/02-pandas-limpieza-datos/notebook.ipynb`
5. Abrir `docs/entorno-interactivo.md`
6. Ejecutar `python -m app.app`

## Público objetivo

Pensado para personas que:

- están dando sus primeros pasos en Python;
- necesitan conectar programación con análisis de datos;
- requieren acompañamiento guiado y ejercicios progresivos;
- aprenden mejor a partir de ejemplos concretos.

## Resultados de aprendizaje esperados

Al completar el recorrido base de este repositorio, la persona podrá:

- comprender fundamentos de Python aplicados a datos;
- cargar y explorar archivos CSV con pandas;
- limpiar y transformar datos básicos;
- generar visualizaciones sencillas e interpretar hallazgos;
- resolver un mini proyecto con preguntas guiadas;
- practicar dentro de un cuaderno local por celdas con salida integrada.

## Instalación rápida

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.app
# o bien
python run_bootcamp.py
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m app.app
# o bien
python run_bootcamp.py
```

Luego abre `http://127.0.0.1:8000`.

## Ruta alternativa con Jupyter

```bash
jupyter notebook
```

## Docker opcional

```bash
docker compose up --build
```

## Comandos útiles

```bash
python examples/run_demo.py
python examples/validate_bootcamp.py
pytest
```

Si usas `make`:

```bash
make setup
make app
make demo
make validate
make test
make notebook
```

## Filosofía del material

Este repositorio no busca impresionar por complejidad técnica, sino por su capacidad de:

- ordenar contenidos de forma pedagógica;
- convertir conceptos técnicos en práctica comprensible;
- dejar evidencia concreta de preparación de clases;
- facilitar adaptación por nivel;
- permitir que el mismo curso tenga un entorno donde probar ejercicios y explicar en vivo.

## Sugerencia de uso en entrevista o reunión

Este repo puede mostrarse como una base ya preparada para un bootcamp.
La forma más efectiva de presentarlo es destacar que no solo contiene código, sino también:

- estructura de clases,
- criterios de evaluación,
- notebooks reutilizables,
- guía docente,
- entorno interactivo de práctica,
- posibilidad de ejecución simple local y Docker opcional.

## Autor

**Vladimir Acuña**
Arquitecto de Software / Full-Stack Senior / Relator Técnico
Santiago, Chile
