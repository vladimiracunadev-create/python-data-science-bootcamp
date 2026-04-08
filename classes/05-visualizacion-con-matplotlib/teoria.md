# 🧠 Documento teórico — Clase 05: Visualización con matplotlib

> 🧠 Base conceptual para preparar, reforzar o profundizar lo visto en clase.

## 💡 Idea central

No basta con que el gráfico funcione: debe poder leerse sin fricción.

## ❓ Por qué importa este módulo

Matplotlib permite controlar detalle visual y comunicar mejor una conclusión.

## 💻 Bloque de código documentado

### Serie temporal de clientes activos

Crear una figura explícita permite controlar tamaño, etiquetas y orden visual con intención.

**Qué hace:** crear figura → dibujar → rotular → ajustar

**Para qué sirve:** Sirve para pasar de una visualización funcional a una visualización comunicable.

```python
# Qué hace: crear figura → dibujar → rotular → ajustar.
# Para qué sirve: Sirve para pasar de una visualización funcional a una visualización comunicable.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("datasets/retencion_clientes.csv")

fig, ax = plt.subplots(figsize=(9, 4))
ax.plot(df["mes"], df["clientes_activos"], marker="o", linewidth=2)
ax.set_title("Clientes activos por mes")
ax.set_xlabel("Mes")
ax.set_ylabel("Clientes activos")
ax.tick_params(axis="x", rotation=45)
ax.grid(alpha=0.2)
plt.tight_layout()
```

## ⚠️ Errores frecuentes a vigilar

- Saltar al código sin aclarar la pregunta.
- Ejecutar bloques sin leer la salida.
- Dejar bloques importantes sin comentarios o sin explicación oral.

## 🔗 Conexión con el siguiente módulo

La clase 06 amplía el repertorio con texto, fechas y transformaciones.
