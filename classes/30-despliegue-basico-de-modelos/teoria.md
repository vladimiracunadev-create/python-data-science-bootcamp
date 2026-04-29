# 📖 Teoría — Clase 30: Despliegue básico de modelos

## 1. El problema del notebook

Durante el bootcamp construimos modelos muy útiles: clasificadores de estudiantes, predicciones de ventas, detectores de anomalías. Pero todos viven dentro de notebooks de Jupyter. Solo nosotros podemos usarlos, solo en nuestra computadora, solo cuando abrimos el archivo manualmente.

Esto tiene un nombre: **el abismo de despliegue** (deployment gap). Es la diferencia entre "un modelo que funciona en mi máquina" y "un modelo que el mundo puede usar".

El despliegue es el proceso de cruzar ese abismo.

---

## 2. Conceptos clave

### Serialización

Serializar significa convertir un objeto Python (como un modelo entrenado) en una secuencia de bytes que puede guardarse en disco o transmitirse por red. Deserializar es el proceso inverso: leer esos bytes y reconstruir el objeto original.

Cuando haces `joblib.dump(modelo, 'modelo.pkl')`, estás serializando el modelo. Cuando haces `joblib.load('modelo.pkl')`, estás deserializando.

### El archivo `.pkl`

Los archivos con extensión `.pkl` (pickle) o a veces `.joblib` contienen un modelo serializado. Incluyen:
- Los parámetros aprendidos durante el entrenamiento (pesos del árbol, splits, etc.)
- La arquitectura del modelo (qué tipo de modelo es, con qué hiperparámetros)
- Metadatos de versión de scikit-learn

**Importante:** Si actualizas la versión de scikit-learn, es posible que los archivos `.pkl` antiguos no sean compatibles. Por eso es buena práctica guardar también la versión usada.

### API (Application Programming Interface)

Una API es una interfaz que permite a dos sistemas comunicarse. En el contexto de modelos ML, una API de predicción recibe datos de entrada, los procesa y devuelve una predicción.

La comunicación más común es HTTP (el mismo protocolo que usan los sitios web). Los datos se envían y reciben en formato JSON (JavaScript Object Notation), que es simplemente texto estructurado.

---

## 3. joblib vs pickle

Python incluye la librería `pickle` desde el principio para serializar objetos. `joblib` es una librería externa que mejora a pickle para el caso específico de objetos que contienen arrays de NumPy grandes, que es exactamente el caso de los modelos de scikit-learn.

```python
# Con pickle (librería estándar de Python)
import pickle

with open('modelo.pkl', 'wb') as f:
    pickle.dump(modelo, f)

with open('modelo.pkl', 'rb') as f:
    modelo_cargado = pickle.load(f)

# Con joblib (más eficiente para sklearn)
import joblib

joblib.dump(modelo, 'modelo.pkl')
modelo_cargado = joblib.load('modelo.pkl')
```

Para modelos simples de sklearn, la diferencia de velocidad es pequeña. Para modelos grandes (Random Forest con muchos árboles) o cuando el modelo incluye arrays numpy muy grandes, joblib puede ser significativamente más rápido.

---

## 4. Lo que debes guardar además del modelo

Un error muy común es guardar solo el modelo y olvidar guardar el preprocessor. Si entrenas con datos normalizados, necesitas aplicar exactamente la misma normalización a los datos nuevos.

```python
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Entrenar
scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)

modelo = RandomForestClassifier()
modelo.fit(X_train_sc, y_train)

# GUARDAR AMBOS
joblib.dump(modelo, 'modelo.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Cargar y usar
modelo_prod = joblib.load('modelo.pkl')
scaler_prod = joblib.load('scaler.pkl')

# Nuevos datos -> normalizar con EL MISMO scaler -> predecir
X_nuevo = [[7.5, 6.8, 0.90, 23]]
X_nuevo_sc = scaler_prod.transform(X_nuevo)  # fit_transform en producción sería un error
prediccion = modelo_prod.predict(X_nuevo_sc)
```

**Nota crítica:** En producción siempre usa `.transform()`, nunca `.fit_transform()`. El scaler debe estar calibrado con los datos de entrenamiento y solo transformar los datos nuevos.

---

## 5. Una función de predicción limpia

Antes de construir la API, es buena práctica encapsular la lógica de predicción en una función que:
- Acepta datos en formato legible (un diccionario o una lista de valores)
- Hace toda la transformación necesaria
- Devuelve la predicción en formato legible

```python
import joblib
import numpy as np

modelo = joblib.load('modelo.pkl')
scaler = joblib.load('scaler.pkl')

def predecir_estudiante(nota_matematicas, nota_lengua, asistencia, edad):
    """
    Predice si un estudiante aprobará basándose en sus características.
    
    Parámetros:
        nota_matematicas (float): Nota de 1 a 10
        nota_lengua (float): Nota de 1 a 10
        asistencia (float): Porcentaje de 0 a 1
        edad (int): Edad del estudiante
    
    Retorna:
        dict: {'aprobado': bool, 'probabilidad': float}
    """
    X = np.array([[nota_matematicas, nota_lengua, asistencia, edad]])
    X_scaled = scaler.transform(X)
    
    prediccion = modelo.predict(X_scaled)[0]
    probabilidad = modelo.predict_proba(X_scaled)[0][1]
    
    return {
        'aprobado': bool(prediccion),
        'probabilidad': round(float(probabilidad), 3)
    }

# Uso
resultado = predecir_estudiante(7.5, 6.8, 0.90, 23)
print(resultado)  # {'aprobado': True, 'probabilidad': 0.847}
```

