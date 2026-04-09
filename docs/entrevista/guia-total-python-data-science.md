# Guía total de estudio: Python con Data Science

> Manual ampliado de estudio personal. Este documento no resume solo un curso ni una ruta mínima. Su propósito es darte una visión amplia, ordenada y seria de lo que significa formarse en Python con orientación a Data Science: lenguaje, herramientas, bibliotecas, estadística, análisis, machine learning, comunicación, buenas prácticas y ecosistema profesional.

## Cómo leer esta guía

No la leas como una lista para memorizar. Léela como mapa. Python con Data Science no es un tema único: es un campo compuesto por capas que se apoyan entre sí. Si te quedas solo con la sintaxis, no podrás analizar. Si te quedas solo con bibliotecas, no podrás razonar. Si te quedas solo con gráficos, no podrás defender una conclusión. Si te quedas solo con modelos, no podrás explicar de dónde salió el dato ni por qué el resultado merece confianza.

Esta guía está organizada con una lógica acumulativa. Primero se entiende qué papel juega Python. Luego se revisan los entornos y herramientas. Después se construyen los fundamentos del lenguaje. Más adelante aparecen las bibliotecas numéricas y tabulares, la visualización, la estadística, el machine learning, la comunicación y las capas más amplias del ecosistema.

## Parte 1. Qué es realmente Data Science y por qué Python ocupa un lugar central

Data Science no es una sola disciplina. Es una práctica que combina preguntas, datos, programación, estadística, visualización, modelado y comunicación. En contextos reales también incorpora documentación, control de versiones, criterios éticos y, muchas veces, despliegue o automatización.

Python ocupa un lugar central porque permite transitar varias capas del trabajo con una misma base:

- sirve para programar;
- sirve para leer y transformar datos;
- sirve para visualizar;
- sirve para construir modelos;
- sirve para automatizar procesos;
- sirve para conectar con bases de datos, APIs y aplicaciones.

Su fuerza no está solo en la sintaxis. Está en su ecosistema. Alrededor del lenguaje existe una red enorme de bibliotecas y herramientas que hacen posible pasar desde un CSV simple hasta un pipeline de entrenamiento, una aplicación de visualización o un cuaderno reproducible.

## Parte 2. El entorno de trabajo: dónde y cómo se aprende

Antes de hablar de modelos, conviene entender con qué herramientas se trabaja.

### Scripts, terminal y proyectos

Un script de Python es un archivo `.py` ejecutable. Trabajar con scripts enseña orden, modularidad y separación de responsabilidades. Un proyecto bien organizado suele tener carpetas, dependencias, tests, documentación y comandos reproducibles.

La terminal importa porque permite ejecutar el proyecto, instalar paquetes, correr pruebas y entender cómo funciona el entorno más allá de un botón gráfico.

### Jupyter Notebook y JupyterLab

La documentación oficial de Jupyter explica que un notebook combina código, texto, visualizaciones y resultados en un mismo documento. Esa combinación lo vuelve especialmente útil para enseñanza, exploración, prototipado y análisis narrado.

¿Por qué importa tanto en Data Science?

Porque el análisis de datos no consiste solo en producir un resultado final. También consiste en mostrar el camino. Un notebook bien trabajado deja visible:

- la pregunta;
- la carga de datos;
- la limpieza;
- la transformación;
- la evidencia visual;
- la interpretación.

JupyterLab amplía esa experiencia con una interfaz más completa: paneles, archivos, terminal, visores y trabajo multipestaña.

### Visual Studio Code

VS Code es especialmente fuerte cuando quieres pasar desde exploración a proyecto. Su valor en una ruta de Python con Data Science está en que combina:

- editor de scripts;
- notebooks integrados;
- terminal;
- extensiones de Python y Jupyter;
- navegación de archivos;
- depuración;
- integración con Git.

La documentación oficial de VS Code para Data Science muestra precisamente ese puente entre notebook, exploración y proyecto reproducible.

### Google Colab

