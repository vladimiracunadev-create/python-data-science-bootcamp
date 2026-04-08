from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.utils import add_total_column, load_csv, resumen_por_columna


def test_load_csv_returns_dataframe():
    df = load_csv("ventas_tienda.csv")
    assert not df.empty
    assert "sucursal" in df.columns


def test_load_csv_missing_file_raises():
    import pytest
    with pytest.raises(FileNotFoundError):
        load_csv("archivo_que_no_existe.csv")


def test_add_total_column_creates_expected_fields():
    df = load_csv("ventas_tienda.csv")
    result = add_total_column(df)
    assert "total_bruto" in result.columns
    assert "total_neto" in result.columns


def test_add_total_column_values_are_positive():
    df = add_total_column(load_csv("ventas_tienda.csv"))
    assert (df["total_bruto"] >= 0).all()
    assert (df["total_neto"] >= 0).all()


def test_resumen_por_columna_returns_ordered_output():
    df = add_total_column(load_csv("ventas_tienda.csv"))
    summary = resumen_por_columna(df, "sucursal", "total_neto")
    assert summary.iloc[0]["total_neto"] >= summary.iloc[-1]["total_neto"]


def test_resumen_por_columna_has_all_groups():
    df = add_total_column(load_csv("ventas_tienda.csv"))
    summary = resumen_por_columna(df, "sucursal", "total_neto")
    assert len(summary) == df["sucursal"].nunique()
