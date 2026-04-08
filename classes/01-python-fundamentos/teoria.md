# Documento teorico - Clase 01: Python fundamentos

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Construir confianza en la sintaxis y conectar cada estructura con un uso real.

## Por que importa este modulo

Comprender los bloques basicos de Python y usarlos en tareas pequenas con datos.

## Bloque de codigo documentado

### Funcion con validacion simple

La funcion encapsula una tarea reutilizable y evita errores con una validacion minima.

**Que hace:** entrada -> validar -> calcular -> devolver

```python
def calcular_promedio(notas):
# Evitamos dividir por cero si la lista esta vacia.
if len(notas) == 0:
return 0

total = sum(notas)
return total / len(notas)

print(calcular_promedio([6.0, 6.5, 7.0]))
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 02 traslada estas bases a tablas con pandas.
