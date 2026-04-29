# 📊 Slides — Clase 30: Despliegue básico de modelos

---

## Slide 1: ¿Qué es el despliegue (deployment)?

**El problema:**
- Entrenaste un modelo con 95% de precisión en tu notebook
- Solo tú puedes usarlo... en tu computadora
- No es útil para nadie más

**El despliegue es:** Convertir ese modelo en un **servicio** que otros sistemas o personas pueden usar directamente.

> "Un modelo que solo funciona en un notebook no es un producto — es un experimento."

---

## Slide 2: El pipeline completo

```
1. ENTRENAR          → modelo.fit(X_train, y_train)
       ↓
2. GUARDAR           → joblib.dump(modelo, 'modelo.pkl')
       ↓
3. CARGAR            → modelo = joblib.load('modelo.pkl')
       ↓
4. PREDECIR          → resultado = predecir(datos_nuevos)
       ↓
5. SERVIR            → API recibe solicitud → devuelve predicción
```

---

## Slide 3: Guardar modelos con joblib

```python
import joblib
from sklearn.ensemble import RandomForestClassifier

# Entrenar
modelo = RandomForestClassifier(n_estimators=100)
modelo.fit(X_train, y_train)

# Guardar (serializar)
joblib.dump(modelo, 'modelo_estudiantes.pkl')
print('Modelo guardado')

# Cargar (deserializar) — en otro script, otro momento
modelo_cargado = joblib.load('modelo_estudiantes.pkl')
predicciones = modelo_cargado.predict(X_nuevos)
```

**¿Por qué joblib?**
- Más eficiente que pickle para arrays numpy grandes
- Estándar en el ecosistema scikit-learn
- Muy simple de usar

---

## Slide 4: Guardar también el scaler

Muy importante: si normalizaste los datos al entrenar, debes guardar también el scaler.

```python
from sklearn.preprocessing import StandardScaler
import joblib

# Guardar
joblib.dump(modelo, 'modelo.pkl')
joblib.dump(scaler, 'scaler.pkl')

# Cargar y usar
modelo = joblib.load('modelo.pkl')
scaler = joblib.load('scaler.pkl')

# Nuevos datos
nuevos_datos = [[7.5, 6.8, 0.90, 23]]
nuevos_datos_scaled = scaler.transform(nuevos_datos)
predicción = modelo.predict(nuevos_datos_scaled)
```

---

## Slide 5: Diferencia entre joblib y pickle

| Aspecto | joblib | pickle |
|---------|--------|--------|
| Eficiencia con arrays | Mejor | Menor |
| Facilidad de uso | Igual | Igual |
| Estándar en sklearn | Sí | No oficial |
| Parte de Python estándar | No (librería externa) | Sí (incluida) |
| Recomendado para ML | ✅ Sí | Puede usarse |

---

## Slide 6: ¿Qué es Flask?

**Flask** es un framework web minimalista para Python.

Permite crear un servidor HTTP con muy poco código:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hola')
def hola():
    return 'Hola mundo!'

if __name__ == '__main__':
    app.run()
```

Cuando ejecutas este script, Flask levanta un servidor en `http://localhost:5000`

---

## Slide 7: Un endpoint /predict

```python
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
modelo = joblib.load('modelo.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    datos = request.get_json()
    
    X = np.array([[
        datos['nota_matematicas'],
        datos['nota_lengua'],
        datos['asistencia'],
        datos['edad']
    ]])
    
    X_scaled = scaler.transform(X)
    predicción = modelo.predict(X_scaled)[0]
    probabilidad = modelo.predict_proba(X_scaled)[0][1]
    
    return jsonify({
        'aprobado': bool(predicción),
        'probabilidad': round(float(probabilidad), 3)
    })

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Slide 8: Cómo probar la API

**Desde Python (requests):**
```python
import requests

respuesta = requests.post(
    'http://localhost:5000/predict',
    json={
        'nota_matematicas': 7.5,
        'nota_lengua': 6.8,
        'asistencia': 0.90,
        'edad': 23
    }
)
print(respuesta.json())
# {'aprobado': True, 'probabilidad': 0.847}
```

**Desde terminal (curl):**
```bash
curl -X POST http://localhost:5000/predict \
  -H "Content-Type: application/json" \
  -d '{"nota_matematicas": 7.5, "nota_lengua": 6.8, "asistencia": 0.90, "edad": 23}'
```

---

## Slide 9: ¿Qué pasa en producción real?

En un entorno real, hay mucho más que un script de Flask:

| Componente | Para qué sirve |
|------------|---------------|
| **Docker** | Empaquetar el código + dependencias en un contenedor |
| **Nube (AWS, GCP, Azure)** | Correr el contenedor 24/7 para cualquier usuario |
| **Load Balancer** | Distribuir tráfico entre múltiples instancias |
| **Monitoring** | Detectar si el modelo empeora con el tiempo |
| **Logging** | Registrar cada predicción para auditoría |

---

## Slide 10: Próximos pasos

### FastAPI (recomendado sobre Flask para producción)
- Más moderno y rápido
- Genera documentación automática
- Validación de datos incluida

### Streamlit (para interfaces rápidas)
- Crea una interfaz web con pocas líneas
- Ideal para demos y dashboards
- No requiere conocimientos de HTML/CSS

### MLflow / BentoML (plataformas de MLOps)
- Gestión completa del ciclo de vida del modelo
- Versionado, tracking, despliegue automatizado

---

## Slide 11: Resumen

> Desplegar un modelo significa convertirlo en un servicio que otros sistemas o personas pueden usar directamente, sin abrir un notebook.

**Los 5 pasos que aprendimos hoy:**
1. Entrenar el modelo en scikit-learn
2. Guardarlo con `joblib.dump()`
3. Cargarlo con `joblib.load()`
4. Crear una función de predicción limpia
5. Servirla con Flask en un endpoint `/predict`
