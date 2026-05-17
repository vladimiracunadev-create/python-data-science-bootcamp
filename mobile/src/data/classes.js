// Datos del currículo embebidos en la app móvil.
//
// El currículo v2 (197 clases en 9 partes) vive en el repositorio bajo `classes/`.
// La migración del contenido v2 a este archivo está pendiente: requiere decidir
// cómo se presentan 197 clases en una UX móvil (jerarquía por partes, búsqueda,
// progreso por bloque) sin perder la accesibilidad que tenía la v1 plana.
//
// Hasta que esa migración se diseñe y ejecute, este archivo queda como stub
// vacío para que la app no embeba contenido desactualizado del currículo v1.
// El portal web y el laboratorio Flask sí consumen v2 — la app móvil va detrás.
//
// Ver: ROADMAP.md → "Trabajo crítico — completar la migración v1 → v2"

export const CLASSES = [];

export const CURRICULUM_VERSION = "v2.0.0-scaffold";

export const CURRICULUM_STATUS = {
  totalClasses: 197,
  totalParts: 9,
  contentReady: false,
  message:
    "Pauta v2 disponible en el repositorio. Adaptación a la app móvil pendiente.",
};