Colab es una variante muy útil cuando quieres empezar rápido, compartir notebooks o evitar una instalación local. Está basado en notebooks alojados y permite ejecutar código desde el navegador. En formación inicial tiene ventajas evidentes:

- cero instalación local;
- facilidad para compartir;
- acceso simple desde múltiples dispositivos;
- buen punto de entrada para estudiantes.

Sin embargo, también conviene entender sus límites: depende de conectividad, del entorno alojado y de una sesión externa que no siempre controla el usuario.

### Entornos virtuales y dependencias

La documentación oficial de Python sobre `venv` es clave para entender por qué no conviene instalar todo globalmente. Un entorno virtual aísla dependencias y permite que un proyecto tenga su propia combinación de paquetes.

Los comandos mínimos son estos:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Esto no es burocracia. Es una forma de mantener orden y reproducibilidad. Si no gestionas tus entornos, tarde o temprano un proyecto deja de funcionar porque una versión cambió o porque mezclaste dependencias incompatibles.

## Parte 3. Fundamentos del lenguaje Python que debes dominar

Una formación seria en Data Science no puede saltarse la base del lenguaje. Quien intenta aprender solo funciones de bibliotecas sin entender Python termina copiando sin criterio.

### Variables, nombres y modelo mental

Una variable es un nombre que referencia un valor. Esta idea parece simple, pero instala la base del pensamiento programático: dar nombre, manipular, transformar y volver a usar.

Los nombres importan. Un nombre como `ventas_totales` comunica más que `x`. La legibilidad importa porque el código será leído muchas más veces de las que será escrito, como recuerda PEP 8.

### Tipos de datos

Los tipos básicos son `int`, `float`, `str` y `bool`. A eso se suman estructuras más ricas como listas, tuplas, conjuntos y diccionarios.

¿Por qué esto importa en Data Science? Porque casi todos los errores de análisis pasan por tipos mal interpretados:

- números leídos como texto;
- fechas leídas como cadenas;
- categorías mezcladas con valores nulos;
- variables binarias mal representadas.

Quien domina tipos domina mejor la limpieza y la transformación.

### Estructuras de datos básicas

Las listas almacenan secuencias ordenadas. Los diccionarios almacenan pares clave-valor. Las tuplas representan agrupaciones inmutables. Los conjuntos ayudan con operaciones de membresía y unicidad.

Estas estructuras son importantes incluso cuando luego se trabaja con pandas. No desaparecen. Siguen apareciendo en configuración, recorridos, transformaciones intermedias, parámetros y lógica auxiliar.

### Condicionales

Los condicionales permiten tomar decisiones. En un análisis real, esto aparece en reglas simples como:

- marcar un estudiante en riesgo si la asistencia cae bajo cierto umbral;
- etiquetar una venta como alta si supera un monto;
- decidir qué tratamiento aplicar a un valor faltante.

No se trata solo de aprender `if` y `else`. Se trata de entender cómo una regla se vuelve código.

### Bucles

Los bucles `for` y `while` enseñan repetición y control. En Data Science muchas operaciones pueden vectorizarse, y de hecho eso suele ser preferible. Pero comprender el bucle sigue siendo valioso porque construye intuición sobre iteración, recorrido y acumulación.

### Funciones

La función es una de las unidades más importantes de la programación. Encapsula comportamiento y reduce repetición. En un trabajo de datos, una función puede servir para:

- limpiar un campo;
- calcular una métrica;
- validar una tabla;
- transformar fechas;
- empaquetar un pequeño proceso reutilizable.

Dominar funciones ayuda a pasar de notebooks improvisados a análisis con más estructura.

### Módulos y paquetes

Un módulo es un archivo de Python con funciones, clases o variables. Un paquete es una agrupación de módulos. Entender imports, rutas y organización del código es clave para construir proyectos sostenibles.

### Manejo de errores

La documentación oficial de Python sobre errores y excepciones recuerda una idea central: los programas no solo deben funcionar cuando todo sale bien; también deben responder razonablemente cuando algo falla.

