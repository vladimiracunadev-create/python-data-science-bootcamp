# 🏋️ Ejercicios — Clase 30: Despliegue básico de modelos

---

## Ejercicio 1: Guardar y cargar un modelo

```python
import numpy as np
import pandas as pd
import joblib
import pickle
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

np.random.seed(42)
n = 400
cursos = np.random.choice(['A', 'B', 'C'], size=n, p=[0.4, 0.4, 0.2])
nota_mate = np.where(cursos == 'A', np.random.normal(7.5, 1.2, n),
    np.where(cursos == 'B', np.random.normal(7.0, 1.3, n), np.random.normal(5.8, 1.5, n))).clip(1, 10)
nota_lengua = np.where(cursos == 'A', np.random.normal(7.2, 1.1, n),
    np.where(cursos == 'B', np.random.normal(6.8, 1.2, n), np.random.normal(5.5, 1.4, n))).clip(1, 10)
asistencia = np.where(cursos == 'C', np.random.uniform(0.55, 0.85, n), np.random.uniform(0.70, 0.99, n))
edades = np.random.randint(18, 35, size=n)
prob = (nota_mate * 0.4 + nota_lengua * 0.4 + asistencia * 10 * 0.2) / 10
aprobado = (np.random.uniform(0, 1, n) < prob).astype(int)

features = ['nota_matematicas', 'nota_lengua', 'asistencia', 'edad']
X = pd.DataFrame({'nota_matematicas': nota_mate.round(1), 'nota_lengua': nota_lengua.round(1),
                  'asistencia': asistencia.round(2), 'edad': edades})[features]
y = aprobado

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_sc = scaler.fit_transform(X_train)
X_test_sc = scaler.transform(X_test)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train_sc, y_train)

# a) Guardar con joblib
joblib.dump(modelo, 'modelo_ejercicio.pkl')
joblib.dump(scaler, 'scaler_ejercicio.pkl')
print('Modelos guardados con joblib')

# b) Cargar en "producción" (otro contexto)
modelo_prod = joblib.load('modelo_ejercicio.pkl')
scaler_prod = joblib.load('scaler_ejercicio.pkl')

# c) Verificar que la precisión es la misma
acc_original = accuracy_score(y_test, modelo.predict(X_test_sc))
acc_cargado = accuracy_score(y_test, modelo_prod.predict(scaler_prod.transform(X_test)))

print(f'Precisión modelo original:  {acc_original:.2%}')
print(f'Precisión modelo cargado:   {acc_cargado:.2%}')
print(f'Son iguales: {acc_original == acc_cargado}')

# d) Ver tamaño del archivo
tamano = os.path.getsize('modelo_ejercicio.pkl') / 1024
print(f'Tamaño del archivo: {tamano:.1f} KB')
```

**Pregunta:** ¿Por qué es importante verificar que la precisión del modelo cargado sea igual a la del original? ¿Qué podría salir mal?

---

## Ejercicio 2: Guardar con pickle (alternativa)

```python
# Guardar con pickle
with open('modelo_pickle.pkl', 'wb') as f:
    pickle.dump(modelo, f)

# Cargar con pickle
with open('modelo_pickle.pkl', 'rb') as f:
    modelo_pickle = pickle.load(f)

# Comparar tamaños
tam_joblib = os.path.getsize('modelo_ejercicio.pkl')
tam_pickle = os.path.getsize('modelo_pickle.pkl')

print(f'Tamaño con joblib: {tam_joblib / 1024:.1f} KB')
print(f'Tamaño con pickle: {tam_pickle / 1024:.1f} KB')
print(f'joblib es {((tam_pickle - tam_joblib) / tam_pickle * 100):.1f}% más pequeño')

# Verificar que el modelo funciona igual
acc_pickle = accuracy_score(y_test, modelo_pickle.predict(X_test_sc))
print(f'Precisión con pickle: {acc_pickle:.2%}')
```

---

## Ejercicio 3: Función de predicción limpia

Crea una función que acepte los datos de un estudiante y devuelva la predicción de forma legible:

```python
def predecir_estudiante(nota_matematicas, nota_lengua, asistencia, edad,
                        modelo=None, scaler=None):
    """
    Predice si un estudiante aprobará.
    
    Parámetros:
        nota_matematicas (float): Nota de 1 a 10
        nota_lengua (float): Nota de 1 a 10
        asistencia (float): Porcentaje de asistencia (0.0 a 1.0)
        edad (int): Edad del estudiante
    
    Retorna:
        dict con 'aprobado' (bool), 'probabilidad' (float) y 'nivel_confianza' (str)
    """
    # Tu código aquí
    pass

# Prueba la función
casos = [
    (8.5, 7.8, 0.95, 22, 'estudiante destacado'),
    (5.0, 5.2, 0.75, 25, 'estudiante promedio'),
    (3.8, 4.1, 0.60, 31, 'estudiante en riesgo'),
]

for nota_m, nota_l, asist, edad, descripcion in casos:
    resultado = predecir_estudiante(nota_m, nota_l, asist, edad,
                                     modelo=modelo_prod, scaler=scaler_prod)
    print(f'{descripcion}: {resultado}')
```

---

## Ejercicio 4: Construir la API de Flask

Crea un archivo `app.py` con la API completa:

