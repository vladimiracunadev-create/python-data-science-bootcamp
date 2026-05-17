# 📖 Teoría — Clase 23: Reducción de dimensionalidad — PCA

---

## 1. El problema de la alta dimensionalidad

Cuando hablamos de "dimensionalidad" en datos, nos referimos al número de variables (columnas) de nuestro dataset. Un dataset con 3 columnas vive en un espacio 3D. Uno con 50 columnas vive en un espacio 50-dimensional.

¿Cuál es el problema? A medida que aumenta el número de dimensiones, los datos se vuelven progresivamente más difíciles de analizar:

- **Visualización**: solo podemos ver hasta 3 dimensiones directamente. Con 50 columnas, necesitamos elegir qué pares de variables mostrar, y hay miles de combinaciones.
- **Distancia**: en espacios de alta dimensión, todos los puntos tienden a estar igualmente lejos entre sí. Los algoritmos basados en distancias (como K-Means o KNN) pierden efectividad.
- **Redundancia**: muchas columnas están altamente correlacionadas. Por ejemplo, "nota_matematicas" y "nota_fisica" suelen moverse juntas. Incluir ambas aporta poca información nueva pero sí añade ruido.
- **Overfitting**: más variables = mayor riesgo de que el modelo aprenda ruido.

A este conjunto de problemas se le llama la **maldición de la dimensionalidad** (*curse of dimensionality*).

---

## 2. ¿Qué es la reducción de dimensionalidad?

La reducción de dimensionalidad es el proceso de transformar un dataset con muchas columnas en uno con pocas columnas, intentando **conservar la mayor cantidad de información posible**.

La idea clave: si 3 columnas están muy correlacionadas, podemos "resumirlas" en 1 o 2 nuevas variables que capturen casi toda su varianza conjunta. Esas nuevas variables son **combinaciones lineales** de las originales.

Tipos principales:
- **PCA (Principal Component Analysis)**: lineal, basado en varianza
- **t-SNE**: no lineal, excelente para visualización
- **UMAP**: no lineal, rápido y escalable

En esta clase nos enfocamos en **PCA**, el más usado en práctica.

---

## 3. Intuición de PCA

Imagina que tienes una nube de puntos en 3D que tiene forma de "plato" — está bastante aplanada. Si la proyectas desde arriba, capturarías casi toda su forma. Si la proyectas de costado, vería solo una línea.

**PCA encuentra automáticamente el "desde arriba" óptimo** — la proyección que captura la mayor varianza (dispersión) de los datos.

Técnicamente, PCA hace lo siguiente:
1. **Centra los datos**: resta la media de cada variable para que el centro esté en el origen
2. Calcula la **matriz de covarianza**: mide cómo se relacionan las variables entre sí
3. Calcula los **vectores propios (eigenvectors)** de esa matriz: son las "direcciones principales"
4. Ordena esos vectores por su **valor propio (eigenvalue)**: el mayor eigenvalue corresponde a la dirección de mayor varianza → PC1
5. **Proyecta** los datos originales sobre las primeras K componentes

No necesitas memorizar la matemática — sklearn lo hace todo. Lo importante es entender el concepto.

---

## 4. PCA en sklearn: paso a paso

### Paso 1: Escalar los datos (¡obligatorio!)

PCA es sensible a la escala de las variables. Si una variable va de 0 a 1.000.000 y otra de 0 a 1, la primera dominará todo. Siempre usa `StandardScaler` antes de PCA.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Paso 2: Crear y entrenar PCA

```python
from sklearn.decomposition import PCA

# Reducir a 2 dimensiones (para visualización)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

print(f'Forma original:  {X_scaled.shape}')   # (n_filas, n_columnas)
print(f'Forma reducida:  {X_pca.shape}')        # (n_filas, 2)
```

### Paso 3: Revisar cuánta información se conserva

```python
print('Varianza explicada por componente:')
for i, var in enumerate(pca.explained_variance_ratio_):
    print(f'  PC{i+1}: {var*100:.1f}%')

print(f'Total explicado: {pca.explained_variance_ratio_.sum()*100:.1f}%')
```

---

## 5. Explained Variance Ratio

El atributo `explained_variance_ratio_` es el más importante de PCA. Indica qué fracción de la varianza total de los datos explica cada componente principal.

Ejemplo:
```
pca.explained_variance_ratio_ = [0.62, 0.21, 0.10, 0.07]
```
- PC1 captura el 62% de la varianza
- PC2 captura el 21%
- PC1 + PC2 = 83% — con solo 2 componentes conservamos el 83% de la información

