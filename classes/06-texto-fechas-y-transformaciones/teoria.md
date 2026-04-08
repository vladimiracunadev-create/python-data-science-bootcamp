# Documento Teórico — Clase 06: Texto, Fechas y Transformaciones

> **Nivel:** Intermedio · **Duración estimada de lectura:** 25 minutos

---

## 1. Manejo de texto con pandas

### 1.1 Accessor `.str`

El accessor `.str` de pandas aplica métodos de string a toda una columna vectorialmente:

```python
import pandas as pd
df = pd.read_csv("datasets/ventas_tienda.csv")

# Limpieza básica
df["producto"] = df["producto"].str.strip()      # eliminar espacios
df["producto"] = df["producto"].str.lower()       # minúsculas
df["producto"] = df["producto"].str.title()       # Title Case

# Contiene / empieza con / termina con
mascaras = df["producto"].str.contains("teclado", case=False, na=False)
perifericos = df[df["producto"].str.startswith("Peri")]
```

### 1.2 Tabla de métodos `.str` más usados

| Método | Descripción | Ejemplo |
|---|---|---|
| `.str.strip()` | Eliminar espacios al inicio y final | `" datos "` → `"datos"` |
| `.str.lower()` | Convertir a minúsculas | `"NORTE"` → `"norte"` |
| `.str.upper()` | Convertir a mayúsculas | `"sur"` → `"SUR"` |
| `.str.title()` | Primera letra mayúscula | `"san pedro"` → `"San Pedro"` |
| `.str.replace(a, b)` | Reemplazar texto | `"Stgo"` → `"Santiago"` |
| `.str.contains(p)` | Si contiene un patrón (regex) | `True/False` |
| `.str.startswith(p)` | Si empieza con el patrón | `True/False` |
| `.str.split(sep)` | Dividir por separador | `"a,b,c"` → `["a","b","c"]` |
| `.str.len()` | Longitud del texto | `"hola"` → `4` |
| `.str[:n]` | Primeros n caracteres | `"abcde"[:3]` → `"abc"` |
| `.str.extract(regex)` | Extraer grupos con regex | Extraer código numérico |
| `.str.cat(sep=)` | Concatenar Series | `"a" + "-" + "b"` |

### 1.3 Expresiones regulares (regex) básicas

```python
import re

# Extraer números de un texto
df["codigo_num"] = df["codigo"].str.extract(r"(\d+)")

# Reemplazar múltiples patrones
df["texto_limpio"] = df["texto"].str.replace(r"[^a-zA-Z0-9\s]", "", regex=True)

# Validar formato de código
df["codigo_valido"] = df["codigo"].str.match(r"^[A-Z]{2}\d{4}$")
```

| Patrón regex | Coincide con |
|---|---|
| `\d` | Cualquier dígito (0-9) |
| `\w` | Letra, dígito o guión bajo |
| `\s` | Espacio en blanco |
| `[A-Z]` | Letra mayúscula |
| `^` | Inicio de string |
| `$` | Final de string |
| `+` | Una o más repeticiones |
| `*` | Cero o más repeticiones |
| `{n}` | Exactamente n repeticiones |

---

## 2. Manejo de fechas con pandas

### 2.1 Convertir texto a fecha

```python
# Formato automático
df["fecha"] = pd.to_datetime(df["fecha"])

# Formato explícito (más rápido en datasets grandes)
df["fecha"] = pd.to_datetime(df["fecha"], format="%d/%m/%Y")
df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d %H:%M:%S")
```

### 2.2 Accessor `.dt`

```python
df["año"]         = df["fecha"].dt.year
df["mes"]         = df["fecha"].dt.month
df["dia"]         = df["fecha"].dt.day
df["dia_semana"]  = df["fecha"].dt.dayofweek    # 0=lunes, 6=domingo
df["nombre_dia"]  = df["fecha"].dt.day_name()
df["nombre_mes"]  = df["fecha"].dt.month_name()
df["trimestre"]   = df["fecha"].dt.quarter
df["semana_año"]  = df["fecha"].dt.isocalendar().week
df["es_fin_sem"]  = df["fecha"].dt.dayofweek >= 5
```

### 2.3 Operaciones con fechas

```python
from datetime import datetime, timedelta

# Diferencia entre fechas
df["dias_desde_venta"] = (datetime.now() - df["fecha"]).dt.days
df["semanas"]          = df["dias_desde_venta"] // 7

# Resampling (agregar por periodo)
df = df.set_index("fecha")
ventas_mensuales  = df["total_neto"].resample("ME").sum()   # fin de mes
ventas_semanales  = df["total_neto"].resample("W").sum()
ventas_diarias    = df["total_neto"].resample("D").sum()
df = df.reset_index()
```

