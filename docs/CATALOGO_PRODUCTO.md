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
| Instalador Windows (`launcher.py` + `installer/`) | distribucion de escritorio | listo para build | alumno / docente en aula | empaqueta el laboratorio como .exe instalable, sin Python ni configuracion |
| App Android (`mobile/`) | distribucion movil | listo para build | alumno en movimiento | lectura de contenido, codigo documentado, apertura directa en Google Colab |
| Portal del alumno (`site/`) | superficie publica | operativo | alumno | enlace oficial, ruta, recursos, reglas de uso de tecnologia |
| Vista institucional (`site/product/`) | superficie publica | operativo | institucion / evaluador | narrativa de producto, alcance, arquitectura, operacion y crecimiento |
| Curriculum modular (`classes/`) | base pedagogica | operativo | docente | 12 clases con notebooks profusamente documentados, ejercicios, tareas y soluciones |
| Kit documental (`docs/`) | capa editorial | operativo | docente / stakeholder / repo | metodologia, implementacion, evaluacion, seguridad y entrevista |
| PDFs (`docs/pdfs/`) | artefacto de apoyo | operativo | entrevista / presentacion | piezas imprimibles y de muestra |

## ⚙ 3. Funcionalidad real por superficie

| Capacidad | Laboratorio Flask | Instalador Windows | App Android | Portal alumno | Vista institucional |
|---|---|---|---|---|---|
| Ver contenido de las clases | si | si (embebido) | si (embebido) | no | no |
| Ejecutar codigo Python | si (runner local) | si (runner local) | via Google Colab | no | no |
| Leer codigo documentado | si | si | si | no | no |
| Descargar / abrir en Colab | no | no | si | no | no |
| Guardar notebooks | si | si | no | no | no |
| Seguimiento de progreso | no | no | si (local) | no | no |
| Mostrar producto a terceros | parcial | no | no | parcial | si |
| Operar sin internet | si | si | si (contenido) | no | no |
| Instalar sin Python | no | si | si | no | no |

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
- la app Android no ejecuta Python de forma nativa: usa Google Colab para la ejecucion;
- el instalador Windows no es una app de escritorio nueva: es el mismo laboratorio Flask empaquetado;
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
