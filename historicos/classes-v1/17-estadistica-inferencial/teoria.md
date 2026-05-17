# 🧠 Documento teórico — Clase 17: Estadística inferencial — pruebas de hipótesis
> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central
Las pruebas de hipótesis nos dicen si una diferencia que vemos en los datos es real o simplemente producto del azar.

## ❓ Por qué importa este módulo
En ciencia de datos, observar una diferencia no es suficiente. Si el promedio de retrasos en días lluviosos es 12 minutos y en días secos es 10 minutos, ¿eso es una diferencia real o simplemente variación normal? Sin una herramienta formal, cualquier conclusión es especulación. Las pruebas de hipótesis dan una respuesta probabilística rigurosa a esa pregunta, y son la base de toda investigación científica, médica, económica y tecnológica.

## 💻 Bloque de código documentado

### Estadística descriptiva vs inferencial
La diferencia fundamental entre ambos enfoques.

**Qué hace:** La descriptiva resume lo que ya tienes. La inferencial usa una muestra para sacar conclusiones sobre una población más grande.
**Para qué sirve:** Entender este límite es fundamental para no sobreinterpretar los datos.

```python
import pandas as pd
import numpy as np
from scipy import stats

# Carga de datos
transporte = pd.read_csv("datasets/transporte.csv")
estudiantes = pd.read_csv("datasets/estudiantes.csv")

# Estadística descriptiva: resume lo que tenemos
print("=== DESCRIPTIVA ===")
print(transporte.groupby("lluvia")["retraso_min"].describe())

# La inferencial va más lejos: ¿esta diferencia aplica más allá de esta muestra?
```

### Hipótesis nula y alternativa (H0 y H1)
**Qué hace:** Define formalmente las dos posibilidades antes de analizar los datos.
**Para qué sirve:** Establece el marco de la prueba. H0 siempre es la posición de "no hay diferencia". H1 es lo que queremos comprobar.

```python
# Pregunta de investigación:
# ¿El tiempo de retraso es diferente en días con lluvia vs sin lluvia?

# H0 (hipótesis nula):    La media de retraso en días con lluvia
#                         es IGUAL a la media en días sin lluvia.
# H1 (hipótesis alternativa): La media de retraso en días con lluvia
#                              es DIFERENTE a la media en días sin lluvia.

# Separar los dos grupos
con_lluvia = transporte[transporte["lluvia"] == True]["retraso_min"]
sin_lluvia = transporte[transporte["lluvia"] == False]["retraso_min"]

print(f"Promedio con lluvia:    {con_lluvia.mean():.2f} min")
print(f"Promedio sin lluvia:    {sin_lluvia.mean():.2f} min")
print(f"Diferencia observada:   {con_lluvia.mean() - sin_lluvia.mean():.2f} min")
```

### Prueba t de Student para dos grupos independientes
**Qué hace:** Calcula el estadístico t y el p-value para determinar si la diferencia de medias entre dos grupos es estadísticamente significativa.
**Para qué sirve:** Para comparar el promedio de una variable numérica entre dos grupos cuando las observaciones son independientes entre sí.

```python
# Prueba t para comparar retrasos en días con y sin lluvia
estadistico_t, p_value = stats.ttest_ind(con_lluvia, sin_lluvia)

print(f"Estadístico t:  {estadistico_t:.4f}")
print(f"p-value:        {p_value:.4f}")
print()

# Interpretación basada en umbral estándar de 0.05
if p_value < 0.05:
    print("✅ Rechazamos H0: la diferencia de retrasos ES estadísticamente significativa.")
    print("   Es muy poco probable que esta diferencia sea solo producto del azar.")
else:
    print("❌ No rechazamos H0: no hay evidencia suficiente de diferencia real.")
    print("   La diferencia observada podría deberse al azar.")
```

### El p-value explicado con la analogía de la moneda
**Qué hace:** Ilustra conceptualmente qué significa el p-value antes de usarlo con datos reales.
**Para qué sirve:** Hace accesible un concepto que suele confundirse con "la probabilidad de que H0 sea verdadera" (que no lo es).

```python
# Simulación: moneda lanzada 100 veces
# ¿Cuántas veces hay que sacar "cara" para sospechar que la moneda está cargada?

np.random.seed(42)
resultados = []

for _ in range(10000):
    # Simular 100 lanzamientos con una moneda justa (p=0.5)
    lanzamientos = np.random.binomial(1, 0.5, 100)
    resultados.append(lanzamientos.sum())

# ¿Con qué frecuencia una moneda justa da 60+ caras?
prob_60_o_mas = (np.array(resultados) >= 60).mean()
print(f"Probabilidad de obtener 60+ caras con moneda justa: {prob_60_o_mas:.4f}")
# Si p < 0.05, sospecharíamos que la moneda no es justa
# Eso es exactamente lo que hace una prueba de hipótesis
```