En Data Science esto importa muchísimo. Los errores comunes incluyen:

- archivos no encontrados;
- columnas ausentes;
- conversiones fallidas;
- valores inválidos;
- divisiones por cero;
- modelos entrenados con entradas mal formadas.

Aprender `try`, `except` y una lectura correcta de tracebacks vuelve al estudiante más autónomo.

### Archivos, rutas y datos externos

Trabajar con datos exige leer y escribir archivos. Aquí aparecen `pathlib`, CSV, JSON, Excel y, en escenarios más amplios, bases de datos o APIs.

Quien entiende archivos y rutas entiende mejor cómo entra el dato al sistema.

## Parte 4. Reglas de programación que hacen una diferencia real

Python con Data Science no debería enseñarse como si cualquier código bastara. Hay reglas de oficio que mejoran muchísimo la calidad del trabajo.

### PEP 8 y legibilidad

PEP 8 no es una ley absoluta, pero sí una referencia muy útil. Lo más valioso del documento no es recordar números exactos, sino su idea central: escribir código legible y consistente.

Eso implica, por ejemplo:

- nombres claros;
- espacios consistentes;
- imports ordenados;
- funciones y módulos con nombres comprensibles;
- comentarios que no contradigan el código.

### Docstrings y documentación

PEP 257 formaliza buenas prácticas para docstrings. En un proyecto de datos, una docstring puede explicar:

- qué hace una función;
- qué parámetros recibe;
- qué devuelve;
- qué supuestos tiene.

Esto no solo mejora mantenimiento. También mejora aprendizaje, porque obliga a pensar qué se espera realmente de un bloque de código.

### Comentarios útiles versus comentarios inútiles

Un mal comentario repite lo obvio. Un buen comentario explica intención, motivo o criterio.

Ejemplo malo:

```python
x = x + 1  # suma 1
```

Ejemplo mejor:

```python
x = x + 1  # Compensamos el desfase del índice de origen.
```

### Testing y validación

No todo proyecto educativo necesita una infraestructura de pruebas complejísima, pero sí conviene enseñar que validar es parte del oficio. Incluso un test pequeño puede proteger contra errores de transformación o supuestos rotos.

### Linting

Herramientas como `ruff` ayudan a detectar errores frecuentes, imports innecesarios, problemas de estilo y otras señales tempranas. No reemplazan pensamiento, pero sí refuerzan disciplina.

### Git y control de versiones

La documentación oficial de Git explica la lógica de importar un proyecto, cambiar archivos y compartir cambios. En una formación moderna, Git importa porque:

- permite volver atrás;
- deja historia de cambios;
- favorece colaboración;
- obliga a pensar en unidades de trabajo.

Los comandos mínimos que conviene conocer son:

```bash
git status
git add .
git commit -m "mensaje"
git push
```

No se trata de convertir Git en tema central del curso, pero sí de entenderlo como parte del trabajo profesional.

## Parte 5. El núcleo numérico: NumPy

`NumPy` es una de las bases del ecosistema científico de Python. Su importancia no está solo en ofrecer arreglos más rápidos que las listas. Está en proporcionar una estructura eficiente para cálculo numérico y servir de soporte a muchas otras bibliotecas.

### Qué es un array

Un `ndarray` es una estructura homogénea y multidimensional. Homogénea significa que sus elementos comparten tipo. Multidimensional significa que puede representar vectores, matrices o tensores más generales.

### Conceptos fundamentales

Los conceptos más importantes son:

- `shape`, que describe dimensiones;
- `dtype`, que describe el tipo interno;
- indexación y slicing;
- operaciones vectorizadas;
- broadcasting;
- diferencia entre copia y vista.

### Por qué NumPy es importante

NumPy permite expresar operaciones matemáticas sobre conjuntos completos de datos sin depender de bucles explícitos en Python puro. Esa vectorización suele ser más clara y eficiente.

### Broadcasting

