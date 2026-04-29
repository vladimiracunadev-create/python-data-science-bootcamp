# 📝 Tarea — Clase 30: Despliegue básico de modelos

**Entrega:** Antes de la próxima clase  
**Formato:** Jupyter Notebook + archivo `app.py`  
**Modalidad:** Individual

---

## Descripción general

En esta tarea vas a construir un sistema de predicción completo: desde entrenar un modelo hasta desplegarlo como una API funcional. Al terminar, tendrás un servicio que puede recibir datos de cualquier estudiante y devolver una predicción en tiempo real.

---

## Parte 1: Entrenar y guardar el modelo (20 minutos)

Usando el dataset `estudiantes.csv` (o el dataset generado en clase), entrena el mejor modelo que puedas y guárdalo correctamente.

### Requisitos:
1. Prueba al menos 2 modelos distintos (ej. Random Forest y Gradient Boosting)
2. Selecciona el que tenga mejor precisión en test set
3. Guarda el modelo Y el scaler con joblib
4. Documenta la precisión del modelo guardado

```python
# Estructura esperada de archivos:
# modelo_final.pkl    <- el modelo entrenado
# scaler_final.pkl    <- el StandardScaler ajustado
# modelo_info.txt     <- precisión, fecha de entrenamiento, parámetros
```

**Bonus:** Guarda también un archivo `modelo_info.json` con metadatos:
```json
{
    "modelo": "RandomForestClassifier",
    "precision_test": 0.875,
    "n_features": 4,
    "features": ["nota_matematicas", "nota_lengua", "asistencia", "edad"],
    "fecha_entrenamiento": "2026-04-28",
    "version_sklearn": "1.3.0"
}
```

---

## Parte 2: Función de predicción robusta (20 minutos)

Escribe una función `predecir_estudiante()` que incluya:
- Validación de tipos y rangos de los parámetros
- Manejo de errores con mensajes claros
- Retorno de predicción + probabilidad + nivel de confianza

```python
def predecir_estudiante(nota_matematicas, nota_lengua, asistencia, edad):
    """
    Completa esta función con:
    - Validación de que los parámetros están en rango válido
    - Transformación con el scaler guardado
    - Predicción con el modelo guardado
    - Retorno de un diccionario con la predicción completa
    
    Retorna:
    {
        'aprobado': True/False,
        'probabilidad': 0.847,
        'nivel_confianza': 'alta'/'media'/'baja',
        'mensaje': 'El estudiante tiene alta probabilidad de aprobar'
    }
    """
    pass
```

### Criterio de nivel de confianza:
- Alta: probabilidad > 0.80 o < 0.20
- Media: probabilidad entre 0.60-0.80 o 0.20-0.40
- Baja: probabilidad entre 0.40-0.60 (el modelo no está seguro)

---

## Parte 3: API Flask completa (30 minutos)

Crea un archivo `app.py` con una API que tenga los siguientes endpoints:

### Endpoints requeridos:

**GET `/health`**
```json
Respuesta: {"status": "ok", "modelo": "...", "versión": "1.0"}
```

**POST `/predict`**
```json
Entrada: {"nota_matematicas": 7.5, "nota_lengua": 6.8, "asistencia": 0.90, "edad": 23}
Respuesta: {"aprobado": true, "probabilidad": 0.847, "nivel_confianza": "alta", "mensaje": "..."}
```

**POST `/predict/batch`** (desafío extra)
```json
Entrada: {"estudiantes": [
    {"nota_matematicas": 7.5, "nota_lengua": 6.8, "asistencia": 0.90, "edad": 23},
    {"nota_matematicas": 4.2, "nota_lengua": 3.9, "asistencia": 0.60, "edad": 30}
]}
Respuesta: {"predicciones": [...], "total": 2, "aprobados": 1, "reprobados": 1}
```

### Requisitos de la API:
- Manejo de errores con códigos HTTP apropiados (400 para datos inválidos, 500 para errores internos)
- Validación de todos los campos de entrada
- Mensajes de error descriptivos

---

## Parte 4: Probar la API (10 minutos)

Escribe un script o notebook que pruebe todos los endpoints de tu API:

```python
import requests

# 1. Health check
# 2. Predicción válida (estudiante con buen rendimiento)
# 3. Predicción válida (estudiante en riesgo)
# 4. Manejo de campo faltante — ¿devuelve error 400?
# 5. Manejo de valor fuera de rango — ¿devuelve error 400?
# 6. Predicción batch (si implementaste el bonus)
```

Para cada caso, imprime:
- El status code HTTP recibido
- El JSON de respuesta
- Si el resultado es el esperado

---

## Parte 5: Reflexión (10 minutos)

Responde en 2-3 oraciones cada pregunta:

1. **Seguridad:** ¿Qué podría pasar si alguien envía datos maliciosos a tu API? ¿Cómo la protegerías?

2. **Escalabilidad:** Si 1000 usuarios enviaran predicciones al mismo tiempo, ¿tendría problemas tu API? ¿Qué cambiarías para soportar más tráfico?

3. **Mantenimiento:** El modelo fue entrenado hoy. En 6 meses, si la distribución de estudiantes cambia, ¿cómo sabrías que el modelo necesita reentrenamiento?

---

## Estructura de entrega esperada

```
tarea_clase30/
├── notebook_entrenamiento.ipynb  ← Parte 1 y 2
├── app.py                         ← Parte 3
├── test_api.ipynb                 ← Parte 4 y 5
├── modelo_final.pkl               ← Modelo guardado
├── scaler_final.pkl               ← Scaler guardado
└── modelo_info.json               ← Metadatos (bonus)
```

---

## Criterios de evaluación

| Criterio | Puntaje |
|----------|---------|
| Modelo entrenado y guardado correctamente | 20 pts |
| Función predecir_estudiante() con validación | 25 pts |
| API Flask con todos los endpoints | 30 pts |
| Tests de la API (casos válidos e inválidos) | 15 pts |
| Reflexión escrita | 10 pts |
| **Total** | **100 pts** |
| Endpoint `/predict/batch` (bonus) | +15 pts |
| Archivo `modelo_info.json` con metadatos (bonus) | +5 pts |

---

## Tips para el éxito

- Prueba la función de predicción antes de integrarla en Flask
- Corre el servidor Flask en una terminal separada mientras pruebas con el notebook
- Si hay un error, lee el traceback completo — Flask muestra mensajes de error muy descriptivos en modo `debug=True`
- Guarda el modelo Y el scaler — si olvidas el scaler, la API no va a funcionar correctamente
