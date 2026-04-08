# Clase 10 — Modelos Supervisados: Clasificación y Comparación

## Objetivo

Entrenar y comparar modelos de clasificación para tomar decisiones basadas en datos.

## Duración sugerida

90 minutos

## Dataset base

`datasets/retencion_clientes.csv` · `datasets/estudiantes.csv`

## Resultados esperados

Al finalizar, el estudiante podrá:

- construir un modelo de clasificación binaria (árbol de decisión, regresión logística);
- interpretar la matriz de confusión;
- calcular y comparar accuracy, precisión y recall;
- elegir el modelo adecuado según el contexto del negocio;
- visualizar la importancia de las variables.

## Materiales

- `notebook.ipynb` — práctica guiada
- `slides.md` — pauta de la clase
- `ejercicios.md` — ejercicios progresivos
- `homework.md` — tarea
- `soluciones.ipynb` — soluciones comentadas
- `teoria.md` — documento teórico completo (base para PDF)

## Idea central

No existe un único modelo "mejor": el modelo correcto depende del problema, los datos y el costo de equivocarse. Comparar siempre con al menos dos modelos y una línea base.

## Conceptos clave

| Concepto | Descripción |
|---|---|
| Clasificación | Predecir a qué categoría pertenece un caso |
| Árbol de decisión | Divide el espacio de decisión en reglas if/else |
| Regresión logística | Estima probabilidades entre 0 y 1 |
| Matriz de confusión | Tabla de predicciones vs. realidad |
| Accuracy | % de predicciones correctas totales |
| Precisión | % de positivos predichos que son reales |
| Recall | % de positivos reales que fueron detectados |
| F1-Score | Media armónica de precisión y recall |

## Nota para el docente

El ejemplo de retención de clientes es ideal: los costos de falso negativo (no detectar un cliente que se va) vs. falso positivo (contactar a quien no iba a irse) son fácilmente comprensibles.
