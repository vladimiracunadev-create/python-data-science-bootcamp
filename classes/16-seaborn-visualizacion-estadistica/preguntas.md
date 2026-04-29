# ❓ Preguntas — Clase 16: Seaborn y visualización estadística

> Preguntas de comprensión, discusión y evaluación para consolidar esta clase.

## 🧠 Preguntas de comprensión

1. ¿Cuál es la diferencia principal entre un histograma (`histplot`) y un gráfico de densidad (`kdeplot`)? ¿Qué muestra cada uno en el eje Y?
2. ¿Qué información muestra un boxplot? Identifica los 5 elementos que lo componen (caja, bigotes, línea central, etc.).
3. ¿En qué se diferencia un violinplot de un boxplot? ¿Qué ventaja ofrece el violinplot al usar `inner="box"`?
4. ¿Para qué sirve el parámetro `hue` en los gráficos de Seaborn? ¿Qué tipo de columna debe ser la que se pasa como `hue`?
5. ¿Qué muestra un heatmap de correlación y qué significa un valor cercano a 1, a -1 y a 0?

## 💬 Preguntas de discusión

1. ¿Por qué es importante visualizar la distribución de los datos antes de calcular la media? ¿Qué podría pasar si la distribución es muy asimétrica y solo reportas el promedio?
2. ¿Cuándo usarías un boxplot versus un violinplot para presentar datos a directivos de empresa que no tienen formación técnica?
3. Si el heatmap de correlación muestra que dos variables tienen una correlación de 0.95, ¿eso significa que una causa a la otra? ¿Por qué?

## 🧪 Preguntas de código

1. Escribe el código para crear un histograma de la columna `ventas` del DataFrame `df` con 20 intervalos y una línea KDE superpuesta, con título y etiquetas en los ejes.
2. ¿Cómo crearías un boxplot que compare la distribución de `ventas` para cada valor único en la columna `categoria`? Incluye el código completo con configuración del tamaño de figura.
3. Dado un DataFrame `df` con varias columnas numéricas, escribe el código para crear un heatmap de correlación con los valores numéricos anotados en cada celda, usando la paleta `"coolwarm"`.

## 🎯 Pregunta integradora

Tienes un dataset de notas de estudiantes con las columnas: `nombre`, `edad`, `sexo`, `nota_matematicas`, `nota_ciencias`, `nota_lenguaje`, `horas_estudio`. Diseña un análisis visual completo usando Seaborn: (1) elige al menos 4 tipos de gráficos distintos de los vistos en clase, (2) explica qué pregunta analítica específica responde cada gráfico, (3) describe qué insights esperarías encontrar y por qué, y (4) escribe el código completo para al menos 2 de los gráficos incluyendo títulos y etiquetas.
