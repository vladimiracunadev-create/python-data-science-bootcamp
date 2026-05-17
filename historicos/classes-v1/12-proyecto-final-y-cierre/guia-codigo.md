# 💻 Guía de código — Clase 12: Proyecto final y cierre

> Walkthrough detallado del código clave de esta clase, bloque por bloque.

## Bloque 1: Carga, exploración y formulación de la pregunta

```python
import pandas as pd

# 1. Cargar los datos y hacer una copia de trabajo para no modificar el original.
df = pd.read_csv("datasets/ventas_tienda.csv")
trabajo = df.copy()

# 2. Exploración inicial: dimensión, tipos y valores nulos.
print("Dimensiones:", trabajo.shape)
print("\nTipos de datos:")
print(trabajo.dtypes)
print("\nValores nulos por columna:")
print(trabajo.isnull().sum())
print("\nPrimeras filas:")
print(trabajo.head())

# 3. Formular la pregunta antes de seguir explorando.
# Esta línea actúa como ancla conceptual: todo el análisis responde a esta pregunta.
pregunta = "¿Qué sucursal conviene reforzar en la próxima campaña de ventas?"
print(f"\n→ Pregunta del proyecto: {pregunta}")
```

**¿Qué hace este bloque?**
Establece la base del proyecto: carga los datos, hace una exploración mínima para entender su estructura, y formula la pregunta de negocio antes de construir variables o entrenar modelos. Trabajar sobre una copia previene modificaciones accidentales del dataset original.

**¿Por qué se escribe así y no de otra forma?**
Escribir la pregunta como variable de texto (`pregunta = "..."`) obliga a hacerla explícita en el notebook. Un proyecto sin pregunta formulada tiende a derivar hacia análisis sin dirección. La exploración inicial evita sorpresas tardías (nulos, tipos incorrectos) que rompan el flujo.

**Resultado esperado:**
```
Dimensiones: (1200, 7)

Tipos de datos:
sucursal            object
fecha               object
producto            object
unidades             int64
precio_unitario    float64
descuento_pct      float64
region              object

Valores nulos por columna:
sucursal           0
fecha              0
producto           3
unidades           0
precio_unitario    0
descuento_pct      8
region             0

→ Pregunta del proyecto: ¿Qué sucursal conviene reforzar en la próxima campaña de ventas?
```

---

## Bloque 2: Limpieza y construcción de variables relevantes

```python
import numpy as np

# 1. Imputar valores nulos antes de calcular variables derivadas.
# descuento_pct nulo se interpreta como sin descuento (0 %).
trabajo["descuento_pct"] = trabajo["descuento_pct"].fillna(0.0)

# producto nulo: imputar con "Desconocido" para no perder la fila completa.
trabajo["producto"] = trabajo["producto"].fillna("Desconocido")

# 2. Convertir fecha al tipo correcto para poder extraer períodos.
trabajo["fecha"] = pd.to_datetime(trabajo["fecha"])
trabajo["mes"] = trabajo["fecha"].dt.month
trabajo["trimestre"] = trabajo["fecha"].dt.quarter

# 3. Construir la variable objetivo del análisis: ingreso neto por venta.
trabajo["total_neto"] = (
    trabajo["unidades"]
    * trabajo["precio_unitario"]
    * (1 - trabajo["descuento_pct"])
)

print("Variables tras limpieza:")
print(trabajo[["sucursal", "mes", "trimestre", "total_neto"]].head())
print(f"\nRango de total_neto: ${trabajo['total_neto'].min():,.0f} – ${trabajo['total_neto'].max():,.0f}")
```

**¿Qué hace este bloque?**
Trata los valores nulos con criterio (no simplemente los elimina), convierte fechas a tipo correcto para poder extraer información temporal, y calcula la variable central del análisis (`total_neto`). Cada decisión de limpieza debe estar justificada.

**¿Por qué se escribe así y no de otra forma?**
Imputar `descuento_pct` con 0 en lugar de con la media evita inflar artificialmente los descuentos donde no los hubo. Construir `mes` y `trimestre` desde la fecha es más seguro que trabajar con strings de fecha en filtros y agrupaciones.

**Resultado esperado:**
```
Variables tras limpieza:
  sucursal  mes  trimestre  total_neto
0   Norte     1          1     4750.00
1     Sur     1          1     3200.00
2   Norte     2          1     6100.00
3    Este     1          1     2890.00
4   Norte     2          1     5430.00

Rango de total_neto: $580 – $48,200
```

---

## Bloque 3: Análisis exploratorio orientado a la pregunta

```python
import matplotlib.pyplot as plt

# Agrupamos por sucursal para responder la pregunta directamente.
resumen_sucursal = (
    trabajo.groupby("sucursal", as_index=False)
    .agg(
        total_ventas=("total_neto", "sum"),
        ticket_promedio=("total_neto", "mean"),
        num_transacciones=("total_neto", "count")
    )
    .sort_values("total_ventas", ascending=False)
)

print("Resumen por sucursal:")
print(resumen_sucursal.to_string(index=False))

# Gráfico de barras: fácil de leer y defender en una presentación.
fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(resumen_sucursal["sucursal"], resumen_sucursal["total_ventas"] / 1e6,
       color=["#2196F3", "#FF9800", "#4CAF50", "#F44336"])
ax.set_xlabel("Sucursal")
ax.set_ylabel("Ventas totales (millones $)")
ax.set_title("Ventas por sucursal — período completo")
plt.tight_layout()
plt.show()

# Identificar la sucursal con menor rendimiento para la recomendación.
peor_sucursal = resumen_sucursal.iloc[-1]["sucursal"]
print(f"\n→ Sucursal con menor desempeño: {peor_sucursal}")
```

