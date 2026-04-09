# Guía maestra de estudio del repositorio

> Documento principal de preparación para estudiar el contenido del repositorio a profundidad y poder explicar producto, pedagogía, arquitectura, operación y contenidos de clase con seguridad.

## Cómo usar esta guía

No la leas como un folleto. Úsala como plan de estudio personal. La idea es que al terminar puedas:

- explicar qué hace el producto;
- defender cómo enseñas;
- recorrer la arquitectura sin perderte;
- resumir cada clase y sus conceptos;
- sostener una conversación técnica y pedagógica con criterio.

## Parte 1. Qué es realmente este repositorio

Este proyecto reúne tres niveles distintos:

1. una base pedagógica reusable;
2. una base operativa local para practicar;
3. una capa documental y pública para presentar el producto.

### Base pedagógica

Vive principalmente en:

- `classes/`
- `datasets/`
- notebooks y soluciones

Aquí está el corazón educativo del bootcamp.

### Base operativa

Vive principalmente en:

- `app/`
- `launcher.py`
- `mobile/`
- `bootcamp.spec`

Aquí está la forma en que el contenido se usa en superficies reales.

### Base documental y pública

Vive principalmente en:

- `README.md`
- `docs/`
- `site/`
- `site/product/`

Aquí está la forma en que el producto se explica y se presenta a terceros.

## Parte 2. Conceptos de producto que debes poder explicar

### Superficie

Forma concreta en que una audiencia interactúa con el producto.

Ejemplos:

- portal del alumno;
- laboratorio local;
- app Windows;
- app Android.

### Artefacto

Archivo reusable que apoya clase, evaluación o presentación.

Ejemplos:

- PDFs de clase;
- PPTX por módulo;
- PDFs de entrevista;
- notebooks.

### Ruta documental

Documento que ordena y explica el sistema.

Ejemplos:

- `README.md`
- `docs/CATALOGO_PRODUCTO.md`
- `docs/ARQUITECTURA_PRODUCTO.md`
- `RUNBOOK.md`
- `SECURITY.md`

### Evolución

Parte proyectada o escalable, pero no necesariamente desplegada como producto final abierto.

## Parte 3. Mi forma de enseñar y cómo defenderla

La metodología del repositorio no se basa en “mostrar código” como espectáculo. Su lógica es:

1. presentar un objetivo claro;
2. conectar la idea con un problema entendible;
3. mostrar un ejemplo breve;
4. pasar a práctica guiada;
5. pedir interpretación y no solo ejecución;
6. cerrar con evidencia y siguiente paso.

### Principios que debes recordar

- contexto antes que tecnicismo;
- progresión antes que saturación;
- error como material de trabajo;
- un mínimo común para todo el grupo;
- tecnología como apoyo, no como reemplazo del razonamiento.

### Frase útil para entrevista

No enseño una herramienta aislada. Enseño una secuencia que permita que el estudiante entienda qué hizo, para qué sirve y cómo seguir avanzando.

## Parte 4. Comandos y rutas que debes dominar

### Arranque local

- `python run_bootcamp.py`
- `python launcher.py`
- `http://127.0.0.1:8000`

### Validación técnica

- `pytest`
- `python -m pytest`
- `ruff check .`

### Docker

- `docker compose up --build`
- `docker compose -f docker-compose.prod.yml up -d --build`

### Android

- `cd mobile`
- `npm install`
- `npx expo start`
- `npx expo prebuild --platform android`
- `cd android`
- `gradlew.bat assembleDebug`

### Windows

- `build_windows.bat`
- `python -m PyInstaller bootcamp.spec --noconfirm`

### Rutas documentales claves

- `README.md`
- `docs/INDEX.md`
- `docs/CATALOGO_PRODUCTO.md`
- `docs/ARQUITECTURA_PRODUCTO.md`
- `docs/GUIA_EVALUACION.md`
- `docs/metodologia-docente.md`
- `docs/implementacion-v1-skillnest-san-nicolas.md`

## Parte 5. Qué debes entender de la arquitectura

### Portal del alumno

Rol:

- entrada pública;
- orientación inicial;
- explicación general del programa.

No hace:

- ejecutar Python;
- reemplazar el laboratorio.

### Laboratorio local

Rol:

- mostrar clases;
- cargar notebooks;
- ejecutar código;
- guardar trabajo local.

### App Windows

Rol:

- empaquetar el laboratorio en una distribución lista para usar;
- reducir fricción técnica en aula;
- evitar depender de tener Python instalado.

