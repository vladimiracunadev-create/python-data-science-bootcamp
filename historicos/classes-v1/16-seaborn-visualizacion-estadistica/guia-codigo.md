# 💻 Guía de código — Clase 16: Seaborn y visualización estadística

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Distribuciones con histplot y kdeplot

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("ventas_tienda.csv")
sns.set_theme(style="whitegrid")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Panel izquierdo: histograma con KDE superpuesto
sns.histplot(data=df, x="ventas", bins=20, kde=True, ax=axes[0])
axes[0].set_title("Distribución de Ventas")
axes[0].set_xlabel("Ventas (unidades)")
axes[0].set_ylabel("Frecuencia")

# Panel derecho: KDE separado por categoría
sns.kdeplot(data=df, x="ventas", hue="categoría", ax=axes[1])
axes[1].set_title("Densidad de Ventas por Categoría")
axes[1].set_xlabel("Ventas (unidades)")

plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?**
- `sns.set_theme(style="whitegrid")`: aplica un tema visual global a todos los gráficos de la sesión. `"whitegrid"` pone un fondo blanco con líneas de cuadrícula grises.
- `plt.subplots(1, 2, figsize=(14, 5))`: crea una figura con 1 fila y 2 columnas de paneles (subgráficos), de 14×5 pulgadas de ancho total.
- `sns.histplot(..., bins=20, kde=True)`: dibuja un histograma dividiendo los datos en 20 intervalos de igual ancho. `kde=True` superpone la curva de densidad estimada (una versión suavizada de la distribución).
- `hue="categoría"`: colorea una curva diferente por cada valor único en `categoría`.
- `plt.tight_layout()`: ajusta automáticamente los márgenes para que los paneles no se superpongan.

**¿Por qué se escribe así y no de otra forma?**
El histograma muestra frecuencias discretas (cuántos datos caen en cada rango). El KDE muestra la distribución como una curva continua suavizada. Combinarlos con `kde=True` da más información visual: ves la distribución discreta y la forma general al mismo tiempo.

**Resultado esperado:**
Panel izquierdo: barras de histograma con una curva suave encima. Panel derecho: múltiples curvas de densidad de diferentes colores, una por cada categoría, con leyenda automática.

---

## Bloque 2: Boxplot y violinplot para comparar grupos

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Boxplot: muestra Q1, mediana, Q3 y outliers
sns.boxplot(
    data=df,
    x="categoría",
    y="ventas",
    palette="Set2",
    ax=axes[0]
)
axes[0].set_title("Boxplot: Ventas por Categoría")
axes[0].set_xlabel("Categoría")
axes[0].set_ylabel("Ventas")
axes[0].tick_params(axis='x', rotation=45)

# Violinplot: misma info + forma completa de la distribución
sns.violinplot(
    data=df,
    x="categoría",
    y="ventas",
    palette="Set2",
    inner="box",      # muestra el boxplot compacto dentro del violín
    ax=axes[1]
)
axes[1].set_title("Violinplot: Ventas por Categoría")
axes[1].set_xlabel("Categoría")
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?**
- `sns.boxplot(x="categoría", y="ventas")`: crea un boxplot por cada categoría. Muestra: la caja (del cuartil 1 al cuartil 3), la línea horizontal dentro de la caja (la mediana), los bigotes (rango sin outliers) y puntos separados (valores atípicos u outliers).
- `palette="Set2"`: usa una paleta de colores predefinida de Seaborn. Otras opciones populares: `"pastel"`, `"muted"`, `"tab10"`.
- `inner="box"` en el violinplot: dibuja un boxplot compacto dentro del violín para ver medianas y cuartiles sin perder la información de forma.
- `tick_params(axis='x', rotation=45)`: rota las etiquetas del eje X 45 grados para que no se superpongan cuando son largas.

**¿Por qué se escribe así y no de otra forma?**
El boxplot es más compacto y familiar para audiencias técnicas. El violinplot muestra la forma completa de la distribución (si es bimodal, asimétrica, etc.) con más detalle que el boxplot. Usar `inner="box"` combina las ventajas de ambos en un solo gráfico.

**Resultado esperado:**
Dos paneles. En el boxplot: cajas rectangulares con bigotes, la línea de mediana visible dentro, y puntos separados para outliers. En el violinplot: figuras en forma de violín (más anchas donde hay más datos concentrados) con un boxplot mini en el centro.

---

## Bloque 3: Heatmap de correlación

