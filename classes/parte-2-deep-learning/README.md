# Parte 2 — Deep Learning — Keras, TensorFlow, Transformers, RL y Despliegue

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-1-machine-learning-clasico/README.md) · [⏭️ Parte siguiente](../parte-3-estadistica-inferencial/README.md)

**75 clases** · ~17–19 semanas · ✅ Contenido completo (expansión 2026: PyTorch dedicado, Lion/Sophia, Stochastic Depth, SAM/YOLOv11, CLIP/Whisper, LoRA/DPO/vLLM, MCP, agentes, eval, SDXL, ONNX, JAX, Flash Attention)

**Fuente principal:** **Géron** ([*Hands-On ML*, 3ª ed.](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)) — capítulos 10–19. Complementado con **Howard & Gugger** (*Deep Learning for Coders with fastai & PyTorch*), **Prince** (*Understanding Deep Learning*, 2024), papers seminales de Transformers/LLMs y documentación oficial de PyTorch, Hugging Face, JAX y ONNX.

Cada clase tiene su `README.md` con objetivo, resultados de aprendizaje verificables, dataset recomendado, 5 ejercicios y homework con criterio de aceptación. Todas las 75 clases incluyen las tres secciones del patrón pedagógico v2.2.0:

- **📖 Definiciones y características** — términos técnicos con explicación y características clave.
- **⚠️ Errores comunes** — tabla de síntomas/mensajes con causa y solución concretas (CUDA OOM, NaN loss, gradient explosion, etc.).
- **❓ Preguntas frecuentes** — FAQs auténticas que aparecen al estudiar cada tema.

**📌 Cobertura moderna (audit 2026) — 19 clases dedicadas:**

Todos los temas modernos ahora son clases independientes con patrón completo + ejercicios + homework:

- Clase **106** → Ray Tune: HPO distribuido y a escala (ASHA, PBT).
- Clase **114** → Optimizadores modernos: Lion, Sophia, Schedule-Free.
- Clase **117** → Regularización moderna: Stochastic Depth, DropPath, LayerDrop.
- Clase **122** / **123** → PyTorch fundamentos + PyTorch Lightning.
- Clase **133** → Segment Anything (SAM / SAM 2).
- Clase **134** → YOLOv11 práctico (detección, segmentación, pose, tracking).
- Clase **144** → Flash Attention v2/v3, RoPE, GQA (motor de LLMs modernos).
- Clase **146** → CLIP / SigLIP: multimodal embeddings.
- Clase **147** → Whisper: ASR, transcripción, traducción de audio.
- Clase **149** → LoRA / QLoRA: fine-tuning eficiente de LLMs.
- Clase **150** → DPO y RLHF: alineamiento de LLMs.
- Clase **151** → vLLM y TGI: serving de LLMs en producción.
- Clase **153** → MCP (Model Context Protocol).
- Clase **154** → Agentes: tool use, ReAct, multi-agent.
- Clase **155** → LLM Evaluation: MMLU, MT-Bench, LLM-as-judge.
- Clase **160** → Stable Diffusion XL + ControlNet en profundidad.
- Clase **167** → ONNX y ONNX Runtime: portabilidad e inference optimizada.
- Clase **173** → JAX y Flax: stack moderno de Google.

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

- **Fundamentos de redes neuronales** — clases 100–106 — perceptrón, MLP, backprop, Keras (Sequential, Functional, Subclassing), Keras Tuner.
- **Entrenamiento de redes profundas** — clases 107–117 — gradientes, inicialización, activaciones, normalización, optimizadores, schedules, regularización.
- **TensorFlow avanzado** — clases 118–127 — tensores, custom layers/loops, autograph, tf.data, TFRecord, preprocessing layers, TFDS.
- **Visión por computadora** — clases 128–134 — convoluciones, pooling, arquitecturas CNN modernas, transfer learning, detección/segmentación.
- **Secuencias y NLP** — clases 135–155 — RNN, LSTM, GRU, 1D CNN, char-RNN, sentimiento, encoder-decoder, atención, Transformers, BERT/GPT, Hugging Face, LLMs, RAG.
- **Modelos generativos** — clases 156–160 — autoencoders, VAE, GAN, difusión.
- **Reinforcement Learning** — clases 161–165 — Gymnasium, policy gradients, MDPs, Q-learning, DQN, PPO/SAC.
- **Despliegue y escala** — clases 166–174 — TF Serving, Vertex AI, TF Lite, TensorFlow.js, GPU, tf.distribute, entrenamiento a escala.

## 📚 Índice de clases (75)

