# Clase 045 — APIs REST con requests

> Parte: **0 — Prerrequisitos** · Fuente: *HTTP: The Definitive Guide* caps. 1-2 · requests docs.
> ⏱️ Duración estimada: **90 min**.

---

## 🎯 Objetivo

Que el alumno consuma APIs REST públicas con `requests`: GET con parámetros, manejo de status codes, autenticación (header, bearer token), paginación, rate limiting con `Retry`, y carga eficiente con `Session`. Lo mínimo para no romper la API del proveedor ni tu pipeline.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Hacer GET/POST** con `requests`, manejar params, headers, body JSON.
2. **Verificar status code** (200 vs 4xx vs 5xx) y usar `raise_for_status()`.
3. **Autenticarse** con header `Authorization: Bearer ...` o API key en header/query.
4. **Paginar** correctamente cuando la API devuelve resultados en páginas.
5. **Rate-limiting** con `urllib3.util.retry.Retry` para reintentos exponenciales.
6. **Reusar conexión** con `requests.Session` para múltiples requests.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Métodos HTTP: GET, POST, PUT, DELETE | Verbos REST. |
| 2 | Status codes: 2xx/3xx/4xx/5xx | Cómo reaccionar a cada uno. |
| 3 | Params, headers, body | Las 3 formas de mandar datos. |
| 4 | Autenticación: Bearer token, API key | Header `Authorization`. |
| 5 | Paginación: offset/limit, cursor, link header | 3 patrones comunes. |
| 6 | Rate limiting + retry exponencial | No tirar la API ajena. |
| 7 | `requests.Session` para reuso | Más rápido + cookies persistentes. |

## 📂 Dataset / recursos

API pública sin auth: https://api.coingecko.com (precios cripto). Sin API key necesaria.

## 🧪 Ejercicios

**1.** **GET básico.** `requests.get('https://api.github.com')`. Inspecciona `status_code`, `headers`, `.json()`.

**2.** **Con params.** GitHub search: `https://api.github.com/search/repositories?q=python+ml&sort=stars`. Imprime top 5.

**3.** **`raise_for_status` + try.** Pega a una URL que devuelve 404 (`/notfound`) y maneja la excepción.

**4.** **Paginación.** GitHub events API. Itera 3 páginas con `page=1,2,3`.

**5.** **Session + Retry.** Configura una `Session` con `HTTPAdapter` + `Retry` (3 intentos, backoff 1s). Verifica que reintenta en 5xx simulado.

## 📝 Homework verificable

Notebook que: (a) consulta una API pública (CoinGecko, GitHub, JSONPlaceholder) con GET; (b) maneja status codes con try/except; (c) pagina 3+ páginas; (d) configura Session con Retry exponencial; (e) reporta cuánto se tardó vs un loop sin Session.

**Criterio de aceptación:** Maneja al menos un error sin crash. Pagination devuelve datos esperados.

## 🔗 Referencias

- [requests docs](https://requests.readthedocs.io/)
- [urllib3 Retry](https://urllib3.readthedocs.io/en/stable/reference/urllib3.util.html#urllib3.util.Retry)
- [GitHub REST API](https://docs.github.com/en/rest)
- [HTTP status codes (MDN)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## ➡️ Siguiente clase

[Clase 046 — Web scraping con BeautifulSoup](../046-web-scraping-con-beautifulsoup/README.md)
