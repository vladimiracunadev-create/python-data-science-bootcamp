# 🖥 Slides â€” Clase 09: IntroducciÃ³n al Machine Learning

## Bloque 1 (20 min) â€” Â¿QuÃ© es el Machine Learning?

**Punto de partida:** Â¿CÃ³mo decide un banco si aprobar un crÃ©dito?

- Antes: reglas escritas a mano por expertos.
- Ahora: el sistema aprende de miles de casos anteriores.

**Tipos de ML:**

| Tipo | DescripciÃ³n | Ejemplo |
|---|---|---|
| Supervisado | Datos etiquetados | Predecir ventas |
| No supervisado | Sin etiqueta | Segmentar clientes |
| Por refuerzo | Aprende por recompensa | Juegos, robÃ³tica |

**En este bootcamp:** nos enfocamos en supervisado (regresiÃ³n y clasificaciÃ³n).

---

## Bloque 2 (30 min) â€” El flujo de trabajo de ML

```
Datos â†’ Explorar â†’ Limpiar â†’ Features â†’ Modelo â†’ Evaluar â†’ Comunicar
```

**PrÃ¡ctica guiada:**

1. Cargar `ventas_tienda.csv`
2. Identificar: Â¿quÃ© queremos predecir?
3. Dividir en train/test: `train_test_split`
4. Entrenar regresiÃ³n lineal
5. Calcular MAE y RMSE

---

## Bloque 3 (25 min) â€” Interpretar el modelo

- **Coeficientes:** Â¿quÃ© variable influye mÃ¡s?
- **MAE:** en promedio, Â¿cuÃ¡nto nos equivocamos?
- **RMSE:** castiga mÃ¡s los errores grandes.

**Pregunta clave:** Â¿Es nuestro modelo mejor que simplemente predecir el promedio?

---

## Cierre (15 min) â€” ReflexiÃ³n

- Â¿QuÃ© aprendiÃ³ el modelo?
- Â¿En quÃ© casos fallarÃ­a?
- Â¿QuÃ© datos adicionales mejorarÃ­an la predicciÃ³n?