---

## 6. Flask — construcción de la API

### ¿Qué es Flask?

Flask es un framework web minimalista para Python. Permite crear un servidor HTTP funcional con muy pocas líneas de código. Es ideal para prototipos, servicios internos y aprender los conceptos de APIs.

### El concepto de ruta (route)

Una ruta es una URL + un método HTTP que el servidor sabe cómo manejar.

```python
@app.route('/predict', methods=['POST'])
def predict():
    # Esta función se ejecuta cuando alguien envía un POST a /predict
    ...
```

Los métodos HTTP más comunes:
- **GET:** obtener información (leer)
- **POST:** enviar información para procesamiento (crear, predecir)
- **PUT:** actualizar
- **DELETE:** eliminar

Para predicciones usamos POST porque enviamos datos al servidor.

### JSON como formato de comunicación

JSON (JavaScript Object Notation) es el formato estándar para intercambiar datos en APIs web. Es texto legible que representa diccionarios, listas y valores básicos.

```json
{
    "nota_matematicas": 7.5,
    "nota_lengua": 6.8,
    "asistencia": 0.90,
    "edad": 23
}
```

En Flask:
- `request.get_json()` lee el JSON que envió el cliente
- `jsonify(diccionario)` convierte un diccionario Python en respuesta JSON

### La API completa

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo y scaler al iniciar (no en cada request)
modelo = joblib.load('modelo_estudiantes.pkl')
scaler = joblib.load('scaler_estudiantes.pkl')

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de verificación — confirma que el servidor está funcionando"""
    return jsonify({'status': 'ok', 'modelo': 'Random Forest Estudiantes'})

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint de predicción — recibe datos del estudiante y devuelve predicción"""
    try:
        datos = request.get_json()
        
        # Validar que los campos requeridos estén presentes
        campos = ['nota_matematicas', 'nota_lengua', 'asistencia', 'edad']
        for campo in campos:
            if campo not in datos:
                return jsonify({'error': f'Campo faltante: {campo}'}), 400
        
        X = np.array([[
            datos['nota_matematicas'],
            datos['nota_lengua'],
            datos['asistencia'],
            datos['edad']
        ]])
        
        X_scaled = scaler.transform(X)
        prediccion = modelo.predict(X_scaled)[0]
        probabilidad = modelo.predict_proba(X_scaled)[0][1]
        
        return jsonify({
            'aprobado': bool(prediccion),
            'probabilidad': round(float(probabilidad), 3),
            'mensaje': 'Aprobado' if prediccion else 'Reprobado'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

## 7. Probar la API con requests

```python
import requests

URL = 'http://localhost:5000/predict'

# Caso 1: estudiante con buen rendimiento
respuesta = requests.post(URL, json={
    'nota_matematicas': 8.5,
    'nota_lengua': 7.8,
    'asistencia': 0.95,
    'edad': 22
})
print('Estudiante bueno:', respuesta.json())

# Caso 2: estudiante con bajo rendimiento
respuesta = requests.post(URL, json={
    'nota_matematicas': 4.2,
    'nota_lengua': 3.9,
    'asistencia': 0.60,
    'edad': 30
})
print('Estudiante en riesgo:', respuesta.json())
```

---

## 8. Lo que sucede en producción real

Para un proyecto real, hay muchas más consideraciones:

### Docker
Empaquetar la aplicación y todas sus dependencias en un contenedor, para que funcione igual en cualquier computadora o servidor.

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### Cloud (nube)
Desplegar el contenedor en servicios como AWS ECS, Google Cloud Run o Azure Container Instances para que esté disponible 24/7.

### Monitoreo
Registrar las predicciones en producción para detectar si el modelo empieza a tener peor rendimiento (data drift: los datos reales se vuelven diferentes a los de entrenamiento).

---

## 9. Próximos pasos

### FastAPI
Alternativa moderna a Flask, más rápida y con documentación automática:
```python
from fastapi import FastAPI
app = FastAPI()

@app.post('/predict')
def predict(datos: EstudianteInput):
    ...
```

### Streamlit
Para crear interfaces web sin HTML/CSS:
```python
import streamlit as st

nota = st.slider('Nota de matemáticas', 1.0, 10.0, 7.0)
if st.button('Predecir'):
    resultado = predecir_estudiante(nota, ...)
    st.write(resultado)
```

---

## Resumen

Desplegar un modelo requiere cuatro componentes: guardarlo correctamente (con todo su preprocessor), tener una función de predicción limpia, envolver esa función en un servidor HTTP, y probar que funciona correctamente. Flask es la forma más sencilla de hacer el servidor HTTP. joblib es la forma más directa de guardar modelos de scikit-learn.
