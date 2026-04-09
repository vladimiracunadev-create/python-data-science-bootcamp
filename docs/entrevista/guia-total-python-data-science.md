# Guía total de estudio: Python con Data Science

> Documento ampliado de estudio personal, construido con el contenido del repositorio y contrastado el 9 de abril de 2026 con documentación oficial de Python, NumPy, pandas, Matplotlib, seaborn, SciPy, scikit-learn y Jupyter, además de programas formales de formación en Data Science con Python.

## Qué es este documento

Este PDF no reemplaza las clases del repositorio. Su función es distinta: darte un mapa completo, profundo y ordenado de todo lo que deberías saber si quieres defender con seguridad una formación orientada a Python con Data Science.

Está pensado como manual de estudio. La idea es que te permita revisar desde fundamentos hasta temas avanzados, sin perder la lógica pedagógica del propio repositorio.

## Cómo estudiarlo

No intentes memorizarlo de una vez. Úsalo en tres niveles:

1. para construir una visión completa del campo;
2. para identificar vacíos concretos;
3. para practicar explicación técnica y pedagógica.

## Parte 1. Mapa general de un curso serio de Python con Data Science

Una ruta formativa robusta debería cubrir como mínimo estos territorios:

- fundamentos de Python;
- entorno de trabajo y notebooks;
- computación numérica con NumPy;
- manipulación y limpieza de datos con pandas;
- visualización con Matplotlib y bibliotecas estadísticas;
- estadística descriptiva e inferencial básica;
- exploración, interpretación y comunicación de hallazgos;
- machine learning con evaluación seria;
- buenas prácticas de código, documentación y reproducibilidad;
- proyecto final o integración aplicada.

Si falta una de estas capas, el curso queda incompleto.

## Parte 2. Fundamentos de Python que debes dominar de verdad

### 2.1 Sintaxis y modelo mental del lenguaje

Debes sentirte cómodo con:

- variables y asignación;
- tipos básicos (`int`, `float`, `str`, `bool`);
- listas, tuplas, conjuntos y diccionarios;
- indexación y slicing;
- operadores aritméticos, lógicos y relacionales;
- condicionales;
- bucles `for` y `while`;
- comprensiones;
- funciones;
- alcance de variables;
- módulos e imports;
- manejo de errores con `try` y `except`.

### 2.2 Lo que importa para Data Science

No basta con “saber Python”. Debes poder explicar por qué estos fundamentos importan para datos:

- una función evita repetir lógica de limpieza o cálculo;
- una lista o diccionario ayuda a modelar registros intermedios;
- un `for` puede servir para iterar, pero muchas veces conviene vectorizar;
- una excepción bien manejada evita romper un pipeline entero;
- nombres claros y comentarios precisos hacen el análisis más auditable.

### 2.3 Temas que elevan el nivel

Además de lo básico, conviene estudiar:

- `lambda`;
- funciones de orden superior;
- iteradores y generadores;
- `pathlib`;
- `datetime`;
- `collections`;
- lectura y escritura de archivos;
- serialización simple (`json`, `csv`);
- ambientes virtuales y dependencias.

## Parte 3. Entorno de trabajo profesional

### 3.1 Jupyter y notebooks

Un curso serio de Python con Data Science debe incluir trabajo con notebooks porque permiten combinar:

- código;
- texto;
- salidas;
- gráficos;
- explicación.

Debes poder explicar:

- qué es un notebook;
- cómo documentar una celda;
- cuándo conviene usar notebook y cuándo script;
- por qué un notebook mal ordenado se vuelve ilegible.

### 3.2 Entornos y dependencias

Debes saber:

- crear un entorno virtual;
- instalar dependencias;
- fijar versiones cuando el proyecto lo exige;
- distinguir entorno local, contenedor y build empaquetado.

### 3.3 Flujo de trabajo mínimo

Un curso serio debería entrenarte en este flujo:

1. preparar entorno;
2. abrir notebook o proyecto;
3. cargar datos;
4. explorar;
5. limpiar;
6. analizar;
7. visualizar;
8. interpretar;
9. guardar evidencia;
10. validar.

## Parte 4. NumPy: el corazón numérico

La documentación oficial de NumPy pone énfasis en:

- creación de arrays;
- tipos de datos;
- indexación;
- broadcasting;
- copias y vistas;
- entrada y salida;
- operaciones vectorizadas.

### 4.1 Conceptos que debes entender

- array multidimensional;
- `dtype`;
- shape;
- axis;
- vectorización;
- broadcasting;
- copia versus vista.

