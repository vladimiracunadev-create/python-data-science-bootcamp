# 🖥️ Diapositivas sugeridas — Clase 19

> 🖥️ Guion visual breve para conducir la sesión sin sobrecargar la clase.

## 🚪 Apertura

- Pregunta inicial: "¿Puedes adivinar el precio de una pizza solo por su tamaño?"
- Mostrar un scatter plot de puntos y preguntar: "¿Dónde trazarías una línea?"
- Conectar con la pregunta real del módulo: predecir `total_neto` a partir de `unidades` y `descuento_pct`.

## 🛤️ Ruta de la sesión

| Tramo | Tiempo sugerido | Enfoque | Evidencia |
|---|---|---|---|
| Inicio | 10 min | Intuición visual: scatter + línea | Respuesta a la pregunta de la pizza |
| Desarrollo 1 | 20 min | Regresión simple con sklearn | Coeficiente e intercepto leídos en voz alta |
| Desarrollo 2 | 25 min | Regresión múltiple + R² + residuos | Interpretación del score |
| Práctica | 25 min | Ejercicio con ventas_tienda.csv | Predicción entregada |
| Cierre | 10 min | Cuándo usar regresión vs clasificación | Autoevaluación breve |

## 📌 Puntos que deben quedar claros

- La regresión predice un número continuo, no una categoría.
- El coeficiente dice "cuánto sube Y por cada unidad extra de X".
- R² cerca de 1 es bueno; cerca de 0 el modelo no explica nada.
- Los residuos muestran dónde el modelo se equivoca.

## 🏁 Cierre esperado

La clase 20 sube la complejidad con árboles de decisión, que pueden capturar relaciones no lineales.
