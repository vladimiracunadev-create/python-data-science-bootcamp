"""Chequeos de calidad para DataFrames del bootcamp.

Estas funciones se usan como apoyo docente y también como utilidades de sistema.
Su objetivo es detectar problemas comunes de calidad antes de que un análisis o
un modelo produzca conclusiones poco confiables.
"""

from __future__ import annotations

import pandas as pd


def assert_no_empty_dataframe(df: pd.DataFrame) -> bool:
    """Verifica que la tabla tenga filas antes de continuar.

    Qué resuelve:
        Evita seguir con cálculos, gráficos o modelos cuando la carga de datos
        devolvió una tabla vacía y el resto del flujo dejaría resultados engañosos.
    """
    if df.empty:
        raise ValueError("El DataFrame está vacío")
    return True


def assert_columns_exist(df: pd.DataFrame, columns: list[str]) -> bool:
    """Valida que existan todas las columnas esperadas.

    Qué resuelve:
        Detecta temprano errores de nombres, cambios de esquema o datasets mal
        preparados antes de aplicar transformaciones dependientes de esas columnas.
    """
    missing = [col for col in columns if col not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas: {missing}")
    return True


def required_columns_present(df: pd.DataFrame, columns: list[str]) -> tuple[bool, list[str]]:
    """Indica si el DataFrame cumple el esquema esperado.

    Qué resuelve:
        Entrega una respuesta booleana y la lista de faltantes para que tests,
        notebooks o validadores puedan decidir cómo reaccionar.
    """
    missing = [col for col in columns if col not in df.columns]
    return len(missing) == 0, missing


def null_report(df: pd.DataFrame) -> pd.DataFrame:
    """Resume cantidad y porcentaje de nulos por columna.

    Qué resuelve:
        Ofrece un informe rápido de calidad para decidir si conviene limpiar,
        imputar o descartar variables antes del análisis.
    """
    report = pd.DataFrame(
        {
            "columna": df.columns,
            "nulos": [int(df[col].isna().sum()) for col in df.columns],
        }
    )
    report["porcentaje_nulos"] = (report["nulos"] / len(df)).round(4)
    return report