La guía oficial de NumPy sobre broadcasting es especialmente importante porque enseña cómo operar entre arreglos de formas compatibles. Esta idea reaparece constantemente, incluso cuando el estudiante no la nombra explícitamente.

### Cuándo aparece en la práctica

Aunque muchos principiantes entren por pandas, NumPy sigue apareciendo debajo de muchas operaciones. También importa en álgebra lineal, simulación, procesamiento numérico, preparación de matrices y modelado.

## Parte 6. El corazón del trabajo tabular: pandas

Si NumPy es el núcleo numérico, `pandas` suele ser la puerta de entrada al trabajo cotidiano con datos estructurados.

### Series y DataFrame

Una `Series` representa una secuencia indexada de valores. Un `DataFrame` representa una tabla bidimensional con índice y columnas. Entender estas estructuras es fundamental porque casi toda la limpieza y exploración inicial se apoya en ellas.

### Carga y lectura de datos

La guía oficial de pandas cubre múltiples formas de entrada y salida: CSV, Excel, parquet, SQL y más. En una primera etapa de estudio conviene dominar bien CSV y luego entender que el ecosistema real es mucho más amplio.

### Selección e indexación

Saber usar `loc`, `iloc`, selección por columnas y filtros booleanos no es detalle menor. Es la forma concreta de preguntar sobre la tabla.

### Valores faltantes

Los valores faltantes son uno de los temas más delicados del análisis. No basta con detectarlos. Hay que decidir qué hacer con ellos:

- eliminarlos;
- imputarlos;
- señalarlos;
- cambiar el tipo de análisis;
- volver al origen del dato si es posible.

Una decisión incorrecta sobre faltantes puede distorsionar todo el resultado.

### Transformación y limpieza

Aquí aparecen tareas comunes como:

- renombrar columnas;
- corregir tipos;
- estandarizar texto;
- convertir fechas;
- reemplazar categorías;
- derivar nuevas variables.

### GroupBy, merge y pivot

Estas operaciones representan saltos conceptuales importantes.

- `groupby` permite resumir por grupos;
- `merge` permite combinar tablas;
- `pivot_table` permite reorganizar resúmenes y comparaciones.

Quien domina estas tres familias ya puede resolver una enorme cantidad de problemas reales de análisis.

### Texto, categorías y fechas

Una formación madura en pandas no se limita a columnas numéricas. También debe cubrir:

- operaciones con cadenas;
- tipos categóricos;
- parsing de fechas;
- series temporales básicas.

Eso amplía radicalmente el tipo de preguntas que pueden abordarse.

## Parte 7. Visualización: hacer visible lo que el dato sugiere

Una buena formación no enseña gráficos como decoración. Enseña visualización como herramienta de pensamiento y de comunicación.

### Matplotlib

La documentación oficial de Matplotlib pone mucho énfasis en la relación entre `figure` y `axes`, además de mostrar cómo construir gráficos de línea, dispersión, barras, histogramas y más.

Su fuerza está en el control explícito. Permite ajustar detalles de formato, escalas, anotaciones, tamaños, paneles y exportación.

### Seaborn

`seaborn` ofrece una capa de visualización estadística de alto nivel sobre Matplotlib. Suele ser muy útil para:

- comparaciones categóricas;
- distribuciones;
- relaciones entre variables;
- visualización más rápida de patrones comunes.

Su valor está en simplificar tareas frecuentes y ofrecer defaults más agradables, pero sin reemplazar la necesidad de comprender qué se está mostrando.

### Plotly y visualización interactiva

Cuando el foco cambia desde análisis local a presentación interactiva, `plotly` se vuelve relevante. Permite gráficos navegables, tooltips, zoom y experiencias más cercanas a dashboard.

No siempre es la primera biblioteca a enseñar, pero sí conviene conocerla porque ocupa un lugar importante en comunicación de resultados.

### Qué hace bueno a un gráfico

Un gráfico bueno responde con honestidad a una pregunta. Eso supone:

