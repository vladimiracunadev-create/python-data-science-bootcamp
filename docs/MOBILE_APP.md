# Guía: App Móvil Android

App React Native (Expo) standalone para que los alumnos lean el contenido del bootcamp, vean los ejemplos de código con resaltado de sintaxis y abran los notebooks directamente en Google Colab desde su celular.

---

## Qué hace la app

```
ALUMNO
  |
  ├── [Lista de clases]
  │     13 módulos: clase 0 diagnóstica + 12 clases con título, descripción, temas y estado de progreso
  │
  ├── [Detalle de clase]
  │     - Pestaña "Teoría": contenido con esquemas y explicaciones
  │     - Pestaña "Ejercicios": código documentado para practicar
  ?     - Pestaña "Diagnóstico": quiz con corrección inmediata cuando aplica
  │
  ├── [Bloques de código]
  │     - Resaltado de sintaxis Python (tema oscuro)
  │     - Boton "Copiar" con feedback visual
  │     - Esquemas ASCII del concepto antes del código
  │
  └── [Boton Colab]
        Abre el notebook de la clase en Google Colab con un tap
        URL: colab.research.google.com/github/[repo]/blob/master/classes/.../notebook.ipynb
```

---

## Arquitectura

```
mobile/
├── App.js                      <- Entrada + navegacion
├── app.json                    <- Config Expo (nombre, icono, permisos)
├── package.json                <- Dependencias npm
├── src/
│   ├── data/
│   │   └── classes.js          <- Contenido de la clase 0 diagnóstica y las 12 clases troncales embebido
│   ├── screens/
│   │   ├── HomeScreen.js       <- Lista de clases + barra de progreso
│   │   └── ClassScreen.js      <- Detalle con pestañas teoría/ejercicios
│   ├── components/
│   │   ├── CodeBlock.js        <- Bloque de código con syntax highlight
│   │   ├── ClassCard.js        <- Tarjeta de clase en la lista
│   │   └── ColabButton.js      <- Boton flotante "Abrir en Colab"
│   ├── navigation/
│   │   └── AppNavigator.js     <- Stack navigator
│   └── utils/
│       ├── colab.js            <- Generador de URLs de Colab
│       └── progress.js         <- Progreso del alumno (AsyncStorage)
```

---

## Flujo de ejecución de código

La app móvil NO ejecuta Python directamente. El flujo es:

```
[App Android]
     |
     ├── Mostrar código documentado con syntax highlighting
     |         (el alumno lee, comprende, copia)
     |
     └── [Boton "Abrir en Colab"]
               |
               └── Abre en el navegador:
                   https://colab.research.google.com/github/[user]/[repo]/blob/master/classes/[clase]/notebook.ipynb
                             |
                             └── Google Colab ejecuta el notebook en la nube
                                 (el alumno puede modificarlo y ejecutar celda a celda)
```

### Por qué este enfoque?

| Alternativa | Problema |
|---|---|
| Python nativo en Android | Requiere Termux o compilar CPython — demasiado pesado y complejo |
| Pyodide en WebView | 30+ MB de descarga, lento en celulares de gama baja |
| Servidor Flask remoto | Requiere internet y un servidor pagado |
| Google Colab | Gratuito, en la nube, ya conocido por alumnos, sin setup |

---

## Requisitos para desarrollar

| Herramienta | Versión | Instalacion |
|---|---|---|
| Node.js | 18+ | nodejs.org |
| npm | incluido con Node | - |
| Expo CLI | ultimo | `npm install -g @expo/cli` |
| Expo Go app | ultimo | Play Store en Android |

No se requiere Android Studio ni SDK de Android para desarrollo y pruebas con Expo Go.

---

## Instalar y ejecutar en desarrollo

```bash
# 1. Entrar al directorio de la app
cd mobile

# 2. Instalar dependencias
npm install

# 3. Iniciar el servidor de desarrollo
npx expo start

# 4. En el celular Android:
#    - Instalar "Expo Go" desde Play Store
#    - Escanear el código QR que aparece en la consola
```

