# 🧠 Documento TeÃ³rico â€” Clase 08: PresentaciÃ³n de Hallazgos con Claridad

> **Nivel:** Intermedio Â· **DuraciÃ³n estimada de lectura:** 20 minutos

---

## 1. El problema de comunicar datos

Los datos cuentan historias. Pero la mayorÃ­a de los anÃ¡lisis tÃ©cnicamente correctos **fracasan en comunicar** porque:

1. EstÃ¡n escritos para el analista, no para la audiencia.
2. Usan jerga tÃ©cnica innecesaria.
3. Presentan todos los resultados en lugar de los relevantes.
4. No proponen acciones concretas.

---

## 2. Principios de Storytelling con datos

### 2.1 El arco narrativo de un anÃ¡lisis

```
Contexto â†’ Conflicto â†’ ResoluciÃ³n â†’ Llamado a la acciÃ³n
```

| Parte | QuÃ© comunica | Ejemplo |
|---|---|---|
| **Contexto** | SituaciÃ³n inicial | "Analizamos ventas del Q3 2024." |
| **Conflicto** | El problema o hallazgo | "Las ventas cayeron 18% en agosto." |
| **ResoluciÃ³n** | La causa o patrÃ³n | "La caÃ­da se concentra en la sucursal Sur." |
| **AcciÃ³n** | QuÃ© hacer al respecto | "Reforzar inventario y equipo de ventas en Sur." |

### 2.2 La regla del "Â¿y quÃ©?"

Cada dato o grÃ¡fico debe responder la pregunta: **Â¿y quÃ© deberÃ­a hacer la audiencia con esta informaciÃ³n?**

| âŒ Sin "y quÃ©?" | âœ… Con "y quÃ©?" |
|---|---|
| "La sucursal Norte tuvo $512K en ventas" | "La sucursal Norte lidera el ranking con $512K. Replicar su estrategia de upselling en otras sucursales." |
| "El ticket promedio es $45.200" | "El ticket promedio ($45.200) estÃ¡ 15% bajo la meta. Los vendedores necesitan entrenamiento en productos complementarios." |

---

## 3. DiseÃ±o de visualizaciones comunicativas

### 3.1 JerarquÃ­a visual

El ojo humano sigue un orden natural al ver un grÃ¡fico:

```
1ï¸âƒ£ TÃ­tulo (primera lectura)
2ï¸âƒ£ Elemento mÃ¡s destacado (barra mÃ¡s alta, punto mÃ¡s alejado)
3ï¸âƒ£ Ejes y etiquetas
4ï¸âƒ£ Leyenda (Ãºltima)
```

DiseÃ±a guiando la atenciÃ³n hacia el insight principal.

### 3.2 Usar color como semÃ¡foro

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

ax.set_title("Ventas por sucursal vs. meta â€” Q3 2024\nðŸŸ¢ Sobre meta  ðŸ”´ Bajo meta",
    fontsize=12, fontweight="bold")
ax.set_ylabel("Ventas ($)")
ax.legend()
plt.tight_layout()
plt.show()
```

### 3.3 Antes y despuÃ©s: mismo dato, distinta comunicaciÃ³n

**VersiÃ³n tÃ©cnica (antes):**
```
"El anÃ¡lisis de correlaciÃ³n de Pearson entre precio_unitario y 
unidades_vendidas arrojÃ³ r = -0.63 (p < 0.05)."
```

**VersiÃ³n comunicativa (despuÃ©s):**
```
"A mayor precio, se venden menos unidades. Los productos bajo $15.000
se venden 3Ã— mÃ¡s que los de $40.000+. Aumentar el mix de productos
accesibles podrÃ­a incrementar el volumen sin sacrificar mÃ¡rgenes."
```

---

## 4. Estructura de un reporte ejecutivo en 5 slides

### Slide 1: Contexto y objetivo
- Una oraciÃ³n de contexto
- La pregunta que respondemos
- Los datos que usamos

### Slide 2: Hallazgo principal
- El insight mÃ¡s importante en una oraciÃ³n
- Un solo grÃ¡fico que lo sustente
- No mÃ¡s de 3 bullet points de apoyo

### Slide 3: Detalle de hallazgos
- 2-3 hallazgos secundarios
- Con sus grÃ¡ficos correspondientes
- Cada uno con una implicaciÃ³n para el negocio

### Slide 4: Recomendaciones
- MÃ¡ximo 3 acciones concretas
- Cada una con: Â¿QuÃ© hacer? + Â¿Por quÃ©? + Â¿Impacto esperado?

### Slide 5: PrÃ³ximos pasos
- Â¿QuÃ© falta para profundizar?
- Â¿QuÃ© datos adicionales se necesitan?
- Â¿CuÃ¡ndo hacer la siguiente revisiÃ³n?

---

## 5. KPIs para comunicar resultados de ventas

| KPI | CÃ³mo calcularlo | QuÃ© comunica |
|---|---|---|
| **Crecimiento YoY** | (actual - aÃ±o anterior) / aÃ±o anterior | Tendencia de largo plazo |
| **Ticket promedio** | total ventas / nÂ° transacciones | Valor por cliente |
| **Share de mercado interno** | ventas sucursal / total empresa | Peso relativo |
| **Tasa de conversiÃ³n** | ventas / visitas | Efectividad comercial |
| **Margen bruto estimado** | (ventas - costo estimado) / ventas | Rentabilidad |

---

## 6. Tabla de traducciÃ³n tÃ©cnico â†’ negocio

| TÃ©rmino tÃ©cnico | TraducciÃ³n para audiencia no tÃ©cnica |
|---|---|
| `mean()` | Promedio |
| `median()` | Valor central (la mitad gana mÃ¡s, la mitad gana menos) |
| `std()` | CuÃ¡nto varÃ­an los nÃºmeros alrededor del promedio |
| `correlation = 0.8` | "EstÃ¡n muy relacionados: cuando uno sube, el otro tambiÃ©n sube" |
| `outlier` | "Caso atÃ­pico" o "caso excepcional" |
| `normalizaciÃ³n` | "Ajustamos las escalas para poder comparar" |
| `modelo predictivo` | "Sistema que estima valores futuros basado en el pasado" |

---

## 7. Resumen rÃ¡pido

```
âœ… Contexto â†’ Conflicto â†’ ResoluciÃ³n â†’ AcciÃ³n (arco narrativo)
âœ… Cada dato debe responder "Â¿y quÃ©?"
âœ… Color como semÃ¡foro: verde = bueno, rojo = problema
âœ… TÃ­tulo descriptivo (insight, no descripciÃ³n)
âœ… MÃ¡ximo 3 recomendaciones accionables
âœ… Lenguaje de negocio, no tÃ©cnico
```
