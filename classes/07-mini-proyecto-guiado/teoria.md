# Documento Teórico — Clase 07: Mini Proyecto Guiado

> **Nivel:** Integrador · **Duración estimada de lectura:** 20 minutos

---

## 1. ¿Qué es un análisis integrado?

Un análisis integrado combina todas las habilidades aprendidas en un flujo coherente:

```
Pregunta de negocio → Datos → Exploración → Limpieza → Análisis → Visualización → Conclusiones
```

La diferencia entre un análisis aficionado y uno profesional no está en las herramientas usadas, sino en la **coherencia del razonamiento** y la **claridad de la comunicación**.

---

## 2. El método de las 5 preguntas

Antes de tocar el código, responde estas 5 preguntas:

| Pregunta | Ejemplo |
|---|---|
| **¿Qué queremos saber?** | ¿Qué sucursales tienen mayor rentabilidad? |
| **¿Qué datos tenemos?** | Ventas diarias por producto y sucursal |
| **¿Qué nos puede faltar?** | Costos, devoluciones, datos temporales |
| **¿Qué asumimos?** | Sin devoluciones, precio = ganancia bruta |
| **¿Para quién es el análisis?** | Gerente de ventas, sin formación técnica |

---

## 3. Estructura del análisis guiado

### Sección 1: Comprensión del problema

```python
# Siempre documentar el contexto al inicio del notebook
"""
PROYECTO: Análisis de rentabilidad por sucursal
DATASET:  datasets/ventas_tienda.csv
OBJETIVO: Identificar las 3 sucursales más rentables y los
          factores que explican la diferencia.
AUDIENCIA: Dirección comercial
FECHA:    2024-09
"""
```

### Sección 2: Carga y primera inspección

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")

print(f"Dataset: {df.shape[0]:,} filas × {df.shape[1]} columnas")
print(f"\nColumnas: {df.columns.tolist()}")
print(f"\nValores nulos:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
print(f"\nPrimeras filas:")
df.head()
```

### Sección 3: Limpieza documentada

```python
# Documentar CADA decisión
pasos_limpieza = []

# Paso 1: Fechas
df["fecha_venta"] = pd.to_datetime(df["fecha_venta"])
pasos_limpieza.append("Fecha convertida a datetime")

# Paso 2: Columnas derivadas
df["total_bruto"] = df["unidades_vendidas"] * df["precio_unitario"]
df["total_neto"]  = df["total_bruto"] * (1 - df["descuento_pct"] / 100)
pasos_limpieza.append("Columnas total_bruto y total_neto creadas")

print("Pasos de limpieza realizados:")
for i, paso in enumerate(pasos_limpieza, 1):
    print(f"  {i}. {paso}")
```

### Sección 4: Análisis exploratorio guiado

```python
# Siempre empezar con las preguntas más simples
print("=== RESUMEN GENERAL ===")
print(f"Sucursales: {df['sucursal'].nunique()} ({', '.join(df['sucursal'].unique())})")
print(f"Período: {df['fecha_venta'].min().date()} → {df['fecha_venta'].max().date()}")
print(f"Total ventas: ${df['total_neto'].sum():,.0f}")
print(f"Ticket promedio: ${df['total_neto'].mean():,.0f}")

# Luego responder preguntas específicas
resumen_sucursal = df.groupby("sucursal").agg(
    ventas_totales=("total_neto", "sum"),
    n_transacciones=("total_neto", "count"),
    ticket_promedio=("total_neto", "mean"),
    descuento_promedio=("descuento_pct", "mean")
).sort_values("ventas_totales", ascending=False).round(2)

print("\n=== RANKING DE SUCURSALES ===")
print(resumen_sucursal)
```

---

## 4. Buenas prácticas de código en un proyecto

### 4.1 Organización del notebook

```
Celda 0: Encabezado (markdown) — título, objetivo, autor
Celda 1: Imports y configuración global
Celda 2: Carga de datos
Celda 3-N: Análisis con secciones separadas por markdown
Celda final: Conclusiones y recomendaciones
```

### 4.2 Código limpio y legible

```python
# ❌ Difícil de leer
r = df.groupby("s")["t"].sum().sort_values(ascending=False)

# ✅ Claro y mantenible
ranking_sucursales = (df
    .groupby("sucursal")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .rename("ventas_totales")
    .reset_index()
)
```

### 4.3 Comentarios útiles

```python
# ❌ Comentario inútil (describe el qué, no el por qué)
# Calcular la media
media = df["total_neto"].mean()

# ✅ Comentario útil (explica el razonamiento)
# Usamos mediana en lugar de media porque la distribución
# está sesgada a la derecha por ventas corporativas grandes
mediana = df["total_neto"].median()
```

---

## 5. Plantilla de conclusiones

```markdown
## Conclusiones

### Hallazgo principal
[Una oración que resume el insight más importante]

### Hallazgos secundarios
1. [Segundo hallazgo]
2. [Tercer hallazgo]

### Limitaciones del análisis
- [Qué no podemos concluir con estos datos]

### Recomendaciones
1. **[Acción concreta]**: justificación breve.
2. **[Segunda acción]**: justificación breve.

### Próximos pasos
- [Qué datos adicionales mejorarían el análisis]
```

---

## 6. Checklist antes de entregar

| ✅ | Elemento |
|---|---|
| ☐ | El notebook se ejecuta de principio a fin sin errores |
| ☐ | Todas las celdas tienen output visible |
| ☐ | Todos los gráficos tienen título y ejes etiquetados |
| ☐ | El análisis responde la pregunta inicial |
| ☐ | Las conclusiones usan lenguaje de negocio |
| ☐ | Se documentan las decisiones de limpieza |
| ☐ | Los insights son accionables |

---

## 7. Resumen rápido

```
✅ Empezar siempre con las 5 preguntas del negocio
✅ Documentar cada decisión de limpieza
✅ Código legible > código corto
✅ Conclusiones en lenguaje de negocio
✅ El notebook debe ejecutarse sin errores de principio a fin
```
