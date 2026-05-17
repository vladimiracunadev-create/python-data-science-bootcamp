"""Utilidades de datos usadas en clases, demos y pruebas del bootcamp.

Este módulo concentra operaciones pequeñas y repetibles sobre los datasets de
trabajo. Así evitamos duplicar lógica en notebooks, scripts y tests, y dejamos
explícito qué problema resuelve cada transformación básica.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATASETS_DIR = BASE_DIR / "datasets"


def load_csv(filename: str) -> pd.DataFrame:
    """Carga un CSV del repositorio y falla temprano si el archivo no existe.

    Qué resuelve:
        Centraliza la ruta base de datasets para que clases, ejemplos y tests
        usen siempre la misma fuente de datos.
    """
    path = DATASETS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    return pd.read_csv(path)


def add_total_column(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula totales bruto y neto a partir de unidades, precio y descuento.

    Qué resuelve:
        Evita repetir la fórmula comercial en cada notebook o script cuando se
        necesita transformar ventas fila por fila.
    """
    required = {"unidades", "precio_unitario", "descuento_pct"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    result = df.copy()
    # Primero estimamos el ingreso sin descuento para conservar una referencia.
    result["total_bruto"] = result["unidades"] * result["precio_unitario"]
    # Luego aplicamos el descuento porcentual para obtener el valor final.
    result["total_neto"] = result["total_bruto"] * (1 - result["descuento_pct"])
    return result


def resumen_por_columna(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Agrupa una métrica por categoría y la ordena de mayor a menor.

    Qué resuelve:
        Prepara una tabla resumen lista para comparar sucursales, categorías u
        otros grupos antes de graficar o comunicar resultados.
    """
    if group_col not in df.columns or value_col not in df.columns:
        raise ValueError("Las columnas indicadas no existen en el DataFrame.")
    return (
        df.groupby(group_col, as_index=False)[value_col]
        .sum()
        .sort_values(value_col, ascending=False)
    )


def tasa_perdida_clientes(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula la tasa de pérdida de clientes sobre la base activa.

    Qué resuelve:
        Convierte dos columnas operativas en una métrica comparable mes a mes
        para seguimiento comercial o análisis de retención.
    """
    required = {"clientes_activos", "clientes_perdidos"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    result = df.copy()
    result["tasa_perdida"] = (
        result["clientes_perdidos"] / result["clientes_activos"]
    ).round(4)
    return result
