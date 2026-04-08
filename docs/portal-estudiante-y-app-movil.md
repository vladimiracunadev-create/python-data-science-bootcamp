# Portal del alumno y ruta hacia app movil

## Objetivo

Agregar una superficie publica, clara y reutilizable para estudiantes, separada del portal Flask de laboratorio.

## Enlace oficial del alumno

Si este repositorio se publica desde `vladimiracunadev-create/python-data-science-bootcamp`, el enlace esperado de GitHub Pages es:

`https://vladimiracunadev-create.github.io/python-data-science-bootcamp/`

Ese debe ser el enlace canonicamente compartido con estudiantes.

## Que resuelve GitHub Pages en este proyecto

- un punto de entrada estable y publico;
- una landing clara para alumnos;
- una URL facil de guardar y compartir;
- una capa informativa que no depende del backend Flask;
- una base visual que despues puede crecer a experiencia movil.

## Que queda en GitHub Pages

- presentacion del bootcamp;
- ruta de aprendizaje;
- recursos publicos;
- normas de trabajo y uso de tecnologia;
- enlace oficial del curso;
- explicacion de como se usa el programa desde celular.

## Que sigue viviendo en la app Flask

- catalogo dinamico de clases desde archivos locales;
- notebooks interactivos;
- guardado de notebooks;
- runner de codigo;
- ejecucion controlada del backend.

## Lo portable a una app movil

Lo que puede moverse casi directo:

- listado de clases;
- detalle de clase;
- avisos y recordatorios;
- datasets y recursos;
- tareas y checklist.

Lo que requiere mantener backend:

- ejecutar codigo;
- guardar notebooks;
- mantener sesiones;
- capturar salida y graficos;
- seguimiento individual por estudiante.

## Ruta recomendada de evolucion

1. GitHub Pages como portal publico del alumno.
2. App web movil para lectura y seguimiento.
3. App movil con backend del bootcamp para funciones interactivas.
4. Autenticacion y progreso individual si el programa lo necesita.

## Implementacion agregada en este repo

- `site/index.html`
- `site/styles.css`
- `site/app.js`
- `site/assets/icon.svg`
- `.github/workflows/deploy-pages.yml`

## Mensaje claro para reunion

"El proyecto ya no depende de un solo portal. Ahora tiene una cara publica para estudiantes en GitHub Pages y una ruta clara para evolucionar a movil, mientras la parte interactiva de laboratorio sigue aislada y controlada en la app Flask."
