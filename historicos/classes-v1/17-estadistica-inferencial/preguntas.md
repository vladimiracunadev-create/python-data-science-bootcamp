# ❓ Preguntas — Clase 17: Estadística inferencial — pruebas de hipótesis

> Preguntas de comprensión, discusión y evaluación para consolidar esta clase.

## 🧠 Preguntas de comprensión

1. ¿Qué es una hipótesis nula (H0) y una hipótesis alternativa (H1)? ¿Por qué siempre se definen en par y antes de ver los datos?
2. ¿Qué es el p-valor? ¿Qué significa que un p-valor sea 0.03 cuando el nivel de significancia es 0.05?
3. ¿Cuándo se usa una prueba t de Student y cuándo se usa una prueba chi-cuadrado? ¿Qué tipo de datos requiere cada una?
4. Explica con tus propias palabras la diferencia entre un Error Tipo I y un Error Tipo II. ¿Cuál es el "falso positivo" y cuál el "falso negativo"?
5. ¿Qué es un intervalo de confianza del 95%? ¿Qué afirmación correcta puedes hacer sobre él y cuál afirmación es incorrecta pero común?

## 💬 Preguntas de discusión

1. Un fabricante dice que sus baterías duran en promedio 100 horas. Compras 30 baterías y el promedio es 95 horas. ¿Cómo usarías una prueba de hipótesis para saber si la diferencia es real o puede explicarse por azar?
2. ¿Por qué "correlación no implica causalidad"? Da un ejemplo real de dos variables que estén correlacionadas pero donde claramente una no causa a la otra.
3. En ensayos clínicos de medicamentos, ¿por qué se usa p < 0.05 como mínimo? ¿En qué tipo de medicamentos (por ejemplo, para cáncer vs. para el resfriado) deberían usar un umbral más estricto y por qué?

## 🧪 Preguntas de código

1. Escribe el código completo para comparar los tiempos de entrega de dos empresas de mensajería usando `scipy.stats.ttest_ind()`. Incluye la visualización previa de ambas distribuciones y la interpretación automática del resultado con `if/else`.
2. Dado un p-valor de 0.032 y un nivel de significancia de 0.05, escribe el código Python que imprima automáticamente si se rechaza o no la hipótesis nula, mostrando el mensaje con el valor del p-valor.
3. Escribe el código para realizar una prueba chi-cuadrado entre las variables `genero` y `aprobado` de un DataFrame de estudiantes. Incluye la tabla de contingencia, el estadístico chi², el p-valor y la interpretación.

## 🎯 Pregunta integradora

Una empresa de retail implementó un nuevo sistema de recomendaciones en su tienda online. Quieren saber si el nuevo sistema aumentó el ticket promedio de compra. Tienen los datos de 200 compras antes del cambio y 200 compras después. Diseña el análisis estadístico completo: (1) define H0 y H1 con precisión, (2) elige la prueba estadística apropiada y justifica tu elección, (3) escribe el código Python completo incluyendo visualización previa, la prueba y la interpretación, (4) explica cómo interpretarías el p-valor obtenido para tomar una decisión de negocio, y (5) menciona qué información adicional (más allá del p-valor) necesitarías para hacer una recomendación completa.
