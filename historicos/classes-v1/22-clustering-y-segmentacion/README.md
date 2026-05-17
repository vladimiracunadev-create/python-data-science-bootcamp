# 📘 Clase 22: Clustering y segmentación

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Aprender qué es el aprendizaje no supervisado y cómo el algoritmo K-Means puede agrupar datos similares sin necesidad de etiquetas previas. Al trabajar con datos reales de ventas y estudiantes, el alumno comprenderá cómo encontrar segmentos naturales dentro de un conjunto de datos y cómo interpretar esos grupos para tomar decisiones.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/ventas_tienda.csv`
- `datasets/estudiantes.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Explicar la diferencia entre aprendizaje supervisado y no supervisado con sus propias palabras
- Aplicar K-Means con sklearn para agrupar datos y visualizar los clusters resultantes
- Usar el Método del Codo y el Silhouette Score para elegir el número óptimo de clusters

## 🧭 Temas clave
- Aprendizaje no supervisado: encontrar grupos sin etiquetas
- K-Means: asignar puntos al centro más cercano, mover centros, repetir
- Método del Codo (Elbow Method) para elegir K
- Silhouette Score para evaluar la calidad de los clusters
- DBSCAN: clusters de cualquier forma, tolerante al ruido
- Visualización de clusters con scatter plot coloreado
- Interpretación de negocio: ¿qué significa cada grupo?

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.

## 💡 Idea central
El clustering agrupa datos similares sin necesidad de etiquetas, revelando segmentos naturales dentro de los datos.

## 👩‍🏫 Nota para el docente
Empieza mostrando un puñado de M&Ms de distintos colores sobre la mesa y pide a los alumnos que los "agrupen" sin darte ninguna instrucción. Cuando lo hagan por color (o por tamaño), explica: eso es exactamente lo que hace K-Means. La analogía funciona para cualquier edad y hace que el concepto de "sin etiquetas" sea inmediatamente intuitivo.
