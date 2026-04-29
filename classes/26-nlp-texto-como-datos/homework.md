# 📝 Homework — Clase 26: Procesamiento de Texto — NLP Básico

> Entrega individual. Plazo: antes de la próxima clase.

---

## Tarea 1 — Analiza tus propias reseñas (obligatoria)

Recopila **10 comentarios reales** de productos, servicios, restaurantes o aplicaciones en español. Puedes tomarlos de Google Maps, Mercado Libre, Amazon, redes sociales, o inventarlos.

Crea un CSV manualmente o con código:

```python
import pandas as pd

mis_comentarios = [
    {"comentario": "Escribe aquí tu comentario 1", "sentimiento": "Positivo"},
    {"comentario": "Escribe aquí tu comentario 2", "sentimiento": "Negativo"},
    # ... agrega al menos 10 filas
]

df_propio = pd.DataFrame(mis_comentarios)
```

Luego:
1. Aplica la función `preprocesar_texto` de clase.
2. Vectoriza con `TfidfVectorizer`.
3. Usa el modelo entrenado en clase para predecir el sentimiento de tus comentarios.
4. ¿El modelo predijo correctamente? ¿En cuáles se equivocó?

---

## Tarea 2 — Experimento con hiperparámetros de TF-IDF (obligatoria)

El `TfidfVectorizer` tiene varios parámetros importantes. Experimenta cambiando cada uno y observa el efecto en el accuracy del clasificador:

```python
experimentos = [
    {'max_features': 100, 'ngram_range': (1, 1)},
    {'max_features': 500, 'ngram_range': (1, 1)},
    {'max_features': 500, 'ngram_range': (1, 2)},
    {'max_features': 1000, 'ngram_range': (1, 2)},
    {'max_features': 1000, 'ngram_range': (1, 3)},
]

resultados = []
for params in experimentos:
    tfidf = TfidfVectorizer(**params)
    X_train_v = tfidf.fit_transform(X_train_raw)
    X_test_v = tfidf.transform(X_test_raw)
    
    modelo = LogisticRegression(max_iter=1000)
    modelo.fit(X_train_v, y_train)
    
    acc = modelo.score(X_test_v, y_test)
    resultados.append({**params, 'accuracy': acc})

print(pd.DataFrame(resultados))
```

**Preguntas:**
1. ¿Qué configuración de TF-IDF dio el mejor accuracy?
2. ¿Agregar bigramas (`ngram_range=(1,2)`) siempre mejora el resultado?
3. ¿Cuál es el efecto de aumentar `max_features`?

---

## Tarea 3 — Investiga: ¿qué sigue después del BoW? (opcional, +1 punto)

El Bag of Words ignora el orden de las palabras. Investiga y explica brevemente:

- ¿Qué son los **Word Embeddings** (word2vec, GloVe)?
- ¿Cómo representan el significado de las palabras de manera diferente al TF-IDF?
- ¿Qué es un modelo de lenguaje como BERT?

No necesitas implementarlo. Con 3-4 párrafos claros es suficiente. Incluye una analogía de tu propia creación para explicar la diferencia entre BoW y word embeddings.

---

## Formato de entrega

- Archivo `.ipynb` con código comentado y celdas de texto con tus respuestas.
- Nombre del archivo: `homework_clase26_[tu_nombre].ipynb`

---

## Rúbrica

| Criterio | Puntos |
|---|---|
| Tarea 1: 10 comentarios propios preparados | 2 |
| Tarea 1: predicciones del modelo y análisis | 3 |
| Tarea 2: experimentos con TF-IDF | 3 |
| Tarea 2: interpretación de resultados | 2 |
| Tarea 3 (opcional) | 1 |
| **Total** | **10 (+1)** |
