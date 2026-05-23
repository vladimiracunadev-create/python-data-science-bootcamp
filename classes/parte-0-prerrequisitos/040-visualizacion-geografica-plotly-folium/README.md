# Clase 040 — Visualización geográfica (Plotly / folium)

> Parte: **0 — Prerrequisitos** · Fuente: Plotly Choropleth docs · folium docs · *Cartographies of the Mind* (background).
> ⏱️ Duración estimada: **60 min**.

---

## 🎯 Objetivo

Que el alumno construya mapas básicos cuando los datos tienen componente geográfico: **folium** (mapas Leaflet interactivos, markers, choropleth), **plotly** (choropleth, scatter geo). Sin entrar a GIS profundo (eso es geopandas, fuera del scope de Parte 0).

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Crear mapa folium** centrado, con tile layer básico.
2. **Añadir markers** con popup, tooltip, color según valor.
3. **Construir choropleth** (mapa de calor por región) con folium o plotly.
4. **Decidir entre folium y plotly geo** según destino (HTML standalone vs dashboard).
5. **Citar fuentes** de tiles y GeoJSON públicos.

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | Sistemas de coordenadas: lat/lng | Convención: lat primero en folium, lng primero en plotly. |
| 2 | folium: mapa + markers + popups | Mapas Leaflet en notebook. |
| 3 | folium choropleth con GeoJSON | Mapas de calor por país/región. |
| 4 | plotly choropleth y scatter_geo | Cuando ya usas plotly. |
| 5 | Tile providers (OSM, CartoDB) | Estética y licencia. |
| 6 | Cuándo geopandas | Análisis geoespacial real. |

## 📖 Definiciones y características

**Coordenadas geográficas (lat, lng)**
: **Latitud** (-90 a 90): N/S del ecuador. **Longitud** (-180 a 180): E/W de Greenwich. Convención y orden varía: folium `[lat, lng]`, GeoJSON `[lng, lat]` — fuente clásica de bugs.

**folium**
: Wrapper Python de Leaflet.js. Mapas interactivos (zoom, pan, popups) embebidos en notebook como HTML. Ideal para exploración.

**plotly geo**
: Mapas en plotly (scatter_geo, choropleth). Bonitos, interactivos, integran con dashboards Plotly/Dash. Para choropleth de países usa códigos ISO-3.

**Choropleth**
: Mapa de calor por región: color de cada polígono representa un valor (PIB, población, casos). Requiere GeoJSON con las shapes.

**Tile provider**
: Servidor de "baldosas" (imágenes 256×256) que componen el mapa de fondo. OpenStreetMap (default), CartoDB (limpio), Mapbox (premium).

**geopandas**
: Extensión de pandas con geometrías (Shapely). Para **análisis** espacial (intersection, buffer, dissolve), no solo visualizar. Fuera del scope Parte 0.

## 📂 Dataset / recursos

Sintético: lista de ciudades con coords + métrica simulada. GeoJSON de países público desde un CDN para choropleth.

## 🧪 Ejercicios

**1.** **Mapa con markers.** 5 ciudades españolas con marker y popup mostrando nombre + población.

**2.** **Markers coloreados.** Mismo, pero color verde si pop>1M, rojo si <500k.

**3.** **Choropleth folium.** Mapa mundial con un valor sintético por país (ej: PIB).

**4.** **Choropleth plotly.** Lo mismo con `plotly.express.choropleth`.

**5.** **Comparar.** ¿Cuándo folium (mapa físico explorable) vs plotly (integra con dashboard)?

## 📝 Homework verificable

Notebook: (a) mapa folium con 10+ markers + popups + tooltips; (b) choropleth folium de un dataset por país; (c) mismo choropleth con plotly express; (d) reporte 1-párrafo comparando ambos.

**Criterio de aceptación:** Mapas funcionales en notebook; popups muestran info correcta; choropleth con leyenda.

## ⚠️ Errores comunes

| Síntoma / mensaje | Causa y cómo arreglar |
|---|---|
| Marcadores aparecen en medio del océano | Invertiste lat/lng. **Fix**: folium espera `[lat, lng]`. Para Madrid: `[40.42, -3.70]` (lat positiva, lng negativa). |
| Mapa folium no se renderiza en VS Code | Algunas extensiones de notebook no muestran HTML inline complejo. **Fix**: `m.save('mapa.html')` y abre en navegador. |
| choropleth plotly sale gris | El código ISO no matchea con el shape. **Fix**: usa ISO-3 (`'ESP'` no `'ES'`). Verifica que los códigos del dataset coinciden con los esperados. |
| Mapa pesa MB y carga lento | Demasiados markers (>1000). **Fix**: usa `MarkerCluster` (`folium.plugins.MarkerCluster`) que agrupa por zoom level. |
| Tiles fallan a cargar | Provider con rate limit (Mapbox sin token, Stamen down). **Fix**: usa `'OpenStreetMap'` o `'CartoDB positron'` que son gratis sin token. |

## ❓ Preguntas frecuentes

**❓ ¿folium o plotly?**

**folium** para exploración interactiva en notebook (mapa real con zoom/pan/popups). **plotly** para integrar en dashboard o cuando ya usas plotly. Ambos producen HTML standalone.

**❓ ¿Cómo encuentro lat/lng de un lugar?**

Click derecho en Google Maps → "¿Qué hay aquí?". O geocodifica con `geopy` (`from geopy.geocoders import Nominatim`).

**❓ ¿GeoJSON dónde lo consigo?**

Para países: [Natural Earth](https://www.naturalearthdata.com/) (público). Para regiones: portal gov del país. Para custom: dibuja en geojson.io.

**❓ ¿Cuándo necesito geopandas?**

Análisis espacial real: "¿cuántos puntos caen en este polígono?", "buffer de 1km alrededor", re-proyección entre CRS. Para solo visualizar puntos en mapa: folium basta.

**❓ ¿Mapas offline?**

Tiles son online por default. Para offline: descarga tiles con `mbtiles`, sirve local con `folium.raster_layers.TileLayer(url='file://...')`. Setup complejo, considera si vale.

## 🔗 Referencias

- [folium docs](https://python-visualization.github.io/folium/)
- [plotly choropleth docs](https://plotly.com/python/choropleth-maps/)
- [Natural Earth GeoJSON](https://datahub.io/core/geo-countries)

## ➡️ Siguiente clase

[Clase 041 — SQL fundamental](../041-sql-fundamental-select-where-join-group-by-having/README.md)
