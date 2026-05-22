# Clase 044 — NoSQL: MongoDB con pymongo

> Parte: **0 — Prerrequisitos** · Fuente: MongoDB docs · pymongo docs · *MongoDB: The Definitive Guide* (Bradshaw et al.) cap. 1.
> ⏱️ Duración estimada: **75 min**.

---

## 🎯 Objetivo

Que el alumno entienda el modelo NoSQL documento (collections de JSON-like), cuándo conviene sobre SQL, y use `pymongo` para CRUD básico + queries con operadores típicos. Sin pretender competir con un curso entero de MongoDB.

## 📚 Resultados de aprendizaje

Al finalizar la clase, el alumno podrá:

1. **Diferenciar** modelo relacional (tablas + filas) vs documento (collections + docs JSON).
2. **Reconocer** cuándo NoSQL aporta (schema flexible, datos jerárquicos, escala horizontal).
3. **Conectar con pymongo**, hacer insert/find/update/delete.
4. **Filtrar** con operadores: `$gt`, `$lt`, `$in`, `$regex`, `$and`, `$or`.
5. **Hacer agregaciones** con el pipeline (`$match`, `$group`, `$sort`).

## 🗺️ Temas

| # | Tema | Por qué importa |
|---|---|---|
| 1 | SQL vs NoSQL — cuándo cada uno | No "NoSQL es mejor" — distinto. |
| 2 | Modelo documento: collections + docs JSON | Schema flexible. |
| 3 | pymongo: connect, insert_one, find, update_one | CRUD básico. |
| 4 | Operadores de query: $gt/$lt/$in/$regex | Equivalentes a WHERE. |
| 5 | Aggregation pipeline | $match/$group/$sort — análogo a SQL. |
| 6 | Cuándo NO usar Mongo | Cuando relacional es claramente mejor. |

## 📂 Dataset / recursos

MongoDB local (Docker o Atlas free tier) — o usar `mongomock` para tests. Datos sintéticos: collection de productos.

## 🧪 Ejercicios

**1.** **CRUD básico.** Conecta a Mongo (o mongomock), inserta 5 productos, lee todos, actualiza uno, borra uno.

**2.** **Find con operadores.** Productos con `precio > 100` y categoría en `['libros', 'musica']`.

**3.** **Update con `$set` y `$inc`.** Incrementa stock de un producto en 10 unidades.

**4.** **Aggregation pipeline.** Promedio de precio por categoría con `$group`.

**5.** **Documento jerárquico.** Inserta un producto con array de `reviews` (sub-documentos). Consulta los que tienen alguna review con `rating < 3` usando `$elemMatch`.

## 📝 Homework verificable

Notebook con `mongomock` (no requiere Mongo real): (a) collection productos con 20 docs sintéticos; (b) 5 queries demostrando operadores; (c) aggregation pipeline con `$match` → `$group` → `$sort`; (d) reporte: 3 casos donde Mongo es mejor que SQL y 3 donde no.

**Criterio de aceptación:** Las queries funcionan; el reporte tiene casos justificados.

## 🔗 Referencias

- [pymongo docs](https://pymongo.readthedocs.io/)
- [MongoDB query operators](https://www.mongodb.com/docs/manual/reference/operator/query/)
- [mongomock](https://github.com/mongomock/mongomock)
- Bradshaw, *MongoDB: The Definitive Guide* 3e, cap. 1.

## ➡️ Siguiente clase

[Clase 045 — APIs REST con requests](../045-apis-rest-con-requests/README.md)
