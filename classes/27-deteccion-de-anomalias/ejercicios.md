# 🏋️ Ejercicios — Clase 27: Detección de Anomalías

> Completa estos ejercicios en orden. Cada uno construye sobre el anterior.

---

## Ejercicio 1 — Identificación intuitiva

**Sin usar código**, responde las siguientes preguntas:

1. En una lista de temperaturas diarias en grados Celsius: [22, 23, 21, 24, 22, 75, 23, 22], ¿cuál es la anomalía? ¿Cómo lo sabes?

2. Una tienda tiene ventas diarias entre $500 y $2,000. Un día registra $50. ¿Es una anomalía? ¿Podría tener una explicación válida?

3. Diferencia entre outlier y anomalía: imagina un hospital que registra tiempos de espera en urgencias. Un tiempo de espera de 30 segundos podría ser estadísticamente inusual (outlier), pero ¿es una anomalía problemática? Explica.

---

## Ejercicio 2 — Exploración del dataset de ventas

```python
import pandas as pd
import matplotlib.pyplot as plt

df_ventas = pd.read_csv('datasets/ventas_tienda.csv')
print("Forma:", df_ventas.shape)
print("\nColumnas:", df_ventas.columns.tolist())
print("\nEstadísticas descriptivas:")
print(df_ventas['total_neto'].describe())
```

**Visualización inicial:**
```python
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Serie temporal
df_ventas['total_neto'].plot(ax=axes[0], color='steelblue', alpha=0.7)
axes[0].set_title('Ventas diarias (total_neto)')
axes[0].set_xlabel('Índice')
axes[0].set_ylabel('Total neto ($)')

# Boxplot
df_ventas['total_neto'].plot(kind='box', ax=axes[1])
axes[1].set_title('Distribución de ventas (boxplot)')

plt.tight_layout()
plt.show()
```

**Preguntas:**
1. ¿Hay valores que visualmente parecen anómalos?
2. ¿Cómo es la distribución? ¿Simétrica o sesgada?
3. ¿Cuál es la diferencia entre el valor máximo y el percentil 95?

---

## Ejercicio 3 — Método IQR

```python
# Calcular IQR manualmente
Q1 = df_ventas['total_neto'].quantile(0.25)
Q3 = df_ventas['total_neto'].quantile(0.75)
IQR = Q3 - Q1

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

print(f"Q1: {Q1:.2f}")
print(f"Q3: {Q3:.2f}")
print(f"IQR: {IQR:.2f}")
print(f"Límite inferior: {limite_inferior:.2f}")
print(f"Límite superior: {limite_superior:.2f}")

# Identificar anomalías
df_ventas['outlier_iqr'] = (
    (df_ventas['total_neto'] < limite_inferior) |
    (df_ventas['total_neto'] > limite_superior)
)

print(f"\nAnomalías detectadas por IQR: {df_ventas['outlier_iqr'].sum()}")
print(f"Porcentaje del total: {df_ventas['outlier_iqr'].mean():.1%}")
print("\nDías con anomalías:")
print(df_ventas[df_ventas['outlier_iqr']])
```

**Preguntas:**
1. ¿Cuántas anomalías detectó el método IQR?
2. ¿Son valores inusualmente altos, inusualmente bajos, o ambos?
3. Prueba con `1.5 * IQR` vs `3.0 * IQR`. ¿Cómo cambia el número de anomalías?

---

## Ejercicio 4 — Método Z-score

```python
from scipy import stats
import numpy as np

z_scores = np.abs(stats.zscore(df_ventas['total_neto']))
df_ventas['z_score'] = np.abs(stats.zscore(df_ventas['total_neto']))
df_ventas['outlier_zscore'] = df_ventas['z_score'] > 3

print(f"Anomalías detectadas por Z-score: {df_ventas['outlier_zscore'].sum()}")
print("\nTop 5 valores con mayor Z-score:")
print(df_ventas.nlargest(5, 'z_score')[['total_neto', 'z_score']])
```

**Comparación IQR vs Z-score:**
```python
ambos = df_ventas['outlier_iqr'] & df_ventas['outlier_zscore']
solo_iqr = df_ventas['outlier_iqr'] & ~df_ventas['outlier_zscore']
solo_zscore = ~df_ventas['outlier_iqr'] & df_ventas['outlier_zscore']

print(f"Detectadas por ambos métodos: {ambos.sum()}")
print(f"Solo por IQR: {solo_iqr.sum()}")
print(f"Solo por Z-score: {solo_zscore.sum()}")
```

**Preguntas:**
1. ¿Los dos métodos detectan las mismas anomalías?
2. ¿Qué método es más estricto (detecta menos anomalías)?
3. ¿Cuándo preferirías usar Z-score sobre IQR?

---

## Ejercicio 5 — Isolation Forest

