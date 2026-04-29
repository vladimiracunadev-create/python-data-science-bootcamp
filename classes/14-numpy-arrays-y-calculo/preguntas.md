# ❓ Preguntas — Clase 14: NumPy — Arrays y cálculo vectorizado

> Preguntas de comprensión, discusión y evaluación para consolidar esta clase.

## 🧠 Preguntas de comprensión

1. ¿Qué es un array de NumPy y en qué se diferencia de una lista de Python? Menciona al menos dos diferencias concretas.
2. ¿Qué significa el atributo `dtype` de un array? ¿Por qué importa que todos los elementos sean del mismo tipo?
3. ¿Cuál es la diferencia entre `np.arange(0, 10, 2)` y `np.linspace(0, 10, 5)`? ¿En qué casos preferirías cada uno?
4. ¿Qué hace `arr[arr > 5]` sobre un array? ¿Cómo se llama esta técnica y en qué se diferencia de un ciclo `for`?
5. Explica con tus propias palabras qué significa el atributo `shape` de un array. ¿Qué diferencia hay entre un array con `shape=(6,)` y uno con `shape=(6, 1)`?

## 💬 Preguntas de discusión

1. ¿Por qué NumPy es mucho más rápido que las listas de Python para operaciones matemáticas? ¿Qué tiene diferente en cómo almacena los datos?
2. Los datos de imágenes digitales se representan como arrays 3D (alto × ancho × canales de color). ¿Cómo se vería una imagen de 100×100 píxeles a color (RGB) como un array de NumPy? ¿Qué `shape` tendría?
3. Si quisieras analizar las ventas diarias de una tienda durante 5 años (365 días × 5 años), ¿cómo organizarías los datos en un array de NumPy? ¿Qué forma le darías y por qué?

## 🧪 Preguntas de código

1. Dado el array `ventas = np.array([150, 230, 180, 310, 275])`, escribe el código para calcular la media, el valor máximo y el índice donde se encuentra ese máximo.
2. Dado `precios = np.array([10, 25, 8, 42, 15, 30])`, escribe el código para obtener solo los precios mayores a 20, y luego calcula cuánto representan de la suma total.
3. Crea un array de 12 números del 1 al 12, reordénalo como una matriz de 3×4 e imprime la suma de cada columna y la media de cada fila.

## 🎯 Pregunta integradora

Tienes un dataset de ventas diarias durante un año (365 días) cargado en un array de NumPy llamado `ventas_diarias`. Describe y escribe el código paso a paso para: (1) calcular el total de ventas de cada semana (asumiendo semanas de 7 días usando `reshape`), (2) encontrar los días con ventas por encima del promedio anual usando filtrado booleano, y (3) calcular qué porcentaje del total anual representan esas ventas altas. Comenta cada parte del código explicando qué hace.