### Intervalos de confianza
**Qué hace:** Calcula el rango dentro del cual se espera que caiga el verdadero parámetro de la población con un 95% de confianza.
**Para qué sirve:** Agrega contexto a la estimación puntual (la media de la muestra) mostrando cuánta incertidumbre existe.

```python
# Intervalo de confianza del 95% para el retraso promedio con lluvia
n = len(con_lluvia)
media = con_lluvia.mean()
error_estandar = stats.sem(con_lluvia)  # error estándar de la media

# Calcular intervalo con scipy
ic_inferior, ic_superior = stats.t.interval(0.95, df=n-1, loc=media, scale=error_estandar)

print(f"Media muestral:          {media:.2f} min")
print(f"Intervalo de confianza:  [{ic_inferior:.2f}, {ic_superior:.2f}] min")
print("Interpretación: si repitiéramos el muestreo 100 veces,")
print("en ~95 de ellas el intervalo contendría la media real de la población.")
```

### Prueba chi-cuadrado para variables categóricas
**Qué hace:** Compara las frecuencias observadas de categorías entre dos grupos con las frecuencias que se esperarían si no hubiera relación entre ellos.
**Para qué sirve:** Para determinar si dos variables categóricas están relacionadas. Por ejemplo: ¿el resultado del examen (aprobado/reprobado) depende del curso?

```python
# ¿Hay relación entre el curso y si el estudiante aprobó?
estudiantes["aprobado"] = estudiantes["nota_final"] >= 60

# Tabla de contingencia: frecuencia de cada combinación curso × aprobado
tabla = pd.crosstab(estudiantes["curso"], estudiantes["aprobado"])
print("Tabla de contingencia:")
print(tabla)
print()

# Prueba chi-cuadrado
chi2, p_value, grados_libertad, frecuencias_esperadas = stats.chi2_contingency(tabla)

print(f"Chi-cuadrado:       {chi2:.4f}")
print(f"p-value:            {p_value:.4f}")
print(f"Grados de libertad: {grados_libertad}")
print()

if p_value < 0.05:
    print("✅ Hay una relación estadísticamente significativa entre el curso y la aprobación.")
else:
    print("❌ No hay evidencia suficiente de relación entre el curso y la aprobación.")
```

### Errores tipo I y tipo II
**Qué hace:** Define los dos tipos de errores posibles en una prueba de hipótesis.
**Para qué sirve:** Para entender los límites de cualquier conclusión estadística y comunicar los resultados con honestidad.

```python
# Visualización conceptual de los errores
print("=== TABLA DE DECISIONES ===")
print()
print("                    | Realidad: H0 verdadera | Realidad: H0 falsa")
print("--------------------|------------------------|--------------------")
print("Decisión: Rechazar  | Error tipo I (falsa    | Decisión CORRECTA")
print("H0                  | alarma) — alfa = 0.05  | (potencia estadística)")
print("--------------------|------------------------|--------------------")
print("Decisión: No        | Decisión CORRECTA      | Error tipo II")
print("rechazar H0         |                        | (detección fallida) — beta")
print()
print("Recuerda: alfa = 0.05 significa que aceptamos un 5% de chance")
print("de cometer un error tipo I cada vez que hacemos una prueba.")
```

## ⚠️ Errores frecuentes a vigilar
- Interpretar p < 0.05 como "la diferencia es grande o importante": el p-value solo dice si es probable que sea real, no si es relevante en la práctica.
- Confundir "no rechazar H0" con "probar que H0 es verdadera": no encontrar evidencia no es lo mismo que probar que no hay diferencia.
- Hacer muchas pruebas sobre el mismo dataset sin corrección: si haces 20 pruebas con alfa=0.05, esperas al menos una positiva por azar.
- Mezclar la prueba t con la chi-cuadrado: la t es para variables numéricas continuas; la chi-cuadrado, para variables categóricas.
- No revisar los supuestos de la prueba t (normalidad aproximada, varianzas similares) antes de aplicarla.

## 🔗 Conexión con el siguiente módulo
En la Clase 18, daremos un paso más allá del análisis: prepararemos las variables del dataset para que sean útiles como entrada a un modelo de machine learning. El feature engineering transforma el entendimiento estadístico que desarrollamos aquí en insumos concretos para el modelado predictivo.
