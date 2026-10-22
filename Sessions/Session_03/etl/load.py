"""LOAD: save the clean table where it can be reused."""
import json
import sqlite3
from pathlib import Path

import duckdb
import pandas as pd


def to_documents(df: pd.DataFrame) -> list[dict]:
    """One JSON-like document per country, the shape a document database (MongoDB…) stores.

    {"geo": "ES", "country": "Spain", "spending": {"2014": 4.15, …}, "flags": {"2019": "p", …}}
    Missing values become ``None`` (``null`` in JSON). ``flags`` only appears when the
    country has at least one flag: documents do not need to share the same fields.
    """
    documents = []
    for (geo, country), group in df.groupby(["geo", "country"]):
        document = {
            "geo": geo,
            "country": country,
            "spending": {str(year): (None if pd.isna(value) else float(value))
                         for year, value in zip(group["year"], group["value"])},
        }
        flags = {str(year): flag for year, flag in zip(group["year"], group["flag"]) if isinstance(flag, str)}
        if flags:
            document["flags"] = flags
        documents.append(document)
    return documents


def save_all(df: pd.DataFrame, out_dir: Path, name: str = "education_spending") -> dict:
    """Save ``df`` as CSV, Parquet, SQLite, DuckDB and JSON documents. Returns {format: path}."""
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = {
        "csv": out_dir / f"{name}.csv",
        "parquet": out_dir / f"{name}.parquet",
        "sqlite": out_dir / f"{name}.db",
        "duckdb": out_dir / f"{name}.duckdb",
        "json": out_dir / f"{name}.json",
    }
    df.to_csv(paths["csv"], index=False)
    df.to_parquet(paths["parquet"], index=False)

    con = sqlite3.connect(paths["sqlite"])
    try:
        df.to_sql(name, con, if_exists="replace", index=False)
    finally:
        con.close()

    con = duckdb.connect(paths["duckdb"])
    try:
        con.register("df_to_load", df)
        con.execute(f"CREATE OR REPLACE TABLE {name} AS SELECT * FROM df_to_load")
    finally:
        con.close()

    paths["json"].write_text(json.dumps(to_documents(df), indent=2, ensure_ascii=False), encoding="utf-8")
    return paths


def roundtrip_ok(df: pd.DataFrame, parquet_path: Path) -> bool:
    """Read the Parquet file back and check it is identical to ``df``."""
    back = pd.read_parquet(parquet_path)
    return back.reset_index(drop=True).equals(df.reset_index(drop=True))
