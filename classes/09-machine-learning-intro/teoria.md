# 🧠 Documento TeÃ³rico â€” Clase 09: IntroducciÃ³n al Machine Learning

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.


> **Nivel:** Intermedio Â· **DuraciÃ³n estimada de lectura:** 25â€“30 minutos

---

## 1. Â¿QuÃ© es el Machine Learning?

El Machine Learning (ML) es una rama de la inteligencia artificial que permite a los sistemas **aprender patrones a partir de datos** sin ser programados explÃ­citamente para cada tarea.

En lugar de escribir reglas como:
```
SI ventas > 500 Y descuento < 10% â†’ ENTONCES ganancia_alta
```

Un modelo de ML aprende estas reglas automÃ¡ticamente a partir de ejemplos histÃ³ricos.

### 1.1 ComparaciÃ³n: ProgramaciÃ³n tradicional vs ML

| Aspecto | ProgramaciÃ³n tradicional | Machine Learning |
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
- Predecir el precio de una vivienda (regresiÃ³n)
- Clasificar correos como spam / no spam (clasificaciÃ³n)
- Detectar fraude en transacciones (clasificaciÃ³n binaria)

**Proceso:**
```
Datos histÃ³ricos (X, y) â†’ Entrenamiento â†’ Modelo â†’ Predicciones (Å·)
```

### 2.2 Aprendizaje No Supervisado

No hay etiquetas. El algoritmo encuentra **estructura oculta** en los datos.

**Casos de uso:**
- SegmentaciÃ³n de clientes (clustering)
- ReducciÃ³n de dimensionalidad (PCA)
- DetecciÃ³n de anomalÃ­as

### 2.3 Aprendizaje por Refuerzo

Un agente aprende a tomar decisiones recibiendo **recompensas o penalizaciones**. Usado en robÃ³tica, juegos y sistemas de recomendaciÃ³n.

---

## 3. TerminologÃ­a fundamental

| TÃ©rmino | DefiniciÃ³n | Ejemplo |
|---|---|---|
| **Feature / X** | Variable de entrada del modelo | precio_unitario, unidades_vendidas |
| **Target / y** | Variable que queremos predecir | total_ventas |
| **Instancia** | Un ejemplo o fila del dataset | Una transacciÃ³n de venta |
| **Etiqueta** | El valor real del target para una instancia | $45.000 |
| **ParÃ¡metro** | Valor aprendido por el modelo | coeficiente de regresiÃ³n |
| **HiperparÃ¡metro** | ConfiguraciÃ³n previa al entrenamiento | profundidad mÃ¡xima del Ã¡rbol |
| **PredicciÃ³n / Å·** | Valor estimado por el modelo | $43.200 (estimado) |
| **Error / Residuo** | Diferencia entre real y estimado | $45.000 - $43.200 = $1.800 |

---

## 4. El flujo de trabajo de ML

```
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”   â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ ComprensiÃ³n â”‚ â†’ â”‚ ExploraciÃ³n  â”‚ â†’ â”‚ PreparaciÃ³n  â”‚ â†’ â”‚  Modelado    â”‚
â”‚ del problemaâ”‚   â”‚ de datos EDA â”‚   â”‚ de datos     â”‚   â”‚ y evaluaciÃ³n â”‚
â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜   â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
                                                                â†“
                                                    â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
                                                    â”‚ ComunicaciÃ³n de      â”‚
                                                    â”‚ resultados           â”‚
                                                    â””â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
```

### 4.1 DivisiÃ³n Train/Test

Para evaluar un modelo de forma honesta, debemos probarlo con datos que **nunca vio durante el entrenamiento**.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% para test
    random_state=42     # semilla para reproducibilidad
)
```

| Split | Uso | ProporciÃ³n tÃ­pica |
|---|---|---|
| Train | Entrenamiento del modelo | 70-80% |
| Validation | Ajuste de hiperparÃ¡metros | 10-15% |
| Test | EvaluaciÃ³n final (una sola vez) | 10-20% |

> âš ï¸ **Regla de oro:** el conjunto de test se toca **una sola vez**, al final. Usarlo mÃºltiples veces invalida la evaluaciÃ³n.

---

## 5. RegresiÃ³n Lineal

### 5.1 Â¿QuÃ© aprende?

La relaciÃ³n lineal entre features y target:

```
Å· = Î²â‚€ + Î²â‚Â·xâ‚ + Î²â‚‚Â·xâ‚‚ + ... + Î²â‚™Â·xâ‚™
```

Donde:
- `Î²â‚€` = intercepto (valor de Å· cuando todo X=0)
- `Î²â‚...Î²â‚™` = coeficientes (impacto de cada feature)

### 5.2 ImplementaciÃ³n en scikit-learn

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

### 5.3 MÃ©tricas de evaluaciÃ³n para regresiÃ³n

| MÃ©trica | FÃ³rmula | InterpretaciÃ³n | Unidades |
|---|---|---|---|
| **MAE** | mean(\|y - Å·\|) | Error promedio absoluto | Mismas que y |
| **MSE** | mean((y - Å·)Â²) | Error promedio cuadrÃ¡tico | yÂ² |
| **RMSE** | âˆšMSE | Penaliza errores grandes | Mismas que y |
| **RÂ²** | 1 - SS_res/SS_tot | % de varianza explicada | 0 a 1 (mÃ¡s alto = mejor) |

```python
from sklearn.metrics import mean_absolute_error, root_mean_squared_error, r2_score

