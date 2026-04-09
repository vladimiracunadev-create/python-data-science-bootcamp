# 📚 Guía de estudio del repositorio

> 🧠 Documento personal de estudio para preparar entrevista, demo y conversación técnica usando solo el contenido existente del repositorio.

## 🧭 Qué debo dominar del producto

Necesito poder explicar con seguridad estas capas:

- qué hace el portal del alumno;
- qué hace el laboratorio local;
- qué hace la app Android;
- qué hace la versión Windows;
- qué límites tiene hoy la solución;
- cómo se aterriza a una implementación escolar acotada.

## ⚙️ Comandos que debo manejar y poder explicar

### 🪟 Arranque local del bootcamp

- `python run_bootcamp.py`
- `python launcher.py`
- `http://127.0.0.1:8000`

### ✅ Validación técnica

- `pytest`
- `ruff check .`
- `python -m pytest`

### 🐳 Ejecución con contenedores

- `docker compose up --build`
- `docker compose -f docker-compose.prod.yml up -d --build`

### 📱 App Android

- `cd mobile`
- `npm install`
- `npx expo start`
- `npx expo prebuild --platform android`
- `cd android`
- `gradlew.bat assembleDebug`

### 🪟 Empaque Windows

- `build_windows.bat`
- `python -m PyInstaller bootcamp.spec --noconfirm`

## 🧱 Rutas del repo que debo conocer

- `README.md`
- `docs/INDEX.md`
- `docs/CATALOGO_PRODUCTO.md`
- `docs/ARQUITECTURA_PRODUCTO.md`
- `docs/GUIA_EVALUACION.md`
- `docs/implementacion-v1-skillnest-san-nicolas.md`
- `classes/`
- `app/`
- `mobile/`
- `site/`
- `installer/`

## 🎯 Temas teóricos por clase que debo repasar

### 🧪 Clase 00

- diagnóstico inicial;
- fortalezas y vacíos;
- hábitos de trabajo.

### 🐍 Clase 01

- variables y tipos;
- listas y diccionarios;
- funciones;
- control de flujo.

### 🧹 Clase 02

- `pandas.read_csv`;
- inspección inicial;
- nulos;
- limpieza básica;
- estandarización.

### 📊 Clase 03

- agrupación;
- gráficos de barras;
- lectura visual;
- preguntas exploratorias.

### 📐 Clase 04

- media;
- mediana;
- dispersión;
- interpretación de resumen estadístico.

### 🎨 Clase 05

- `figure` y `axes`;
- títulos y ejes;
- legibilidad;
- ajuste visual.

### 🗓️ Clase 06

- tratamiento de texto;
- fechas;
- columnas derivadas;
- transformaciones útiles.

### 🧩 Clase 07

- mini proyecto guiado;
- pregunta analítica;
- limpieza;
- visualización;
- conclusión.

### 🗣️ Clase 08

- lectura de hallazgos;
- síntesis;
- storytelling con datos;
- comunicación breve.

### 🤖 Clase 09

- idea general de machine learning;
- features y target;
- entrenamiento inicial;
- interpretación del primer modelo.

### 🧠 Clase 10

- modelos supervisados;
- clasificación y regresión;
- flujo básico de entrenamiento;
- lectura de resultados.

### 📏 Clase 11

- evaluación;
- train/test split;
- métricas;
- pipelines;
- comparación de modelos.

### 🏁 Clase 12

- proyecto final;
- integración del recorrido;
- cierre de aprendizaje;
- reflexión final.

## 💻 Ejercicios que me conviene practicar antes de la entrevista

- escribir una función simple y explicarla en voz alta;
- cargar un CSV con pandas y describirlo;
- detectar nulos y justificar una limpieza;
- construir un `groupby` con una conclusión simple;
- hacer un gráfico de barras o línea legible;
- comparar media y mediana sin caer en teoría abstracta;
- explicar qué problema resuelve una visualización;
- describir cuándo un modelo simple sí aporta y cuándo no.

## 🔐 Seguridad y despliegue que debo poder defender

- por qué el laboratorio local escucha en `127.0.0.1`;
- por qué no conviene presentarlo como SaaS abierto;
- qué protecciones existen hoy;
- qué falta si se quisiera exponer a internet;
- por qué `health` y `ready` ayudan a operación;
- por qué el runner local no equivale a aislamiento fuerte.

## 🧪 Pruebas y calidad que debo mencionar

- `pytest` para validar comportamiento;
- `ruff` para calidad base;
- GitHub Actions para CI;
- diferencia entre validar backend y validar superficies visuales;
- necesidad de revisar también la experiencia de app y entregables.

## 🎤 Explicación breve que debo ensayar

“Este repositorio no es solo contenido. Reúne una base docente real: clases, teoría, práctica, evaluación, portal público, app móvil y laboratorio local. La fortaleza está en la progresión pedagógica y en que la solución ya puede mostrarse, ejecutarse y adaptarse para una primera implementación escolar acotada.”

## 📝 Checklist personal de repaso

- abrir y recorrer `README.md`;
- revisar `docs/implementacion-v1-skillnest-san-nicolas.md`;
- repasar `classes/01` a `classes/07`;
- volver a mirar `docs/CATALOGO_PRODUCTO.md`;
- revisar seguridad y despliegue;
- practicar dos respuestas cortas: una pedagógica y una técnica;
- entrar a la entrevista con preguntas claras sobre alcance y pago.
