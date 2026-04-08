# Documento Teórico — Clase 05: Visualización Avanzada con Matplotlib

> **Nivel:** Intermedio · **Duración estimada de lectura:** 25 minutos

---

## 1. Matplotlib vs. otras bibliotecas

| Biblioteca | Fortaleza | Cuándo usarla |
|---|---|---|
| **Matplotlib** | Control total, base de todo | Gráficos personalizados, publicaciones |
| **Seaborn** | Estadístico, estético, fácil | EDA rápido, distribuciones, heatmaps |
| **Plotly** | Interactivo | Dashboards, exploración online |
| **Altair** | Declarativo, limpio | Visualizaciones web |

En este bootcamp dominamos **matplotlib** porque es la base de todas las demás.

---

## 2. Sistema de coordenadas y anatomía

```
Figure
└── Axes (subplot)
    ├── Title
    ├── X-axis
    │   ├── Label (xlabel)
    │   ├── Ticks (marcas)
    │   └── Ticklabels (etiquetas de marcas)
    ├── Y-axis
    │   ├── Label (ylabel)
    │   ├── Ticks
    │   └── Ticklabels
    ├── Spine (bordes del gráfico)
    ├── Grid (cuadrícula)
    ├── Legend
    └── Artist (líneas, barras, puntos, texto)
```

---

## 3. Configuración global de estilo

```python
import matplotlib.pyplot as plt
import matplotlib as mpl

# Estilo oscuro profesional
plt.style.use("dark_background")

# O configurar manualmente
mpl.rcParams.update({
    "figure.facecolor":  "#0f172a",
    "axes.facecolor":    "#111827",
    "axes.edgecolor":    "#334155",
    "axes.labelcolor":   "#e5e7eb",
    "xtick.color":       "#94a3b8",
    "ytick.color":       "#94a3b8",
    "text.color":        "#e5e7eb",
    "grid.color":        "#334155",
    "grid.alpha":        0.4,
    "font.family":       "sans-serif",
    "font.size":         11,
    "axes.titlesize":    13,
    "axes.titleweight":  "bold",
    "figure.dpi":        120,
})
```

---

## 4. Gráficos avanzados

### 4.1 Gráfico de líneas con anotaciones

```python
import pandas as pd
import numpy as np

ventas = pd.Series([45000, 52000, 38000, 67000, 71000, 85000, 62000, 91000, 78000, 95000, 88000, 102000],
    index=range(1, 13), name="Ventas")

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(ventas.index, ventas.values / 1000,
    color="#22c55e", linewidth=2.5, marker="o",
    markersize=6, markerfacecolor="#0f172a", markeredgewidth=2)

ax.fill_between(ventas.index, ventas.values / 1000,
    alpha=0.1, color="#22c55e")

# Anotar máximo
idx_max = ventas.idxmax()
ax.annotate(f"Máximo\n${ventas[idx_max]/1000:.0f}K",
    xy=(idx_max, ventas[idx_max]/1000),
    xytext=(idx_max - 1.5, ventas[idx_max]/1000 + 5),
    fontsize=9, color="#22c55e",
    arrowprops=dict(arrowstyle="->", color="#22c55e", lw=1.5))

ax.set_title("Evolución de ventas mensuales — Año 2024")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas (miles $)")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"])
ax.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()
```

### 4.2 Barras apiladas

```python
sucursales = ["Norte", "Sur", "Centro", "Oriente"]
productos   = ["Mouse", "Teclado", "Webcam"]
datos = {
    "Mouse":   [45000, 32000, 67000, 21000],
    "Teclado": [28000, 41000, 38000, 35000],
    "Webcam":  [12000, 18000, 25000, 9000],
}

colores = ["#22c55e", "#3b82f6", "#f59e0b"]
bottoms = [0] * len(sucursales)

fig, ax = plt.subplots(figsize=(10, 5))

for producto, color in zip(productos, colores):
    valores = datos[producto]
    bars = ax.bar(sucursales, valores, bottom=bottoms,
        label=producto, color=color, edgecolor="white", linewidth=0.5)
    bottoms = [b + v for b, v in zip(bottoms, valores)]

ax.set_title("Ventas por sucursal y producto")
ax.set_ylabel("Ventas ($)")
ax.legend(title="Producto", bbox_to_anchor=(1.01, 1))
plt.tight_layout()
plt.show()
```

