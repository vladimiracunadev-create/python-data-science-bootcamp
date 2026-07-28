# Clase 167 — ONNX y ONNX Runtime: portabilidad e inference optimizada

> Parte: **2 — Deep Learning** · Fuente: [ONNX docs](https://onnx.ai/) + ONNX Runtime team blogs. ⏱️ Duración estimada: **80 min**.
>
> 🎚️ **Nivel:** Avanzado

## 🎯 Objetivo

Dominar **ONNX** (formato intermedio) y **ONNX Runtime** (runtime cross-platform) — la solución portable para inference: entrenás en TF/PyTorch/JAX, exportás a ONNX, corrés en cualquier hardware (CPU, GPU NVIDIA, GPU AMD, mobile, browser, edge). Conocer **TensorRT** (NVIDIA-specific, mayor performance).

## 📚 Resultados de aprendizaje

Al finalizar, el estudiante podrá:

- Exportar modelos: `torch.onnx.export`, `tf2onnx.convert`.
- Cargar e inferir con `onnxruntime.InferenceSession`.
- Elegir **execution provider**: CPU, CUDA, TensorRT, OpenVINO, DirectML, CoreML.
- Optimizar modelos: graph optimization, quantization int8/fp16.
- Reconocer cuándo ONNX vs TF Serving vs vLLM (LLMs).

## 🗺️ Temas

- ONNX como protocolo (protobuf): operator set + tensor types.
- Conversión: cada framework tiene su exporter.
- Verificación: outputs deben coincidir framework ↔ ONNX (±1e-5).
- Optimization: graph simplification, layer fusion.
- Quantization: dynamic, static (con calibration), QAT.
- Execution providers: priority order.

## 📖 Definiciones y características

- **ONNX**: formato; archivo `.onnx`.
- **Opset version**: versión del set de ops. Higher = newer ops (ej. opset 17 incluye attention).
- **InferenceSession**: objeto runtime que carga modelo y ejecuta.
- **Execution Provider (EP)**: backend de hardware. ORT elige el primero disponible.
- **`onnxruntime-gpu`**: pip package específico para CUDA.
- **`onnxruntime-directml`**: Windows GPU (AMD/Intel via DirectX).

## 📂 Dataset / recursos

- Modelo de clases anteriores (Fashion-MNIST o ResNet preentrenado).
- Librerías: `onnx`, `onnxruntime` o `onnxruntime-gpu`, `tf2onnx` (TF), `torch.onnx` built-in.

## 🧪 Ejercicios

1. **PyTorch → ONNX**: `torch.onnx.export(model, dummy_input, 'model.onnx', opset_version=17, input_names=['input'], output_names=['output'])`.
2. **TF → ONNX**: `python -m tf2onnx.convert --saved-model dir/ --output model.onnx --opset 17`.
3. **Inference**: `sess = ort.InferenceSession('model.onnx', providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])`. Verificar outputs.
4. **Graph optimization**: `sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL`.
5. **Quantization**: `onnxruntime.quantization.quantize_dynamic('model.onnx', 'model_q.onnx', weight_type=QuantType.QUInt8)`.

## 📝 Homework verificable

Exportar y deployar un modelo CNN ya entrenado:

1. PyTorch ResNet50 preentrenado → ONNX.
2. Quantization dynamic.
3. Comparar latencia + accuracy: PyTorch CUDA vs ORT CUDA vs ORT CPU vs ORT CPU quantized.
4. Verificar correctness (output diff < 1e-4 vs PyTorch).

**Criterio de aceptación**: ORT CUDA ≥ PyTorch CUDA en velocidad; quantization reduce tamaño 4× con < 1 pp accuracy loss.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| `opset version X not supported` | EP version vieja. **Fix**: actualizar onnxruntime. |
| Output diff vs framework grande | Conversión incompleta (custom ops). **Fix**: `verbose=True` en export, identificar op problemática. |
| CUDA provider no disponible | Falta `onnxruntime-gpu` install. **Fix**: `pip install onnxruntime-gpu`. |
| Dynamic axes mal | Mal export. **Fix**: `dynamic_axes={'input': {0: 'batch'}}`. |
| Quantization rompe accuracy | Modelo sensible. **Fix**: usar static quantization con calibration set. |

## ❓ Preguntas frecuentes

**❓ ONNX vs TensorRT?**

ONNX Runtime + TensorRT EP combina ambos: ORT como interfaz, TensorRT como backend para GPUs NVIDIA. Best of both.

**❓ ONNX en mobile?**

ONNX Runtime Mobile: optimizado para Android/iOS. Soporta CoreML, NNAPI delegates.

**❓ ONNX en browser?**

ONNX.js — corre en WebGL/WebGPU/WASM.

**❓ LLMs con ONNX?**

Posible (especialmente con `onnxruntime-genai`). vLLM/TGI siguen siendo mejores para LLMs grandes.

**❓ Triton vs ORT?**

Triton (NVIDIA) puede servir modelos ONNX como uno de sus backends. Triton para infra multi-modelo; ORT solo para inference.

## 🔗 Referencias

- [ONNX](https://onnx.ai/).
- [ONNX Runtime](https://onnxruntime.ai/).
- [ONNX Runtime Mobile](https://onnxruntime.ai/docs/tutorials/mobile/).
- [ONNX Runtime GenAI](https://github.com/microsoft/onnxruntime-genai).

## 📥 Material descargable

- 📄 [Guía explicativa (PDF)](./clase-167-onnx-onnx-runtime-portabilidad-guia-explicativa.pdf) — versión imprimible con todo el contenido de la clase.
- 🎞️ [Presentación (PPTX)](./clase-167-onnx-onnx-runtime-portabilidad-presentacion.pptx) — deck PowerPoint listo para proyectar en clase.
- 🧮 [Notebook ejecutable (.ipynb)](./notebook.ipynb) — abrilo desde el laboratorio del programa o desde Jupyter.

## ➡️ Siguiente clase

[Clase 168 — Despliegue en Vertex AI](../168-despliegue-en-vertex-ai/README.md)
