# 🧠 Documento TeÃ³rico â€” Clase 04: EstadÃ­stica Descriptiva

> **Nivel:** Principiante-Intermedio Â· **DuraciÃ³n estimada de lectura:** 25 minutos

---

## 1. Â¿QuÃ© es la estadÃ­stica descriptiva?

La estadÃ­stica descriptiva **resume y describe** los datos sin hacer inferencias sobre una poblaciÃ³n mayor. Es el primer paso obligatorio de cualquier anÃ¡lisis.

### 1.1 Tipos de variables

| Tipo | Subtipo | DescripciÃ³n | Ejemplo |
|---|---|---|---|
| **Cuantitativa** | Continua | Toma cualquier valor en un rango | Ventas: $45.230,50 |
| **Cuantitativa** | Discreta | Solo valores enteros | Unidades vendidas: 3 |
| **Cualitativa** | Nominal | Sin orden | Sucursal: Norte, Sur |
| **Cualitativa** | Ordinal | Con orden | Nivel: Bajo, Medio, Alto |

---

## 2. Medidas de tendencia central

### 2.1 Media (promedio aritmÃ©tico)

La media es la suma de todos los valores dividida por el nÃºmero de observaciones.

```
xÌ„ = (xâ‚ + xâ‚‚ + ... + xâ‚™) / n
```

**Debilidad:** muy sensible a outliers.

```python
import pandas as pd

df = pd.read_csv("datasets/ventas_tienda.csv")
media = df["total_neto"].mean()
print(f"Media: ${media:,.2f}")
```

### 2.2 Mediana

El valor central cuando los datos estÃ¡n ordenados. **Robusta frente a outliers.**

```python
mediana = df["total_neto"].median()
```

### 2.3 Moda

El valor mÃ¡s frecuente. Ãštil para variables categÃ³ricas.

```python
moda = df["sucursal"].mode()[0]
```

### 2.4 ComparaciÃ³n: Media vs. Mediana

| SituaciÃ³n | RecomendaciÃ³n |
|---|---|
| DistribuciÃ³n simÃ©trica | Media y mediana son similares â†’ usar media |
| DistribuciÃ³n sesgada a la derecha | Mediana < media â†’ usar mediana |
| Muchos outliers | Mediana mÃ¡s representativa |
| Ingresos, precios de vivienda | Siempre usar mediana |
| Temperatura, altura | Media es apropiada |

---

## 3. Medidas de dispersiÃ³n

### 3.1 Rango

```
Rango = MÃ¡ximo - MÃ­nimo
```

Simple pero muy sensible a outliers.

### 3.2 Varianza y DesviaciÃ³n EstÃ¡ndar

La desviaciÃ³n estÃ¡ndar mide cuÃ¡nto se alejan los datos del promedio, **en las mismas unidades que los datos**.

```python
varianza = df["total_neto"].var()
desv_std = df["total_neto"].std()
print(f"DesviaciÃ³n estÃ¡ndar: ${desv_std:,.2f}")
```

### 3.3 Coeficiente de VariaciÃ³n (CV)

Compara la dispersiÃ³n entre variables con diferentes escalas:

```python
cv = df["total_neto"].std() / df["total_neto"].mean()
print(f"CV: {cv:.1%}")  # mientras mÃ¡s alto, mÃ¡s disperso
```

### 3.4 Cuartiles y Percentiles

Dividen los datos ordenados en partes iguales:

| Cuartil | Percentil | Significado |
|---|---|---|
| Q1 | P25 | 25% de los datos estÃ¡n por debajo |
| Q2 (Mediana) | P50 | 50% de los datos estÃ¡n por debajo |
| Q3 | P75 | 75% de los datos estÃ¡n por debajo |
| IQR = Q3 - Q1 | â€” | Rango intercuartÃ­lico (datos centrales) |

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

## 4. DetecciÃ³n de outliers

### 4.1 Regla del IQR (mÃ©todo Tukey)

Un valor es outlier si:
- EstÃ¡ por debajo de Q1 âˆ’ 1.5 Ã— IQR, o
- EstÃ¡ por encima de Q3 + 1.5 Ã— IQR

```python
limite_inferior = q1 - 1.5 * iqr
limite_superior = q3 + 1.5 * iqr

outliers = df[(df["total_neto"] < limite_inferior) | (df["total_neto"] > limite_superior)]
print(f"Outliers detectados: {len(outliers)}")
print(f"LÃ­mite inferior: ${limite_inferior:,.0f}")
print(f"LÃ­mite superior: ${limite_superior:,.0f}")
```