**¿Qué hace este bloque?**
Responde la pregunta formulada en el bloque 1 con un análisis de agrupación. El gráfico de barras hace la evidencia visible e inmediatamente comunicable. Terminar con una variable (`peor_sucursal`) que nombra la conclusión conecta el análisis con la recomendación final.

**¿Por qué se escribe así y no de otra forma?**
Un EDA orientado a una pregunta produce una conclusión. Un EDA sin pregunta produce observaciones sin dirección. El gráfico usa colores distintos por sucursal para que sea legible incluso en blanco y negro.

**Resultado esperado:**
```
Resumen por sucursal:
 sucursal  total_ventas  ticket_promedio  num_transacciones
    Norte    2150000.00          5375.00                400
     Este    1830000.00          4575.00                400
      Sur    1490000.00          3725.00                400
    Oeste     980000.00          2450.00                400

→ Sucursal con menor desempeño: Oeste
```

---

## Bloque 4: Pipeline de clasificación y evaluación final

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import classification_report
import pandas as pd

# Definir si una transacción es de "alto valor" (por encima del percentil 75).
umbral = trabajo["total_neto"].quantile(0.75)
trabajo["transaccion_alta"] = (trabajo["total_neto"] >= umbral).astype(int)

# Variables de entrada: numéricas disponibles antes de conocer el resultado.
# No incluimos total_neto (sería leakage: ya contiene la información de la etiqueta).
X_final = trabajo[["unidades", "precio_unitario", "descuento_pct", "mes", "trimestre"]]
y_final = trabajo["transaccion_alta"]

# Pipeline completo: estandarización + modelo de bosque aleatorio.
pipeline_final = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42))
])

# Validación cruzada para un score honesto.
scores = cross_val_score(pipeline_final, X_final, y_final, cv=5, scoring="f1")
print(f"F1 medio (validación cruzada 5-fold): {scores.mean():.3f} ± {scores.std():.3f}")

# Entrenamiento final y reporte en conjunto de prueba.
X_tr, X_te, y_tr, y_te = train_test_split(
    X_final, y_final, test_size=0.2, random_state=42, stratify=y_final
)
pipeline_final.fit(X_tr, y_tr)
print("\nReporte final:")
print(classification_report(y_te, pipeline_final.predict(X_te)))

# Importancia de variables del bosque.
rf = pipeline_final.named_steps["model"]
importancias = pd.Series(rf.feature_importances_, index=X_final.columns)
print("Importancia de variables:")
print(importancias.sort_values(ascending=False).round(3))
```

**¿Qué hace este bloque?**
Cierra el ciclo completo del proyecto: define la etiqueta, construye el pipeline con un modelo más robusto (Random Forest), lo valida de forma rigurosa con validación cruzada, y genera evidencia de qué variables explican mejor las transacciones de alto valor.

**¿Por qué se escribe así y no de otra forma?**
Usar `quantile(0.75)` para definir el umbral de "alto valor" es una decisión basada en los propios datos (no arbitraria). Mostrar la importancia de variables permite comunicar los hallazgos del modelo a una audiencia no técnica: "el precio unitario y los descuentos son los principales determinantes de una transacción de alto valor".

**Resultado esperado:**
```
F1 medio (validación cruzada 5-fold): 0.821 ± 0.018

Reporte final:
              precisión  recall  f1-score  support
           0       0.87    0.89      0.88      181
           1       0.73    0.70      0.71       59

    accuracy                         0.84      240

Importancia de variables:
precio_unitario    0.412
descuento_pct      0.281
unidades           0.178
mes                0.083
trimestre          0.046
```

---

## ⚠️ Errores comunes y cómo resolverlos

| Error típico | Por qué ocurre | Cómo solucionarlo |
|---|---|---|
| Incluir `total_neto` en X al predecir `transaccion_alta` | Es leakage directo: la etiqueta se deriva de `total_neto` | Nunca incluir en X variables que sean transformaciones directas de y |
| Notebook desorganizado: código sin contexto narrativo | El notebook creció sin estructura y es difícil de defender | Reorganizar en secciones: Pregunta → Datos → EDA → Modelo → Conclusión |
| Modelo con score alto pero conclusión vaga | El modelo funciona pero no conecta con la pregunta de negocio | Terminar siempre con una respuesta explícita a la pregunta formulada en el bloque 1 |
| `ValueError: could not convert string to float` en el pipeline | Hay columnas categóricas (como `sucursal`) en X que el modelo no puede procesar | Codificar variables categóricas con `OneHotEncoder` dentro del pipeline antes del modelo |
| Diferencia grande entre score de CV y score en test final | El conjunto de prueba tiene una distribución muy diferente al entrenamiento | Verificar que se usó `stratify=y` en el split y que no hubo leakage en la preparación de X |
