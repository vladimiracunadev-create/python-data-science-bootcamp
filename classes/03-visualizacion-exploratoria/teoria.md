# 🧠 Documento TeÃ³rico â€” Clase 03: VisualizaciÃ³n Exploratoria

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.


> **Nivel:** Principiante-Intermedio Â· **DuraciÃ³n estimada de lectura:** 25 minutos

---

## 1. Â¿Por quÃ© visualizar datos?

Una tabla con 10.000 filas no dice nada a simple vista. Un grÃ¡fico bien construido comunica el mismo insight en segundos.

### 1.1 CuÃ¡ndo usar cada grÃ¡fico

| GrÃ¡fico | Uso | CuÃ¡ndo lo elijo |
|---|---|---|
| **Histograma** | DistribuciÃ³n de 1 variable numÃ©rica | "Â¿CÃ³mo se distribuyen las ventas?" |
| **Boxplot** | DistribuciÃ³n + outliers + comparaciÃ³n | "Â¿Hay ventas anormalmente altas por sucursal?" |
| **Barras** | Comparar categorÃ­as | "Â¿QuÃ© sucursal vendiÃ³ mÃ¡s?" |
| **LÃ­nea** | Tendencia en el tiempo | "Â¿CÃ³mo evolucionaron las ventas?" |
| **Scatter** | RelaciÃ³n entre 2 variables numÃ©ricas | "Â¿El precio afecta las unidades vendidas?" |
| **Heatmap** | Correlaciones entre mÃºltiples variables | "Â¿QuÃ© variables estÃ¡n relacionadas?" |
| **Pie** | Proporciones de un todo | "Â¿QuÃ© % representa cada categorÃ­a?" (usar con moderaciÃ³n) |

---

## 2. Matplotlib â€” Fundamentos

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")

# Figura con ejes explÃ­citos (forma recomendada)
fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(df["total_neto"], bins=20, color="#22c55e", edgecolor="white", linewidth=0.5)
ax.set_title("DistribuciÃ³n de ventas netas", fontsize=14, fontweight="bold")
ax.set_xlabel("Total neto ($)")
ax.set_ylabel("Frecuencia")

plt.tight_layout()
plt.savefig("distribucion_ventas.png", dpi=150)
plt.show()
```

### 2.1 AnatomÃ­a de una figura matplotlib

```
Figure (contenedor principal)
â””â”€â”€ Axes (sistema de coordenadas con grÃ¡fico)
    â”œâ”€â”€ Title (tÃ­tulo)
    â”œâ”€â”€ X-axis (eje X con label y ticks)
    â”œâ”€â”€ Y-axis (eje Y con label y ticks)
    â”œâ”€â”€ LÃ­neas / Barras / Puntos (el grÃ¡fico en sÃ­)
    â””â”€â”€ Legend (leyenda)
```

---

## 3. Tipos de grÃ¡ficos y cuÃ¡ndo usarlos

### 3.1 Histograma â€” distribuciÃ³n de una variable

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histograma simple
axes[0].hist(df["total_neto"], bins=20, color="#22c55e", edgecolor="white")
axes[0].set_title("DistribuciÃ³n de ventas netas")

# Con KDE (lÃ­nea de densidad)
df["total_neto"].plot(kind="hist", ax=axes[1], bins=20,
    density=True, color="#3b82f6", edgecolor="white", alpha=0.7)
df["total_neto"].plot(kind="kde", ax=axes[1], color="white", lw=2)
axes[1].set_title("DistribuciÃ³n + densidad (KDE)")

plt.tight_layout()
plt.show()
```

### 3.2 Barras â€” comparar categorÃ­as

```python
ventas_sucursal = df.groupby("sucursal")["total_neto"].sum().sort_values(ascending=True)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(ventas_sucursal.index, ventas_sucursal.values,
    color="#22c55e", edgecolor="white", linewidth=0.5)

# Agregar etiquetas de valor
for bar in bars:
    ax.text(bar.get_width() + 1000, bar.get_y() + bar.get_height()/2,
        f"${bar.get_width():,.0f}", va="center", ha="left", fontsize=9)

ax.set_title("Ventas totales por sucursal")
ax.set_xlabel("Total ($)")
plt.tight_layout()
plt.show()
```

### 3.3 LÃ­nea â€” tendencia temporal

```python
ventas_mes = df.groupby("mes")["total_neto"].sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(ventas_mes.index, ventas_mes.values,
    marker="o", linewidth=2, color="#3b82f6",
    markersize=6, markerfacecolor="white", markeredgewidth=2)

ax.fill_between(ventas_mes.index, ventas_mes.values, alpha=0.1, color="#3b82f6")
ax.set_title("EvoluciÃ³n de ventas mensuales")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas ($)")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

### 3.4 Scatter â€” relaciÃ³n entre dos variables

```python
fig, ax = plt.subplots(figsize=(8, 5))

