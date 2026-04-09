# Guía integrada de estudio del programa

> Documento de estudio construido a partir de las 13 clases del bootcamp. Su objetivo no es explicar el repositorio como producto, sino integrar en un solo texto el contenido real que debes aprender sobre Python y Data Science si quieres dominar lo que el programa enseña.

## Cómo usar esta guía

Este documento no está pensado como un folleto. Está pensado como un manual de estudio. La idea es que puedas leerlo con calma, volver a ciertas secciones, tomar notas al margen y usarlo para preparar clases, entrevistas o una etapa de autoformación más intensa.

Hay dos reglas para aprovecharlo bien. La primera es no estudiar solo definiciones sueltas: cada concepto debe quedar conectado con un uso real. La segunda es no leer Python y Data Science como compartimentos separados. En este programa, la programación se aprende para manipular datos, analizarlos, interpretarlos y comunicarlos.

## Parte 1. Qué enseña realmente este programa

El recorrido del bootcamp no intenta convertir a un estudiante en investigador estadístico ni en ingeniero de producción desde la primera semana. Su propósito es más concreto y más serio: construir una base sólida para trabajar con Python en problemas reales de datos.

Eso significa que el estudiante debería salir pudiendo hacer cuatro cosas con sentido:

1. leer y escribir código Python comprensible;
2. cargar, limpiar y transformar datos tabulares;
3. analizar y visualizar resultados con criterio;
4. iniciar un flujo básico de machine learning sin confundir demostración con rigor.

El valor del programa está en su progresión. No parte con modelos complejos ni con bibliotecas avanzadas. Parte con lectura de código, comentarios, funciones simples, CSV, tablas, métricas, visualizaciones y preguntas concretas. Sobre esa base recién aparecen la predicción, la evaluación y los pipelines.

## Parte 2. El entorno de trabajo que debes dominar

Antes de entrar a pandas o a machine learning, conviene entender dónde se aprende y cómo se trabaja.

### Python no es solo un lenguaje; es un entorno de trabajo

Cuando alguien dice que "aprende Python", en realidad está aprendiendo varias capas a la vez:

- la sintaxis del lenguaje;
- la lógica para resolver problemas;
- la ejecución desde consola, script o notebook;
- la instalación de dependencias;
- la lectura de errores;
- la escritura de código que otra persona pueda entender.

Por eso este programa no se limita a mostrar líneas de código. También obliga a trabajar con notebooks, archivos, comentarios y una forma ordenada de presentar resultados.

### Qué editor o entorno conviene usar

Para este tipo de formación suelen aparecer tres entornos principales:

- `Visual Studio Code`, útil cuando quieres trabajar con scripts, carpetas, terminal integrada, linting, testing y edición de varios archivos;
- `Jupyter Notebook` o `JupyterLab`, útil cuando quieres alternar explicación, código, resultados y gráficos en un mismo documento;
- `Google Colab`, útil cuando quieres ejecutar notebooks sin instalar nada localmente.

No cumplen exactamente la misma función. VS Code es muy bueno para desarrollar hábitos de proyecto. Jupyter es excelente para aprender, explorar y documentar. Colab baja la barrera de entrada cuando no quieres depender de una instalación local completa.

La documentación oficial de Jupyter explica que un notebook combina código, texto, datos y visualizaciones en un mismo documento. Esa idea es clave para este programa: no basta con ejecutar una celda, también hay que explicar qué se hizo y por qué.

### Entorno virtual, dependencias y orden técnico

Una parte importante de aprender Python con seriedad es no mezclar todo en la instalación global del sistema. Para eso se usan entornos virtuales. Un entorno virtual crea un espacio aislado donde puedes instalar versiones de paquetes sin contaminar otros proyectos.

Los comandos mínimos que deberías reconocer son estos:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

¿Qué resuelve esto? Resuelve reproducibilidad. Si un proyecto necesita `pandas`, `numpy`, `matplotlib`, `scikit-learn` y `pytest`, lo correcto es dejar esa dependencia declarada y levantar un entorno propio.

### Reglas de trabajo que sí importan

