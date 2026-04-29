# ❓ Preguntas — Clase 29: Introducción a Redes Neuronales

> Preguntas de comprensión, discusión y evaluación para esta clase.

## 🧠 Preguntas de comprensión

1. ¿Qué es una **neurona artificial**? ¿Qué analogía tiene con las neuronas biológicas del cerebro humano?
2. ¿Cuál es la diferencia entre las funciones de activación **sigmoid** y **ReLU**? ¿Por qué ReLU suele preferirse en capas ocultas de redes profundas?
3. ¿Qué son las **capas** de una red neuronal? ¿Qué diferencia hay entre la capa de entrada, las capas ocultas y la capa de salida?
4. ¿Por qué es obligatorio aplicar `StandardScaler` antes de entrenar un `MLPClassifier`? ¿Qué pasa si no escalamos los datos?
5. ¿Qué es la **función de pérdida** (loss function) en una red neuronal? ¿Qué mide y por qué queremos minimizarla?
6. ¿Qué información muestra la **curva de pérdida** (loss curve) durante el entrenamiento de una red neuronal?
7. ¿Qué son Keras y TensorFlow? ¿Cuál es la relación entre estas dos tecnologías?

## 💬 Preguntas de discusión

1. Un árbol de decisión de 5 niveles tardó 2 segundos en entrenarse y obtuvo 88% de accuracy. Una red neuronal de 3 capas tardó 15 minutos y obtuvo 89%. ¿Cuál elegirías para producción y por qué?
2. ¿Por qué las redes neuronales son difíciles de interpretar (son "cajas negras")? ¿En qué contextos es este un problema crítico?
3. Discute la analogía entre cómo aprende una red neuronal y cómo aprende un humano a reconocer figuras. ¿En qué se parecen y en qué se diferencian?
4. Si la curva de pérdida en entrenamiento sigue bajando pero la de validación empieza a subir, ¿qué está pasando? ¿Cómo lo resolverías?
5. ¿Crees que las redes neuronales reemplazarán a modelos más simples como la regresión logística o los árboles de decisión en todas las aplicaciones? Argumenta tu posición.
6. ¿Qué aplicaciones cotidianas que usas todos los días probablemente usan redes neuronales? Menciona al menos cinco.

## 🧪 Preguntas de código

1. Escribe el código para crear un `MLPClassifier` con dos capas ocultas de 100 y 50 neuronas respectivamente, función de activación ReLU, y un máximo de 500 iteraciones.
2. ¿Por qué hay que escalar los datos antes de entrenar el MLP? Escribe el código para hacerlo correctamente, evitando data leakage en train/test.
3. ¿Cómo graficarías la curva de pérdida de un `MLPClassifier` ya entrenado usando `loss_curve_`? Escribe el código.
4. Escribe el código para comparar el rendimiento de `MLPClassifier` vs `RandomForestClassifier` en el mismo dataset de estudiantes, usando las mismas métricas.
5. ¿Cómo instalarías TensorFlow y crearías una red neuronal básica equivalente al `MLPClassifier` de sklearn usando Keras? Escribe el código esqueleto.
6. ¿Qué significa el atributo `n_iter_` de un `MLPClassifier`? ¿Cuándo termina el entrenamiento si `max_iter` no se alcanza?

## 🎯 Pregunta integradora

Eres data scientist en una empresa y debes elegir entre tres modelos para predecir si un estudiante aprobará: un árbol de decisión, un Random Forest y una red neuronal MLP. El dataset tiene 500 filas y 15 variables. Describe el proceso de comparación que seguirías: preprocesamiento para cada modelo, métricas de evaluación, criterios de selección, y cómo comunicarías la decisión final al equipo directivo (que no sabe de machine learning). ¿En qué escenario elegiría cada uno de los tres modelos? Incluye consideraciones de tiempo de entrenamiento, interpretabilidad, mantenimiento y rendimiento.
