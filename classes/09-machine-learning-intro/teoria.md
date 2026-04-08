# Documento Teórico — Clase 09: Introducción al Machine Learning

> **Nivel:** Intermedio · **Duración estimada de lectura:** 25–30 minutos

---

## 1. ¿Qué es el Machine Learning?

El Machine Learning (ML) es una rama de la inteligencia artificial que permite a los sistemas **aprender patrones a partir de datos** sin ser programados explícitamente para cada tarea.

En lugar de escribir reglas como:
```
SI ventas > 500 Y descuento < 10% → ENTONCES ganancia_alta
```

Un modelo de ML aprende estas reglas automáticamente a partir de ejemplos históricos.

### 1.1 Comparación: Programación tradicional vs ML

| Aspecto | Programación tradicional | Machine Learning |
|---|---|---|
| Entrada | Datos + Reglas | Datos + Respuestas esperadas |
| Salida | Respuestas | Reglas (modelo) |
| Mantenimiento | Actualizar reglas manualmente | Reentrenar con nuevos datos |
| Escalabilidad | Limitada por complejidad de reglas | Escala con volumen de datos |
| Interpretabilidad | Alta | Variable (depende del modelo) |

---

## 2. Tipos de Machine Learning

### 2.1 Aprendizaje Supervisado

El algoritmo aprende de datos **etiquetados**: cada ejemplo incluye la respuesta correcta.

**Casos de uso:**
- Predecir el precio de una vivienda (regresión)
- Clasificar correos como spam / no spam (clasificación)
- Detectar fraude en transacciones (clasificación binaria)

**Proceso:**
```
Datos históricos (X, y) → Entrenamiento → Modelo → Predicciones (ŷ)
```

### 2.2 Aprendizaje No Supervisado

No hay etiquetas. El algoritmo encuentra **estructura oculta** en los datos.

**Casos de uso:**
- Segmentación de clientes (clustering)
- Reducción de dimensionalidad (PCA)
- Detección de anomalías

### 2.3 Aprendizaje por Refuerzo

Un agente aprende a tomar decisiones recibiendo **recompensas o penalizaciones**. Usado en robótica, juegos y sistemas de recomendación.

---

## 3. Terminología fundamental

| Término | Definición | Ejemplo |
|---|---|---|
| **Feature / X** | Variable de entrada del modelo | precio_unitario, unidades_vendidas |
| **Target / y** | Variable que queremos predecir | total_ventas |
| **Instancia** | Un ejemplo o fila del dataset | Una transacción de venta |
| **Etiqueta** | El valor real del target para una instancia | $45.000 |
| **Parámetro** | Valor aprendido por el modelo | coeficiente de regresión |
| **Hiperparámetro** | Configuración previa al entrenamiento | profundidad máxima del árbol |
| **Predicción / ŷ** | Valor estimado por el modelo | $43.200 (estimado) |
| **Error / Residuo** | Diferencia entre real y estimado | $45.000 - $43.200 = $1.800 |

---

## 4. El flujo de trabajo de ML

```
┌─────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│ Comprensión │ → │ Exploración  │ → │ Preparación  │ → │  Modelado    │
│ del problema│   │ de datos EDA │   │ de datos     │   │ y evaluación │
└─────────────┘   └──────────────┘   └──────────────┘   └──────────────┘
                                                                ↓
                                                    ┌──────────────────────┐
                                                    │ Comunicación de      │
                                                    │ resultados           │
                                                    └──────────────────────┘
```

### 4.1 División Train/Test

Para evaluar un modelo de forma honesta, debemos probarlo con datos que **nunca vio durante el entrenamiento**.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% para test
    random_state=42     # semilla para reproducibilidad
)
```

| Split | Uso | Proporción típica |
|---|---|---|
| Train | Entrenamiento del modelo | 70-80% |
| Validation | Ajuste de hiperparámetros | 10-15% |
| Test | Evaluación final (una sola vez) | 10-20% |

> ⚠️ **Regla de oro:** el conjunto de test se toca **una sola vez**, al final. Usarlo múltiples veces invalida la evaluación.

---

## 5. Regresión Lineal

### 5.1 ¿Qué aprende?

La relación lineal entre features y target:

```
ŷ = β₀ + β₁·x₁ + β₂·x₂ + ... + βₙ·xₙ
```

Donde:
- `β₀` = intercepto (valor de ŷ cuando todo X=0)
- `β₁...βₙ` = coeficientes (impacto de cada feature)

### 5.2 Implementación en scikit-learn

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)        # aprende los coeficientes
y_pred = model.predict(X_test)    # genera predicciones

# Inspeccionar el modelo
print(f"Intercepto: {model.intercept_:.2f}")
for feat, coef in zip(feature_names, model.coef_):
    print(f"  {feat}: {coef:.4f}")
```

