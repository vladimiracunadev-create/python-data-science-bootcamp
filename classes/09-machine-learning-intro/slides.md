# Slides — Clase 09: Introducción al Machine Learning

## Bloque 1 (20 min) — ¿Qué es el Machine Learning?

**Punto de partida:** ¿Cómo decide un banco si aprobar un crédito?

- Antes: reglas escritas a mano por expertos.
- Ahora: el sistema aprende de miles de casos anteriores.

**Tipos de ML:**

| Tipo | Descripción | Ejemplo |
|---|---|---|
| Supervisado | Datos etiquetados | Predecir ventas |
| No supervisado | Sin etiqueta | Segmentar clientes |
| Por refuerzo | Aprende por recompensa | Juegos, robótica |

**En este bootcamp:** nos enfocamos en supervisado (regresión y clasificación).

---

## Bloque 2 (30 min) — El flujo de trabajo de ML

```
Datos → Explorar → Limpiar → Features → Modelo → Evaluar → Comunicar
```

**Práctica guiada:**

1. Cargar `ventas_tienda.csv`
2. Identificar: ¿qué queremos predecir?
3. Dividir en train/test: `train_test_split`
4. Entrenar regresión lineal
5. Calcular MAE y RMSE

---

## Bloque 3 (25 min) — Interpretar el modelo

- **Coeficientes:** ¿qué variable influye más?
- **MAE:** en promedio, ¿cuánto nos equivocamos?
- **RMSE:** castiga más los errores grandes.

**Pregunta clave:** ¿Es nuestro modelo mejor que simplemente predecir el promedio?

---

## Cierre (15 min) — Reflexión

- ¿Qué aprendió el modelo?
- ¿En qué casos fallaría?
- ¿Qué datos adicionales mejorarían la predicción?
