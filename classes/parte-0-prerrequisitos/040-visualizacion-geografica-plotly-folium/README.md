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

## 🔗 Referencias

- [folium docs](https://python-visualization.github.io/folium/)
- [plotly choropleth docs](https://plotly.com/python/choropleth-maps/)
- [Natural Earth GeoJSON](https://datahub.io/core/geo-countries)

## ➡️ Siguiente clase

[Clase 041 — SQL fundamental](../041-sql-fundamental-select-where-join-group-by-having/README.md)
