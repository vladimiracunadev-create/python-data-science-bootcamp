# 💻 Guía de código — Clase 27: Detección de Anomalías

> Explicación detallada del código clave, bloque por bloque.

## Bloque 1: Métodos estadísticos — IQR y Z-score

```python
import pandas as pd
import numpy as np
from scipy import stats

# Cargar datos de ventas
df = pd.read_csv("ventas_tienda.csv")
print(df.head())
print(df.describe())

# --- Método IQR ---
Q1 = df["ventas"].quantile(0.25)   # percentil 25
Q3 = df["ventas"].quantile(0.75)   # percentil 75
IQR = Q3 - Q1                      # rango intercuartílico

limite_inferior = Q1 - 1.5 * IQR
limite_superior = Q3 + 1.5 * IQR

anomalias_iqr = df[(df["ventas"] < limite_inferior) | (df["ventas"] > limite_superior)]
print(f"\nIQR — Límites: [{limite_inferior:.2f}, {limite_superior:.2f}]")
print(f"Anomalías detectadas: {len(anomalias_iqr)}")

# --- Método Z-score ---
df["zscore"] = np.abs(stats.zscore(df["ventas"]))
anomalias_zscore = df[df["zscore"] > 3]
print(f"\nZ-score — Anomalías con |z| > 3: {len(anomalias_zscore)}")
```

**¿Qué hace este bloque?** Calcula los límites de anomalías por IQR (los puntos que caen más de 1.5 veces el rango intercuartílico por debajo del Q1 o por encima del Q3) y por Z-score (los puntos que se alejan más de 3 desviaciones estándar de la media).

**¿Por qué se escribe así?** El factor `1.5 * IQR` es la convención de Tukey, la misma que usa un boxplot estándar. Usar `np.abs(stats.zscore(...))` nos da el valor absoluto del Z-score porque nos interesa la distancia sin importar la dirección (tan anómalo es un valor muy alto como uno muy bajo).

**Resultado esperado:** Dos conteos de anomalías. En datasets con distribución normal, IQR y Z-score suelen coincidir bastante. Cuando la distribución es asimétrica (skewed), los resultados pueden diferir significativamente.

---

## Bloque 2: Isolation Forest con sklearn

```python
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Preparar los datos (Isolation Forest espera array 2D)
X = df[["ventas"]].values   # dobles corchetes para mantener forma 2D

# Entrenar Isolation Forest
isolation_forest = IsolationForest(
    n_estimators=100,         # número de árboles de aislamiento
    contamination=0.05,       # estimamos que ~5% de los datos son anomalías
    random_state=42
)

df["anomalia_if"] = isolation_forest.fit_predict(X)
# El modelo predice: 1 = normal, -1 = anomalía

# Separar normales y anomalías para visualizar
normales = df[df["anomalia_if"] == 1]
anomalias = df[df["anomalia_if"] == -1]

print(f"Puntos normales: {len(normales)}")
print(f"Anomalías detectadas: {len(anomalias)}")
print("\nAnomalías encontradas:")
print(anomalias[["fecha", "ventas"]].to_string())

# Visualizar
plt.figure(figsize=(12, 5))
plt.scatter(normales.index, normales["ventas"],
            color="steelblue", alpha=0.6, label="Normal", s=20)
plt.scatter(anomalias.index, anomalias["ventas"],
            color="red", s=80, marker="x", label="Anomalía", zorder=5)
plt.axhline(y=limite_superior, color="orange", linestyle="--", label="Límite IQR")
plt.xlabel("Índice")
plt.ylabel("Ventas")
plt.title("Detección de anomalías con Isolation Forest")
plt.legend()
plt.show()
```

**¿Qué hace este bloque?** Entrena un Isolation Forest: construye árboles de decisión aleatorios y mide cuántos cortes se necesitan para aislar cada punto. Los puntos anómalos (alejados del grupo principal) se aíslan con muy pocos cortes, por eso tienen menor "profundidad de aislamiento".

**¿Por qué se escribe así?** El parámetro `contamination=0.05` le dice al modelo que esperamos que el 5% de los datos sean anomalías. Si no conocemos este porcentaje, podemos experimentar con distintos valores o usar `contamination='auto'`. Los dobles corchetes `df[["ventas"]]` son necesarios porque sklearn espera un array 2D.

**Resultado esperado:** Un scatter plot donde los puntos rojos (anomalías) aparecen claramente separados de la nube principal de datos azules. Esto permite validar visualmente que las anomalías detectadas tienen sentido en el contexto del negocio.

---

## Bloque 3: Local Outlier Factor (LOF)