### 4.3 Scatter con tamaño y color variable

```python
import pandas as pd
df = pd.read_csv("datasets/ventas_tienda.csv")

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(
    df["precio_unitario"],
    df["unidades_vendidas"],
    c=df["total_neto"],
    s=df["descuento_pct"] * 10 + 20,   # tamaño según descuento
    cmap="YlGn",
    alpha=0.75,
    edgecolors="white",
    linewidth=0.4
)

plt.colorbar(scatter, ax=ax, label="Total neto ($)")
ax.set_xlabel("Precio unitario ($)")
ax.set_ylabel("Unidades vendidas")
ax.set_title("Relación precio-unidades\n(tamaño = descuento, color = venta total)")
plt.tight_layout()
plt.show()
```

### 4.4 Heatmap desde cero

```python
corr = df.select_dtypes(include="number").corr()
n = len(corr)

fig, ax = plt.subplots(figsize=(n + 2, n))

im = ax.imshow(corr.values, cmap="RdYlGn", vmin=-1, vmax=1, aspect="auto")

ax.set_xticks(range(n))
ax.set_yticks(range(n))
ax.set_xticklabels(corr.columns, rotation=45, ha="right", fontsize=9)
ax.set_yticklabels(corr.columns, fontsize=9)

for i in range(n):
    for j in range(n):
        val = corr.iloc[i, j]
        color = "black" if abs(val) < 0.6 else "white"
        ax.text(j, i, f"{val:.2f}", ha="center", va="center",
            fontsize=8, color=color, fontweight="bold")

plt.colorbar(im, ax=ax)
ax.set_title("Mapa de correlaciones")
plt.tight_layout()
plt.show()
```

---

## 5. Dashboard completo: múltiples gráficos

```python
fig = plt.figure(figsize=(16, 10))
fig.suptitle("Dashboard de Ventas — Vista Ejecutiva", fontsize=16, fontweight="bold")

# Layout con GridSpec
gs = fig.add_gridspec(2, 3, hspace=0.4, wspace=0.35)

ax1 = fig.add_subplot(gs[0, :2])   # fila 0, columnas 0-1
ax2 = fig.add_subplot(gs[0, 2])    # fila 0, columna 2
ax3 = fig.add_subplot(gs[1, 0])    # fila 1, columna 0
ax4 = fig.add_subplot(gs[1, 1])    # fila 1, columna 1
ax5 = fig.add_subplot(gs[1, 2])    # fila 1, columna 2

# ax1: tendencia temporal (grande)
# ax2: top categorías (barras)
# ax3: distribución (histograma)
# ax4: scatter precio-unidades
# ax5: boxplot por sucursal

plt.savefig("dashboard_ventas.png", dpi=150, bbox_inches="tight")
plt.show()
```

---

## 6. Guardar para reportes

```python
# Alta resolución para impresión
plt.savefig("grafico.png", dpi=300, bbox_inches="tight", transparent=False)

# PDF vectorial (ideal para documentos)
plt.savefig("grafico.pdf", bbox_inches="tight")

# SVG (escalable para web)
plt.savefig("grafico.svg", bbox_inches="tight")
```

---

## 7. Checklist de visualización profesional

| ✅ Elemento | Descripción |
|---|---|
| Título descriptivo | Comunica el insight, no solo "Ventas mensuales" |
| Ejes etiquetados | Siempre con unidades |
| Fuente legible | Mínimo 10pt en el gráfico final |
| Escala apropiada | Eje Y desde 0 si muestra magnitud |
| Colores con propósito | Accesibles para daltónicos |
| Sin elementos innecesarios | Eliminar bordes, grids excesivos |
| Leyenda clara | Fuera del gráfico si tapa datos |

---

## 8. Resumen rápido

```
✅ mpl.rcParams → configurar estilo global
✅ GridSpec → layout complejo de subplots
✅ ax.annotate() → anotaciones en el gráfico
✅ scatter(c=, s=) → codificar 3ª y 4ª dimensión en scatter
✅ ax.bar(bottom=) → barras apiladas
✅ plt.savefig(dpi=300) → exportar en alta resolución
```
