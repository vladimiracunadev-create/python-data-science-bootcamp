# ❓ Preguntas — Clase 22: Clustering y Segmentación

> Preguntas de comprensión, discusión y evaluación.

## 🧠 Preguntas de comprensión

1. ¿Cuál es la diferencia fundamental entre aprendizaje supervisado y no supervisado? ¿Por qué no se pueden usar métricas como accuracy en clustering?
2. Describe en tus palabras los 3 pasos del algoritmo K-Means: asignar, mover, repetir.
3. ¿Qué es la inercia en K-Means y por qué siempre disminuye al aumentar el número de clusters?
4. ¿Qué es el método del codo (elbow method) y cómo se usa para elegir el número de clusters?
5. ¿Qué mide el `silhouette_score`? ¿Un valor de 0.7 es bueno o malo? ¿Y uno de 0.1?
6. ¿En qué se diferencia DBSCAN de K-Means en cuanto a la forma de los clusters que puede detectar?
7. ¿Qué significa que DBSCAN clasifique algunos puntos como "ruido" (-1)? ¿Cuándo es eso útil?

## 💬 Preguntas de discusión

1. Una empresa de retail quiere segmentar a sus clientes. ¿Qué variables usarías como input para K-Means? ¿Qué significaría cada cluster en términos de negocio?
2. Aplicas K-Means con k=3 y obtienes clusters de tamaño 2, 450 y 448. ¿Qué puede estar pasando? ¿Cómo lo diagnosticarías?
3. ¿Cuándo preferirías DBSCAN sobre K-Means? Da un ejemplo de un caso de uso real donde la forma irregular de los clusters sea importante.

## 🧪 Preguntas de código

1. Aplica K-Means con k=2, 3, 4, 5, 6 sobre `ventas_tienda.csv`. Para cada k, calcula la inercia y gráfica la curva del codo. ¿Cuántos clusters elegirías?
2. Calcula el `silhouette_score` para k=2, 3, 4, 5 y encuentra el k que maximiza el score. ¿Coincide con el método del codo?
3. Aplica DBSCAN con `eps=0.5` y `min_samples=5` sobre `estudiantes.csv` (normaliza primero con `StandardScaler`). ¿Cuántos clusters encontró? ¿Cuántos puntos marcó como ruido?

## 🎯 Pregunta integradora

Usa `ventas_tienda.csv` con variables como `ticket_promedio`, `frecuencia_compra` y `meses_activo`. Primero normaliza los datos con `StandardScaler`. Luego: (1) determina el número óptimo de clusters con el método del codo y silhouette score, (2) aplica K-Means con ese k, (3) visualiza los clusters en un scatter plot con colores distintos, (4) calcula la media de cada variable por cluster y describe con palabras qué tipo de cliente representa cada uno (ej: "clientes VIP", "clientes esporádicos", etc.).
