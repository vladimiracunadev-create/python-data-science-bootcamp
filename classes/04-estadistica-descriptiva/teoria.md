# Documento teorico - Clase 04: Estadistica descriptiva

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Pasar de mirar valores sueltos a resumir poblaciones con una pregunta clara.

## Por que importa este modulo

Interpretar medidas descriptivas simples y relacionarlas con preguntas reales.

## Bloque de codigo documentado

### Resumen general de una columna

Usamos varias medidas juntas para no depender de un unico numero.

**Que hace:** seleccionar variable -> calcular resumen -> interpretar

```python
import pandas as pd

df = pd.read_csv("datasets/retencion_clientes.csv")
columna = df["clientes_activos"]

print("Media:", columna.mean())
print("Mediana:", columna.median())
print("Desv. estandar:", columna.std())
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 05 lleva estas conclusiones a graficos mas controlados.
