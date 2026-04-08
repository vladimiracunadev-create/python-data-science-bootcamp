# Documento Teórico — Clase 08: Presentación de Hallazgos con Claridad

> **Nivel:** Intermedio · **Duración estimada de lectura:** 20 minutos

---

## 1. El problema de comunicar datos

Los datos cuentan historias. Pero la mayoría de los análisis técnicamente correctos **fracasan en comunicar** porque:

1. Están escritos para el analista, no para la audiencia.
2. Usan jerga técnica innecesaria.
3. Presentan todos los resultados en lugar de los relevantes.
4. No proponen acciones concretas.

---

## 2. Principios de Storytelling con datos

### 2.1 El arco narrativo de un análisis

```
Contexto → Conflicto → Resolución → Llamado a la acción
```

| Parte | Qué comunica | Ejemplo |
|---|---|---|
| **Contexto** | Situación inicial | "Analizamos ventas del Q3 2024." |
| **Conflicto** | El problema o hallazgo | "Las ventas cayeron 18% en agosto." |
| **Resolución** | La causa o patrón | "La caída se concentra en la sucursal Sur." |
| **Acción** | Qué hacer al respecto | "Reforzar inventario y equipo de ventas en Sur." |

### 2.2 La regla del "¿y qué?"

Cada dato o gráfico debe responder la pregunta: **¿y qué debería hacer la audiencia con esta información?**

| ❌ Sin "y qué?" | ✅ Con "y qué?" |
|---|---|
| "La sucursal Norte tuvo $512K en ventas" | "La sucursal Norte lidera el ranking con $512K. Replicar su estrategia de upselling en otras sucursales." |
| "El ticket promedio es $45.200" | "El ticket promedio ($45.200) está 15% bajo la meta. Los vendedores necesitan entrenamiento en productos complementarios." |

---

## 3. Diseño de visualizaciones comunicativas

### 3.1 Jerarquía visual

El ojo humano sigue un orden natural al ver un gráfico:

```
1️⃣ Título (primera lectura)
2️⃣ Elemento más destacado (barra más alta, punto más alejado)
3️⃣ Ejes y etiquetas
4️⃣ Leyenda (última)
```

Diseña guiando la atención hacia el insight principal.

### 3.2 Usar color como semáforo

```python
import matplotlib.pyplot as plt

# Destacar un elemento
sucursales = ["Norte", "Sur", "Centro", "Oriente"]
ventas = [512000, 289000, 678000, 198000]
meta = 400000

colores = ["#22c55e" if v >= meta else "#ef4444" for v in ventas]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(sucursales, ventas, color=colores, edgecolor="white", linewidth=0.5)
ax.axhline(meta, color="#f59e0b", linestyle="--", lw=1.5, label=f"Meta: ${meta:,}")

# Etiquetas de valor
for bar, val in zip(bars, ventas):
    color_txt = "#22c55e" if val >= meta else "#ef4444"
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5000,
        f"${val/1000:.0f}K", ha="center", fontsize=10, color=color_txt, fontweight="bold")

ax.set_title("Ventas por sucursal vs. meta — Q3 2024\n🟢 Sobre meta  🔴 Bajo meta",
    fontsize=12, fontweight="bold")
ax.set_ylabel("Ventas ($)")
ax.legend()
plt.tight_layout()
plt.show()
```

### 3.3 Antes y después: mismo dato, distinta comunicación

**Versión técnica (antes):**
```
"El análisis de correlación de Pearson entre precio_unitario y 
unidades_vendidas arrojó r = -0.63 (p < 0.05)."
```

**Versión comunicativa (después):**
```
"A mayor precio, se venden menos unidades. Los productos bajo $15.000
se venden 3× más que los de $40.000+. Aumentar el mix de productos
accesibles podría incrementar el volumen sin sacrificar márgenes."
```

---

## 4. Estructura de un reporte ejecutivo en 5 slides

### Slide 1: Contexto y objetivo
- Una oración de contexto
- La pregunta que respondemos
- Los datos que usamos

### Slide 2: Hallazgo principal
- El insight más importante en una oración
- Un solo gráfico que lo sustente
- No más de 3 bullet points de apoyo

### Slide 3: Detalle de hallazgos
- 2-3 hallazgos secundarios
- Con sus gráficos correspondientes
- Cada uno con una implicación para el negocio

### Slide 4: Recomendaciones
- Máximo 3 acciones concretas
- Cada una con: ¿Qué hacer? + ¿Por qué? + ¿Impacto esperado?

### Slide 5: Próximos pasos
- ¿Qué falta para profundizar?
- ¿Qué datos adicionales se necesitan?
- ¿Cuándo hacer la siguiente revisión?

---

## 5. KPIs para comunicar resultados de ventas

| KPI | Cómo calcularlo | Qué comunica |
|---|---|---|
| **Crecimiento YoY** | (actual - año anterior) / año anterior | Tendencia de largo plazo |
| **Ticket promedio** | total ventas / n° transacciones | Valor por cliente |
| **Share de mercado interno** | ventas sucursal / total empresa | Peso relativo |
| **Tasa de conversión** | ventas / visitas | Efectividad comercial |
| **Margen bruto estimado** | (ventas - costo estimado) / ventas | Rentabilidad |

---

## 6. Tabla de traducción técnico → negocio

| Término técnico | Traducción para audiencia no técnica |
|---|---|
| `mean()` | Promedio |
| `median()` | Valor central (la mitad gana más, la mitad gana menos) |
| `std()` | Cuánto varían los números alrededor del promedio |
| `correlation = 0.8` | "Están muy relacionados: cuando uno sube, el otro también sube" |
| `outlier` | "Caso atípico" o "caso excepcional" |
| `normalización` | "Ajustamos las escalas para poder comparar" |
| `modelo predictivo` | "Sistema que estima valores futuros basado en el pasado" |

---

## 7. Resumen rápido

```
✅ Contexto → Conflicto → Resolución → Acción (arco narrativo)
✅ Cada dato debe responder "¿y qué?"
✅ Color como semáforo: verde = bueno, rojo = problema
✅ Título descriptivo (insight, no descripción)
✅ Máximo 3 recomendaciones accionables
✅ Lenguaje de negocio, no técnico
```
