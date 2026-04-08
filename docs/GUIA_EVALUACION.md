# 🧾 Guia de evaluacion rapida

> Audiencia: institucion, recruiter, evaluador tecnico y personas que necesitan entender el valor del repositorio sin leer todo el codigo.

## Executive summary

Este repositorio demuestra una forma de construir capacitaciones tecnicas con criterio:

- curriculum modular y reusable;
- laboratorio local para practicar;
- portal del alumno para la capa publica;
- presentacion institucional separada del README tecnico;
- documentacion de operacion y seguridad visible;
- crecimiento posible hacia nuevas cohortes y experiencia movil.

No es un SaaS multiusuario terminado ni pretende vender madurez que todavia no existe.

## Lo que demuestra hoy

| Area | Evidencia visible |
|---|---|
| Diseno pedagogico | `classes/`, `metodologia-docente.md`, `herramientas-pedagogicas-de-aula.md` |
| Producto navegable | `site/` y `site/product/` |
| Entorno operativo | `app/`, `RUNBOOK.md`, `GET /health`, `GET /ready` |
| Postura responsable | `SECURITY.md`, `docker-compose.prod.yml`, CI y security workflows |
| Escalabilidad honesta | `CATALOGO_PRODUCTO.md`, `ARQUITECTURA_PRODUCTO.md`, ruta movil como evolucion |

## Que mirar en 10 minutos

1. [../README.md](../README.md)
2. [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md)
3. [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md)
4. `site/product/`
5. [../SECURITY.md](../SECURITY.md)

## Senales de madurez documental

| Senal | Donde se ve |
|---|---|
| Rutas por audiencia | [INDEX.md](INDEX.md) |
| Fuente de verdad del producto | [CATALOGO_PRODUCTO.md](CATALOGO_PRODUCTO.md) |
| Arquitectura explicada con diagramas | [ARQUITECTURA_PRODUCTO.md](ARQUITECTURA_PRODUCTO.md) |
| Operacion reproducible | [../RUNBOOK.md](../RUNBOOK.md) |
| Seguridad honesta | [../SECURITY.md](../SECURITY.md) |
| Capa publica no tecnica | `site/product/` |

## Lo que este repositorio si es

- una base seria de capacitacion tecnica;
- un sistema que integra contenido, practica y presentacion;
- una demostracion de criterio pedagogico y operacional;
- una propuesta que puede partir acotada y crecer sin rehacerse.

## Lo que no intenta vender

- una plataforma multiusuario endurecida para internet abierta;
- una app movil ya operativa;
- personalizacion infinita antes de definir condiciones reales;
- un bootcamp que ya despliega toda la profundidad tecnica desde la primera version escolar.

## Conclusiones que una evaluacion justa deberia poder sacar

- hay una forma de trabajo y no solo una clase aislada;
- existe coherencia entre producto, operacion y documentacion;
- la propuesta esta acotada de forma responsable para una primera implementacion;
- el valor no depende de una tecnologia puntual, sino de la mediacion pedagogica y del criterio de diseno.
