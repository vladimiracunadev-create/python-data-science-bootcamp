# 📘 Clase 23: Reducción de dimensionalidad — PCA

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Comprender el problema de la "maldición de la dimensionalidad" y aprender a reducir datos de muchas variables a unas pocas componentes principales usando PCA. Al final de la clase el alumno podrá comprimir información de 4 o más columnas en 2 dimensiones y visualizarla en un scatter plot, entendiendo cuánta información se conserva con cada componente.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/estudiantes.csv` (4+ columnas numéricas)
- `datasets/ventas_tienda.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Explicar qué es la dimensionalidad y por qué reducirla puede ser útil
- Aplicar PCA con sklearn para reducir un dataset de varias dimensiones a 2 componentes
- Interpretar el `explained_variance_ratio_` para saber cuánta información se conserva

## 🧭 Temas clave
- La maldición de la dimensionalidad: más columnas = más difícil aprender
- PCA: encontrar las direcciones de mayor varianza en los datos
- `PCA(n_components=2)`, `fit_transform`, `explained_variance_ratio_`
- Biplot: visualizar muestras Y variables en el mismo espacio 2D
- Usar PCA antes de clustering o visualización
- Limitación: las componentes son difíciles de interpretar directamente

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.

## 💡 Idea central
PCA encuentra las direcciones de mayor variación en los datos para representar información compleja con menos dimensiones.

## 👩‍🏫 Nota para el docente
Usa la analogía de la sombra: si sostienes una pelota de béisbol frente a una lámpara, la sombra en la pared es una proyección 2D del objeto 3D. PCA elige el ángulo que produce la sombra más "informativa" — la que revela mejor la forma del objeto. Funciona para todas las edades y hace que el concepto de "proyección" sea tangible.
