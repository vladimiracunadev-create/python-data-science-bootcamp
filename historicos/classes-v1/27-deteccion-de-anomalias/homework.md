# 📝 Homework — Clase 27: Detección de Anomalías

> Entrega individual. Plazo: antes de la próxima clase.

---

## Tarea 1 — Detección en el dataset de transporte (obligatoria)

Aplica los cuatro métodos vistos en clase al dataset `transporte.csv` sobre la columna `retraso_min`:

```python
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/transporte.csv')

# 1. IQR
Q1 = df['retraso_min'].quantile(0.25)
Q3 = df['retraso_min'].quantile(0.75)
# ... completar

# 2. Z-score
# ... completar

# 3. Isolation Forest
# ... completar

# 4. LOF
# ... completar

# Tabla comparativa
# ... completar
```

**Entrega:**
1. Código funcionando para los 4 métodos.
2. Tabla comparativa: cuántas anomalías detectó cada método.
3. Visualización de las anomalías en la serie temporal de retrasos.
4. ¿Qué método detectó las anomalías más "extremas"? ¿Cuál fue más "conservador"?

---

## Tarea 2 — Detección bivariada (obligatoria)

Si el dataset `ventas_tienda.csv` tiene al menos dos columnas numéricas (por ejemplo, `total_neto` y `cantidad_items`), aplica **Isolation Forest con dos variables al mismo tiempo**:

```python
# Selecciona las dos columnas más relevantes
cols = ['total_neto', 'cantidad_items']  # ajusta según el dataset

iso_bi = IsolationForest(contamination=0.05, random_state=42)
df_ventas['anomalia_bivariada'] = iso_bi.fit_predict(df_ventas[cols])

# Visualización: scatter con ambas variables
plt.figure(figsize=(8, 6))
normales = df_ventas[df_ventas['anomalia_bivariada'] == 1]
anomalas = df_ventas[df_ventas['anomalia_bivariada'] == -1]

plt.scatter(normales[cols[0]], normales[cols[1]], c='steelblue', alpha=0.5, label='Normal')
plt.scatter(anomalas[cols[0]], anomalas[cols[1]], c='red', s=80, label='Anomalía')
plt.xlabel(cols[0])
plt.ylabel(cols[1])
plt.legend()
plt.title('Detección bivariada con Isolation Forest')
plt.show()
```

**Preguntas:**
1. ¿Las anomalías bivariadas coinciden con las univariadas?
2. ¿Encontraste alguna anomalía que NO sería detectada mirando cada variable por separado? (Por ejemplo, valores moderados en ambas variables, pero combinados de forma inusual.)
3. ¿Qué tipo de fraude o error podría representar ese tipo de anomalía combinada?

---

## Tarea 3 — Contexto de negocio (opcional, +1 punto)

Elige uno de los siguientes escenarios y describe (sin código, solo texto) cómo diseñarías un sistema de detección de anomalías:

**Opción A:** Una cadena de supermercados quiere detectar transacciones de caja registradora sospechosas (posible robo interno).

**Opción B:** Una empresa de delivery quiere detectar repartidores que podrían estar manipulando las entregas (marcando como entregado sin realmente entregar).

**Opción C:** Un hospital quiere detectar pacientes cuyas métricas vitales (presión, temperatura, frecuencia cardíaca) sugieren un deterioro rápido.

Para el escenario elegido, responde:
1. ¿Qué variables usarías?
2. ¿Qué método de detección sería más apropiado y por qué?
3. ¿Cómo validarías que las anomalías detectadas son realmente problemas?
4. ¿Qué harías cuando el sistema detecte una anomalía? ¿Alerta automática, revisión manual?

---

## Formato de entrega

- Archivo `.ipynb` con código comentado y respuestas en markdown.
- Nombre del archivo: `homework_clase27_[tu_nombre].ipynb`

---

## Rúbrica

| Criterio | Puntos |
|---|---|
| Tarea 1: 4 métodos implementados | 3 |
| Tarea 1: tabla comparativa y visualización | 2 |
| Tarea 2: detección bivariada con scatter | 3 |
| Tarea 2: análisis de anomalías combinadas | 2 |
| Tarea 3 (opcional) | 1 |
| **Total** | **10 (+1)** |
