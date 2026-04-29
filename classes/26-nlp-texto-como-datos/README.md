# 📘 Clase 26: Procesamiento de Texto — NLP Básico

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Introducir el procesamiento de lenguaje natural (NLP) y aprender a convertir texto en representaciones numéricas usando Bag of Words y TF-IDF, para entrenar un clasificador de sentimientos sobre reseñas de productos en español.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/comentarios_productos.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Preprocesar texto (minúsculas, puntuación, stop words), vectorizar documentos con CountVectorizer y TfidfVectorizer, entrenar un clasificador de sentimientos con LogisticRegression.

## 🧭 Temas clave
- ¿Qué es NLP?
- Pipeline de preprocesamiento de texto
- Bag of Words y CountVectorizer
- TF-IDF y TfidfVectorizer
- Clasificación de sentimientos
- Palabras más importantes por clase (coef_)
- Evaluación con classification_report

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.

## 💡 Idea central
El procesamiento de texto convierte palabras en números para que los modelos puedan aprender a entender el lenguaje.

## 👩‍🏫 Nota para el docente
Comienza con 5 oraciones simples antes de cargar el dataset completo. Si los estudiantes tienen instalada la librería wordcloud, es muy visual mostrar una nube de palabras por sentimiento. Resalta que TF-IDF penaliza palabras muy comunes como "el", "de", "que" que no aportan significado.
