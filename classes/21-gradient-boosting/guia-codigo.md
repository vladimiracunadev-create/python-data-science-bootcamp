# 💻 Guía de código — Clase 21: Gradient Boosting

> Walkthrough del código clave, bloque por bloque.

## Bloque 1: GradientBoostingClassifier y efecto del learning_rate

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("estudiantes.csv")
features = ["horas_estudio", "ausencias", "promedio_anterior", "edad"]
X = df[features]
y = df["aprobado"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Learning rate bajo: aprende despacio pero generaliza mejor
gbm_lento = GradientBoostingClassifier(
    n_estimators=200,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)
gbm_lento.fit(X_train, y_train)
print(f"LR=0.05 | Train: {gbm_lento.score(X_train, y_train):.4f} | Test: {gbm_lento.score(X_test, y_test):.4f}")

# Learning rate alto: aprende rápido pero puede sobreajustar
gbm_rapido = GradientBoostingClassifier(
    n_estimators=50,
    learning_rate=0.5,
    max_depth=3,
    random_state=42
)
gbm_rapido.fit(X_train, y_train)
print(f"LR=0.50 | Train: {gbm_rapido.score(X_train, y_train):.4f} | Test: {gbm_rapido.score(X_test, y_test):.4f}")
```

**¿Qué hace?** Entrena dos modelos con distinto `learning_rate` para mostrar el trade-off: learning rate bajo + más árboles suele generalizar mejor que learning rate alto + pocos árboles.

**¿Por qué así?** Cada árbol en boosting corrige una fracción del error del árbol anterior. Con `learning_rate=0.05`, cada corrección es pequeña y cuidadosa; con `0.5`, las correcciones son grandes y pueden sobrepasar el objetivo.

**Resultado esperado:** El modelo lento (`lr=0.05`) generalmente tendrá mejor accuracy en test aunque el entrenamiento sea idéntico o inferior en train.

---

## Bloque 2: Comparar 4 modelos en el mismo dataset

```python
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

modelos = {
    "Regresión Logística": LogisticRegression(max_iter=500),
    "Árbol de Decisión": DecisionTreeClassifier(max_depth=5, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, random_state=42)
}

resultados = {}
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)
    acc = accuracy_score(y_test, modelo.predict(X_test))
    resultados[nombre] = acc
    print(f"{nombre}: {acc:.4f}")

# Gráfico comparativo
plt.figure(figsize=(9, 4))
plt.barh(list(resultados.keys()), list(resultados.values()), color=["#4C72B0","#DD8452","#55A868","#C44E52"])
plt.xlabel("Accuracy en test")
plt.title("Comparación de modelos")
plt.xlim(0.5, 1.0)
for i, (k, v) in enumerate(resultados.items()):
    plt.text(v + 0.005, i, f"{v:.3f}", va="center")
plt.tight_layout()
plt.show()
```

**¿Qué hace?** Entrena los 4 modelos con la misma división train/test y los compara visualmente, facilitando la selección del mejor modelo para el problema.

**¿Por qué así?** Usar el mismo `X_train`, `X_test` garantiza una comparación justa. El gráfico de barras horizontales es más legible que vertical cuando los nombres son largos.

**Resultado esperado:** GBM y Random Forest deberían superar a LogReg y al árbol solo. La diferencia entre RF y GBM suele ser pequeña pero GBM generalmente gana.

---

## Bloque 3: XGBoost para retención de clientes

```python
from xgboost import XGBClassifier, plot_importance
import matplotlib.pyplot as plt

df_clientes = pd.read_csv("retencion_clientes.csv")
features_c = ["edad", "meses_cliente", "productos_contratados", "llamadas_soporte", "saldo_promedio"]
X_c = df_clientes[features_c]
y_c = df_clientes["se_da_de_baja"]

X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(X_c, y_c, test_size=0.2, random_state=42)

# Entrenar XGBoost
xgb = XGBClassifier(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4,
    use_label_encoder=False,
    eval_metric="logloss",
    random_state=42
)
xgb.fit(X_train_c, y_train_c)
print(f"XGBoost accuracy: {xgb.score(X_test_c, y_test_c):.4f}")

# Importancia de variables
plt.figure(figsize=(8, 4))
plot_importance(xgb, max_num_features=5, importance_type="gain")
plt.title("Top 5 variables más importantes — XGBoost")
plt.tight_layout()
plt.show()
```

**¿Qué hace?** Aplica XGBoost a un problema de retención de clientes y visualiza qué variables tienen mayor ganancia de información al hacer los splits en los árboles.

**¿Por qué así?** `importance_type="gain"` mide la ganancia promedio de cada variable al ser usada en un split, lo que es más informativo que contar frecuencia de uso (`weight`).

**Resultado esperado:** Un gráfico de barras con las 5 variables que más aportan a predecir la baja del cliente. Típicamente variables como `meses_cliente` o `llamadas_soporte` suelen tener alto impacto.

---

## ⚠️ Errores comunes y cómo resolverlos

| Error | Por qué ocurre | Solución |
|---|---|---|
| `XGBClassifier` da warning sobre `use_label_encoder` | Parámetro deprecado en versiones recientes de XGBoost | Agregar `use_label_encoder=False, eval_metric="logloss"` al constructor |
| GBM muy lento de entrenar | `n_estimators` muy alto o dataset grande | Usar `sklearn.ensemble.HistGradientBoostingClassifier` o LightGBM, que son mucho más rápidos |
| Train accuracy 100%, test mucho menor | Overfitting por `learning_rate` alto o `max_depth` grande | Reducir `learning_rate` a 0.05-0.1 y `max_depth` a 3-4 |
| XGBoost falla con variables categóricas | XGBoost no acepta strings como features | Aplicar `pd.get_dummies()` o `LabelEncoder` antes de entrenar |