scatter = ax.scatter(df["precio_unitario"], df["unidades_vendidas"],
    c=df["total_neto"], cmap="YlGn",
    alpha=0.7, s=60, edgecolors="white", linewidth=0.5)

plt.colorbar(scatter, ax=ax, label="Total neto ($)")
ax.set_xlabel("Precio unitario ($)")
ax.set_ylabel("Unidades vendidas")
ax.set_title("Precio vs. Unidades vendidas (color = ventas totales)")
plt.tight_layout()
plt.show()
```

### 3.5 Boxplot â€” outliers y distribuciÃ³n comparada

```python
sucursales = df["sucursal"].unique()
datos_por_sucursal = [df[df["sucursal"] == s]["total_neto"] for s in sucursales]

fig, ax = plt.subplots(figsize=(10, 5))
bp = ax.boxplot(datos_por_sucursal, labels=sucursales, patch_artist=True)

colores = ["#22c55e", "#3b82f6", "#f59e0b", "#ef4444"]
for patch, color in zip(bp["boxes"], colores):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_title("DistribuciÃ³n de ventas por sucursal")
ax.set_ylabel("Total neto ($)")
plt.tight_layout()
plt.show()
```

---

## 4. Subplots â€” mÃºltiples grÃ¡ficos en una figura

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Dashboard EDA â€” Ventas Tienda", fontsize=16, fontweight="bold", y=1.01)

# GrÃ¡fico 1: distribuciÃ³n
axes[0, 0].hist(df["total_neto"], bins=15, color="#22c55e", edgecolor="white")
axes[0, 0].set_title("DistribuciÃ³n de ventas")

# GrÃ¡fico 2: barras
ventas = df.groupby("sucursal")["total_neto"].sum().sort_values()
axes[0, 1].barh(ventas.index, ventas.values, color="#3b82f6")
axes[0, 1].set_title("Ventas por sucursal")

# GrÃ¡fico 3: scatter
axes[1, 0].scatter(df["precio_unitario"], df["unidades_vendidas"], alpha=0.5, color="#f59e0b")
axes[1, 0].set_title("Precio vs. Unidades")

# GrÃ¡fico 4: boxplot
axes[1, 1].boxplot([df[df["sucursal"] == s]["total_neto"] for s in df["sucursal"].unique()])
axes[1, 1].set_title("Boxplot por sucursal")

plt.tight_layout()
plt.show()
```

---

## 5. Buenas prÃ¡cticas de visualizaciÃ³n

| PrÃ¡ctica | Por quÃ© importa |
|---|---|
| Siempre incluir tÃ­tulo | Sin tÃ­tulo, el grÃ¡fico es ambiguo |
| Etiquetar los ejes | El lector no sabe quÃ© se mide sin etiquetas |
| Indicar unidades | "$", "kg", "%" cambian la interpretaciÃ³n |
| No saturar de colores | MÃ¡s de 5-6 colores confunde |
| Usar colores con propÃ³sito | Rojo = alerta, verde = positivo, azul = neutro |
| Empezar el eje Y en 0 | Excepto cuando la variaciÃ³n es el foco |
| Fuente de datos | Indicar de dÃ³nde vienen los datos |

---

## 6. Paletas de colores recomendadas

```python
# Colores del bootcamp
VERDE    = "#22c55e"   # positivo, correcto
AZUL     = "#3b82f6"   # informativo, neutro
NARANJA  = "#f59e0b"   # advertencia
ROJO     = "#ef4444"   # error, negativo
MORADO   = "#8b5cf6"   # alternativa

# Paleta secuencial (para gradientes)
colores_seq = ["#bbf7d0", "#4ade80", "#22c55e", "#16a34a", "#166534"]

# Divergente (para correlaciones, positivo/negativo)
colores_div = ["#ef4444", "#fca5a5", "#f9fafb", "#86efac", "#22c55e"]
```

---

## ✅ 7. Resumen rÃ¡pido

```
âœ… fig, ax = plt.subplots() â†’ crear figura con ejes
âœ… ax.hist() â†’ distribuciÃ³n de una variable
âœ… ax.bar() / ax.barh() â†’ comparar categorÃ­as
âœ… ax.plot() â†’ tendencia temporal
âœ… ax.scatter() â†’ relaciÃ³n entre variables
âœ… ax.boxplot() â†’ distribuciÃ³n + outliers
âœ… plt.tight_layout() â†’ ajustar espaciado automÃ¡tico
âœ… plt.savefig() â†’ guardar como imagen
```