### 5.3 Métricas de evaluación para regresión

| Métrica | Fórmula | Interpretación | Unidades |
|---|---|---|---|
| **MAE** | mean(\|y - ŷ\|) | Error promedio absoluto | Mismas que y |
| **MSE** | mean((y - ŷ)²) | Error promedio cuadrático | y² |
| **RMSE** | √MSE | Penaliza errores grandes | Mismas que y |
| **R²** | 1 - SS_res/SS_tot | % de varianza explicada | 0 a 1 (más alto = mejor) |

```python
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

mae  = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2   = r2_score(y_test, y_pred)

print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"R²:   {r2:.4f}")
```

---

## 6. La línea base (Baseline)

Antes de celebrar el resultado del modelo, compáralo contra una **predicción trivial**:

```python
import numpy as np
from sklearn.metrics import mean_absolute_error

# Baseline: siempre predecir el promedio
baseline = np.full(len(y_test), y_train.mean())
baseline_mae = mean_absolute_error(y_test, baseline)
model_mae = mean_absolute_error(y_test, y_pred)

print(f"MAE Baseline: {baseline_mae:.2f}")
print(f"MAE Modelo:   {model_mae:.2f}")
print(f"Mejora:       {(1 - model_mae/baseline_mae)*100:.1f}%")
```

Si el modelo no supera la línea base, algo está mal (features incorrectas, data leakage, bug en el código).

---

## 7. Visualización de resultados

### 7.1 Gráfico de predicciones vs. valores reales

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_test, y_pred, alpha=0.6, color="#22c55e", edgecolors="white", lw=0.5)

# Línea perfecta (predicción ideal)
lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
ax.plot(lims, lims, "r--", lw=1.5, label="Predicción perfecta")

ax.set_xlabel("Valor real")
ax.set_ylabel("Predicción del modelo")
ax.set_title("Predicciones vs. Valores reales")
ax.legend()
plt.tight_layout()
plt.show()
```

### 7.2 Distribución de residuos

```python
residuos = y_test - y_pred
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(residuos, bins=20, color="#3b82f6", edgecolor="white")
axes[0].axvline(0, color="red", linestyle="--")
axes[0].set_title("Distribución de residuos")
axes[0].set_xlabel("Error (real - predicho)")

axes[1].scatter(y_pred, residuos, alpha=0.5, color="#f59e0b")
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set_title("Residuos vs. Predicciones")
axes[1].set_xlabel("Predicción")
axes[1].set_ylabel("Residuo")

plt.tight_layout()
plt.show()
```

---

## 8. Errores frecuentes y cómo evitarlos

| Error | Descripción | Cómo evitarlo |
|---|---|---|
| **Data leakage** | Información del futuro contamina el entrenamiento | Siempre aplicar el scaler SOLO al train |
| **Usar test para ajustar** | El test set se usa para tomar decisiones | Usar validation set o cross-validation |
| **Sin línea base** | No saber si el modelo agrega valor real | Siempre calcular baseline |
| **Métricas sin contexto** | RMSE=500 ¿es bueno? | Comparar con el rango de y_test |
| **Features irrelevantes** | Agregar columnas al azar | Analizar correlaciones primero |

---

## 9. Resumen rápido

```
✅ ML supervisado = aprender de ejemplos etiquetados
✅ Regresión = predecir un número continuo
✅ Train/Test split = evaluar honestamente
✅ MAE, RMSE, R² = métricas de regresión
✅ Baseline = el mínimo que tu modelo debe superar
✅ Residuos = diferencia entre real y predicción
```

---

## 10. Recursos para profundizar

- Documentación oficial scikit-learn: [scikit-learn.org](https://scikit-learn.org)
- "Hands-On Machine Learning" — Aurélien Géron (Capítulos 1-4)
- Google ML Crash Course (gratuito)
- Kaggle Learn — Intro to Machine Learning
