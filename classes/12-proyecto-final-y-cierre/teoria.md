# Documento Teórico — Clase 12: Proyecto Final y Cierre del Bootcamp

> **Nivel:** Integrador · **Duración estimada de lectura:** 20 minutos

---

## 1. ¿Qué hace a un proyecto de Data Science profesional?

Un análisis de datos profesional no se mide solo por la precisión del modelo, sino por su **claridad, reproducibilidad y utilidad para el negocio**.

### 1.1 Los tres ejes de calidad

| Eje | Pregunta clave | Indicadores |
|---|---|---|
| **Técnico** | ¿El análisis es correcto y reproducible? | Código limpio, métricas correctas, sin data leakage |
| **Comunicación** | ¿Los resultados son comprensibles? | Visualizaciones claras, lenguaje accesible |
| **Negocio** | ¿El análisis genera valor real? | Recomendaciones concretas y accionables |

---

## 2. Estructura de un proyecto completo

### 2.1 Organización de archivos

```
📁 proyecto_ventas/
├── 📄 README.md              ← descripción del proyecto
├── 📁 datos/
│   ├── ventas_tienda.csv     ← datos originales (nunca modificar)
│   └── ventas_limpio.csv     ← versión procesada
├── 📁 notebooks/
│   ├── 01_exploracion.ipynb
│   ├── 02_limpieza.ipynb
│   └── 03_modelado.ipynb
├── 📁 src/
│   └── utils.py              ← funciones reutilizables
├── 📁 resultados/
│   ├── figura_correlaciones.png
│   └── modelo_final.pkl
└── requirements.txt
```

### 2.2 El notebook de análisis — estructura recomendada

```
Sección 1: Contexto y pregunta de negocio
Sección 2: Carga e inspección inicial de datos
Sección 3: Análisis Exploratorio (EDA)
Sección 4: Limpieza y transformación
Sección 5: Modelado y evaluación
Sección 6: Conclusiones e insights
Sección 7: Recomendaciones para el negocio
```

---

## 3. Análisis Exploratorio (EDA) completo

### 3.1 Checklist de EDA

```python
# Dimensiones
print(f"Filas: {df.shape[0]:,} | Columnas: {df.shape[1]}")

# Tipos de datos
print(df.dtypes)

# Valores nulos
null_info = pd.DataFrame({
    "nulos": df.isnull().sum(),
    "porcentaje": (df.isnull().sum() / len(df) * 100).round(2)
})
print(null_info[null_info["nulos"] > 0])

# Estadísticas descriptivas
print(df.describe().T)

# Duplicados
print(f"Filas duplicadas: {df.duplicated().sum()}")
```

### 3.2 Visualizaciones esenciales de EDA

```python
import matplotlib.pyplot as plt
import pandas as pd

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Análisis Exploratorio — Dataset Ventas", fontsize=14, fontweight="bold")

# 1. Distribución de la variable objetivo
axes[0, 0].hist(df["total_neto"], bins=20, color="#22c55e", edgecolor="white")
axes[0, 0].set_title("Distribución de ventas netas")
axes[0, 0].set_xlabel("Total neto ($)")

# 2. Ventas por sucursal
ventas_sucursal = df.groupby("sucursal")["total_neto"].sum().sort_values()
axes[0, 1].barh(ventas_sucursal.index, ventas_sucursal.values, color="#3b82f6")
axes[0, 1].set_title("Ventas totales por sucursal")
axes[0, 1].set_xlabel("Ventas ($)")

# 3. Correlaciones
numeric_df = df.select_dtypes(include="number")
corr = numeric_df.corr()
im = axes[1, 0].imshow(corr, cmap="RdYlGn", vmin=-1, vmax=1)
axes[1, 0].set_xticks(range(len(corr.columns)))
axes[1, 0].set_yticks(range(len(corr.columns)))
axes[1, 0].set_xticklabels(corr.columns, rotation=45, ha="right")
axes[1, 0].set_yticklabels(corr.columns)
axes[1, 0].set_title("Mapa de correlaciones")
plt.colorbar(im, ax=axes[1, 0])

# 4. Outliers
axes[1, 1].boxplot(
    [df[df["sucursal"] == s]["total_neto"] for s in df["sucursal"].unique()],
    labels=df["sucursal"].unique()
)
axes[1, 1].set_title("Distribución por sucursal (boxplot)")
axes[1, 1].set_ylabel("Total neto ($)")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("resultados/eda_completo.png", dpi=150, bbox_inches="tight")
plt.show()
```

---

## 4. Limpieza de datos — Guía práctica

### 4.1 Estrategias para valores nulos

| Tipo de columna | Porcentaje nulo | Estrategia recomendada |
|---|---|---|
| Numérica | < 5% | Imputar con mediana |
| Numérica | 5–30% | Imputar con mediana + crear flag |
| Numérica | > 30% | Evaluar eliminar columna |
| Categórica | < 10% | Imputar con moda o "Desconocido" |
| Categórica | > 10% | "Desconocido" como categoría propia |
| Fecha | Cualquiera | Investigar origen del nulo |

### 4.2 Código de limpieza documentada

