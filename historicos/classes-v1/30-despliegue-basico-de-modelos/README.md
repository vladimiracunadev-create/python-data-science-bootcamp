# 📘 Clase 30: Despliegue básico de modelos

> 🎯 Ficha de clase con objetivo, materiales y foco de aprendizaje.

## 🎯 Objetivo
Aprender a convertir un modelo entrenado en un servicio real que puede recibir solicitudes y devolver predicciones. En esta clase entrenamos un modelo, lo guardamos con joblib, lo cargamos en otro script y construimos un endpoint HTTP mínimo con Flask para que cualquier sistema pueda consultarlo.

## ⏱️ Duración sugerida
90 minutos

## 📦 Dataset base
- `datasets/estudiantes.csv`

## ✅ Resultados esperados
Al finalizar, el estudiante podrá:
- Guardar y cargar modelos con joblib y pickle, construir una función de predicción que acepte datos crudos, crear un endpoint /predict con Flask que reciba JSON y devuelva JSON

## 🧭 Temas clave
- Serialización de modelos: joblib.dump / joblib.load
- Pipeline de despliegue: entrenar → guardar → cargar → predecir → servir
- Flask: rutas, requests, respuestas JSON
- Testing de la API con la librería requests
- Próximos pasos: FastAPI, Streamlit, Docker

## 🧰 Materiales del módulo
- `README.md`, `slides.md`, `teoria.md`, `ejercicios.md`, `homework.md`, `notebook.ipynb`, `soluciones.ipynb`

## 💻 Cómo leer el código de esta clase
- Cada bloque debe responder una pregunta concreta.

## 💡 Idea central
Desplegar un modelo significa convertirlo en un servicio que otros sistemas o personas pueden usar directamente, sin abrir un notebook.

## 👩‍🏫 Nota para el docente
Haz una demo en vivo: corre el servidor Flask en una terminal y envía un POST request desde otra terminal o desde el notebook. Ver la predicción llegar en tiempo real es el momento "¡wow!" de esta clase. Asegúrate de tener Flask instalado antes de clase: `pip install flask`.
