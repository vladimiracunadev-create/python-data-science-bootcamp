# Clase 046 — Web scraping con BeautifulSoup

> Parte: **0 — Prerrequisitos** · Fuente: *Web Scraping with Python* (Mitchell, 2ª ed.) caps. 1-3 · BeautifulSoup docs.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno extraiga datos de páginas HTML cuando **no hay API disponible**, usando `requests` + `BeautifulSoup`. Y entienda los **límites éticos y legales**: robots.txt, rate limiting humano, ToS, datos personales, copyright. Lo último que debe hacer al scrapear es tirar abajo el sitio o meterse en problemas.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Parsear HTML** con `BeautifulSoup(html, 'html.parser')`.
2. **Encontrar elementos** con `find`, `find_all`, `select` (CSS selectors).
3. **Extraer texto y atributos** (`.text`, `['href']`).
4. **Respetar `robots.txt`** y rate limit (delay entre requests).
5. **Identificar** cuándo scraping es buena idea vs cuándo buscar otra fuente (API, dataset público).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | HTTP → HTML → parser tree | Cómo funciona scraping. |
| 2 | BeautifulSoup: find vs select | Selectores CSS son más potentes. |
| 3 | Extracción de texto y atributos | `.text`, `.get_text(strip=True)`, `['href']`. |
| 4 | Páginas dinámicas (JS) — `requests` no las renderiza | Para eso: Playwright/Selenium. |
| 5 | robots.txt — qué dice y por qué respetar | `User-agent`, `Disallow`, `Crawl-delay`. |
| 6 | Ética: ToS, rate limiting, datos personales | Lo que sí, lo que no. |

## 📂 Dataset / recursos

Página HTML simple servida desde un string en el notebook (sin tocar internet). Ejercicios opcionales con `https://quotes.toscrape.com` (sitio diseñado para practicar).

## 🧪 Ejercicios

**1.** **Parsea HTML local.** Crea un HTML con 3 productos (`<div class='product'>`). Extrae nombres y precios con `find_all`.

**2.** **Selectores CSS.** Lo mismo con `soup.select('.product .price')`.

**3.** **Tabla a DataFrame.** `pd.read_html(url)` para una tabla HTML — bonus: `requests` + `BeautifulSoup` para tablas custom.

**4.** **Scrape ético.** Scrapea `quotes.toscrape.com` (público, diseñado para esto). Respeta `Crawl-delay`. 3 páginas con `time.sleep(1)` entre cada una.

**5.** **Inspeccionar robots.txt.** Lee `https://quotes.toscrape.com/robots.txt` con requests. Identifica qué paths están `Disallow`.

## 📝 Homework verificable

Notebook: (a) HTML local con 5 productos, extrae nombre/precio/url; (b) scrape `quotes.toscrape.com` (3 páginas, con delay); (c) consulta robots.txt y razona; (d) listado de 3 escenarios cuando scrapear es buena idea y 3 cuando no.

**Criterio de aceptación:** Scraping respeta delays. Análisis de robots.txt correcto.

## 🔗 Referencias

- Mitchell, *Web Scraping with Python* 2e, caps. 1-3.
- [BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [quotes.toscrape.com](https://quotes.toscrape.com/) (sitio para practicar)
- [Google — robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

## ➡️ Siguiente clase

[Clase ../ — Parte 1 — Panorama del ML](../../parte-1-machine-learning-clasico/047-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based/README.md)