### 4.2 Regla de los 3 sigma (distribuciÃ³n normal)

Si los datos son aproximadamente normales: valor outlier si estÃ¡ a mÃ¡s de 3 desviaciones de la media.

```python
z_scores = (df["total_neto"] - df["total_neto"].mean()) / df["total_neto"].std()
outliers_zscore = df[abs(z_scores) > 3]
```

### 4.3 Â¿QuÃ© hacer con los outliers?

| SituaciÃ³n | AcciÃ³n |
|---|---|
| Error de entrada de datos | Corregir o eliminar |
| Caso legÃ­timo pero extremo | Mantener y documentar |
| Afecta el modelo significativamente | Crear variable indicadora `es_outlier` |
| Variable sesgada | Aplicar transformaciÃ³n (log, raÃ­z cuadrada) |

---

## 5. CorrelaciÃ³n

Mide la **fuerza y direcciÃ³n** de la relaciÃ³n lineal entre dos variables.

### 5.1 Coeficiente de Pearson

| Valor de r | InterpretaciÃ³n |
|---|---|
| 0.9 a 1.0 | CorrelaciÃ³n muy fuerte positiva |
| 0.7 a 0.9 | CorrelaciÃ³n fuerte positiva |
| 0.5 a 0.7 | CorrelaciÃ³n moderada positiva |
| 0.3 a 0.5 | CorrelaciÃ³n dÃ©bil positiva |
| 0.0 a 0.3 | CorrelaciÃ³n muy dÃ©bil o nula |
| Negativo | Misma interpretaciÃ³n en direcciÃ³n inversa |

```python
# CorrelaciÃ³n entre dos variables
r = df["precio_unitario"].corr(df["unidades_vendidas"])
print(f"CorrelaciÃ³n precio-unidades: {r:.3f}")

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

# Agregar valores numÃ©ricos
for i in range(len(corr)):
    for j in range(len(corr.columns)):
        ax.text(j, i, f"{corr.iloc[i, j]:.2f}",
            ha="center", va="center", fontsize=9,
            color="black" if abs(corr.iloc[i, j]) < 0.7 else "white")

plt.colorbar(im, ax=ax, label="CorrelaciÃ³n de Pearson")
ax.set_title("Mapa de correlaciones")
plt.tight_layout()
plt.show()
```

> âš ï¸ **CorrelaciÃ³n â‰  causalidad.** Dos variables pueden correlacionarse sin que una cause la otra.

---

## 6. AsimetrÃ­a y curtosis

| EstadÃ­stico | QuÃ© mide | Valores notables |
|---|---|---|
| **AsimetrÃ­a (skewness)** | DesviaciÃ³n de la simetrÃ­a | 0 = simÃ©trica, >0 = cola derecha, <0 = cola izquierda |
| **Curtosis (kurtosis)** | "Peso" de las colas | 0 = normal, >0 = colas pesadas, <0 = colas ligeras |

```python
asimetria = df["total_neto"].skew()
curtosis  = df["total_neto"].kurt()
print(f"AsimetrÃ­a: {asimetria:.3f}")
print(f"Curtosis:  {curtosis:.3f}")
```

---

## 7. Tabla resumen completa

```python
def estadisticas_completas(serie, nombre="Variable"):
    return pd.DataFrame({
        "EstadÃ­stico": [
            "N", "Media", "Mediana", "Moda",
            "MÃ­nimo", "MÃ¡ximo", "Rango",
            "Q1", "Q3", "IQR",
            "Desv. Std.", "CV",
            "AsimetrÃ­a", "Curtosis"
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
    }).set_index("EstadÃ­stico")

print(estadisticas_completas(df["total_neto"], "Total Neto"))
```

---

## 8. Resumen rÃ¡pido

```
âœ… Media â†’ promedio (sensible a outliers)
âœ… Mediana â†’ central (robusta a outliers)
âœ… Desv. std. â†’ dispersiÃ³n en mismas unidades que los datos
âœ… IQR â†’ dispersiÃ³n robusta (Q3 - Q1)
âœ… Outliers â†’ IQR Ã— 1.5 o Z-score > 3
âœ… CorrelaciÃ³n de Pearson â†’ relaciÃ³n lineal entre âˆ’1 y +1
âœ… AsimetrÃ­a â†’ forma de la distribuciÃ³n
```
