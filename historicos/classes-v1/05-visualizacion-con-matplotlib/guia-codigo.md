# 💻 Guía de código — Clase 05: Visualización con matplotlib

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Gráfico improvisado vs. gráfico controlado

```python
import pandas as pd
import matplotlib.pyplot as plt

# Simulamos datos similares al dataset real
import numpy as np
meses = [f"2024-{str(i).zfill(2)}" for i in range(1, 7)]
clientes_activos = [320, 298, 345, 310, 360, 390]

# --- Forma improvisada (sin control) ---
plt.plot(meses, clientes_activos)
plt.show()

# --- Forma controlada (con Figure y Axes) ---
fig, ax = plt.subplots(figsize=(9, 4))          # Tamaño en pulgadas
ax.plot(meses, clientes_activos, marker="o", linewidth=2, color="steelblue")
ax.set_title("Clientes activos por mes", fontsize=14)
ax.set_xlabel("Mes")
ax.set_ylabel("Clientes activos")
ax.tick_params(axis="x", rotation=45)          # Rota etiquetas para que se lean
ax.grid(alpha=0.2)                              # Cuadrícula suave de fondo
plt.tight_layout()                             # Evita que etiquetas queden cortadas
plt.show()
```

**¿Qué hace este bloque?** Muestra la diferencia entre graficar con la API implícita de matplotlib (`plt.plot`) y la API orientada a objetos (`fig, ax`). La segunda permite controlar cada elemento por separado.

**¿Por qué se escribe así?** El patrón `fig, ax = plt.subplots()` es el estándar profesional porque permite manipular el gráfico con precisión después de crearlo, y escala bien cuando se necesitan múltiples subgráficos.

**Resultado esperado:** Dos ventanas (o celdas en Jupyter) con el mismo gráfico; el segundo visiblemente más legible, con tamaño controlado, marcadores en los puntos, etiquetas rotadas y cuadrícula sutil.

---

## Bloque 2: Cargar datos reales y graficar una serie temporal

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset real de retención de clientes
df = pd.read_csv("datasets/retencion_clientes.csv")

# Verificamos columnas disponibles antes de graficar
print(df.columns.tolist())
print(df.head(3))

# Creamos el gráfico con la figura explícita
fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(
    df["mes"],
    df["clientes_activos"],
    marker="o",
    linewidth=2,
    color="steelblue",
    label="Clientes activos"
)
ax.set_title("Clientes activos por mes — Dataset real")
ax.set_xlabel("Mes")
ax.set_ylabel("Número de clientes")
ax.tick_params(axis="x", rotation=45)
ax.grid(alpha=0.2)
ax.legend()           # Muestra la leyenda con el label del plot
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?** Lee el CSV real, inspecciona las columnas disponibles y luego construye un gráfico de serie temporal rotulado con leyenda.

**¿Por qué se escribe así?** Siempre se debe verificar `df.head()` y `df.columns` antes de graficar para evitar KeyError y confirmar que los datos tienen la forma esperada.

**Resultado esperado:** Un gráfico de línea con marcadores, eje X con los meses del dataset rotados 45°, eje Y con conteos de clientes y una leyenda en la esquina.

---

## Bloque 3: Agregar una línea de referencia y anotaciones

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/retencion_clientes.csv")

promedio = df["clientes_activos"].mean()   # Calculamos el promedio general

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(df["mes"], df["clientes_activos"], marker="o", linewidth=2, color="steelblue", label="Clientes activos")

# Línea horizontal de referencia
ax.axhline(
    y=promedio,
    color="tomato",
    linestyle="--",
    linewidth=1.5,
    label=f"Promedio: {promedio:.0f}"
)

ax.set_title("Clientes activos — con línea de promedio")
ax.set_xlabel("Mes")
ax.set_ylabel("Clientes activos")
ax.tick_params(axis="x", rotation=45)
ax.grid(alpha=0.2)
ax.legend()
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?** Calcula el promedio de clientes activos y lo dibuja como una línea horizontal punteada de color distinto al de la serie principal.

**¿Por qué se escribe así?** Las líneas de referencia (`axhline`) permiten al lector comparar inmediatamente si cada mes está por encima o debajo del promedio sin necesidad de calcular mentalmente. El `f-string` en el label muestra el valor exacto en la leyenda.

**Resultado esperado:** El mismo gráfico de línea, ahora con una línea punteada roja horizontal que indica el promedio y aparece explicada en la leyenda.

---

## Bloque 4: Guardar el gráfico como imagen

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/retencion_clientes.csv")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(df["mes"], df["clientes_activos"], marker="o", linewidth=2, color="steelblue")
ax.set_title("Clientes activos por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Clientes activos")
ax.tick_params(axis="x", rotation=45)
ax.grid(alpha=0.2)
plt.tight_layout()

# Guardar antes de mostrar (savefig ANTES de show)
fig.savefig("clientes_activos.png", dpi=150, bbox_inches="tight")
print("Gráfico guardado como clientes_activos.png")

plt.show()
```

**¿Qué hace este bloque?** Exporta el gráfico a un archivo PNG con resolución de 150 DPI apto para presentaciones.

**¿Por qué se escribe así?** `savefig` debe llamarse antes de `plt.show()` porque `show()` limpia el estado de la figura. El parámetro `bbox_inches="tight"` evita que las etiquetas rotadas queden cortadas en la imagen exportada.

**Resultado esperado:** El archivo `clientes_activos.png` aparece en la carpeta de trabajo con el gráfico completo y sin elementos cortados.

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `KeyError: 'mes'` al graficar | El nombre de la columna no coincide exactamente (mayúsculas, espacios) | Verificar con `df.columns.tolist()` antes de graficar |
| El gráfico aparece en blanco o no se muestra | Se llamó `plt.show()` antes de agregar los datos, o se usa `savefig` después de `show` | Asegurarse de que `savefig` va antes de `show` y de que los datos se asignan al `ax` correcto |
| Las etiquetas del eje X se superponen | Las cadenas son largas y el gráfico es estrecho | Usar `ax.tick_params(axis="x", rotation=45)` o reducir la cantidad de ticks con `ax.set_xticks` |
| `plt.title()` no afecta el gráfico esperado | Se mezcla la API implícita (`plt.*`) con la orientada a objetos (`ax.*`) | Usar siempre `ax.set_title()`, `ax.set_xlabel()`, etc. cuando se trabaja con `fig, ax` |
