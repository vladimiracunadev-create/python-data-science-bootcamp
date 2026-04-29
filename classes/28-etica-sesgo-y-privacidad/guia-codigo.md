# 💻 Guía de código — Clase 28: Ética, Sesgo y Privacidad

> Explicación detallada del código clave, bloque por bloque.

## Bloque 1: Detectar sesgo en el dataset

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("estudiantes.csv")
print(df.head())
print(df.columns.tolist())

# Analizar tasas de aprobación por grupo demográfico
tasa_por_genero = df.groupby("genero")["aprobado"].mean()
print("\nTasa de aprobación por género:")
print(tasa_por_genero)

# Analizar distribución de características por grupo
print("\nPromedio de horas de estudio por género:")
print(df.groupby("genero")["horas_estudio"].mean())

# Visualizar distribuciones para detectar desigualdades
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Tasa de aprobación por género
tasa_por_genero.plot(kind="bar", ax=axes[0], color=["steelblue", "salmon"])
axes[0].set_title("Tasa de aprobación por género")
axes[0].set_ylabel("Proporción de aprobados")
axes[0].set_ylim(0, 1)
axes[0].axhline(y=df["aprobado"].mean(), color="red", linestyle="--", label="Promedio global")
axes[0].legend()

# Distribución de notas por género
df.boxplot(column="nota_final", by="genero", ax=axes[1])
axes[1].set_title("Distribución de notas por género")
axes[1].set_xlabel("Género")
axes[1].set_ylabel("Nota final")
plt.suptitle("")  # eliminar título automático de boxplot

plt.tight_layout()
plt.show()
```

**¿Qué hace este bloque?** Analiza si existen disparidades en las tasas de aprobación entre grupos del dataset. Muestra las medias por grupo y las visualiza para identificar inequidades de manera intuitiva.

**¿Por qué se escribe así?** El análisis de sesgo comienza siempre con exploración de datos desagregada por grupo. La línea roja punteada (`.axhline`) marca el promedio global, lo que facilita ver qué grupos están por encima o por debajo. Este análisis no implica causalidad: puede haber factores legítimos o ilegítimos detrás de las diferencias.

**Resultado esperado:** Si existen disparidades significativas entre grupos, aparecerán visualmente como barras de diferente altura. Una diferencia del 10% o más en tasas de aprobación entre grupos es una señal de alerta que merece investigación.

---

## Bloque 2: Evaluar equidad del modelo por grupos

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# Entrenar un modelo
X = df.drop(columns=["aprobado", "nombre", "id_estudiante"])
y = df["aprobado"]

# Guardar la columna de género para el análisis de equidad (ANTES de eliminarla del modelo)
genero = df["genero"]

X_train, X_test, y_train, y_test, genero_train, genero_test = train_test_split(
    X, y, genero, test_size=0.2, random_state=42
)

# Eliminar género del entrenamiento (no queremos que el modelo use esta variable)
X_train_sin_genero = X_train.drop(columns=["genero"], errors="ignore")
X_test_sin_genero = X_test.drop(columns=["genero"], errors="ignore")

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train_sin_genero, y_train)

y_pred = modelo.predict(X_test_sin_genero)

# Evaluar el rendimiento POR GRUPO
print("=== Evaluación global ===")
print(classification_report(y_test, y_pred))

for grupo in genero_test.unique():
    mascara = genero_test == grupo
    y_test_grupo = y_test[mascara]
    y_pred_grupo = y_pred[mascara]
    
    accuracy_grupo = (y_test_grupo == y_pred_grupo).mean()
    print(f"\n=== Grupo: {grupo} (n={mascara.sum()}) ===")
    print(f"Accuracy: {accuracy_grupo:.3f}")
    print(classification_report(y_test_grupo, y_pred_grupo))
```

**¿Qué hace este bloque?** Entrena el modelo sin usar la variable de género como predictor, pero luego evalúa su rendimiento separadamente para cada grupo. Este es el análisis de equidad fundamental: medir si el modelo tiene el mismo rendimiento para todos los grupos.

**¿Por qué se escribe así?** Eliminar la variable protegida (género) del modelo no garantiza la equidad: el modelo puede aprender sesgos indirectamente a través de otras variables correlacionadas (por ejemplo, tipo de carrera o número de extracurriculares). Por eso es esencial evaluar el rendimiento por grupo después del entrenamiento.

**Resultado esperado:** Si el modelo es equitativo, los accuracy y F1-scores por grupo serán similares. Una diferencia de más del 10% en accuracy entre grupos es una señal de sesgo algorítmico que debe reportarse y mitigarse.

---

## Bloque 3: Explicabilidad con SHAP

```python
# pip install shap  (si no está instalado)
import shap

# Crear explainer para el modelo de Random Forest
explainer = shap.TreeExplainer(modelo)

# Calcular valores SHAP para el conjunto de test
# (puede tardar unos segundos con datasets grandes)
shap_values = explainer.shap_values(X_test_sin_genero)

# Si es clasificación binaria, shap_values es una lista [clase_0, clase_1]
# Usamos la clase 1 (aprobado)
shap_values_clase1 = shap_values[1] if isinstance(shap_values, list) else shap_values

# Gráfico 1: Importancia global de variables
print("Generando summary plot (importancia global)...")
shap.summary_plot(shap_values_clase1, X_test_sin_genero,
                  plot_type="bar", show=True)

# Gráfico 2: Dirección del impacto de cada variable
print("Generando summary plot (dirección de impacto)...")
shap.summary_plot(shap_values_clase1, X_test_sin_genero, show=True)

# Explicar UNA predicción individual
idx = 0  # primer estudiante del test
print(f"\nExplicando predicción para estudiante {idx}:")
print(f"Predicción: {'Aprobado' if y_pred[idx] == 1 else 'Reprobado'}")
print(f"Valor real: {'Aprobado' if y_test.iloc[idx] == 1 else 'Reprobado'}")

shap.waterfall_plot(
    shap.Explanation(
        values=shap_values_clase1[idx],
        base_values=explainer.expected_value[1] if isinstance(explainer.expected_value, list) else explainer.expected_value,
        data=X_test_sin_genero.iloc[idx],
        feature_names=X_test_sin_genero.columns.tolist()
    )
)
```

