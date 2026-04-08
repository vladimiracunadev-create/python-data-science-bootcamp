# Documento Teórico — Clase 04: Estadística Descriptiva

> **Nivel:** Principiante-Intermedio · **Duración estimada de lectura:** 25 minutos

---

## 1. ¿Qué es la estadística descriptiva?

La estadística descriptiva **resume y describe** los datos sin hacer inferencias sobre una población mayor. Es el primer paso obligatorio de cualquier análisis.

### 1.1 Tipos de variables

| Tipo | Subtipo | Descripción | Ejemplo |
|---|---|---|---|
| **Cuantitativa** | Continua | Toma cualquier valor en un rango | Ventas: $45.230,50 |
| **Cuantitativa** | Discreta | Solo valores enteros | Unidades vendidas: 3 |
| **Cualitativa** | Nominal | Sin orden | Sucursal: Norte, Sur |
| **Cualitativa** | Ordinal | Con orden | Nivel: Bajo, Medio, Alto |

---

## 2. Medidas de tendencia central

### 2.1 Media (promedio aritmético)

La media es la suma de todos los valores dividida por el número de observaciones.

```
x̄ = (x₁ + x₂ + ... + xₙ) / n
```

**Debilidad:** muy sensible a outliers.

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
media = df["total_neto"].mean()
print(f"Media: ${media:,.2f}")
```

### 2.2 Mediana

El valor central cuando los datos están ordenados. **Robusta frente a outliers.**

```python
mediana = df["total_neto"].median()
```

### 2.3 Moda

El valor más frecuente. Útil para variables categóricas.

```python
moda = df["sucursal"].mode()[0]
```

### 2.4 Comparación: Media vs. Mediana

| Situación | Recomendación |
|---|---|
| Distribución simétrica | Media y mediana son similares → usar media |
| Distribución sesgada a la derecha | Mediana < media → usar mediana |
| Muchos outliers | Mediana más representativa |
| Ingresos, precios de vivienda | Siempre usar mediana |
| Temperatura, altura | Media es apropiada |

---

## 3. Medidas de dispersión

### 3.1 Rango

```
Rango = Máximo - Mínimo
```

Simple pero muy sensible a outliers.

### 3.2 Varianza y Desviación Estándar

La desviación estándar mide cuánto se alejan los datos del promedio, **en las mismas unidades que los datos**.

```python
varianza = df["total_neto"].var()
desv_std = df["total_neto"].std()
print(f"Desviación estándar: ${desv_std:,.2f}")
```

### 3.3 Coeficiente de Variación (CV)

Compara la dispersión entre variables con diferentes escalas:

```python
cv = df["total_neto"].std() / df["total_neto"].mean()
print(f"CV: {cv:.1%}")  # mientras más alto, más disperso
```

### 3.4 Cuartiles y Percentiles

Dividen los datos ordenados en partes iguales:

| Cuartil | Percentil | Significado |
|---|---|---|
| Q1 | P25 | 25% de los datos están por debajo |
| Q2 (Mediana) | P50 | 50% de los datos están por debajo |
| Q3 | P75 | 75% de los datos están por debajo |
| IQR = Q3 - Q1 | — | Rango intercuartílico (datos centrales) |

```python
q1   = df["total_neto"].quantile(0.25)
q2   = df["total_neto"].quantile(0.50)  # mediana
q3   = df["total_neto"].quantile(0.75)
iqr  = q3 - q1
p90  = df["total_neto"].quantile(0.90)

