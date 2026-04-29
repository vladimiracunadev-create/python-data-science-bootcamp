# 🏠 Homework — Clase 22: Clustering y segmentación

> Entrega tu notebook con todos los bloques ejecutados. Incluye texto explicativo en celdas Markdown entre cada sección.

---

## Contexto del problema

La tienda quiere entender mejor a sus vendedores. El gerente sospecha que hay distintos "perfiles" de vendedor según su volumen de ventas y el tipo de productos que venden. Tu tarea es usar clustering para identificar esos perfiles y presentarlos de forma clara.

---

## Parte 1 — Exploración y preparación (2 puntos)

1. Carga `datasets/ventas_tienda.csv`
2. Selecciona al menos 3 columnas numéricas relevantes para el análisis de vendedores o productos
3. Maneja los valores nulos si los hay (explica tu decisión: ¿eliminar filas, imputar con la media?)
4. Escala las variables con `StandardScaler`
5. Muestra la forma del dataset antes y después de la preparación

**Incluye en Markdown:** una descripción de las variables que elegiste y por qué son relevantes.

---

## Parte 2 — Elegir el número de clusters (3 puntos)

1. Grafica el **Método del Codo** para K de 1 a 10
2. Calcula el **Silhouette Score** para K de 2 a 8
3. Crea una tabla comparativa:

| K | Inercia | Silhouette Score |
|---|---------|-----------------|
| 2 |         |                 |
| 3 |         |                 |
| 4 |         |                 |
| … |         |                 |

4. Elige un K justificando tu decisión con ambas métricas

**Incluye en Markdown:** una explicación en tus propias palabras de por qué elegiste ese K.

---

## Parte 3 — Clustering y visualización (3 puntos)

1. Entrena K-Means con el K elegido
2. Agrega la columna `cluster` al DataFrame original
3. Crea un scatter plot con los clusters coloreados y los centroides marcados
4. (Bonus) Crea un segundo scatter plot con un par de variables diferente para ver otra perspectiva

**Requisito visual:** El gráfico debe tener título, etiquetas en los ejes y leyenda.

---

## Parte 4 — Interpretación y nombre de clusters (2 puntos)

1. Calcula el perfil promedio de cada cluster (media de cada variable numérica por grupo)
2. Muestra cuántos registros hay en cada cluster
3. Asigna un nombre descriptivo a cada cluster
4. Escribe un párrafo de conclusión (mínimo 5 oraciones) respondiendo:
   - ¿Qué tipos de vendedores/productos encontraste?
   - ¿Cuál cluster es más valioso para la tienda?
   - ¿Qué acciones concretas le recomendarías al gerente basándote en estos segmentos?

---

## Criterios de evaluación

| Criterio | Puntos |
|----------|--------|
| Datos correctamente preparados y escalados | 2 |
| Método del Codo + Silhouette Score con justificación | 3 |
| Visualización clara y correcta de los clusters | 3 |
| Interpretación con nombres y conclusión escrita | 2 |
| **Total** | **10** |

---

## Bonus (punto extra)

Repite el análisis con DBSCAN. ¿Detecta el mismo número de grupos? ¿Encuentra outliers interesantes? Describe qué podrían representar esos puntos de ruido en el negocio.

---

## Entrega

- Archivo: `homework_clase22_tunombre.ipynb`
- Todas las celdas deben estar ejecutadas (no dejes celdas vacías o con error)
- Cada sección debe tener al menos una celda Markdown con explicación en español
