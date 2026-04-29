# 🏋️ Ejercicios — Clase 26: Procesamiento de Texto — NLP Básico

> Completa estos ejercicios en orden. Cada uno construye sobre el anterior.

---

## Ejercicio 1 — Preprocesamiento manual

Dado el siguiente texto, aplica manualmente el pipeline de preprocesamiento:

```
"¡¡¡El envío llegó MUY TARDE!!! Me prometieron 3 días y tardó 15. 
Además, el producto estaba dañado. NO lo recomiendo para nada."
```

**Pasos a seguir:**
1. Convierte a minúsculas.
2. Elimina signos de puntuación y caracteres especiales.
3. Elimina las siguientes stop words: `el, la, me, lo, y, no, además, de, a, para, en`.
4. Escribe el texto resultante.

**Ahora en código:**
```python
import re

texto = "¡¡¡El envío llegó MUY TARDE!!! Me prometieron 3 días y tardó 15. Además, el producto estaba dañado. NO lo recomiendo para nada."

# Paso 1: minúsculas
texto_lower = # tu código aquí

# Paso 2: eliminar puntuación
texto_limpio = # tu código aquí (pista: usa re.sub)

# Paso 3: eliminar stop words
stop_words = {'el', 'la', 'me', 'lo', 'y', 'no', 'además', 'de', 'a', 'para', 'en', 'que', 'se'}
palabras = texto_limpio.split()
texto_final = # tu código aquí

print(texto_final)
```

---

## Ejercicio 2 — CountVectorizer con frases simples

Antes de usar el dataset completo, experimenta con 5 frases:

```python
from sklearn.feature_extraction.text import CountVectorizer

frases = [
    "el producto es excelente muy recomendado",
    "muy malo no lo recomiendo para nada",
    "llegó rápido producto bien empacado",
    "producto defectuoso muy decepcionante",
    "calidad excelente precio justo llegó rápido"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(frases)

print("Vocabulario:")
print(vectorizer.vocabulary_)
print("\nForma de la matriz:", X.shape)
print("\nMatriz como array:")
print(X.toarray())
```

**Preguntas:**
1. ¿Cuántas palabras tiene el vocabulario?
2. ¿Cuál frase tiene el mayor conteo total de palabras?
3. ¿Qué palabra aparece en más frases?
4. Agrega `stop_words=['el', 'la', 'lo', 'muy', 'no', 'para']` al CountVectorizer. ¿Cómo cambia el vocabulario?

---

## Ejercicio 3 — TF-IDF con las mismas frases

```python
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(frases)

df_tfidf = pd.DataFrame(
    X_tfidf.toarray(),
    columns=tfidf.get_feature_names_out()
)
print(df_tfidf.round(3))
```

**Preguntas:**
1. Compara la matriz de CountVectorizer con la de TF-IDF. ¿Qué diferencias observas?
2. ¿Qué palabra tiene el score TF-IDF más alto en la frase 1? ¿Por qué?
3. La palabra "producto" aparece en varias frases. ¿Tiene un score TF-IDF alto o bajo? ¿Por qué?

---

## Ejercicio 4 — Cargar y explorar el dataset real

```python
import pandas as pd

df = pd.read_csv('datasets/comentarios_productos.csv')
print("Forma:", df.shape)
print("\nColumnas:", df.columns.tolist())
print("\nPrimeras filas:")
print(df.head())
print("\nDistribución de sentimientos:")
print(df['sentimiento'].value_counts())
```

**Preguntas:**
1. ¿Cuántas reseñas tiene el dataset?
2. ¿Está balanceado el dataset entre clases?
3. Lee 3 comentarios de cada clase. ¿Puedes identificar patrones de palabras?

---

## Ejercicio 5 — Función de preprocesamiento

Crea una función reutilizable que aplique el pipeline completo:

