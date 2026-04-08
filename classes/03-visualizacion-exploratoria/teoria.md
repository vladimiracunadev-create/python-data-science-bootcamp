# Documento Teórico — Clase 03: Visualización Exploratoria

> **Nivel:** Principiante-Intermedio · **Duración estimada de lectura:** 25 minutos

---

## 1. ¿Por qué visualizar datos?

Una tabla con 10.000 filas no dice nada a simple vista. Un gráfico bien construido comunica el mismo insight en segundos.

### 1.1 Cuándo usar cada gráfico

| Gráfico | Uso | Cuándo lo elijo |
|---|---|---|
| **Histograma** | Distribución de 1 variable numérica | "¿Cómo se distribuyen las ventas?" |
| **Boxplot** | Distribución + outliers + comparación | "¿Hay ventas anormalmente altas por sucursal?" |
| **Barras** | Comparar categorías | "¿Qué sucursal vendió más?" |
| **Línea** | Tendencia en el tiempo | "¿Cómo evolucionaron las ventas?" |
| **Scatter** | Relación entre 2 variables numéricas | "¿El precio afecta las unidades vendidas?" |
| **Heatmap** | Correlaciones entre múltiples variables | "¿Qué variables están relacionadas?" |
| **Pie** | Proporciones de un todo | "¿Qué % representa cada categoría?" (usar con moderación) |

---

## 2. Matplotlib — Fundamentos

```python
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")

# Figura con ejes explícitos (forma recomendada)
fig, ax = plt.subplots(figsize=(10, 5))

ax.hist(df["total_neto"], bins=20, color="#22c55e", edgecolor="white", linewidth=0.5)
ax.set_title("Distribución de ventas netas", fontsize=14, fontweight="bold")
ax.set_xlabel("Total neto ($)")
ax.set_ylabel("Frecuencia")

plt.tight_layout()
plt.savefig("distribucion_ventas.png", dpi=150)
plt.show()
```

### 2.1 Anatomía de una figura matplotlib

```
Figure (contenedor principal)
└── Axes (sistema de coordenadas con gráfico)
    ├── Title (título)
    ├── X-axis (eje X con label y ticks)
    ├── Y-axis (eje Y con label y ticks)
    ├── Líneas / Barras / Puntos (el gráfico en sí)
    └── Legend (leyenda)
```

---

## 3. Tipos de gráficos y cuándo usarlos

### 3.1 Histograma — distribución de una variable

```python
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histograma simple
axes[0].hist(df["total_neto"], bins=20, color="#22c55e", edgecolor="white")
axes[0].set_title("Distribución de ventas netas")

# Con KDE (línea de densidad)
df["total_neto"].plot(kind="hist", ax=axes[1], bins=20,
    density=True, color="#3b82f6", edgecolor="white", alpha=0.7)
df["total_neto"].plot(kind="kde", ax=axes[1], color="white", lw=2)
axes[1].set_title("Distribución + densidad (KDE)")

plt.tight_layout()
plt.show()
```

### 3.2 Barras — comparar categorías

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

### 3.3 Línea — tendencia temporal

```python
ventas_mes = df.groupby("mes")["total_neto"].sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(ventas_mes.index, ventas_mes.values,
    marker="o", linewidth=2, color="#3b82f6",
    markersize=6, markerfacecolor="white", markeredgewidth=2)

ax.fill_between(ventas_mes.index, ventas_mes.values, alpha=0.1, color="#3b82f6")
ax.set_title("Evolución de ventas mensuales")
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas ($)")
ax.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()
```

### 3.4 Scatter — relación entre dos variables

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

### 3.5 Boxplot — outliers y distribución comparada

```python
sucursales = df["sucursal"].unique()
datos_por_sucursal = [df[df["sucursal"] == s]["total_neto"] for s in sucursales]

fig, ax = plt.subplots(figsize=(10, 5))
bp = ax.boxplot(datos_por_sucursal, labels=sucursales, patch_artist=True)

colores = ["#22c55e", "#3b82f6", "#f59e0b", "#ef4444"]
for patch, color in zip(bp["boxes"], colores):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)

ax.set_title("Distribución de ventas por sucursal")
ax.set_ylabel("Total neto ($)")
plt.tight_layout()
plt.show()
```

---

## 4. Subplots — múltiples gráficos en una figura

```python
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Dashboard EDA — Ventas Tienda", fontsize=16, fontweight="bold", y=1.01)

# Gráfico 1: distribución
axes[0, 0].hist(df["total_neto"], bins=15, color="#22c55e", edgecolor="white")
axes[0, 0].set_title("Distribución de ventas")

# Gráfico 2: barras
ventas = df.groupby("sucursal")["total_neto"].sum().sort_values()
axes[0, 1].barh(ventas.index, ventas.values, color="#3b82f6")
axes[0, 1].set_title("Ventas por sucursal")

# Gráfico 3: scatter
axes[1, 0].scatter(df["precio_unitario"], df["unidades_vendidas"], alpha=0.5, color="#f59e0b")
axes[1, 0].set_title("Precio vs. Unidades")

# Gráfico 4: boxplot
axes[1, 1].boxplot([df[df["sucursal"] == s]["total_neto"] for s in df["sucursal"].unique()])
axes[1, 1].set_title("Boxplot por sucursal")

plt.tight_layout()
plt.show()
```

---

## 5. Buenas prácticas de visualización

| Práctica | Por qué importa |
|---|---|
| Siempre incluir título | Sin título, el gráfico es ambiguo |
| Etiquetar los ejes | El lector no sabe qué se mide sin etiquetas |
| Indicar unidades | "$", "kg", "%" cambian la interpretación |
| No saturar de colores | Más de 5-6 colores confunde |
| Usar colores con propósito | Rojo = alerta, verde = positivo, azul = neutro |
| Empezar el eje Y en 0 | Excepto cuando la variación es el foco |
| Fuente de datos | Indicar de dónde vienen los datos |

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

## 7. Resumen rápido

```
✅ fig, ax = plt.subplots() → crear figura con ejes
✅ ax.hist() → distribución de una variable
✅ ax.bar() / ax.barh() → comparar categorías
✅ ax.plot() → tendencia temporal
✅ ax.scatter() → relación entre variables
✅ ax.boxplot() → distribución + outliers
✅ plt.tight_layout() → ajustar espaciado automático
✅ plt.savefig() → guardar como imagen
```
