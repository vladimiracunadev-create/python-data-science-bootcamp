# 🧠 Documento teórico — Clase 12: Proyecto final y cierre

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

El cierre del bootcamp debe mostrar integración, criterio y claridad de comunicación.

## ❓ Por qué importa este módulo

El proyecto final permite ver si el estudiante integra análisis, código y comunicación con una lógica completa.

## 💻 Bloque de código documentado

### Esqueleto inicial del proyecto final

Organizar el proyecto por etapas hace que otra persona pueda seguir el razonamiento sin perderse.

**Qué hace:** contexto → carga → análisis → conclusión

**Para qué sirve:** Sirve para modelar una estructura mínima que haga legible el trabajo final ante docentes y compañeros.

```python
# Qué hace: contexto → carga → análisis → conclusión.
# Para qué sirve: Sirve para modelar una estructura mínima que haga legible el trabajo final ante docentes y compañeros.
import pandas as pd

# 1. Cargar datos y dejar una copia de trabajo.
df = pd.read_csv("datasets/ventas_tienda.csv")
trabajo = df.copy()
trabajo["total_neto"] = trabajo["unidades"] * trabajo["precio_unitario"] * (1 - trabajo["descuento_pct"])

# 2. Formular la pregunta antes de seguir.
pregunta = "¿Qué sucursal conviene reforzar en la próxima campaña?"
print(pregunta)

# 3. Generar una evidencia inicial.
resumen = (
    trabajo.groupby("sucursal", as_index=False)["total_neto"]
    .sum()
    .sort_values("total_neto", ascending=False)
)
print(resumen.head())
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

Después del cierre, el estudiante debería salir con un siguiente paso de aprendizaje claro.
