# 🖥️ Diapositivas sugeridas — Clase 20

> 🖥️ Guion visual breve para conducir la sesión sin sobrecargar la clase.

## 🚪 Apertura

- Pregunta inicial: "¿Cómo decidirías si un estudiante aprobará, usando solo tres preguntas de sí/no?"
- Dibujar en la pizarra un árbol manual con tres niveles.
- Conectar con el dataset de estudiantes: vamos a que la computadora construya ese árbol sola.

## 🛤️ Ruta de la sesión

| Tramo | Tiempo sugerido | Enfoque | Evidencia |
|---|---|---|---|
| Inicio | 10 min | Árbol manual en pizarra | El árbol dibujado con la clase |
| Desarrollo 1 | 20 min | DecisionTreeClassifier + visualización | Árbol impreso en pantalla |
| Desarrollo 2 | 20 min | Sobreajuste y max_depth | Comparación train vs test accuracy |
| Desarrollo 3 | 15 min | RandomForestClassifier + feature importance | Gráfico de importancia |
| Práctica | 15 min | Ejercicio de clasificación | Accuracy entregado |
| Cierre | 10 min | Árbol solo vs bosque: ¿cuál elegirías? | Autoevaluación breve |

## 📌 Puntos que deben quedar claros

- Un árbol demasiado profundo memoriza; un árbol poco profundo generaliza.
- Random Forest = muchos árboles entrenados en subconjuntos aleatorios → votación.
- La importancia de variables nos dice qué preguntas usa más el bosque.
- Random Forest casi siempre supera a un solo árbol.

## 🏁 Cierre esperado

La clase 21 introduce Gradient Boosting, donde los árboles se construyen en secuencia, cada uno corrigiendo los errores del anterior.
