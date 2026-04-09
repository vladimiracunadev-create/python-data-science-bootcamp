# Guia de estudio del repositorio

> Documento personal de estudio para preparar entrevista, demo y conversacion tecnica usando solo el contenido existente del repositorio.

## Que debo poder explicar con seguridad

Debo poder resumir estas capas sin improvisar:

- que hace el portal del alumno;
- que hace el laboratorio local;
- que hace la app Android;
- que hace la version Windows;
- que limites tiene hoy la solucion;
- como se aterriza una implementacion escolar acotada.

## Comandos que debo dominar

### Arranque local

- `python run_bootcamp.py`
- `python launcher.py`
- `http://127.0.0.1:8000`

### Validacion tecnica

- `pytest`
- `python -m pytest`
- `ruff check .`

### Docker

- `docker compose up --build`
- `docker compose -f docker-compose.prod.yml up -d --build`

### App Android

- `cd mobile`
- `npm install`
- `npx expo start`
- `npx expo prebuild --platform android`
- `cd android`
- `gradlew.bat assembleDebug`

### Empaque Windows

- `build_windows.bat`
- `python -m PyInstaller bootcamp.spec --noconfirm`

## Rutas que debo conocer

- `README.md`
- `docs/INDEX.md`
- `docs/CATALOGO_PRODUCTO.md`
- `docs/ARQUITECTURA_PRODUCTO.md`
- `docs/GUIA_EVALUACION.md`
- `docs/implementacion-v1-skillnest-san-nicolas.md`
- `classes/`
- `app/`
- `mobile/`
- `site/`
- `installer/`

## Temas por clase que conviene repasar

| Clase | Foco de repaso |
|---|---|
| 00 | diagnostico inicial, fortalezas, vacios y habitos de trabajo |
| 01 | variables, tipos, listas, diccionarios, funciones y control de flujo |
| 02 | lectura de CSV, inspeccion, nulos y limpieza basica |
| 03 | agrupacion, preguntas exploratorias y lectura de graficos |
| 04 | media, mediana, dispersion e interpretacion |
| 05 | construccion y legibilidad de graficos |
| 06 | texto, fechas y columnas derivadas |
| 07 | mini proyecto guiado y secuencia de trabajo |
| 08 | sintesis, hallazgos y comunicacion breve |
| 09 | idea general de machine learning y primer modelo |
| 10 | modelos supervisados y lectura de resultados |
| 11 | evaluacion, metricas y pipelines |
| 12 | integracion del recorrido y cierre |

## Practicas que me conviene ensayar

- escribir una funcion simple y explicarla en voz alta;
- cargar un CSV con pandas y describirlo;
- detectar nulos y justificar una limpieza;
- construir un `groupby` con una conclusion concreta;
- hacer un grafico legible y explicar para que sirve;
- explicar cuando un modelo simple si aporta y cuando no.

## Puntos tecnicos que debo saber defender

- por que el laboratorio local escucha en `127.0.0.1`;
- por que no conviene presentarlo como SaaS abierto;
- que protecciones existen hoy;
- que faltaria para exponerlo a internet;
- que rol cumplen `health` y `ready`;
- por que el runner local no equivale a aislamiento fuerte.

## Explicacion breve que debo ensayar

Este repositorio no es solo contenido. Reune una base docente real con clases, teoria, practica, evaluacion, portal publico, app movil y laboratorio local. La fortaleza esta en la progresion pedagogica y en que la solucion ya puede mostrarse, ejecutarse y adaptarse para una primera implementacion escolar acotada.

## Checklist personal

- abrir y recorrer `README.md`;
- revisar `docs/implementacion-v1-skillnest-san-nicolas.md`;
- repasar `classes/01` a `classes/07`;
- volver a mirar `docs/CATALOGO_PRODUCTO.md`;
- revisar seguridad y despliegue;
- practicar una respuesta pedagogica y una tecnica;
- entrar a la entrevista con preguntas claras sobre alcance y pago.
