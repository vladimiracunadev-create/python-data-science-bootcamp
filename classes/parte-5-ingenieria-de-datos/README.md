# Parte 5 — Ingeniería de Datos

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-4-mlops/README.md) · [⏭️ Parte siguiente](../parte-6-sistemas-de-recomendacion/README.md)

**8 clases** · ~3 semanas

**Fuente principal:** Complementaria — fundamentos prácticos de data engineering necesarios para alimentar pipelines de ML a escala.

---

## 🎯 ¿De qué trata esta parte?

La parte que enseña a **mover y transformar datos a escala**, más allá de lo que pandas aguanta. Cubre orquestación (Airflow, Prefect, Dagster), procesamiento distribuido (PySpark, Polars), almacenamiento analítico (BigQuery, Snowflake, DuckDB), streaming (Kafka, Kinesis), formatos columnares (Parquet, Avro) y modelado dimensional (star/snowflake schemas).

Es la parte donde el data scientist deja de pedirle datos al equipo de data engineering y empieza a moverlos él mismo cuando es necesario. No reemplaza a un data engineer senior, pero sí cubre el 80 % de los casos donde el bottleneck era "esto no cabe en memoria" o "este pipeline corre 8 horas y falla a la mitad".

## 🧩 Problemas que resuelve

- Orquestar un pipeline de N pasos con dependencias, retries y observabilidad.
- Procesar datasets de TBs con PySpark o de GBs con Polars sin cargarlos en RAM.
- Consultar un data warehouse moderno (BigQuery, Snowflake, DuckDB local) desde Python.
- Consumir un stream de eventos en tiempo real (Kafka / Kinesis).
- Elegir el formato de almacenamiento correcto (Parquet vs Avro vs CSV) según el patrón de lectura.
- Diseñar un modelo dimensional (star schema) para BI y para features de ML.

## 🎓 Resultados de aprendizaje

Al finalizar esta parte, el estudiante podrá:

- Convertir un script `pandas` que tomaba horas en un pipeline Airflow/Prefect con Polars o PySpark.
- Migrar un workflow desde CSV a Parquet y medir la mejora en tiempo y espacio.
- Diseñar un star schema para un caso de negocio dado.

## 🗺️ Estructura temática

- **Orquestación** — clases 173–174 — Airflow, Prefect, Dagster.
- **Procesamiento distribuido y moderno** — clases 175–176 — PySpark, Polars.
- **Data warehouses y streaming** — clases 177–178 — BigQuery / Snowflake / DuckDB, Kafka / Kinesis.
- **Formatos y modelado** — clases 179–180 — Parquet/Avro, modelado dimensional.

## 📚 Índice de clases (8)

- [208 — Pipelines ETL/ELT con Airflow](208-pipelines-etl-elt-con-airflow/README.md)
- [209 — Pipelines con Prefect o Dagster](209-pipelines-con-prefect-o-dagster/README.md)
- [210 — PySpark para datasets grandes](210-pyspark-para-datasets-grandes/README.md)
- [211 — Polars como alternativa moderna](211-polars-como-alternativa-moderna/README.md)
- [212 — Data warehouses: BigQuery, Snowflake, DuckDB](212-data-warehouses-bigquery-snowflake-duckdb/README.md)
- [213 — Streaming intro: Kafka, Kinesis](213-streaming-intro-kafka-kinesis/README.md)
- [214 — Formatos columnares: Parquet, Avro](214-formatos-columnares-parquet-avro/README.md)
- [215 — Modelado dimensional (star/snowflake schemas)](215-modelado-dimensional-star-snowflake-schemas/README.md)

---

> [⬅️ Volver al programa](../../README.md) · [📚 Índice completo](../README.md) · [⏮️ Parte anterior](../parte-4-mlops/README.md) · [⏭️ Parte siguiente](../parte-6-sistemas-de-recomendacion/README.md)
