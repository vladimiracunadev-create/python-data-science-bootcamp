# Roadmap

> Dirección futura del Bootcamp Python DS. No es un compromiso de fechas — es un mapa de intención técnica y pedagógica.

---

## Estado actual — v2.0.0-scaffold (mayo 2026)

| Superficie | Estado |
|---|---|
| Currículo v2 (197 clases, 9 partes) | scaffold operativo; contenido en desarrollo |
| Currículo v1 (31 clases con contenido) | archivado en `historicos/classes-v1/` |
| Laboratorio Flask (consume v2) | operativo |
| App de escritorio Windows (pywebview) | publicada — consume v2 tras rebuild |
| App Android (contenido v1) | APK debug publicado — pendiente migración a v2 |
| Portal del alumno (contenido v1) | en vivo — pendiente migración a v2 |
| Vista institucional | en vivo |
| Documentación | realineada con v2 |

---

## Trabajo crítico — completar la migración v1 → v2

Antes de añadir nuevas capacidades, hay que cerrar la migración iniciada en v2.0.0-scaffold:

### Contenido pedagógico

- [ ] Desarrollar las 46 clases de la **Parte 0 — Prerrequisitos** al estándar de calidad de la antigua clase 14 (5+ bloques de código documentados, 4–5 ejercicios concretos con dataset, homework verificable)
- [ ] Desarrollar las 43 clases de la **Parte 1 — ML clásico**
- [ ] Desarrollar las 13 clases de la **Parte 3 — Estadística inferencial** (intercaladas con Parte 1)
- [ ] Desarrollar las 56 clases de la **Parte 2 — Deep Learning**
- [ ] Desarrollar las 14 clases de la **Parte 4 — MLOps**
- [ ] Desarrollar las 25 clases restantes (Partes 5, 6, 7, 8)
- [ ] Migrar material reutilizable desde `historicos/classes-v1/` cuando aplique

### Superficies pendientes de migración

- [ ] `mobile/src/data/classes.js` — regenerar contra el currículo v2
- [ ] `site/` — regenerar portal contra el currículo v2
- [ ] `docs/pdfs/classes/` y `docs/presentaciones/classes/` — regenerar PDFs y PPTX por bloques al madurar el contenido
- [ ] Adaptar `scripts/generate_class_docs.py` y `scripts/generate_class_assets.py` para que recorran la estructura anidada de v2

### Verificación de calidad pedagógica

- [ ] Script de CI que falle si una clase v2 tiene `notebook.ipynb` con menos de N celdas reales
- [ ] Script de CI que verifique que cada clase referencia un dataset existente
- [ ] Quizzes interactivos pre/post lección como parte del estándar v2

---

## Corto plazo — mejoras al núcleo existente

### Laboratorio

- [ ] Indicador de progreso por clase en el sidebar (con cobertura de las 197 clases)
- [ ] Navegación jerárquica (parte → clase) en lugar de lista plana
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

### Plataforma

- [ ] Autenticación básica opcional (PIN por clase o por cohorte)
- [ ] Exportación de notebooks guardados a `.ipynb`
- [ ] Panel de resumen de progreso por alumno (para el docente) con métricas a nivel de las 9 partes
- [ ] Soporte multi-idioma (inglés como segunda lengua de la UI)

### App Android (post-migración v2)

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
- [ ] Generación asistida de nuevos ejercicios por clase a partir del scaffold v2

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
