# 📱 Python Data Science Program — App Android

App móvil del Python Data Science Program.

> **Estado actual:** el código de la app está operativo (UI, navegación, almacenamiento de progreso, integración con Google Colab) pero `src/data/classes.js` quedó como **stub vacío**. La adaptación de las **232 clases** (v3.8.0 — 🎓 232/232 clases · 232/232 notebooks ejecutables · cobertura 100% real) del currículo a una UX móvil está pendiente — ver [ROADMAP.md](../ROADMAP.md). El APK publicado hoy es funcional pero con catálogo vacío.

## 📥 Descarga del APK

APK debug oficial publicado en el [**release v3.8.0**](https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.8.0):

- 📱 [`PythonDSProgram_android_v3.8.0_debug.apk`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.8.0/PythonDSProgram_android_v3.8.0_debug.apk) — 139 MB · Expo SDK 51 · `versionCode 38` · `versionName 3.8.0`.

Instalación directa en Android (habilitar "instalar de fuentes desconocidas"). Verificación de integridad en [`SHA256SUMS_v3.8.0.txt`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.8.0/SHA256SUMS_v3.8.0.txt).

## Requisitos

- Node.js 18+
- npm o yarn
- Expo CLI: `npm install -g @expo/cli`
- Para generar APK: cuenta Expo gratuita en https://expo.dev

## Instalar dependencias

```bash
cd mobile
npm install
```

## Ejecutar en desarrollo

```bash
npx expo start
```

Escanear el QR con la app **Expo Go** en Android (disponible en Play Store).

## Generar APK para Android

```bash
# Instalar EAS CLI (una sola vez)
npm install -g eas-cli

# Login en expo.dev (gratis)
eas login

# Inicializar EAS (primera vez)
eas build:configure

# Generar APK de preview
npx eas build -p android --profile preview
```

El APK se descarga desde el dashboard de expo.dev una vez completado el build.

## Estructura

```
mobile/
├── App.js                      # Entrada principal: Navigation + SafeAreaProvider
├── app.json                    # Configuracion Expo (nombre, slug, android package)
├── babel.config.js             # Config Babel para Expo
├── package.json                # Dependencias
└── src/
    ├── theme.js                # Design system: colores, espaciado, tipografia
    ├── data/
    │   └── classes.js          # Stub vacío (CLASSES = []); pendiente cargar el catálogo
    ├── navigation/
    │   └── AppNavigator.js     # Stack Navigator con rutas Home y Class
    ├── screens/
    │   ├── HomeScreen.js       # Lista de clases con barra de progreso
    │   └── ClassScreen.js      # Detalle de clase: teoría + ejercicios + Colab
    ├── components/
    │   ├── ClassCard.js        # Tarjeta de clase con badge, topics y boton
    │   ├── CodeBlock.js        # Bloque de código con syntax highlighting y copiar
    │   └── ColabButton.js      # Boton para abrir Google Colab
    └── utils/
        ├── progress.js         # AsyncStorage: guardar/leer/limpiar progreso
        └── colab.js            # Helpers para generar URLs de Colab
```

## Tecnologias

| Libreria | Versión | Uso |
|---|---|---|
| Expo | ~51.0.0 | Framework base |
| React Native | 0.74 | UI nativa |
| @react-navigation/stack | ~6.4 | Navegacion entre pantallas |
| react-native-syntax-highlighter | ~2.1 | Coloreado de código Python |
| @react-native-async-storage | 1.23 | Persistencia de progreso |
| expo-clipboard | ~6.0 | Copiar código al portapapeles |
| expo-linking | ~6.3 | Abrir Google Colab en el navegador |

## Agregar/modificar contenido

> El archivo `src/data/classes.js` está hoy vacío (stub). Cuando se decida la UX para representar **232 clases** (v3.7.0) en móvil (jerarquía por partes, búsqueda, progreso por bloque), se irán cargando entradas en este archivo. Estructura de objeto sugerida por clase:

```js
codeExamples: [
  {
    id: 'c01-ex5',          // ID unico
    title: 'Mi ejemplo',
    explanation: 'Descripción breve de lo que hace el código.',
    schema: 'opcional: formula o esquema',
    code: `# Tu código aquí
print("Hola mundo")`,
    language: 'python',
  }
]
```

## Colores del design system

| Token | Hex | Uso |
|---|---|---|
| `bg` | `#0f0f1a` | Fondo principal |
| `bgCard` | `#1a1a2e` | Tarjetas y headers |
| `bgCode` | `#0d1117` | Bloques de código |
| `accent` | `#22c55e` | Verde: botones, progreso |
| `accentBlue` | `#3b82f6` | Azul: info, schemas |
| `text` | `#f1f5f9` | Texto principal |
| `textMuted` | `#94a3b8` | Texto secundario |