### 4.2 Qué deberías poder hacer

- crear arrays desde listas o rangos;
- seleccionar subconjuntos;
- aplicar operaciones element-wise;
- combinar arrays compatibles;
- usar máscaras booleanas;
- resumir con medias, sumas y agregaciones;
- entender cuándo NumPy es mejor que un bucle puro de Python.

### 4.3 Por qué importa

NumPy no es solo una librería más. Es la base numérica sobre la que se apoyan muchas herramientas del ecosistema, incluidas pandas, SciPy y partes de scikit-learn.

## Parte 5. pandas: manipulación real de datos tabulares

La guía oficial de pandas cubre como áreas centrales:

- estructuras `Series` y `DataFrame`;
- IO;
- selección e indexación;
- `merge`, `join`, `concat`;
- `groupby`;
- tablas pivote;
- datos faltantes;
- texto;
- fechas y series temporales;
- categóricos;
- visualización;
- escalamiento a datos más grandes.

### 5.1 Conceptos esenciales

- `Series`;
- `DataFrame`;
- índice;
- columna;
- filtro;
- dato faltante;
- columna derivada;
- agregación;
- transformación;
- reshaping.

### 5.2 Operaciones mínimas que debes dominar

- `read_csv`;
- `head`, `tail`, `sample`;
- `info`, `describe`;
- selección por columnas;
- filtros booleanos;
- `loc` y `iloc`;
- `isna`, `fillna`, `dropna`;
- `astype`;
- `sort_values`;
- `groupby`;
- `merge`;
- `pivot_table`;
- trabajo con texto;
- trabajo con fechas.

### 5.3 Nivel intermedio obligatorio

Si quieres ir más allá de lo introductorio, también deberías revisar:

- `apply` y cuándo evitarlo;
- funciones vectorizadas;
- operaciones window;
- `MultiIndex`;
- datos categóricos;
- rendimiento;
- lectura y escritura de múltiples formatos.

### 5.4 Error clásico

Muchos creen que usar pandas es “hacer cosas con CSV”. No. Usar pandas bien implica construir una disciplina de inspección, limpieza, transformación y validación.

## Parte 6. Limpieza, calidad y preparación de datos

Una formación seria debe enseñarte a detectar y tratar:

- nulos;
- duplicados;
- categorías inconsistentes;
- fechas mal parseadas;
- tipos incorrectos;
- valores extremos;
- columnas inútiles;
- unidades mezcladas;
- sesgos introducidos por limpieza mal hecha.

### 6.1 Preguntas que siempre debes hacerte

- ¿Qué representa cada fila?
- ¿Qué representa cada columna?
- ¿Qué falta?
- ¿Qué está duplicado?
- ¿Qué está mal tipado?
- ¿Qué transformación es legítima y cuál sería una manipulación engañosa?

### 6.2 Buen criterio

Limpiar no es borrar por reflejo. Limpiar bien significa justificar cada decisión y poder explicarla.

## Parte 7. Visualización de datos

### 7.1 Matplotlib

La documentación oficial de Matplotlib insiste en:

- la relación entre `figure` y `axes`;
- control explícito de elementos visuales;
- gráficos de líneas, barras, dispersión, histogramas y más;
- formato, escalas, leyendas y anotaciones.

Debes poder explicar:

- qué pregunta responde cada tipo de gráfico;
- cómo etiquetar correctamente;
- cómo evitar gráficos decorativos pero inútiles.

### 7.2 seaborn y visualización estadística

La documentación oficial de seaborn enfatiza:

- relaciones entre variables;
- distribuciones;
- comparación por categorías;
- estimación estadística visual;
- elección del gráfico según la pregunta.

Debes conocer al menos:

- histogramas;
- KDE con criterio;
- boxplot;
- violinplot;
- scatterplot;
- lineplot;
- barplot;
- countplot;
- gráficas con `hue`.

### 7.3 Qué significa visualizar bien

Visualizar bien no es “hacer un gráfico bonito”. Es:

- elegir el gráfico correcto;
- reducir ruido;
- dejar claro el mensaje;
- permitir interpretación.

## Parte 8. Estadística que no puede faltar

Una ruta seria de Data Science con Python debe incluir estadística. No necesariamente matemática pesada desde el inicio, pero sí:

- media;
- mediana;
- moda;
- rango;
- varianza;
- desviación estándar;
- percentiles;
- outliers;
- distribuciones;
- muestreo;
- correlación;
- intervalos de confianza;
- pruebas de hipótesis básicas.