```python
import re

stop_words_es = {
    'el', 'la', 'los', 'las', 'un', 'una', 'de', 'del', 'al', 'en',
    'que', 'y', 'a', 'se', 'no', 'me', 'te', 'lo', 'le', 'su', 'por',
    'con', 'para', 'es', 'son', 'fue', 'era', 'pero', 'si', 'como'
}

def preprocesar_texto(texto):
    """
    Aplica el pipeline de preprocesamiento:
    1. Minúsculas
    2. Eliminar puntuación y números
    3. Eliminar stop words
    4. Eliminar espacios extra
    """
    # Tu implementación aquí
    pass

# Probar la función
ejemplo = "¡¡Llegó muy rápido!! El producto es excelente, lo recomiendo al 100%."
print(preprocesar_texto(ejemplo))

# Aplicar al dataset
df['texto_limpio'] = df['comentario'].apply(preprocesar_texto)
print(df[['comentario', 'texto_limpio']].head(3))
```

---

## Ejercicio 6 — Clasificador de sentimientos completo

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Preparar datos
X_raw = df['texto_limpio']
y = df['sentimiento']

# Dividir
X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X_raw, y, test_size=0.2, random_state=42, stratify=y
)

# Vectorizar
tfidf = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
X_train = tfidf.fit_transform(X_train_raw)
X_test = tfidf.transform(X_test_raw)  # ¡solo transform, no fit_transform!

# Entrenar
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train, y_train)

# Evaluar
y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))

# Matriz de confusión
cm = confusion_matrix(y_test, y_pred, labels=modelo.classes_)
sns.heatmap(cm, annot=True, fmt='d', xticklabels=modelo.classes_, yticklabels=modelo.classes_)
plt.title('Matriz de confusión')
plt.ylabel('Real')
plt.xlabel('Predicho')
plt.show()
```

**Preguntas:**
1. ¿Qué clase tiene mejor F1-score? ¿A qué crees que se debe?
2. ¿Qué clase confunde más el modelo? ¿Tiene sentido intuitivamente?
3. ¿Por qué usamos `tfidf.transform()` en el test set y no `fit_transform()`?

---

## Ejercicio 7 — Palabras más importantes

```python
import numpy as np

feature_names = tfidf.get_feature_names_out()
clases = modelo.classes_

fig, axes = plt.subplots(1, len(clases), figsize=(15, 5))

for idx, clase in enumerate(clases):
    coefs = modelo.coef_[idx]
    top_indices = coefs.argsort()[-10:][::-1]
    top_palabras = feature_names[top_indices]
    top_scores = coefs[top_indices]

    axes[idx].barh(top_palabras, top_scores, color='steelblue')
    axes[idx].set_title(f'Palabras clave: {clase}')
    axes[idx].set_xlabel('Coeficiente')

plt.tight_layout()
plt.show()
```

**Preguntas:**
1. ¿Las palabras más importantes para cada clase tienen sentido?
2. ¿Hay alguna palabra sorprendente que el modelo consideró importante?
3. ¿Qué pasa si agregas `ngram_range=(1, 2)` al TF-IDF? ¿Aparecen frases como "muy bueno" o "no recomiendo"?

---

## Ejercicio 8 — Desafío: predice tu propio comentario

```python
def predecir_sentimiento(texto, vectorizer, modelo):
    texto_limpio = preprocesar_texto(texto)
    X = vectorizer.transform([texto_limpio])
    predicción = modelo.predict(X)[0]
    probabilidades = modelo.predict_proba(X)[0]
    
    print(f"Comentario: '{texto}'")
    print(f"Sentimiento predicho: {predicción}")
    print("Probabilidades por clase:")
    for clase, prob in zip(modelo.classes_, probabilidades):
        print(f"  {clase}: {prob:.2%}")

# Prueba con tus propios comentarios
predecir_sentimiento("El paquete llegó a tiempo y el producto funciona perfecto", tfidf, modelo)
predecir_sentimiento("Me llegó completamente roto y el servicio al cliente no respondió", tfidf, modelo)
predecir_sentimiento("El producto está bien, nada especial", tfidf, modelo)
```

---

## Criterios de evaluación

- Ejercicios 1-3: comprensión del preprocesamiento y vectorización.
- Ejercicios 4-5: limpieza y preparación de datos reales.
- Ejercicio 6: pipeline completo funcionando con métricas correctas.
- Ejercicios 7-8: interpretación del modelo y experimentación propia.