```python
# BUENA PRÁCTICA: documentar cada decisión de limpieza

# 1. Eliminar duplicados exactos
n_antes = len(df)
df = df.drop_duplicates()
print(f"Duplicados eliminados: {n_antes - len(df)}")

# 2. Corregir tipos de datos
df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
df["descuento_pct"] = df["descuento_pct"].astype(float)

# 3. Imputar nulos numéricos con mediana
for col in ["descuento_pct", "precio_unitario"]:
    mediana = df[col].median()
    n_nulos = df[col].isnull().sum()
    df[col] = df[col].fillna(mediana)
    print(f"'{col}': {n_nulos} nulos imputados con mediana ({mediana:.2f})")

# 4. Crear variables derivadas
df["mes"] = df["fecha_venta"].dt.month
df["dia_semana"] = df["fecha_venta"].dt.dayofweek
df["total_bruto"] = df["unidades_vendidas"] * df["precio_unitario"]
df["total_neto"] = df["total_bruto"] * (1 - df["descuento_pct"] / 100)
```

---

## 5. Storytelling con datos

### 5.1 Estructura de un buen reporte

1. **Contexto:** ¿Qué problema resolvemos? ¿Para quién?
2. **Hallazgos:** Los 3–5 insights más importantes.
3. **Evidencia:** Las visualizaciones que los sustentan.
4. **Recomendaciones:** Acciones concretas para el negocio.
5. **Limitaciones:** Qué no puede decir este análisis.

### 5.2 Principios de visualización efectiva

| Principio | Aplicación |
|---|---|
| **Una idea, un gráfico** | No saturar con demasiada información |
| **Título descriptivo** | "Ventas caen 30% en Q3" en lugar de "Ventas por trimestre" |
| **Etiquetas legibles** | Ejes, unidades, leyendas siempre presentes |
| **Color con propósito** | Un color destaca, muchos confunden |
| **Audiencia no técnica** | Sin jerga, sin notación matemática |

### 5.3 Ejemplo de visualización comunicativa

```python
fig, ax = plt.subplots(figsize=(10, 5))

ventas_mes = df.groupby("mes")["total_neto"].sum() / 1_000_000

colores = ["#ef4444" if v < ventas_mes.mean() else "#22c55e" for v in ventas_mes]
bars = ax.bar(ventas_mes.index, ventas_mes.values, color=colores, edgecolor="white", linewidth=0.5)

ax.axhline(ventas_mes.mean(), color="white", linestyle="--", lw=1, alpha=0.5, label=f"Promedio: ${ventas_mes.mean():.1f}M")

# Etiquetas de valor en cada barra
for bar, val in zip(bars, ventas_mes.values):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f"${val:.1f}M", ha="center", va="bottom", fontsize=9, color="white")

ax.set_title("Ventas mensuales — Los meses rojos están bajo el promedio anual",
             fontsize=12, fontweight="bold", pad=15)
ax.set_xlabel("Mes")
ax.set_ylabel("Ventas (millones $)")
ax.set_xticks(range(1, 13))
ax.set_xticklabels(["Ene","Feb","Mar","Abr","May","Jun","Jul","Ago","Sep","Oct","Nov","Dic"])
ax.legend()
plt.tight_layout()
plt.show()
```

---

## 6. Cómo presentar un modelo de ML a audiencia no técnica

### 6.1 Traducción de métricas

| Métrica técnica | Traducción para negocio |
|---|---|
| F1 = 0.82 | "El modelo identifica correctamente 8 de cada 10 clientes en riesgo" |
| RMSE = $1.200 | "Nuestras predicciones de ventas se desvían en promedio $1.200" |
| Recall = 0.90 | "De cada 10 clientes que se irían, detectamos 9" |
| Precisión = 0.75 | "De cada 4 clientes que el modelo marca como riesgo, 3 realmente se van" |

### 6.2 Estructura de presentación de 5 minutos

```
00:00 – 00:30  ¿Qué problema resolvimos y por qué importa?
00:30 – 01:30  ¿Qué encontramos en los datos? (1 gráfico clave)
01:30 – 02:30  ¿Cómo funciona el modelo? (sin matemáticas)
02:30 – 03:30  ¿Qué tan bueno es? (métricas en lenguaje de negocio)
03:30 – 04:30  ¿Qué debería hacer el negocio con esto?
04:30 – 05:00  Limitaciones y próximos pasos
```

---

## 7. Lo que aprendiste en este bootcamp

| Clase | Habilidad | Herramienta |
|---|---|---|
| 01 | Variables, tipos, control de flujo | Python básico |
| 02 | Carga, limpieza, transformación | pandas |
| 03 | Exploración visual de datos | matplotlib, seaborn |
| 04 | Estadísticas descriptivas | pandas, statistics |
| 05 | Visualizaciones comunicativas | matplotlib avanzado |
| 06 | Texto, fechas, ingeniería de features | pandas, re |
| 07 | Proyecto guiado integrador | Todas las anteriores |
| 08 | Presentación de hallazgos | Storytelling |
| 09 | Machine Learning — regresión | scikit-learn |
| 10 | Clasificación y evaluación | scikit-learn |
| 11 | Pipelines y validación cruzada | scikit-learn |
| 12 | Proyecto final integrador | Todas las anteriores |

---

## 8. Próximos pasos recomendados

| Nivel | Recurso | Tiempo estimado |
|---|---|---|
| Práctica inmediata | Kaggle Learn (gratuito) | 2–4 semanas |
| Profundizar ML | "Hands-On ML" — Géron | 2–3 meses |
| Portfolio | 3 proyectos con datos reales en GitHub | 3–6 meses |
| Especialización | MLOps, Deep Learning, o NLP | 6–12 meses |
| Comunidad | Meetups de Data Science locales | Ongoing |

---

> **Mensaje final:** El análisis de datos es una habilidad que se construye proyecto a proyecto. Lo más importante no es saber todos los algoritmos, sino hacer las preguntas correctas y comunicar los hallazgos con claridad.
