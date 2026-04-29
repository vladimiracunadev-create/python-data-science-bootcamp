# 🧪 Ejercicios — Clase 19

> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar

- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.
- Explica qué hace cada transformación relevante y para qué sirve.

## 🧭 Trabajo guiado

### Ejercicio 1 — Regresión simple
1. Carga `datasets/ventas_tienda.csv`.
2. Crea un scatter plot de `unidades` vs `total_neto`.
3. Entrena un `LinearRegression` usando solo `unidades` como variable predictora.
4. Imprime el intercepto y el coeficiente. Explica con una frase qué significa cada uno.
5. Calcula el R² y responde: ¿cuánto del comportamiento de `total_neto` explica el modelo?

### Ejercicio 2 — Regresión múltiple
1. Agrega la columna `descuento_pct` como segunda variable predictora.
2. Entrena un nuevo modelo con ambas variables.
3. Compara el R² del modelo simple vs el múltiple. ¿Mejoró? ¿Por qué crees que sí o no?
4. Usa `model.predict()` para predecir el `total_neto` de una venta hipotética de 50 unidades con 10% de descuento.

### Ejercicio 3 — Residuos
1. Calcula los residuos del modelo múltiple.
2. Haz un scatter plot de `y_pred` vs `residuos`.
3. Traza una línea horizontal en y=0.
4. Observa: ¿los residuos están distribuidos uniformemente alrededor de 0, o hay algún patrón?

### Ejercicio 4 — Dataset estudiantes
1. Carga `datasets/estudiantes.csv`.
2. Predice `evaluacion_python` usando `asistencia_pct` como variable.
3. Imprime el coeficiente y explica: por cada punto extra de asistencia, ¿cuánto cambia la nota predicha?

## ✅ Criterios de autocorrección

- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
- Puedes decir qué cambiaría si el R² fuera 0.1 en lugar de 0.8.
