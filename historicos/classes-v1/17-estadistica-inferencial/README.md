# 📘 Clase 17: Estadística inferencial — pruebas de hipótesis

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Comprender la diferencia entre estadística descriptiva e inferencial, y aprender a usar pruebas de hipótesis para determinar si una diferencia observada en los datos es real o producto del azar. El estudiante aplicará la prueba t de Student y la prueba chi-cuadrado sobre datasets reales de transporte y estudiantes, interpretando el p-value de forma práctica y accesible.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/transporte.csv`
- `datasets/estudiantes.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Explicar con sus propias palabras qué es un p-value y qué significa que sea menor a 0.05.
- Aplicar una prueba t de Student para comparar dos grupos numéricos y una prueba chi-cuadrado para comparar distribuciones categóricas.
- Identificar errores de tipo I y tipo II y entender sus consecuencias prácticas.

## 🧭 Temas clave
- Diferencia entre estadística descriptiva e inferencial
- Concepto de población vs muestra (analogía: no necesitas comer toda la sopa para saber si le falta sal)
- Intervalos de confianza (qué significan en términos simples)
- Qué es una prueba de hipótesis (H0 y H1)
- p-value explicado de forma simple (si p < 0.05, el resultado probablemente es real, no fruto del azar)
- Prueba t (`scipy.stats.ttest_ind`) para comparar dos grupos
- Prueba chi-cuadrado (`scipy.stats.chi2_contingency`) para comparar distribuciones categóricas
- Error tipo I (falsa alarma) y error tipo II (detección fallida)
- Ejemplo práctico: ¿El retraso es realmente diferente en días de lluvia? ¿Las notas difieren según el curso?

## 🧰 Materiales del módulo
- `README.md`
- `slides.md`
- `teoria.md`
- `ejercicios.md`
- `homework.md`
- `notebook.ipynb`
- `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.
- Los comentarios deben explicar qué hace el bloque y para qué sirve.
- Antes de pasar al siguiente paso, verifica que entiendes la salida.

## 💡 Idea central
Las pruebas de hipótesis nos dicen si una diferencia que vemos en los datos es real o simplemente producto del azar.

## 👩‍🏫 Nota para el docente
Usa la analogía de la moneda: si tiras 60 caras de 100 lanzamientos, ¿la moneda está cargada? Eso es exactamente una prueba de hipótesis. Esta analogía hace que el concepto de p-value sea intuitivo antes de ver cualquier fórmula. Refuerza siempre que el p-value no dice "qué tan importante es la diferencia", sino "qué tan probable es que la diferencia sea por azar".
