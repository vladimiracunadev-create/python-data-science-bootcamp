from pathlib import Path
import sys
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
sys.path.append(str(BASE_DIR))

from src.data_checks import required_columns_present, null_report


def test_required_columns_present_detects_all():
    df = pd.DataFrame({"a": [1], "b": [2]})
    ok, missing = required_columns_present(df, ["a", "b"])
    assert ok is True
    assert missing == []


def test_null_report_structure():
    df = pd.DataFrame({"a": [1, None], "b": [2, 3]})
    report = null_report(df)
    assert {"columna", "nulos", "porcentaje_nulos"} <= set(report.columns)