```python
# Seleccionar solo columnas numéricas
numericas = df.select_dtypes(include='number')

# Calcular la matriz de correlación de Pearson
correlación = numericas.corr()

# Crear el heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    correlación,
    annot=True,          # escribe el valor numérico en cada celda
    fmt=".2f",           # formato: 2 decimales
    cmap="coolwarm",     # paleta divergente: azul=negativo, rojo=positivo
    vmin=-1, vmax=1,     # fija la escala de color entre -1 y 1
    linewidths=0.5,      # líneas finas entre celdas para separación visual
    square=True          # celdas cuadradas (no rectangulares)
)
plt.title("Mapa de Calor: Correlación entre Variables Numéricas")
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?**
- `df.select_dtypes(include='number')`: filtra el DataFrame para quedarse solo con columnas numéricas (tipo `int` o `float`).
- `.corr()`: calcula el coeficiente de correlación de Pearson entre todos los pares de columnas. Devuelve una matriz cuadrada donde cada celda es un valor entre -1 y 1.
- `annot=True`: escribe el valor numérico de la correlación dentro de cada celda del heatmap, lo que hace el gráfico autodescriptivo.
- `cmap="coolwarm"`: usa colores divergentes — azul intenso para correlación negativa fuerte, rojo intenso para positiva fuerte, y blanco/gris para cercana a cero.
- `vmin=-1, vmax=1`: ancla la escala de colores al rango teórico de la correlación para que sea comparable entre distintos datasets.

**¿Por qué se escribe así y no de otra forma?**
El heatmap de correlación es una herramienta clave en el análisis exploratorio para identificar rápidamente qué variables se mueven juntas (correlación positiva alta) o en sentido opuesto (negativa). Es especialmente importante antes de construir modelos, porque variables muy correlacionadas entre sí pueden causar problemas de multicolinealidad.

**Resultado esperado:**
Una cuadrícula de colores donde la diagonal principal siempre es 1.0 (rojo intenso, ya que cada variable correlaciona perfectamente consigo misma). Celdas con valores cercanos a 1 son rojo, cercanas a -1 son azul, y cercanas a 0 son blancas.

---

## Bloque 4: Scatterplot con múltiples dimensiones

```python
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="precio",
    y="ventas",
    hue="categoría",    # color por categoría (dimensión 3)
    size="descuento",   # tamaño del punto por variable numérica (dimensión 4)
    alpha=0.7,          # transparencia para ver puntos superpuestos
    palette="tab10"
)
plt.title("Ventas vs Precio por Categoría y Descuento")
plt.xlabel("Precio unitario")
plt.ylabel("Unidades vendidas")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?**
- `hue="categoría"`: asigna un color diferente a cada valor único en `categoría`. Seaborn genera la leyenda automáticamente.
- `size="descuento"`: varía el tamaño de cada punto proporcionalmente al valor de `descuento`. Permite visualizar 4 dimensiones en un gráfico 2D: eje X, eje Y, color y tamaño.
- `alpha=0.7`: aplica 70% de opacidad a los puntos. Cuando muchos puntos se superponen, la transparencia permite ver la densidad (zonas más oscuras = más puntos).
- `bbox_to_anchor=(1.05, 1)`: posiciona la leyenda fuera del área del gráfico (a la derecha) para no tapar los datos.

**¿Por qué se escribe así y no de otra forma?**
El scatterplot con `hue` y `size` es una forma eficiente de explorar múltiples relaciones simultáneamente en una sola figura. Sin embargo, si hay demasiadas categorías, el gráfico se vuelve difícil de leer — en ese caso conviene usar `FacetGrid` para crear un panel por categoría.

**Resultado esperado:**
Un gráfico de dispersión con puntos de distintos colores (una por categoría) y distintos tamaños (proporcionales al descuento). Se aprecian agrupaciones visuales si las categorías tienen diferentes rangos de precio o ventas.

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| `ValueError: Could not interpret input 'columna'` | El nombre de columna no existe en el DataFrame o está mal escrito | Verificar con `df.columns.tolist()` que el nombre sea exacto (respeta mayúsculas) |
| El gráfico aparece muy pequeño o pixelado | No se configuró `figsize` antes de crear el gráfico | Agregar `plt.figure(figsize=(12, 6))` antes del comando de Seaborn |
| Los colores no cambian con `hue` | La columna en `hue` tiene tipo numérico en vez de categórico | Convertir con `df['col'] = df['col'].astype(str)` antes de graficar |
| La leyenda tapa el contenido del gráfico | Hay muchas categorías y la leyenda se genera dentro del área | Mover con `plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')` |
| `pairplot` tarda mucho o se cuelga | El DataFrame tiene muchas filas o muchas columnas numéricas | Seleccionar solo las columnas relevantes: `sns.pairplot(df[['col1','col2','col3']])` |
