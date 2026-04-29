# 💻 Guía de código — Clase 08: Presentación de hallazgos

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Construir el resumen ejecutivo en texto

```python
import pandas as pd

# Cargamos y preparamos los datos del mini proyecto
df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])
df["categoría"]  = df["categoría"].str.strip().str.lower()

# Calculamos el ranking para obtener el dato concreto
ranking = (
    df.groupby("categoría")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
ranking.columns = ["categoría", "ingreso_neto_total"]

# Identificamos la categoría ganadora de forma programática (no hardcodeada)
ganadora   = ranking.iloc[0]["categoría"].title()
monto      = ranking.iloc[0]["ingreso_neto_total"]
porcentaje = monto / ranking["ingreso_neto_total"].sum() * 100

# Construimos el resumen ejecutivo con valores reales
hallazgo      = f"La categoría {ganadora} concentra el mayor ingreso neto del período."
evidencia     = f"Representa ${monto:,.0f} ({porcentaje:.1f}% del total), encabezando el ranking de categorías."
recomendacion = "Conviene revisar margen, stock y campañas antes de ampliar la oferta en esa categoría."

print("=== RESUMEN EJECUTIVO ===")
print(hallazgo)
print(evidencia)
print(recomendacion)
```

**¿Qué hace este bloque?** Extrae el hallazgo principal del ranking de manera programática (sin hardcodear el nombre de la categoría) y lo convierte en tres oraciones ejecutivas: hallazgo, evidencia cuantitativa y recomendación.

**¿Por qué se escribe así y no de otra forma?** Usar `ranking.iloc[0]` en lugar de escribir el nombre de la categoría directamente hace que el resumen se actualice automáticamente si los datos cambian. El f-string con `{monto:,.0f}` formatea el número con separadores de miles y sin decimales, lo que facilita la lectura a una audiencia no técnica.

**Resultado esperado:**
```
=== RESUMEN EJECUTIVO ===
La categoría Electrónica concentra el mayor ingreso neto del período.
Representa $285,400 (38.2% del total), encabezando el ranking de categorías.
Conviene revisar margen, stock y campañas antes de ampliar la oferta en esa categoría.
```

---

## Bloque 2: Gráfico de presentación con categoría destacada

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])
df["categoría"]  = df["categoría"].str.strip().str.lower()

ranking = (
    df.groupby("categoría")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
ranking.columns = ["categoría", "ingreso_neto_total"]

# Asignamos un color distinto a la categoría ganadora para que destaque
colores = [
    "steelblue" if i > 0 else "tomato"
    for i in range(len(ranking))
]

fig, ax = plt.subplots(figsize=(9, 4))
ax.barh(ranking["categoría"], ranking["ingreso_neto_total"], color=colores)
ax.invert_yaxis()

# Título descriptivo con el hallazgo incorporado — el gráfico se explica solo
ax.set_title("Electrónica lidera el ingreso neto por categoría", fontsize=13, fontweight="bold")
ax.set_xlabel("Ingreso neto total ($)")
ax.grid(axis="x", alpha=0.2)
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?** Crea un gráfico de barras horizontales donde la categoría ganadora se colorea en rojo (`tomato`) para que el ojo del lector la identifique de inmediato sin necesidad de leer todos los valores.

**¿Por qué se escribe así y no de otra forma?** La lista `colores` se construye con una comprensión de lista que aplica `"tomato"` solo al índice 0 (la categoría mayor) y `"steelblue"` al resto. El título incorpora el hallazgo directamente, siguiendo el principio de storytelling: el título dice la conclusión, el gráfico muestra la evidencia.

**Resultado esperado:**
```
Gráfico de barras horizontales con la primera barra (Electrónica) en rojo
y las demás en azul acero. El título ya enuncia la conclusión del análisis.
```

---

## Bloque 3: Agregar anotaciones para reforzar el mensaje

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])
df["categoría"]  = df["categoría"].str.strip().str.lower()

