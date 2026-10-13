"""Cleaning of the raw temperature file (task 2 of TASKS.md)."""
import pandas as pd


def clean_readings(df: pd.DataFrame) -> pd.DataFrame:
    """Return a clean copy of the raw readings.

    Input columns: date, station, temperature_c (messy, see SPECS.md).
    Output: one row per (date, station), datetime dates, Title-case stations,
    float temperatures without -999 / missing values, sorted by station and date.
    """
    raise NotImplementedError("Task 2: write me (see TASKS.md and SPECS.md)")
