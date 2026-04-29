# Guia de código - Clase 30: Despliegue Básico de Modelos

> Walkthrough del código clave, bloque por bloque.

## Bloque 1: Guardar el modelo y el preprocesador con joblib

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Cargar y preparar datos
df = pd.read_csv("estudiantes.csv")
X = df[["horas_estudio", "asistencia", "promedio_anterior", "tareas_entregadas"]]
y = df["aprobado"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Entrenar el preprocesador y el modelo
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train_scaled, y_train)

accuracy = accuracy_score(y_test, modelo.predict(X_test_scaled))
print(f"Accuracy del modelo: {accuracy:.3f}")

# Guardar modelo Y scaler en archivos separados
joblib.dump(modelo, "modelo_estudiantes.pkl")
joblib.dump(scaler, "scaler_estudiantes.pkl")

print("Modelo guardado como: modelo_estudiantes.pkl")
print("Scaler guardado como: scaler_estudiantes.pkl")

# Verificar que se pueden cargar correctamente
modelo_cargado = joblib.load("modelo_estudiantes.pkl")
scaler_cargado = joblib.load("scaler_estudiantes.pkl")
print("Carga verificada correctamente.")
```

**Que hace?** Entrena un RandomForestClassifier con datos escalados y guarda tanto el modelo como el scaler en archivos .pkl usando joblib.

**Por que asi?** Es fundamental guardar el scaler junto con el modelo porque en producción los datos nuevos deben escalarse con exactamente los mismos parámetros (media y desviacion estandar) aprendidos durante el entrenamiento. Si reentrenamos el scaler con datos nuevos, el modelo recibira valores en escala diferente y dara predicciones incorrectas.

**Resultado esperado:**
```
Accuracy del modelo: 0.875
Modelo guardado como: modelo_estudiantes.pkl
Scaler guardado como: scaler_estudiantes.pkl
Carga verificada correctamente.
```

---

## Bloque 2: Función de predicción limpia con validación

```python
import joblib
import numpy as np

# Cargar modelo y scaler una sola vez al inicio del programa
modelo = joblib.load("modelo_estudiantes.pkl")
scaler = joblib.load("scaler_estudiantes.pkl")

def predict_single(horas_estudio, asistencia, promedio_anterior, tareas_entregadas):
    # Validación de entrada
    if not (0 <= horas_estudio <= 40):
        raise ValueError(f"horas_estudio debe estar entre 0 y 40, recibido: {horas_estudio}")
    if not (0 <= asistencia <= 100):
        raise ValueError(f"asistencia debe estar entre 0 y 100, recibido: {asistencia}")
    if not (0 <= promedio_anterior <= 10):
        raise ValueError(f"promedio_anterior debe estar entre 0 y 10, recibido: {promedio_anterior}")
    if not (0 <= tareas_entregadas <= 20):
        raise ValueError(f"tareas_entregadas debe estar entre 0 y 20, recibido: {tareas_entregadas}")

    # Crear array con los datos de entrada
    datos = np.array([[horas_estudio, asistencia, promedio_anterior, tareas_entregadas]])

    # Escalar con el mismo scaler del entrenamiento
    datos_scaled = scaler.transform(datos)

    # Predecir
    predicción = int(modelo.predict(datos_scaled)[0])
    probabilidad = float(modelo.predict_proba(datos_scaled)[0][1])

    return {
        "predicción": predicción,
        "resultado": "Aprobado" if predicción == 1 else "Reprobado",
        "probabilidad_aprobado": round(probabilidad, 3)
    }

# Probar la función
resultado = predict_single(
    horas_estudio=15,
    asistencia=85,
    promedio_anterior=7.5,
    tareas_entregadas=18
)
print("Resultado de predicción:", resultado)
```

**Que hace?** Define una función reutilizable que encapsula todo el pipeline: validación de entrada, escalado y predicción. Devuelve un diccionario con la predicción y la probabilidad.

**Por que asi?** Encapsular la logica en una función con validación de entrada hace el código mas robusto. Si alguien envia un valor de asistencia de 150% (imposible), el sistema devuelve un error claro en lugar de predecir algo sin sentido.

**Resultado esperado:**
```
Resultado de predicción: {'predicción': 1, 'resultado': 'Aprobado', 'probabilidad_aprobado': 0.87}
```

---

## Bloque 3: API minima con Flask

```python
# archivo: app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar modelo y scaler una sola vez al iniciar la aplicación
modelo = joblib.load("modelo_estudiantes.pkl")
scaler = joblib.load("scaler_estudiantes.pkl")

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensaje": "API de predicción de estudiantes",
        "versión": "1.0",
        "rutas": {"POST /predict": "Predice si un estudiante aprobara"}
    })

