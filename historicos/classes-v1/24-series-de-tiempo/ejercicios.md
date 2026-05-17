# 🏋️ Ejercicios — Clase 24: Series de tiempo — datos temporales

> Completa cada ejercicio en tu notebook. Ejecuta las celdas y responde las preguntas de reflexión.

---

## Ejercicio 1 — Cargar y convertir fechas
**Nivel: Básico**

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/ventas_tienda.csv')
print(df.head())
print(df.dtypes)
print(df.shape)
```

**Tareas:**
1. ¿Hay alguna columna que parezca una fecha? ¿Cuál es su tipo de dato actual?
2. Conviértela a datetime:
```python
df['fecha'] = pd.to_datetime(df['fecha'])
print(df['fecha'].dtype)  # debe decir datetime64
```
3. Extrae el año, mes y día en columnas separadas

**Preguntas de reflexión:**
1. ¿Qué rango de fechas cubre el dataset? (usa `.min()` y `.max()` en la columna fecha)
2. ¿Cuántos días distintos hay en el dataset?

---

## Ejercicio 2 — Fecha como índice y filtrado
**Nivel: Básico**

```python
# Poner la fecha como índice y ordenar cronológicamente
df = df.set_index('fecha')
df = df.sort_index()

print('Primeros registros:')
print(df.head())

print('\nPrimera y última fecha:')
print(df.index.min(), '→', df.index.max())
```

**Tareas:**
1. Filtra solo los datos de un mes específico (usa `df['YYYY-MM']`)
2. Filtra un rango de 3 meses (usa `df['YYYY-MM':'YYYY-MM']`)
3. ¿Cuántos registros hay en cada mes? (usa `df.resample('M').count()`)

---

## Ejercicio 3 — Resample: ventas por período
**Nivel: Básico**

```python
# Identificar la columna de ventas del dataset
col_ventas = 'ventas'  # ajusta al nombre real

# Agregar ventas por mes
ventas_mensuales = df[col_ventas].resample('M').sum()
print('Ventas mensuales:')
print(ventas_mensuales)
```

**Tareas:**
1. Calcula también las ventas semanales con `.resample('W').sum()`
2. Calcula el promedio mensual de ventas
3. gráfica las ventas mensuales como gráfico de barras:
```python
ventas_mensuales.plot(kind='bar', figsize=(12, 4), color='steelblue')
plt.title('Ventas totales por mes')
plt.xlabel('Mes')
plt.ylabel('Ventas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Qué mes tuvo las ventas más altas? ¿Y las más bajas?
2. ¿Hay algún patrón estacional visible?

---

## Ejercicio 4 — Promedio móvil: suavizar el ruido
**Nivel: Básico**

```python
# Calcular promedios móviles de distintas ventanas
df['media_7d']  = df[col_ventas].rolling(window=7).mean()
df['media_30d'] = df[col_ventas].rolling(window=30).mean()

print(f'Valores NaN en media_7d: {df["media_7d"].isna().sum()}')
print('(Los primeros 6 valores son NaN porque no hay suficiente historial)')
```

**Graficar:**
```python
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(df.index, df[col_ventas], label='Ventas diarias',
        alpha=0.4, color='steelblue')
ax.plot(df.index, df['media_7d'],  label='Media 7 días',
        color='red', linewidth=2)
ax.plot(df.index, df['media_30d'], label='Media 30 días',
        color='darkgreen', linewidth=2.5)
ax.set_title('Ventas con promedios móviles')
ax.set_xlabel('Fecha')
ax.set_ylabel(col_ventas)
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Qué diferencia ves entre la media de 7 días y la de 30 días?
2. ¿La línea verde (30 días) revela alguna tendencia que no se veía en los datos diarios?

---

## Ejercicio 5 — Tendencia y estacionalidad visual
**Nivel: Intermedio**

```python
# Graficar ventas mensuales y agregar una línea de tendencia
import numpy as np

y = ventas_mensuales.values
x = np.arange(len(y))

# Ajustar una línea de tendencia (regresión lineal simple)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(ventas_mensuales.index, y, marker='o', label='Ventas mensuales')
ax.plot(ventas_mensuales.index, p(x), '--',
        color='red', linewidth=2, label='Tendencia lineal')
ax.set_title('Ventas mensuales + Tendencia')
ax.set_xlabel('Mes')
ax.set_ylabel('Ventas')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

pendiente = z[0]
print(f'Pendiente de la tendencia: {pendiente:.2f}')
print(f'Interpretación: las ventas {"crecen" if pendiente > 0 else "decrecen"} '
      f'{abs(pendiente):.0f} por mes en promedio')
```

**Preguntas de reflexión:**
1. ¿Las ventas tienen tendencia creciente o decreciente?
2. ¿Ves algún mes que siempre sube o siempre baja (estacionalidad)?

---

## Ejercicio 6 — Descomposición estacional
**Nivel: Intermedio**

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# La serie debe tener al menos 2 ciclos completos (2 años si period=12)
# Si el dataset es más corto, ajusta el period
serie_limpia = ventas_mensuales.dropna()

período = min(12, len(serie_limpia) // 2)
resultado = seasonal_decompose(serie_limpia, model='additive', period=período)

fig = resultado.plot()
fig.set_size_inches(12, 10)
plt.suptitle('Descomposición estacional — Ventas mensuales', y=1.02)
plt.tight_layout()
plt.show()
```

**Preguntas de reflexión:**
1. ¿Cuál es el mes con mayor componente estacional (más alto que el promedio)?
2. ¿Los residuos son pequeños (buen modelo) o grandes (modelo impreciso)?
3. ¿La tendencia es lineal o tiene cambios de dirección?

---

## Ejercicio 7 — Pronóstico simple
**Nivel: Intermedio**

```python
# Comparar varios métodos de pronóstico simple
último = ventas_mensuales.iloc[-1]
promedio_historico = ventas_mensuales.mean()
promedio_3meses = ventas_mensuales.tail(3).mean()

if len(ventas_mensuales) >= 13:
    seasonal_naive = ventas_mensuales.iloc[-12]
    print(f'Seasonal naive (hace 12 meses):  ${seasonal_naive:,.0f}')

print(f'Método naive (último valor):      ${último:,.0f}')
print(f'Promedio histórico:               ${promedio_historico:,.0f}')
print(f'Promedio 3 últimos meses:         ${promedio_3meses:,.0f}')

print('\n¿Cuál método usarías? Justifica tu respuesta.')
```

**Preguntas de reflexión:**
1. Si las ventas tienen tendencia creciente, ¿qué método sobreestimará menos?
2. ¿Cuándo sería mejor usar el seasonal naive sobre el promedio móvil?

---

## Ejercicio 8 — Dataset de retención de clientes
**Nivel: Avanzado**

```python
df_ret = pd.read_csv('datasets/retencion_clientes.csv')
print(df_ret.head())
print(df_ret.dtypes)
```

**Pasos:**
1. Identifica la columna de tiempo (puede llamarse `mes`, `fecha`, `período`)
2. Conviértela a datetime si es necesario
3. Ponla como índice
4. gráfica la tasa de retención a lo largo del tiempo
5. Calcula y gráfica el promedio móvil de 3 meses
6. ¿Hay algún mes donde la retención cayó notablemente? ¿A qué podría deberse?

**Entrega:** Un gráfico y un párrafo de análisis en una celda Markdown.