- escoger el tipo correcto;
- no exagerar diferencias;
- rotular ejes;
- poner contexto;
- evitar colorido innecesario;
- distinguir exploración de comunicación final.

## Parte 8. Estadística: el puente entre dato y argumento

Data Science sin estadística se vuelve superficial. Estadística sin contexto se vuelve abstracta. Lo importante es la conexión entre ambas.

### Estadística descriptiva

La primera capa incluye:

- media;
- mediana;
- moda;
- rango;
- varianza;
- desviación estándar;
- percentiles;
- distribuciones.

Estas medidas sirven para describir, comparar y empezar a interpretar.

### Probabilidad y muestreo

Más adelante conviene comprender conceptos como:

- evento;
- probabilidad;
- independencia;
- distribución;
- muestra versus población;
- error estándar.

Sin esta base es muy difícil entender inferencia o evaluación rigurosa.

### Inferencia y pruebas

Una ruta más completa debería tocar, al menos conceptualmente:

- intervalos de confianza;
- pruebas de hipótesis;
- valor p;
- error tipo I y tipo II;
- tamaño de efecto.

No para convertir cada estudiante en especialista estadístico, sino para evitar una cultura de análisis basada solo en "miré el promedio y listo".

### SciPy y statsmodels

`SciPy` aporta funciones estadísticas, distribuciones y utilidades numéricas más amplias. `statsmodels` aporta herramientas muy valiosas cuando el foco está en inferencia, modelos estadísticos clásicos y diagnósticos de regresión.

Conocer estas bibliotecas amplía mucho la idea de lo que Python puede hacer más allá del stack introductorio.

## Parte 9. Exploratory Data Analysis: pensar antes de modelar

El análisis exploratorio de datos, o EDA, es una fase donde el objetivo no es predecir todavía, sino entender.

### Qué preguntas se hacen en EDA

- ¿qué representa cada fila?;
- ¿qué representa cada columna?;
- ¿qué falta?;
- ¿qué está duplicado?;
- ¿qué distribuciones aparecen?;
- ¿qué outliers merecen revisión?;
- ¿qué relaciones parecen relevantes?;
- ¿qué problemas de calidad impiden avanzar?

### Qué evita un buen EDA

Evita modelar a ciegas. Evita construir conclusiones sobre datos mal entendidos. Evita usar métricas sin contexto.

### Qué produce un buen EDA

Produce hipótesis mejores, limpieza más justificada, visualizaciones más informativas y decisiones de modelado mejor orientadas.

## Parte 10. Machine Learning: cuándo y cómo entra de verdad

No todo problema de datos necesita machine learning. Pero una formación orientada a Data Science sí debería enseñar cuándo empieza a tener sentido.

### Supervised y unsupervised

La primera gran distinción es entre aprendizaje supervisado y no supervisado.

- En el supervisado existe una variable objetivo.
- En el no supervisado se buscan estructuras, grupos o relaciones sin etiqueta final explícita.

En una ruta inicial suele entrar primero el supervisado porque es más fácil de conectar con preguntas concretas de predicción.

### Framing del problema

Antes de elegir algoritmo, hay que formular bien el problema:

- ¿qué quieres predecir?;
- ¿con qué variables?;
- ¿para qué decisión?;
- ¿con qué costo de error?;
- ¿qué significa éxito aquí?

Sin ese encuadre, elegir modelo es casi azar.

### Preprocesamiento

Aquí entran tareas como:

- imputación;
- escalado;
- codificación categórica;
- selección de variables;
- creación de features.

Una gran parte del trabajo útil ocurre antes del modelo.

### Modelos básicos que conviene conocer

En una primera formación seria conviene entender al menos:

- regresión lineal;
- regresión logística;
- árboles de decisión;
- random forest;
- KNN;
- SVM a nivel conceptual;
- clustering básico como extensión.

No necesitas dominarlos todos con la misma profundidad, pero sí reconocer qué problemas intentan resolver y qué trade-offs tienen.