En este programa, la forma de escribir importa tanto como el resultado. No porque se busque rigidez artificial, sino porque el código educativo tiene que ser legible. Las reglas prácticas son simples:

- nombrar variables y funciones de forma clara;
- comentar bloques importantes cuando el propósito no es obvio;
- dejar una conclusión breve después de un análisis;
- no ejecutar sin leer la salida;
- no copiar soluciones sin poder explicarlas.

Eso conecta con la exigencia transversal de las tareas del bootcamp: no se pide solo que el código "corra", sino que el estudiante deje evidencia de comprensión.

## Parte 3. Fundamentos de Python aplicados a datos

La clase 01 instala la base. Sin esa base, el resto del curso se vuelve memorización de recetas.

### Variables y tipos

Una variable es un nombre que referencia un valor. Aprender esta idea parece básico, pero es la entrada a todo lo demás. Si un estudiante no entiende que una variable guarda un número, una cadena, una lista o un diccionario, después no va a comprender qué está manipulando en un análisis.

Los tipos más importantes al inicio son:

- `int` para enteros;
- `float` para decimales;
- `str` para texto;
- `bool` para verdadero o falso.

En Data Science esto importa porque casi todos los problemas reales exigen distinguir entre números, etiquetas, fechas y categorías. Una columna mal tipada puede arruinar un análisis entero.

### Colecciones

Las listas permiten almacenar una secuencia ordenada de elementos. Los diccionarios permiten guardar pares clave-valor. Ambas estructuras aparecen temprano porque ayudan a pensar cómo se representa información en Python antes de pasar a tablas más complejas.

Una lista puede modelar una secuencia de ventas. Un diccionario puede modelar un registro con campos como producto, precio y cantidad. Entender esto vuelve más natural el salto posterior a `Series` y `DataFrame`.

### Condicionales y bucles

Los `if`, `elif` y `else` permiten tomar decisiones. Los bucles `for` y `while` permiten repetir operaciones. En un curso serio no conviene enseñarlos como puro formalismo. Conviene mostrarlos ligados a preguntas concretas: recorrer registros, filtrar casos, acumular resultados o detectar errores.

El punto pedagógico importante es este: antes de aprender a usar bibliotecas grandes, el estudiante necesita sentir que comprende la lógica básica de un programa.

### Funciones

Una función encapsula lógica reusable. En la clase 01 esto se trabaja con ejemplos simples, como calcular ingresos brutos o transformar datos pequeños. La función enseña cuatro ideas muy poderosas:

- una tarea puede separarse en partes;
- una misma lógica puede reutilizarse;
- el nombre de la función ayuda a leer el programa;
- el retorno hace explícito qué resultado produce el bloque.

Cuando luego el estudiante usa `groupby`, `apply` o un pipeline, ya no está pensando solo en líneas aisladas, sino en procesos.

### Comentarios y explicación del código

El programa insiste en algo que suele omitirse en cursos acelerados: comentar no es decorar. Comentar bien significa aclarar qué hace un bloque y para qué sirve. El comentario debe aportar intención, no repetir literalmente el código.

Por ejemplo, este tipo de comentario es útil:

```python
def calcular_total_bruto(unidades, precio_unitario):
    # Multiplicamos cantidad por precio para estimar el ingreso bruto.
    return unidades * precio_unitario
```

Aquí el comentario ayuda a una persona que todavía no traduce con rapidez la operación matemática a una idea de negocio.

## Parte 4. Cargar, inspeccionar y limpiar datos con pandas

La clase 02 marca un cambio importante. Hasta aquí el estudiante aprendía lógica básica. Desde este punto empieza a trabajar con datos tabulares de manera más realista.

### Qué es pandas y por qué se usa

`pandas` es una biblioteca de Python orientada a manipulación de datos estructurados. Sus estructuras principales son `Series` y `DataFrame`. Un `DataFrame` puede pensarse como una tabla con filas, columnas e índices. Esa imagen es útil, pero incompleta: además de "parecer una planilla", el `DataFrame` permite filtrar, transformar, agrupar, unir y resumir datos con mucha rapidez.

