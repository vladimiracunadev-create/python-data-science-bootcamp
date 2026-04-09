# 🧱 Catálogo del producto

Documento fuente de verdad para distinguir:

- que es una superficie real del producto;
- que es un artefacto de apoyo;
- que es una ruta documental;
- y que partes siguen siendo evolución futura.

## 🧭 1. Definiciones

### Superficie

Forma concreta en que una audiencia interactua con el producto.

### Artefacto

Archivo o salida reusable que apoya la evaluación, la presentación o la operación.

### Ruta documental

Documento canónico que ordena, explica o limita el producto.

### Evolución

Capacidad proyectada, pero no operativa hoy como pieza principal del sistema.

## 🧱 2. Matriz canónica de superficies

| Superficie | Tipo | Estado | Audiencia | Qué entrega hoy |
|---|---|---|---|---|
| Laboratorio interactivo (`app/`) | núcleo operativo | operativo | docente / estudiante guiado | visualización de clases, carga de notebooks, runner y guardado local |
| App de escritorio Windows (`launcher.py` + `installer/`) | distribución de escritorio | listo para build | alumno / docente en aula | app nativa con ventana propia (pywebview + Edge WebView2), sin navegador, sin Python, sin configuración |
| App Android (`mobile/`) | distribucion móvil | listo para build | alumno en movimiento | lectura de contenido, código documentado, apertura directa en Google Colab |
| Portal del alumno (`site/`) | superficie pública | operativo | alumno | enlace oficial, ruta, recursos, reglas de uso de tecnología |
| Vista institucional (`site/product/`) | superficie pública | operativo | institución / evaluador | narrativa de producto, alcance, arquitectura, operación y crecimiento |
| Curriculum modular (`classes/`) | base pedagógica | operativo | docente | clase 0 diagnóstica + 12 clases troncales con notebooks profusamente documentados, ejercicios, tareas y soluciones |
| Kit documental (`docs/`) | capa editorial | operativo | docente / stakeholder / repo | metodología, implementación, evaluación, seguridad y entrevista |
| PDFs (`docs/pdfs/`) | artefacto de apoyo | operativo | entrevista / presentación | piezas imprimibles y de muestra |

## ⚙ 3. Funcionalidad real por superficie

| Capacidad | Laboratorio Flask | Instalador Windows | App Android | Portal alumno | Vista institucional |
|---|---|---|---|---|---|
| Ver contenido de las clases | si | si (embebido) | si (embebido) | no | no |
| Ejecutar código Python | si (runner local) | si (runner local) | via Google Colab | no | no |
| Leer código documentado | si | si | si | no | no |
| Descargar / abrir en Colab | no | no | si | no | no |
| Guardar notebooks | si | si | no | no | no |
| Seguimiento de progreso | no | no | si (local) | no | no |
| Mostrar producto a terceros | parcial | no | no | parcial | si |
| Operar sin internet | si | si | si (contenido) | no | no |
| Instalar sin Python | no | si | si | no | no |

## 📦 4. Artefactos oficiales de apoyo

| Artefacto | Rol | Estado |
|---|---|---|
| `docs/pdfs/preparacion-entrevista-imprimible.pdf` | apoyo personal para reunión y proceso | vigente |
| `docs/pdfs/muestra-producto-para-skillnest.pdf` | muestra imprimible del producto | vigente |
| `docs/pdfs/entrevista-skillnest-presentacion-v2.pdf` | presentación breve | vigente |
| `scripts/generar_pdf_documento.py` | generacion reproducible de PDFs | vigente |

## 🗣 5. Reglas de comunicación

### Lo que si se puede afirmar

- el repo ya contiene una base de capacitación real y no solo una landing;
- el laboratorio interactivo es operativo como herramienta local de aula;
- existe una superficie pública para alumnos y otra para institución;
- la propuesta puede partir acotada y crecer sin rehacer la base.

### Lo que no se debe mezclar

- el portal del alumno no es todo el producto;
- la vista institucional no reemplaza el laboratorio;
- los PDFs no son el producto, son artefactos de apoyo;
- la app Android no ejecuta Python de forma nativa: usa Google Colab para la ejecución;
- el instalador Windows es una app de escritorio real con ventana nativa (no abre el navegador); el backend Flask corre internamente de forma transparente para el usuario;
- el runner local no debe presentarse como SaaS expuesto a internet.

## 🏫 6. Versión inicial recomendada para colegio

La primera implementación no necesita usar todo el catálogo.

La V1 recomendable es:

1. fundamentos de Python;
2. lectura de CSV con pandas;
3. filtros y tablas resumen;
4. visualización básica;
5. mini proyecto guiado;
6. presentación breve de hallazgos.

## 📌 7. Regla de prioridad

Si alguna presentación, README o landing contradice esta matriz, este documento tiene prioridad.
