# Históricos

Esta carpeta guarda versiones anteriores del producto que ya no son la fuente de verdad pero se preservan por trazabilidad.

## Contenido

| Carpeta | Qué es |
|---|---|
| `classes-v1/` | Currículo v1 (31 clases en 13 módulos). Estuvo activo entre 2025 y mayo de 2026. Reemplazado por el currículo v2 de 197 clases en 9 partes que vive en [`classes/`](../classes/) en la raíz del repo. |

## Por qué se conserva

- Permite recuperar material pedagógico ya redactado (teoría, ejercicios, soluciones) para reutilizar al rellenar las clases v2.
- Mantiene el historial de Git accesible: las carpetas se movieron con `git mv`, así que `git log --follow` funciona.
- Sirve de referencia para validar regresiones o comparar el alcance entre versiones.

## Qué NO hacer aquí

- No agregar contenido nuevo. Si surge una idea, va en `classes/` (v2).
- No editar para mantener al día. El contenido aquí está congelado.
