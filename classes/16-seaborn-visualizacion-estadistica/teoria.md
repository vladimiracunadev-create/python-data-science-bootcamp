# 🧠 Documento teórico — Clase 16: Seaborn y visualización estadística
> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central
Seaborn convierte datos en gráficos estadísticos con pocas líneas de código, revelando patrones que las tablas ocultan.

## ❓ Por qué importa este módulo
Cuando tienes miles de filas de datos, es imposible entender la estructura leyendo la tabla. Un gráfico bien elegido puede mostrar en segundos lo que tomaría horas analizar en texto: dónde están los valores extremos, qué variable tiene mayor variación, si dos grupos se comportan distinto, si dos variables van juntas. Seaborn está diseñado específicamente para este tipo de análisis estadístico visual, y su sintaxis es directa y expresiva.

## 💻 Bloque de código documentado

### Configuración inicial y carga de datos
Antes de graficar, se importan las librerías y se aplica un tema visual.

**Qué hace:** Importa seaborn, matplotlib y pandas, luego establece un estilo visual uniforme para todos los gráficos de la sesión.
**Para qué sirve:** Garantiza que todos los gráficos tengan consistencia visual y que las fuentes, colores y fondos sean legibles sin configuración extra.

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Aplica un tema visual a todos los gráficos de la sesión
sns.set_theme(style="whitegrid", palette="muted")

# Carga los datos
ventas = pd.read_csv("datasets/ventas_tienda.csv")
estudiantes = pd.read_csv("datasets/estudiantes.csv")
```

### Histograma y curva de densidad
Permiten ver cómo se distribuyen los valores de una variable numérica.

**Qué hace:** `histplot` divide los valores en rangos (bins) y muestra cuántos caen en cada uno. `kdeplot` traza una curva suave que estima la distribución.
**Para qué sirve:** Para entender si los datos son simétricos, si tienen una cola larga, o si hay múltiples grupos mezclados.

```python
# Distribución de ventas diarias
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Histograma: muestra la frecuencia de cada rango de valores
sns.histplot(data=ventas, x="total_venta", bins=30, kde=True, ax=axes[0])
axes[0].set_title("Distribución de ventas diarias")

# KDE puro: curva de densidad sin barras, más suave
sns.kdeplot(data=ventas, x="total_venta", fill=True, ax=axes[1])
axes[1].set_title("Densidad de ventas diarias")

plt.tight_layout()
plt.show()
```

### Boxplot: distribución por categoría con outliers
**Qué hace:** Muestra la mediana, el rango intercuartílico (caja) y los valores atípicos (puntos fuera de los bigotes) para cada categoría.
**Para qué sirve:** Para comparar cómo se comporta una variable numérica en distintos grupos. Es ideal para detectar si hay diferencias sistemáticas entre categorías.

```python
# Ventas por categoría de producto
plt.figure(figsize=(10, 5))
sns.boxplot(data=ventas, x="categoria", y="total_venta", palette="Set2")
plt.title("Distribución de ventas por categoría")
plt.xlabel("Categoría de producto")
plt.ylabel("Total de venta")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### Violinplot: boxplot + densidad combinados
**Qué hace:** Combina el boxplot con una estimación de densidad a cada lado, formando una figura en forma de violín.
**Para qué sirve:** Muestra no solo dónde están los valores típicos, sino también la forma completa de la distribución. Es más informativo que el boxplot cuando los datos tienen formas irregulares.

```python
# Notas por curso, con forma de distribución visible
plt.figure(figsize=(10, 5))
sns.violinplot(data=estudiantes, x="curso", y="nota_final", palette="pastel", inner="quartile")
plt.title("Distribución de notas por curso")
plt.xlabel("Curso")
plt.ylabel("Nota final")
plt.tight_layout()
plt.show()
```

### Barplot con intervalos de confianza
**Qué hace:** Calcula el promedio de una variable numérica por categoría y dibuja una barra. Las líneas verticales en cada barra representan el intervalo de confianza del 95%.
**Para qué sirve:** Para comparar promedios entre grupos y ver cuánta incertidumbre hay en cada estimación. Útil en reportes y presentaciones.

```python
# Promedio de ventas por día de la semana
plt.figure(figsize=(8, 4))
sns.barplot(data=ventas, x="dia_semana", y="total_venta", palette="Blues_d",
            order=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])
plt.title("Promedio de ventas por día de la semana")
plt.xlabel("Día")
plt.ylabel("Venta promedio")
plt.tight_layout()
plt.show()
```

### Scatterplot con hue y size
**Qué hace:** Dibuja un punto por cada fila del dataset. El color (`hue`) y el tamaño (`size`) de cada punto pueden codificar variables adicionales.
**Para qué sirve:** Para explorar la relación entre dos variables numéricas y al mismo tiempo ver cómo una tercera variable (como la categoría o el canal) se superpone.

```python
# Relación entre unidades vendidas y total de venta, coloreado por categoría
plt.figure(figsize=(9, 5))
sns.scatterplot(data=ventas, x="unidades", y="total_venta",
                hue="categoria", size="descuento", sizes=(20, 200), alpha=0.7)
plt.title("Unidades vs Total de venta por categoría")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
```

### Heatmap de correlación
**Qué hace:** Muestra la correlación entre todas las variables numéricas del dataset en una grilla de colores. Valores cercanos a 1 son correlaciones positivas fuertes; cercanos a -1 son negativas fuertes.
**Para qué sirve:** Para identificar de un vistazo qué variables están relacionadas entre sí, lo que es especialmente útil antes de construir modelos.

```python
# Seleccionar solo columnas numéricas
numericas = ventas.select_dtypes(include="number")

# Calcular la matriz de correlación
correlacion = numericas.corr()

# Visualizar como heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlacion, annot=True, fmt=".2f", cmap="coolwarm", center=0,
            linewidths=0.5, square=True)
plt.title("Matriz de correlación — Ventas")
plt.tight_layout()
plt.show()
```

### Pairplot: exploración de relaciones múltiples
**Qué hace:** Genera una grilla de gráficos donde cada par de variables tiene su propio scatterplot. La diagonal muestra la distribución de cada variable por separado.
**Para qué sirve:** Para explorar todas las relaciones entre variables numéricas en un solo vistazo. Es una herramienta de exploración inicial muy poderosa.

```python
# Pairplot de variables numéricas de estudiantes, coloreado por modalidad
sns.pairplot(estudiantes[["nota_final", "asistencia", "horas_estudio", "modalidad"]],
             hue="modalidad", plot_kws={"alpha": 0.6})
plt.suptitle("Relaciones entre variables de estudiantes", y=1.02)
plt.show()
```

## ⚠️ Errores frecuentes a vigilar
- Usar el gráfico incorrecto: un `barplot` sobre datos sin promedios claros puede ser engañoso; el `boxplot` o `violinplot` suele ser más honesto.
- Olvidar `plt.tight_layout()`: provoca que los títulos y etiquetas se superpongan.
- Confundir `hue` (color por categoría) con `palette` (esquema de colores general).
- Llamar `plt.show()` antes de terminar de configurar el gráfico: el gráfico se cierra y los cambios posteriores se pierden.
- No leer los ejes antes de interpretar: siempre verificar las escalas y unidades.

## 🔗 Conexión con el siguiente módulo
En la Clase 17, usaremos lo que vemos visualmente en los gráficos para hacer una pregunta más precisa: ¿esta diferencia que noto entre grupos es estadísticamente real, o pudo ocurrir por azar? Las visualizaciones de esta clase serán el punto de partida para formular hipótesis formales.
