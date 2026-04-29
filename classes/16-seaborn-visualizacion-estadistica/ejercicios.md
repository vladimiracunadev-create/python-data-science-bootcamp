# 🧪 Ejercicios — Clase 16
> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar
- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.

## 🧭 Trabajo guiado

### Ejercicio 1 — Distribución de ventas
Carga el dataset `ventas_tienda.csv`. Crea un `histplot` de la columna `total_venta` con `kde=True`.

Luego responde:
- ¿La distribución parece simétrica o tiene una cola hacia algún lado?
- ¿La mayoría de las ventas están concentradas en un rango específico?

Modifica el gráfico para usar 20 bins y un color diferente al predeterminado. Agrega título y etiquetas de ejes.

---

### Ejercicio 2 — Boxplot por categoría
Crea un `boxplot` que muestre la distribución de `total_venta` para cada `categoria` de producto.

Luego responde:
- ¿Qué categoría tiene el rango más amplio de ventas?
- ¿Hay categorías con muchos valores atípicos (outliers)?
- ¿La mediana es similar entre categorías o hay diferencias notables?

---

### Ejercicio 3 — Violinplot vs Boxplot
Crea el mismo gráfico que el ejercicio 2 pero usando `violinplot` en lugar de `boxplot`.

Compara ambos gráficos y responde:
- ¿Qué información adicional te da el violinplot que el boxplot no mostraba?
- ¿Hay alguna categoría donde la distribución tenga una forma inusual (dos picos, asimetría fuerte)?

---

### Ejercicio 4 — Barplot por día de la semana
Carga el dataset y asegúrate de que `fecha` esté en formato datetime. Extrae el nombre del día de la semana y crea un `barplot` que muestre el promedio de `total_venta` por día.

Luego responde:
- ¿Qué día de la semana tiene el mayor promedio de ventas?
- ¿Los intervalos de confianza se superponen entre días? ¿Qué dice eso sobre las diferencias?

---

### Ejercicio 5 — Scatterplot con hue
Con el dataset `ventas_tienda.csv`, crea un `scatterplot` con:
- Eje X: `unidades`
- Eje Y: `total_venta`
- Hue: `categoria`

Responde:
- ¿La relación entre unidades y total de venta es lineal en todas las categorías?
- ¿Hay alguna categoría que se comporte de forma diferente a las demás?

---

### Ejercicio 6 — Heatmap de correlación
Calcula la matriz de correlación de las variables numéricas del dataset `ventas_tienda.csv`.

Visualízala con un `heatmap` usando `annot=True` y el colormap `"coolwarm"`.

Luego responde:
- ¿Qué par de variables tiene la correlación más alta?
- ¿Hay alguna variable con correlación cercana a 0 con todas las demás?

---

### Ejercicio 7 — Pairplot de estudiantes
Carga el dataset `estudiantes.csv`. Selecciona las columnas `nota_final`, `asistencia`, `horas_estudio` y `modalidad`.

Crea un `pairplot` con `hue="modalidad"`.

Luego responde:
- ¿Las notas están relacionadas con la asistencia?
- ¿La modalidad (presencial/virtual) parece afectar el rendimiento?

---

### Ejercicio 8 — Gráfico libre
Elige una pregunta que quieras responder sobre cualquiera de los dos datasets y crea el gráfico que mejor responda esa pregunta. Escribe la pregunta como comentario en la primera línea del bloque y escribe debajo una conclusión en 2-3 líneas.

## ✅ Criterios de autocorrección
- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
