# 🧠 Documento TeÃ³rico â€” Clase 02: Pandas y Limpieza de Datos

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.


> **Nivel:** Principiante-Intermedio Â· **DuraciÃ³n estimada de lectura:** 30 minutos

---

## 1. Â¿QuÃ© es pandas?

`pandas` es la biblioteca estÃ¡ndar de Python para **manipular datos tabulares**. Permite trabajar con filas y columnas de forma eficiente, similar a Excel pero programÃ¡ticamente.

### 1.1 Estructuras fundamentales

| Estructura | DescripciÃ³n | AnalogÃ­a |
|---|---|---|
| `Series` | Columna de datos con Ã­ndice | Una columna de Excel |
| `DataFrame` | Tabla de datos bidimensional | Una hoja de Excel completa |

```python
import pandas as pd

# Series
precios = pd.Series([8990, 15990, 25990], name="precio", index=["Mouse", "Teclado", "Webcam"])

# DataFrame
df = pd.DataFrame({
    "producto": ["Mouse", "Teclado", "Webcam"],
    "precio":   [8990, 15990, 25990],
    "stock":    [45, 12, 8]
})
```

---

## 2. Carga de datos

### 2.1 Formatos mÃ¡s comunes

| FunciÃ³n | Formato | Ejemplo |
|---|---|---|
| `pd.read_csv()` | CSV (texto separado por comas) | `pd.read_csv("ventas.csv")` |
| `pd.read_excel()` | Excel (.xlsx, .xls) | `pd.read_excel("datos.xlsx")` |
| `pd.read_json()` | JSON | `pd.read_json("api.json")` |
| `pd.read_sql()` | SQL | `pd.read_sql(query, conn)` |

```python
# ParÃ¡metros Ãºtiles de read_csv
df = pd.read_csv(
    "datasets/ventas_tienda.csv",
    sep=",",                    # separador
    encoding="utf-8",           # codificaciÃ³n
    parse_dates=["fecha"],      # parsear fechas
    decimal=",",                # decimal en formato europeo
    thousands=".",              # separador de miles
    na_values=["", "N/A", "-"] # valores a tratar como nulos
)
```

---

## 3. ExploraciÃ³n inicial

### 3.1 Comandos de inspecciÃ³n esenciales

| Comando | QuÃ© muestra |
|---|---|
| `df.shape` | (filas, columnas) |
| `df.dtypes` | Tipo de cada columna |
| `df.head(n)` | Primeras n filas |
| `df.tail(n)` | Ãšltimas n filas |
| `df.info()` | Resumen completo con tipos y nulos |
| `df.describe()` | EstadÃ­sticas descriptivas de columnas numÃ©ricas |
| `df.columns.tolist()` | Lista de nombres de columnas |
| `df.nunique()` | Cantidad de valores Ãºnicos por columna |
| `df.value_counts()` | Frecuencia de valores en una Series |

```python
print(f"Dimensiones: {df.shape}")
print(f"Columnas: {df.columns.tolist()}")
print(f"\nPrimeras filas:")
print(df.head())
print(f"\nInformaciÃ³n general:")
df.info()
print(f"\nEstadÃ­sticas:")
print(df.describe())
```

---

## 4. SelecciÃ³n de datos

### 4.1 Seleccionar columnas

```python
# Una columna â†’ Series
precios = df["precio_unitario"]

# MÃºltiples columnas â†’ DataFrame
ventas = df[["producto", "precio_unitario", "unidades_vendidas"]]
```

### 4.2 Filtrar filas con condiciones

```python
# Una condiciÃ³n
ventas_altas = df[df["total_neto"] > 50000]

# MÃºltiples condiciones
ventas_norte_altas = df[(df["sucursal"] == "Norte") & (df["total_neto"] > 30000)]

# Usando isin()
sucursales_objetivo = df[df["sucursal"].isin(["Norte", "Centro"])]

# Usando query() (mÃ¡s legible)
resultado = df.query("total_neto > 50000 and sucursal == 'Norte'")
```

### 4.3 SelecciÃ³n por posiciÃ³n (iloc) e Ã­ndice (loc)

| MÃ©todo | Selecciona por | Ejemplo |
|---|---|---|
| `df.loc[filas, cols]` | Etiquetas/condiciones | `df.loc[0:5, ["nombre", "precio"]]` |
| `df.iloc[filas, cols]` | PosiciÃ³n numÃ©rica | `df.iloc[0:5, 0:3]` |

---

## 5. Limpieza de datos

### 5.1 Valores nulos

```python
# Detectar nulos
print(df.isnull().sum())
print(df.isnull().mean().round(3) * 100)  # porcentaje

# Eliminar filas con nulos
df_sin_nulos = df.dropna()

# Eliminar filas donde TODAS las columnas son nulas
df_parcial = df.dropna(how="all")

# Imputar con estadÃ­sticas
df["precio"] = df["precio"].fillna(df["precio"].median())
df["categoria"] = df["categoria"].fillna("Sin categorÃ­a")

# Imputar con forward fill (propagar Ãºltimo valor vÃ¡lido)
df["serie_temporal"] = df["serie_temporal"].ffill()
```

