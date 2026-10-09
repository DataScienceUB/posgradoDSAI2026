"""Cleaning function for the raw temperature file.

Your job (with your AI assistant, but YOU review it):
implement clean_readings so that the tests in test_clean.py pass.
"""
import pandas as pd


def clean_readings(df: pd.DataFrame) -> pd.DataFrame:
    """Return a clean copy of the raw readings.

    Expected columns: date, station, temperature_c.
    TODO: tidy the station names, make temperature_c numeric, remove the
    "no measurement" values, remove duplicated rows, and sort the result.
    """
    raise NotImplementedError("Write me!")
