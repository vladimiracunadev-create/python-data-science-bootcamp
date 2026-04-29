# 🧠 Documento teórico — Clase 21: Gradient Boosting — modelos potentes

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

El Gradient Boosting construye cada árbol para corregir los errores del anterior, logrando una de las mayores precisiones disponibles para datos tabulares.

## ❓ Por qué importa este módulo

Gradient Boosting es consistentemente el algoritmo más ganador en competencias de machine learning con datos tabulares (Kaggle, KDD, etc.). Entender su intuición permite usarlo con criterio y afinar sus parámetros con confianza.

## 📖 Conceptos clave

### Boosting vs Bagging

| Característica | Random Forest (Bagging) | Gradient Boosting |
|---|---|---|
| Construcción | Paralela (árboles independientes) | Secuencial (cada árbol aprende del error anterior) |
| Objetivo de cada árbol | Predecir la etiqueta directamente | Corregir los residuos del modelo anterior |
| Fortaleza | Reduce varianza (menos sobreajuste) | Reduce sesgo (más precisión) |
| Sensibilidad al ruido | Baja | Media-alta |

### Intuición del proceso de boosting
Imagina que eres estudiante y tienes el resultado de un examen con los errores marcados:
1. El primer árbol hace su mejor predicción (comete errores).
2. El segundo árbol solo mira los errores del primero y aprende a corregirlos.
3. El tercero corrige los errores que aún quedaban del segundo.
4. Y así sucesivamente hasta `n_estimators` árboles.

La predicción final es la suma acumulada de todos los árboles: cada uno aporta un pequeño ajuste.

### Parámetros clave

**`n_estimators`** — número de árboles a construir.
- Más árboles = más capacidad de aprender, pero también más tiempo y riesgo de sobreajuste.

**`learning_rate`** — qué tan grande es el "paso" de corrección de cada árbol.
- **Analogía:** bajar una colina a oscuras. Si das pasos muy grandes (learning_rate alto), puedes caerte (sobreajuste). Si das pasos muy pequeños (learning_rate bajo), tardas más pero llegas con más seguridad.
- Regla práctica: reducir `learning_rate` y aumentar `n_estimators` juntos suele mejorar el resultado.

**`max_depth`** — profundidad máxima de cada árbol individual.
- Los árboles en GBM suelen ser poco profundos (max_depth=3 a 5) para evitar memorizar.

### XGBoost
XGBoost ("Extreme Gradient Boosting") es una librería externa que implementa el mismo concepto de boosting pero con optimizaciones computacionales importantes:
- Regularización incorporada (penaliza la complejidad).
- Manejo nativo de valores nulos.
- Paralelización interna para mayor velocidad.
- API compatible con sklearn (mismos métodos `fit`, `predict`, `score`).

```python
import xgboost as xgb
modelo_xgb = xgb.XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=3)
modelo_xgb.fit(X_train, y_train)
```

### ¿Cuándo usar Gradient Boosting?
- Datos tabulares estructurados (filas y columnas).
- Cuando Random Forest no alcanza la precisión requerida.
- Cuando se tiene tiempo para afinar hiperparámetros.
- **No es ideal para:** imágenes, texto crudo, audio (para eso existen redes neuronales).

## 💻 Bloque de código documentado

### GradientBoostingClassifier básico

**Qué hace:** entrenar GBM → comparar con árbol y bosque → imprimir resultados

**Para qué sirve:** mostrar la ganancia de precisión del GBM frente a modelos más simples.

```python
# Qué hace: entrenar GradientBoostingClassifier y comparar con modelos anteriores.
# Para qué sirve: ver la mejora real en accuracy al pasar de árbol a bosque a boosting.
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("datasets/estudiantes.csv")
df["estado"] = ((df["evaluacion_python"] >= 60) & (df["asistencia_pct"] >= 70)).astype(int)

X = df[["asistencia_pct", "evaluacion_python", "evaluacion_pandas", "edad"]]
y = df["estado"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

modelos = {
    "Regresión Logística": LogisticRegression(max_iter=1000),
    "Árbol (d=3)":         DecisionTreeClassifier(max_depth=3, random_state=42),
    "Random Forest":       RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
    "Gradient Boosting":   GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
}

for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    acc = modelo.score(X_test, y_test)
    print(f"{nombre:25s}: {acc:.3f}")
```

## ⚠️ Errores frecuentes a vigilar

- Usar `learning_rate` muy alto (> 0.5) esperando aprender más rápido: suele sobreajustar.
- No instalar xgboost antes de importarlo (`pip install xgboost`).
- Comparar modelos en el conjunto de entrenamiento en lugar del test.

## 🔗 Conexión con el siguiente módulo

Con Gradient Boosting completamos el arsenal de modelos supervisados para datos tabulares. Los próximos pasos del bootcamp pueden incluir selección automática de hiperparámetros (GridSearchCV, Optuna) o el desarrollo del proyecto final integrador.
