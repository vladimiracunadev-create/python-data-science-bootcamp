# 📘 Clase 10 â€” Modelos Supervisados: ClasificaciÃ³n y ComparaciÃ³n

## Objetivo

Entrenar y comparar modelos de clasificaciÃ³n para tomar decisiones basadas en datos.

## DuraciÃ³n sugerida

90 minutos

## Dataset base

`datasets/retencion_clientes.csv` Â· `datasets/estudiantes.csv`

## Resultados esperados

Al finalizar, el estudiante podrÃ¡:

- construir un modelo de clasificaciÃ³n binaria (Ã¡rbol de decisiÃ³n, regresiÃ³n logÃ­stica);
- interpretar la matriz de confusiÃ³n;
- calcular y comparar accuracy, precisiÃ³n y recall;
- elegir el modelo adecuado segÃºn el contexto del negocio;
- visualizar la importancia de las variables.

## Materiales

- `notebook.ipynb` â€” prÃ¡ctica guiada
- `slides.md` â€” pauta de la clase
- `ejercicios.md` â€” ejercicios progresivos
- `homework.md` â€” tarea
- `soluciones.ipynb` â€” soluciones comentadas
- `teoria.md` â€” documento teÃ³rico completo (base para PDF)

## Idea central

No existe un Ãºnico modelo "mejor": el modelo correcto depende del problema, los datos y el costo de equivocarse. Comparar siempre con al menos dos modelos y una lÃ­nea base.

## Conceptos clave

| Concepto | DescripciÃ³n |
|---|---|
| ClasificaciÃ³n | Predecir a quÃ© categorÃ­a pertenece un caso |
| Ãrbol de decisiÃ³n | Divide el espacio de decisiÃ³n en reglas if/else |
| RegresiÃ³n logÃ­stica | Estima probabilidades entre 0 y 1 |
| Matriz de confusiÃ³n | Tabla de predicciones vs. realidad |
| Accuracy | % de predicciones correctas totales |
| PrecisiÃ³n | % de positivos predichos que son reales |
| Recall | % de positivos reales que fueron detectados |
| F1-Score | Media armÃ³nica de precisiÃ³n y recall |

## Nota para el docente

El ejemplo de retenciÃ³n de clientes es ideal: los costos de falso negativo (no detectar un cliente que se va) vs. falso positivo (contactar a quien no iba a irse) son fÃ¡cilmente comprensibles.