ranking = (
    df.groupby("categoría")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
ranking.columns = ["categoría", "ingreso_neto_total"]
ranking["porcentaje"] = (ranking["ingreso_neto_total"] / ranking["ingreso_neto_total"].sum() * 100).round(1)

colores = ["tomato" if i == 0 else "steelblue" for i in range(len(ranking))]

fig, ax = plt.subplots(figsize=(10, 4))
barras = ax.barh(ranking["categoría"], ranking["ingreso_neto_total"], color=colores)
ax.invert_yaxis()

# Agregamos el porcentaje como etiqueta al final de cada barra
for barra, pct in zip(barras, ranking["porcentaje"]):
    ancho = barra.get_width()
    ax.text(
        ancho + 1000,                # Posición X: ligeramente a la derecha de la barra
        barra.get_y() + barra.get_height() / 2,  # Posición Y: centro vertical de la barra
        f"{pct}%",
        va="center",
        fontsize=9
    )

ax.set_title("Electrónica lidera el ingreso neto por categoría", fontsize=13, fontweight="bold")
ax.set_xlabel("Ingreso neto total ($)")
ax.grid(axis="x", alpha=0.2)
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?** Agrega el porcentaje de participación como etiqueta de texto al final de cada barra, permitiendo que el lector compare proporciones sin necesidad de leer el eje X.

**¿Por qué se escribe así y no de otra forma?** `barra.get_width()` devuelve el valor numérico de cada barra; sumarle un offset fijo (`+1000`) posiciona la etiqueta levemente a la derecha del extremo. `va="center"` centra verticalmente el texto respecto a la barra. Este patrón es reutilizable para cualquier gráfico de barras horizontales.

**Resultado esperado:**
```
Gráfico de barras con porcentajes visibles a la derecha de cada barra:
Electrónica  ████████████████████  38.2%
Accesorios   ██████████████        26.6%
Ropa         ██████████            20.7%
...
```

---

## Bloque 4: Exportar el gráfico listo para presentación

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")
df["total_neto"] = df["unidades"] * df["precio_unitario"] * (1 - df["descuento_pct"])
df["categoría"]  = df["categoría"].str.strip().str.lower()

ranking = (
    df.groupby("categoría")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
ranking.columns = ["categoría", "ingreso_neto_total"]
ranking["porcentaje"] = (ranking["ingreso_neto_total"] / ranking["ingreso_neto_total"].sum() * 100).round(1)

colores = ["tomato" if i == 0 else "steelblue" for i in range(len(ranking))]

fig, ax = plt.subplots(figsize=(10, 4))
barras = ax.barh(ranking["categoría"], ranking["ingreso_neto_total"], color=colores)
ax.invert_yaxis()

for barra, pct in zip(barras, ranking["porcentaje"]):
    ax.text(
        barra.get_width() + 1000,
        barra.get_y() + barra.get_height() / 2,
        f"{pct}%",
        va="center",
        fontsize=9
    )

ax.set_title("Electrónica lidera el ingreso neto por categoría", fontsize=13, fontweight="bold")
ax.set_xlabel("Ingreso neto total ($)")
ax.grid(axis="x", alpha=0.2)
plt.tight_layout()

# Guardamos con alta resolución para insertarlo en diapositivas o informes
fig.savefig("hallazgo_categorias.png", dpi=180, bbox_inches="tight")
print("Gráfico guardado: hallazgo_categorias.png")

plt.show()
```

**¿Qué hace este bloque?** Exporta el gráfico final a un archivo PNG de alta resolución listo para insertar en PowerPoint, Canva o un informe PDF.

**¿Por qué se escribe así y no de otra forma?** `dpi=180` produce una imagen nítida sin ser excesivamente pesada. `bbox_inches="tight"` garantiza que las etiquetas de porcentaje y el título no queden cortados al exportar. `savefig` debe llamarse antes de `plt.show()` porque `show()` limpia el estado de la figura.

**Resultado esperado:**
```
Gráfico guardado: hallazgo_categorias.png
(Archivo PNG de ~150 KB con resolución adecuada para proyección o impresión)
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| Las etiquetas de porcentaje quedan fuera del área visible | El offset `+1000` es mayor que el margen disponible del gráfico | Ajustar el límite del eje X con `ax.set_xlim(0, ranking["ingreso_neto_total"].max() * 1.15)` |
| El gráfico exportado sale en blanco | `savefig` se llamó después de `plt.show()` | Siempre llamar `fig.savefig()` antes de `plt.show()` |
| El título hardcodeado no coincide con los datos reales | Se escribió el nombre de la categoría directamente en lugar de obtenerlo del ranking | Construir el título con `f-string` usando `ranking.iloc[0]["categoría"].title()` |
| Las barras no aparecen ordenadas de mayor a menor | Se graficó antes de ordenar el ranking | Asegurarse de que `sort_values(ascending=False)` se aplica antes de crear el gráfico |
| El resumen ejecutivo muestra `NaN` en el monto | La columna `descuento_pct` tiene valores nulos que propagan `NaN` al calcular `total_neto` | Agregar `df["descuento_pct"].fillna(0)` antes de la multiplicación |
