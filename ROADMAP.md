# 🗺️ Roadmap

> Dirección futura del Bootcamp Python DS. No es un compromiso de fechas — es un mapa de intención técnica y pedagógica.

---

## Estado actual — v1.0.0 (abril 2026)

| Superficie | Estado |
|---|---|
| Laboratorio Flask (13 clases + 6 notebooks) | operativo |
| App de escritorio Windows (pywebview) | publicada |
| App Android (Expo/React Native) | APK debug publicado |
| Portal del alumno (GitHub Pages) | en vivo |
| Vista institucional | en vivo |
| Documentación completa | operativa |

---

## Corto plazo — mejoras al núcleo existente

### Laboratorio

- [ ] Quiz interactivo para las clases 01–12 (actualmente solo clase 00 tiene quiz)
- [ ] Indicador de progreso por clase en el sidebar
- [ ] Soporte para importar notebooks `.ipynb` externos
- [ ] Modo oscuro / claro configurable desde la interfaz

### App de escritorio Windows

- [ ] Icono personalizado (.ico) para el ejecutable y el instalador
- [ ] Instalador con soporte explícito a Edge WebView2 Runtime (descarga automática si falta)
- [ ] Modo quiosco (pantalla completa sin barra de menú)
- [ ] Versión firmada digitalmente (para eliminar alertas de SmartScreen)

### Seguridad y operación

- [ ] Rate limiting básico en el motor de ejecución (por sesión)
- [ ] Log estructurado de ejecuciones para auditoría docente
- [ ] Opción de modo demo (sin guardado de notebooks)

---

## Mediano plazo — nuevas capacidades

### Curriculum

- [ ] Clase 13: introducción a APIs y datos en tiempo real
- [ ] Módulo de NLP básico (tokenización, frecuencias, nube de palabras)
- [ ] Variante del programa para 4 sesiones (versión acortada para talleres)
- [ ] Banco de preguntas adicionales para quiz diagnóstico

### Plataforma

- [ ] Autenticación básica opcional (PIN por clase o por cohorte)
- [ ] Exportación de notebooks guardados a `.ipynb`
- [ ] Panel de resumen de progreso por alumno (para el docente)
- [ ] Soporte multi-idioma (inglés como segunda lengua de la UI)

### App Android

- [ ] Publicación en APK release (firmado) para distribución directa
- [ ] Seguimiento de progreso con sincronización local
- [ ] Modo offline completo (sin Google Colab como dependencia para ver código)

---

## Largo plazo — evolución del producto

### Multiusuario y red

- [ ] Modo servidor local de aula (múltiples alumnos en la misma red WiFi)
- [ ] Autenticación real (OAuth básico) para entornos compartidos
- [ ] Dashboard de clase para el instructor con estado de alumnos

### IA integrada

- [ ] Asistente local de consulta pedagógica (vía Ollama/modelo local)
- [ ] Sugerencias automáticas de corrección en ejercicios
- [ ] Generación asistida de nuevos ejercicios por clase

### Distribución

- [ ] Paquete de instalación para macOS (usando pywebview con backend cocoa)
- [ ] Instalador para Linux (AppImage o .deb)
- [ ] Imagen Docker pre-construida publicada en Docker Hub

---

## Lo que NO es parte del roadmap

- conversión a SaaS con hosting externo (sale del scope de herramienta docente local);
- soporte para múltiples lenguajes de programación en el runner (el foco es Python);
- integración con LMS (Moodle, Canvas) sin un contrato específico que lo justifique;
- versión cloud con datos de alumnos en servidor externo sin acuerdo de privacidad.

---

## Cómo influir en el roadmap

- abre un issue describiendo la necesidad y el contexto educativo que la justifica;
- las mejoras con casos de uso reales (cohortes específicas, problemas documentados) tienen prioridad;
- las contribuciones de código son bienvenidas — ver [CONTRIBUTING.md](CONTRIBUTING.md).
