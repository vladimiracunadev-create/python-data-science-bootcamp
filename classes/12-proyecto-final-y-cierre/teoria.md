# 🧠 Documento TeÃ³rico â€” Clase 12: Proyecto Final y Cierre del Bootcamp

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.


> **Nivel:** Integrador Â· **DuraciÃ³n estimada de lectura:** 20 minutos

---

## 1. Â¿QuÃ© hace a un proyecto de Data Science profesional?

Un anÃ¡lisis de datos profesional no se mide solo por la precisiÃ³n del modelo, sino por su **claridad, reproducibilidad y utilidad para el negocio**.

### 1.1 Los tres ejes de calidad

| Eje | Pregunta clave | Indicadores |
|---|---|---|
| **TÃ©cnico** | Â¿El anÃ¡lisis es correcto y reproducible? | CÃ³digo limpio, mÃ©tricas correctas, sin data leakage |
| **ComunicaciÃ³n** | Â¿Los resultados son comprensibles? | Visualizaciones claras, lenguaje accesible |
| **Negocio** | Â¿El anÃ¡lisis genera valor real? | Recomendaciones concretas y accionables |

---

## 2. Estructura de un proyecto completo

### 2.1 OrganizaciÃ³n de archivos

```
ðŸ“ proyecto_ventas/
â”œâ”€â”€ ðŸ“„ README.md              â† descripciÃ³n del proyecto
â”œâ”€â”€ ðŸ“ datos/
â”‚   â”œâ”€â”€ ventas_tienda.csv     â† datos originales (nunca modificar)
â”‚   â””â”€â”€ ventas_limpio.csv     â† versiÃ³n procesada
â”œâ”€â”€ ðŸ“ notebooks/
â”‚   â”œâ”€â”€ 01_exploracion.ipynb
â”‚   â”œâ”€â”€ 02_limpieza.ipynb
â”‚   â””â”€â”€ 03_modelado.ipynb
â”œâ”€â”€ ðŸ“ src/
â”‚   â””â”€â”€ utils.py              â† funciones reutilizables
â”œâ”€â”€ ðŸ“ resultados/
â”‚   â”œâ”€â”€ figura_correlaciones.png
â”‚   â””â”€â”€ modelo_final.pkl
â””â”€â”€ requirements.txt
```

### 2.2 El notebook de anÃ¡lisis â€” estructura recomendada

```
SecciÃ³n 1: Contexto y pregunta de negocio
SecciÃ³n 2: Carga e inspecciÃ³n inicial de datos
SecciÃ³n 3: AnÃ¡lisis Exploratorio (EDA)
SecciÃ³n 4: Limpieza y transformaciÃ³n
SecciÃ³n 5: Modelado y evaluaciÃ³n
SecciÃ³n 6: Conclusiones e insights
SecciÃ³n 7: Recomendaciones para el negocio
```

---

## 3. AnÃ¡lisis Exploratorio (EDA) completo

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

# EstadÃ­sticas descriptivas
print(df.describe().T)

# Duplicados
print(f"Filas duplicadas: {df.duplicated().sum()}")
```

### 3.2 Visualizaciones esenciales de EDA

```python
import matplotlib.pyplot as plt
import pandas as pd

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("AnÃ¡lisis Exploratorio â€” Dataset Ventas", fontsize=14, fontweight="bold")

# 1. DistribuciÃ³n de la variable objetivo
axes[0, 0].hist(df["total_neto"], bins=20, color="#22c55e", edgecolor="white")
axes[0, 0].set_title("DistribuciÃ³n de ventas netas")
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
axes[1, 1].set_title("DistribuciÃ³n por sucursal (boxplot)")
axes[1, 1].set_ylabel("Total neto ($)")
axes[1, 1].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig("resultados/eda_completo.png", dpi=150, bbox_inches="tight")
plt.show()
```

---

## 4. Limpieza de datos â€” GuÃ­a prÃ¡ctica

### 4.1 Estrategias para valores nulos

| Tipo de columna | Porcentaje nulo | Estrategia recomendada |
|---|---|---|
| NumÃ©rica | < 5% | Imputar con mediana |
| NumÃ©rica | 5â€“30% | Imputar con mediana + crear flag |
| NumÃ©rica | > 30% | Evaluar eliminar columna |
| CategÃ³rica | < 10% | Imputar con moda o "Desconocido" |
| CategÃ³rica | > 10% | "Desconocido" como categorÃ­a propia |
| Fecha | Cualquiera | Investigar origen del nulo |

### 4.2 CÃ³digo de limpieza documentada

```python
# BUENA PRÃCTICA: documentar cada decisiÃ³n de limpieza

# 1. Eliminar duplicados exactos
n_antes = len(df)
df = df.drop_duplicates()
print(f"Duplicados eliminados: {n_antes - len(df)}")

