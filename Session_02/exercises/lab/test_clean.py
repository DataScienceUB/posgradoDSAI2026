"""Tests for clean_readings. Run with:  uv run pytest

The first test is written for you. Add the others (ask your assistant, then CHECK the tests:
a test that cannot fail is useless).
"""
import pandas as pd

from clean import clean_readings


def make_raw():
    return pd.DataFrame(
        {
            "date": ["2024-01-01", "2024-01-01", "2024-01-02", "2024-01-03", "2024-01-04"],
            "station": ["Raval", "  raval", "RAVAL", "Raval", "Raval"],
            "temperature_c": ["12,5", "12.5", -999, "N/A", 13.0],
        }
    )


def test_station_names_are_normalised():
    result = clean_readings(make_raw())
    assert set(result["station"]) == {"Raval"}


# TODO: test that temperature_c is numeric (float)
# TODO: test that no value is <= -100 (the -999 "no measurement" marker is gone)
# TODO: test that there are no duplicated (date, station) pairs
# TODO: test that "12,5" (decimal comma) became 12.5
