# 🧠 Documento TeÃ³rico â€” Clase 07: Mini Proyecto Guiado

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.


> **Nivel:** Integrador Â· **DuraciÃ³n estimada de lectura:** 20 minutos

---

## 1. Â¿QuÃ© es un anÃ¡lisis integrado?

Un anÃ¡lisis integrado combina todas las habilidades aprendidas en un flujo coherente:

```
Pregunta de negocio â†’ Datos â†’ ExploraciÃ³n â†’ Limpieza â†’ AnÃ¡lisis â†’ VisualizaciÃ³n â†’ Conclusiones
```

La diferencia entre un anÃ¡lisis aficionado y uno profesional no estÃ¡ en las herramientas usadas, sino en la **coherencia del razonamiento** y la **claridad de la comunicaciÃ³n**.

---

## 2. El mÃ©todo de las 5 preguntas

Antes de tocar el cÃ³digo, responde estas 5 preguntas:

| Pregunta | Ejemplo |
|---|---|
| **Â¿QuÃ© queremos saber?** | Â¿QuÃ© sucursales tienen mayor rentabilidad? |
| **Â¿QuÃ© datos tenemos?** | Ventas diarias por producto y sucursal |
| **Â¿QuÃ© nos puede faltar?** | Costos, devoluciones, datos temporales |
| **Â¿QuÃ© asumimos?** | Sin devoluciones, precio = ganancia bruta |
| **Â¿Para quiÃ©n es el anÃ¡lisis?** | Gerente de ventas, sin formaciÃ³n tÃ©cnica |

---

## 3. Estructura del anÃ¡lisis guiado

### SecciÃ³n 1: ComprensiÃ³n del problema

```python
# Siempre documentar el contexto al inicio del notebook
"""
PROYECTO: AnÃ¡lisis de rentabilidad por sucursal
DATASET:  datasets/ventas_tienda.csv
OBJETIVO: Identificar las 3 sucursales mÃ¡s rentables y los
          factores que explican la diferencia.
AUDIENCIA: DirecciÃ³n comercial
FECHA:    2024-09
"""
```

### SecciÃ³n 2: Carga y primera inspecciÃ³n

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/ventas_tienda.csv")

print(f"Dataset: {df.shape[0]:,} filas Ã— {df.shape[1]} columnas")
print(f"\nColumnas: {df.columns.tolist()}")
print(f"\nValores nulos:\n{df.isnull().sum()[df.isnull().sum() > 0]}")
print(f"\nPrimeras filas:")
df.head()
```

### SecciÃ³n 3: Limpieza documentada

```python
# Documentar CADA decisiÃ³n
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

### SecciÃ³n 4: AnÃ¡lisis exploratorio guiado

```python
# Siempre empezar con las preguntas mÃ¡s simples
print("=== RESUMEN GENERAL ===")
print(f"Sucursales: {df['sucursal'].nunique()} ({', '.join(df['sucursal'].unique())})")
print(f"PerÃ­odo: {df['fecha_venta'].min().date()} â†’ {df['fecha_venta'].max().date()}")
print(f"Total ventas: ${df['total_neto'].sum():,.0f}")
print(f"Ticket promedio: ${df['total_neto'].mean():,.0f}")

# Luego responder preguntas especÃ­ficas
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

## 4. Buenas prÃ¡cticas de cÃ³digo en un proyecto

### 4.1 OrganizaciÃ³n del notebook

```
Celda 0: Encabezado (markdown) â€” tÃ­tulo, objetivo, autor
Celda 1: Imports y configuraciÃ³n global
Celda 2: Carga de datos
Celda 3-N: AnÃ¡lisis con secciones separadas por markdown
Celda final: Conclusiones y recomendaciones
```

### 4.2 CÃ³digo limpio y legible

```python
# âŒ DifÃ­cil de leer
r = df.groupby("s")["t"].sum().sort_values(ascending=False)

# âœ… Claro y mantenible
ranking_sucursales = (df
    .groupby("sucursal")["total_neto"]
    .sum()
    .sort_values(ascending=False)
    .rename("ventas_totales")
    .reset_index()
)
```

### 4.3 Comentarios Ãºtiles

```python
# âŒ Comentario inÃºtil (describe el quÃ©, no el por quÃ©)
# Calcular la media
media = df["total_neto"].mean()

# âœ… Comentario Ãºtil (explica el razonamiento)
# Usamos mediana en lugar de media porque la distribuciÃ³n
# estÃ¡ sesgada a la derecha por ventas corporativas grandes
mediana = df["total_neto"].median()
```

---

## 5. Plantilla de conclusiones

```markdown
## ✅ Conclusiones

### Hallazgo principal
[Una oraciÃ³n que resume el insight mÃ¡s importante]

### Hallazgos secundarios
1. [Segundo hallazgo]
2. [Tercer hallazgo]

### Limitaciones del anÃ¡lisis
- [QuÃ© no podemos concluir con estos datos]

### Recomendaciones
1. **[AcciÃ³n concreta]**: justificaciÃ³n breve.
2. **[Segunda acciÃ³n]**: justificaciÃ³n breve.

### PrÃ³ximos pasos
- [QuÃ© datos adicionales mejorarÃ­an el anÃ¡lisis]
```

---

## 6. Checklist antes de entregar

| âœ… | Elemento |
|---|---|
| â˜ | El notebook se ejecuta de principio a fin sin errores |
| â˜ | Todas las celdas tienen output visible |
| â˜ | Todos los grÃ¡ficos tienen tÃ­tulo y ejes etiquetados |
| â˜ | El anÃ¡lisis responde la pregunta inicial |
| â˜ | Las conclusiones usan lenguaje de negocio |
| â˜ | Se documentan las decisiones de limpieza |
| â˜ | Los insights son accionables |

---

## ✅ 7. Resumen rÃ¡pido

```
âœ… Empezar siempre con las 5 preguntas del negocio
âœ… Documentar cada decisiÃ³n de limpieza
âœ… CÃ³digo legible > cÃ³digo corto
âœ… Conclusiones en lenguaje de negocio
âœ… El notebook debe ejecutarse sin errores de principio a fin
```
