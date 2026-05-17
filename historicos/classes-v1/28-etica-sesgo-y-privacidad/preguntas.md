# ❓ Preguntas — Clase 28: Ética, Sesgo y Privacidad

> Preguntas de comprensión, discusión y evaluación para esta clase.

## 🧠 Preguntas de comprensión

1. ¿Cuáles son los tres tipos principales de sesgo en datos que vimos en clase? Describe brevemente cada uno con un ejemplo diferente al visto en clase.
2. ¿Qué es el **sesgo histórico** en un dataset? ¿Por qué es especialmente difícil de eliminar?
3. ¿Qué significa que un modelo de machine learning sea "justo" (fair)? ¿Existe una sola definición de justicia algorítmica?
4. ¿Qué son los **valores SHAP** y qué información nos dan sobre cómo un modelo toma decisiones?
5. ¿Cuáles son los principios básicos del **RGPD** (GDPR) en relación con el manejo de datos personales? Menciona al menos tres.
6. ¿Qué es la **IA responsable** (Responsible AI)? Menciona tres principios que la guían.
7. ¿Por qué un modelo puede tener alta accuracy general pero ser injusto con ciertos grupos de la población?

## 💬 Preguntas de discusión

1. Se descubrió que un sistema de selección de currículos de una empresa tecnológica penalizaba a candidatas mujeres. ¿Qué tipo de sesgo tiene esto? ¿Cómo pudo ocurrir si el sistema nunca vio directamente el sexo de los candidatos?
2. Un hospital quiere usar un modelo para predecir qué pacientes necesitarán cuidados intensivos. El dataset histórico proviene de los últimos 10 años, pero antes los médicos tenían sesgos en quién derivaban a UCI. ¿Cómo afecta esto al modelo?
3. ¿Crees que la privacidad y la utilidad de los datos son siempre opuestas? ¿Hay formas de tener ambas? Piensa en técnicas como la anonimización.
4. Un modelo de crédito bancario tiene accuracy del 92% pero solo el 65% para personas de cierto origen étnico. ¿Es este modelo aceptable? ¿Qué métricas de equidad deberían exigirse?
5. ¿Quién tiene la responsabilidad ética de los errores de un sistema de IA: el científico de datos que lo construyó, la empresa que lo desplegó, o el cliente que lo usa?
6. Discute: ¿debería ser obligatorio por ley que los sistemas de IA usados en decisiones críticas (créditos, selección laboral, justicia penal) sean explicables? ¿Qué implicaciones tendría esto?

## 🧪 Preguntas de código

1. Dado el dataset `estudiantes.csv`, ¿cómo calcularías la tasa de aprobación por género usando pandas? Escribe el código.
2. Si un modelo tiene accuracy del 88% para hombres y 74% para mujeres en el mismo dataset, ¿cómo detectarías esta disparidad en el código? ¿Qué ajuste harías?
3. ¿Cómo usarías `class_weight='balanced'` en un clasificador de sklearn para compensar un dataset desbalanceado? ¿En qué casos tiene sentido?
4. Escribe el código para instalar `shap` y generar un gráfico de summary plot que muestre qué variables influyen más en las predicciones de un modelo.
5. ¿Cómo anonimizarías en pandas una columna con nombres de estudiantes y otra con números de identificación antes de compartir el dataset?
6. ¿Cómo calcularías y compararías las tasas de falsos positivos y falsos negativos entre grupos demográficos usando la matriz de confusión?

## 🎯 Pregunta integradora

Eres el data scientist líder en una empresa que va a desplegar un modelo de predicción de deserción escolar. El modelo predice qué estudiantes tienen riesgo de abandonar la escuela, y los resultados se usarán para asignar tutorías. Identifica al menos tres riesgos éticos concretos de este sistema, propón cómo mitigarlos técnicamente, y describe qué proceso de revisión ética implementarías antes del despliegue. Incluye: tipos de sesgo que podrían aparecer, métricas de equidad a monitorear, consideraciones de privacidad según el RGPD, y cómo explicarías las decisiones del modelo a estudiantes y familias afectadas.
