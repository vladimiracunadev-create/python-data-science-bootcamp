# Tecnologias complementarias - Clase 30: Despliegue Basico de Modelos

> Herramientas y recursos para ampliar lo aprendido.

## Librerias relacionadas

| Libreria | Para que sirve | Nivel sugerido |
|---|---|---|
| `joblib` | Serializar y deserializar modelos sklearn de forma eficiente | Principiante |
| `Flask` | Framework minimalista para crear APIs web en Python | Principiante |
| `FastAPI` | Framework moderno para APIs con validacion automatica y documentacion interactiva | Intermedio |
| `Streamlit` | Crear aplicaciones web interactivas de datos sin saber HTML/CSS | Principiante |
| `Gradio` | Interfaces web rapidas para modelos de ML, muy popular para demos | Principiante |
| `BentoML` | Framework especializado para empaquetar, testear y desplegar modelos ML | Avanzado |

## Recursos recomendados

- **Documentacion oficial Flask**: https://flask.palletsprojects.com/en/stable/quickstart/ - tutorial de inicio rapido muy accesible
- **Tutorial recomendado**: "Deploying Machine Learning Models with Flask" en Real Python (realpython.com)
- **Concepto clave para buscar**: "REST API machine learning deployment Python" y "FastAPI vs Flask for ML"

## Proximos pasos sugeridos

- Aprender FastAPI para despliegue mas robusto: tiene validacion automatica con Pydantic, documentacion Swagger integrada y mejor rendimiento que Flask
- Explorar Streamlit para crear dashboards interactivos donde usuarios no tecnicos puedan usar el modelo sin saber de APIs
- Estudiar Docker: permite empaquetar la aplicacion y todas sus dependencias para que funcione igual en cualquier computadora o servidor
- Investigar servicios cloud como AWS SageMaker, Google Cloud AI Platform o Azure ML para despliegue escalable

## Herramientas alternativas

| Herramienta | Descripcion | Cuando usarla |
|---|---|---|
| `FastAPI` | API moderna con validacion automatica, tipado fuerte y documentacion Swagger auto-generada | Cuando necesitas una API de produccion robusta y bien documentada |
| `Streamlit` | Convierte scripts de Python en apps web interactivas en minutos | Cuando el usuario final es un analista o tomador de decisiones no tecnico |
| `MLflow Models` | Empaquetado estandar de modelos con servidor de inferencia incluido | Cuando ya usas MLflow para tracking y quieres consistencia |
