# Parte 2 — Deep Learning — Keras, TensorFlow, Transformers, RL y Despliegue

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-1-machine-learning-clasico/README.md) · [⏭️ Parte siguiente](../parte-3-estadistica-inferencial/README.md)

**56 clases** · ~13–14 semanas

**Fuente principal:** **Géron** ([*Hands-On ML*, 3ª ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)) — capítulos 10–19, con incorporación de LLMs modernos, RAG y modelos de difusión.

---

## 🎯 ¿De qué trata esta parte?

La parte **más extensa** del programa. Cubre Deep Learning desde el perceptrón hasta los modelos generativos modernos (Transformers, LLMs, difusión) y reinforcement learning. El énfasis está en **entender qué hace cada bloque** (no solo en copiar `model.fit`): por qué BatchNorm acelera la convergencia, qué hace Adam que no hace SGD, cuándo conviene una CNN vs una ViT, por qué un Transformer dejó obsoletas a las RNN para secuencias largas.

Está organizada en bloques: **fundamentos** (MLPs, optimización, regularización), **ingeniería con TensorFlow/Keras** (custom layers, tf.data, TFRecord), **visión por computadora** (CNNs y arquitecturas modernas), **secuencias** (RNN, LSTM, atención, Transformers, LLMs, RAG), **generativos** (autoencoders, VAE, GAN, difusión), **reinforcement learning** y **despliegue a producción** (TF Serving, Vertex AI, TF Lite, TensorFlow.js, multi-GPU).

## 🧩 Problemas que resuelve

- Entrenar una red neuronal desde cero (MLP) y explicar la matemática del backpropagation.
- Diagnosticar y resolver vanishing/exploding gradients con inicialización, BatchNorm y activaciones modernas.
- Hacer transfer learning con CNNs preentrenadas para visión o con LLMs para texto.
- Construir un pipeline de datos eficiente con tf.data + TFRecord para entrenar sobre datasets que no caben en RAM.
- Implementar arquitecturas modernas: ResNet, EfficientNet, ViT, BERT, GPT, modelos de difusión.
- Usar Hugging Face Transformers para tareas reales (clasificación, NER, generación, embeddings).
- Construir un sistema RAG básico sobre documentos propios.
- Desplegar un modelo entrenado a producción (TF Serving + gRPC, Vertex AI, TF Lite móvil, navegador con TF.js).

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Entrenar y serializar un modelo de visión que supere baseline en un dataset propio.
- Hacer fine-tuning de un Transformer pequeño para clasificación o generación.
- Construir un mini-RAG con embeddings + retriever + LLM sobre un corpus de ~1000 documentos.
- Servir un modelo entrenado vía API en una GPU y medir su latencia.
- Explicar el tradeoff entrenamiento/serving para CNN vs ViT vs LLM para un caso concreto.

## 🗺️ Estructura temática

- **Fundamentos de redes neuronales** — clases 090–095 — perceptrón, MLP, backprop, Keras (Sequential, Functional, Subclassing), Keras Tuner.
- **Entrenamiento de redes profundas** — clases 096–104 — gradientes, inicialización, activaciones, normalización, optimizadores, schedules, regularización.
- **TensorFlow avanzado** — clases 105–112 — tensores, custom layers/loops, autograph, tf.data, TFRecord, preprocessing layers, TFDS.
- **Visión por computadora** — clases 113–117 — convoluciones, pooling, arquitecturas CNN modernas, transfer learning, detección/segmentación.
- **Secuencias y NLP** — clases 118–129 — RNN, LSTM, GRU, 1D CNN, char-RNN, sentimiento, encoder-decoder, atención, Transformers, BERT/GPT, Hugging Face, LLMs, RAG.
- **Modelos generativos** — clases 130–133 — autoencoders, VAE, GAN, difusión.
- **Reinforcement Learning** — clases 134–138 — Gymnasium, policy gradients, MDPs, Q-learning, DQN, PPO/SAC.
- **Despliegue y escala** — clases 139–145 — TF Serving, Vertex AI, TF Lite, TensorFlow.js, GPU, tf.distribute, entrenamiento a escala.

## 📚 Índice de clases (56)

