# Implementacion V1 para Skillnest / Colegio San Nicolas de Maipu

## Objetivo

Traducir este repositorio a una primera implementacion realista para un bootcamp presencial de Python para Data Science en el Colegio San Nicolas de Maipu, manteniendo una muestra fuerte de valor docente sin sobredimensionar la propuesta inicial.

## Contexto confirmado

- Programa: Bootcamp Python para Data Science.
- Institucion: Colegio San Nicolas de Maipu.
- Direccion informada: Mateo de Toro y Zambrano 3016, Maipu, Region Metropolitana.
- Modalidad: presencial.
- Fecha de inicio: por confirmar.
- Fecha de termino informada: 11 de diciembre de 2026.
- Trabajo administrativo informado: 4 horas semanales.

## Bloques horarios recibidos

- Miercoles: 12:15 a 13:45.
- Jueves: 09:30 a 10:15.
- Jueves: 10:35 a 11:20.

## Observaciones operativas que conviene aclarar

1. Los bloques escritos suman 180 minutos semanales.
2. Eso equivale a 4 horas pedagogicas de 45 minutos, no a 6 horas pedagogicas semanales.
3. Tampoco coincide con "2 clases a la semana de 3 horas cada dia".
4. Mientras Skillnest no confirme la carga real, conviene disenar la propuesta sobre bloques de 90 minutos, porque ese formato si coincide con la estructura real de este repositorio.

## Que ya tiene resuelto este repositorio

- 12 clases modulares de 90 minutos.
- README, slides, ejercicios, tareas, notebooks y soluciones por clase.
- Datasets sinteticos listos para usar.
- Documentacion docente, de evaluacion y de metodologia.
- App local para ejecutar codigo y notebooks dentro del mismo proyecto.
- Material suficiente para una demo de clase o reunion comercial.

## Que hoy esta sobredimensionado para una primera implementacion escolar

- Machine Learning, clasificacion, pipelines y proyecto final de modelado.
- Demasiados frentes tematicos para una primera cohorte.
- Mas de un dataset principal para estudiantes que probablemente parten con base inicial.
- Exigencia operativa innecesaria si se presenta Docker, PDF masivo y toda la app como requisito desde el primer contacto.

## Riesgos internos que justifican un recorte

- El dataset `datasets/estudiantes.csv` ya acerca el repo a un contexto educativo, pero su estructura actual no coincide del todo con el diccionario descrito en `datasets/README.md`.
- Esa diferencia vuelve poco recomendable usar el bloque de Machine Learning en una primera version, al menos no hasta alinear dataset, documentacion y actividades.

## Recorte recomendado para la V1

## Promesa de aprendizaje

Al terminar la primera version, el estudiante deberia poder:

- leer y modificar codigo simple en Python;
- cargar un CSV con pandas;
- hacer filtros, conteos y agrupaciones sencillas;
- construir un grafico basico;
- explicar un hallazgo en lenguaje claro.

## Contenido que si conviene mostrar

- `classes/01-python-fundamentos/`
- `classes/02-pandas-limpieza-datos/`
- `classes/03-visualizacion-exploratoria/`
- `classes/04-estadistica-descriptiva/` solo en su parte basica
- `classes/07-mini-proyecto-guiado/`
- `classes/08-presentacion-de-hallazgos/`

## Contenido que conviene dejar para fase 2

- `classes/05-visualizacion-con-matplotlib/`
- `classes/06-texto-fechas-y-transformaciones/`
- `classes/09-machine-learning-intro/`
- `classes/10-modelos-supervisados/`
- `classes/11-evaluacion-y-pipelines/`
- `classes/12-proyecto-final-y-cierre/`

## Dataset recomendado para la primera etapa

### Dataset principal

`datasets/ventas_tienda.csv`

Por que conviene:

- es simple de explicar;
- soporta Python, pandas y graficos sin cambiar de contexto;
- ya viene siendo usado por varias clases;
- incluye una sucursal Maipu, lo que ayuda a aterrizar la narrativa localmente sin forzar el caso.

### Dataset secundario

`datasets/estudiantes.csv`

Uso recomendado:

- analisis descriptivo;
- asistencia, desempeno y seguimiento;
- no usar todavia como base de ML hasta alinear estructura y materiales.

## Ruta minima viable

## Opcion recomendada: 6 unidades

1. Fundamentos de Python aplicados a datos.
2. Carga y lectura de CSV con pandas.
3. Filtros, columnas y tablas resumen.
4. Graficos simples e interpretacion.
5. Mini proyecto guiado en parejas.
6. Presentacion breve de hallazgos y cierre.

## Como escalarla sin agregar complejidad

Si la carga semanal real es de dos bloques de 90 minutos, cada unidad puede dividirse asi:

- bloque 1: explicacion y ejemplo guiado;
- bloque 2: practica, retroalimentacion y cierre.

Eso permite cubrir 6 unidades en 12 bloques sin introducir todavia contenido de ML.

## Como conviene presentar el repo en la entrevista

- No como "bootcamp completo cerrado", sino como base modular adaptable.
- No prometer personalizacion total antes de confirmar contratacion, alcance y grupo.
- Mostrar que ya existe estructura fuerte y que la adaptacion propuesta consiste en recortar con criterio, no en improvisar.

## Diferencial frente a repositorios publicos similares

Comparado con repositorios educativos abiertos en GitHub, este proyecto ya combina tres capas al mismo tiempo:

1. capa curricular: clases, notebooks, ejercicios y soluciones;
2. capa docente: metodologia, evaluacion y guia del instructor;
3. capa operativa: app local para practicar en el mismo entorno.

Ese mix es valioso para entrevista porque muestra mas que contenido tecnico: muestra capacidad de implementacion real.

## Decision practica para esta entrevista

La mejor posicion para una primera reunion es:

- mostrar la ruta V1;
- llevar una demo corta con clases 01, 02 y 07;
- dejar ML y personalizaciones profundas como siguiente etapa pagada;
- pedir confirmacion de horas reales, nivel del grupo, cantidad de estudiantes, equipamiento y forma de pago antes de producir mas material a medida.
