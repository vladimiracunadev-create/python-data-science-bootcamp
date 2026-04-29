# 🧪 Ejercicios — Clase 18
> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar
- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.

## 🧭 Trabajo guiado

### Ejercicio 1 — Explorar el dataset antes de transformar
Carga `ventas_tienda.csv` y ejecuta: `.dtypes`, `.isnull().sum()`, `.describe()`.

Escribe en comentarios:
- ¿Qué columnas son numéricas, cuáles son categóricas y cuáles son fechas?
- ¿Hay valores nulos que deban resolverse antes de crear nuevas variables?
- ¿Qué columnas parecen candidatas para generar variables derivadas?

---

### Ejercicio 2 — Variables numéricas derivadas
A partir de `ventas_tienda.csv`, crea las siguientes columnas nuevas:
1. `ingreso_bruto`: precio unitario × unidades vendidas
2. `ingreso_neto`: ingreso bruto × (1 - descuento / 100)
3. `ganancia_por_unidad`: precio unitario - costo unitario
4. `ratio_descuento`: descuento / precio unitario (cuidado con dividir entre cero)

Verifica que los valores tengan sentido imprimiendo las primeras 5 filas de esas columnas.

---

### Ejercicio 3 — Extracción desde fechas
Convierte la columna `fecha` a datetime. Luego crea estas columnas:
- `mes_venta`
- `dia_semana_num` (número, 0=lunes)
- `nombre_dia` (texto: "Lunes", "Martes", etc.)
- `es_fin_semana` (1 si sábado o domingo, 0 si no)
- `trimestre`

¿Cuántas ventas ocurrieron en fin de semana vs días de semana?

---

### Ejercicio 4 — Codificación one-hot
Aplica `pd.get_dummies` a la columna `categoría` del dataset de ventas.

1. ¿Cuántas columnas nuevas se crearon?
2. ¿Por qué en la práctica se elimina una de esas columnas (la primera o la última)?
3. Vuelve a correr con el parámetro `drop_first=True` y compara el resultado.

---

### Ejercicio 5 — Codificación ordinal
En el dataset `estudiantes.csv`, supón que hay una columna `nivel_estudio` con valores: "primaria", "secundaria", "universitario".

Crea un diccionario de mapeo y aplícalo con `.map()` para crear una columna `nivel_cod`.

Si la columna no existe, créala manualmente asignando uno de los tres valores aleatoriamente para practicar.

---

### Ejercicio 6 — Binning con pd.cut y pd.qcut
Con la columna `nota_final` de `estudiantes.csv`:

1. Usa `pd.cut` para crear grupos: [0-49], [50-69], [70-89], [90-100] con etiquetas: "reprobado", "suficiente", "bueno", "excelente".
2. Usa `pd.qcut` para dividir en cuartiles iguales y asignarles etiquetas Q1, Q2, Q3, Q4.

¿Cuántos estudiantes cayeron en cada grupo con cada método? ¿Por qué los resultados son diferentes?

---

### Ejercicio 7 — Escalado de variables
Selecciona 3 columnas numéricas de `ventas_tienda.csv`.

1. Aplica `StandardScaler` y verifica que la media sea ~0 y la desviación estándar ~1.
2. Aplica `MinMaxScaler` y verifica que los valores estén entre 0 y 1.
3. ¿Cuándo preferirías usar uno u otro? Escribe tu razonamiento como comentario.

---

### Ejercicio 8 — Selección por correlación
Con el dataset de estudiantes, calcula la correlación de todas las variables numéricas con `nota_final`.

1. ¿Cuáles son las 3 variables más correlacionadas?
2. ¿Hay variables con correlación menor a 0.05 en valor absoluto? ¿Las eliminarías?
3. ¿Hay alguna variable que esté muy correlacionada con otra variable (no con el target)? ¿Qué harías en ese caso?

## ✅ Criterios de autocorrección
- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
