# 🎞️ Slides — Clase 23: Reducción de dimensionalidad — PCA

---

## Diapositiva 1 — Título
# Reducción de dimensionalidad
## PCA: Principal Component Analysis
### ¿Cómo comprimir muchas variables en pocas sin perder lo importante?

---

## Diapositiva 2 — El problema: demasiadas columnas
## ¿Qué pasa cuando tienes 50 columnas?
- Con 2 variables puedes hacer un scatter plot y ver todo
- Con 3 variables quizás un gráfico 3D
- Con 50 variables... ¿cómo lo visualizas?
- **El problema:**
  - Más columnas = más lento el aprendizaje
  - Más columnas = más difícil encontrar patrones
  - Muchas columnas están **correlacionadas** (dicen casi lo mismo)

---

## Diapositiva 3 — La maldición de la dimensionalidad
## Por qué demasiadas dimensiones son un problema
- En 1D: puedes cubrir el espacio con 10 puntos
- En 2D: necesitas 100 puntos (10²)
- En 10D: necesitas 10.000.000.000 puntos (10¹⁰)
- Los datos se vuelven **muy dispersos** en espacios de alta dimensión
- Los algoritmos de ML necesitan más datos para aprender bien

> A esto se le llama la **"maldición de la dimensionalidad"** (curse of dimensionality).

---

## Diapositiva 4 — La solución: reducir dimensiones
## Queremos pasar de muchas columnas a pocas
- De 10 columnas → 2 columnas
- Sin perder demasiada información
- Las nuevas columnas son **combinaciones** de las originales
- Este proceso se llama **reducción de dimensionalidad**

Casos de uso:
- Visualización de datos de alta dimensión
- Eliminar ruido y redundancia
- Acelerar modelos de ML
- Detectar estructura latente en los datos

---

## Diapositiva 5 — La analogía de la sombra
## PCA es como encontrar la mejor sombra
- Imagina una pelota de béisbol frente a una lámpara
- La sombra en la pared es una versión 2D del objeto 3D
- Si la rotas, algunas sombras revelan más la forma que otras
- **PCA elige el ángulo que produce la sombra más informativa**
  - La que captura la mayor varianza posible
  - La que "pierde" menos información en la proyección

---

## Diapositiva 6 — ¿Cómo funciona PCA?
## PCA encuentra las direcciones de mayor varianza
1. Centra los datos (resta la media de cada columna)
2. Calcula la dirección donde los datos varían **más** → primera componente principal (PC1)
3. Calcula la dirección perpendicular a PC1 con la segunda mayor varianza → PC2
4. Proyecta todos los puntos sobre estas nuevas direcciones

> Las componentes principales son combinaciones lineales de las columnas originales.

---

## Diapositiva 7 — PCA en sklearn
## Solo 3 pasos
```python
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# 1. Escalar (¡siempre antes de PCA!)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 2. Crear y ajustar PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)  # shape: (n_filas, 2)

# 3. Ver cuánta información conservamos
print(pca.explained_variance_ratio_)
```

---

## Diapositiva 8 — Explained Variance Ratio
## ¿Cuánta información conservamos?
```
explained_variance_ratio_ = [0.58, 0.23]
```
- **PC1 explica el 58%** de la varianza total
- **PC2 explica el 23%** de la varianza total
- **Juntas: 81%** de la información original

> Si dos componentes explican más del 70-80%, la reducción es buena.

```python
varianza_acumulada = pca.explained_variance_ratio_.cumsum()
print(f'Varianza explicada acumulada: {varianza_acumulada}')
```

---

## Diapositiva 9 — Visualización de las componentes
## Scatter plot en 2D con PCA
```python
import matplotlib.pyplot as plt

plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.title('Datos reducidos a 2 dimensiones con PCA')
plt.show()
```

---

## Diapositiva 10 — Biplot: variables y muestras juntas
## El biplot muestra dos cosas a la vez
- **Puntos**: cada fila del dataset proyectada en 2D
- **Flechas**: cada variable original, indicando su dirección e influencia
- Si dos flechas apuntan en la misma dirección → esas variables están correlacionadas
- Si una flecha es larga → esa variable contribuye mucho a ese componente

```python
# Cargar vectores de las variables
loadings = pca.components_.T
for i, col in enumerate(columnas):
    plt.arrow(0, 0, loadings[i, 0]*3, loadings[i, 1]*3,
              head_width=0.1, color='red')
    plt.text(loadings[i, 0]*3.2, loadings[i, 1]*3.2, col)
```

---

## Diapositiva 11 — PCA + Clustering
## PCA hace que el clustering sea más fácil
1. Reducir a 2 dimensiones con PCA
2. Aplicar K-Means en el espacio 2D
3. Visualizar directamente con scatter plot coloreado

```python
# PCA → K-Means → Visualización
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_2d)

plt.scatter(X_2d[:, 0], X_2d[:, 1], c=kmeans.labels_, cmap='tab10')
```

---

## Diapositiva 12 — Cuándo usar PCA
## Usa PCA cuando...
| Situación | ¿Usar PCA? |
|-----------|-----------|
| Tienes más de 10 columnas numéricas | ✅ Sí |
| Quieres visualizar datos en 2D | ✅ Sí |
| Antes de K-Means con muchas variables | ✅ Sí |
| Para velocidad en modelos ML | ✅ Sí |
| Necesitas interpretar exactamente qué mide cada componente | ❌ No ideal |
| Tienes columnas categóricas | ❌ No (PCA solo trabaja con números) |

---

## Diapositiva 13 — Resumen
## Lo que aprendimos hoy
- La **maldición de la dimensionalidad**: más variables = más problemas
- **PCA** comprime muchas variables en pocas componentes
- `explained_variance_ratio_`: mide cuánta información se conserva
- El **biplot** muestra muestras y variables en el mismo espacio 2D
- PCA + clustering = una combinación muy poderosa
- La limitación de PCA: las componentes son difíciles de interpretar directamente
