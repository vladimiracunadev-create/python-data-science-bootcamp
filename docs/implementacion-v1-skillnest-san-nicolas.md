# 🏫 Implementacion V1 para Skillnest / Colegio San Nicolas de Maipu

Documento de aterrizaje para convertir este repositorio en una primera implementacion escolar concreta, acotada y defendible. La idea no es prometer "todo el bootcamp completo", sino mostrar que la base ya existe y que sabes recortarla con criterio.

## 1. Contexto confirmado

Datos entregados por Skillnest:

- programa: Bootcamp Python para Data Science;
- modalidad: presencial;
- establecimiento: Colegio San Nicolas de Maipu;
- direccion informada: Mateo de Toro y Zambrano 3016, Santiago, Maipu, Region Metropolitana;
- inicio: por confirmar;
- termino informado: 11 de diciembre de 2026;
- trabajo administrativo: 4 horas semanales.

Bloques horarios informados:

- miercoles de 12:15 a 13:45;
- jueves de 09:30 a 10:15;
- jueves de 10:35 a 11:20.

## 2. Observacion critica sobre la carga horaria

Los bloques informados suman 180 minutos semanales. Eso equivale a:

- 4 horas pedagogicas de 45 minutos; o
- 3 horas cronologicas.

Eso no coincide con:

- "2 clases a la semana de 3 horas cada dia"; ni
- "6 horas pedagogicas semanales".

Esta inconsistencia debe aclararse en la entrevista. Mientras no exista confirmacion, la propuesta V1 conviene presentarla como modular y adaptable a bloques de 90 minutos.

## 3. Lo que ya resuelve el repo para una V1

- 12 clases modulares con materiales reutilizables;
- notebooks, soluciones y datasets;
- documentacion docente y de evaluacion;
- laboratorio local para demostracion;
- portal del alumno y capa institucional;
- CI/CD y postura operativa visible.

Eso significa que no partes desde cero. Partes desde una base que se puede recortar sin improvisar.

## 4. Criterio de recorte recomendado

Primera implementacion escolar:

- menos temas;
- mas profundidad en fundamentos;
- un dataset principal;
- evaluacion simple y seguimiento visible;
- tecnologia usada con criterio, no como show.

## 5. Promesa de aprendizaje para la V1

Al terminar la primera version, el estudiante deberia poder:

- leer y modificar codigo simple en Python;
- cargar un CSV con pandas;
- limpiar datos basicos;
- construir una tabla resumen;
- hacer un grafico sencillo;
- explicar un hallazgo con lenguaje claro.

## 6. Contenido recomendado para mostrar ahora

| Prioridad | Clase | Rol en la V1 |
|---|---|---|
| alta | `classes/01-python-fundamentos/` | entrada al lenguaje |
| alta | `classes/02-pandas-limpieza-datos/` | lectura y manipulacion basica |
| alta | `classes/03-visualizacion-exploratoria/` | primeras conclusiones desde datos |
| media | `classes/04-estadistica-descriptiva/` | interpretacion simple |
| alta | `classes/07-mini-proyecto-guiado/` | integracion de habilidades |
| alta | `classes/08-presentacion-de-hallazgos/` | cierre comunicable |

## 7. Contenido que conviene dejar para fase 2

- `classes/05-visualizacion-con-matplotlib/`
- `classes/06-texto-fechas-y-transformaciones/`
- `classes/09-machine-learning-intro/`
- `classes/10-modelos-supervisados/`
- `classes/11-evaluacion-y-pipelines/`
- `classes/12-proyecto-final-y-cierre/`

No porque no sirvan, sino porque en una primera cohorte escolar pueden abrir demasiados frentes a la vez.

## 8. Dataset recomendado para la etapa inicial

### Principal

`datasets/ventas_tienda.csv`

Ventajas:

- facil de explicar;
- sirve para Python, pandas y graficos;
- soporta preguntas concretas y hallazgos simples;
- incluye una sucursal Maipu que ayuda a aterrizar la narrativa.

### Secundario

`datasets/estudiantes.csv`

Uso recomendado:

- analisis descriptivo;
- asistencia y seguimiento;
- no usar como base de ML en la V1 hasta alinear completamente estructura y materiales.

## 9. Ruta minima viable

```mermaid
flowchart LR
    A["Python base"] --> B["Leer CSV"]
    B --> C["Filtrar y resumir"]
    C --> D["Graficar"]
    D --> E["Mini proyecto"]
    E --> F["Presentar hallazgos"]
```

Esta ruta es suficiente para una primera implementacion creible, medible y ejecutable.

## 10. Como usar las horas administrativas

Las 4 horas administrativas no deberian gastarse en regalar produccion infinita previa. Conviene orientarlas a:

- ajuste final de materiales segun grupo;
- revision de asistencia y evidencias;
- comunicacion con coordinacion;
- preparacion de la siguiente sesion;
- retroalimentacion corta y util.

## 11. Riesgos y mitigaciones

| Riesgo | Impacto | Mitigacion |
|---|---|---|
| horas reales no confirmadas | desalineacion del plan | pedir confirmacion antes de cerrar cronograma |
| grupo con base muy heterogenea | brecha de avance | minimo comun claro y desafio opcional |
| expectativa de demasiado contenido | sobrecarga | presentar V1 como ruta acotada y escalable |
| uso desordenado de tecnologia | copia sin comprension | reglas de uso, adaptacion y explicacion |
| pedir mas trabajo previo sin acuerdo | desgaste y devaluacion | mostrar base existente y acotar personalizacion |

## 12. Que demostrar en la reunion

- que sabes convertir un repo amplio en una implementacion viable;
- que no sobredimensionas la primera entrega;
- que entiendes ritmo escolar, mediacion y evaluacion;
- que sabes diferenciar demo, piloto y despliegue real.

## 13. Que no regalar en la entrevista

No conviene dejar instalada la idea de que haras, sin cierre formal:

- personalizacion total por colegio;
- rediseno completo del curriculum;
- desarrollo movil completo;
- integraciones extras o despliegue abierto del runner.

El mensaje correcto es otro: la base ya existe, la V1 se puede activar con criterio, y el crecimiento posterior se disena con el alcance ya confirmado.

## 14. Mensaje recomendado para presentar esta V1

"No estoy proponiendo empezar por la version mas grande del repositorio. Estoy proponiendo una primera implementacion escolar, clara y medible, montada sobre una base ya seria. Eso permite comenzar bien, evidenciar resultados y crecer despues sin rehacer el trabajo."

## 15. Relacion con otros documentos

- [GUIA_EVALUACION.md](GUIA_EVALUACION.md)
- [plan-evaluacion.md](plan-evaluacion.md)
- [metodologia-docente.md](metodologia-docente.md)
- [entrevista/proceso-seleccion-skillnest.md](entrevista/proceso-seleccion-skillnest.md)
