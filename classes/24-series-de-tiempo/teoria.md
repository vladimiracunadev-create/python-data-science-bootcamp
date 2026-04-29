# 📖 Teoría — Clase 24: Series de tiempo — datos temporales

---

## 1. ¿Qué es una serie de tiempo?

Una **serie de tiempo** (o serie temporal) es un conjunto de observaciones de una variable, medidas en instantes sucesivos de tiempo y ordenadas cronológicamente.

La característica fundamental que distingue una serie de tiempo de otros datos es que **el orden importa**. Si reordenas aleatoriamente las filas de un dataset de ventas anuales, destruyes su significado. El día 5 viene después del día 4 y antes del día 6, y esa posición relativa es parte de la información.

### Ejemplos cotidianos:
- El precio de Bitcoin cada hora durante un año
- La temperatura de una ciudad a las 8:00 AM cada día
- El número de pasajeros que usa el metro por semana
- Las ventas semanales de una cadena de restaurantes
- El nivel de un río medido cada día durante una inundación

### ¿Por qué analizar series de tiempo?
- **Entender el pasado**: ¿cómo ha evolucionado la variable?
- **Detectar anomalías**: ¿hubo algo inusual en cierta fecha?
- **Predecir el futuro**: ¿qué valor tendrá la variable el próximo mes?

---

## 2. Trabajar con fechas en pandas

### 2.1 Convertir texto a fecha

Los CSV suelen guardar las fechas como texto. Pandas no puede operar sobre texto como si fuera una fecha. El primer paso siempre es convertir:

```python
import pandas as pd

df = pd.read_csv('datos.csv')
print(df['fecha'].dtype)    # object (texto)

# Convertir a datetime
df['fecha'] = pd.to_datetime(df['fecha'])
print(df['fecha'].dtype)    # datetime64[ns]
```

Formatos comunes que `pd.to_datetime()` reconoce automáticamente:
- `'2023-01-15'` (ISO 8601, el más común)
- `'15/01/2023'`
- `'January 15, 2023'`
- `'2023-01-15 08:30:00'` (con hora)

Si el formato es ambiguo, especifícalo:
```python
df['fecha'] = pd.to_datetime(df['fecha'], format='%d/%m/%Y')
```

### 2.2 Extraer componentes de la fecha

Una vez que la columna es datetime, puedes extraer partes de la fecha:

```python
df['anio']      = df['fecha'].dt.year
df['mes']       = df['fecha'].dt.month
df['dia']       = df['fecha'].dt.day
df['hora']      = df['fecha'].dt.hour
df['dia_semana'] = df['fecha'].dt.dayofweek   # 0=lunes, 6=domingo
df['nombre_dia'] = df['fecha'].dt.day_name()  # 'Monday', 'Tuesday', ...
df['trimestre'] = df['fecha'].dt.quarter
```

### 2.3 Establecer la fecha como índice

Para aprovechar las operaciones especiales de pandas con tiempo, ponemos la fecha como índice:

```python
df = df.set_index('fecha')
df = df.sort_index()    # muy importante: ordenar cronológicamente
```

Ventajas de tener fecha como índice:
```python
# Filtrar por rango de fechas
datos_2023 = df['2023']
enero_marzo = df['2023-01':'2023-03']
un_dia = df['2023-06-15']
```

---

## 3. Resample: agregar datos por período

`resample()` es el equivalente de `groupby()` para datos temporales. En lugar de agrupar por una categoría, agrupas por períodos de tiempo.

### Alias de frecuencia más comunes:
| Alias | Período |
|-------|---------|
| `'D'` | Día |
| `'W'` | Semana |
| `'M'` | Mes (fin de mes) |
| `'MS'` | Mes (inicio de mes) |
| `'Q'` | Trimestre |
| `'Y'` | Año |
| `'H'` | Hora |

```python
# Ventas diarias → ventas mensuales
ventas_mensuales = df['ventas'].resample('M').sum()

# Precio diario → precio semanal promedio
precio_semanal = df['precio'].resample('W').mean()

# Registros por día → conteo mensual
conteo_mensual = df['id_venta'].resample('M').count()

# Múltiples estadísticas a la vez
resumen = df['ventas'].resample('M').agg(['sum', 'mean', 'max', 'min'])
```

---

## 4. Rolling: ventana deslizante (promedio móvil)

El **promedio móvil** (moving average) es una técnica que suaviza las fluctuaciones de una serie calculando el promedio de los últimos K valores en cada punto.

Piénsalo así: si las ventas de un día son excepcionalmente altas o bajas (por una oferta especial o un día festivo), el promedio móvil de los últimos 7 días "amortigua" ese pico y muestra la tendencia subyacente.

