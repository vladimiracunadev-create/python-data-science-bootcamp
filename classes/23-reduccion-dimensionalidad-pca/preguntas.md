# ❓ Preguntas — Clase 23: Reducción de Dimensionalidad y PCA

> Preguntas de comprensión, discusión y evaluación.

## 🧠 Preguntas de comprensión

1. ¿Qué es la "maldición de la dimensionalidad"? ¿Por qué agregar más variables a un dataset puede perjudicar en lugar de ayudar a un modelo?
2. Explica la metáfora de la "sombra que captura la forma": ¿qué relación tiene con lo que hace PCA matemáticamente?
3. ¿Qué representa cada componente principal? ¿Por qué el primer componente siempre explica más varianza que el segundo?
4. ¿Qué información te da `explained_variance_ratio_`? ¿Cómo usarías esa información para decidir cuántos componentes conservar?
5. ¿Por qué es obligatorio normalizar los datos antes de aplicar PCA?
6. ¿Qué es un biplot y qué información muestra sobre las variables originales?
7. ¿Cuál es la ventaja de aplicar PCA antes de clustering? ¿Qué problema de K-Means ayuda a reducir?

## 💬 Preguntas de discusión

1. Tienes un dataset con 50 variables y quieres reducirlo a 2 dimensiones para visualizar. El gráfico PCA muestra que los grupos no se separan bien. ¿Significa eso que no hay estructura en los datos? ¿Qué otras opciones explorarías?
2. Un compañero dice: "PCA elimina variables, así que perdemos información". ¿Es correcto? ¿Cómo explicarías la diferencia entre selección de features y PCA?
3. ¿En qué situaciones preferirías mantener todas las variables originales en lugar de aplicar PCA, a pesar de la alta dimensionalidad?

## 🧪 Preguntas de código

1. Aplica PCA con 2 componentes sobre `estudiantes.csv` (con al menos 5 variables numéricas). Grafica los puntos en el espacio de 2 componentes y colorea por la variable `aprobado`. ¿Se separan los grupos?
2. Calcula y grafica la varianza acumulada (scree plot) para 1 hasta n componentes. ¿Cuántos componentes necesitas para explicar el 90% de la varianza?
3. Crea un pipeline que aplique `StandardScaler` → `PCA(n_components=2)` → `KMeans(n_clusters=3)` sobre `estudiantes.csv`. Visualiza el resultado.

## 🎯 Pregunta integradora

Usa `estudiantes.csv` con todas las variables numéricas disponibles. Primero aplica PCA completo (sin reducir) y grafica el scree plot de varianza acumulada. Determina el número de componentes que explican el 85% de la varianza. Luego: (1) crea un biplot con los 2 primeros componentes mostrando la dirección de las variables originales, (2) interpreta cuáles variables están más correlacionadas entre sí (apuntan en dirección similar) y cuáles son ortogonales (independientes), (3) aplica K-Means sobre estos 2 componentes y compara la calidad del clustering (silhouette) contra aplicarlo sobre todas las variables originales.