Se usa porque muchas tareas reales de análisis parten así:

- cargar un CSV;
- revisar columnas;
- detectar nulos;
- corregir formatos;
- derivar nuevas variables;
- resumir resultados.

### Inspeccionar antes de analizar

La clase 02 empuja una idea fundamental: antes de graficar o concluir, primero hay que inspeccionar. Eso implica mirar las primeras filas, revisar tipos, contar nulos y detectar inconsistencias evidentes.

Las funciones mínimas que debes dominar son:

- `pd.read_csv()`;
- `head()`;
- `info()`;
- `describe()`;
- `isna()`;
- `fillna()` y `dropna()`.

No basta con saber que existen. Debes entender qué problema resuelven. `head()` permite mirar el comienzo de la tabla y detectar si el archivo parece haber cargado bien. `info()` ayuda a ver tipos y conteos. `isna()` permite medir la ausencia de datos. `fillna()` y `dropna()` representan decisiones distintas: completar o eliminar.

### Qué significa limpiar datos

Limpiar no es "borrar lo feo". Limpiar significa volver el dato más confiable para la pregunta que quieres responder. A veces eso implica estandarizar texto. Otras veces convertir fechas, corregir espacios, unificar categorías o decidir cómo tratar registros incompletos.

Hay una diferencia importante entre limpieza mecánica y limpieza justificada. La primera sigue pasos sin pensar. La segunda pregunta:

- ¿qué representa cada fila?;
- ¿qué significa un valor faltante aquí?;
- ¿conviene imputar, eliminar o dejar explícito el faltante?;
- ¿esta transformación mejora la calidad o está escondiendo un problema?

Ese criterio es uno de los núcleos del programa.

## Parte 5. Exploración, agregación y primeras visualizaciones

Las clases 03 y 05 enseñan una transición importante: pasar de la tabla al patrón visible.

### Agrupar no es solo resumir; es responder preguntas

El corazón de la exploración temprana está en `groupby()`. Agrupar significa reunir filas que comparten una categoría y luego calcular una métrica sobre cada grupo. Por ejemplo:

- ventas por categoría;
- asistencia promedio por curso;
- cantidad de casos por región;
- puntaje medio por nivel.

El grupo por sí solo no dice nada. Lo que da sentido es la pregunta. Si no sabes qué quieres comparar, el `groupby` se vuelve puro procedimiento.

### Métrica, orden y lectura

En la clase 03 el estudiante empieza a entender que un gráfico no nace de la nada. Primero se elige la métrica, luego se agrupa, después se ordena y recién entonces se visualiza. Esa secuencia es valiosa porque rompe la ilusión de que analizar consiste en "hacer clic y ver qué sale".

### Visualización exploratoria

La visualización exploratoria sirve para detectar patrones, contrastes y anomalías. No reemplaza la interpretación. Un gráfico de barras puede mostrar diferencias entre categorías, pero no explica por sí solo por qué existen. Un histograma puede mostrar la distribución de una variable, pero necesita lectura. Un scatter puede sugerir relación entre dos variables, pero no prueba causalidad.

Por eso el programa insiste tanto en conectar gráfico y lenguaje. Cada visualización debería poder responder tres preguntas:

1. ¿qué estoy mostrando?;
2. ¿qué patrón aparece?;
3. ¿qué conclusión sí puedo y no puedo sacar?

### Matplotlib y control explícito

La clase 05 da un paso más allá y enseña a construir gráficos con `matplotlib`. Aquí aparece una diferencia pedagógica muy importante entre "generar un gráfico" y "diseñar un gráfico legible".

Un gráfico útil necesita:

- título;
- etiquetas de ejes;
- escala razonable;
- colores no engañosos;
- leyenda cuando corresponde;
- orden visual.

En términos conceptuales, también conviene entender la diferencia entre `figure` y `axes`. La figura es el lienzo general; los ejes son el área concreta donde se dibuja el gráfico. Dominar esa distinción vuelve al estudiante menos dependiente de funciones de alto nivel.

## Parte 6. Estadística descriptiva y lectura de resultados

