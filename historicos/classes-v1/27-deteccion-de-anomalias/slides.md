# 🎞️ Slides — Clase 27: Detección de Anomalías

---

## Slide 1 — ¿Qué problema resolvemos hoy?

Imagina que eres gerente de una tienda. Un día las ventas son 10 veces mayores de lo normal.
¿Es un error? ¿Una promoción viral? ¿Un fraude?

**Detectar lo inusual es tan importante como entender lo normal.**

---

## Slide 2 — Anomalía vs Outlier

| Concepto | Definición | Ejemplo |
|---|---|---|
| **Outlier** | Valor estadísticamente extremo | Venta de $50,000 cuando el promedio es $500 |
| **Anomalía** | Comportamiento inesperado en contexto | Transacción bancaria a las 3am en otro país |

> 💡 Todo outlier puede ser una anomalía, pero no toda anomalía es un outlier estadístico.
> Una compra de $20 puede ser anómala si siempre compras $200.

---

## Slide 3 — Ejemplos del mundo real

- **Banca:** transacción en un país diferente minutos después de una compra local
- **Manufactura:** temperatura de una máquina fuera del rango habitual
- **Salud:** frecuencia cardíaca inusualmente baja a las 2pm
- **E-commerce:** producto con 500 reseñas en un día (reseñas falsas)
- **Transporte:** tiempo de entrega 5 veces mayor al habitual

---

## Slide 4 — Método 1: Regla del IQR

```
Q1 = percentil 25
Q3 = percentil 75
IQR = Q3 - Q1

Límite inferior = Q1 - 1.5 × IQR
Límite superior = Q3 + 1.5 × IQR

Todo lo que quede fuera = posible anomalía
```

```python
Q1 = df['total_neto'].quantile(0.25)
Q3 = df['total_neto'].quantile(0.75)
IQR = Q3 - Q1

anomalias = df[(df['total_neto'] < Q1 - 1.5*IQR) |
               (df['total_neto'] > Q3 + 1.5*IQR)]
```

---

## Slide 5 — Método 2: Z-score

```
z = (x - media) / desviación_estándar

Si |z| > 3 → anomalía (está a más de 3 desviaciones de la media)
```

```python
from scipy import stats

z_scores = stats.zscore(df['total_neto'])
anomalias = df[abs(z_scores) > 3]
```

> ⚠️ El Z-score asume distribución normal. El IQR es más robusto con datos sesgados.

---

## Slide 6 — Método 3: Isolation Forest

Idea: las anomalías son más fáciles de aislar con cortes aleatorios.

```
Imagina un bosque de árboles de decisión al azar.
Los puntos normales necesitan MUCHOS cortes para quedar solos.
Los puntos anómalos quedan solos muy rápido.
```

```python
from sklearn.ensemble import IsolationForest

iso = IsolationForest(contamination=0.05, random_state=42)
df['anomalia_iso'] = iso.fit_predict(df[['total_neto']])
# -1 = anomalía, 1 = normal
```

---

## Slide 7 — Método 4: Local Outlier Factor (LOF)

Idea: un punto es anómalo si su densidad local es mucho menor que la de sus vecinos.

```
Punto normal: está rodeado de vecinos cercanos (alta densidad).
Anomalía: sus vecinos están muy lejos (baja densidad local).
```

```python
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(n_neighbors=20, contamination=0.05)
df['anomalia_lof'] = lof.fit_predict(df[['retraso_min']])
```

LOF es especialmente bueno cuando las anomalías se definen localmente (no globalmente).

---

## Slide 8 — Visualizando anomalías

```python
import matplotlib.pyplot as plt

# Boxplot
df['total_neto'].plot(kind='box')
plt.title('Distribución de ventas con outliers')

# Scatter con anomalías resaltadas
normales = df[df['anomalia_iso'] == 1]
anomalas = df[df['anomalia_iso'] == -1]

plt.scatter(normales.index, normales['total_neto'], c='blue', label='Normal')
plt.scatter(anomalas.index, anomalas['total_neto'], c='red', label='Anomalía')
```

---

## Slide 9 — ¿Cuándo usar cada método?

| Método | Cuándo usarlo |
|---|---|
| **IQR** | Simple, rápido, datos con outliers claros, sin supuestos |
| **Z-score** | Datos con distribución aproximadamente normal |
| **Isolation Forest** | Muchas dimensiones, datos no etiquetados |
| **LOF** | Anomalías locales, densidad variable en el espacio |

---

## Slide 10 — Conclusión

- Las anomalías son puntos que no siguen el patrón esperado.
- Los métodos estadísticos (IQR, Z-score) son simples y explicables.
- Isolation Forest y LOF son más potentes pero menos interpretables.
- Siempre visualiza los resultados antes de actuar sobre una anomalía detectada.