```python
# Promedio móvil de 7 días
df['media_7d'] = df['ventas'].rolling(window=7).mean()

# Promedio móvil de 30 días (más suavizado)
df['media_30d'] = df['ventas'].rolling(window=30).mean()

# Suma acumulada móvil
df['suma_7d'] = df['ventas'].rolling(window=7).sum()

# Desviación estándar móvil (para detectar cambios en variabilidad)
df['std_7d'] = df['ventas'].rolling(window=7).std()
```

**Importante:** los primeros `window-1` valores serán `NaN` porque no hay suficiente historial para calcular la ventana completa.

---

## 5. Visualizar series de tiempo

El gráfico de línea es el estándar para series de tiempo:

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 5))

ax.plot(df.index, df['ventas'],
        label='Ventas diarias', color='steelblue', alpha=0.5, linewidth=1)
ax.plot(df.index, df['media_7d'],
        label='Media móvil 7 días', color='red', linewidth=2)
ax.plot(df.index, df['media_30d'],
        label='Media móvil 30 días', color='darkgreen', linewidth=2.5)

ax.set_xlabel('Fecha')
ax.set_ylabel('Ventas ($)')
ax.set_title('Evolución de ventas con medias móviles')
ax.legend()
ax.grid(alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Colorear áreas entre líneas:
```python
ax.fill_between(df.index, df['ventas'], alpha=0.1, color='steelblue')
```

### Graficar múltiples series en subplots:
```python
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)
df['ventas'].plot(ax=axes[0], title='Ventas')
df['clientes'].plot(ax=axes[1], title='Clientes', color='green')
plt.tight_layout()
```

---

## 6. Componentes de una serie de tiempo

Toda serie de tiempo puede descomponerse en tres partes:

### Tendencia (Trend)
La dirección general de largo plazo. ¿Las ventas crecen, decrecen o se mantienen estables a lo largo del tiempo? La tendencia es el "rumbo" de la serie, ignorando las fluctuaciones.

### Estacionalidad (Seasonality)
Patrones que se repiten en ciclos regulares: diarios, semanales, mensuales, anuales. Por ejemplo:
- Las ventas de helado son máximas en verano cada año
- El tráfico web sube los lunes y baja los domingos cada semana

### Residuo (Residual / Noise)
Lo que queda después de eliminar la tendencia y la estacionalidad. Son las fluctuaciones "aleatorias" o eventos únicos (una oferta especial, una noticia, una crisis).

---

## 7. Descomposición estacional con statsmodels

`seasonal_decompose` hace este análisis automáticamente:

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Necesitamos la serie con índice de fechas y sin valores nulos
serie = df['ventas'].resample('M').sum().dropna()

# Descomponer (model='additive': tendencia + estacional + residuo)
resultado = seasonal_decompose(serie, model='additive', period=12)

# Graficar todos los componentes
fig = resultado.plot()
fig.set_size_inches(12, 8)
plt.tight_layout()
plt.show()
```

**model='additive'** asume: serie = tendencia + estacional + residuo
**model='multiplicative'** asume: serie = tendencia × estacional × residuo

Usa multiplicativo cuando la amplitud de la estacionalidad crece con la tendencia.

---

## 8. Pronóstico simple

### Métodos naïve (sin modelos complejos):

```python
# Método 1: último valor observado
ultimo_valor = serie.iloc[-1]
pronostico_naive = ultimo_valor

# Método 2: promedio histórico
pronostico_promedio = serie.mean()

# Método 3: promedio móvil de los últimos K períodos
k = 3
pronostico_ma = serie.tail(k).mean()

# Método 4: mismo período del año anterior (seasonal naive)
pronostico_seasonal = serie.iloc[-12]  # hace 12 meses

print(f'Pronóstico naive: {pronostico_naive:,.0f}')
print(f'Pronóstico promedio: {pronostico_promedio:,.0f}')
print(f'Pronóstico media móvil ({k}m): {pronostico_ma:,.0f}')
print(f'Pronóstico seasonal: {pronostico_seasonal:,.0f}')
```

> Para pronósticos avanzados existen modelos como ARIMA, Prophet y LSTM, que se verán en módulos avanzados.

---

## Resumen de conceptos

| Concepto | Qué es / Para qué sirve |
|----------|------------------------|
| Serie de tiempo | Secuencia de valores ordenados por tiempo |
| `pd.to_datetime()` | Convierte texto en fechas que pandas entiende |
| `set_index()` | Pone la fecha como índice para operaciones temporales |
| `resample()` | Agrega datos por período (mes, semana, año) |
| `rolling()` | Calcula estadísticas sobre una ventana deslizante |
| Tendencia | Dirección general de largo plazo de la serie |
| Estacionalidad | Patrón repetitivo en ciclos regulares |
| Residuo | Fluctuaciones después de quitar tendencia y estacionalidad |
| `seasonal_decompose` | Separa la serie en sus componentes |
| Promedio móvil | Media de los últimos K valores para suavizar ruido |
