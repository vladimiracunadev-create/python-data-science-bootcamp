# Documento teorico - Clase 12: Proyecto final y cierre

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Cerrar con evidencia de aprendizaje integrado, no con una lista de tecnicas desconectadas.

## Por que importa este modulo

Integrar las habilidades del bootcamp en un proyecto final acotado y defendible.

## Bloque de codigo documentado

### Esqueleto del proyecto final

El codigo organiza el proyecto por etapas para que otra persona siga el razonamiento sin perderse.

**Que hace:** contexto -> carga -> analisis -> conclusion

```python
import pandas as pd

# 1. Cargar datos y dejar una copia de trabajo.
df = pd.read_csv("datasets/ventas_tienda.csv")
trabajo = df.copy()

# 2. Formular una pregunta visible antes de seguir.
pregunta = "Que categoria conviene reforzar en la proxima campana"
print(pregunta)
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

Despues del cierre, el estudiante deberia tener un siguiente paso de aprendizaje claro.