```python
from sklearn.neighbors import LocalOutlierFactor

# LOF evalúa la densidad local de cada punto respecto a sus vecinos
lof = LocalOutlierFactor(
    n_neighbors=20,         # número de vecinos a considerar
    contamination=0.05
)

# IMPORTANTE: LOF usa fit_predict, no fit + predict por separado
df["anomalia_lof"] = lof.fit_predict(df[["ventas"]])

# El score negativo indica cuán anómalo es el punto (más negativo = más anómalo)
df["lof_score"] = lof.negative_outlier_factor_

anomalias_lof = df[df["anomalia_lof"] == -1]
print(f"LOF — Anomalías detectadas: {len(anomalias_lof)}")

# Comparar los tres métodos
df["anomalia_iqr"] = ((df["ventas"] < limite_inferior) | (df["ventas"] > limite_superior)).astype(int)
df["anomalia_zscore"] = (df["zscore"] > 3).astype(int)
df["anomalia_if_bin"] = (df["anomalia_if"] == -1).astype(int)
df["anomalia_lof_bin"] = (df["anomalia_lof"] == -1).astype(int)

# Resumen comparativo
print("\nComparación de métodos:")
print(f"IQR:              {df['anomalia_iqr'].sum()} anomalías")
print(f"Z-score:          {df['anomalia_zscore'].sum()} anomalías")
print(f"Isolation Forest: {df['anomalia_if_bin'].sum()} anomalías")
print(f"LOF:              {df['anomalia_lof_bin'].sum()} anomalías")

# Puntos que TODOS los métodos identifican como anómalos (alta confianza)
df["todos_acuerdan"] = (
    df["anomalia_iqr"] + df["anomalia_zscore"] +
    df["anomalia_if_bin"] + df["anomalia_lof_bin"]
) == 4

print(f"\nPuntos que los 4 métodos clasifican como anomalía: {df['todos_acuerdan'].sum()}")
```

**¿Qué hace este bloque?** Aplica LOF, que en lugar de usar una métrica global (como la media o mediana de todo el dataset) evalúa qué tan densa es la vecindad de cada punto comparada con la vecindad de sus vecinos. Un punto es anómalo si está en una zona mucho menos densa que sus vecinos cercanos.

**¿Por qué se escribe así?** LOF tiene una limitación importante: no se puede usar el modelo entrenado para predecir nuevos puntos (no tiene `.predict()` después de `.fit()`), por eso se usa `fit_predict()` directamente. El `negative_outlier_factor_` da un score de anomalía continuo: cuanto más negativo, más anómalo.

**Resultado esperado:** Una tabla comparativa de cuántas anomalías detecta cada método. Los puntos donde los cuatro métodos coinciden son los de mayor confianza: casi con certeza son anomalías reales que merecen investigación.

---

## Bloque 4: Visualización completa con boxplot y scatter

```python
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Boxplot clásico (muestra outliers del método IQR automáticamente)
axes[0].boxplot(df["ventas"], vert=True)
axes[0].set_title("Boxplot de ventas\n(muestra outliers IQR)")
axes[0].set_ylabel("Ventas")

# Distribución con anomalías marcadas
axes[1].hist(df[df["anomalia_if"] == 1]["ventas"],
             bins=30, alpha=0.7, color="steelblue", label="Normal")
axes[1].hist(df[df["anomalia_if"] == -1]["ventas"],
             bins=10, alpha=0.8, color="red", label="Anomalía")
axes[1].set_title("Distribución de ventas\n(Isolation Forest)")
axes[1].set_xlabel("Ventas")
axes[1].legend()

# Scatter plot temporal si hay columna de fecha/orden
axes[2].scatter(range(len(df[df["anomalia_if"] == 1])),
                df[df["anomalia_if"] == 1]["ventas"],
                color="steelblue", alpha=0.5, s=15, label="Normal")
axes[2].scatter(anomalias.index, anomalias["ventas"],
                color="red", s=100, marker="*", label="Anomalía", zorder=5)
axes[2].set_title("Anomalías en el tiempo\n(Isolation Forest)")
axes[2].set_xlabel("Índice temporal")
axes[2].set_ylabel("Ventas")
axes[2].legend()

plt.tight_layout()
plt.savefig("anomalias_ventas.png", dpi=150, bbox_inches="tight")
plt.show()
```

**¿Qué hace este bloque?** Genera tres visualizaciones complementarias: el boxplot clásico que muestra outliers visualmente, un histograma que muestra cómo se distribuyen los valores normales vs. anómalos, y un scatter plot temporal que permite ver si las anomalías se concentran en ciertas épocas.

**¿Por qué se escribe así?** Las tres visualizaciones juntas cuentan historias distintas. El boxplot es intuitivo para comunicar a no-técnicos. El histograma muestra la separación estadística. El scatter temporal es clave para detectar patrones (por ejemplo, anomalías que ocurren siempre en fin de mes).

**Resultado esperado:** Una figura guardada como `anomalias_ventas.png` con tres paneles. Esta imagen puede usarse directamente en un reporte de negocio.

---

## Errores comunes y cómo resolverlos

| Error | Causa | Solución |
|---|---|---|
| `ValueError: Input contains NaN` en IsolationForest | El dataset tiene valores faltantes | Usar `df.dropna()` o `SimpleImputer` antes de entrenar |
| LOF no tiene `.predict()` para nuevos datos | Es un método transductivo, no inductivo | Usar IsolationForest si necesitas predecir en datos nuevos |
| Todos los puntos son marcados como anómalos | El parámetro `contamination` es muy alto | Reducir `contamination` a 0.01-0.05 como punto de partida |
| IQR no detecta anomalías con distribución muy sesgada | Los límites IQR se distorsionan con distribuciones no simétricas | Aplicar transformación logarítmica antes: `np.log1p(df["ventas"])` |
| Z-score no funciona bien con distribuciones no normales | Z-score asume distribución normal | Usar IQR o métodos no paramétricos con datos muy asimétricos |
| `ValueError: could not broadcast` en IsolationForest | Se pasó un array 1D en lugar de 2D | Usar `df[["columna"]]` con dobles corchetes en lugar de `df["columna"]` |