### 8.1 Qué deberías poder explicar

- diferencia entre media y mediana;
- por qué un outlier importa;
- diferencia entre correlación y causalidad;
- por qué una muestra puede engañar;
- qué significa una distribución sesgada;
- para qué sirve una prueba básica.

### 8.2 Herramientas

La documentación de SciPy y SciPy Stats muestra que el ecosistema Python también cubre:

- distribuciones de probabilidad;
- estimación;
- pruebas estadísticas;
- KDE;
- estadística descriptiva y funciones de frecuencia.

## Parte 9. Exploración y pensamiento analítico

Muchos cursos enseñan funciones. Un curso serio enseña además a pensar preguntas.

### 9.1 Flujo de análisis

1. definir la pregunta;
2. revisar los datos;
3. limpiar lo necesario;
4. construir métricas;
5. comparar;
6. visualizar;
7. interpretar;
8. comunicar.

### 9.2 Qué debes practicar

- formular preguntas concretas;
- distinguir descripción de explicación;
- justificar qué métrica usas;
- no sobreinterpretar un gráfico;
- cerrar con hallazgo y evidencia.

## Parte 10. Machine Learning que sí debe formar parte del recorrido

La guía oficial de scikit-learn cubre un campo muy amplio. Un curso orientado a Python con Data Science no necesita enseñar todo el catálogo, pero sí estas bases:

- diferencia entre aprendizaje supervisado y no supervisado;
- features y target;
- train, validation y test;
- regresión;
- clasificación;
- métricas;
- overfitting;
- pipelines;
- validación cruzada;
- búsqueda de hiperparámetros.

### 10.1 Conceptos que debes poder explicar

- `train_test_split`;
- generalización;
- fuga de información o leakage;
- pipeline;
- métrica apropiada;
- baseline;
- tuning;
- sesgo-varianza.

### 10.2 Modelos mínimos que conviene conocer

- regresión lineal;
- regresión logística;
- árboles;
- random forest;
- KNN;
- SVM a nivel conceptual;
- clustering básico como tema adicional.

### 10.3 Evaluación seria

La documentación oficial de scikit-learn sobre cross-validation es especialmente importante porque recuerda una idea crítica:

entrenar y evaluar sobre los mismos datos es un error metodológico.

Debes poder explicar:

- por qué se separan datos;
- por qué la validación cruzada ayuda;
- por qué un pipeline evita problemas de preprocesamiento fuera de lugar.

## Parte 11. Ingeniería de características y preprocesamiento

Un curso serio no puede quedarse solo en “entrena el modelo”. También debe cubrir:

- escalado;
- codificación categórica;
- imputación;
- selección de variables;
- columnas derivadas;
- tratamiento de texto;
- fechas como features;
- pipelines de preprocesamiento.

### 11.1 Qué deberías poder decir

- una buena variable puede importar más que un modelo más complejo;
- una mala transformación puede introducir fuga o ruido;
- preprocesamiento y modelado conviene mantenerlos juntos.

## Parte 12. Comunicación de resultados

Un curso bueno no termina en una métrica. Debe enseñarte a traducir resultados a lenguaje útil.

Debes practicar:

- resumen ejecutivo;
- hallazgo con evidencia;
- recomendación;
- explicación oral breve;
- estructura de notebook o informe;
- defensa de decisiones.

### Fórmula útil

hallazgo → evidencia → interpretación → recomendación

## Parte 13. Buenas prácticas de código y proyecto

Una formación madura debe incluir:

- comentarios útiles;
- nombres claros;
- separación de funciones;
- estructura de carpetas;
- control de versiones;
- tests básicos;
- linting;
- documentación;
- reproducibilidad.

### Lo mínimo que debes saber defender

- por qué comentas qué hace y para qué sirve un bloque importante;
- por qué pruebas antes de afirmar que algo funciona;
- por qué una estructura clara importa incluso en proyectos educativos;
- por qué documentación y código no deben contradecirse.

## Parte 14. Temas avanzados que conviene conocer, aunque no todos sean núcleo de una V1

Si el curso quiere ser realmente amplio, conviene que al menos mencione o abra puertas hacia:

- NLP o text mining;
- análisis de redes;
- series de tiempo;
- geodatos;
- SQL y bases de datos;
- dashboards;
- despliegue y APIs;
- cloud;
- MLOps;
- ética de datos;
- privacidad;
- fairness y sesgo algorítmico.

### Regla importante

No todos estos temas deben entrar en una primera implementación escolar. Pero sí es valioso saber que forman parte del ecosistema ampliado de Data Science con Python.

