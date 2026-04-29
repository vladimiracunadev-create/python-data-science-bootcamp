# 💻 Guía de código — Clase 24: Series de Tiempo

> Walkthrough del código clave, bloque por bloque.

## Bloque 1: Cargar, indexar y resamplear una serie temporal

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("ventas_tienda.csv")

# Paso 1: convertir la columna de fecha a tipo datetime
df["fecha"] = pd.to_datetime(df["fecha"])

# Paso 2: establecer la fecha como índice
df = df.set_index("fecha")
df = df.sort_index()  # asegurar orden cronológico

print(f"Rango temporal: {df.index.min()} → {df.index.max()}")
print(f"Frecuencia detectada: {pd.infer_freq(df.index)}")

# Paso 3: resamplear a frecuencia mensual
ventas_mensuales = df["ventas"].resample("M").sum()

# Graficar serie mensual
plt.figure(figsize=(12, 4))
plt.plot(ventas_mensuales, marker="o", linewidth=1.5, color="steelblue")
plt.title("Ventas mensuales totales")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

**¿Qué hace?** Transforma una columna de fechas en texto a un índice temporal real, lo que permite todas las operaciones temporales de pandas: resample, rolling, slicing por fecha, etc.

**¿Por qué así?** Sin `pd.to_datetime()`, pandas trata las fechas como strings y no puede hacer operaciones temporales. `resample('M').sum()` agrupa todas las ventas de cada mes en un solo valor.

**Resultado esperado:** Una serie con una observación por mes. Puedes ver a simple vista si hay tendencia (¿sube o baja con el tiempo?) y estacionalidad (¿hay picos recurrentes?).

---

## Bloque 2: Media móvil para suavizar el ruido

```python
# Media móvil de 3 meses (suaviza fluctuaciones a corto plazo)
mm_3 = ventas_mensuales.rolling(window=3).mean()

# Media móvil de 6 meses (suaviza más, muestra tendencia general)
mm_6 = ventas_mensuales.rolling(window=6).mean()

plt.figure(figsize=(12, 5))
plt.plot(ventas_mensuales, alpha=0.4, label="Ventas originales", color="gray")
plt.plot(mm_3, label="Media móvil 3 meses", color="coral", linewidth=2)
plt.plot(mm_6, label="Media móvil 6 meses", color="steelblue", linewidth=2)
plt.title("Ventas mensuales con medias móviles")
plt.xlabel("Fecha")
plt.ylabel("Ventas")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Uso como pronóstico naive: último valor de la media móvil
ultimo_valor_mm6 = mm_6.iloc[-1]
print(f"Pronóstico naive (media móvil 6m) para el próximo mes: {ultimo_valor_mm6:.0f}")
```

**¿Qué hace?** `rolling(n).mean()` calcula el promedio de las últimas n observaciones en cada punto. Ventanas más grandes suavizan más pero reaccionan más lento a cambios recientes.

**¿Por qué así?** Las primeras `n-1` observaciones de la media móvil serán NaN porque no hay suficiente historial para calcularlas. Esto es esperado y correcto.

**Resultado esperado:** La media móvil de 6 meses muestra la tendencia general más claramente que la original; la de 3 meses es un intermedio. La serie original tiene más "ruido" visible.

---

## Bloque 3: Descomposición estacional con statsmodels

```python
from statsmodels.tsa.seasonal import seasonal_decompose

# Descomposición aditiva (componentes se suman)
# period=12 indica estacionalidad anual en datos mensuales
descomp = seasonal_decompose(
    ventas_mensuales.dropna(),
    model="additive",
    period=12
)

# Graficar los 4 componentes
fig, axes = plt.subplots(4, 1, figsize=(12, 10), sharex=True)

descomp.observed.plot(ax=axes[0], title="Serie original", color="steelblue")
descomp.trend.plot(ax=axes[1], title="Tendencia", color="coral")
descomp.seasonal.plot(ax=axes[2], title="Estacionalidad", color="green")
descomp.resid.plot(ax=axes[3], title="Residual (ruido)", color="gray")

for ax in axes:
    ax.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Identificar mes de mayor estacionalidad
mes_pico = descomp.seasonal.groupby(descomp.seasonal.index.month).mean().idxmax()
print(f"Mes con mayor componente estacional: {mes_pico}")
```

**¿Qué hace?** Descompone la serie en sus 3 componentes. En el modelo aditivo: `observado = tendencia + estacionalidad + residual`. Muestra cada componente por separado para analizarlos individualmente.

**¿Por qué así?** `model='additive'` asume que la amplitud de la estacionalidad es constante en el tiempo. Si la estacionalidad crece con el nivel de la serie (ej: pico de diciembre cada vez más grande), usar `model='multiplicative'`.

**Resultado esperado:** Cuatro subgráficos: el original con todos sus patrones, la tendencia suave (sube/baja sostenidamente), la estacionalidad que se repite cada año, y el residual (lo que no explicó el modelo).

---

## ⚠️ Errores comunes y cómo resolverlos

| Error | Por qué ocurre | Solución |
|---|---|---|
| `seasonal_decompose` da error de "period" | La serie tiene menos de 2 ciclos completos (menos de 24 meses para period=12) | Reducir `period` o usar más datos históricos |
| `rolling().mean()` devuelve NaN al inicio | Las primeras `window-1` observaciones no tienen suficiente historial | Esto es correcto; usar `min_periods=1` si necesitas valores desde la primera observación |
| `resample('M').sum()` da valores inesperados | La columna de fecha no es el índice o no es tipo datetime | Verificar `df.index.dtype` == `datetime64[ns]` antes de resamplear |
| Gráfico temporal con eje X desordenado | El índice datetime no está ordenado cronológicamente | Agregar `df = df.sort_index()` después de `set_index("fecha")` |
