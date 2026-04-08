# Diccionario de datasets del Bootcamp Python Data Science

> Catalogo de datasets sinteticos y su uso dentro del bootcamp.

Este directorio contiene los datasets base usados en las clases. Todos los datos son sinteticos con contexto realista y fueron preparados para practicar lectura, limpieza, analisis, visualizacion y modelado inicial.

## 1. ventas_tienda.csv

**Descripcion:** Registro de ventas de una tienda con varias sucursales, categorias y medios de pago. Es el dataset principal del recorrido.

**Clases que lo usan:** 01, 02, 03, 04, 05, 07, 09, 11

| Columna | Tipo | Descripcion | Ejemplo |
|---|---|---|---|
| `fecha` | date | Fecha de la venta | `2026-01-03` |
| `sucursal` | str | Sede donde se realizo la venta | `Centro` |
| `categoria` | str | Familia del producto | `Accesorios` |
| `producto` | str | Producto vendido | `Mouse` |
| `unidades` | int | Cantidad vendida | `12` |
| `precio_unitario` | float | Precio por unidad en CLP | `8990` |
| `descuento_pct` | float | Descuento expresado entre `0` y `1` | `0.10` |
| `vendedor` | str | Responsable de la venta | `Ana` |
| `medio_pago` | str | Medio de pago registrado | `Debito` |

**Columnas derivadas sugeridas:**
- `total_bruto = unidades * precio_unitario`
- `total_neto = total_bruto * (1 - descuento_pct)`
- `mes` y `dia_semana` a partir de `fecha`

**Notas:**
- Sirve para practicar agrupaciones, metricas comerciales y graficos comparativos.
- El descuento ya viene normalizado como proporcion, no como porcentaje entero.

## 2. retencion_clientes.csv

**Descripcion:** Serie mensual para analizar actividad de clientes, perdidas, altas y valor economico promedio.

**Clases que lo usan:** 03, 08, 10

| Columna | Tipo | Descripcion | Ejemplo |
|---|---|---|---|
| `mes` | str | Periodo mensual en formato `YYYY-MM` | `2026-01` |
| `clientes_activos` | int | Base activa al cierre del periodo | `120` |
| `clientes_perdidos` | int | Clientes que dejaron de operar | `9` |
| `nuevos_clientes` | int | Altas del periodo | `18` |
| `ingreso_promedio` | float | Ingreso promedio por cliente | `41.2` |

**Columnas derivadas sugeridas:**
- `saldo_clientes = nuevos_clientes - clientes_perdidos`
- `churn_pct = clientes_perdidos / clientes_activos * 100`
- `crecimiento_pct` respecto del mes anterior

**Notas:**
- Es util para series temporales simples y storytelling de negocio.
- Funciona bien para ejercicios de tendencia, comparacion mensual y riesgo.

## 3. soporte_tickets.csv

**Descripcion:** Tickets de soporte clasificados por categoria, prioridad, canal y tiempo de resolucion.

**Clases que lo usan:** 02, 06

| Columna | Tipo | Descripcion | Ejemplo |
|---|---|---|---|
| `ticket_id` | str | Identificador del ticket | `T-1001` |
| `categoria` | str | Tipo de incidencia | `Acceso` |
| `prioridad` | str | Nivel de urgencia | `Alta` |
| `horas_resolucion` | float | Tiempo de resolucion en horas | `2.1` |
| `satisfaccion` | float | Nota del usuario | `4.5` |
| `canal` | str | Canal por el que entro el ticket | `Correo` |

**Columnas derivadas sugeridas:**
- `resuelto_rapido = horas_resolucion <= 4`
- `satisfaccion_redondeada = satisfaccion.round()`
- `prioridad_orden` para ordenar tableros

**Notas:**
- Permite contrastar velocidad, calidad de servicio y mezcla de canales.
- Es un buen set para filtrar, recodificar texto y resumir indicadores.

## 4. transporte.csv

**Descripcion:** Registro de viajes con origen, destino, pasajeros, retraso y contexto operativo.

**Clases que lo usan:** 04, 06

| Columna | Tipo | Descripcion | Ejemplo |
|---|---|---|---|
| `id_viaje` | int | Identificador del viaje | `1` |
| `linea` | str | Linea o servicio | `L1` |
| `origen` | str | Punto de salida | `Centro` |
| `destino` | str | Punto de llegada | `Norte` |
| `duracion_min` | int | Duracion del viaje en minutos | `35` |
| `pasajeros` | int | Carga de pasajeros | `120` |
| `retraso_min` | int | Retraso acumulado | `4` |
| `dia_semana` | str | Dia del viaje | `Lunes` |
| `lluvia` | str | Indicador simple de clima | `No` |

**Columnas derivadas sugeridas:**
- `puntual = retraso_min <= 5`
- `tramo = origen + '-' + destino`
- `carga_por_min = pasajeros / duracion_min`

**Notas:**
- Ayuda a practicar comparaciones por categoria y lectura de contexto operativo.
- Tambien sirve para ejemplos de variables binarias y mezcla de tipos.

## 5. estudiantes.csv

**Descripcion:** Registro academico sintetico para analizar desempeno, asistencia y estado del alumno.

**Clases que lo usan:** 04, 09, 10

| Columna | Tipo | Descripcion | Ejemplo |
|---|---|---|---|
| `id_estudiante` | int | Identificador del estudiante | `1` |
| `nombre` | str | Nombre visible en el ejemplo | `Valentina` |
| `edad` | int | Edad del estudiante | `19` |
| `curso` | str | Cohorte o grupo | `Bootcamp A` |
| `asistencia_pct` | int | Asistencia acumulada | `92` |
| `evaluacion_python` | int | Resultado en Python | `78` |
| `evaluacion_pandas` | int | Resultado en pandas | `74` |
| `entrega_proyecto` | str | Si entrego el proyecto | `Si` |
| `situacion` | str | Estado academico resumido | `Regular` |

**Columnas derivadas sugeridas:**
- `promedio_tecnico = (evaluacion_python + evaluacion_pandas) / 2`
- `riesgo = asistencia_pct < 75 or entrega_proyecto == 'No'`
- `cumplimiento = situacion == 'Regular'`

**Notas:**
- Es util para clasificacion basica, lectura de cohortes y segmentacion.
- Conviene revisar relaciones entre asistencia, evaluaciones y entrega final.

## Origen y licencia

Todos los datasets son datos sinteticos generados para uso educativo dentro del bootcamp. No representan personas ni organizaciones reales.

Licencia: MIT para uso educativo y de demostracion con atribucion.