### Métricas

Una métrica correcta depende del problema.

Para regresión conviene comprender ideas como:

- MAE;
- MSE;
- RMSE;
- R².

Para clasificación conviene comprender:

- accuracy;
- precision;
- recall;
- F1;
- matriz de confusión;
- ROC-AUC en contextos más avanzados.

### Validación cruzada y generalización

La documentación oficial de scikit-learn sobre cross-validation es una referencia obligada. Enseña una idea central: un modelo no vale por lo bien que recuerda los datos vistos, sino por lo bien que generaliza.

### Leakage

La fuga de información es uno de los errores más dañinos y más subestimados. Si preprocesas con información del conjunto completo antes de separar, o si una variable revela indirectamente la respuesta, la evaluación deja de ser confiable.

### Pipelines

Los pipelines ayudan a encapsular preprocesamiento y modelo dentro de una misma estructura reproducible. Son pedagógicamente valiosos porque enseñan que el flujo analítico serio no termina en un `fit()`.

## Parte 11. Deep Learning y el ecosistema ampliado

Una guía total no puede fingir que Data Science termina en scikit-learn.

### TensorFlow y PyTorch

Cuando el problema escala hacia redes neuronales, visión computacional profunda, procesamiento de lenguaje a gran escala o secuencias más complejas, suelen aparecer marcos como `TensorFlow` y `PyTorch`.

No todos los cursos introductorios deben incluirlos como núcleo, pero sí conviene saber por qué existen:

- modelan arquitecturas neuronales complejas;
- aprovechan aceleración en GPU;
- se usan muchísimo en aprendizaje profundo.

### NLP

El procesamiento de lenguaje natural en Python puede apoyarse en bibliotecas como:

- `spaCy`;
- `NLTK`;
- ecosistemas de transformadores más recientes.

Aquí entran tareas como tokenización, lematización, clasificación de texto, extracción de entidades y embeddings.

### Visión por computador

Bibliotecas como `OpenCV` y marcos de deep learning permiten trabajar con imágenes, detección, clasificación y segmentación. Esto ensancha enormemente el campo de Data Science más allá de tablas.

## Parte 12. Big Data y escalamiento

Cuando los datos crecen demasiado para una sola máquina o para flujos simples en memoria, aparecen herramientas de otra escala.

### Dask y PySpark

`Dask` permite paralelizar y escalar ciertos flujos en Python manteniendo una sintaxis cercana al ecosistema conocido. `PySpark` conecta con el mundo de Apache Spark para trabajo distribuido, DataFrames a gran escala y pipelines más robustos.

No son herramientas de entrada para un principiante absoluto, pero sí forman parte del mapa que conviene conocer si alguien quiere entender el mundo completo de Python con Data Science.

## Parte 13. Bases de datos, SQL y acceso a datos

Un error común en formación muy centrada en notebooks es olvidar que gran parte del dato real no vive en CSV.

### SQL

Aunque SQL no sea "Python", forma parte del trabajo de muchos perfiles de datos. Conviene conocer:

- `SELECT`;
- `WHERE`;
- `GROUP BY`;
- `ORDER BY`;
- `JOIN`;
- funciones de agregación.

### Bibliotecas y conectores

En Python pueden aparecer bibliotecas como:

- `sqlalchemy` para conexión y modelado de acceso a bases;
- conectores específicos de PostgreSQL, MySQL o SQLite;
- `requests` para trabajar con APIs.

Esto amplía el tipo de fuentes de datos que puedes integrar.

## Parte 14. Comunicación, dashboards y productos ligeros de datos

Data Science no termina cuando termina el análisis. Muchas veces recién ahí empieza la parte más visible.

### Streamlit

`Streamlit` se volvió popular porque permite construir aplicaciones ligeras de datos escribiendo Python casi como si fuera un script normal. Es especialmente útil para prototipos, demostraciones, paneles simples y productos internos.

### Dash y ecosistemas interactivos