```python
# app.py — Servidor Flask para predicción de estudiantes
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo y scaler al iniciar el servidor
modelo = joblib.load('modelo_ejercicio.pkl')
scaler = joblib.load('scaler_ejercicio.pkl')
FEATURES = ['nota_matematicas', 'nota_lengua', 'asistencia', 'edad']

@app.route('/health', methods=['GET'])
def health():
    """Verificar que el servidor está funcionando"""
    return jsonify({'status': 'ok', 'modelo': 'RandomForest Estudiantes v1'})

@app.route('/predict', methods=['POST'])
def predict():
    """
    Recibe datos de un estudiante y devuelve predicción.
    
    Cuerpo esperado (JSON):
        {
            "nota_matematicas": 7.5,
            "nota_lengua": 6.8,
            "asistencia": 0.90,
            "edad": 23
        }
    """
    try:
        datos = request.get_json()
        
        # Validar campos
        for campo in FEATURES:
            if campo not in datos:
                return jsonify({'error': f'Campo faltante: {campo}'}), 400
        
        # Preparar datos
        X = np.array([[datos[f] for f in FEATURES]])
        X_scaled = scaler.transform(X)
        
        # Predecir
        prediccion = int(modelo.predict(X_scaled)[0])
        probabilidad = float(modelo.predict_proba(X_scaled)[0][1])
        
        return jsonify({
            'aprobado': bool(prediccion),
            'probabilidad': round(probabilidad, 3),
            'mensaje': 'El estudiante aprobará' if prediccion else 'El estudiante está en riesgo'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

**Para ejecutar:** En una terminal, corre `python app.py`. El servidor quedará activo en `http://localhost:5000`.

---

## Ejercicio 5: Probar la API con requests

Con el servidor corriendo en otra terminal, ejecuta esto en el notebook:

```python
import requests

BASE_URL = 'http://localhost:5000'

# a) Verificar que el servidor está vivo
resp = requests.get(f'{BASE_URL}/health')
print('Health check:', resp.json())

# b) Predecir para distintos estudiantes
estudiantes = [
    {'nota_matematicas': 8.5, 'nota_lengua': 7.8, 'asistencia': 0.95, 'edad': 22},
    {'nota_matematicas': 5.0, 'nota_lengua': 5.2, 'asistencia': 0.75, 'edad': 25},
    {'nota_matematicas': 3.8, 'nota_lengua': 4.1, 'asistencia': 0.60, 'edad': 31},
]

for est in estudiantes:
    resp = requests.post(f'{BASE_URL}/predict', json=est)
    resultado = resp.json()
    print(f'Notas: {est[\"nota_matematicas\"]:.1f}/{est[\"nota_lengua\"]:.1f} | '
          f'Asistencia: {est[\"asistencia\"]:.0%} | '
          f'Resultado: {resultado[\"mensaje\"]} ({resultado[\"probabilidad\"]:.1%})')
```

---

## Ejercicio 6: Manejo de errores

Prueba que tu API maneja errores correctamente:

```python
# a) Campo faltante
resp = requests.post(f'{BASE_URL}/predict', json={'nota_matematicas': 7.5})
print('Campo faltante:', resp.status_code, resp.json())

# b) Valor fuera de rango (el modelo igual lo procesa — ¿debería rechazarlo?)
resp = requests.post(f'{BASE_URL}/predict', json={
    'nota_matematicas': 15.0,  # nota > 10
    'nota_lengua': 6.8,
    'asistencia': 0.90,
    'edad': 23
})
print('Valor fuera de rango:', resp.json())

# c) Datos inválidos (texto en lugar de número)
resp = requests.post(f'{BASE_URL}/predict', json={
    'nota_matematicas': 'siete',  # string, no número
    'nota_lengua': 6.8,
    'asistencia': 0.90,
    'edad': 23
})
print('Tipo de dato incorrecto:', resp.status_code)
```

**Reflexión:** ¿Debería la API validar rangos (ej. nota entre 1 y 10)? ¿Quién es responsable de esa validación, el servidor o el cliente?

---

## Ejercicio 7 (desafío): Agregar validación de datos

Mejora el endpoint `/predict` para rechazar valores fuera de rango:

```python
def validar_datos(datos):
    """
    Valida que los datos del estudiante estén en rangos válidos.
    Retorna None si todo está bien, o un mensaje de error si no.
    """
    validaciones = [
        ('nota_matematicas', 1.0, 10.0),
        ('nota_lengua', 1.0, 10.0),
        ('asistencia', 0.0, 1.0),
        ('edad', 15, 80),
    ]
    
    for campo, minimo, maximo in validaciones:
        valor = datos.get(campo)
        if valor is None:
            return f'Campo faltante: {campo}'
        if not isinstance(valor, (int, float)):
            return f'{campo} debe ser un número'
        if valor < minimo or valor > maximo:
            return f'{campo} debe estar entre {minimo} y {maximo}'
    
    return None  # Todo válido

# Prueba
print(validar_datos({'nota_matematicas': 7.5, 'nota_lengua': 6.8, 'asistencia': 0.9, 'edad': 23}))
print(validar_datos({'nota_matematicas': 15.0, 'nota_lengua': 6.8, 'asistencia': 0.9, 'edad': 23}))
print(validar_datos({'nota_matematicas': 7.5, 'nota_lengua': 'siete', 'asistencia': 0.9, 'edad': 23}))
```
