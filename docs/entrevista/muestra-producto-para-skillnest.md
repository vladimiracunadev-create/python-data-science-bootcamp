# 📦 Bootcamp Python para Data Science

## Muestra de producto

### Base de capacitación adaptable para colegios

## Resumen

Este repositorio no es solo una colección de archivos. Es una base de capacitación pensada para enseñanza real: combina contenidos, progresión pedagógica, práctica guiada, evaluación y un entorno de trabajo local.

## Qué incluye hoy

- clase 0 diagnóstica + 12 clases modulares de 90 minutos;
- notebooks, ejercicios, tareas y soluciones;
- datasets sinteticos listos para usar;
- documentación docente y metodologica;
- app local para exploracion y práctica;
- portal público del alumno para GitHub Pages.

## Dos superficies complementarias

### 1. Portal del alumno

Landing pública, simple y facil de compartir con estudiantes.

Rol:

- punto de entrada oficial del curso;
- ruta del programa;
- recursos públicos;
- uso responsable de tecnología;
- base para evolución futura a móvil.

### 2. Portal interactivo de laboratorio

Aplicacion Flask para trabajo guiado.

Rol:

- ver clases;
- cargar notebooks;
- ejecutar código;
- guardar práctica;
- mantener el trabajo del bootcamp dentro del mismo entorno.

## Enfoque de valor

La propuesta no compite contra una tecnología especifica. Su valor esta en:

- traducir tecnología a aprendizaje real;
- secuenciar bien la dificultad;
- combinar teoría, práctica e interpretacion;
- reducir friccion para estudiantes que recien comienzan;
- dejar una base reusable para siguientes cohortes.

## Versión inicial recomendada para colegio

Para una primera implementación escolar, la propuesta se acota a:

1. fundamentos de Python;
2. lectura de CSV con pandas;
3. filtros y tablas resumen;
4. visualización básica;
5. mini proyecto guiado;
6. presentación breve de hallazgos.

## Postura de despliegue y seguridad

El entorno interactivo esta pensado para uso local y docente.

Hoy ya contempla:

- validación de entradas;
- límites de payload y de código;
- control de sesiones y timeout;
- headers de seguridad básicos;
- despliegue local por defecto;
- `docker-compose` enlazado a `127.0.0.1`.

Si en algun momento se expusiera fuera de entorno controlado, la siguiente capa recomendada es:

- reverse proxy con TLS;
- autenticacion adicional;
- rate limiting;
- observabilidad y operación más formal.

## Escalabilidad

Esta base puede crecer en tres direcciones:

- más profundidad técnica;
- adaptaciónes por institución o perfil;
- evolución a experiencia móvil conectada al backend del curso.

## Cierre

La fortaleza de este producto no es solo el contenido técnico. Es que ya muestra una forma de hacer capacitaciones con criterio pedagógico, estructura operacional y espacio real para crecer.
