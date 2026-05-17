# 🔐 SECURITY

> Postura de seguridad actual y hardening recomendado para `python-data-science-bootcamp`.

---

## Estado actual

Este repositorio está pensado para uso local, docente y de laboratorio. La app interactiva permite ejecutar código Python, por lo que su postura de seguridad es adecuada para entornos controlados, demos guiadas y máquinas administradas por el docente, pero **no para exposición abierta a internet sin capas adicionales**.

---

## Versiones soportadas

| Versión | Estado |
|---|---|
| `v1.0.0` (rama `master`) | soportada activamente |
| versiones anteriores al tag v1.0.0 | sin soporte |

---

## Superficies de ataque por modo de ejecución

| Modo | Superficie expuesta | Nivel de riesgo |
|---|---|---|
| App de escritorio Windows (`BootcampPythonDS.exe`) | loopback interno, no accesible desde la red | bajo (local) |
| Modo desarrollo (`python run_bootcamp.py`) | `http://127.0.0.1:8000`, vinculado a loopback | bajo si no se cambia HOST |
| Docker Compose (`docker-compose.yml`) | `127.0.0.1:8000`, mapeado a loopback | bajo por configuración |
| Docker Compose endurecido (`docker-compose.prod.yml`) | igual, con configuración adicional | bajo |
| Expuesto a red o internet sin proxy | cualquier superficie | alto — no recomendado sin hardening adicional |

---

## Protecciones que existen hoy

### Validación de entrada

- validación de `slug` e identificadores con regex `^[\w\-]{1,80}$` — previene path traversal;
- todos los slugs pasan por `_safe_resolve()` que verifica que la ruta resuelta permanezca dentro del directorio permitido;
- nombres de notebooks saneados con `re.sub` antes de escribir a disco.

### Límites de carga

- límite de payload por request: 1 MB (`MAX_PAYLOAD_BYTES`);
- límite de longitud de código por celda: 20 KB (`MAX_CODE_LENGTH`).

### Ejecución de código

- timeout por celda: 30 segundos (`EXECUTION_TIMEOUT_SECONDS`);
- reinicio automático de sesión si una celda supera el timeout;
- máximo 100 sesiones concurrentes (`MAX_SESSIONS`);
- TTL de sesión: 1 hora (`SESSION_TTL_SECONDS`);
- eviction automática de sesiones antiguas.

### Headers HTTP

- `Content-Security-Policy`: default-src 'self', sin dependencias CDN externas, sin Google Fonts;
- `X-Content-Type-Options: nosniff`;
- `X-Frame-Options: SAMEORIGIN`;
- `Referrer-Policy: no-referrer`;
- `Permissions-Policy: camera=(), microphone=(), geolocation=()`.

### Configuración de red

- defaults de arranque en `127.0.0.1` tanto en Flask como en Docker Compose;
- en modo app de escritorio Windows, Flask usa un puerto efímero interno no accesible desde la red;
- en Docker, el binding es explícitamente `127.0.0.1:8000:8000`.

### Análisis estático

- Bandit integrado en CI (`security.yml`);
- los únicos `# nosec` presentes son B310 y B110 en los polling loops de `launcher.py` y `run_bootcamp.py` — justificados porque la URL es siempre `http://127.0.0.1:{port}/health` construida internamente, sin input de usuario;
- los usos de `exec` y `eval` en `execution_engine.py` son intencionales y necesarios para la funcionalidad tipo notebook; están mitigados por timeout, límites de payload y la restricción de uso local.

---

## Lo que no existe todavía

- autenticación de usuarios;
- aislamiento fuerte por estudiante (sandbox de OS);
- rate limiting por cliente;
- TLS nativo;
- auditoría estructurada de accesos;
- separación de procesos por sesión.

---

## Recomendaciones de hardening

### Para uso local y docente

- mantener `BOOTCAMP_HOST=127.0.0.1` (por defecto);
- ejecutar en máquina controlada por el docente;
- limpiar `app/saved_notebooks/` antes de compartir el repo o una imagen;
- usar la app de escritorio Windows en lugar del modo desarrollo cuando sea posible (no expone puerto).

### Si se publica fuera del equipo local

- poner la app detrás de un reverse proxy con TLS (nginx, Caddy);
- exigir autenticación externa antes de abrir el runner (OAuth, Basic Auth a nivel de proxy);
- aplicar rate limiting en proxy o gateway;
- registrar accesos y errores en logs centralizados;
- separar entorno demo de cualquier entorno con usuarios reales.

---

## Riesgos aceptados

- el runner ejecuta código Python del usuario dentro del proceso de la app;
- el timeout reduce riesgo de bloqueos, pero no reemplaza un sandbox real;
- el proyecto prioriza facilidad de uso en laboratorio por sobre postura multiusuario endurecida;
- estos riesgos están documentados explícitamente y son conscientes, no accidentales.

---

## Reporte responsable

Si detectas una vulnerabilidad:

1. no publiques secretos ni pasos destructivos en issues públicos;
2. reporta el hallazgo al mantenedor con versión, entorno y pasos de reproducción;
3. si involucra ejecución remota o exposición de datos, coordina una divulgación privada antes de publicar;
4. las correcciones serán incorporadas en la versión `master` y documentadas en [CHANGELOG.md](CHANGELOG.md).
