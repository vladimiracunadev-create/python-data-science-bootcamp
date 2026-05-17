# 💻 Guía de código — Clase 26: NLP — Texto como Datos

> Explicación detallada del código clave, bloque por bloque.

## Bloque 1: Preprocesamiento de texto en español

```python
import pandas as pd
import re

# Cargar datos
df = pd.read_csv("comentarios_productos.csv")
print(df.head())
print(df["sentimiento"].value_counts())

# Función de limpieza de texto
def limpiar_texto(texto):
    texto = texto.lower()                          # convertir a minúsculas
    texto = re.sub(r"[^a-záéíóúüñ\s]", "", texto) # eliminar puntuación y números
    texto = re.sub(r"\s+", " ", texto).strip()     # eliminar espacios múltiples
    return texto

# Aplicar limpieza a la columna de comentarios
df["comentario_limpio"] = df["comentario"].apply(limpiar_texto)

print("\nAntes:", df["comentario"].iloc[0])
print("Después:", df["comentario_limpio"].iloc[0])
```

**¿Qué hace este bloque?** Carga el dataset de comentarios y aplica una función de limpieza que: convierte todo a minúsculas (para que "Bueno" y "bueno" sean la misma palabra), elimina puntuación y números con expresiones regulares, y elimina espacios extra.

**¿Por qué se escribe así?** La expresión `[^a-záéíóúüñ\s]` usa una negación (`^` dentro de `[]`) para conservar solo letras del alfabeto español y espacios, descartando todo lo demás. Sin este paso, "¡¡¡Excelente!!!" y "Excelente" serían tratadas como palabras distintas por el vectorizador.

**Resultado esperado:** Una nueva columna `comentario_limpio` con texto normalizado, lista para ser vectorizada. La distribución de `sentimiento` nos muestra si las clases están balanceadas.

---

## Bloque 2: Vectorización con TF-IDF y clasificación

```python
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

# Separar datos
X = df["comentario_limpio"]
y = df["sentimiento"]

# División estratificada: mantiene la proporción de clases en train y test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Crear y entrenar el vectorizador SOLO con los datos de entrenamiento
vectorizador = TfidfVectorizer(
    max_features=1000,      # usar solo las 1000 palabras más importantes
    ngram_range=(1, 2),     # incluir palabras individuales Y bigramas
    min_df=2,               # ignorar palabras que aparecen en menos de 2 documentos
    stop_words=None         # manejaremos stopwords manualmente si es necesario
)

X_train_vec = vectorizador.fit_transform(X_train)   # aprende vocabulario y transforma
X_test_vec = vectorizador.transform(X_test)          # solo transforma (sin aprender)

# Entrenar modelo de clasificación
modelo = LogisticRegression(max_iter=1000, random_state=42)
modelo.fit(X_train_vec, y_train)

# Evaluar
y_pred = modelo.predict(X_test_vec)
print(classification_report(y_test, y_pred))
```

**¿Qué hace este bloque?** Vectoriza el texto con TF-IDF (convierte cada comentario en un vector numérico donde cada posición representa una palabra o bigrama), entrena una regresión logística y evalúa con `classification_report` que muestra precisión, recall y F1 por clase.

**¿Por qué se escribe así?** Es crítico usar `.fit_transform()` solo en datos de entrenamiento y `.transform()` en test. Si usamos `.fit_transform()` en todo el dataset, el vectorizador "aprende" del vocabulario del test, causando data leakage. `stratify=y` asegura que cada clase esté representada proporcionalmente en train y test.

**Resultado esperado:** Un reporte de clasificación con métricas por clase. Es normal que "Neutro" tenga peor F1 que "Positivo" y "Negativo" porque su señal textual es más débil (los neutros suelen mezclar palabras positivas y negativas).

---

## Bloque 3: Importancia de palabras por clase