### App Android

Rol:

- consulta móvil;
- lectura del contenido;
- acceso a Colab.

Limitación:

- no ejecuta Python nativamente en el dispositivo.

### Documentación

Rol:

- separar audiencias;
- aclarar límites;
- ordenar la narrativa del producto;
- defender arquitectura, operación y seguridad.

## Parte 6. Seguridad y operación que debes poder defender

### Por qué el laboratorio escucha en `127.0.0.1`

Porque la postura del sistema es local-first. La aplicación está diseñada para uso de aula o uso local, no para internet abierta.

### Qué protecciones existen hoy

- validación de slugs e identificadores;
- límite de tamaño de payload;
- límite de longitud del código;
- timeout por ejecución;
- headers de seguridad;
- separación de rutas y carga segura de contenido.

### Qué falta si alguien quisiera abrirlo a internet

- autenticación;
- rate limiting;
- TLS y reverse proxy;
- observabilidad;
- mayor aislamiento del runner;
- políticas de despliegue más estrictas.

### Idea corta que debes recordar

La madurez del repositorio está en separar honestamente lo que ya es operativo de lo que todavía no debe prometerse como SaaS abierto.

## Parte 7. Contenido educativo del bootcamp, módulo por módulo

### Clase 00. Diagnóstico inicial y orientación

Objetivo:

- estimar punto de partida;
- detectar vacíos;
- alinear expectativas.

Definiciones que debes manejar:

- diagnóstico de entrada;
- fortalezas iniciales;
- vacíos de apoyo;
- hábitos de trabajo.

Qué deberías poder decir:

- esta clase no busca “pasar materia”, sino ubicar el punto real de arranque;
- sirve para ajustar ritmo, apoyos y ejemplos de las primeras clases.

### Clase 01. Fundamentos de Python aplicados a datos

Objetivo:

- comprender los elementos básicos del lenguaje y aplicarlos a ejemplos cercanos a datos.

Definiciones:

- variable: nombre que referencia un valor;
- tipo de dato: naturaleza del valor;
- lista: colección ordenada;
- diccionario: estructura clave-valor;
- función: bloque reusable que recibe entradas y devuelve una salida;
- control de flujo: forma en que el programa decide o repite pasos.

Qué debes poder explicar:

- por qué comentar el código es importante;
- cómo una función evita repetir lógica;
- cómo una lista o diccionario ayuda a representar información real.

### Clase 02. Pandas y limpieza de datos

Objetivo:

- cargar un CSV, revisar su estructura y aplicar una limpieza justificada.

Definiciones:

- DataFrame: tabla de pandas;
- inspección inicial: revisar filas, columnas y tipos;
- nulo: dato ausente;
- estandarización: volver consistente formato o texto.

Comandos o métodos clave:

- `pd.read_csv`
- `head`
- `info`
- `isna`
- `fillna`
- `dropna`

Idea central:

Antes de analizar o graficar, conviene instalar una rutina mínima de calidad.

### Clase 03. Visualización exploratoria

Objetivo:

- responder una pregunta simple con agregación y gráfico.

Definiciones:

- agregación: resumir múltiples filas en una métrica;
- `groupby`: agrupar por categoría;
- gráfico exploratorio: visualización para entender patrón, no solo decorar.

Qué debes poder explicar:

- que un gráfico no nace de un clic, sino de una decisión previa;
- por qué la pregunta analítica define la agregación.

### Clase 04. Estadística descriptiva

Objetivo:

- leer y explicar resúmenes estadísticos simples.

Definiciones:

- media: promedio;
- mediana: valor central;
- dispersión: cuánto se alejan los valores;
- outlier: valor atípico.

Qué debes poder decir:

- descripción no es causalidad;
- media y mediana pueden contar historias distintas.

### Clase 05. Visualización con matplotlib

Objetivo:

- construir gráficos con control explícito de ejes, títulos y legibilidad.

Definiciones:

- figura: lienzo general;
- axes: área del gráfico;
- legibilidad: capacidad de entender un gráfico sin fricción.

Qué debes poder explicar:

- por qué un buen gráfico necesita títulos, etiquetas y orden;
- qué diferencia hay entre “hacer un gráfico” y “hacer un gráfico comunicable”.

### Clase 06. Texto, fechas y transformaciones

Objetivo:

- convertir columnas a fecha, limpiar texto y crear variables derivadas útiles.

Definiciones:

