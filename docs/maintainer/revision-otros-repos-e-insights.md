# 🔎 Revision de otros repos e insights aplicables a este bootcamp

## Repos revisados

- `C:/dev/gabysql`
- `C:/dev/langgraph-realworld`
- `C:/dev/ferremarket`
- `C:/dev/rootcause-landing`
- `C:/dev/portal_python`

## Insight 1: documentacion orientada por perfil

Visto con fuerza en `gabysql` y `langgraph-realworld`.

Lo valioso:

- rutas recomendadas segun tipo de lector;
- mapa documental claro;
- documentos separados para seguridad, operacion, troubleshooting y roadmap.

Aplicacion a este repo:

- dejar materiales distintos para entrevista, desafio tecnico, despliegue y aula;
- no depender de un README unico para todo.

## Insight 2: seguridad explicita y honesta

Visto con fuerza en `gabysql`, `langgraph-realworld` y `ferremarket`.

Lo valioso:

- separar demo local de despliegue real;
- decir que controles existen hoy y cuales no;
- recomendar TLS, proxy, auth y rate limit cuando hay exposicion externa;
- fijar defaults seguros como puertos locales.

Aplicacion a este repo:

- host y puerto configurables por entorno;
- Docker local enlazado a `127.0.0.1`;
- headers de seguridad basicos en Flask;
- documentar posture actual y siguiente capa de hardening.

## Insight 3: visuales con intencion

Visto con fuerza en `rootcause-landing` y `ferremarket`.

Lo valioso:

- narrativa visual clara;
- tablas y diagramas que ordenan la lectura;
- lenguaje de producto y de operacion, no solo de codigo.

Aplicacion a este repo:

- presentaciones mas limpias;
- diagramas del proceso de seleccion;
- docs con tablas de decisiones y rutas segun objetivo.

## Insight 4: operacion realista

Visto con fuerza en `gabysql` y `ferremarket`.

Lo valioso:

- runbooks;
- health checks;
- separacion entre quickstart y produccion;
- observabilidad y validaciones minimas.

Aplicacion a este repo:

- explicar como levantar local de forma segura;
- dejar claro que el runner es para laboratorio;
- sugerir reverse proxy y auth adicional si se expone;
- validar cambios con tests antes de presentar.

## Insight 5: que no repetir

`portal_python` recuerda varios riesgos clasicos:

- secreto hardcodeado;
- `debug=True`;
- credenciales y comparacion insegura;
- postura poco clara entre demo y uso real.

Aplicacion a este repo:

- no dejar secretos en codigo;
- usar defaults locales seguros;
- evitar exponer la app con configuracion abierta;
- presentar siempre los limites reales del entorno.

## Conclusion

La mejor evolucion de este bootcamp no es solo agregar mas clases. Es adoptar el estandar que ya se ve en tus mejores repos:

- documentacion por capas;
- narrativa visual clara;
- seguridad explicita;
- despliegue local seguro por defecto;
- operacion y limites bien comunicados.
