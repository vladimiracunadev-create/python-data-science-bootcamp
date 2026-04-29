# 🔧 Tecnologías complementarias — Clase 26: NLP — Texto como Datos

> Herramientas, librerías y recursos para ampliar lo visto en clase.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel |
|---|---|---|
| `scikit-learn` (TfidfVectorizer) | Vectorización TF-IDF y clasificación de texto con modelos clásicos | Básico |
| `NLTK` | Tokenización, stemming, lematización, stopwords en múltiples idiomas | Básico |
| `spaCy` | Procesamiento NLP industrial: POS tagging, NER, dependencias sintácticas | Intermedio |
| `Hugging Face Transformers` | Modelos preentrenados de última generación (BERT, RoBERTa, etc.) | Avanzado |
| `Gensim` | Word2Vec, Doc2Vec, LDA para embeddings y modelado de temas | Intermedio |
| `TextBlob` | NLP simplificado: análisis de sentimientos, traducción, corrección ortográfica | Básico |
| `fastText` | Clasificación de texto ultrarrápida de Facebook, funciona bien con poco texto | Intermedio |
| `sentence-transformers` | Embeddings semánticos de oraciones para búsqueda y similitud | Avanzado |

## 🌐 Recursos recomendados

- **Documentación de TfidfVectorizer**: https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html — todos los parámetros disponibles con ejemplos.
- **Curso NLP de Hugging Face**: https://huggingface.co/learn/nlp-course/chapter1/1 — gratuito, muy completo, en español disponible.
- **spaCy en español**: https://spacy.io/models/es — modelos preentrenados para español (`es_core_news_sm`, `es_core_news_lg`).
- **NLTK Book (gratuito)**: https://www.nltk.org/book/ — libro completo de NLP con Python, capítulos 1-3 son fundamentales.
- **Kaggle NLP competitions**: https://www.kaggle.com/competitions?search=NLP — problemas reales de clasificación de texto con soluciones comentadas.

## 🚀 Próximos pasos

- Aprender **lematización** con spaCy en español: reduce palabras a su forma base ("corriendo" → "correr").
- Explorar **Word2Vec** con Gensim para representar palabras como vectores densos que capturan significado semántico.
- Investigar **BERT en español** (BETO): modelo preentrenado que entiende el contexto completo de una oración.
- Practicar **LDA (Latent Dirichlet Allocation)** para descubrir temas latentes en una colección de documentos sin etiquetas.
- Explorar técnicas para manejar **emojis y lenguaje informal** en textos de redes sociales.

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `spaCy` | Pipeline NLP completo con modelos preentrenados en español | Cuando necesitas análisis lingüístico profundo (entidades, relaciones) |
| `Hugging Face` | Ecosistema de modelos transformers de última generación | Cuando la precisión es crítica y tienes recursos computacionales |
| `Azure Text Analytics` | API en la nube para análisis de sentimientos y NER | Proyectos empresariales sin necesidad de entrenar modelos propios |
| `Google Natural Language API` | Análisis de texto en la nube de Google, incluye español | Cuando necesitas NLP en producción rápidamente |
| `OpenAI API` | Clasificación y análisis de texto con GPT mediante prompts | Prototipado rápido o cuando los datos de entrenamiento son escasos |
