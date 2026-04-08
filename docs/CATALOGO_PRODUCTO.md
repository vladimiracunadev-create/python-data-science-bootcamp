# 🧱 Catalogo del producto

Documento fuente de verdad para distinguir:

- que es una superficie real del producto;
- que es un artefacto de apoyo;
- que es una ruta documental;
- y que partes siguen siendo evolucion futura.

## 🧭 1. Definiciones

### Superficie

Forma concreta en que una audiencia interactua con el producto.

### Artefacto

Archivo o salida reusable que apoya la evaluacion, la presentacion o la operacion.

### Ruta documental

Documento canonico que ordena, explica o limita el producto.

### Evolucion

Capacidad proyectada, pero no operativa hoy como pieza principal del sistema.

## 🧱 2. Matriz canonica de superficies

| Superficie | Tipo | Estado | Audiencia | Que entrega hoy |
|---|---|---|---|---|
| Laboratorio interactivo (`app/`) | nucleo operativo | operativo | docente / estudiante guiado | visualizacion de clases, carga de notebooks, runner y guardado local |
| Portal del alumno (`site/`) | superficie publica | operativo | alumno | enlace oficial, ruta, recursos, reglas de uso de tecnologia |
| Vista institucional (`site/product/`) | superficie publica | operativo | institucion / evaluador | narrativa de producto, alcance, arquitectura, operacion y crecimiento |
| Curriculum modular (`classes/`) | base pedagogica | operativo | docente | clases, ejercicios, notebooks, tareas y soluciones |
| Kit documental (`docs/`) | capa editorial | operativo | docente / stakeholder / repo | metodologia, implementacion, evaluacion, seguridad y entrevista |
| PDFs (`docs/pdfs/`) | artefacto de apoyo | operativo | entrevista / presentacion | piezas imprimibles y de muestra |
| Ruta movil | evolucion | planificada | alumno | seguimiento, avisos y progreso individual |

## ⚙ 3. Funcionalidad real por superficie

| Capacidad | Laboratorio | Portal alumno | Vista institucional | Curriculum | Ruta movil |
|---|---|---|---|---|---|
| Ver ruta del bootcamp | parcial | si | si | si | futura |
| Ejecutar codigo | si | no | no | no | futura |
| Cargar notebooks base | si | no | no | parcial | futura |
| Mostrar producto a terceros | parcial | parcial | si | no | no |
| Presentar arquitectura | no | no | si | no | no |
| Operar en entorno local | si | no | no | no | futura |
| Funcionar como base reutilizable | si | si | si | si | futura |

## 📦 4. Artefactos oficiales de apoyo

| Artefacto | Rol | Estado |
|---|---|---|
| `docs/pdfs/preparacion-entrevista-imprimible.pdf` | apoyo personal para reunion y proceso | vigente |
| `docs/pdfs/muestra-producto-para-skillnest.pdf` | muestra imprimible del producto | vigente |
| `docs/pdfs/entrevista-skillnest-presentacion-v2.pdf` | presentacion breve | vigente |
| `scripts/generar_pdf_documento.py` | generacion reproducible de PDFs | vigente |

## 🗣 5. Reglas de comunicacion

### Lo que si se puede afirmar

- el repo ya contiene una base de capacitacion real y no solo una landing;
- el laboratorio interactivo es operativo como herramienta local de aula;
- existe una superficie publica para alumnos y otra para institucion;
- la propuesta puede partir acotada y crecer sin rehacer la base.

### Lo que no se debe mezclar

- el portal del alumno no es todo el producto;
- la vista institucional no reemplaza el laboratorio;
- los PDFs no son el producto, son artefactos de apoyo;
- la ruta movil no debe venderse como funcionalidad actual;
- el runner local no debe presentarse como SaaS expuesto a internet.

## 🏫 6. Version inicial recomendada para colegio

La primera implementacion no necesita usar todo el catalogo.

La V1 recomendable es:

1. fundamentos de Python;
2. lectura de CSV con pandas;
3. filtros y tablas resumen;
4. visualizacion basica;
5. mini proyecto guiado;
6. presentacion breve de hallazgos.

## 📌 7. Regla de prioridad

Si alguna presentacion, README o landing contradice esta matriz, este documento tiene prioridad.