- [100 — Perceptrón, MLP y backpropagation](100-perceptron-mlp-y-backpropagation/README.md)
- [101 — Regresión y clasificación con MLP](101-regresion-y-clasificacion-con-mlp/README.md)
- [102 — Keras Sequential API](102-keras-sequential-api/README.md)
- [103 — Keras Functional API y Subclassing](103-keras-functional-api-y-subclassing/README.md)
- [104 — Callbacks, TensorBoard, guardar/restaurar modelos](104-callbacks-tensorboard-guardar-restaurar-modelos/README.md)
- [105 — Keras Tuner (+ Optuna, Ray Tune)](105-keras-tuner/README.md)
- [106 — Ray Tune: HPO distribuido y a escala](106-ray-tune-hpo-distribuido/README.md)
- [107 — Vanishing/exploding gradients](107-vanishing-exploding-gradients/README.md)
- [108 — Inicialización (Glorot, He)](108-inicializacion-glorot-he/README.md)
- [109 — Activaciones: ReLU, ELU, GELU, Swish, Mish](109-activaciones-relu-elu-gelu-swish-mish/README.md)
- [110 — Batch Normalization, Layer Normalization](110-batch-normalization-layer-normalization/README.md)
- [111 — Gradient clipping](111-gradient-clipping/README.md)
- [112 — Transfer learning, unsupervised pretraining](112-transfer-learning-unsupervised-pretraining/README.md)
- [113 — Optimizadores: Momentum, Nesterov, AdaGrad, RMSProp, Adam, AdamW (+ Lion, Sophia)](113-optimizadores-momentum-nesterov-adagrad-rmsprop-adam-adamw/README.md)
- [114 — Optimizadores modernos: Lion, Sophia, Schedule-Free](114-optimizadores-modernos-lion-sophia/README.md)
- [115 — Learning rate scheduling](115-learning-rate-scheduling/README.md)
- [116 — Regularización: L1/L2, dropout, max-norm, MC dropout (+ Stochastic Depth, DropPath)](116-regularizacion-l1-l2-dropout-max-norm-mc-dropout/README.md)
- [117 — Regularización moderna: Stochastic Depth, DropPath, LayerDrop](117-stochastic-depth-droppath-layerdrop/README.md)
- [118 — TensorFlow: tensores, variables, operaciones](118-tensorflow-tensores-variables-operaciones/README.md)
- [119 — Losses, métricas, capas, modelos custom](119-losses-metricas-capas-modelos-custom/README.md)
- [120 — Funciones y grafos (autograph)](120-funciones-y-grafos-autograph/README.md)
- [121 — Custom training loops (+ PyTorch & PyTorch Lightning)](121-custom-training-loops/README.md)
- [122 — PyTorch fundamentos: tensores, autograd, nn.Module](122-pytorch-fundamentos-tensores-autograd/README.md)
- [123 — PyTorch Lightning: Trainer, callbacks, distributed](123-pytorch-lightning-trainer-distribuido/README.md)
- [124 — tf.data API](124-tf-data-api/README.md)
- [125 — TFRecord](125-tfrecord/README.md)
- [126 — Keras preprocessing layers](126-keras-preprocessing-layers/README.md)
- [127 — TensorFlow Datasets (TFDS)](127-tensorflow-datasets-tfds/README.md)
- [128 — Capas convolucionales, filtros, feature maps](128-capas-convolucionales-filtros-feature-maps/README.md)
- [129 — Pooling](129-pooling/README.md)
- [130 — Arquitecturas CNN: LeNet, AlexNet, VGG, GoogLeNet, ResNet, Xception, SENet, EfficientNet, ConvNeXt](130-arquitecturas-cnn-lenet-alexnet-vgg-googlenet-resnet-xception-senet-ef/README.md)
- [131 — Transfer learning con CNNs preentrenadas](131-transfer-learning-con-cnns-preentrenadas/README.md)
- [132 — Localización, detección, segmentación (+ DETR, Segment Anything, YOLOv11)](132-localizacion-deteccion-yolo-faster-r-cnn-segmentacion-semantica/README.md)
- [133 — Segment Anything (SAM / SAM 2): foundation model para segmentación](133-segment-anything-sam-sam2/README.md)
- [134 — YOLOv11 práctico: detección, segmentación, pose, tracking](134-yolov11-deteccion-segmentacion-practica/README.md)
- [135 — RNNs: neuronas recurrentes, BPTT](135-rnns-neuronas-recurrentes-bptt/README.md)
- [136 — Forecasting de series con RNN](136-forecasting-de-series-con-rnn/README.md)
- [137 — LSTM, GRU](137-lstm-gru/README.md)
- [138 — 1D CNNs y WaveNet](138-1d-cnns-y-wavenet/README.md)
- [139 — Generación de texto char-RNN](139-generacion-de-texto-char-rnn/README.md)
- [140 — Análisis de sentimiento](140-analisis-de-sentimiento/README.md)
- [141 — Encoder-Decoder para traducción](141-encoder-decoder-para-traduccion/README.md)
- [142 — Mecanismos de atención](142-mecanismos-de-atencion/README.md)
- [143 — Transformers: arquitectura, BERT, GPT (+ Flash Attention, RoPE, GQA)](143-transformers-arquitectura-bert-gpt/README.md)
- [144 — Flash Attention v2/v3, RoPE, GQA: el motor de los LLMs modernos](144-flash-attention-rope-gqa-llm-engines/README.md)
- [145 — Hugging Face Transformers (uso práctico)](145-hugging-face-transformers-uso-practico/README.md)
- [146 — CLIP, SigLIP: multimodal embeddings (visión + texto)](146-clip-siglip-multimodal-embeddings/README.md)
- [147 — Whisper: ASR, transcripción, traducción de audio](147-whisper-asr-audio-transcripcion-traduccion/README.md)
- [148 — LLMs aplicados: fine-tuning, prompting (+ LoRA / QLoRA, DPO, vLLM)](148-llms-aplicados-fine-tuning-prompting/README.md)
- [149 — LoRA / QLoRA: fine-tuning eficiente de LLMs](149-lora-qlora-fine-tuning-eficiente/README.md)
- [150 — DPO y RLHF: alineamiento de LLMs](150-dpo-rlhf-alineamiento-de-llms/README.md)
- [151 — vLLM y TGI: serving de LLMs en producción](151-vllm-tgi-serving-llm-produccion/README.md)
- [152 — RAG básico y embeddings (+ hybrid search, re-ranking, MCP)](152-rag-basico-y-embeddings/README.md)
- [153 — MCP (Model Context Protocol): herramientas y datos para LLMs](153-mcp-model-context-protocol/README.md)
- [154 — Agentes: tool use, ReAct, multi-agent](154-agentes-tool-use-react-multi-agent/README.md)
- [155 — LLM Evaluation: MMLU, MT-Bench, LLM-as-judge, evals propios](155-llm-evaluation-mmlu-mtbench-llm-as-judge/README.md)
- [156 — Autoencoders: undercomplete, stacked, denoising, sparse](156-autoencoders-undercomplete-stacked-denoising-sparse/README.md)
- [157 — Variational Autoencoders (VAE)](157-variational-autoencoders-vae/README.md)
- [158 — GANs: DCGAN, Progressive GAN, StyleGAN](158-gans-dcgan-progressive-gan-stylegan/README.md)
- [159 — Modelos de difusión (+ Stable Diffusion XL, ControlNet, LCM)](159-modelos-de-difusion-ddpm-score-based/README.md)
- [160 — Stable Diffusion XL + ControlNet en profundidad](160-stable-diffusion-xl-controlnet/README.md)
- [161 — RL: aprendizaje por recompensa, Gymnasium (Farama)](161-rl-aprendizaje-por-recompensa-openai-gymnasium/README.md)
- [162 — Policy gradients](162-policy-gradients/README.md)
- [163 — Markov Decision Processes](163-markov-decision-processes/README.md)
- [164 — TD Learning, Q-Learning, Deep Q-Networks](164-td-learning-q-learning-deep-q-networks/README.md)
- [165 — RL moderno: A3C, PPO, SAC (vista general)](165-rl-moderno-a3c-ppo-sac-vista-general/README.md)
- [166 — TF Serving + gRPC (+ ONNX, TensorRT, vLLM/TGI)](166-tf-serving-grpc/README.md)
- [167 — ONNX y ONNX Runtime: portabilidad e inference optimizada](167-onnx-onnx-runtime-portabilidad/README.md)
- [168 — Despliegue en Vertex AI](168-despliegue-en-vertex-ai/README.md)
- [169 — TF Lite (mobile/embedded)](169-tf-lite-mobile-embedded/README.md)
- [170 — TensorFlow.js (navegador)](170-tensorflow-js-navegador/README.md)
- [171 — Aceleración con GPU](171-aceleracion-con-gpu/README.md)
- [172 — Entrenamiento multi-dispositivo, tf.distribute](172-entrenamiento-multi-dispositivo-tf-distribute/README.md)
- [173 — JAX y Flax: el stack moderno de Google para DL](173-jax-flax-fundamentos/README.md)
- [174 — Entrenamiento a escala con Vertex AI](174-entrenamiento-a-escala-con-vertex-ai/README.md)

## 📥 Material descargable — parte completa

Materiales consolidados con TODAS las clases de esta parte (útiles para revisar offline o imprimir el bloque entero):

- 📄 [Guía PDF — parte completa](../../docs/pdfs/parts/parte-2-deep-learning-completa.pdf) — todas las clases concatenadas con headings demoteados.
- 🎞️ [Presentación PPTX — parte completa](../../docs/presentaciones/parts/parte-2-deep-learning-completa.pptx) — portada + TOC + slides de cada clase.

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-1-machine-learning-clasico/README.md) · [⏭️ Parte siguiente](../parte-3-estadistica-inferencial/README.md)
