# 📝 Tarea — Clase 15

> 📝 Trabajo autónomo para consolidar lo visto y practicar con más calma.

## 🎯 Encargo

Usando el dataset `ventas_tienda.csv`, construye un mini-análisis de negocio completo usando **exclusivamente SQL** para obtener los datos, y pandas solo para mostrar y formatear los resultados finales. El objetivo es demostrar que puedes responder preguntas de negocio reales con consultas SQL bien construidas.

Responde las siguientes preguntas de negocio. Para cada una, escribe la consulta SQL y explica la respuesta en una oración:

**Parte 1 — Preguntas descriptivas (SELECT + WHERE)**

1. ¿Cuántos productos distintos hay en el dataset?
   - Pista: `SELECT COUNT(DISTINCT producto) FROM ventas`

2. ¿Cuáles son los 10 registros con el mayor precio unitario?

3. ¿Cuántos registros tienen más de 15 unidades vendidas?

**Parte 2 — Preguntas por grupo (GROUP BY)**

4. ¿Cuál categoría tiene el precio promedio más alto?

5. ¿Cuál categoría acumula más unidades vendidas en total?

6. Para cada categoría, ¿cuál es la diferencia entre el precio máximo y el mínimo? (calcula `MAX - MIN` en la consulta)

**Parte 3 — Análisis combinado**

7. Crea una consulta que muestre, por categoría: cantidad de registros, suma de unidades, precio promedio, y precio máximo. Ordena por precio promedio descendente. Llama a las columnas calculadas con alias claros (usa `AS nombre`).

8. Filtra esa misma consulta para mostrar solo las categorías donde la suma de unidades supere 50 (usa HAVING).

**Parte 4 — Reflexión**

En 3-5 oraciones: ¿en qué situaciones preferirías usar SQL en lugar de pandas? ¿Y pandas en lugar de SQL? ¿Hay situaciones donde usarías los dos juntos?

## 📦 Entregables

- Código o desarrollo ordenado.
- Conclusión breve conectada con evidencia.
- Comentarios que expliquen qué hace y para qué sirve cada bloque importante.

## 🔍 Autoevaluación final

- Entendí la pregunta del módulo.
- Puedo explicar la salida sin leer el código completo.
- Dejé comentarios útiles en los pasos clave.
- Cada consulta SQL está acompañada de una interpretación en lenguaje natural.
- La reflexión de la Parte 4 está respondida con ejemplos concretos del mundo real.
