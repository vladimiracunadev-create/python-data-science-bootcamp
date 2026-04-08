# Bootcamp Python DS — App Android

App movil para el Bootcamp de Python Data Science. Permite a los estudiantes explorar las 12 clases, leer teoria con ejemplos de codigo documentados, rastrear su progreso y abrir cualquier notebook en Google Colab con un tap.

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
    │   └── classes.js          # 12 clases con ejemplos de codigo (embebido, offline)
    ├── navigation/
    │   └── AppNavigator.js     # Stack Navigator con rutas Home y Class
    ├── screens/
    │   ├── HomeScreen.js       # Lista de clases con barra de progreso
    │   └── ClassScreen.js      # Detalle de clase: teoria + ejercicios + Colab
    ├── components/
    │   ├── ClassCard.js        # Tarjeta de clase con badge, topics y boton
    │   ├── CodeBlock.js        # Bloque de codigo con syntax highlighting y copiar
    │   └── ColabButton.js      # Boton para abrir Google Colab
    └── utils/
        ├── progress.js         # AsyncStorage: guardar/leer/limpiar progreso
        └── colab.js            # Helpers para generar URLs de Colab
```

## Tecnologias

| Libreria | Version | Uso |
|---|---|---|
| Expo | ~51.0.0 | Framework base |
| React Native | 0.74 | UI nativa |
| @react-navigation/stack | ~6.4 | Navegacion entre pantallas |
| react-native-syntax-highlighter | ~2.3 | Coloreado de codigo Python |
| @react-native-async-storage | 1.23 | Persistencia de progreso |
| expo-clipboard | ~6.0 | Copiar codigo al portapapeles |
| expo-linking | ~6.3 | Abrir Google Colab en el navegador |

## Agregar/modificar contenido

Todo el contenido de las clases esta en `src/data/classes.js`. Para agregar un ejemplo de codigo a una clase:

```js
codeExamples: [
  {
    id: 'c01-ex5',          // ID unico
    title: 'Mi ejemplo',
    explanation: 'Descripcion breve de lo que hace el codigo.',
    schema: 'opcional: formula o esquema',
    code: `# Tu codigo aqui
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
| `bgCode` | `#0d1117` | Bloques de codigo |
| `accent` | `#22c55e` | Verde: botones, progreso |
| `accentBlue` | `#3b82f6` | Azul: info, schemas |
| `text` | `#f1f5f9` | Texto principal |
| `textMuted` | `#94a3b8` | Texto secundario |
