# Tecnologias complementarias - Clase 30: Despliegue Básico de Modelos

> Herramientas y recursos para ampliar lo aprendido.

## Librerias relacionadas

| Libreria | Para que sirve | Nivel sugerido |
|---|---|---|
| `joblib` | Serializar y deserializar modelos sklearn de forma eficiente | Principiante |
| `Flask` | Framework minimalista para crear APIs web en Python | Principiante |
| `FastAPI` | Framework moderno para APIs con validación automática y documentación interactiva | Intermedio |
| `Streamlit` | Crear aplicaciones web interactivas de datos sin saber HTML/CSS | Principiante |
| `Gradio` | Interfaces web rápidas para modelos de ML, muy popular para demos | Principiante |
| `BentoML` | Framework especializado para empaquetar, testear y desplegar modelos ML | Avanzado |

## Recursos recomendados

- **Documentación oficial Flask**: https://flask.palletsprojects.com/en/stable/quickstart/ - tutorial de inicio rápido muy accesible
- **Tutorial recomendado**: "Deploying Machine Learning Models with Flask" en Real Python (realpython.com)
- **Concepto clave para buscar**: "REST API machine learning deployment Python" y "FastAPI vs Flask for ML"

## Próximos pasos sugeridos

- Aprender FastAPI para despliegue mas robusto: tiene validación automática con Pydantic, documentación Swagger integrada y mejor rendimiento que Flask
- Explorar Streamlit para crear dashboards interactivos donde usuarios no técnicos puedan usar el modelo sin saber de APIs
- Estudiar Docker: permite empaquetar la aplicación y todas sus dependencias para que funcione igual en cualquier computadora o servidor
- Investigar servicios cloud como AWS SageMaker, Google Cloud AI Platform o Azure ML para despliegue escalable

## Herramientas alternativas

| Herramienta | Descripción | Cuando usarla |
|---|---|---|
| `FastAPI` | API moderna con validación automática, tipado fuerte y documentación Swagger auto-generada | Cuando necesitas una API de producción robusta y bien documentada |
| `Streamlit` | Convierte scripts de Python en apps web interactivas en minutos | Cuando el usuario final es un analista o tomador de decisiones no técnico |
| `MLflow Models` | Empaquetado estandar de modelos con servidor de inferencia incluido | Cuando ya usas MLflow para tracking y quieres consistencia |
