# 💻 Guía de código — Clase 17: Estadística inferencial — pruebas de hipótesis

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Prueba t para comparar dos grupos

```python
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("transporte.csv")

# Separar los dos grupos a comparar
grupo_bus   = df[df["modo"] == "Bus"]["tiempo_minutos"]
grupo_metro = df[df["modo"] == "Metro"]["tiempo_minutos"]

# Visualizar las distribuciones antes de la prueba
plt.figure(figsize=(10, 4))
sns.histplot(grupo_bus,   label="Bus",   color="steelblue", alpha=0.5, bins=20)
sns.histplot(grupo_metro, label="Metro", color="orange",    alpha=0.5, bins=20)
plt.legend()
plt.title("Distribución de tiempos de viaje por modo de transporte")
plt.xlabel("Tiempo (minutos)")
plt.show()

# Realizar la prueba t de Student para dos muestras independientes
estadistico, p_valor = stats.ttest_ind(grupo_bus, grupo_metro)

print(f"Estadístico t: {estadistico:.4f}")
print(f"P-valor:       {p_valor:.4f}")

# Interpretar el resultado automáticamente
alpha = 0.05
if p_valor < alpha:
    print(f"\nCon p={p_valor:.4f} < α={alpha}: RECHAZAMOS H0")
    print("Hay evidencia estadística de que los tiempos son diferentes.")
else:
    print(f"\nCon p={p_valor:.4f} >= α={alpha}: NO rechazamos H0")
    print("No hay evidencia suficiente de diferencia significativa.")
```

**¿Qué hace este bloque?**
- `stats.ttest_ind(grupo_a, grupo_b)`: realiza la prueba t de Student para dos muestras independientes. Devuelve dos valores: el estadístico t y el p-valor.
- El **estadístico t** mide qué tan diferentes son las medias en unidades de error estándar. Un valor absoluto grande indica más diferencia.
- El **p-valor** es la probabilidad de observar una diferencia tan grande (o mayor) si H0 fuera verdadera, es decir, si no hubiera diferencia real entre los grupos.
- `alpha = 0.05` es el nivel de significancia: la probabilidad máxima de cometer un Error Tipo I (rechazar H0 cuando es verdadera) que estamos dispuestos a aceptar.

**¿Por qué se escribe así y no de otra forma?**
Siempre se visualizan las distribuciones primero para verificar que los datos son razonablemente "normales" y no tienen formas muy distintas (la prueba t asume aproximación a la normalidad). La interpretación con `if/else` hace el código autodescriptivo y útil como plantilla para futuros análisis.

**Resultado esperado:**
```
Estadístico t: 3.2145
P-valor:       0.0015

Con p=0.0015 < α=0.05: RECHAZAMOS H0
Hay evidencia estadística de que los tiempos son diferentes.
```

---

## Bloque 2: Prueba chi-cuadrado para variables categóricas

```python
df_est = pd.read_csv("estudiantes.csv")

# Crear tabla de contingencia
tabla = pd.crosstab(
    df_est["genero"],
    df_est["aprobado"],
    margins=True   # agrega totales por fila y columna
)
print("Tabla de contingencia:")
print(tabla)

# Prueba chi-cuadrado de independencia
chi2, p_valor, grados_libertad, freq_esperadas = stats.chi2_contingency(
    pd.crosstab(df_est["genero"], df_est["aprobado"])
)

print(f"\nEstadístico chi²:    {chi2:.4f}")
print(f"P-valor:             {p_valor:.4f}")
print(f"Grados de libertad:  {grados_libertad}")

alpha = 0.05
if p_valor < alpha:
    print(f"\nRESULTADO: Existe asociación significativa entre género y aprobación (p={p_valor:.4f})")
else:
    print(f"\nRESULTADO: No hay asociación significativa entre las variables (p={p_valor:.4f})")
```

