"""The whole ETL in one command:  uv run python -m etl.pipeline"""
from pathlib import Path

import pandas as pd

from etl.extract import read_raw_tsv
from etl.load import roundtrip_ok, save_all
from etl.transform import countries_only, tidy_tsv, validate

ROOT = Path(__file__).resolve().parent.parent


def run(first_year: int = 2014, last_year: int = 2023, verbose: bool = True) -> pd.DataFrame:
    # Extract
    raw = read_raw_tsv(ROOT / "data" / "raw" / "educ_uoe_fine06.tsv")
    codes = pd.read_csv(ROOT / "data" / "reference" / "geo_codes.csv")
    if verbose:
        print(f"Extract : {raw.shape[0]} rows x {raw.shape[1]} columns (wide)")

    # Transform
    tidy = tidy_tsv(raw, codes, keep_raw=True)
    problems = {k: v for k, v in validate(tidy).items() if v}
    if problems:
        raise ValueError(f"Data quality problems found: {problems}")
    final = (
        countries_only(tidy)
        .query("@first_year <= year <= @last_year")
        .drop(columns=["is_aggregate", "raw_cell"])
        .reset_index(drop=True)
    )
    if verbose:
        print(f"Transform: {len(final)} rows, {int(final['value'].isnull().sum())} missing values left as missing")

    # Load
    paths = save_all(final, ROOT / "data" / "processed")
    ok = roundtrip_ok(final, paths["parquet"])
    if verbose:
        print("Load    :", ", ".join(p.name for p in paths.values()), "| round trip OK:", ok)
    if not ok:
        raise RuntimeError("Parquet round trip failed")
    return final


if __name__ == "__main__":
    run()