- [090 — Perceptrón, MLP y backpropagation](090-perceptron-mlp-y-backpropagation/README.md)
- [091 — Regresión y clasificación con MLP](091-regresion-y-clasificacion-con-mlp/README.md)
- [092 — Keras Sequential API](092-keras-sequential-api/README.md)
- [093 — Keras Functional API y Subclassing](093-keras-functional-api-y-subclassing/README.md)
- [094 — Callbacks, TensorBoard, guardar/restaurar modelos](094-callbacks-tensorboard-guardar-restaurar-modelos/README.md)
- [095 — Keras Tuner](095-keras-tuner/README.md)
- [096 — Vanishing/exploding gradients](096-vanishing-exploding-gradients/README.md)
- [097 — Inicialización (Glorot, He)](097-inicializacion-glorot-he/README.md)
- [098 — Activaciones: ReLU, ELU, GELU, Swish, Mish](098-activaciones-relu-elu-gelu-swish-mish/README.md)
- [099 — Batch Normalization, Layer Normalization](099-batch-normalization-layer-normalization/README.md)
- [100 — Gradient clipping](100-gradient-clipping/README.md)
- [101 — Transfer learning, unsupervised pretraining](101-transfer-learning-unsupervised-pretraining/README.md)
- [102 — Optimizadores: Momentum, Nesterov, AdaGrad, RMSProp, Adam, AdamW](102-optimizadores-momentum-nesterov-adagrad-rmsprop-adam-adamw/README.md)
- [103 — Learning rate scheduling](103-learning-rate-scheduling/README.md)
- [104 — Regularización: L1/L2, dropout, max-norm, MC dropout](104-regularizacion-l1-l2-dropout-max-norm-mc-dropout/README.md)
- [105 — TensorFlow: tensores, variables, operaciones](105-tensorflow-tensores-variables-operaciones/README.md)
- [106 — Losses, métricas, capas, modelos custom](106-losses-metricas-capas-modelos-custom/README.md)
- [107 — Funciones y grafos (autograph)](107-funciones-y-grafos-autograph/README.md)
- [108 — Custom training loops](108-custom-training-loops/README.md)
- [109 — tf.data API](109-tf-data-api/README.md)
- [110 — TFRecord](110-tfrecord/README.md)
- [111 — Keras preprocessing layers](111-keras-preprocessing-layers/README.md)
- [112 — TensorFlow Datasets (TFDS)](112-tensorflow-datasets-tfds/README.md)
- [113 — Capas convolucionales, filtros, feature maps](113-capas-convolucionales-filtros-feature-maps/README.md)
- [114 — Pooling](114-pooling/README.md)
- [115 — Arquitecturas CNN: LeNet, AlexNet, VGG, GoogLeNet, ResNet, Xception, SENet, EfficientNet](115-arquitecturas-cnn-lenet-alexnet-vgg-googlenet-resnet-xception-senet-ef/README.md)
- [116 — Transfer learning con CNNs preentrenadas](116-transfer-learning-con-cnns-preentrenadas/README.md)
- [117 — Localización, detección (YOLO, Faster R-CNN), segmentación semántica](117-localizacion-deteccion-yolo-faster-r-cnn-segmentacion-semantica/README.md)
- [118 — RNNs: neuronas recurrentes, BPTT](118-rnns-neuronas-recurrentes-bptt/README.md)
- [119 — Forecasting de series con RNN](119-forecasting-de-series-con-rnn/README.md)
- [120 — LSTM, GRU](120-lstm-gru/README.md)
- [121 — 1D CNNs y WaveNet](121-1d-cnns-y-wavenet/README.md)
- [122 — Generación de texto char-RNN](122-generacion-de-texto-char-rnn/README.md)
- [123 — Análisis de sentimiento](123-analisis-de-sentimiento/README.md)
- [124 — Encoder-Decoder para traducción](124-encoder-decoder-para-traduccion/README.md)
- [125 — Mecanismos de atención](125-mecanismos-de-atencion/README.md)
- [126 — Transformers: arquitectura, BERT, GPT](126-transformers-arquitectura-bert-gpt/README.md)
- [127 — Hugging Face Transformers (uso práctico)](127-hugging-face-transformers-uso-practico/README.md)
- [128 — LLMs aplicados: fine-tuning, prompting](128-llms-aplicados-fine-tuning-prompting/README.md)
- [129 — RAG básico y embeddings](129-rag-basico-y-embeddings/README.md)
- [130 — Autoencoders: undercomplete, stacked, denoising, sparse](130-autoencoders-undercomplete-stacked-denoising-sparse/README.md)
- [131 — Variational Autoencoders (VAE)](131-variational-autoencoders-vae/README.md)
- [132 — GANs: DCGAN, Progressive GAN, StyleGAN](132-gans-dcgan-progressive-gan-stylegan/README.md)
- [133 — Modelos de difusión (DDPM, score-based)](133-modelos-de-difusion-ddpm-score-based/README.md)
- [134 — RL: aprendizaje por recompensa, OpenAI Gymnasium](134-rl-aprendizaje-por-recompensa-openai-gymnasium/README.md)
- [135 — Policy gradients](135-policy-gradients/README.md)
- [136 — Markov Decision Processes](136-markov-decision-processes/README.md)
- [137 — TD Learning, Q-Learning, Deep Q-Networks](137-td-learning-q-learning-deep-q-networks/README.md)
- [138 — RL moderno: A3C, PPO, SAC (vista general)](138-rl-moderno-a3c-ppo-sac-vista-general/README.md)
- [139 — TF Serving + gRPC](139-tf-serving-grpc/README.md)
- [140 — Despliegue en Vertex AI](140-despliegue-en-vertex-ai/README.md)
- [141 — TF Lite (mobile/embedded)](141-tf-lite-mobile-embedded/README.md)
- [142 — TensorFlow.js (navegador)](142-tensorflow-js-navegador/README.md)
- [143 — Aceleración con GPU](143-aceleracion-con-gpu/README.md)
- [144 — Entrenamiento multi-dispositivo, tf.distribute](144-entrenamiento-multi-dispositivo-tf-distribute/README.md)
- [145 — Entrenamiento a escala con Vertex AI](145-entrenamiento-a-escala-con-vertex-ai/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-1-machine-learning-clasico/README.md) · [⏭️ Parte siguiente](../parte-3-estadistica-inferencial/README.md)