La clase 04 introduce la capa estadística del curso. No se trata de formalismo matemático vacío, sino de herramientas para describir datos con mayor precisión.

### Medidas de tendencia central

Las medidas más conocidas son media, mediana y moda. Cada una responde una pregunta distinta.

- La media resume el promedio general, pero puede verse muy afectada por valores extremos.
- La mediana muestra el punto central y es más robusta cuando la distribución está sesgada.
- La moda muestra el valor más frecuente y es útil en ciertos contextos categóricos o discretos.

No se trata solo de memorizar nombres. Se trata de entender cuándo una media engaña y cuándo una mediana describe mejor el centro de la distribución.

### Dispersión y variabilidad

La desviación estándar, el rango y otras medidas de dispersión ayudan a responder cuán concentrados o dispersos están los datos. Dos grupos pueden tener la misma media y, sin embargo, comportamientos completamente distintos. Esa es una lección importante para cualquier análisis serio.

### El paso más importante: interpretar

El programa no presenta estadística descriptiva como una lista de fórmulas. La presenta como lectura de situación. Si la asistencia media es alta pero la dispersión también es alta, entonces el grupo no está siendo estable. Si la mediana de ventas es muy inferior a la media, quizá existen unos pocos valores extremos arrastrando el promedio.

El buen uso de la estadística empieza cuando una medida deja de ser un número aislado y se convierte en argumento.

## Parte 7. Texto, fechas y transformaciones

La clase 06 muestra algo que distingue a un curso práctico de uno demasiado simplificado: en la vida real, los datos rara vez vienen listos para analizar.

### Por qué texto y fechas importan tanto

Muchas preguntas interesantes dependen de columnas textuales o temporales:

- nombres de categorías;
- tipos de producto;
- regiones;
- fechas de compra;
- meses, días, semanas;
- descripciones cortas;
- estados de un proceso.

Si estas columnas vienen mal formateadas, el análisis se vuelve frágil. Espacios extra, diferencias de mayúsculas y minúsculas, fechas como texto o formatos inconsistentes son problemas comunes.

### Transformar es crear variables útiles

Aquí aparece otra idea fuerte: transformar no es alterar por capricho. Transformar significa derivar nuevas columnas que vuelven el dato más analizable.

Ejemplos:

- extraer mes y año desde una fecha;
- normalizar nombres de categorías;
- combinar columnas;
- crear indicadores binarios;
- calcular diferencias entre fechas;
- resumir texto en etiquetas más manejables.

Esta clase es clave porque prepara el terreno para visualizaciones más ricas y, más adelante, para modelado.

## Parte 8. Del ejercicio suelto al mini proyecto

La clase 07 marca un cambio pedagógico muy sano: el estudiante deja de resolver tareas aisladas y empieza a sostener un flujo completo.

### Qué hace que un mini proyecto sea realmente formativo

Un mini proyecto no es un conjunto largo de celdas. Es una secuencia con sentido:

1. definir una pregunta;
2. delimitar un conjunto de datos;
3. preparar y limpiar la base;
4. analizar;
5. visualizar;
6. concluir con evidencia.

Ese orden enseña algo más profundo que una técnica puntual: enseña a pensar en proceso.

### La pregunta manda

Muchos estudiantes creen que hacer Data Science es "usar muchas funciones". El mini proyecto corrige ese error. La pregunta es el centro. Si no sabes qué quieres investigar, la limpieza pierde foco, la visualización se vuelve decorativa y la conclusión se vuelve vaga.

## Parte 9. Presentación de hallazgos

La clase 08 da una lección que suele faltar en programas demasiado técnicos: analizar bien no basta si no puedes comunicar lo encontrado.

### Hallazgo, evidencia, interpretación y recomendación

El curso trabaja una fórmula muy útil:

hallazgo -> evidencia -> interpretación -> recomendación

El hallazgo dice qué observaste. La evidencia muestra de dónde sale. La interpretación explica qué significa. La recomendación propone una acción o una lectura posterior.

Sin esta estructura, el estudiante tiende a dos extremos igual de problemáticos:

