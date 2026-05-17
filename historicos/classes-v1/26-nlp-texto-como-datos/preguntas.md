# ❓ Preguntas — Clase 26: NLP — Texto como Datos

> Preguntas de comprensión, discusión y evaluación para esta clase.

## 🧠 Preguntas de comprensión

1. ¿Qué significa "vectorizar" texto y por qué es necesario antes de pasarlo a un modelo de machine learning?
2. ¿Qué diferencia hay entre `CountVectorizer` y `TfidfVectorizer`? ¿Cuál de los dos penaliza las palabras muy frecuentes en todos los documentos?
3. Explica con tus palabras qué significa "TF-IDF". ¿Qué mide el término TF y qué mide el término IDF?
4. ¿Por qué se llama "Bag of Words" (bolsa de palabras) a la representación que genera `CountVectorizer`? ¿Qué información se pierde con esta representación?
5. ¿Qué hace el paso de **preprocesamiento de texto** antes de vectorizar? Menciona al menos 4 técnicas comunes.
6. ¿Para qué sirve el parámetro `stop_words` en los vectorizadores de sklearn? ¿Qué tipo de palabras elimina?
7. ¿Cómo se interpreta la **importancia de características por clase** en un modelo de clasificación de texto con `LogisticRegression`?

## 💬 Preguntas de discusión

1. El dataset `comentarios_productos.csv` tiene reseñas en español. ¿Por qué no se puede usar directamente `stop_words='english'`? ¿Cómo resolverías esto?
2. Imagina que tienes un comentario: "¡¡¡PÉSIMO PRODUCTO!!!! no lo recomiendo para NADA". ¿Qué pasos de preprocesamiento aplicarías y por qué?
3. ¿Crees que la etiqueta "Neutro" es más difícil de clasificar que "Positivo" o "Negativo"? ¿Por qué?
4. Discute las limitaciones del modelo Bag of Words: ¿qué tipos de frases confundiría? Ejemplo: "no es malo" vs "es malo".
5. ¿En qué situaciones reales de negocio sería útil clasificar automáticamente comentarios de productos? Da tres ejemplos concretos.
6. ¿Por qué se usa `LogisticRegression` frecuentemente para clasificación de texto en lugar de modelos más complejos como redes neuronales?

## 🧪 Preguntas de código

1. Escribe el código para cargar `comentarios_productos.csv`, aplicar `TfidfVectorizer` y dividir en train/test con estratificación por la columna `sentimiento`.
2. ¿Cómo obtienes la lista de palabras (vocabulario) que aprendió el `CountVectorizer` después de entrenarlo? Escribe el código.
3. Escribe el código para mostrar las 10 palabras con mayor peso para la clase "Positivo" en un modelo `LogisticRegression` entrenado sobre texto.
4. ¿Cómo usarías el modelo entrenado para predecir el sentimiento de una nueva reseña: "El producto llegó rápido y funciona perfecto"?
5. Escribe el código para mostrar el `classification_report` con precisión, recall y F1-score por clase.
6. ¿Cómo modificarías el `TfidfVectorizer` para incluir bigramas (pares de palabras consecutivas) además de palabras individuales?

## 🎯 Pregunta integradora

Eres data scientist en una empresa de e-commerce que recibe 50.000 reseñas de productos por día. Describe el pipeline completo que construirías para clasificar automáticamente cada reseña como Positiva, Negativa o Neutra. Incluye: limpieza de texto, vectorización, elección del modelo, evaluación, y cómo gestionarías el caso de que las clases estén desbalanceadas (por ejemplo, 80% Positivo, 15% Negativo, 5% Neutro). ¿Qué métricas reportarías al equipo de negocio y por qué?
