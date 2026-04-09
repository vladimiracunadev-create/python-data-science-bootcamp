"""Pruebas para utilidades de validación de DataFrames.

Confirman que los chequeos de calidad reportan columnas faltantes, nulos y
casos de tabla vacía de la misma forma que lo esperan clases y scripts.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.data_checks import assert_no_empty_dataframe, null_report, required_columns_present


def test_required_columns_present_detects_all():
    df = pd.DataFrame({"a": [1], "b": [2]})
    ok, missing = required_columns_present(df, ["a", "b"])
    assert ok is True
    assert missing == []


def test_required_columns_present_detects_missing():
    df = pd.DataFrame({"a": [1]})
    ok, missing = required_columns_present(df, ["a", "b", "c"])
    assert ok is False
    assert "b" in missing
    assert "c" in missing


def test_null_report_structure():
    df = pd.DataFrame({"a": [1, None], "b": [2, 3]})
    report = null_report(df)
    assert {"columna", "nulos", "porcentaje_nulos"} <= set(report.columns)


def test_null_report_counts_correctly():
    df = pd.DataFrame({"x": [None, None, 1], "y": [1, 2, 3]})
    report = null_report(df)
    row_x = report[report["columna"] == "x"].iloc[0]
    assert row_x["nulos"] == 2


def test_assert_no_empty_dataframe_passes():
    df = pd.DataFrame({"a": [1, 2]})
    assert_no_empty_dataframe(df)


def test_assert_no_empty_dataframe_raises():
    df = pd.DataFrame()
    with pytest.raises((AssertionError, ValueError)):
        assert_no_empty_dataframe(df)


def test_null_report_percentage():
    df = pd.DataFrame({"col": [None, None, 1, 1]})
    report = null_report(df)
    row = report[report["columna"] == "col"].iloc[0]
    # porcentaje_nulos se expresa como fracción (0.0–1.0), no como porcentaje (0–100).
    # 2 nulos de 4 filas → 0.5, no 50. Este contrato es importante porque las clases
    # que consumen el reporte aplican filtros del tipo "if pct > 0.3: drop_column",
    # y usar la escala equivocada descartaría todas las columnas (50 > 0.3 siempre).
    assert abs(row["porcentaje_nulos"] - 0.5) < 0.01
