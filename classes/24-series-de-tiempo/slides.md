# 🎞️ Slides — Clase 24: Series de tiempo — datos temporales

---

## Diapositiva 1 — Título
# Series de tiempo
### Detectar tendencias, estacionalidad y anomalías en datos que cambian con el tiempo

---

## Diapositiva 2 — ¿Qué es una serie de tiempo?
## Datos ordenados en el tiempo
- Una **serie de tiempo** es una secuencia de observaciones medidas en momentos sucesivos
- El **tiempo** es el eje X y la variable observada es el eje Y
- Ejemplos del mundo real:
  - Precio de una acción cada día
  - Temperatura a cada hora
  - Ventas de una tienda cada semana
  - Número de visitas a una web por hora

> La diferencia clave con otros datos: **el orden importa**. No puedes barajar las filas.

---

## Diapositiva 3 — Ejemplos cotidianos
## Todos conocemos series de tiempo sin saberlo
| Contexto | Variable | Frecuencia |
|----------|----------|------------|
| Tu teléfono | Uso de batería | Cada minuto |
| Una tienda | Ventas totales | Cada día |
| El clima | Temperatura | Cada hora |
| Streaming | Reproducciones | Cada mes |
| Tu cuenta bancaria | Saldo | Cada transacción |

---

## Diapositiva 4 — Paso 1: Convertir fechas con pandas
## Las fechas en texto no sirven para análisis
```python
import pandas as pd

df = pd.read_csv('datasets/ventas_tienda.csv')

# ANTES: la fecha es solo texto
print(df['fecha'].dtype)       # object (texto)

# Convertir a datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# DESPUÉS: pandas entiende que es una fecha
print(df['fecha'].dtype)       # datetime64[ns]
```

Ahora podemos extraer:
```python
df['anio']  = df['fecha'].dt.year
df['mes']   = df['fecha'].dt.month
df['dia']   = df['fecha'].dt.day
df['dow']   = df['fecha'].dt.day_name()  # lunes, martes...
```

---

## Diapositiva 5 — Paso 2: Fecha como índice
## Poner la fecha como índice permite muchas operaciones especiales
```python
df = df.set_index('fecha')
df = df.sort_index()  # ordenar cronológicamente

# Ahora puedes filtrar por rango de fechas
enero_2023 = df['2023-01']
todo_2023  = df['2023']
segundo_semestre = df['2023-07':'2023-12']
```

---

## Diapositiva 6 — Paso 3: Resample — agregar por periodo
## Como un groupby para tiempo
- En lugar de sumar por "mes" (que es un número), usamos `resample`
- `resample('M')` → agrupa por mes
- `resample('W')` → agrupa por semana
- `resample('D')` → agrupa por día
- `resample('Y')` → agrupa por año

```python
# Total de ventas por mes
ventas_mensuales = df['ventas'].resample('M').sum()

# Promedio diario por semana
promedio_semanal = df['ventas'].resample('W').mean()
```

---

## Diapositiva 7 — Paso 4: Rolling — promedio móvil
## Para suavizar el ruido y ver la tendencia
- Las ventas diarias tienen mucho "ruido" (días buenos y días malos)
- El **promedio móvil** suaviza esas variaciones
- `rolling(7)` → ventana de 7 días
- `rolling(30)` → ventana de 30 días

```python
# Promedio móvil de 7 días
df['media_7d'] = df['ventas'].rolling(window=7).mean()

# Comparar original vs suavizado
df[['ventas', 'media_7d']].plot(figsize=(12, 4))
```

> Es como calcular "el promedio de los últimos 7 días" para cada punto.

---

## Diapositiva 8 — Visualizar series de tiempo
## El gráfico más básico: línea a lo largo del tiempo
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 4))
ax.plot(df.index, df['ventas'], label='Ventas diarias', alpha=0.6)
ax.plot(df.index, df['media_7d'], label='Media 7 días', linewidth=2)
ax.set_xlabel('Fecha')
ax.set_ylabel('Ventas ($)')
ax.set_title('Ventas de la tienda en el tiempo')
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

---

## Diapositiva 9 — Tendencia y estacionalidad
## Las dos preguntas clave al analizar una serie de tiempo
| Patrón | Pregunta | Ejemplo |
|--------|----------|---------|
| **Tendencia** | ¿Las ventas están subiendo o bajando con el tiempo? | +5% cada año |
| **Estacionalidad** | ¿Hay un patrón que se repite cada ciclo? | Pico en diciembre |
| **Residuo** | ¿Qué queda después de quitar los dos anteriores? | Eventos aleatorios |

---

## Diapositiva 10 — Descomposición estacional con statsmodels
## Separar una serie en sus componentes
```python
from statsmodels.tsa.seasonal import seasonal_decompose

resultado = seasonal_decompose(
    ventas_mensuales,
    model='additive',  # tendencia + estacional + residuo
    period=12          # ciclo anual (12 meses)
)
resultado.plot()
plt.show()
```

Esto produce 4 gráficas:
1. Serie original
2. Tendencia
3. Componente estacional
4. Residuo

---

## Diapositiva 11 — Pronóstico simple
## Sin modelos complejos, hay buenas aproximaciones
| Método | Descripción | Cuándo usar |
|--------|-------------|-------------|
| Último valor | Siguiente = último observado | Serie estable |
| Media histórica | Siguiente = promedio de toda la serie | Sin tendencia |
| Promedio móvil | Siguiente = media de los últimos K periodos | Con ruido |
| Seasonal naive | Siguiente = mismo período del año anterior | Con estacionalidad |

```python
# Pronóstico simple: promedio móvil de los últimos 3 meses
ultimo_pronostico = ventas_mensuales.tail(3).mean()
print(f'Pronóstico próximo mes: ${ultimo_pronostico:,.0f}')
```

---

## Diapositiva 12 — Resumen
## Lo que aprendimos hoy
- Una serie de tiempo es una secuencia de valores **ordenados en el tiempo**
- `pd.to_datetime()` convierte texto a fechas que pandas puede procesar
- `resample()` agrega datos por periodo (mes, semana, año)
- `rolling()` calcula promedios móviles para suavizar tendencias
- La **tendencia** y la **estacionalidad** son los patrones más importantes a identificar
- `seasonal_decompose` separa una serie en tendencia + estacional + residuo

---

## Diapositiva 13 — Tarea para casa
## Homework — Clase 24
- Analiza las ventas de `ventas_tienda.csv` por mes durante el año disponible
- Calcula y grafica el promedio móvil de 3 meses
- Identifica el mes con más ventas y el de menos ventas
- Aplica `seasonal_decompose` y explica qué muestra cada componente
- Genera un pronóstico simple para el siguiente mes y justifícalo
