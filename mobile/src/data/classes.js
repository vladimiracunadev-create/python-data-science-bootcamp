// Datos del currículo embebidos en la app móvil.
//
// El currículo v3.0.0 (232 clases en 9 partes, numeración secuencial 001-232)
// vive en el repositorio bajo `classes/`. La migración del contenido v3 a este
// archivo está pendiente: requiere decidir cómo se presentan 232 clases en una
// UX móvil (jerarquía por partes, búsqueda, progreso por bloque) sin perder
// la accesibilidad que tenía la v1 plana.
//
// Hasta que esa migración se diseñe y ejecute, este archivo queda como stub
// vacío para que la app no embeba contenido desactualizado. El portal web y
// el laboratorio Flask sí consumen v3 — la app móvil va detrás.
//
// Ver: ROADMAP.md → "Trabajo crítico — completar el contenido pedagógico"

export const CLASSES = [];

export const CURRICULUM_VERSION = "v3.0.0-scaffold";

export const CURRICULUM_STATUS = {
  totalClasses: 232,
  totalParts: 9,
  completedClasses: 193,
  developmentParts: [
    "parte-0-prerrequisitos",
    "parte-1-machine-learning-clasico",
    "parte-2-deep-learning",
    "parte-3-estadistica-inferencial",
  ],
  scaffoldParts: [
    "parte-4-mlops",
    "parte-5-ingenieria-de-datos",
    "parte-6-sistemas-de-recomendacion",
    "parte-7-etica-fairness-privacidad",
    "parte-8-capstones",
  ],
  contentReady: false,
  message:
    "Pauta v3.0.0 disponible en el repositorio (232 clases, 193 desarrolladas). Adaptación a la app móvil pendiente.",
};
