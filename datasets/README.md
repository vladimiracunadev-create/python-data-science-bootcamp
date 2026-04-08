# 🗂 Diccionario de Datasets â€” Bootcamp Python Data Science

> 🗂 Catalogo de datasets sinteticos y su uso dentro del bootcamp.


Este directorio contiene los datasets utilizados en las clases del bootcamp. Todos los datos son **sintÃ©ticos con contexto realista** generados para fines educativos.

---

## 1. ventas_tienda.csv

**DescripciÃ³n:** Registro de transacciones de una tienda de tecnologÃ­a con varias sucursales. Dataset principal del bootcamp.

**Clases que lo usan:** 01, 02, 03, 04, 05, 07, 09, 11

| Columna | Tipo | DescripciÃ³n | Ejemplo |
|---|---|---|---|
| `id_venta` | str | Identificador Ãºnico de la transacciÃ³n | `V-00123` |
| `fecha_venta` | date | Fecha de la transacciÃ³n (YYYY-MM-DD) | `2024-03-15` |
| `sucursal` | str | Nombre de la sucursal | `Norte`, `Sur`, `Centro`, `Oriente` |
| `vendedor` | str | Nombre del vendedor | `FernÃ¡ndez, Ana` |
| `categoria` | str | CategorÃ­a del producto | `PerifÃ©ricos`, `ComputaciÃ³n`, `Audio` |
| `producto` | str | Nombre del producto vendido | `Teclado mecÃ¡nico RGB` |
| `precio_unitario` | float | Precio antes del descuento ($) | `45990.0` |
| `unidades_vendidas` | int | Cantidad vendida | `3` |
| `descuento_pct` | float | Porcentaje de descuento aplicado (0â€“100) | `10.0` |

**Columnas derivadas sugeridas:**
- `total_bruto = precio_unitario Ã— unidades_vendidas`
- `total_neto = total_bruto Ã— (1 - descuento_pct / 100)`
- `mes`, `dia_semana` (desde `fecha_venta`)

**Notas:**
- Los precios estÃ¡n en pesos chilenos (CLP).
- El descuento mÃ¡ximo es 30%.
- No hay valores nulos en el dataset base.

---

## 2. retencion_clientes.csv

**DescripciÃ³n:** Indicadores de retenciÃ³n de clientes a lo largo del tiempo. Ãštil para anÃ¡lisis de series temporales y storytelling.

**Clases que lo usan:** 03, 08, 10

| Columna | Tipo | DescripciÃ³n | Ejemplo |
|---|---|---|---|
| `periodo` | str | Mes-AÃ±o del registro | `2024-01`, `2024-06` |
| `clientes_inicio` | int | Clientes activos al inicio del periodo | `1250` |
| `clientes_nuevos` | int | Nuevos clientes captados | `180` |
| `clientes_perdidos` | int | Clientes que cancelaron o no renovaron | `95` |
| `tasa_retencion` | float | % de clientes retenidos vs. periodo anterior | `87.5` |
| `nps_promedio` | float | Net Promoter Score promedio (0â€“100) | `62.3` |

**Columnas derivadas sugeridas:**
- `clientes_fin = clientes_inicio + clientes_nuevos - clientes_perdidos`
- `tasa_churn = clientes_perdidos / clientes_inicio Ã— 100`

**Notas:**
- 12 filas: un registro por mes del aÃ±o 2024.
- NPS > 50 se considera "bueno", > 70 "excelente".

---

## 3. soporte_tickets.csv

**DescripciÃ³n:** Registro de tickets de soporte tÃ©cnico. Permite analizar tiempos de resoluciÃ³n, categorÃ­as y satisfacciÃ³n del usuario.

**Clases que lo usan:** 02, 06

| Columna | Tipo | DescripciÃ³n | Ejemplo |
|---|---|---|---|
| `id_ticket` | str | Identificador Ãºnico del ticket | `TK-0045` |
| `fecha_apertura` | datetime | Fecha y hora de apertura | `2024-05-12 09:30` |
| `fecha_cierre` | datetime | Fecha y hora de cierre (nulo si abierto) | `2024-05-13 14:20` |
| `categoria` | str | Tipo de problema | `Hardware`, `Software`, `Red`, `Otro` |
| `prioridad` | str | Nivel de urgencia | `Baja`, `Media`, `Alta`, `CrÃ­tica` |
| `agente` | str | TÃ©cnico asignado | `Rodrigo Morales` |
| `satisfaccion` | int | CalificaciÃ³n del usuario (1â€“5) | `4` |