La app se recarga automaticamente cada vez que se guarda un archivo.

---

## Generar APK para distribucion

### Opción A — EAS Build (recomendado, en la nube)

```bash
# Instalar EAS CLI
npm install -g eas-cli

# Iniciar sesion en Expo (cuenta gratuita en expo.dev)
eas login

# Configurar el proyecto (primera vez)
eas build:configure

# Generar APK de preview (sin firma de produccion)
eas build -p android --profile preview

# El APK se sube a expo.dev y se puede descargar desde ahi
```

El APK generado se puede instalar en cualquier Android con "Instalar desde fuentes desconocidas" activado.

### Opción B — Build local (requiere Android Studio)

```bash
# Generar proyecto Android nativo
npx expo prebuild --platform android

# Compilar APK de debug
cd android && ./gradlew assembleDebug

# El APK estara en:
# android/app/build/outputs/apk/debug/app-debug.apk
```

---

## Configuración del contenido

El contenido de las clases esta embebido en `src/data/classes.js`. Cada clase tiene:

```js
{
  id: "01-python-fundamentos",
  number: 1,
  title: "Python Fundamentos",
  description: "...",
  duration: "90 min",
  level: "Basico",
  colabUrl: "https://colab.research.google.com/github/.../notebook.ipynb",
  topics: ["Variables", "Listas", ...],
  codeExamples: [
    {
      id: "ex1",
      title: "Titulo del ejemplo",
      explanation: "Explicacion del concepto",
      schema: "ESQUEMA ASCII del concepto (opcional)",
      code: "# codigo Python documentado\n...",
      language: "python"
    }
  ]
}
```

Para actualizar el contenido: editar `src/data/classes.js` y volver a hacer el build.

---

## Progreso del alumno

El progreso se guarda localmente en el dispositivo con AsyncStorage (no se sincroniza a ningun servidor). Se persiste entre sesiones.

```
Clase marcada como completada
        ↓
AsyncStorage.setItem('progress', JSON.stringify([...ids]))
        ↓
HomeScreen lee el progreso y muestra la barra y los checkmarks
```

Para resetear el progreso: ir a la pantalla principal y usar "Reiniciar progreso" (si se implemento) o borrar los datos de la app desde Ajustes de Android.

---

## Colores y diseño

```js
const colors = {
  bg: '#0f0f1a',         // Fondo principal (negro azulado)
  bgCard: '#1a1a2e',     // Fondo de tarjetas
  bgCode: '#0d1117',     // Fondo de bloques de codigo (GitHub Dark)
  accent: '#22c55e',     // Verde (botones principales, progreso)
  accentBlue: '#3b82f6', // Azul (esquemas, info secundaria)
  text: '#f1f5f9',       // Texto principal
  textMuted: '#94a3b8',  // Texto secundario
  border: '#334155',     // Bordes de tarjetas
};
```

---

## Diferencias entre la app Android y el laboratorio Windows

| Caracteristica | App Android | Laboratorio Windows (Flask) |
|---|---|---|
| Ejecución de código | Via Google Colab (browser) | En el mismo navegador (runner local) |
| Contenido | Embebido en la app | Leido desde archivos en disco |
| Progreso | AsyncStorage local | No implementado (v1) |
| Acceso | Sin internet para el contenido | Sin internet para el laboratorio |
| Guardado de notebooks | No (va a Colab) | Si (app/saved_notebooks/) |
| Modo de uso | Lectura + referencia | Clase activa con práctica guiada |

---

## Actualizar la app con nuevo contenido

1. Editar `mobile/src/data/classes.js`
2. Ejecutar `npx expo start` para probar
3. Generar nuevo APK con `eas build`
4. Distribuir el nuevo APK

Para actualizaciones menores de contenido (sin cambios en el código de la app), Expo permite "OTA updates" (over-the-air) que no requieren publicar un nuevo APK.
