"""TRANSFORM: turn the raw wide table into a clean, typed, long table."""
import pandas as pd


def tidy_tsv(raw: pd.DataFrame, codes: pd.DataFrame, keep_raw: bool = False) -> pd.DataFrame:
    """Clean the raw Eurostat table.

    Steps: wide -> long, split value and flag, convert types, add country names.

    ``raw`` has one column per year plus code columns (at least ``geo``).
    Columns returned: geo, country, is_aggregate, year, value, flag
    (plus ``raw_cell`` when ``keep_raw=True``, handy for debugging).
    Codes with no match in ``codes`` get ``country = NaN`` (they are not hidden).
    """
    id_columns = [c for c in raw.columns if not c.isdigit()]
    long = raw.melt(id_vars=id_columns, var_name="year", value_name="raw_cell")
    parts = long["raw_cell"].str.strip().str.split(r"\s+", n=1, expand=True)
    long["value"] = pd.to_numeric(parts[0].where(parts[0] != ":"), errors="coerce")
    long["flag"] = parts[1] if parts.shape[1] > 1 else None
    long["year"] = long["year"].astype(int)
    tidy = long.merge(codes, on="geo", how="left")
    columns = ["geo", "country", "is_aggregate", "year", "value", "flag"]
    if keep_raw:
        columns.append("raw_cell")
    return tidy[columns]


def countries_only(df: pd.DataFrame) -> pd.DataFrame:
    """Drop aggregates such as EU27_2020 or EU28 (they are not countries)."""
    return df[df["is_aggregate"] == False]  # noqa: E712  (NaN is not False)


def validate(df: pd.DataFrame) -> dict:
    """Quality checks. Returns a dict {check name: number of problems}."""
    unconverted = df["value"].isnull() & ~df["raw_cell"].str.strip().str.startswith(":")
    return {
        "duplicate (country, year) rows": int(df.duplicated(["geo", "year"]).sum()),
        "values outside 0-15": int(((df["value"] < 0) | (df["value"] > 15)).sum()),
        "codes without a country name": int(df["country"].isnull().sum()),
        "text that could not be converted to a number": int(unconverted.sum()),
    }
