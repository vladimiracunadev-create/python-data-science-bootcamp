# 📱 Python Data Science Program — App Android

App móvil del Python Data Science Program.

> **Estado actual (v3.9.0):** la app embebe las **232 clases** del currículo (232/232 notebooks ejecutables). `src/data/classes.js` se **genera** desde `classes/**/README.md` con `python scripts/generate_mobile_curriculum.py` y se valida en `tests/test_mobile_curriculum.py`. El APK se **reutiliza sin cambios desde v3.8.1** (mismo catálogo, mismo `versionCode 39`; los enlaces a Colab ahora resuelven a notebooks reales del release v3.9.0).
>
> La UX es jerárquica: **Home** lista las 9 partes con su progreso → **Parte** lista sus clases con buscador → **Clase** muestra objetivo, resultados, temas, materiales, práctica y el enlace a Colab.
>
> ⚠️ **Histórico:** el APK `v3.8.0` se publicó con `classes.js` como stub vacío y se instalaba **con el catálogo vacío**. Corregido en `v3.8.1` — ese mismo APK corregido es el que se reutiliza en el release v3.9.0.

## 📥 Descarga del APK

APK debug oficial publicado en el [**release v3.9.0**](https://github.com/vladimiracunadev-create/python-data-science-program/releases/tag/v3.9.0) (reutilizado sin cambios desde v3.8.1):

- 📱 [`PythonDSProgram_android_v3.8.1_debug.apk`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.9.0/PythonDSProgram_android_v3.8.1_debug.apk) — 139 MB · Expo SDK 51 · `versionCode 39` · `versionName 3.8.1`.

Instalación directa en Android (habilitar "instalar de fuentes desconocidas"). Verificación de integridad en [`SHA256SUMS_v3.9.0.txt`](https://github.com/vladimiracunadev-create/python-data-science-program/releases/download/v3.9.0/SHA256SUMS_v3.9.0.txt).

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
    │   └── classes.js          # GENERADO: 232 clases + 9 partes (no editar a mano)
    ├── navigation/
    │   └── AppNavigator.js     # Stack Navigator: rutas Home, Part y Class
    ├── screens/
    │   ├── HomeScreen.js       # Las 9 partes con progreso global
    │   ├── PartScreen.js       # Clases de una parte, con buscador
    │   └── ClassScreen.js      # Detalle de clase: teoría + práctica + Colab
    ├── components/
    │   ├── ClassCard.js        # Tarjeta de clase con badge, topics y boton
    │   ├── PartCard.js         # Tarjeta de parte con progreso propio
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

> **No edites `src/data/classes.js` a mano** — se sobrescribe. La fuente de verdad es
> `classes/parte-*/NNN-*/README.md`. Edita el markdown y regenera:
>
> ```bash
> python scripts/generate_mobile_curriculum.py
> pytest tests/test_mobile_curriculum.py
> ```
>
> El parser ancla las secciones en el emoji del encabezado (`🎯` objetivo, `📚` resultados,
> `🗺️` temas, `📂` recursos, `🧪` ejercicios) porque el texto del título varía entre partes.
> Si añades una clase con otra estructura, el test de sincronización la delata.
>
> Cada clase generada expone además `codeExamples`, que solo se llena en las clases cuyo
> README trae bloques de código:

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
