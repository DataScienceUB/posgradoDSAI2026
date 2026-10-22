"""EXTRACT: get the raw data into DataFrames, without cleaning it."""
import ssl
import urllib.error
import urllib.request
from pathlib import Path

import pandas as pd

# Eurostat dissemination API (SDMX 2.1). Docs:
# https://wikis.ec.europa.eu/display/EUROSTATHELP/API+SDMX+2.1+-+data+query
BASE = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data"

# The dataset used in class and the slice we keep:
# A (annual) . PC_GDP (% of GDP) . ED02-8 (pre-primary to tertiary) . all countries
DATASET = "educ_uoe_fine06"
KEY = "A.PC_GDP.ED02-8."


def _ssl_context() -> ssl.SSLContext:
    """Use the certificates of ``certifi`` when installed (some Python installs
    on macOS cannot find the system ones and every HTTPS download fails)."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def download_eurostat(code: str = DATASET, dest_dir: Path = Path("."), key: str | None = None) -> Path:
    """Download a Eurostat dataset as TSV into ``dest_dir`` and return its path.

    ``key`` selects a slice of the dataset: one code per dimension, separated
    by dots, in the order of the file's first column; an empty position means
    "all". By default it is ``KEY`` for the class dataset and the whole
    dataset for any other code; ``key=""`` always downloads the whole dataset.

    Raises ``RuntimeError`` with a readable message if the download fails
    (no network, dataset withdrawn or changed).
    """
    if key is None:
        key = KEY if code == DATASET else ""
    url = f"{BASE}/{code}/{key}?format=TSV&compressed=false" if key else f"{BASE}/{code}?format=TSV&compressed=false"
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{code}.tsv"
    try:
        with urllib.request.urlopen(url, timeout=30, context=_ssl_context()) as resp:
            body = resp.read()
    except (urllib.error.URLError, TimeoutError) as err:
        raise RuntimeError(f"Could not download '{code}': {err}") from err
    if not body.strip():
        raise RuntimeError(f"Empty response for '{code}': the dataset may not exist.")
    tmp = dest.with_suffix(".tsv.tmp")
    tmp.write_bytes(body)
    tmp.replace(dest)
    return dest


def read_long_csv(path: Path) -> pd.DataFrame:
    """Long SDMX-CSV (one row per country and year). Missing values are empty cells."""
    return pd.read_csv(path, usecols=["geo", "TIME_PERIOD", "OBS_VALUE", "OBS_FLAG"])


def read_raw_tsv(path: Path) -> pd.DataFrame:
    """Raw Eurostat TSV: wide (one column per year), flags inside the cells.

    The first column packs several codes separated by commas, for example
    ``A,PC_GDP,ED02-8,ES`` under the header ``freq,unit,isced11,geo\\TIME_PERIOD``.
    It is split into one column per code (``freq``, ``unit``, ``isced11``, ``geo``).

    Everything is read as text (``dtype=str``) so pandas does not guess types
    on values like ``5.98 d`` or ``: u``.
    """
    df = pd.read_csv(path, sep="\t", dtype=str)
    df.columns = [c.strip() for c in df.columns]
    key = df.columns[0]
    names = key.split("\\")[0].split(",")
    df[names] = df[key].str.split(",", expand=True)
    years = [c for c in df.columns if c.isdigit()]
    return df[names + years]