**¿Qué hace este bloque?**
- `pd.crosstab(variable_fila, variable_columna)`: crea una tabla de contingencia que muestra cuántos casos hay en cada combinación de dos variables categóricas. Es el input requerido por la prueba chi-cuadrado.
- `stats.chi2_contingency(tabla)`: realiza la prueba chi-cuadrado de independencia. Devuelve 4 valores: el estadístico χ², el p-valor, los grados de libertad y las frecuencias esperadas bajo H0.
- Las **frecuencias esperadas** muestran cuántos casos habría en cada celda si las dos variables fueran completamente independientes entre sí.

**¿Por qué se escribe así y no de otra forma?**
Chi-cuadrado prueba si dos variables categóricas son independientes. La hipótesis nula es "las variables no están relacionadas". Se usa cuando las variables son categóricas (no numéricas), lo que lo diferencia de la prueba t que compara medias de variables numéricas.

**Resultado esperado:**
```
Tabla de contingencia:
aprobado    No  Sí  All
genero
Femenino    15  35   50
Masculino   20  30   50
All         35  65  100

Estadístico chi²:   0.9890
P-valor:            0.3199
Grados de libertad: 1
RESULTADO: No hay asociación significativa entre las variables (p=0.3199)
```

---

## Bloque 3: Intervalos de confianza

```python
tiempos = df["tiempo_minutos"]
nivel_confianza = 0.95

# Calcular el intervalo de confianza para la media
ic = stats.t.interval(
    confidence=nivel_confianza,
    df=len(tiempos) - 1,        # grados de libertad = n - 1
    loc=tiempos.mean(),          # media muestral como estimador puntual
    scale=stats.sem(tiempos)    # error estándar de la media
)

print(f"Media muestral: {tiempos.mean():.2f} minutos")
print(f"Error estándar: {stats.sem(tiempos):.2f}")
print(f"IC al {nivel_confianza*100:.0f}%: [{ic[0]:.2f}, {ic[1]:.2f}] minutos")

# Visualizar el intervalo sobre la distribución
plt.figure(figsize=(10, 4))
sns.histplot(tiempos, kde=True, color="steelblue")
plt.axvline(tiempos.mean(), color='red',   linestyle='--', label=f'Media: {tiempos.mean():.1f}')
plt.axvline(ic[0],          color='green', linestyle=':',  label=f'IC 95%: [{ic[0]:.1f}, {ic[1]:.1f}]')
plt.axvline(ic[1],          color='green', linestyle=':')
plt.legend()
plt.title("Distribución de tiempos con Intervalo de Confianza al 95%")
plt.xlabel("Tiempo (minutos)")
plt.show()
```

**¿Qué hace este bloque?**
- `stats.t.interval(confidence, df, loc, scale)`: calcula el intervalo de confianza usando la distribución t. Los parámetros son: nivel de confianza, grados de libertad (n-1), la media muestral y el error estándar.
- `stats.sem(tiempos)`: calcula el error estándar de la media (SEM = desviación estándar / √n). Mide qué tan precisa es la media muestral como estimador de la media poblacional.
- El resultado `ic` es una tupla con el límite inferior y el límite superior del intervalo.
- `plt.axvline(...)`: dibuja una línea vertical en el valor especificado.

**¿Por qué se escribe así y no de otra forma?**
El intervalo de confianza del 95% significa: si repitiéramos este muestreo muchas veces, el 95% de los intervalos calculados contendrían la verdadera media poblacional. No significa que hay 95% de probabilidad de que la media real esté en este intervalo específico (esa interpretación es incorrecta pero muy común).

**Resultado esperado:**
```
Media muestral: 32.45 minutos
Error estándar: 1.23
IC al 95%: [30.03, 34.87] minutos
```
Y un histograma con tres líneas verticales: la media en rojo (línea discontinua) y los límites del IC en verde (líneas punteadas).

---

## Bloque 4: Función reutilizable de prueba de hipótesis

