from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.utils import load_csv, add_total_column, resumen_por_columna


def test_load_csv_returns_dataframe():
    df = load_csv("ventas_tienda.csv")
    assert not df.empty
    assert "sucursal" in df.columns


def test_add_total_column_creates_expected_fields():
    df = load_csv("ventas_tienda.csv")
    result = add_total_column(df)
    assert "total_bruto" in result.columns
    assert "total_neto" in result.columns


def test_resumen_por_columna_returns_ordered_output():
    df = add_total_column(load_csv("ventas_tienda.csv"))
    summary = resumen_por_columna(df, "sucursal", "total_neto")
    assert summary.iloc[0]["total_neto"] >= summary.iloc[-1]["total_neto"]
