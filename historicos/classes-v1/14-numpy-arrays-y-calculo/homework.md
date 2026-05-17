# 📝 Tarea — Clase 14

> 📝 Trabajo autónomo para consolidar lo visto y practicar con más calma.

## 🎯 Encargo

Usando el dataset `ventas_tienda.csv`, realiza un análisis numérico completo con NumPy sobre la columna de `total_venta` (o calcúlala si no existe como `precio_unitario × unidades`). El objetivo es que demuestres dominio de las operaciones fundamentales de NumPy trabajando con datos reales.

Completa los siguientes puntos en un cuaderno Jupyter o script Python bien comentado:

**Parte 1 — Carga y extracción**
- Carga el dataset con pandas
- Extrae `precio_unitario` y `unidades` como arrays NumPy usando `.values`
- Calcula el array `total_venta` mediante operación vectorizada
- Muestra el `dtype`, `shape` y `size` del array resultante

**Parte 2 — Estadísticas descriptivas**
- Calcula: media, mediana, desviación estándar, mínimo, máximo, suma total
- Identifica el índice del registro con la venta más alta y el más bajo
- Responde: ¿la media es mayor o menor que la mediana? ¿Qué significa eso sobre la distribución?

**Parte 3 — Filtrado**
- Crea un array con solo las ventas que están por encima de la media
- Crea un array con solo las ventas del cuartil superior (mayores al percentil 75)
- Pista: `np.percentile(arr, 75)` calcula el percentil 75

**Parte 4 — Transformación**
- Aplica la normalización min-max al array de totales
- Redondea los valores normalizados a 4 decimales con `np.round`
- Verifica que el mínimo normalizado sea 0.0 y el máximo sea 1.0

**Parte 5 — Reflexión**
En no más de 5 oraciones: ¿en qué casos usarías NumPy directamente en lugar de pandas? ¿Cuándo preferirías pandas?

## 📦 Entregables

- Código o desarrollo ordenado.
- Conclusión breve conectada con evidencia.
- Comentarios que expliquen qué hace y para qué sirve cada bloque importante.

## 🔍 Autoevaluación final

- Entendí la pregunta del módulo.
- Puedo explicar la salida sin leer el código completo.
- Dejé comentarios útiles en los pasos clave.
- Usé operaciones vectorizadas en lugar de bucles `for`.
- La reflexión de la Parte 5 está respondida con argumentos concretos.
