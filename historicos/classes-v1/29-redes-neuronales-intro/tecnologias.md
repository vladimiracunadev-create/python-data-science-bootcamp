# 🔧 Tecnologías complementarias — Clase 29: Introducción a Redes Neuronales

> Herramientas, librerías y recursos para ampliar lo visto en clase.

## 📦 Librerías relacionadas

| Librería | Para qué sirve | Nivel |
|---|---|---|
| `scikit-learn` (MLPClassifier) | Redes neuronales simples integradas en el ecosistema sklearn | Básico |
| `TensorFlow + Keras` | Framework principal de Google para deep learning, interfaz de alto nivel | Intermedio |
| `PyTorch` | Framework principal de Meta para investigación en deep learning | Intermedio |
| `FastAI` | API de alto nivel sobre PyTorch, facilita el entrenamiento con mejores prácticas | Intermedio |
| `Keras` | API de alto nivel que puede ejecutarse sobre TensorFlow o JAX | Básico |
| `JAX` | Framework de Google para cómputo numérico diferenciable y acelerado | Avanzado |
| `ONNX` | Formato estándar para exportar modelos entre frameworks (TF ↔ PyTorch) | Avanzado |
| `TensorBoard` | Visualización del entrenamiento: curvas de loss, grafos de red, embeddings | Intermedio |

## 🌐 Recursos recomendados

- **Keras documentación oficial**: https://keras.io/guides/ — guías paso a paso para construir redes neuronales de todo tipo.
- **TensorFlow playground**: https://playground.tensorflow.org/ — experimenta visualmente con redes neuronales en el navegador sin código.
- **Deep Learning Specialization (Coursera/Andrew Ng)**: https://www.coursera.org/specializations/deep-learning — el curso más completo y gratuito para auditar.
- **3Blue1Brown: Neural Networks**: https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi — animaciones que explican redes neuronales visualmente, excelente para principiantes.
- **Fast.ai Practical Deep Learning**: https://course.fast.ai/ — enfoque práctico, en inglés pero con subtítulos.

## 🚀 Próximos pasos

- Explorar **TensorFlow Playground** para entender visualmente cómo las capas ocultas aprenden representaciones.
- Aprender a construir una red neuronal con **Keras functional API** para arquitecturas más complejas que las secuenciales.
- Investigar **redes convolucionales (CNN)** para clasificación de imágenes: la aplicación más exitosa del deep learning.
- Explorar **redes recurrentes (LSTM, GRU)** para datos secuenciales como texto o series temporales.
- Practicar con **Transfer Learning**: reutilizar un modelo preentrenado en millones de imágenes y adaptarlo a tu problema con pocos datos.

## 🧰 Herramientas alternativas

| Herramienta | Descripción | Cuándo usarla |
|---|---|---|
| `PyTorch` | Framework flexible, preferido en investigación académica | Implementar arquitecturas personalizadas o experimentar con nuevas ideas |
| `FastAI` | Simplifica PyTorch con mejores prácticas incorporadas | Comenzar con deep learning rápidamente con resultados estado-del-arte |
| `Hugging Face` | Modelos preentrenados de NLP y visión, muy fáciles de usar | Clasificación de texto, generación, embeddings sin entrenar desde cero |
| `Google Colab` | Entorno gratuito con GPU en la nube para entrenar redes neuronales | Cuando la computadora local no tiene GPU o es lenta |
| `TensorBoard` | Visualización del entrenamiento en tiempo real | Monitorear redes neuronales grandes durante horas de entrenamiento |
