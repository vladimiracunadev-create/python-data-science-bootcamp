# 🏠 Homework — Clase 23: Reducción de dimensionalidad — PCA

> Entrega tu notebook con todas las celdas ejecutadas. Incluye celdas Markdown con explicaciones en español antes de cada sección de código.

---

## Contexto del problema

El departamento de análisis tiene un dataset de estudiantes con muchas columnas numéricas (notas, horas de estudio, faltas, participación, etc.). Quieren entender la **estructura general** del rendimiento estudiantil en un vistazo rápido. Tu tarea es usar PCA para comprimir toda esa información en 2 dimensiones y crear visualizaciones que puedan usarse en una presentación para directivos.

---

## Parte 1 — Exploración y correlación (2 puntos)

1. Carga `datasets/estudiantes.csv`
2. Selecciona todas las columnas numéricas
3. Muestra la **matriz de correlación** con un heatmap:

```python
import seaborn as sns
corr = X.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title('Matriz de correlación')
plt.show()
```

4. Identifica los **3 pares de variables más correlacionadas** (positiva o negativamente)

**Incluye en Markdown:** ¿Por qué las variables correlacionadas son candidatas a reducción con PCA?

---

## Parte 2 — Scree Plot y elección de componentes (2 puntos)

1. Aplica PCA completo (sin especificar `n_components`)
2. gráfica el **Scree Plot** con varianza individual Y acumulada (como en el ejercicio 3)
3. Crea una tabla:

| n_componentes | Varianza explicada acumulada |
|--------------|------------------------------|
| 1            |                              |
| 2            |                              |
| 3            |                              |
| 4            |                              |

4. Elige el número de componentes justificando: ¿llegan al 80%? ¿al 90%?

---

## Parte 3 — Reducción y visualización (3 puntos)

1. Aplica PCA con `n_components=2`
2. Crea el **scatter plot 2D** con los ejes etiquetados incluyendo el % de varianza:
   - Eje X: `PC1 (XX.X% varianza)`
   - Eje Y: `PC2 (XX.X% varianza)`
3. Crea el **biplot** con las flechas de las variables
4. (Bonus) Si el dataset tiene una columna categórica (ej. género, grupo), colorea los puntos por esa categoría

**Requisito:** Ambos gráficos deben tener título, ejes etiquetados y aspecto profesional.

---

## Parte 4 — PCA + Clustering (2 puntos)

1. Aplica K-Means con K=3 en el espacio de 2 componentes PCA
2. Visualiza los clusters en el scatter plot PCA (coloreados)
3. Calcula el Silhouette Score del clustering en el espacio PCA
4. Calcula el perfil promedio de cada cluster **en las variables originales** (no en las componentes PCA):

```python
df_resultado = df[cols_num].copy().dropna()
df_resultado['cluster'] = kmeans.labels_
perfil = df_resultado.groupby('cluster').mean().round(2)
```

---

## Parte 5 — Interpretación final (1 punto)

Escribe un párrafo de conclusión (mínimo 6 oraciones) respondiendo:
- ¿Cuánta información se preservó al reducir a 2 componentes?
- ¿Qué variables contribuyen más a PC1? ¿Y a PC2? (mira los loadings)
- ¿Los clusters encontrados en el espacio PCA son coherentes con los de la clase anterior?
- ¿Le recomendarías usar PCA + clustering a un director sin conocimientos técnicos? ¿Por qué?

---

## Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Matriz de correlación con análisis | 2 |
| Scree Plot + tabla + justificación de K | 2 |
| Scatter plot 2D + biplot profesionales | 3 |
| PCA + Clustering + perfil en variables originales | 2 |
| Conclusión escrita y razonada | 1 |
| **Total** | **10** |

---

## Bonus (punto extra)

Aplica PCA también al dataset `ventas_tienda.csv`. ¿Los componentes principales de ventas tienen interpretación parecida a los de estudiantes? Compara en una tabla los loadings principales de ambos datasets.

---

## Entrega

- Archivo: `homework_clase23_tunombre.ipynb`
- Todas las celdas ejecutadas sin errores
- Mínimo 3 celdas Markdown con explicaciones