### ¿Cuántas componentes elegir?

Convención común: elegir el número de componentes que explique entre el 70% y el 95% de la varianza total.

El **scree plot** (gráfica de varianza acumulada) ayuda a elegir:

```python
import matplotlib.pyplot as plt

pca_full = PCA()  # sin especificar n_components: calcula todos
pca_full.fit(X_scaled)

varianza_acumulada = pca_full.explained_variance_ratio_.cumsum()

plt.plot(range(1, len(varianza_acumulada)+1), varianza_acumulada, marker='o')
plt.axhline(y=0.95, color='red', linestyle='--', label='95%')
plt.xlabel('Número de componentes')
plt.ylabel('Varianza explicada acumulada')
plt.title('Scree Plot — ¿Cuántos componentes necesito?')
plt.legend()
plt.show()
```

---

## 6. Visualizar con PCA

Una vez reducidos a 2 dimensiones, podemos hacer un scatter plot normal:

```python
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, edgecolors='k', linewidths=0.3)
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% varianza)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% varianza)')
plt.title('Datos en espacio PCA (2D)')
plt.show()
```

Si tienes etiquetas (por ejemplo, de un clustering previo), puedes colorear los puntos:

```python
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=etiquetas, cmap='tab10', alpha=0.6)
```

---

## 7. El Biplot: variables y muestras juntas

El biplot superpone dos cosas en el mismo gráfico:
- Los **puntos** (cada observación proyectada en el espacio PC1-PC2)
- Los **vectores** (cada variable original, indicando cómo contribuye a los componentes)

Cómo leer un biplot:
- **Vectores largos**: esa variable tiene mucha influencia en los componentes graficados
- **Vectores en la misma dirección**: esas variables están positivamente correlacionadas
- **Vectores opuestos**: correlación negativa
- **Vectores perpendiculares**: variables sin correlación entre sí

```python
fig, ax = plt.subplots(figsize=(8, 7))

# Graficar los puntos
ax.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.4, s=30)

# Graficar los vectores de las variables (loadings)
loadings = pca.components_.T  # shape: (n_variables, 2)
escala = 3

for i, nombre_col in enumerate(columnas_originales):
    ax.arrow(0, 0,
             loadings[i, 0] * escala,
             loadings[i, 1] * escala,
             head_width=0.1, head_length=0.05,
             fc='red', ec='red')
    ax.text(loadings[i, 0] * escala * 1.15,
            loadings[i, 1] * escala * 1.15,
            nombre_col, fontsize=10, color='darkred')

ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_title('Biplot PCA')
ax.axhline(0, color='gray', linewidth=0.5)
ax.axvline(0, color='gray', linewidth=0.5)
plt.show()
```

---

## 8. PCA + Clustering: flujo de trabajo recomendado

Cuando tienes muchas variables y quieres hacer clustering:

```
Datos originales (muchas columnas)
        ↓ StandardScaler
Datos escalados
        ↓ PCA(n_components=2 o más)
Datos en 2-3 dimensiones
        ↓ KMeans o DBSCAN
Clusters + Visualización directa
```

```python
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Escalar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Reducir con PCA
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X_scaled)

# Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
etiquetas = kmeans.fit_predict(X_2d)

# Visualizar
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=etiquetas, cmap='tab10', alpha=0.7)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Clusters en espacio PCA')
plt.show()
```

---

## 9. Limitaciones de PCA

- **Solo lineal**: PCA no captura relaciones no lineales entre variables
- **Interpretabilidad baja**: las componentes principales son mezclas de las variables originales y no tienen un significado directo fácil de explicar
- **Escala obligatoria**: sin escalar, las variables de mayor magnitud dominan los componentes
- **Pérdida de información**: siempre se pierde algo al reducir dimensiones
- **Variables categóricas**: PCA solo funciona con variables numéricas

---

## Resumen de conceptos

| Concepto | Significado |
|----------|-------------|
| Dimensionalidad | Número de columnas (variables) de un dataset |
| Maldición de la dimensionalidad | Los problemas que aparecen al tener demasiadas variables |
| PCA | Algoritmo que busca las direcciones de mayor varianza para comprimir datos |
| Componente principal | Nueva variable = combinación lineal de las originales |
| `explained_variance_ratio_` | Fracción de varianza que explica cada componente |
| Scree plot | Gráfica para elegir cuántos componentes usar |
| Biplot | Visualización de muestras y variables en el espacio PCA |
| Loadings | Pesos de cada variable original en cada componente principal |