### 2.4 Análisis temporal útil

```python
# Ventas por día de la semana
df["dia_semana"] = df["fecha"].dt.dayofweek
ventas_por_dia = df.groupby("dia_semana")["total_neto"].mean()
ventas_por_dia.index = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

# Heatmap hora × día (si tenemos hora)
df["hora"] = df["fecha"].dt.hour
pivot = df.pivot_table(values="total_neto", index="dia_semana", columns="hora", aggfunc="mean")
```

---

## 3. Ingeniería de features

La ingeniería de features es el proceso de **crear nuevas variables** a partir de las existentes para mejorar el análisis o los modelos.

### 3.1 Features derivadas de variables numéricas

```python
# Ratios
df["ticket_promedio"]    = df["total_neto"] / df["unidades_vendidas"]
df["margen_estimado"]    = (df["total_neto"] - df["total_neto"] * 0.6) / df["total_neto"]

# Interacciones
df["precio_x_descuento"] = df["precio_unitario"] * df["descuento_pct"]

# Transformaciones logarítmicas (para distribuciones sesgadas)
import numpy as np
df["log_ventas"] = np.log1p(df["total_neto"])  # log(1 + x) evita log(0)

# Binning (convertir continuo a categorías)
df["tramo_venta"] = pd.cut(df["total_neto"],
    bins=[0, 20000, 50000, 100000, float("inf")],
    labels=["Básico", "Estándar", "Premium", "Top"]
)
```

### 3.2 Features derivadas de fechas

```python
# Estacionalidad
df["es_diciembre"]  = (df["mes"] == 12).astype(int)
df["es_verano"]     = df["mes"].isin([12, 1, 2]).astype(int)
df["es_fin_de_mes"] = (df["dia"] >= 25).astype(int)
df["es_finde"]      = (df["dia_semana"] >= 5).astype(int)

# Antigüedad (días desde primera compra)
primera_compra = df.groupby("cliente_id")["fecha"].transform("min")
df["antiguedad_dias"] = (df["fecha"] - primera_compra).dt.days
```

### 3.3 Codificación de variables categóricas

| Técnica | Cuándo usar | Código |
|---|---|---|
| **Label Encoding** | Ordinal (Bajo < Medio < Alto) | `df["nivel"].map({"Bajo":0, "Medio":1, "Alto":2})` |
| **One-Hot Encoding** | Nominal sin orden | `pd.get_dummies(df, columns=["sucursal"])` |
| **Frequency Encoding** | Muchas categorías | `df["suc_freq"] = df["sucursal"].map(df["sucursal"].value_counts())` |
| **Target Encoding** | Con variable objetivo disponible | Media del target por categoría |

```python
# One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=["sucursal", "categoria"], drop_first=True)

# Label Encoding manual
nivel_map = {"Bajo": 0, "Medio": 1, "Alto": 2, "Premium": 3}
df["nivel_num"] = df["nivel"].map(nivel_map)
```

---

## 4. Normalización y estandarización

### 4.1 Diferencia clave

| Técnica | Fórmula | Resultado | Cuándo usar |
|---|---|---|---|
| **Min-Max (Normalización)** | (x - min) / (max - min) | Valores entre 0 y 1 | KNN, redes neuronales |
| **Z-Score (Estandarización)** | (x - media) / std | Media=0, std=1 | Regresión, SVM, PCA |
| **Robust Scaler** | (x - Q2) / IQR | Robusto a outliers | Datos con muchos outliers |

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

scaler_minmax  = MinMaxScaler()
scaler_zscore  = StandardScaler()
scaler_robust  = RobustScaler()

# Aplicar (solo en columnas numéricas)
cols_num = ["precio_unitario", "unidades_vendidas", "descuento_pct"]
df_norm  = df.copy()
df_norm[cols_num] = scaler_minmax.fit_transform(df[cols_num])
```

---

## 5. Resumen rápido

```
✅ .str accessor → operaciones de texto vectorizadas
✅ pd.to_datetime() → convertir texto a fecha
✅ .dt accessor → extraer año, mes, día, día semana
✅ resample() → agregar por periodo temporal
✅ pd.get_dummies() → one-hot encoding
✅ np.log1p() → transformación log para distribuciones sesgadas
✅ pd.cut() / pd.qcut() → convertir continuo a categorías
```
