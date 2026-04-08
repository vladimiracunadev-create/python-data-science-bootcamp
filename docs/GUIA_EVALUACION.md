# 🧾 Guía de evaluación rápida

> Audiencia: institución, recruiter, evaluador técnico y personas que necesitan entender el valor del repositorio sin leer todo el código.

## Executive summary

Este repositorio demuestra una forma de construir capacitaciones técnicas con criterio:

- curriculum modular y reusable;
- laboratorio local para practicar;
- portal del alumno para la capa pública;
- presentación institucional separada del README técnico;
- documentación de operación y seguridad visible;
- crecimiento posible hacia nuevas cohortes y experiencia móvil.

No es un SaaS multiusuario terminado ni pretende vender madurez que todavia no existe.

## Lo que demuestra hoy

| ?rea | Evidencia visible |
|---|---|
| Diseño pedagógico | `classes/`, `metodologia-docente.md`, `herramientas-pedagogicas-de-aula.md` |
| Producto navegable | `site/` y `site/product/` |
| Entorno operativo | `app/`, `RUNBOOK.md`, `GET /health`, `GET /ready` |
| Postura responsable | `SECURITY.md`, `docker-compose.prod.yml`, CI y security workflows |
| Escalabilidad honesta | `CATALOGO_PRODUCTO.md`, `ARQUITECTURA_PRODUCTO.md`, ruta móvil como evolución |

## Qué mirar en 10 minutos

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
| Operación reproducible | [../RUNBOOK.md](../RUNBOOK.md) |
| Seguridad honesta | [../SECURITY.md](../SECURITY.md) |
| Capa pública no técnica | `site/product/` |

## Lo que este repositorio si es

- una base seria de capacitación técnica;
- un sistema que integra contenido, práctica y presentación;
- una demostracion de criterio pedagógico y operacional;
- una propuesta que puede partir acotada y crecer sin rehacerse.

## Lo que no intenta vender

- una plataforma multiusuario endurecida para internet abierta;
- una app móvil ya operativa;
- personalización infinita antes de definir condiciones reales;
- un bootcamp que ya despliega toda la profundidad técnica desde la primera versión escolar.

## Conclusiones que una evaluación justa deberia poder sacar

- hay una forma de trabajo y no solo una clase aislada;
- existe coherencia entre producto, operación y documentación;
- la propuesta esta acotada de forma responsable para una primera implementación;
- el valor no depende de una tecnología puntual, sino de la mediación pedagógica y del criterio de diseño.