El ecosistema de `Plotly` también permite construir visualizaciones y aplicaciones interactivas más elaboradas.

### Qué hace buena a una salida comunicable

Una buena salida final no depende solo de lo "bonito". Depende de:

- claridad;
- foco;
- capacidad de responder una pregunta;
- relación honesta entre evidencia y conclusión;
- facilidad para ser entendida por otra audiencia.

## Parte 15. Reproducibilidad, calidad y trabajo profesional

Una formación moderna debería incluir algo más que análisis puntual. También debería enseñar cómo sostener ese trabajo.

### Reproducibilidad

Reproducir significa que otra persona pueda seguir el proceso y llegar razonablemente al mismo resultado. Para eso ayudan:

- entornos virtuales;
- dependencias declaradas;
- notebooks ordenados;
- scripts reutilizables;
- control de versiones;
- documentación.

### Testing y validación

No todo análisis necesita una suite grande de tests, pero sí conviene cultivar una cultura de comprobación. Esto puede incluir:

- tests de funciones auxiliares;
- validación de supuestos sobre columnas;
- chequeos de integridad del dato;
- revisión de resultados esperados.

### Documentación

La documentación no es un adorno final. Es parte del producto intelectual. Un buen analista documenta no solo qué corrió, sino también por qué decidió limpiar, agrupar, modelar o descartar ciertas rutas.

## Parte 16. Ética, sesgo y criterio profesional

Una guía seria no puede omitir esta capa.

### Por qué importa

Trabajar con datos implica trabajar con representaciones incompletas del mundo. Esos datos pueden contener sesgos de origen, problemas de medición, vacíos importantes o variables sensibles.

### Preguntas que siempre conviene hacer

- ¿de dónde salió el dato?;
- ¿qué población representa y cuál deja fuera?;
- ¿qué sesgos puede arrastrar?;
- ¿qué impacto tiene un error aquí?;
- ¿qué daño puede causar una clasificación incorrecta?;
- ¿qué variables son sensibles o delicadas?

### IA y automatización

Hoy es fácil usar asistentes, generación automática de código y herramientas de apoyo. Eso puede ser útil, pero no reemplaza criterio. Una formación sana debería enseñar a usar ayuda externa sin abdicar del razonamiento.

## Parte 17. Qué bibliotecas de Python conviene al menos reconocer por familias

No necesitas dominar todas estas herramientas de inmediato, pero sí conviene saber qué lugar ocupan.

### Núcleo científico y análisis

- `numpy`: cálculo numérico y arrays;
- `pandas`: datos tabulares;
- `scipy`: funciones científicas y estadísticas;
- `statsmodels`: inferencia, modelos estadísticos y diagnósticos.

### Visualización

- `matplotlib`: control explícito de gráficos;
- `seaborn`: visualización estadística de alto nivel;
- `plotly`: visualización interactiva.

### Machine learning

- `scikit-learn`: modelos clásicos, evaluación, preprocessing y pipelines.

### Deep learning

- `tensorflow`;
- `pytorch`.

### NLP

- `spacy`;
- `nltk`.

### Visión

- `opencv`.

### Apps de datos y visualización operativa

- `streamlit`;
- `dash`.

### Escalamiento y big data

- `dask`;
- `pyspark`.

### Acceso a datos y servicios

- `sqlalchemy`;
- conectores SQL;
- `requests`.

### Calidad y desarrollo

- `pytest`;
- `ruff`.

## Parte 18. Qué deberías saber explicar después de estudiar esta guía

Si estudias esta guía a fondo, deberías poder explicar con claridad:

- qué es Data Science más allá de una moda;
- por qué Python es tan relevante en el área;
- qué función cumple cada entorno de trabajo;
- cómo se relacionan scripts, notebooks y proyectos;
- qué problema resuelven NumPy, pandas, Matplotlib, seaborn y scikit-learn;
- por qué la estadística no puede omitirse;
- por qué limpiar datos no es un paso trivial;
- por qué modelar sin validación es metodológicamente frágil;
- qué bibliotecas amplían el campo hacia NLP, visión, dashboards o escalamiento;
- qué hábitos vuelven reproducible y profesional un trabajo de datos.