```python
def prueba_t_completa(grupo1, grupo2, nombre1="Grupo 1", nombre2="Grupo 2", alpha=0.05):
    """Realiza una prueba t entre dos grupos con reporte completo."""
    print(f"{'='*50}")
    print(f"PRUEBA T: {nombre1} vs {nombre2}")
    print(f"{'='*50}")
    print(f"{nombre1}: n={len(grupo1)}, media={grupo1.mean():.2f}, std={grupo1.std():.2f}")
    print(f"{nombre2}: n={len(grupo2)}, media={grupo2.mean():.2f}, std={grupo2.std():.2f}")

    t_stat, p_valor = stats.ttest_ind(grupo1, grupo2)
    print(f"\nEstadístico t: {t_stat:.4f}")
    print(f"P-valor:       {p_valor:.4f}")

    # Tamaño del efecto: Cohen's d
    pooled_std = np.sqrt((grupo1.std()**2 + grupo2.std()**2) / 2)
    cohens_d = abs(grupo1.mean() - grupo2.mean()) / pooled_std
    print(f"Cohen's d:     {cohens_d:.3f}  ", end="")
    if cohens_d < 0.2:
        print("(efecto pequeño)")
    elif cohens_d < 0.8:
        print("(efecto mediano)")
    else:
        print("(efecto grande)")

    if p_valor < alpha:
        print(f"\n[RESULTADO] Diferencia SIGNIFICATIVA (p < {alpha})")
    else:
        print(f"\n[RESULTADO] Diferencia NO significativa (p >= {alpha})")

# Ejemplo de uso
ciudad_a = df[df["ciudad"] == "Ciudad A"]["tiempo_minutos"]
ciudad_b = df[df["ciudad"] == "Ciudad B"]["tiempo_minutos"]
prueba_t_completa(ciudad_a, ciudad_b, "Ciudad A", "Ciudad B")
```

**¿Qué hace este bloque?**
Esta función encapsula todo el proceso de una prueba de hipótesis en un flujo reutilizable. Calcula estadísticas descriptivas, ejecuta la prueba t, calcula el tamaño del efecto (Cohen's d) y muestra una interpretación clara.

**¿Por qué se escribe así y no de otra forma?**
El **tamaño del efecto** (Cohen's d) es fundamental porque complementa el p-valor. Un resultado puede ser estadísticamente significativo pero prácticamente irrelevante, especialmente con muestras muy grandes. Cohen's d mide la diferencia en unidades de desviación estándar: d < 0.2 es efecto pequeño, 0.5 mediano, 0.8 grande.

**Resultado esperado:**
```
==================================================
PRUEBA T: Ciudad A vs Ciudad B
==================================================
Ciudad A: n=120, media=28.5, std=8.2
Ciudad B: n=115, media=35.1, std=10.4

Estadístico t: -4.8821
P-valor:       0.0000
Cohen's d:     0.718  (efecto mediano)

[RESULTADO] Diferencia SIGNIFICATIVA (p < 0.05)
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| P-valor imprime 0.0 exacto | El float es tan pequeño que se redondea a cero con `.4f` | Usar notación científica: `f"{p_valor:.2e}"` para ver ej. `3.2e-08` |
| Prueba t con datos muy no normales y n < 30 | La t-test asume normalidad aproximada; con pocos datos y distribución muy sesgada no es válida | Usar la prueba no paramétrica Mann-Whitney: `stats.mannwhitneyu(a, b)` |
| `chi2_contingency` da advertencia de frecuencias bajas | El test chi² no es confiable cuando celdas tienen frecuencia esperada < 5 | Combinar categorías poco frecuentes en "Otros" o usar el test exacto de Fisher |
| Rechazar H0 siempre con datasets muy grandes | Con millones de datos, diferencias minúsculas son "significativas" estadísticamente | Siempre reportar el tamaño del efecto (Cohen's d) además del p-valor |
| Interpretar "no rechazar H0" como "probar que H0 es verdadera" | Ausencia de evidencia no es evidencia de ausencia | "No rechazar H0" solo significa que no tenemos suficiente evidencia; no prueba que H0 sea cierta |