@app.route("/predict", methods=["POST"])
def predecir():
    try:
        datos = request.get_json()

        if datos is None:
            return jsonify({"error": "El cuerpo debe ser JSON valido"}), 400

        campos_requeridos = ["horas_estudio", "asistencia", "promedio_anterior", "tareas_entregadas"]
        for campo in campos_requeridos:
            if campo not in datos:
                return jsonify({"error": f"Falta el campo: {campo}"}), 400

        entrada = np.array([[
            datos["horas_estudio"],
            datos["asistencia"],
            datos["promedio_anterior"],
            datos["tareas_entregadas"]
        ]])

        entrada_scaled = scaler.transform(entrada)
        predicción = int(modelo.predict(entrada_scaled)[0])
        probabilidad = float(modelo.predict_proba(entrada_scaled)[0][1])

        return jsonify({
            "predicción": predicción,
            "resultado": "Aprobado" if predicción == 1 else "Reprobado",
            "probabilidad_aprobado": round(probabilidad, 3),
            "datos_recibidos": datos
        })

    except ValueError as e:
        return jsonify({"error": f"Valor invalido: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Error interno: {str(e)}"}), 500

if __name__ == "__main__":
    print("Iniciando API en http://localhost:5000")
    app.run(debug=True, port=5000)
```

**Que hace?** Crea una API web minima con dos rutas: GET `/` para verificar que la API esta corriendo, y POST `/predict` que recibe datos de un estudiante en JSON y devuelve la predicción.

**Por que asi?** Cargar el modelo fuera de las funciones de ruta garantiza que se carga una sola vez al iniciar el servidor, no en cada peticion. El bloque `try/except` captura errores y devuelve respuestas HTTP con códigos de estado apropiados (400 para errores del cliente, 500 para errores del servidor).

**Resultado esperado:** Al ejecutar `python app.py` el servidor se inicia en el puerto 5000 y queda esperando peticiones.

---

## Bloque 4: Probar la API con requests

```python
import requests
import json

BASE_URL = "http://localhost:5000"

# Probar la ruta de bienvenida
respuesta = requests.get(f"{BASE_URL}/")
print("Estado:", respuesta.status_code)
print("Respuesta:", json.dumps(respuesta.json(), indent=2, ensure_ascii=False))

# Probar la predicción con un estudiante con buen rendimiento
estudiante_bueno = {
    "horas_estudio": 20,
    "asistencia": 92,
    "promedio_anterior": 8.5,
    "tareas_entregadas": 19
}
respuesta = requests.post(f"{BASE_URL}/predict", json=estudiante_bueno)
print("\nPrediccion estudiante con buen rendimiento:")
print(json.dumps(respuesta.json(), indent=2, ensure_ascii=False))

# Probar con un estudiante en riesgo
estudiante_riesgo = {
    "horas_estudio": 3,
    "asistencia": 45,
    "promedio_anterior": 4.2,
    "tareas_entregadas": 5
}
respuesta = requests.post(f"{BASE_URL}/predict", json=estudiante_riesgo)
print("\nPrediccion estudiante en riesgo:")
print(json.dumps(respuesta.json(), indent=2, ensure_ascii=False))

# Probar con datos incorrectos (debe devolver error 400)
datos_malos = {"horas_estudio": 10}
respuesta = requests.post(f"{BASE_URL}/predict", json=datos_malos)
print("\nPrueba con datos incompletos:")
print(f"Estado HTTP: {respuesta.status_code}")
print(json.dumps(respuesta.json(), indent=2, ensure_ascii=False))
```

**Que hace?** Prueba la API desde Python usando `requests`. Envia peticiones GET y POST con diferentes datos y verifica que las respuestas sean correctas, incluyendo el manejo de errores.

**Por que asi?** Probar la API programaticamente permite automatizar las pruebas. El parámetro `json=` en `requests.post()` serializa el diccionario a JSON automaticamente y agrega el header `Content-Type: application/json`, que Flask necesita para que `request.get_json()` funcione correctamente.

**Resultado esperado:**
```
Estado: 200
Predicción estudiante con buen rendimiento:
{"predicción": 1, "resultado": "Aprobado", "probabilidad_aprobado": 0.91, ...}
Predicción estudiante en riesgo:
{"predicción": 0, "resultado": "Reprobado", "probabilidad_aprobado": 0.23, ...}
Estado HTTP: 400
{"error": "Falta el campo: asistencia"}
```

---

## Errores comunes y como resolverlos

| Error | Por que ocurre | Solución |
|---|---|---|
| `ConnectionRefusedError` al hacer requests | El servidor Flask no esta corriendo | Ejecutar `python app.py` antes de probar con requests |
| `joblib.load` da error al cargar el modelo | El archivo .pkl no existe o esta en otra carpeta | Verificar la ruta con `os.path.exists("modelo.pkl")` y usar ruta absoluta si es necesario |
| `request.get_json()` devuelve None | La peticion no tiene `Content-Type: application/json` | Usar `json=datos` en requests o agregar el header manualmente |
| El modelo predice bien en notebook pero mal en la API | Se usa un scaler diferente en producción | Siempre guardar y cargar el mismo scaler del entrenamiento |
| `ValueError: X has N features but model expects M` | Los datos de entrada no tienen el mismo número de columnas que el entrenamiento | Verificar que se usan exactamente las mismas columnas en el mismo orden |
