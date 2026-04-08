# Clase 11 — Evaluación robusta y Pipelines de ML

## Objetivo

Aplicar validación cruzada, búsqueda de hiperparámetros y construir pipelines reproducibles de preprocesamiento + modelo.

## Duración sugerida

90 minutos

## Dataset base

`datasets/ventas_tienda.csv` · `datasets/retencion_clientes.csv`

## Resultados esperados

Al finalizar, el estudiante podrá:

- aplicar validación cruzada (k-fold) para evaluar modelos de forma robusta;
- construir un Pipeline de scikit-learn con preprocesamiento y modelo;
- escalar variables numéricas y codificar variables categóricas dentro del pipeline;
- realizar búsqueda de hiperparámetros con GridSearchCV;
- interpretar la curva de aprendizaje.

## Materiales

- `notebook.ipynb` — práctica guiada
- `slides.md` — pauta de la clase
- `ejercicios.md` — ejercicios progresivos
- `homework.md` — tarea
- `soluciones.ipynb` — soluciones comentadas
- `teoria.md` — documento teórico completo (base para PDF)

## Idea central

Un modelo que funciona en el notebook pero falla en producción es inútil. Los pipelines garantizan que el preprocesamiento en producción sea idéntico al del entrenamiento.

## Conceptos clave

| Concepto | Descripción |
|---|---|
| Overfitting | El modelo memoriza en lugar de generalizar |
| Underfitting | El modelo es demasiado simple para los datos |
| Cross-validation | Evaluar en múltiples particiones del dataset |
| K-fold | Dividir datos en K grupos para validación cruzada |
| Pipeline | Encadenar pasos de preprocesamiento y modelo |
| StandardScaler | Normaliza variables a media 0 y desv. estándar 1 |
| GridSearchCV | Probar combinaciones de hiperparámetros sistemáticamente |
| Curva de aprendizaje | Diagnóstico de overfitting/underfitting |

## Nota para el docente

Usar ejemplos concretos de cómo el data leakage (filtración de datos del futuro al entrenamiento) distorsiona los resultados y cómo el Pipeline lo evita automáticamente.