- describir gráficos sin concluir nada;
- dar opiniones sin mostrar sustento.

### Qué significa escribir un buen cierre

Un buen cierre no necesita ser largo. Necesita ser claro. Debe dejar explícito:

- cuál era la pregunta;
- qué resultado principal apareció;
- qué límites tiene ese resultado;
- qué harías después.

Ese entrenamiento es crucial tanto para el ámbito académico como para el profesional.

## Parte 10. Introducción a machine learning

La clase 09 introduce machine learning con un criterio correcto: como extensión del análisis, no como magia.

### Qué significa aprender supervisado

En aprendizaje supervisado existe una variable objetivo que quieres predecir a partir de otras variables. Las variables de entrada suelen llamarse `features`, y la variable a predecir suele llamarse `target`.

El estudiante necesita comprender esta estructura antes de aprender nombres de modelos. Si no entiende qué es `X` y qué es `y`, todo lo demás se vuelve fórmula vacía.

### Train/test split

Separar los datos en entrenamiento y prueba enseña una idea metodológica esencial: no evaluar el modelo con los mismos datos usados para ajustarlo. Esta separación no es un detalle técnico menor; es una defensa contra la ilusión de desempeño.

### La meta de esta etapa

La meta de la introducción no es profundidad matemática. La meta es instalar un esquema mental sano:

- formular un problema predictivo;
- elegir variables;
- separar datos;
- entrenar;
- predecir;
- evaluar de manera inicial.

## Parte 11. Modelos supervisados

La clase 10 compara tipos de modelos con foco didáctico.

### Regresión y clasificación

La regresión busca predecir valores numéricos continuos. La clasificación busca predecir categorías o etiquetas. Esta diferencia debe quedar muy clara porque muchas confusiones posteriores nacen de mezclar ambos escenarios.

### Por qué empezar con modelos comprensibles

El programa prioriza modelos que permiten explicar la lógica antes de complejizar. Un árbol de decisión, por ejemplo, puede ser pedagógicamente valioso porque deja ver con más claridad cómo ciertas variables se usan para separar casos. Lo importante aquí no es lucirse con un algoritmo sofisticado, sino entender el flujo.

### Métricas

La idea de métrica entra con más fuerza en esta etapa. No todos los problemas se evalúan igual. En regresión aparecen medidas como error absoluto o error cuadrático. En clasificación aparecen precisión, recall, F1 o accuracy, según el objetivo del problema.

Lo importante no es memorizarlas todas de inmediato, sino entender que el valor de un modelo depende de cómo se juzga.

## Parte 12. Evaluación, leakage y pipelines

La clase 11 es una de las más importantes del tramo final porque corrige errores típicos de cursos superficiales.

### Evaluar mejor

Una sola partición train/test puede no ser suficiente para entender el comportamiento de un modelo. La validación cruzada introduce una visión más robusta: repetir el proceso sobre distintos cortes y observar el comportamiento promedio.

### Qué es leakage

`leakage` o fuga de información ocurre cuando el modelo recibe indirectamente información que no debería tener al momento de predecir. Eso produce resultados artificialmente buenos y conclusiones engañosas.

Esta idea es crítica. Un estudiante que no entiende leakage puede creer que logró un gran modelo cuando en realidad solo contaminó la evaluación.

### Qué resuelve un pipeline

Un `Pipeline` en scikit-learn permite encadenar pasos de preprocesamiento y modelado dentro de una sola estructura. Eso ayuda a mantener consistencia, evita errores manuales y reduce el riesgo de aplicar transformaciones de forma desordenada.

Conceptualmente, el pipeline enseña algo poderoso: un modelo serio no es solo el algoritmo final. También incluye cómo se preparan los datos antes de entrenar.

## Parte 13. Proyecto final y cierre

La clase 12 integra todo lo anterior en una pieza más completa.

### Qué debería mostrar un proyecto final correcto

Un buen proyecto final no necesita ser gigantesco. Necesita ser coherente. Idealmente debería incluir:

- una pregunta clara;
- contexto suficiente del conjunto de datos;
- limpieza explicada;
- análisis con evidencia;
- visualizaciones legibles;
- si corresponde, una aproximación de modelado;
- una conclusión honesta.