**¿Qué hace este bloque?** Calcula los valores SHAP (SHapley Additive exPlanations) para cada predicción. SHAP mide cuánto contribuyó cada variable a empujar la predicción por encima o por debajo del valor base (la predicción promedio del modelo). Genera dos gráficos: uno de importancia global y uno de dirección de impacto.

**¿Por qué se escribe así?** `TreeExplainer` es el más rápido para modelos basados en árboles (Random Forest, XGBoost, etc.). El `summary_plot` con `plot_type="bar"` muestra cuáles son las variables más importantes globalmente. El `waterfall_plot` explica una predicción individual: "este estudiante fue predicho como reprobado principalmente porque estudió pocas horas y faltó a muchas clases".

**Resultado esperado:** Una visualización donde cada punto del gráfico es un estudiante del test. Los colores muestran si el valor de la variable era alto (rojo) o bajo (azul), y la posición horizontal muestra si esa variable empujó la predicción hacia "aprobado" (+) o "reprobado" (-). Esto permite explicar las decisiones del modelo de manera transparente.

---

## Bloque 4: Anonimizar datos antes de compartir

```python
import hashlib
import random

# Cargar datos con información sensible
df_original = pd.read_csv("estudiantes.csv")

# Método 1: Eliminar columnas identificadoras directamente
df_anonimizado = df_original.drop(columns=["nombre", "email", "telefono",
                                            "dni", "direccion"], errors="ignore")

# Método 2: Pseudoanonimizar (reemplazar por hash irreversible)
def hash_id(valor):
    """Genera un identificador pseudoanónimo irreversible."""
    return hashlib.sha256(str(valor).encode()).hexdigest()[:12]

if "id_estudiante" in df_original.columns:
    df_anonimizado["id_anonimo"] = df_original["id_estudiante"].apply(hash_id)

# Método 3: Generalizar valores numéricos en rangos
if "edad" in df_original.columns:
    df_anonimizado["rango_edad"] = pd.cut(
        df_original["edad"],
        bins=[0, 18, 25, 35, 50, 100],
        labels=["<18", "18-25", "25-35", "35-50", "50+"]
    )
    df_anonimizado = df_anonimizado.drop(columns=["edad"], errors="ignore")

# Método 4: Añadir ruido diferencial a columnas numéricas sensibles
def ruido_diferencial(serie, epsilon=1.0):
    """Añade ruido laplaciano para privacidad diferencial básica."""
    sensibilidad = serie.max() - serie.min()
    escala = sensibilidad / epsilon
    ruido = np.random.laplace(0, escala, len(serie))
    return serie + ruido

# Verificar que no queden datos identificables
print("Columnas en dataset anonimizado:")
print(df_anonimizado.columns.tolist())
print(f"\nForma original: {df_original.shape}")
print(f"Forma anonimizada: {df_anonimizado.shape}")

# Guardar dataset anonimizado
df_anonimizado.to_csv("estudiantes_anonimizado.csv", index=False)
print("\nDataset anonimizado guardado.")
```

**¿Qué hace este bloque?** Aplica cuatro técnicas de anonimización: eliminación directa de columnas identificadoras, pseudoanonimización con hash irreversible (el ID original no se puede recuperar desde el hash), generalización de datos precisos en rangos (edad exacta → rango de edad), y una introducción conceptual al ruido diferencial.

**¿Por qué se escribe así?** El RGPD exige proteger los datos personales antes de compartirlos o publicarlos. SHA-256 produce un hash determinístico (el mismo ID siempre genera el mismo hash), lo que permite hacer seguimiento interno sin exponer el dato original. `pd.cut()` convierte edades exactas en rangos, reduciendo el riesgo de reidentificación combinando múltiples variables.

**Resultado esperado:** Un archivo CSV sin columnas identificadoras, con IDs anónimos y edades en rangos. Este dataset puede compartirse con otros equipos o publicarse con menor riesgo de vulnerar la privacidad de los estudiantes.

---

## Errores comunes y cómo resolverlos

| Error | Causa | Solución |
|---|---|---|
| SHAP tarda demasiado | Dataset muy grande o modelo con muchos estimadores | Usar una muestra: `shap_values = explainer.shap_values(X_test_sin_genero.sample(100))` |
| `ImportError: No module named 'shap'` | SHAP no está instalado | Ejecutar `pip install shap` en la terminal |
| El modelo tiene alta accuracy pero baja equidad | El dataset de entrenamiento refleja desigualdades históricas | Usar `class_weight='balanced'` o remuestrear para equilibrar grupos |
| El análisis por grupo tiene muy pocos datos | Grupo minoritario con pocos ejemplos en test | Reportar la limitación e interpretar con cautela; buscar más datos de ese grupo |
| Hash no es suficiente para anonimizar | Con pocos datos únicos, se puede reidentificar por combinación de variables | Usar k-anonimato o privacidad diferencial para datasets pequeños |
| SHAP values no suman al prediction | Diferencia de versiones entre SHAP y sklearn | Actualizar ambas librerías a versiones compatibles |
