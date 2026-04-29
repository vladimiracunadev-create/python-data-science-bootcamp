# 📖 Teoría — Clase 26: Procesamiento de Texto — NLP Básico

## 1. ¿Qué es el NLP?

El **Procesamiento de Lenguaje Natural** (NLP, por sus siglas en inglés: *Natural Language Processing*) es la rama de la inteligencia artificial que permite a las computadoras entender, interpretar y generar lenguaje humano.

Aplicaciones cotidianas de NLP:
- Traducción automática (Google Translate)
- Asistentes de voz (Siri, Alexa, Google Assistant)
- Corrector ortográfico y autocompletado en el celular
- Filtros de spam en el correo electrónico
- Análisis de sentimientos en redes sociales
- Chatbots de atención al cliente

---

## 2. ¿Por qué el texto es difícil para las computadoras?

Los algoritmos de Machine Learning esperan números como entrada. El texto presenta varios desafíos:

**Sin estructura numérica directa:** "bueno" no es mayor que "malo" en ningún sentido matemático obvio.

**Ambigüedad:** "El banco estaba lleno" — ¿banco del parque o banco financiero?

**Contexto:** "No está mal" significa algo positivo. "Estuvo buenísimo... para quedarse dormido" es sarcasmo.

**Variabilidad:** "genial", "excelente", "10/10", "me encantó", "lo recomiendo" pueden significar lo mismo.

**Errores humanos:** "mui varato", "exelente", "prodcuto" — las personas escriben con errores.

---

## 3. Pipeline de preprocesamiento de texto

Antes de convertir texto en números, es importante limpiarlo. El pipeline típico incluye:

### Paso 1: Convertir a minúsculas
```python
texto = "¡El Producto Llegó MUY Rápido!"
texto = texto.lower()
# "¡el producto llegó muy rápido!"
```
"Excelente" y "excelente" son la misma palabra para nosotros, pero son distintos tokens para la computadora si no normalizamos.

### Paso 2: Eliminar puntuación y caracteres especiales
```python
import re
texto = re.sub(r'[^\w\s]', '', texto)
# "el producto llegó muy rápido"
```

### Paso 3: Eliminar stop words
Las **stop words** son palabras muy comunes que aparecen en casi todos los textos y no aportan significado diferenciador: "el", "la", "de", "que", "un", "en", "y", "a", "los".

```python
stop_words = {'el', 'la', 'de', 'que', 'un', 'en', 'y', 'a', 'los', 'las',
              'se', 'del', 'al', 'por', 'con', 'no', 'una', 'su', 'para'}

palabras = texto.split()
palabras_limpias = [p for p in palabras if p not in stop_words]
texto_limpio = ' '.join(palabras_limpias)
```

### (Opcional) Stemming y Lematización
- **Stemming:** reduce la palabra a su raíz ("corriendo" → "corr", "corrí" → "corr").
- **Lematización:** reduce la palabra a su forma base ("corriendo" → "correr").

---

## 4. Modelo Bag of Words (Bolsa de Palabras)

El modelo Bag of Words (BoW) es la representación más simple de texto. Cada documento se convierte en un vector de conteos de palabras, ignorando el orden.

**Ejemplo:**

Vocabulario: [bueno, malo, rápido, lento, excelente]

| Documento | bueno | malo | rápido | lento | excelente |
|---|---|---|---|---|---|
| "producto bueno y rápido" | 1 | 0 | 1 | 0 | 0 |
| "producto malo muy lento" | 0 | 1 | 0 | 1 | 0 |
| "excelente bueno y rápido" | 1 | 0 | 1 | 0 | 1 |

Se pierde el orden de las palabras, pero se captura qué palabras están presentes y con qué frecuencia.

---

## 5. CountVectorizer en sklearn

```python
from sklearn.feature_extraction.text import CountVectorizer

textos = [
    "el producto es excelente muy bueno",
    "muy malo no lo recomiendo para nada",
    "llegó rápido y en perfectas condiciones excelente"
]

vectorizer = CountVectorizer(
    max_features=1000,   # máximo 1000 palabras en el vocabulario
    min_df=2,            # ignorar palabras que aparecen en menos de 2 docs
    stop_words=None      # podemos pasar lista de stop words aquí
)

X = vectorizer.fit_transform(textos)

# Ver el vocabulario
print(vectorizer.vocabulary_)

# Ver la matriz como array
print(X.toarray())
```