### Qué demuestra un buen cierre

Demuestra que el estudiante ya no solo ejecuta pasos. Demuestra que puede sostener una historia analítica completa.

## Parte 14. Lo que debes saber al terminar cada clase

### Clase 00. Diagnóstico inicial y orientación

Debes entender que el diagnóstico no es una formalidad. Sirve para ubicar tu punto de partida, tus vacíos y tu forma de trabajo. Una formación seria no ignora el nivel real del grupo.

### Clase 01. Fundamentos de Python aplicados a datos

Debes poder leer variables, tipos, estructuras básicas, condicionales, bucles y funciones simples. También deberías poder comentar un bloque importante con una idea clara de propósito.

### Clase 02. Pandas y limpieza de datos

Debes poder cargar un CSV, inspeccionarlo, detectar nulos, revisar tipos y hacer una limpieza pequeña pero justificada.

### Clase 03. Visualización exploratoria

Debes poder agrupar, resumir y producir una visualización que responda una pregunta concreta, no solo "muestre algo".

### Clase 04. Estadística descriptiva

Debes poder interpretar media, mediana, dispersión y resumen estadístico básico en relación con un problema real.

### Clase 05. Visualización con matplotlib

Debes poder construir un gráfico legible y explicar por qué su diseño ayuda o entorpece la comprensión.

### Clase 06. Texto, fechas y transformaciones

Debes poder convertir, normalizar y derivar columnas que hagan el análisis más útil.

### Clase 07. Mini proyecto guiado

Debes poder sostener una secuencia analítica completa desde una pregunta hasta una conclusión inicial.

### Clase 08. Presentación de hallazgos

Debes poder comunicar resultados con una estructura clara y sin esconder los límites del análisis.

### Clase 09. Introducción a machine learning

Debes poder explicar la estructura mínima de un flujo supervisado: problema, variables, split, entrenamiento y predicción.

### Clase 10. Modelos supervisados

Debes distinguir regresión de clasificación y entender por qué un modelo se evalúa según el tipo de objetivo.

### Clase 11. Evaluación y pipelines

Debes comprender qué significa validar mejor, por qué existe el leakage y por qué un pipeline mejora la consistencia del flujo.

### Clase 12. Proyecto final y cierre

Debes ser capaz de integrar limpieza, análisis, visualización, comunicación y, si corresponde, modelado en una pieza única y explicable.

## Parte 15. Comandos mínimos del recorrido

