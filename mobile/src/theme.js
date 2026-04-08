// ============================================================
// DESIGN SYSTEM — BOOTCAMP PYTHON DS
// Colores, espaciado, tipografia y bordes usados en toda la app
// ============================================================

export const colors = {
  // Fondos
  bg: '#0f0f1a',          // fondo principal (casi negro azulado)
  bgCard: '#1a1a2e',      // fondo de tarjetas
  bgCode: '#0d1117',      // fondo de bloques de codigo (GitHub dark)
  bgInput: '#16213e',     // fondo de inputs
  bgMuted: '#1e293b',     // fondo secundario suave

  // Acentos
  accent: '#22c55e',      // verde principal (botones, progreso, destacados)
  accentDark: '#16a34a',  // verde oscuro (pressed states)
  accentBlue: '#3b82f6',  // azul (esquemas, info boxes)
  accentBlueDark: '#2563eb',

  // Texto
  text: '#f1f5f9',        // texto principal (casi blanco)
  textMuted: '#94a3b8',   // texto secundario (gris)
  textCode: '#e2e8f0',    // texto en bloques de codigo

  // Estados / semaforo
  warning: '#f59e0b',     // amarillo / advertencia
  error: '#ef4444',       // rojo / error
  success: '#22c55e',     // verde / exito (mismo que accent)
  info: '#3b82f6',        // azul / informacion

  // Bordes y separadores
  border: '#334155',      // borde sutil
  borderMuted: '#1e293b', // borde muy sutil

  // Niveles de dificultad
  levelBasic: '#22c55e',
  levelInter: '#f59e0b',
  levelAdv: '#ef4444',
};

export const spacing = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 48,
};

export const radius = {
  sm: 6,
  md: 12,
  lg: 20,
  full: 999,
};

export const fontSize = {
  xs: 11,
  sm: 13,
  md: 15,
  lg: 17,
  xl: 20,
  xxl: 24,
  title: 28,
};

export const fontWeight = {
  normal: '400',
  medium: '500',
  semibold: '600',
  bold: '700',
};

// Mapa de color por nivel de dificultad
export const levelColor = (level) => {
  if (!level) return colors.textMuted;
  const l = level.toLowerCase();
  if (l === 'diagnostico') return colors.info;
  if (l === 'basico') return colors.levelBasic;
  if (l === 'intermedio') return colors.levelInter;
  if (l === 'integrador') return colors.warning;
  if (l === 'avanzado') return colors.levelAdv;
  if (l === 'intermedio-avanzado') return colors.info;
  return colors.textMuted;
};
