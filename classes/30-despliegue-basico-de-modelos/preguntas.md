# Preguntas - Clase 30: Despliegue Basico de Modelos

> Preguntas de comprension, discusion y evaluacion.

## Preguntas de comprension

1. Que significa "desplegar" un modelo de machine learning? Por que no es suficiente con tener el modelo entrenado en un notebook?
2. Que hace `joblib.dump(modelo, 'modelo.pkl')`? Por que es necesario guardar el modelo en un archivo?
3. Por que debemos guardar el `StandardScaler` junto con el modelo cuando hacemos despliegue? Que pasaria si no lo hicieramos?
4. Que es Flask y para que se usa en el contexto del despliegue de modelos?
5. Que diferencia hay entre una peticion GET y una peticion POST en una API REST? Cual se usa para enviar datos al modelo?
6. Que hace `request.get_json()` dentro de una ruta de Flask? Que tipo de dato devuelve?
7. Que son Docker y la nube (cloud) en el contexto del despliegue? Que problema resuelven?

## Preguntas de discusion

1. Un cientifico de datos entrega su modelo como un archivo `.ipynb` al equipo de ingenieria. Por que esto no es suficiente para produccion? Que deberia entregar en su lugar?
2. Que riesgos de seguridad tiene exponer un modelo de ML como una API publica sin autenticacion? Como los mitigarias?
3. Compara Flask, FastAPI y Streamlit para desplegar un modelo: cuando usarias cada uno segun el tipo de usuario final (otro sistema, un desarrollador, o un usuario no tecnico)?

## Preguntas de codigo

1. Escribe el codigo para cargar un modelo guardado con joblib y usarlo para predecir sobre nuevos datos.
2. Como crearias una ruta `/predict` en Flask que reciba un JSON con datos de un estudiante y devuelva la prediccion?
3. Escribe el codigo para probar tu API de Flask desde Python usando la libreria `requests`, enviando datos como JSON.

## Pregunta integradora

Entrenaste un modelo para predecir si un estudiante aprobara el examen. Ahora el equipo de tecnologia quiere integrarlo en el sistema de la escuela. Describe el proceso completo de despliegue: como guardarias el modelo y el preprocesador, como diseniarias la funcion `predict_single()`, como construirias la API con Flask, que pruebas harias antes de entregar, y que consideraciones de mantenimiento tendrias cuando el modelo necesite reentrenarse con datos nuevos.
