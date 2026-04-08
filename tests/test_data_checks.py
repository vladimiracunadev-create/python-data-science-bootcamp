from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import pandas as pd

from src.data_checks import required_columns_present, null_report, assert_no_empty_dataframe


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
    import pytest
    df = pd.DataFrame()
    with pytest.raises((AssertionError, ValueError)):
        assert_no_empty_dataframe(df)


def test_null_report_percentage():
    df = pd.DataFrame({"col": [None, None, 1, 1]})
    report = null_report(df)
    row = report[report["columna"] == "col"].iloc[0]
    # porcentaje_nulos está en fracción (0.5 = 50%)
    assert abs(row["porcentaje_nulos"] - 0.5) < 0.01