## Parte 19. Ruta sugerida de estudio profundo

### Semana 1: base técnica

1. sintaxis y fundamentos de Python;
2. tipos de datos, funciones, errores y archivos;
3. entornos virtuales y flujo de trabajo básico;
4. notebooks y VS Code.

### Semana 2: análisis tabular

1. NumPy;
2. pandas;
3. limpieza;
4. groupby, merge y pivot;
5. fechas y texto.

### Semana 3: estadística y visualización

1. estadística descriptiva;
2. muestreo y nociones inferenciales;
3. Matplotlib;
4. seaborn;
5. lectura crítica de gráficos.

### Semana 4: modelado y evaluación

1. framing del problema;
2. modelos supervisados básicos;
3. métricas;
4. validación cruzada;
5. leakage y pipelines.

### Semana 5: ecosistema ampliado

1. statsmodels y SciPy;
2. SQL y acceso a datos;
3. Streamlit y comunicación;
4. PyTorch o TensorFlow a nivel conceptual;
5. PySpark o Dask a nivel conceptual.

### Semana 6: integración

1. construir o revisar un mini proyecto completo;
2. documentar el proceso;
3. preparar una explicación oral del flujo;
4. identificar vacíos concretos para la siguiente etapa.

## Parte 20. Fuentes oficiales y formales consultadas

Estas fuentes fueron revisadas el 9 de abril de 2026 para construir esta guía ampliada:

- [Python Tutorial - Python Docs](https://docs.python.org/3/tutorial/index.html?lang=en)
- [Errors and Exceptions - Python Docs](https://docs.python.org/3.10/tutorial/errors.html)
- [Entornos virtuales y paquetes - Python Docs](https://docs.python.org/es/dev/tutorial/venv.html)
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)
- [Project Jupyter Documentation](https://docs.jupyter.org/en/latest/index.html)
- [VS Code Data Science Tutorial](https://code.visualstudio.com/docs/datascience/data-science-tutorial)
- [Google Colab FAQ](https://research.google.com/colaboratory/faq.html?hl=es)
- [NumPy User Guide](https://numpy.org/doc/stable/user/)
- [pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- [Matplotlib Quick Start Guide](https://matplotlib.org/3.7.5/tutorials/introductory/quick_start.html)
- [seaborn tutorial](https://seaborn.pydata.org/archive/0.11/tutorial/categorical.html)
- [SciPy Statistical Functions Reference](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [statsmodels Getting Started](https://www.statsmodels.org/v0.12.2/gettingstarted.html)
- [scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [scikit-learn Cross-validation Guide](https://scikit-learn.org/stable/modules/cross_validation.html)
- [Streamlit Main Concepts](https://docs.streamlit.io/get-started/fundamentals/main-concepts)
- [Git Tutorial - git-scm](https://git-scm.com/docs/gittutorial/2.8.6)
- [University of Michigan - Introduction to Data Science in Python](https://online.umich.edu/courses/introduction-to-data-science-in-python/)
- [University of Michigan - Applied Data Science with Python](https://online.umich.edu/series/applied-data-science-with-python/)

## Cierre

Python con Data Science no es una colección de comandos. Es un campo de trabajo que une razonamiento, herramientas y criterio. El lenguaje es importante, pero no alcanza. Las bibliotecas son poderosas, pero no piensan por ti. Los modelos son útiles, pero no reemplazan comprensión del dato. Los dashboards comunican, pero no convierten una mala inferencia en una buena conclusión.

Estudiar este campo en serio significa aprender a pasar desde una pregunta hasta una respuesta defendible, con técnicas adecuadas, herramientas bien escogidas, lectura crítica y un nivel de documentación suficiente para que el trabajo tenga valor más allá de la ejecución inmediata.
