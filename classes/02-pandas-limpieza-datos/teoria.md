# Documento teorico - Clase 02: Pandas y limpieza de datos

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Instalar la idea de que no se analiza una tabla sin revisarla primero.

## Por que importa este modulo

Usar pandas para cargar, inspeccionar y limpiar tablas antes de analizarlas.

## Bloque de codigo documentado

### Carga e inspeccion de un CSV

Primero abrimos el archivo y luego lo inspeccionamos para saber si podemos confiar en su estructura.

**Que hace:** cargar -> mirar forma -> revisar columnas

```python
import pandas as pd

# Cargamos el CSV en un DataFrame para trabajar por columnas.
df = pd.read_csv("datasets/ventas_tienda.csv")

print(df.head())
print(df.shape)
print(df.info())
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 03 usa tablas limpias para explorar patrones visuales.