**Columnas derivadas sugeridas:**
- `horas_resolucion = (fecha_cierre - fecha_apertura).dt.total_seconds() / 3600`
- `ticket_abierto = fecha_cierre.isnull()`

**Notas:**
- Algunos tickets no tienen `fecha_cierre` (siguen abiertos).
- La columna `satisfaccion` puede tener nulos (cliente no respondiÃ³ la encuesta).

---

## 4. transporte.csv

**DescripciÃ³n:** Datos operacionales de un sistema de transporte pÃºblico. Permite anÃ¡lisis de demanda, eficiencia y patrones temporales.

**Clases que lo usan:** 04, 06

| Columna | Tipo | DescripciÃ³n | Ejemplo |
|---|---|---|---|
| `fecha` | date | Fecha del registro | `2024-06-01` |
| `linea` | str | LÃ­nea de transporte | `L1`, `L2`, `L5` |
| `estacion` | str | Nombre de la estaciÃ³n | `Baquedano`, `Las Condes` |
| `hora_pico` | str | Franja horaria | `07-09`, `13-15`, `18-20` |
| `pasajeros_subida` | int | Pasajeros que suben en la estaciÃ³n | `1234` |
| `pasajeros_bajada` | int | Pasajeros que bajan | `987` |
| `tiempo_espera_min` | float | Tiempo de espera promedio (minutos) | `4.5` |
| `incidencias` | int | NÃºmero de incidencias registradas | `0` |
| `temperatura_c` | float | Temperatura ambiental en Â°C | `18.5` |

**Columnas derivadas sugeridas:**
- `flujo_neto = pasajeros_subida - pasajeros_bajada`
- `dia_semana` (desde `fecha`)

**Notas:**
- El anÃ¡lisis de temperatura vs. demanda es especialmente interesante.
- Las incidencias estÃ¡n correlacionadas con el tiempo de espera.

---

## 5. estudiantes.csv

**DescripciÃ³n:** Registro acadÃ©mico de estudiantes para anÃ¡lisis educativo. Permite practicar regresiÃ³n y clasificaciÃ³n con variables claras e interpretables.

**Clases que lo usan:** 04, 09, 10

| Columna | Tipo | DescripciÃ³n | Ejemplo |
|---|---|---|---|
| `id_estudiante` | str | Identificador Ãºnico | `EST-001` |
| `nombre` | str | Nombre (anonimizado) | `Estudiante_42` |
| `edad` | int | Edad en aÃ±os | `24` |
| `horas_estudio_semana` | float | Horas de estudio semanal | `12.5` |
| `nota_prueba_1` | float | Nota de la primera prueba (0â€“100) | `72.0` |
| `nota_prueba_2` | float | Nota de la segunda prueba (0â€“100) | `68.5` |
| `asistencia_pct` | float | Porcentaje de asistencia (0â€“100) | `85.0` |
| `trabaja` | bool | Si trabaja mientras estudia | `True` |
| `nota_final` | float | Nota final del curso (0â€“100) | `70.2` |

**Columnas derivadas sugeridas:**
- `aprobado = (nota_final >= 60).astype(int)`
- `promedio_pruebas = (nota_prueba_1 + nota_prueba_2) / 2`

**Variable objetivo para ML:**
- RegresiÃ³n: `nota_final`
- ClasificaciÃ³n: `aprobado`

**Notas:**
- La correlaciÃ³n `horas_estudio_semana` â†’ `nota_final` es intencionalmente fuerte.
- Los estudiantes que trabajan tienen mayor variabilidad en sus notas.

---

## ⚖ Origen y licencia

Todos los datasets son **datos sintÃ©ticos** generados con Python para uso exclusivamente educativo en este bootcamp. No contienen datos reales de personas, empresas o entidades.

Licencia: MIT â€” libre uso educativo con atribuciÃ³n.
