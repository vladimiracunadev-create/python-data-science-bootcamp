# 🧠 Documento teórico — Clase 04: Estadística descriptiva

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

La estadística descriptiva resume poblaciones, pero siempre debe volver a una pregunta concreta.

## ❓ Por qué importa este módulo

Permite pasar de mirar filas sueltas a resumir comportamientos de un grupo con criterio.

## 💻 Bloque de código documentado

### Resumen de asistencia del curso

Usar varias medidas a la vez evita depender de un único número y mejora la interpretación.

**Qué hace:** seleccionar variable → calcular resumen → interpretar

**Para qué sirve:** Sirve para conectar conceptos estadísticos con decisiones pedagógicas o de seguimiento académico.

```python
import pandas as pd

df = pd.read_csv("datasets/estudiantes.csv")
asistencia = df["asistencia_pct"]

print("Media:", asistencia.mean())
print("Mediana:", asistencia.median())
print("Desviación estándar:", asistencia.std())
print(asistencia.describe())
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 05 convierte estos resúmenes en gráficos más controlados con matplotlib.
