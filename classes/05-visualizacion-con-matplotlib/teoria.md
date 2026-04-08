# 🧠 Documento TeÃ³rico â€” Clase 05: VisualizaciÃ³n Avanzada con Matplotlib

> **Nivel:** Intermedio Â· **DuraciÃ³n estimada de lectura:** 25 minutos

---

## 1. Matplotlib vs. otras bibliotecas

| Biblioteca | Fortaleza | CuÃ¡ndo usarla |
|---|---|---|
| **Matplotlib** | Control total, base de todo | GrÃ¡ficos personalizados, publicaciones |
| **Seaborn** | EstadÃ­stico, estÃ©tico, fÃ¡cil | EDA rÃ¡pido, distribuciones, heatmaps |
| **Plotly** | Interactivo | Dashboards, exploraciÃ³n online |
| **Altair** | Declarativo, limpio | Visualizaciones web |

En este bootcamp dominamos **matplotlib** porque es la base de todas las demÃ¡s.

---

## 2. Sistema de coordenadas y anatomÃ­a

```
Figure
â””â”€â”€ Axes (subplot)
    â”œâ”€â”€ Title
    â”œâ”€â”€ X-axis
    â”‚   â”œâ”€â”€ Label (xlabel)
    â”‚   â”œâ”€â”€ Ticks (marcas)
    â”‚   â””â”€â”€ Ticklabels (etiquetas de marcas)
    â”œâ”€â”€ Y-axis
    â”‚   â”œâ”€â”€ Label (ylabel)
    â”‚   â”œâ”€â”€ Ticks
    â”‚   â””â”€â”€ Ticklabels
    â”œâ”€â”€ Spine (bordes del grÃ¡fico)
    â”œâ”€â”€ Grid (cuadrÃ­cula)
    â”œâ”€â”€ Legend
    â””â”€â”€ Artist (lÃ­neas, barras, puntos, texto)
```

---

## 3. ConfiguraciÃ³n global de estilo

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

## 4. GrÃ¡ficos avanzados

### 4.1 GrÃ¡fico de lÃ­neas con anotaciones

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

# Anotar mÃ¡ximo
idx_max = ventas.idxmax()
ax.annotate(f"MÃ¡ximo\n${ventas[idx_max]/1000:.0f}K",
    xy=(idx_max, ventas[idx_max]/1000),
    xytext=(idx_max - 1.5, ventas[idx_max]/1000 + 5),
    fontsize=9, color="#22c55e",
    arrowprops=dict(arrowstyle="->", color="#22c55e", lw=1.5))

ax.set_title("EvoluciÃ³n de ventas mensuales â€” AÃ±o 2024")
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

### 4.3 Scatter con tamaÃ±o y color variable

```python
import pandas as pd
df = pd.read_csv("datasets/ventas_tienda.csv")

fig, ax = plt.subplots(figsize=(10, 6))

scatter = ax.scatter(
    df["precio_unitario"],
    df["unidades_vendidas"],
    c=df["total_neto"],
    s=df["descuento_pct"] * 10 + 20,   # tamaÃ±o segÃºn descuento
    cmap="YlGn",
    alpha=0.75,
    edgecolors="white",
    linewidth=0.4
)

plt.colorbar(scatter, ax=ax, label="Total neto ($)")
ax.set_xlabel("Precio unitario ($)")
ax.set_ylabel("Unidades vendidas")
ax.set_title("RelaciÃ³n precio-unidades\n(tamaÃ±o = descuento, color = venta total)")
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

## 5. Dashboard completo: mÃºltiples grÃ¡ficos

```python
fig = plt.figure(figsize=(16, 10))
fig.suptitle("Dashboard de Ventas â€” Vista Ejecutiva", fontsize=16, fontweight="bold")

# Layout con GridSpec
gs = fig.add_gridspec(2, 3, hspace=0.4, wspace=0.35)

ax1 = fig.add_subplot(gs[0, :2])   # fila 0, columnas 0-1
ax2 = fig.add_subplot(gs[0, 2])    # fila 0, columna 2
ax3 = fig.add_subplot(gs[1, 0])    # fila 1, columna 0
ax4 = fig.add_subplot(gs[1, 1])    # fila 1, columna 1
ax5 = fig.add_subplot(gs[1, 2])    # fila 1, columna 2

# ax1: tendencia temporal (grande)
# ax2: top categorÃ­as (barras)
# ax3: distribuciÃ³n (histograma)
# ax4: scatter precio-unidades
# ax5: boxplot por sucursal

plt.savefig("dashboard_ventas.png", dpi=150, bbox_inches="tight")
plt.show()
```

---

## 6. Guardar para reportes

```python
# Alta resoluciÃ³n para impresiÃ³n
plt.savefig("grafico.png", dpi=300, bbox_inches="tight", transparent=False)

# PDF vectorial (ideal para documentos)
plt.savefig("grafico.pdf", bbox_inches="tight")

# SVG (escalable para web)
plt.savefig("grafico.svg", bbox_inches="tight")
```

---

## 7. Checklist de visualizaciÃ³n profesional

| âœ… Elemento | DescripciÃ³n |
|---|---|
| TÃ­tulo descriptivo | Comunica el insight, no solo "Ventas mensuales" |
| Ejes etiquetados | Siempre con unidades |
| Fuente legible | MÃ­nimo 10pt en el grÃ¡fico final |
| Escala apropiada | Eje Y desde 0 si muestra magnitud |
| Colores con propÃ³sito | Accesibles para daltÃ³nicos |
| Sin elementos innecesarios | Eliminar bordes, grids excesivos |
| Leyenda clara | Fuera del grÃ¡fico si tapa datos |

---

## 8. Resumen rÃ¡pido

```
âœ… mpl.rcParams â†’ configurar estilo global
âœ… GridSpec â†’ layout complejo de subplots
âœ… ax.annotate() â†’ anotaciones en el grÃ¡fico
âœ… scatter(c=, s=) â†’ codificar 3Âª y 4Âª dimensiÃ³n en scatter
âœ… ax.bar(bottom=) â†’ barras apiladas
âœ… plt.savefig(dpi=300) â†’ exportar en alta resoluciÃ³n
```