## Parte 15. Cómo aterriza esto en tu propio repositorio

Tu repositorio ya cubre una parte importante de esta ruta:

- fundamentos de Python;
- pandas y limpieza;
- visualización;
- estadística descriptiva;
- mini proyecto;
- comunicación de hallazgos;
- introducción a ML;
- modelos supervisados;
- evaluación y pipelines;
- proyecto final;
- documentación;
- superficies de uso real.

Eso significa que tu base no es liviana. Ya tiene estructura suficiente para una propuesta seria.

## Parte 16. Qué deberías poder explicar en una entrevista después de estudiar esta guía

- qué hace cada superficie del repositorio;
- cómo se enseña dentro de esta base;
- qué temas incluye una ruta seria de Python con Data Science;
- qué temas mostrarías en una V1 y cuáles dejarías para fase 2;
- por qué tu propuesta no es solo enseñar sintaxis;
- qué límites técnicos reconoces hoy;
- cómo conviertes contenido técnico en aprendizaje real.

## Parte 17. Plan sugerido de estudio profundo

### Día 1

- `README.md`
- `docs/CATALOGO_PRODUCTO.md`
- `docs/ARQUITECTURA_PRODUCTO.md`

### Día 2

- fundamentos de Python;
- clase 01;
- parte 2 de esta guía.

### Día 3

- NumPy y pandas;
- clases 02 y 06;
- parte 4 y parte 5.

### Día 4

- visualización y estadística;
- clases 03, 04, 05 y 08;
- parte 7 y parte 8.

### Día 5

- machine learning;
- clases 09, 10 y 11;
- parte 10 y parte 11.

### Día 6

- proyecto final, comunicación y operación;
- clase 12;
- parte 12, 13 y 15.

## Parte 18. Fuentes oficiales y formales revisadas

Estas fuentes fueron consultadas el 9 de abril de 2026 para construir esta guía:

