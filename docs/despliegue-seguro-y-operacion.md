# Despliegue seguro y operacion del bootcamp

## Postura actual del repositorio

Este proyecto esta pensado para uso local, docente y de laboratorio. No debe presentarse como aplicacion lista para exponerse directamente a internet.

## Controles actuales

- validacion de slugs e identificadores;
- proteccion contra path traversal en carga y guardado;
- limite de tamano de payload;
- limite de longitud de codigo ejecutable;
- timeout y control de sesiones en el motor de ejecucion;
- headers de seguridad basicos en respuestas HTTP;
- host y puerto configurables por entorno;
- `docker-compose.yml` enlazado a `127.0.0.1` para uso local.

## Quickstart local recomendado

### Python nativo

```powershell
$env:BOOTCAMP_HOST="127.0.0.1"
$env:BOOTCAMP_PORT="8000"
python run_bootcamp.py
```

### Docker local

```powershell
docker compose up --build
```

La app quedara disponible en `http://127.0.0.1:8000`.

## Si algun dia hubiera que exponerlo fuera de localhost

No hacerlo directamente. Antes, agregar al menos:

1. reverse proxy con TLS;
2. autenticacion adicional;
3. rate limiting;
4. logging y monitoreo;
5. politica clara de sesiones;
6. separacion entre entorno demo y entorno expuesto;
7. gestion de secretos por variables de entorno o secret manager.

## Patrones heredados de otros repos tuyos

De `langgraph-realworld`:

- puertos locales por defecto;
- seguridad por capas;
- secretos fuera del repo;
- postura explicita entre demo y exposicion externa.

De `gabysql`:

- `SECURITY.md` y `RUNBOOK.md` separados;
- recomendaciones honestas de hardening;
- no vender una demo como plataforma enterprise.

De `ferremarket`:

- separar local y produccion;
- pensar proxy, cookies seguras, observabilidad y salud operacional;
- documentar servicios, puertos y dependencias.

## Siguiente capa de hardening si este proyecto creciera

- imagen Docker non-root;
- versionado y auditoria de dependencias mas estricta;
- healthcheck de contenedor;
- autenticacion simple para demos compartidas;
- `docker-compose.prod.yml` o overlay de produccion;
- CSP afinada si la interfaz se estabiliza;
- CI de seguridad y escaneo de secretos.

## Frase util para entrevista o desafio

"Hoy esta preparado para laboratorio local y demostracion docente. Si el contexto exigiera exposicion mayor, yo no abriria el runner directamente: pondria proxy, TLS, auth, limites de trafico y una politica de operacion acorde."
