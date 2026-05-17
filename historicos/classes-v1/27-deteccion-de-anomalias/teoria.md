# 📖 Teoría — Clase 27: Detección de Anomalías

## 1. ¿Qué es una anomalía?

Una **anomalía** es un punto de datos que se comporta de manera inesperada o diferente al patrón general del conjunto de datos. También se le llama *outlier*, aunque existe una distinción sutil:

- **Outlier estadístico:** valor extremo en términos numéricos (muy alto o muy bajo respecto a la distribución).
- **Anomalía contextual:** valor que no es necesariamente extremo en términos absolutos, pero es inusual en su contexto.

**Ejemplo:** Una compra de $20 normalmente no es un outlier estadístico. Pero si siempre compras $200, esa compra de $20 es una anomalía contextual. Igualmente, una temperatura de 36°C en el cuerpo humano es normal; en una tubería de metal puede ser una alarma.

---

## 2. Aplicaciones reales de detección de anomalías

- **Detección de fraude bancario:** transacciones inusuales por monto, ubicación o frecuencia.
- **Mantenimiento predictivo:** sensores de máquinas que registran valores fuera del rango habitual antes de una falla.
- **Seguridad informática:** patrones de tráfico de red inusuales que pueden indicar un ataque.
- **Salud:** valores de laboratorio que se desvían del patrón histórico de un paciente.
- **Logística y transporte:** rutas o tiempos de entrega muy fuera del promedio.
- **E-commerce:** picos inusuales de reseñas o ventas que pueden indicar manipulación.
- **Calidad de producción:** piezas fabricadas con dimensiones fuera del margen de tolerancia.

---

## 3. Método 1: Regla del IQR (Rango Intercuartil)

El **IQR** (Interquartile Range) es la diferencia entre el percentil 75 (Q3) y el percentil 25 (Q1). Representa el rango del 50% central de los datos.

```
IQR = Q3 - Q1

Límite inferior = Q1 - 1.5 × IQR
Límite superior = Q3 + 1.5 × IQR
```

Cualquier valor fuera de estos límites se considera un posible outlier.

```python
import pandas as pd

Q1 = df['total_neto'].quantile(0.25)
Q3 = df['total_neto'].quantile(0.75)
IQR = Q3 - Q1

limite_inf = Q1 - 1.5 * IQR
limite_sup = Q3 + 1.5 * IQR

df['outlier_iqr'] = (df['total_neto'] < limite_inf) | (df['total_neto'] > limite_sup)
anomalias_iqr = df[df['outlier_iqr']]
```

**Ventajas:** No asume ninguna distribución. Robusto con datos sesgados. Fácil de entender y explicar.

**Desventajas:** Solo funciona para una variable a la vez. No considera relaciones entre variables.

---

## 4. Método 2: Z-score

El **Z-score** mide cuántas desviaciones estándar está un punto de la media. Se usa cuando los datos tienen una distribución aproximadamente normal.

```
z = (x - μ) / σ

Donde:
μ = media de la variable
σ = desviación estándar de la variable
```

Convencionalmente, si |z| > 3, el punto es considerado un outlier (está a más de 3 desviaciones estándar de la media).

```python
from scipy import stats
import numpy as np

z_scores = np.abs(stats.zscore(df['total_neto']))
df['outlier_zscore'] = z_scores > 3

anomalias_zscore = df[df['outlier_zscore']]
```

**Ventajas:** Simple, matemáticamente sólido para distribuciones normales.

**Desventajas:** Sensible a los propios outliers que quieres detectar (la media y desviación estándar se ven afectadas por valores extremos). No funciona bien con distribuciones muy sesgadas.

---

## 5. Método 3: Isolation Forest

**Isolation Forest** es un algoritmo de Machine Learning especialmente diseñado para detección de anomalías. Su idea central es elegante:

> Las anomalías son más fáciles de "aislar" que los puntos normales.

### ¿Cómo funciona?

1. Se construyen múltiples árboles de decisión aleatorios.
2. En cada árbol, se selecciona aleatoriamente una variable y un punto de corte.
3. Se cuenta cuántos cortes son necesarios para aislar un punto.
4. Los puntos normales necesitan muchos cortes (están rodeados de vecinos).
5. Las anomalías necesitan pocos cortes (están alejadas del resto).

```
Puntos normales: necesitan ~15-20 cortes para quedar solos.
Anomalías: necesitan ~3-5 cortes para quedar solas.
```

```python
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(
    n_estimators=100,      # número de árboles
    contamination=0.05,    # porcentaje esperado de anomalías (5%)
    random_state=42
)

df['anomalia_iso'] = iso_forest.fit_predict(df[['total_neto']])
# Devuelve: 1 = normal, -1 = anomalía

anomalias_iso = df[df['anomalia_iso'] == -1]
```