print(f"Q1:  ${q1:,.0f}")
print(f"Q2:  ${q2:,.0f}")
print(f"Q3:  ${q3:,.0f}")
print(f"IQR: ${iqr:,.0f}")
print(f"P90: ${p90:,.0f}")
```

---

## 4. Detección de outliers

### 4.1 Regla del IQR (método Tukey)

Un valor es outlier si:
- Está por debajo de Q1 − 1.5 × IQR, o
- Está por encima de Q3 + 1.5 × IQR

```python
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = df[(df["total_neto"] < limite_inferior) | (df["total_neto"] > limite_superior)]
print(f"Outliers detectados: {len(outliers)}")
print(f"Límite inferior: ${limite_inferior:,.0f}")
print(f"Límite superior: ${limite_superior:,.0f}")
```

### 4.2 Regla de los 3 sigma (distribución normal)

Si los datos son aproximadamente normales: valor outlier si está a más de 3 desviaciones de la media.

```python
z_scores = (df["total_neto"] - df["total_neto"].mean()) / df["total_neto"].std()
outliers_zscore = df[abs(z_scores) > 3]
```

### 4.3 ¿Qué hacer con los outliers?

| Situación | Acción |
|---|---|
| Error de entrada de datos | Corregir o eliminar |
| Caso legítimo pero extremo | Mantener y documentar |
| Afecta el modelo significativamente | Crear variable indicadora `es_outlier` |
| Variable sesgada | Aplicar transformación (log, raíz cuadrada) |

---

## 5. Correlación

Mide la **fuerza y dirección** de la relación lineal entre dos variables.

### 5.1 Coeficiente de Pearson

| Valor de r | Interpretación |
|---|---|
| 0.9 a 1.0 | Correlación muy fuerte positiva |
| 0.7 a 0.9 | Correlación fuerte positiva |
| 0.5 a 0.7 | Correlación moderada positiva |
| 0.3 a 0.5 | Correlación débil positiva |
| 0.0 a 0.3 | Correlación muy débil o nula |
| Negativo | Misma interpretación en dirección inversa |

```python
# Correlación entre dos variables
r = df["precio_unitario"].corr(df["unidades_vendidas"])
print(f"Correlación precio-unidades: {r:.3f}")

# Matriz de correlaciones
correlaciones = df.select_dtypes(include="number").corr()
print(correlaciones.round(2))
```

### 5.2 Visualizar correlaciones

```python
import matplotlib.pyplot as plt
import numpy as np

corr = df.select_dtypes(include="number").corr()

fig, ax = plt.subplots(figsize=(9, 7))
im = ax.imshow(corr, cmap="RdYlGn", vmin=-1, vmax=1, aspect="auto")

ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticklabels(corr.columns)

# Agregar valores numéricos
for i in range(len(corr)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
            ha="center", va="center", fontsize=9,
            color="black" if abs(corr.iloc[i, j]) < 0.7 else "white")

plt.colorbar(im, ax=ax, label="Correlación de Pearson")
ax.set_title("Mapa de correlaciones")
plt.tight_layout()
plt.show()
```

> ⚠️ **Correlación ≠ causalidad.** Dos variables pueden correlacionarse sin que una cause la otra.

---

## 6. Asimetría y curtosis

| Estadístico | Qué mide | Valores notables |
|---|---|---|
| **Asimetría (skewness)** | Desviación de la simetría | 0 = simétrica, >0 = cola derecha, <0 = cola izquierda |
| **Curtosis (kurtosis)** | "Peso" de las colas | 0 = normal, >0 = colas pesadas, <0 = colas ligeras |

```python
asimetria = df["total_neto"].skew()
curtosis  = df["total_neto"].kurt()
print(f"Asimetría: {asimetria:.3f}")
print(f"Curtosis:  {curtosis:.3f}")
```

---

## 7. Tabla resumen completa

```python
def estadisticas_completas(serie, nombre="Variable"):
    return pd.DataFrame({
        "Estadístico": [
            "N", "Media", "Mediana", "Moda",
            "Mínimo", "Máximo", "Rango",
            "Q1", "Q3", "IQR",
            "Desv. Std.", "CV",
            "Asimetría", "Curtosis"
        ],
        "Valor": [
            serie.count(),
            f"${serie.mean():,.2f}",
            f"${serie.median():,.2f}",
            f"${serie.mode()[0]:,.2f}",
            f"${serie.min():,.2f}",
            f"${serie.max():,.2f}",
            f"${serie.max() - serie.min():,.2f}",
            f"${serie.quantile(0.25):,.2f}",
            f"${serie.quantile(0.75):,.2f}",
            f"${serie.quantile(0.75) - serie.quantile(0.25):,.2f}",
            f"${serie.std():,.2f}",
            f"{serie.std() / serie.mean():.1%}",
            f"{serie.skew():.3f}",
            f"{serie.kurt():.3f}"
        ]
    }).set_index("Estadístico")

print(estadisticas_completas(df["total_neto"], "Total Neto"))
```

---

## 8. Resumen rápido

```
✅ Media → promedio (sensible a outliers)
✅ Mediana → central (robusta a outliers)
✅ Desv. std. → dispersión en mismas unidades que los datos
✅ IQR → dispersión robusta (Q3 - Q1)
✅ Outliers → IQR × 1.5 o Z-score > 3
✅ Correlación de Pearson → relación lineal entre −1 y +1
✅ Asimetría → forma de la distribución
```
