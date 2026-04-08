from __future__ import annotations

from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATASETS_DIR = BASE_DIR / "datasets"


def load_csv(filename: str) -> pd.DataFrame:
    path = DATASETS_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {path}")
    return pd.read_csv(path)


def add_total_column(df: pd.DataFrame) -> pd.DataFrame:
    required = {"unidades", "precio_unitario", "descuento_pct"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    result = df.copy()
    result["total_bruto"] = result["unidades"] * result["precio_unitario"]
    result["total_neto"] = result["total_bruto"] * (1 - result["descuento_pct"])
    return result


def resumen_por_columna(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    if group_col not in df.columns or value_col not in df.columns:
        raise ValueError("Las columnas indicadas no existen en el DataFrame.")
    return (
        df.groupby(group_col, as_index=False)[value_col]
        .sum()
        .sort_values(value_col, ascending=False)
    )


def tasa_perdida_clientes(df: pd.DataFrame) -> pd.DataFrame:
    required = {"clientes_activos", "clientes_perdidos"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")
    result = df.copy()
    result["tasa_perdida"] = (result["clientes_perdidos"] / result["clientes_activos"]).round(4)
    return result
