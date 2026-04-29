# 🧪 Ejercicios — Clase 17
> 🧪 Práctica guiada para trabajar en clase y consolidar el aprendizaje.

## 🧱 Antes de empezar
- Lee la consigna completa antes de escribir código.
- Comenta los bloques que no sean obvios.

## 🧭 Trabajo guiado

### Ejercicio 1 — Estadística descriptiva de los grupos
Carga el dataset `transporte.csv`. Separa los registros con lluvia (`lluvia == True`) de los que no tienen lluvia (`lluvia == False`).

Calcula para cada grupo:
- Media de `retraso_min`
- Mediana
- Desviación estándar
- Tamaño de la muestra

¿La diferencia observada en los promedios parece grande o pequeña en relación con la desviación estándar?

---

### Ejercicio 2 — Visualización previa a la prueba
Antes de correr cualquier prueba, crea un `boxplot` o `violinplot` que muestre la distribución de `retraso_min` separado por la columna `lluvia`.

¿La diferencia visual es clara? ¿Los rangos intercuartílicos se superponen mucho?

---

### Ejercicio 3 — Prueba t de Student
Aplica `scipy.stats.ttest_ind` para comparar `retraso_min` entre los grupos con y sin lluvia.

1. Escribe antes de correr el código cuál es tu H0 y cuál es tu H1.
2. Corre la prueba y registra el estadístico t y el p-value.
3. Con alfa = 0.05, ¿rechazas H0 o no?
4. Escribe una conclusión en lenguaje simple que pueda entender alguien sin conocimientos estadísticos.

---

### Ejercicio 4 — Cambiar el umbral alfa
Con los mismos datos del ejercicio anterior, repite la interpretación usando alfa = 0.01 en lugar de 0.05.

¿Cambia la conclusión? ¿Por qué podría importar usar un umbral más estricto?

---

### Ejercicio 5 — Intervalo de confianza
Calcula el intervalo de confianza del 95% para la media de `retraso_min` en días con lluvia.

Luego calcula el intervalo para días sin lluvia.

¿Los dos intervalos se superponen? ¿Qué dice eso sobre la diferencia entre los grupos?

---

### Ejercicio 6 — Notas por curso con prueba t
Carga el dataset `estudiantes.csv`. Elige dos cursos cualesquiera.

Aplica una prueba t para comparar la distribución de `nota_final` entre esos dos cursos.

¿Hay diferencia estadísticamente significativa en el rendimiento promedio entre ellos?

---

### Ejercicio 7 — Prueba chi-cuadrado
Crea una nueva columna en el dataset `estudiantes.csv` que indique si el estudiante aprobó (nota >= 60) o reprobó.

Construye una tabla de contingencia entre `curso` y `aprobado`.

Aplica `scipy.stats.chi2_contingency`. ¿La probabilidad de aprobar depende del curso?

---

### Ejercicio 8 — Reflexión sobre errores
Responde estas preguntas con tus propias palabras:

1. Imagina que realizas una prueba y obtienes p = 0.04. ¿Qué tipo de error podrías estar cometiendo si concluyes que hay una diferencia real?
2. Si en un estudio médico es más grave no detectar una enfermedad que dar una falsa alarma, ¿preferirías minimizar el error tipo I o el tipo II?
3. Si haces 20 pruebas de hipótesis independientes con alfa = 0.05, ¿cuántas positivas esperarías encontrar simplemente por azar?

## ✅ Criterios de autocorrección
- El resultado responde a la pregunta planteada.
- El código está ordenado y comentado en los puntos clave.
- La salida se puede explicar con lenguaje simple.
