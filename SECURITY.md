# SECURITY

> Postura de seguridad actual y hardening recomendado para `python-data-science-bootcamp`.

## Estado actual

Este repositorio esta pensado para uso local, docente y de laboratorio. La app interactiva permite ejecutar codigo Python, por lo que hoy su postura de seguridad es adecuada para entornos controlados, demos guiadas y maquinas administradas por el docente, pero no para exposicion abierta a internet sin capas adicionales.

## Versiones soportadas

| Linea | Estado |
|---|---|
| `2.x` | soportada |
| `1.x` | sin soporte activo |

## Protecciones que existen hoy

- validacion de `slug` e identificadores para evitar rutas arbitrarias;
- limite de payload por request;
- limite de longitud de codigo por ejecucion;
- timeout por celda y reinicio de sesion ante ejecuciones colgadas;
- recoleccion y eviction de sesiones antiguas;
- headers de seguridad basicos (`CSP`, `X-Frame-Options`, `Referrer-Policy`, `nosniff`);
- defaults de arranque local via `127.0.0.1`;
- `docker-compose` enlazado a `127.0.0.1`.

## Lo que no existe todavia

- autenticacion de usuarios;
- aislamiento fuerte por estudiante;
- rate limiting por cliente;
- TLS nativo;
- auditoria estructurada;
- sandbox de sistema operativo para ejecucion de codigo no confiable.

## Recomendaciones de hardening

### Para uso local y docente

- mantener `BOOTCAMP_HOST=127.0.0.1`;
- ejecutar en maquina controlada por el docente;
- limpiar notebooks guardados antes de compartir el repo o una imagen.

### Si se publica fuera del equipo local

- poner la app detras de un reverse proxy con TLS;
- exigir autenticacion externa antes de abrir el runner;
- aplicar rate limiting en proxy o gateway;
- registrar accesos y errores en logs centralizados;
- separar entorno demo de cualquier entorno con usuarios reales.

## Riesgos aceptados

- el runner ejecuta codigo Python del usuario dentro del proceso de la app;
- el timeout reduce riesgo de bloqueos, pero no reemplaza un sandbox real;
- el proyecto prioriza facilidad de uso en laboratorio por sobre postura multiusuario endurecida.

## Nota sobre analisis estatico

- el archivo `app/execution_engine.py` contiene usos intencionales de `exec` y `eval` para emular una experiencia tipo notebook en laboratorio local;
- esas lineas estan marcadas de forma localizada para Bandit, no porque el riesgo no exista, sino porque es una capacidad central del producto;
- la mitigacion real no es "eliminar exec", sino mantener el runner en entorno controlado, con localhost por defecto, timeout, limites de payload y sin exposicion abierta.

## Reporte responsable

Si detectas una vulnerabilidad:

1. no publiques secretos ni pasos destructivos;
2. reporta el hallazgo al mantenedor con version, entorno y pasos de reproduccion;
3. si involucra ejecucion remota o exposicion de datos, coordina primero una divulgacion privada.
