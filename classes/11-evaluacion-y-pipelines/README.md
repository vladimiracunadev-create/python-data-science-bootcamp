# 📘 Clase 11 â€” EvaluaciÃ³n robusta y Pipelines de ML

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.


## 🎯 Objetivo

Aplicar validaciÃ³n cruzada, bÃºsqueda de hiperparÃ¡metros y construir pipelines reproducibles de preprocesamiento + modelo.

## ⏱ DuraciÃ³n sugerida

90 minutos

## 🗂 Dataset base

`datasets/ventas_tienda.csv` Â· `datasets/retencion_clientes.csv`

## ✅ Resultados esperados

Al finalizar, el estudiante podrÃ¡:

- aplicar validaciÃ³n cruzada (k-fold) para evaluar modelos de forma robusta;
- construir un Pipeline de scikit-learn con preprocesamiento y modelo;
- escalar variables numÃ©ricas y codificar variables categÃ³ricas dentro del pipeline;
- realizar bÃºsqueda de hiperparÃ¡metros con GridSearchCV;
- interpretar la curva de aprendizaje.

## 🧰 Materiales

- `notebook.ipynb` â€” prÃ¡ctica guiada
- `slides.md` â€” pauta de la clase
- `ejercicios.md` â€” ejercicios progresivos
- `homework.md` â€” tarea
- `soluciones.ipynb` â€” soluciones comentadas
- `teoria.md` â€” documento teÃ³rico completo (base para PDF)

## 💡 Idea central

Un modelo que funciona en el notebook pero falla en producciÃ³n es inÃºtil. Los pipelines garantizan que el preprocesamiento en producciÃ³n sea idÃ©ntico al del entrenamiento.

## 🔑 Conceptos clave

| Concepto | DescripciÃ³n |
|---|---|
| Overfitting | El modelo memoriza en lugar de generalizar |
| Underfitting | El modelo es demasiado simple para los datos |
| Cross-validation | Evaluar en mÃºltiples particiones del dataset |
| K-fold | Dividir datos en K grupos para validaciÃ³n cruzada |
| Pipeline | Encadenar pasos de preprocesamiento y modelo |
| StandardScaler | Normaliza variables a media 0 y desv. estÃ¡ndar 1 |
| GridSearchCV | Probar combinaciones de hiperparÃ¡metros sistemÃ¡ticamente |
| Curva de aprendizaje | DiagnÃ³stico de overfitting/underfitting |

## 👩‍🏫 Nota para el docente

Usar ejemplos concretos de cÃ³mo el data leakage (filtraciÃ³n de datos del futuro al entrenamiento) distorsiona los resultados y cÃ³mo el Pipeline lo evita automÃ¡ticamente.