```python
from sklearn.ensemble import IsolationForest

iso_forest = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

df_ventas['anomalia_iso'] = iso_forest.fit_predict(df_ventas[['total_neto']])

print(f"Anomalías detectadas: {(df_ventas['anomalia_iso'] == -1).sum()}")
print(f"Puntos normales: {(df_ventas['anomalia_iso'] == 1).sum()}")
```

**Visualización:**
```python
fig, ax = plt.subplots(figsize=(14, 5))

normales = df_ventas[df_ventas['anomalia_iso'] == 1]
anomalas = df_ventas[df_ventas['anomalia_iso'] == -1]

ax.scatter(normales.index, normales['total_neto'], c='steelblue', s=20, alpha=0.6, label='Normal')
ax.scatter(anomalas.index, anomalas['total_neto'], c='red', s=60, zorder=5, label='Anomalía')
ax.axhline(limite_superior, color='orange', linestyle='--', label=f'Límite IQR superior ({limite_superior:.0f})')
ax.axhline(limite_inferior, color='orange', linestyle='--')
ax.set_title('Ventas diarias con anomalías detectadas (Isolation Forest)')
ax.set_xlabel('Día')
ax.set_ylabel('Total neto ($)')
ax.legend()
plt.show()
```

**Preguntas:**
1. ¿Isolation Forest detecta las mismas anomalías que IQR?
2. Cambia `contamination` de 0.05 a 0.10. ¿Cuántas anomalías adicionales aparecen?
3. ¿Las anomalías adicionales al aumentar `contamination` tienen sentido?

---

## Ejercicio 6 — Local Outlier Factor en retrasos de transporte

```python
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

df_transporte = pd.read_csv('datasets/transporte.csv')
print(df_transporte.head())
print(df_transporte['retraso_min'].describe())

lof = LocalOutlierFactor(
    n_neighbors=20,
    contamination=0.05
)

df_transporte['anomalia_lof'] = lof.fit_predict(df_transporte[['retraso_min']])
df_transporte['lof_score'] = lof.negative_outlier_factor_

print(f"\nAnomalías LOF detectadas: {(df_transporte['anomalia_lof'] == -1).sum()}")
print("\nTop 5 rutas más anómalas:")
print(df_transporte.nsmallest(5, 'lof_score')[['retraso_min', 'lof_score', 'anomalia_lof']])
```

**Preguntas:**
1. ¿Qué rutas tienen los retrasos más anómalos?
2. ¿Son los retrasos anómalos siempre los más altos? ¿O también hay valores inusualmente bajos?
3. ¿Qué podría explicar un retraso extremadamente largo en el transporte?

---

## Ejercicio 7 — Comparación de todos los métodos

```python
# Reunir todos los resultados en una tabla comparativa
comparacion = pd.DataFrame({
    'total_neto': df_ventas['total_neto'],
    'IQR': df_ventas['outlier_iqr'].astype(int),
    'Z-score': df_ventas['outlier_zscore'].astype(int),
    'Isolation Forest': (df_ventas['anomalia_iso'] == -1).astype(int)
})

comparacion['total_metodos'] = comparacion[['IQR', 'Z-score', 'Isolation Forest']].sum(axis=1)

print("Anomalías por método:")
print(comparacion[['IQR', 'Z-score', 'Isolation Forest']].sum())

print("\nPuntos marcados por los 3 métodos a la vez:")
print(comparacion[comparacion['total_metodos'] == 3])
```

**Preguntas:**
1. ¿Qué puntos son marcados como anómalos por todos los métodos? ¿Son los más "confiables"?
2. ¿Hay puntos que solo detecta un método? ¿Qué dice esto sobre ese método?
3. Si tuvieras que reportarle a tu jefe cuántas anomalías hay, ¿qué criterio usarías para decidir?

---

## Ejercicio 8 — Desafío: detección multivariada

Si el dataset de ventas tiene más de una columna numérica, aplica Isolation Forest usando múltiples variables a la vez:

```python
# Seleccionar columnas numéricas relevantes
columnas_numericas = df_ventas.select_dtypes(include='number').columns.tolist()
print("Columnas numéricas disponibles:", columnas_numericas)

# Isolation Forest multivariado
iso_multi = IsolationForest(contamination=0.05, random_state=42)
df_ventas['anomalia_multi'] = iso_multi.fit_predict(df_ventas[columnas_numericas])

print(f"Anomalías detectadas (multivariado): {(df_ventas['anomalia_multi'] == -1).sum()}")

# Comparar con univariado
diff = (df_ventas['anomalia_iso'] == -1) != (df_ventas['anomalia_multi'] == -1)
print(f"Diferencias vs detección univariada: {diff.sum()} puntos")
```

**Reflexión final:** ¿Cuándo crees que la detección multivariada sería mejor que la univariada? Da un ejemplo del mundo real.

---

## Criterios de evaluación

- Ejercicios 1-2: comprensión conceptual y exploración de datos.
- Ejercicios 3-4: implementación y comparación de métodos estadísticos.
- Ejercicios 5-6: aplicación de métodos ML con visualización.
- Ejercicios 7-8: análisis comparativo y reflexión crítica.
