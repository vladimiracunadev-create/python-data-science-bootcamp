# Documento teorico - Clase 05: Visualizacion con matplotlib

> Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## Idea central

Pasar de la grafica funcional a la grafica comunicable.

## Por que importa este modulo

Crear graficos mas controlados con matplotlib y mejorar su legibilidad.

## Bloque de codigo documentado

### Grafico de linea legible

Creamos una figura explicita para controlar tamano, titulo y ejes.

**Que hace:** crear figure -> dibujar -> rotular

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/transporte.csv")
resumen = df.groupby("mes", as_index=False)["pasajeros"].sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(resumen["mes"], resumen["pasajeros"], marker="o")
ax.set_title("Pasajeros por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Pasajeros")
plt.tight_layout()
```

## Errores frecuentes a vigilar

- Saltar al codigo sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicacion oral.

## Conexion con el siguiente modulo

La clase 06 amplia el repertorio con texto y fechas.
