# Documento teorico - Clase 06: Texto, fechas y transformaciones

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Muchas preguntas nuevas aparecen cuando una columna se transforma bien.

## Por que importa este modulo

Transformar columnas de texto y fecha para volverlas utiles en analisis y modelado inicial.

## Bloque de codigo documentado

### Conversion de fechas y variables derivadas

Convertir a fecha habilita nuevas preguntas como comportamiento por mes o dia de semana.

**Que hace:** convertir fecha -> extraer componente -> usar

```python
import pandas as pd

tickets = pd.read_csv("datasets/soporte_tickets.csv")
tickets["fecha_creacion"] = pd.to_datetime(tickets["fecha_creacion"])

# Creamos columnas nuevas para responder preguntas posteriores.
tickets["mes"] = tickets["fecha_creacion"].dt.month
tickets["dia_semana"] = tickets["fecha_creacion"].dt.day_name()

print(tickets[["fecha_creacion", "mes", "dia_semana"]].head())
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 07 usa estas habilidades en un mini proyecto guiado.