# 2. Corregir tipos de datos
df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
df["descuento_pct"] = df["descuento_pct"].astype(float)

# 3. Imputar nulos numÃ©ricos con mediana
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

1. **Contexto:** Â¿QuÃ© problema resolvemos? Â¿Para quiÃ©n?
2. **Hallazgos:** Los 3â€“5 insights mÃ¡s importantes.
3. **Evidencia:** Las visualizaciones que los sustentan.
4. **Recomendaciones:** Acciones concretas para el negocio.
5. **Limitaciones:** QuÃ© no puede decir este anÃ¡lisis.

### 5.2 Principios de visualizaciÃ³n efectiva

| Principio | AplicaciÃ³n |
|---|---|
| **Una idea, un grÃ¡fico** | No saturar con demasiada informaciÃ³n |
| **TÃ­tulo descriptivo** | "Ventas caen 30% en Q3" en lugar de "Ventas por trimestre" |
| **Etiquetas legibles** | Ejes, unidades, leyendas siempre presentes |
| **Color con propÃ³sito** | Un color destaca, muchos confunden |
| **Audiencia no tÃ©cnica** | Sin jerga, sin notaciÃ³n matemÃ¡tica |

### 5.3 Ejemplo de visualizaciÃ³n comunicativa

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

ax.set_title("Ventas mensuales â€” Los meses rojos estÃ¡n bajo el promedio anual",
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

## 6. CÃ³mo presentar un modelo de ML a audiencia no tÃ©cnica

### 6.1 TraducciÃ³n de mÃ©tricas

| MÃ©trica tÃ©cnica | TraducciÃ³n para negocio |
|---|---|
| F1 = 0.82 | "El modelo identifica correctamente 8 de cada 10 clientes en riesgo" |
| RMSE = $1.200 | "Nuestras predicciones de ventas se desvÃ­an en promedio $1.200" |
| Recall = 0.90 | "De cada 10 clientes que se irÃ­an, detectamos 9" |
| PrecisiÃ³n = 0.75 | "De cada 4 clientes que el modelo marca como riesgo, 3 realmente se van" |

### 6.2 Estructura de presentaciÃ³n de 5 minutos

```
00:00 â€“ 00:30  Â¿QuÃ© problema resolvimos y por quÃ© importa?
00:30 â€“ 01:30  Â¿QuÃ© encontramos en los datos? (1 grÃ¡fico clave)
01:30 â€“ 02:30  Â¿CÃ³mo funciona el modelo? (sin matemÃ¡ticas)
02:30 â€“ 03:30  Â¿QuÃ© tan bueno es? (mÃ©tricas en lenguaje de negocio)
03:30 â€“ 04:30  Â¿QuÃ© deberÃ­a hacer el negocio con esto?
04:30 â€“ 05:00  Limitaciones y prÃ³ximos pasos
```

---

## 7. Lo que aprendiste en este bootcamp

| Clase | Habilidad | Herramienta |
|---|---|---|
| 01 | Variables, tipos, control de flujo | Python bÃ¡sico |
| 02 | Carga, limpieza, transformaciÃ³n | pandas |
| 03 | ExploraciÃ³n visual de datos | matplotlib, seaborn |
| 04 | EstadÃ­sticas descriptivas | pandas, statistics |
| 05 | Visualizaciones comunicativas | matplotlib avanzado |
| 06 | Texto, fechas, ingenierÃ­a de features | pandas, re |
| 07 | Proyecto guiado integrador | Todas las anteriores |
| 08 | PresentaciÃ³n de hallazgos | Storytelling |
| 09 | Machine Learning â€” regresiÃ³n | scikit-learn |
| 10 | ClasificaciÃ³n y evaluaciÃ³n | scikit-learn |
| 11 | Pipelines y validaciÃ³n cruzada | scikit-learn |
| 12 | Proyecto final integrador | Todas las anteriores |

---

## 🚀 8. PrÃ³ximos pasos recomendados

| Nivel | Recurso | Tiempo estimado |
|---|---|---|
| PrÃ¡ctica inmediata | Kaggle Learn (gratuito) | 2â€“4 semanas |
| Profundizar ML | "Hands-On ML" â€” GÃ©ron | 2â€“3 meses |
| Portfolio | 3 proyectos con datos reales en GitHub | 3â€“6 meses |
| EspecializaciÃ³n | MLOps, Deep Learning, o NLP | 6â€“12 meses |
| Comunidad | Meetups de Data Science locales | Ongoing |

---

> **Mensaje final:** El anÃ¡lisis de datos es una habilidad que se construye proyecto a proyecto. Lo mÃ¡s importante no es saber todos los algoritmos, sino hacer las preguntas correctas y comunicar los hallazgos con claridad.
