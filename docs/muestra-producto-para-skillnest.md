# Bootcamp Python para Data Science

## Muestra de producto

### Base de capacitacion adaptable para colegios

## Resumen

Este repositorio no es solo una coleccion de archivos. Es una base de capacitacion pensada para ensenanza real: combina contenidos, progresion pedagogica, practica guiada, evaluacion y un entorno de trabajo local.

## Que incluye hoy

- 12 clases modulares de 90 minutos;
- notebooks, ejercicios, tareas y soluciones;
- datasets sinteticos listos para usar;
- documentacion docente y metodologica;
- app local para exploracion y practica;
- portal publico del alumno para GitHub Pages.

## Dos superficies complementarias

### 1. Portal del alumno

Landing publica, simple y facil de compartir con estudiantes.

Rol:

- punto de entrada oficial del curso;
- ruta del programa;
- recursos publicos;
- uso responsable de tecnologia;
- base para evolucion futura a movil.

### 2. Portal interactivo de laboratorio

Aplicacion Flask para trabajo guiado.

Rol:

- ver clases;
- cargar notebooks;
- ejecutar codigo;
- guardar practica;
- mantener el trabajo del bootcamp dentro del mismo entorno.

## Enfoque de valor

La propuesta no compite contra una tecnologia especifica. Su valor esta en:

- traducir tecnologia a aprendizaje real;
- secuenciar bien la dificultad;
- combinar teoria, practica e interpretacion;
- reducir friccion para estudiantes que recien comienzan;
- dejar una base reusable para siguientes cohortes.

## Version inicial recomendada para colegio

Para una primera implementacion escolar, la propuesta se acota a:

1. fundamentos de Python;
2. lectura de CSV con pandas;
3. filtros y tablas resumen;
4. visualizacion basica;
5. mini proyecto guiado;
6. presentacion breve de hallazgos.

## Postura de despliegue y seguridad

El entorno interactivo esta pensado para uso local y docente.

Hoy ya contempla:

- validacion de entradas;
- limites de payload y de codigo;
- control de sesiones y timeout;
- headers de seguridad basicos;
- despliegue local por defecto;
- `docker-compose` enlazado a `127.0.0.1`.

Si en algun momento se expusiera fuera de entorno controlado, la siguiente capa recomendada es:

- reverse proxy con TLS;
- autenticacion adicional;
- rate limiting;
- observabilidad y operacion mas formal.

## Escalabilidad

Esta base puede crecer en tres direcciones:

- mas profundidad tecnica;
- adaptaciones por institucion o perfil;
- evolucion a experiencia movil conectada al backend del curso.

## Cierre

La fortaleza de este producto no es solo el contenido tecnico. Es que ya muestra una forma de hacer capacitaciones con criterio pedagogico, estructura operacional y espacio real para crecer.
