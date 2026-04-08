# Clase 09 — Introducción al Machine Learning con scikit-learn

## Objetivo

Comprender qué es el machine learning, cuándo aplicarlo y construir el primer modelo predictivo simple usando scikit-learn.

## Duración sugerida

90 minutos

## Dataset base

`datasets/ventas_tienda.csv` · `datasets/estudiantes.csv`

## Resultados esperados

Al finalizar, el estudiante podrá:

- explicar la diferencia entre aprendizaje supervisado y no supervisado;
- identificar variables predictoras (features) y variable objetivo (target);
- entrenar un modelo de regresión lineal simple con scikit-learn;
- dividir datos en conjunto de entrenamiento y prueba;
- interpretar el error del modelo (MAE, RMSE).

## Materiales

- `notebook.ipynb` — práctica guiada paso a paso
- `slides.md` — pauta de la clase
- `ejercicios.md` — ejercicios progresivos
- `homework.md` — tarea
- `soluciones.ipynb` — soluciones comentadas
- `teoria.md` — documento teórico completo (base para PDF)

## Idea central

Machine learning no es magia: es encontrar patrones en datos históricos para predecir lo que aún no ha ocurrido. El primer paso es siempre entender el problema antes de elegir el modelo.

## Conceptos clave

| Concepto | Descripción |
|---|---|
| Supervisado | Aprende de ejemplos con etiqueta conocida |
| No supervisado | Encuentra estructura sin etiqueta |
| Feature | Variable de entrada del modelo |
| Target | Variable que queremos predecir |
| Train/Test split | División para evaluar sin hacer trampa |
| MAE | Error absoluto medio |
| RMSE | Raíz del error cuadrático medio |

## Nota para el docente

Enfatizar que un modelo simple bien entendido es más valioso que un modelo complejo mal interpretado. No avanzar a modelos complejos sin que el estudiante entienda la regresión lineal.