El resultado es una **matriz dispersa** (sparse matrix): tiene muchos ceros porque cada documento solo usa una fracción del vocabulario total.

---

## 6. TF-IDF: relevancia relativa de palabras

**TF-IDF** (Term Frequency - Inverse Document Frequency) mejora el Bag of Words al ponderar las palabras según su importancia relativa.

### TF (Term Frequency)
¿Con qué frecuencia aparece la palabra en este documento específico?

```
TF(t, d) = número de veces que aparece t en d / total de palabras en d
```

### IDF (Inverse Document Frequency)
¿En cuántos documentos aparece esta palabra? Si aparece en todos, no es informativa.

```
IDF(t) = log(N / número de documentos que contienen t)

Donde N = total de documentos
```

### TF-IDF final
```
TF-IDF(t, d) = TF(t, d) × IDF(t)
```

**Ejemplo intuitivo:**
- La palabra "producto" aparece en 95 de 100 reseñas → IDF muy bajo → TF-IDF bajo.
- La palabra "defectuoso" aparece en 3 de 100 reseñas → IDF alto → TF-IDF alto en esas 3 reseñas.

### TfidfVectorizer en sklearn

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(
    max_features=500,
    ngram_range=(1, 2),  # unigramas y bigramas: "bueno", "muy bueno"
    sublinear_tf=True    # usar log(TF) en lugar de TF bruto
)

X = tfidf.fit_transform(textos_limpios)
```

---

## 7. N-gramas: capturar frases

Los modelos anteriores tratan cada palabra por separado. Los **n-gramas** capturan secuencias de n palabras consecutivas:

- **Unigramas (n=1):** "muy", "bueno"
- **Bigramas (n=2):** "muy bueno", "no recomiendo"
- **Trigramas (n=3):** "muy bueno precio"

```python
# Bigramas: captura "no recomiendo" como una unidad
# Sin bigramas, "no" y "recomiendo" son palabras separadas
# Con bigramas, "no_recomiendo" es un token con significado propio
tfidf = TfidfVectorizer(ngram_range=(1, 2))
```

---

## 8. Clasificación de texto con LogisticRegression

Una vez que tenemos el texto representado como vectores numéricos, podemos usar cualquier algoritmo de clasificación. LogisticRegression funciona muy bien para texto:

```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Entrenar
modelo = LogisticRegression(max_iter=1000, C=1.0)
modelo.fit(X_train, y_train)

# Evaluar
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))
```

---

## 9. ¿Qué palabras aprendió el modelo?

Una de las ventajas de LogisticRegression para NLP es que podemos inspeccionar los coeficientes para entender qué palabras son más importantes para cada clase:

```python
feature_names = tfidf.get_feature_names_out()
coefs = modelo.coef_

# Para clasificación binaria (Positivo vs Negativo)
indices_positivos = coefs[0].argsort()[-15:][::-1]
indices_negativos = coefs[0].argsort()[:15]

print("Palabras más positivas:")
print(feature_names[indices_positivos])

print("Palabras más negativas:")
print(feature_names[indices_negativos])
```

Esto nos da interpretabilidad: podemos explicar por qué el modelo clasifica un texto de cierta manera.

---

## 10. Evaluación de clasificadores de texto

Para texto con múltiples clases (Positivo, Negativo, Neutro), usamos `classification_report`:

```
              precision    recall  f1-score   support

    Negativo       0.82      0.79      0.80        28
      Neutro       0.71      0.65      0.68        20
    Positivo       0.88      0.92      0.90        52

    accuracy                           0.83       100
```

- **Precision:** De los que predije como Positivo, ¿cuántos realmente lo son?
- **Recall:** De los que son realmente Positivos, ¿cuántos encontré?
- **F1-score:** Media armónica entre precision y recall.

---

## 11. Resumen de herramientas de NLP en sklearn

| Herramienta | Qué hace |
|---|---|
| `CountVectorizer` | Convierte texto en conteos de palabras (BoW) |
| `TfidfVectorizer` | Convierte texto en scores TF-IDF ponderados |
| `LogisticRegression` | Clasificador lineal eficiente para texto |
| `classification_report` | Métricas detalladas de clasificación |
| `coef_` | Importancia de cada palabra por clase |