```python
import numpy as np
import matplotlib.pyplot as plt

# Obtener nombres de las características (palabras y bigramas)
palabras = vectorizador.get_feature_names_out()

# Los coeficientes del modelo indican la importancia de cada palabra por clase
clases = modelo.classes_

fig, axes = plt.subplots(1, len(clases), figsize=(15, 5))

for i, clase in enumerate(clases):
    coeficientes = modelo.coef_[i]
    
    # Top 10 palabras que más contribuyen a esta clase (positivo = hacia esta clase)
    top_indices = np.argsort(coeficientes)[-10:][::-1]
    top_palabras = palabras[top_indices]
    top_coefs = coeficientes[top_indices]
    
    axes[i].barh(top_palabras, top_coefs, color="steelblue")
    axes[i].set_title(f"Clase: {clase}")
    axes[i].set_xlabel("Coeficiente (importancia)")

plt.suptitle("Palabras más importantes por clase")
plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?** Extrae los coeficientes de la regresión logística para cada clase. Un coeficiente alto para una palabra en una clase significa que esa palabra es una señal fuerte hacia esa clase. Visualiza las top 10 palabras más discriminativas para cada sentimiento.

**¿Por qué se escribe así?** `modelo.coef_` tiene forma `(n_clases, n_features)`, donde cada fila corresponde a una clase. `np.argsort()` ordena los índices de menor a mayor, por eso tomamos los últimos 10 (`[-10:]`) y los invertimos (`[::-1]`) para tener los mayores primero. `get_feature_names_out()` traduce los índices numéricos de vuelta a palabras legibles.

**Resultado esperado:** Tres gráficos de barras horizontales. Para "Positivo" esperamos ver palabras como "excelente", "recomiendo", "perfecto". Para "Negativo" palabras como "pésimo", "devolver", "decepcionante". Esto permite interpretar y confiar en el modelo.

---

## Bloque 4: Predecir nuevos comentarios

```python
# Función para predecir el sentimiento de texto nuevo
def predecir_sentimiento(comentario_nuevo):
    # Aplicar la misma limpieza que usamos en entrenamiento
    comentario_limpio = limpiar_texto(comentario_nuevo)
    
    # Vectorizar usando el vectorizador ya entrenado (solo transform, no fit)
    comentario_vec = vectorizador.transform([comentario_limpio])
    
    # Predecir clase y probabilidades
    clase = modelo.predict(comentario_vec)[0]
    probabilidades = modelo.predict_proba(comentario_vec)[0]
    
    print(f"Comentario: '{comentario_nuevo}'")
    print(f"Sentimiento predicho: {clase}")
    for c, p in zip(modelo.classes_, probabilidades):
        print(f"  {c}: {p:.1%}")
    print()

# Probar con ejemplos nuevos
predecir_sentimiento("El producto llegó rápido y funciona perfecto, muy recomendado")
predecir_sentimiento("Una porquería, se rompió al segundo día de uso")
predecir_sentimiento("El producto es normal, ni bueno ni malo")
```

**¿Qué hace este bloque?** Define una función reutilizable que aplica el pipeline completo a texto nuevo: limpieza → vectorización → predicción. También muestra las probabilidades de cada clase, lo que permite saber cuán seguro está el modelo.

**¿Por qué se escribe así?** Es importante encapsular todo el proceso en una función para facilitar la reutilización. Pasar el comentario como lista `[comentario_limpio]` es necesario porque el vectorizador espera un iterable. `.predict_proba()` requiere que el modelo tenga `probability=True` o que sea un modelo que lo soporta por defecto como LogisticRegression.

**Resultado esperado:** Para el primer comentario, probabilidad alta de "Positivo". Para el segundo, "Negativo". El tercero es más incierto y mostrará probabilidades más distribuidas entre las clases, ilustrando la dificultad de clasificar textos neutros.

---

## Errores comunes y cómo resolverlos

| Error | Causa | Solución |
|---|---|---|
| `NotFittedError` al transformar | Se llamó `.transform()` sin hacer `.fit()` antes | Llamar `.fit_transform()` en train, luego `.transform()` en test |
| Accuracy muy baja en todas las clases | El texto no fue limpiado y tiene mucho ruido | Aplicar la función de limpieza antes de vectorizar |
| `UnicodeDecodeError` al leer el CSV | El archivo tiene tildes y el encoding no es UTF-8 | Usar `pd.read_csv("archivo.csv", encoding="latin-1")` |
| El modelo siempre predice la misma clase | Las clases están muy desbalanceadas | Usar `class_weight='balanced'` en `LogisticRegression` |
| `ValueError: empty vocabulary` | Todos los textos quedaron vacíos después de la limpieza | Revisar la función de limpieza, puede estar eliminando demasiado |
| El `classification_report` muestra 0.0 en alguna clase | El modelo nunca predice esa clase | Dataset desbalanceado o clase con muy pocos ejemplos en test |