- [Python Tutorial - Python Docs](https://docs.python.org/3/tutorial/index.html?lang=en)
- [Python Documentation Index - Python.org](https://www.python.org/doc/)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Matplotlib Quick Start Guide](https://matplotlib.org/3.7.5/tutorials/introductory/quick_start.html)
- [seaborn Categorical Data Tutorial](https://seaborn.pydata.org/archive/0.12/tutorial/categorical.html)
- [SciPy Statistics Tutorial](https://docs.scipy.org/doc/scipy/tutorial/stats.html)
- [SciPy Statistical Functions Reference](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [scikit-learn Cross-validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Project Jupyter Documentation](https://docs.jupyter.org/en/stable/index.html)
- [Project Jupyter Home](https://jupyter.org/)
- [University of Michigan - Introduction to Data Science in Python](https://online.umich.edu/courses/introduction-to-data-science-in-python/)
- [University of Michigan - Applied Data Science with Python](https://online.umich.edu/series/applied-data-science-with-python/)

## Anexo A. Probabilidad y estadística inferencial que conviene dominar

Un curso serio de Python con Data Science no debería quedarse solo en estadística descriptiva. También conviene construir base en:

- probabilidad básica;
- eventos y reglas elementales;
- distribuciones comunes;
- muestreo;
- error estándar;
- intervalos de confianza;
- pruebas de hipótesis;
- valor p;
- correlación versus causalidad.

### Conceptos que debes poder explicar con palabras simples

- una muestra no es toda la población;
- una media puede moverse por valores extremos;
- correlación no prueba causalidad;
- una diferencia observada puede ser ruido;
- una prueba estadística ayuda a estimar si una señal merece atención, no a reemplazar el criterio.

### Qué deberías practicar

- construir tablas resumen;
- comparar grupos;
- interpretar dispersión;
- leer distribuciones;
- justificar cuándo conviene usar mediana en vez de media;
- explicar por qué un gráfico puede apoyar, pero no reemplazar, una interpretación estadística.

## Anexo B. SQL y acceso a datos

Aunque este repositorio se concentra sobre todo en Python, una formación robusta de Data Science suele incluir al menos una capa básica de SQL porque en la práctica muchos datos viven en bases relacionales.

### Mínimos que deberías conocer

- `SELECT`;
- `WHERE`;
- `ORDER BY`;
- `GROUP BY`;
- `COUNT`, `SUM`, `AVG`;
- `JOIN`;
- subconsultas simples;
- diferencias entre tablas, filas y columnas.

### Por qué importa

- no todos los datos llegan en CSV;
- muchas consultas se deben resolver antes de pasar a pandas;
- saber SQL te permite entender mejor el origen del dato y no trabajar siempre con exportes manuales.

## Anexo C. Diseño de ejercicios y práctica deliberada

Si fueras a enseñar este contenido, no basta con cubrir temas. También debes saber convertirlos en ejercicios con progresión.

### Un buen ejercicio introductorio suele tener

- objetivo pequeño;
- datos o contexto reconocible;
- instrucción precisa;
- resultado verificable;
- espacio para error recuperable.

### Un buen ejercicio intermedio añade

- interpretación;
- justificación de decisiones;
- combinación de dos o más técnicas;
- una pequeña reflexión final.

### Un buen mini proyecto añade

- pregunta inicial;
- recorte del problema;
- limpieza y análisis;
- visualización;
- cierre con hallazgo.

## Anexo D. Evaluación de aprendizaje

Un curso completo necesita medir más que memoria. Conviene evaluar:

- comprensión conceptual;
- ejecución técnica;
- interpretación;
- comunicación;
- autonomía progresiva.

### Formatos útiles

- quiz diagnóstico;
- ejercicios guiados;
- entregas cortas;
- mini proyecto;
- exposición breve;
- rúbrica simple de proceso y resultado.

### Error frecuente

Evaluar solo si el código “corre” es insuficiente. También hay que mirar si la solución tiene sentido, si está explicada y si responde a la pregunta inicial.

## Anexo E. Ética, privacidad y criterio profesional

Hoy no alcanza con enseñar herramientas. También conviene incorporar una conversación mínima sobre:

- privacidad;
- datos sensibles;
- sesgo;
- representatividad;
- consentimiento;
- límites de automatización;
- uso responsable de IA.

### Qué deberías poder decir

- no todo dato disponible debería usarse;
- un dataset puede arrastrar sesgos del mundo real;
- una visualización puede confundir si exagera diferencias;
- un modelo con buena métrica igual puede ser inapropiado en ciertos contextos.

## Anexo F. Despliegue, ciclo de vida y madurez de producto

En una ruta más avanzada, Data Science deja de ser solo análisis exploratorio y empieza a convivir con operación.

### Temas que conviene al menos reconocer

- versionado de código;
- versionado de datos;
- reproducibilidad;
- entornos;
- automatización;
- empaquetado;
- monitoreo;
- documentación técnica;
- mantenimiento.

### Por qué importa para ti

Este repositorio precisamente demuestra un paso más allá del notebook aislado: convierte contenido educativo en una base operativa con app local, app Windows, app Android, portal y documentación por audiencia.

## Anexo G. Portafolio, proyecto final y demostración de dominio

Si quieres mostrar dominio real, conviene poder construir o explicar un proyecto con esta estructura:

1. contexto y problema;
2. datos disponibles;
3. limpieza y criterios;
4. exploración;
5. visualización;
6. modelado, si aplica;
7. evaluación;
8. conclusión;
9. límites;
10. próximos pasos.

### Qué hace fuerte un proyecto final

- que responde una pregunta real;
- que no oculta problemas del dato;
- que usa visualizaciones legibles;
- que justifica las decisiones;
- que diferencia resultado, interpretación y recomendación;
- que está documentado de manera que otra persona pueda seguirlo.

## Anexo H. Glosario mínimo de términos que deberías manejar con naturalidad

- variable;
- observación;
- feature;
- target;
- nulo;
- duplicado;
- agregación;
- distribución;
- correlación;
- outlier;
- escalado;
- imputación;
- leakage;
- baseline;
- overfitting;
- generalización;
- pipeline;
- reproducibilidad;
- métrica;
- validación cruzada.

## Anexo I. Ruta sugerida de estudio intensivo en dos semanas

### Semana 1

1. fundamentos de Python;
2. estructuras de datos;
3. funciones y archivos;
4. NumPy;
5. pandas;
6. limpieza y validación;
7. visualización.

### Semana 2

1. estadística descriptiva e inferencial básica;
2. storytelling con datos;
3. machine learning introductorio;
4. evaluación y pipelines;
5. ética, límites y criterio;
6. revisión del repositorio propio;
7. simulación de entrevista técnica y pedagógica.

## Cierre

Si estudias esta guía bien, no solo vas a poder decir que sabes Python con Data Science. Vas a poder explicar qué contenidos debe tener una formación seria, qué ya cubre tu repositorio, qué podrías ampliar y cómo defender pedagógica y técnicamente esa propuesta.