- conversión a fecha;
- normalización de texto;
- columna derivada;
- transformación.

Qué debes poder explicar:

- por qué fechas y texto mal formateados rompen análisis;
- cómo una variable derivada puede volver más útil una tabla.

### Clase 07. Mini proyecto guiado

Objetivo:

- integrar habilidades en una secuencia completa y coherente.

Partes del mini proyecto:

- pregunta;
- recorte;
- preparación;
- análisis;
- evidencia;
- conclusión.

Qué debes poder defender:

- que aquí deja de haber ejercicios aislados;
- que el estudiante empieza a pensar en flujo y no solo en pasos sueltos.

### Clase 08. Presentación de hallazgos

Objetivo:

- transformar resultado técnico en mensaje claro.

Definiciones:

- hallazgo;
- evidencia;
- recomendación;
- síntesis ejecutiva.

Fórmula importante:

- hallazgo → evidencia → recomendación.

### Clase 09. Introducción a machine learning

Objetivo:

- mostrar la estructura mínima de un flujo supervisado.

Definiciones:

- feature: variable de entrada;
- target: variable objetivo;
- entrenamiento: ajuste del modelo;
- predicción: salida estimada por el modelo.

Qué debes poder explicar:

- que el módulo no busca profundidad matemática;
- busca instalar la lógica mínima del flujo supervisado.

### Clase 10. Modelos supervisados

Objetivo:

- introducir modelos de clasificación o regresión con lógica comprensible.

Definiciones:

- clasificación: predecir categoría;
- regresión: predecir valor numérico;
- etiqueta;
- métrica.

Qué debes poder decir:

- por qué un árbol es útil para una primera aproximación didáctica;
- por qué la transparencia del flujo importa más que complejidad temprana.

### Clase 11. Evaluación y pipelines

Objetivo:

- mostrar una práctica más robusta de validación y modelado.

Definiciones:

- train/test split;
- validación cruzada;
- leakage;
- pipeline.

Qué debes poder explicar:

- por qué un score único puede ser frágil;
- por qué conviene empaquetar preprocesamiento y modelo en un pipeline;
- por qué el leakage da una falsa sensación de desempeño.

### Clase 12. Proyecto final y cierre

Objetivo:

- integrar el recorrido en una estructura comprensible y defendible.

Qué debe tener un proyecto final según esta base:

- pregunta clara;
- datos y contexto;
- análisis con evidencia;
- conclusión legible;
- comentarios que expliquen qué hace cada bloque importante.

## Parte 8. Qué te conviene practicar antes de la entrevista

### Prácticas técnicas

- escribir una función simple y explicarla;
- cargar un CSV y revisarlo;
- detectar nulos y justificar una decisión;
- construir un `groupby` y extraer una conclusión;
- hacer un gráfico legible;
- explicar un flujo básico de ML;
- explicar por qué usarías un pipeline.

### Prácticas pedagógicas

- explicar una idea técnica en lenguaje simple;
- describir cómo dividirías una clase de 90 minutos;
- explicar cómo manejarías un grupo con niveles distintos;
- explicar cómo usarías tecnología o IA sin perder aprendizaje real.

## Parte 9. Preguntas que deberías poder responder

- ¿Qué hace este repositorio más allá de “dar clases de Python”?
- ¿Cómo se adapta esta base a un contexto escolar?
- ¿Qué módulos mostrarías primero y cuáles dejarías para una segunda fase?
- ¿Qué rol cumple la app Windows?
- ¿Qué rol cumple la app Android?
- ¿Qué límites de seguridad reconoces hoy?
- ¿Por qué tu enfoque docente sigue teniendo valor aunque existan nuevas tecnologías?

## Parte 10. Plan de estudio sugerido

### Sesión 1

- `README.md`
- `docs/CATALOGO_PRODUCTO.md`
- `docs/ARQUITECTURA_PRODUCTO.md`

### Sesión 2

- `docs/metodologia-docente.md`
- `docs/implementacion-v1-skillnest-san-nicolas.md`
- clases 00 a 04

### Sesión 3

- clases 05 a 08
- práctica de explicación oral

### Sesión 4

- clases 09 a 12
- seguridad, operación y límites

## Cierre de esta guía

Si estudias este documento bien, no solo vas a recordar archivos. Vas a poder sostener una conversación completa sobre qué enseña el bootcamp, cómo está construido, por qué está diseñado así y cómo lo aterrizarías con criterio en una implementación real.
