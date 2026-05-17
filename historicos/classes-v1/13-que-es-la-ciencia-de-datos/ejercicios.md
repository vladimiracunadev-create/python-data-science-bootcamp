# 🧪 Ejercicios — Clase 13

> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar

- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.
- Explica qué hace cada transformación relevante y para qué sirve.

## 🧭 Trabajo guiado

### Ejercicio 1: Identifica el tipo de pregunta

Para cada situación siguiente, indica si la pregunta es **descriptiva**, **diagnóstica**, **predictiva** o **prescriptiva**. Justifica tu respuesta en una oración.

a) Una tienda quiere saber: "¿Cuántos productos vendimos en enero?"
b) Un médico pregunta: "¿Por qué este grupo de pacientes tiene más recaídas?"
c) Una aplicación de clima pregunta: "¿Lloverá mañana en esta ciudad?"
d) Un gerente pregunta: "¿A qué clientes debemos enviarles un cupón de descuento esta semana?"
e) Un director escolar pregunta: "¿Cuáles fueron los promedios por materia este semestre?"

### Ejercicio 2: Clasifica los tipos de datos

Para cada columna del dataset `ventas_tienda.csv`, indica el tipo de dato (numérico, categórico, texto, serie de tiempo) y explica por qué.

Pistas de columnas que pueden aparecer: `fecha`, `producto`, `categoría`, `precio_unitario`, `unidades`, `total_venta`, `region`.

Carga el dataset con el siguiente código y observa la salida de `df.info()`:

```python
import pandas as pd

# Cargamos el dataset para explorar sus columnas
df = pd.read_csv("datasets/ventas_tienda.csv")

# info() nos dice el nombre de cada columna, cuántos valores tiene y su tipo de dato
df.info()

# head() muestra las primeras filas para ver valores reales
df.head()
```

Responde: ¿Cuáles columnas son numéricas? ¿Cuáles son categóricas? ¿Hay alguna que podría considerarse serie de tiempo?

### Ejercicio 3: Mapea el ciclo CRISP-DM a un problema real

Elige uno de estos problemas o propón el tuyo:

- Una tienda quiere saber qué productos tienen más probabilidad de venderse en verano
- Una escuela quiere identificar estudiantes en riesgo de reprobar
- Un hospital quiere reducir los tiempos de espera en urgencias

Para el problema elegido, completa esta tabla:

| Paso CRISP-DM | ¿Qué harías en este problema? |
|---|---|
| Entender el problema | |
| Recolectar y entender los datos | |
| Preparar los datos | |
| Modelar | |
| Evaluar | |
| Comunicar e implementar | |

No necesitas escribir código — solo describir en lenguaje natural qué harías en cada paso.

### Ejercicio 4: Ciencia de datos en tu vida

Identifica **dos aplicaciones de ciencia de datos** que uses regularmente (pueden ser apps, plataformas, servicios). Para cada una:

a) Nombra la aplicación
b) Describe qué datos probablemente recolecta sobre ti
c) Indica qué tipo de pregunta responde (descriptiva, diagnóstica, predictiva o prescriptiva)
d) Explica cómo eso beneficia tanto a la empresa como a ti

## ✅ Criterios de autocorrección

- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
- Cada tipo de pregunta y de dato está correctamente identificado y justificado.
- La tabla CRISP-DM muestra pasos coherentes y específicos al problema elegido.