mae  = mean_absolute_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2   = r2_score(y_test, y_pred)

print(f"MAE:  {mae:.2f}")
print(f"RMSE: {rmse:.2f}")
print(f"RÂ²:   {r2:.4f}")
```

---

## 6. La lÃ­nea base (Baseline)

Antes de celebrar el resultado del modelo, compÃ¡ralo contra una **predicciÃ³n trivial**:

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

Si el modelo no supera la lÃ­nea base, algo estÃ¡ mal (features incorrectas, data leakage, bug en el cÃ³digo).

---

## 7. VisualizaciÃ³n de resultados

### 7.1 GrÃ¡fico de predicciones vs. valores reales

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(y_test, y_pred, alpha=0.6, color="#22c55e", edgecolors="white", lw=0.5)

# LÃ­nea perfecta (predicciÃ³n ideal)
lims = [min(y_test.min(), y_pred.min()), max(y_test.max(), y_pred.max())]
ax.plot(lims, lims, "r--", lw=1.5, label="PredicciÃ³n perfecta")

ax.set_xlabel("Valor real")
ax.set_ylabel("PredicciÃ³n del modelo")
ax.set_title("Predicciones vs. Valores reales")
ax.legend()
plt.tight_layout()
plt.show()
```

### 7.2 DistribuciÃ³n de residuos

```python
residuos = y_test - y_pred
fig, axes = plt.subplots(1, 2, figsize=(12, 4))

axes[0].hist(residuos, bins=20, color="#3b82f6", edgecolor="white")
axes[0].axvline(0, color="red", linestyle="--")
axes[0].set_title("DistribuciÃ³n de residuos")
axes[0].set_xlabel("Error (real - predicho)")

axes[1].scatter(y_pred, residuos, alpha=0.5, color="#f59e0b")
axes[1].axhline(0, color="red", linestyle="--")
axes[1].set_title("Residuos vs. Predicciones")
axes[1].set_xlabel("PredicciÃ³n")
axes[1].set_ylabel("Residuo")

plt.tight_layout()
plt.show()
```

---

## 8. Errores frecuentes y cÃ³mo evitarlos

| Error | DescripciÃ³n | CÃ³mo evitarlo |
|---|---|---|
| **Data leakage** | InformaciÃ³n del futuro contamina el entrenamiento | Siempre aplicar el scaler SOLO al train |
| **Usar test para ajustar** | El test set se usa para tomar decisiones | Usar validation set o cross-validation |
| **Sin lÃ­nea base** | No saber si el modelo agrega valor real | Siempre calcular baseline |
| **MÃ©tricas sin contexto** | RMSE=500 Â¿es bueno? | Comparar con el rango de y_test |
| **Features irrelevantes** | Agregar columnas al azar | Analizar correlaciones primero |

---

## ✅ 9. Resumen rÃ¡pido

```
âœ… ML supervisado = aprender de ejemplos etiquetados
âœ… RegresiÃ³n = predecir un nÃºmero continuo
âœ… Train/Test split = evaluar honestamente
âœ… MAE, RMSE, RÂ² = mÃ©tricas de regresiÃ³n
âœ… Baseline = el mÃ­nimo que tu modelo debe superar
âœ… Residuos = diferencia entre real y predicciÃ³n
```

---

## 🔎 10. Recursos para profundizar

- DocumentaciÃ³n oficial scikit-learn: [scikit-learn.org](https://scikit-learn.org)
- "Hands-On Machine Learning" â€” AurÃ©lien GÃ©ron (CapÃ­tulos 1-4)
- Google ML Crash Course (gratuito)
- Kaggle Learn â€” Intro to Machine Learning
