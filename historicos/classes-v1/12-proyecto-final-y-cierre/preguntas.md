# ❓ Preguntas de evaluación — Clase 12: Proyecto final y cierre

> Preguntas para verificar comprensión al cierre de la clase o en evaluaciones formativas.

## 🧠 Preguntas conceptuales

1. ¿Qué hace que un notebook de proyecto final sea "defendible"? ¿Qué elementos mínimos debería tener para que un tercero lo entienda sin explicación verbal?
2. ¿Por qué es importante formular la pregunta de negocio antes de explorar los datos, y no después de ver los resultados?
3. ¿Qué diferencia hay entre un EDA descriptivo y uno orientado a una pregunta específica? ¿Cuál es más útil en un proyecto final?
4. ¿Por qué limpiar los datos antes de dividir en train/test puede introducir leakage? ¿Qué pasos de limpieza son seguros hacerlos fuera del pipeline?
5. Al presentar los resultados de un modelo, ¿qué información mínima deberías mostrar para que el oyente pueda juzgar si el modelo es confiable?

## 💻 Preguntas de código

1. ¿Qué hace cada línea de este bloque y por qué es importante hacer una copia antes de transformar?

```python
df = pd.read_csv("datasets/ventas_tienda.csv")
trabajo = df.copy()
trabajo["total_neto"] = trabajo["unidades"] * trabajo["precio_unitario"] * (1 - trabajo["descuento_pct"])
```

2. El siguiente pipeline va a entrenarse con datos que tienen valores nulos. ¿Qué paso falta y dónde deberías agregarlo?

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LogisticRegression())
])
pipeline.fit(X_train, y_train)
```

3. ¿Qué aporta esta visualización al proyecto final y cómo la conectarías con la conclusión?

```python
import matplotlib.pyplot as plt
importancias = pd.Series(modelo.feature_importances_, index=X.columns)
importancias.sort_values().plot(kind="barh")
plt.title("Importancia de variables")
plt.tight_layout()
plt.show()
```

## 🔗 Preguntas integradoras

1. Terminaste el proyecto y tu modelo tiene un F1 de 0.76. Tu compañero tiene un modelo con F1 de 0.81 pero no puede explicar qué variables usa ni por qué. ¿Cuál presentarías y qué argumentos darías?
2. ¿Cómo comunicarías los resultados de tu proyecto a alguien que no sabe de machine learning? ¿Qué mostrarías primero: el código, las métricas o la conclusión del negocio?
3. ¿Qué haría que tu proyecto final fallara en producción aunque haya funcionado bien en el notebook? Lista al menos tres escenarios concretos.