**Ventajas:** Funciona bien con muchas dimensiones. No asume distribución. Escalable a grandes datasets.

**Desventajas:** Menos interpretable que IQR o Z-score. El parámetro `contamination` debe configurarse.

---

## 6. Método 4: Local Outlier Factor (LOF)

**LOF** mide la densidad local de cada punto en comparación con sus vecinos. Un punto es anómalo si su densidad local es mucho menor que la de sus vecinos.

### Intuición

Imagina una ciudad con varios barrios. Cada barrio tiene casas con diferentes densidades (barrios residenciales vs. centros comerciales). LOF no compara cada casa con el promedio de toda la ciudad, sino con las casas de su barrio específico.

Un punto es anómalo si está en una zona de baja densidad cuando sus vecinos están en zonas de alta densidad.

```python
from sklearn.neighbors import LocalOutlierFactor

lof = LocalOutlierFactor(
    n_neighbors=20,        # número de vecinos a considerar
    contamination=0.05     # porcentaje esperado de anomalías
)

df['anomalia_lof'] = lof.fit_predict(df[['retraso_min']])
# Devuelve: 1 = normal, -1 = anomalía

# Scores de outlier (más negativo = más anómalo)
scores = lof.negative_outlier_factor_
df['lof_score'] = scores
```

**Ventajas:** Detecta anomalías locales (útil cuando la densidad varía en el espacio). Bueno para datos con clusters de distinta densidad.

**Desventajas:** Más lento que Isolation Forest para grandes datasets. Sensible a la elección de `n_neighbors`.

---

## 7. Visualización de anomalías

La visualización es fundamental para validar que los resultados tienen sentido.

### Boxplot
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4))
df['total_neto'].plot(kind='box', ax=ax, vert=False)
ax.set_title('Distribución de ventas con outliers marcados')
```

### Serie temporal con anomalías
```python
fig, ax = plt.subplots(figsize=(14, 5))

normales = df[df['anomalia_iso'] == 1]
anomalas = df[df['anomalia_iso'] == -1]

ax.plot(df.index, df['total_neto'], color='steelblue', alpha=0.6, label='Ventas diarias')
ax.scatter(anomalas.index, anomalas['total_neto'],
           color='red', s=80, zorder=5, label='Anomalías detectadas')
ax.legend()
ax.set_title('Ventas diarias con anomalías detectadas (Isolation Forest)')
```

### Scatter bivariado
```python
fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter(normales['feature_1'], normales['feature_2'],
           c='steelblue', alpha=0.5, label='Normal')
ax.scatter(anomalas['feature_1'], anomalas['feature_2'],
           c='red', s=80, label='Anomalía')
ax.legend()
```

---

## 8. ¿Cuándo usar cada método?

| Situación | Método recomendado |
|---|---|
| Una sola variable numérica, distribución simétrica | IQR o Z-score |
| Una sola variable con distribución sesgada | IQR |
| Datos con muchas variables (multidimensional) | Isolation Forest |
| Datos donde las anomalías son locales (diferentes densidades) | LOF |
| Necesitas explicabilidad para un stakeholder no técnico | IQR (más fácil de explicar) |
| Dataset muy grande (millones de filas) | Isolation Forest (más rápido) |

---

## 9. Consideraciones importantes

### El parámetro `contamination`
Tanto Isolation Forest como LOF requieren estimar qué porcentaje de los datos son anomalías. Si no lo sabes, empieza con valores entre 0.01 y 0.10 (1% a 10%) y ajusta según el contexto del negocio.

### Validación con expertos del dominio
Los algoritmos detectan lo estadísticamente inusual, pero un experto del dominio debe validar si esas anomalías tienen sentido. Una venta inusualmente alta puede ser una promoción legítima, no un fraude.

### Datos etiquetados vs no etiquetados
La mayoría de los problemas de detección de anomalías son **no supervisados** (no tenemos etiquetas de qué es anomalía). Los métodos vistos (IQR, Z-score, Isolation Forest, LOF) son todos no supervisados. Si tienes datos etiquetados (sí sé cuáles son fraudes), usa clasificación supervisada.

---

## 10. Resumen de métodos

| Método | Tipo | Supuesto | Dimensiones |
|---|---|---|---|
| IQR | Estadístico | Ninguno | Una variable |
| Z-score | Estadístico | Distribución normal | Una variable |
| Isolation Forest | ML no supervisado | Ninguno | Múltiples variables |
| LOF | ML no supervisado | Ninguno | Múltiples variables |