Los siguientes comandos no son "la materia", pero sí forman parte del oficio práctico de aprender Python con datos:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
ruff check .
jupyter notebook
```

Cada uno resuelve algo distinto:

- `venv` crea un entorno aislado;
- `pip install -r requirements.txt` instala dependencias del proyecto;
- `pytest` valida comportamiento;
- `ruff check .` revisa estilo y errores frecuentes;
- `jupyter notebook` abre un entorno de trabajo interactivo.

## Parte 16. Bibliotecas y herramientas que debes reconocer durante el recorrido

Aunque el programa está organizado por clases y preguntas, también conviene que tengas claro qué bibliotecas aparecen y por qué.

### `numpy`

No siempre es la primera biblioteca visible para el estudiante, pero está debajo de mucho cálculo numérico en Python. Conviene reconocerla porque introduce arrays, operaciones vectorizadas y una forma más eficiente de trabajar con números que las listas puras.

### `pandas`

Es la biblioteca central del tramo de análisis tabular. Se usa para cargar CSV, revisar columnas, limpiar, filtrar, agrupar y transformar datos. Si tu objetivo es trabajar con ventas, estudiantes, registros o tablas de cualquier tipo, pandas es una herramienta básica.

### `matplotlib`

Es la base de visualización explícita del programa. Importa porque obliga a pensar mejor la construcción de un gráfico: qué se dibuja, con qué ejes, con qué etiquetas y con qué nivel de claridad.

### `scikit-learn`

Aparece en el tramo de machine learning para introducir modelos supervisados, validación y pipelines. No es solo un conjunto de algoritmos; también enseña forma de trabajo: separar variables, entrenar, evaluar y comparar.

### `jupyter`

Es una herramienta de estudio tanto como de ejecución. Permite mezclar código, texto, resultados y gráficos. Eso vuelve posible aprender de forma narrativa y dejar evidencia clara del proceso.

### `pytest` y `ruff`

No son bibliotecas de análisis, pero sí herramientas de calidad. `pytest` ayuda a verificar que funciones o comportamientos básicos sigan correctos. `ruff` ayuda a revisar estilo, errores comunes e imports innecesarios. Aprender a usarlas instala hábitos sanos de trabajo técnico.

## Parte 17. Qué hábitos separan a un estudiante que progresa de uno que solo imita

Hay una diferencia importante entre seguir pasos y aprender de verdad. El estudiante que progresa suele hacer esto:

- formula la pregunta antes de codificar;
- deja comentarios en los bloques importantes;
- relee la salida de cada celda;
- compara resultados antes de concluir;
- reconoce cuando un dato está mal formateado;
- acepta que limpiar y explicar también es parte del análisis.

El estudiante que solo imita suele hacer lo contrario:

- ejecuta sin leer;
- copia sin adaptar;
- confunde gráfico con conclusión;
- cree que el modelo "funciona" sin revisar evaluación;
- ignora nombres, comentarios y estructura.

## Parte 18. Plan de estudio sugerido

### Primera pasada

Haz una lectura rápida de las clases 01 a 06 para consolidar fundamentos, tablas, limpieza, estadística y visualización.

### Segunda pasada

Trabaja las clases 07 a 12 como un tramo integrado, poniendo foco en pregunta, hallazgo, predicción, evaluación y cierre.

### Tercera pasada

Vuelve a los notebooks o ejemplos y obliga a que cada bloque importante tenga una explicación breve de qué hace y para qué sirve.

### Cuarta pasada

Prepara una explicación oral de cinco a diez minutos donde cuentes, sin mirar código, cómo pasas desde datos crudos hasta una conclusión o predicción básica.

## Parte 19. Fuentes internas y externas de apoyo

### Fuentes internas del programa

- `classes/00-diagnostico-inicial/teoria.md`
- `classes/01-python-fundamentos/teoria.md`
- `classes/02-pandas-limpieza-datos/teoria.md`
- `classes/03-visualizacion-exploratoria/teoria.md`
- `classes/04-estadistica-descriptiva/teoria.md`
- `classes/05-visualizacion-con-matplotlib/teoria.md`
- `classes/06-texto-fechas-y-transformaciones/teoria.md`
- `classes/07-mini-proyecto-guiado/teoria.md`
- `classes/08-presentacion-de-hallazgos/teoria.md`
- `classes/09-machine-learning-intro/teoria.md`
- `classes/10-modelos-supervisados/teoria.md`
- `classes/11-evaluacion-y-pipelines/teoria.md`
- `classes/12-proyecto-final-y-cierre/teoria.md`
- `docs/metodologia-docente.md`

### Fuentes oficiales de apoyo consultadas

- [Python Tutorial - Python Docs](https://docs.python.org/3/tutorial/index.html?lang=en)
- [Errors and Exceptions - Python Docs](https://docs.python.org/3.10/tutorial/errors.html)
- [Entornos virtuales y paquetes - Python Docs](https://docs.python.org/es/dev/tutorial/venv.html)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Project Jupyter Documentation](https://docs.jupyter.org/en/latest/index.html)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Matplotlib Quick Start Guide](https://matplotlib.org/3.7.5/tutorials/introductory/quick_start.html)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [scikit-learn Cross-validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)

## Cierre

Si estudias esta guía bien, lo que deberías ganar no es una lista de nombres de bibliotecas. Deberías ganar una comprensión encadenada: Python sirve para expresar lógica; pandas sirve para trabajar con tablas reales; la estadística sirve para describir mejor; la visualización sirve para hacer visible un patrón; el machine learning sirve para extender el análisis hacia predicción; y todo eso solo tiene valor si puedes explicarlo con claridad.
