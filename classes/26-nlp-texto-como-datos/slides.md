# 🎞️ Slides — Clase 26: Procesamiento de Texto — NLP Básico

---

## Slide 1 — ¿Qué problema resolvemos hoy?

Una empresa tiene 10,000 reseñas de clientes.
¿Cómo sabe automáticamente cuáles son positivas y cuáles negativas?

**Respuesta:** con NLP (Natural Language Processing).

---

## Slide 2 — ¿Por qué el texto es difícil para las computadoras?

- Las computadoras trabajan con números, no palabras.
- Una misma idea puede expresarse de mil formas: "me encantó", "excelente", "muy bueno", "10/10".
- El contexto cambia el significado: "no está mal" = positivo.
- Los idiomas tienen reglas diferentes, abreviaturas, errores de tipeo.

> 💡 Necesitamos un puente entre palabras y números.

---

## Slide 3 — Pipeline de preprocesamiento de texto

```
Texto original:
"¡El producto llegó MUY rápido!! Excelente calidad."

Paso 1 — Minúsculas:
"¡el producto llegó muy rápido!! excelente calidad."

Paso 2 — Eliminar puntuación:
"el producto llegó muy rápido excelente calidad"

Paso 3 — Eliminar stop words (el, de, que, en...):
"producto llegó rápido excelente calidad"
```

Ahora el texto está limpio y listo para convertirse en números.

---

## Slide 4 — Bag of Words (Bolsa de Palabras)

Idea: cada documento se representa como el conteo de sus palabras.

```
Vocabulario: [producto, llegó, rápido, excelente, malo, lento]

Doc 1: "producto llegó rápido excelente"  → [1, 1, 1, 1, 0, 0]
Doc 2: "producto malo lento"              → [1, 0, 0, 0, 1, 1]
```

Se pierde el orden, pero se captura la presencia de palabras importantes.

---

## Slide 5 — CountVectorizer en sklearn

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "el producto es excelente",
    "muy malo no lo recomiendo",
    "llegó rápido y en perfectas condiciones"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print(vectorizer.vocabulary_)
print(X.toarray())
```

---

## Slide 6 — El problema del Bag of Words

Palabras muy comunes como "el", "de", "producto" aparecen en TODOS los documentos.
No nos dicen nada sobre el sentimiento.

> 💡 Necesitamos premiar las palabras raras y penalizar las comunes.

**Solución: TF-IDF**

---

## Slide 7 — TF-IDF: palabras que realmente importan

**TF** (Term Frequency): ¿cuántas veces aparece la palabra en este documento?
**IDF** (Inverse Document Frequency): ¿en cuántos documentos aparece? Si aparece en todos → menos importante.

```
TF-IDF = TF × log(N / df)

- "excelente" aparece en 2 de 100 docs → IDF alto → importa
- "producto" aparece en 98 de 100 docs → IDF bajo → no importa
```

---

## Slide 8 — TfidfVectorizer en sklearn

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(max_features=500)
X = tfidf.fit_transform(textos)
```

Cada documento queda como un vector de scores entre 0 y 1.
Las palabras más distintivas tienen scores más altos.

---

## Slide 9 — Clasificación de sentimientos

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

print(classification_report(y_test, modelo.predict(X_test)))
```

---

## Slide 10 — ¿Qué palabras usa el modelo?

```python
# Palabras más asociadas a cada sentimiento
feature_names = tfidf.get_feature_names_out()
coefs = modelo.coef_[0]

top_positivos = feature_names[coefs.argsort()[-10:]]
top_negativos = feature_names[coefs.argsort()[:10]]
```

Esto nos dice exactamente qué palabras el modelo aprendió a asociar con cada sentimiento.

---

## Slide 11 — Resumen del pipeline completo

```
Texto crudo
   ↓ Limpieza (lower, puntuación, stop words)
Texto limpio
   ↓ TfidfVectorizer
Matriz numérica X
   ↓ LogisticRegression
Predicción de sentimiento
```

---

## Slide 12 — Conclusión

- El texto necesita ser convertido a números antes de usarse en ML.
- Bag of Words captura la presencia de palabras.
- TF-IDF captura la importancia relativa de cada palabra.
- Con estas representaciones, podemos clasificar texto como cualquier otro dato.