### 5.2 Duplicados

```python
# Detectar
n_duplicados = df.duplicated().sum()
print(f"Filas duplicadas: {n_duplicados}")

# Ver duplicados
print(df[df.duplicated(keep=False)])

# Eliminar (mantener primera ocurrencia)
df = df.drop_duplicates()

# Eliminar basado en columnas especÃ­ficas
df = df.drop_duplicates(subset=["id_transaccion"])
```

### 5.3 Tipos de datos incorrectos

```python
# Convertir texto a nÃºmero
df["precio"] = pd.to_numeric(df["precio"], errors="coerce")  # NaN si falla

# Convertir a fecha
df["fecha"] = pd.to_datetime(df["fecha"], format="%Y-%m-%d")

# Convertir a categorÃ­a (eficiente para texto repetido)
df["sucursal"] = df["sucursal"].astype("category")
```

### 5.4 Limpieza de texto

```python
# Estandarizar mayÃºsculas/minÃºsculas
df["nombre"] = df["nombre"].str.strip()          # eliminar espacios
df["nombre"] = df["nombre"].str.lower()           # a minÃºsculas
df["nombre"] = df["nombre"].str.title()           # Primera letra mayÃºscula

# Reemplazar valores
df["sucursal"] = df["sucursal"].str.replace("Stgo", "Santiago")

# Extraer parte de un texto
df["codigo_producto"] = df["codigo"].str[:3]      # primeros 3 caracteres
```

---

## 6. TransformaciÃ³n de datos

### 6.1 Crear nuevas columnas

```python
# OperaciÃ³n aritmÃ©tica
df["total_bruto"] = df["unidades_vendidas"] * df["precio_unitario"]
df["total_neto"] = df["total_bruto"] * (1 - df["descuento_pct"] / 100)

# CondiciÃ³n con np.where
import numpy as np
df["rendimiento"] = np.where(df["total_neto"] > 50000, "Alto", "Normal")

# CondiciÃ³n mÃºltiple con pd.cut
df["tramo"] = pd.cut(df["total_neto"],
    bins=[0, 20000, 50000, float("inf")],
    labels=["Bajo", "Medio", "Alto"]
)
```

### 6.2 Aplicar funciones

```python
# apply() a una columna
def clasificar(monto):
    if monto > 100000:
        return "Premium"
    elif monto > 50000:
        return "EstÃ¡ndar"
    return "BÃ¡sico"

df["segmento"] = df["total_neto"].apply(clasificar)

# lambda para operaciones simples
df["iva"] = df["total_neto"].apply(lambda x: x * 0.19)
```

### 6.3 Agrupaciones con groupby

```python
# Suma por grupo
ventas_sucursal = df.groupby("sucursal")["total_neto"].sum()

# MÃºltiples agregaciones
resumen = df.groupby("sucursal").agg(
    ventas_totales=("total_neto", "sum"),
    n_transacciones=("total_neto", "count"),
    ticket_promedio=("total_neto", "mean"),
    venta_maxima=("total_neto", "max")
).round(2)

# Ordenar
resumen = resumen.sort_values("ventas_totales", ascending=False)
```

---

## 7. Guardar datos procesados

```python
# CSV
df.to_csv("datos_limpios.csv", index=False, encoding="utf-8")

# Excel
df.to_excel("reporte.xlsx", sheet_name="Ventas", index=False)

# MÃºltiples hojas
with pd.ExcelWriter("reporte_completo.xlsx") as writer:
    df.to_excel(writer, sheet_name="Datos", index=False)
    resumen.to_excel(writer, sheet_name="Resumen")
```

---

## 8. Errores frecuentes con pandas

| Error | Causa | SoluciÃ³n |
|---|---|---|
| `SettingWithCopyWarning` | Modificar un slice del DataFrame | Usar `.copy()` al crear subsets |
| `KeyError: 'columna'` | Nombre de columna incorrecto | Verificar `df.columns.tolist()` |
| `ValueError: mixed types` | Columna con tipos mezclados | Usar `pd.to_numeric(errors='coerce')` |
| Fecha como object | No parsear fechas al cargar | Usar `parse_dates=["columna"]` |
| NaN inesperado despuÃ©s de merge | Claves sin correspondencia | Revisar el tipo de join |

---

## ✅ 9. Resumen rÃ¡pido

```
âœ… pd.read_csv() â†’ cargar datos desde archivo
âœ… df.info() / df.describe() â†’ inspecciÃ³n inicial
âœ… df[condiciÃ³n] â†’ filtrar filas
âœ… df.groupby() â†’ agregar por grupos
âœ… df.isnull().sum() â†’ detectar nulos
âœ… df.fillna() / df.dropna() â†’ manejar nulos
âœ… df.drop_duplicates() â†’ eliminar duplicados
âœ… df["col"] = ... â†’ crear columna nueva
```
