from __future__ import annotations

import pandas as pd


def assert_no_empty_dataframe(df: pd.DataFrame) -> bool:
    if df.empty:
        raise ValueError("El DataFrame está vacío")
    return True


def assert_columns_exist(df: pd.DataFrame, columns: list[str]) -> bool:
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas: {missing}")
    return True


def required_columns_present(df: pd.DataFrame, columns: list[str]) -> tuple[bool, list[str]]:
    missing = [col for col in columns if col not in df.columns]
    return len(missing) == 0, missing


def null_report(df: pd.DataFrame) -> pd.DataFrame:
    report = pd.DataFrame({
        "columna": df.columns,
        "nulos": [int(df[col].isna().sum()) for col in df.columns],
    })
    report["porcentaje_nulos"] = (report["nulos"] / len(df)).round(4)
    return report
