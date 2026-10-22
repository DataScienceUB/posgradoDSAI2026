"""MovieLens 1M: ratings of films by users (used in Part 6, the hands-on exercises).

The dataset is published by GroupLens (University of Minnesota) for education and
research: https://grouplens.org/datasets/movielens/1m/

Three text files with fields separated by ``::``:

* ``users.dat``   UserID::Gender::Age::Occupation::Zip-code
* ``movies.dat``  MovieID::Title::Genres
* ``ratings.dat`` UserID::MovieID::Rating::Timestamp
"""
import io
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

URL = "https://files.grouplens.org/datasets/movielens/ml-1m.zip"


def download_movielens(dest_dir: Path) -> Path:
    """Download and unzip MovieLens 1M into ``dest_dir/ml-1m`` and return that folder.

    Raises ``RuntimeError`` with a readable message if the download fails.
    """
    dest_dir = Path(dest_dir)
    dest_dir.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(URL, timeout=60) as resp:
            body = resp.read()
        with zipfile.ZipFile(io.BytesIO(body)) as zf:
            zf.extractall(dest_dir)
    except (urllib.error.URLError, TimeoutError, zipfile.BadZipFile) as err:
        raise RuntimeError(f"Could not download MovieLens 1M: {err}") from err
    return dest_dir / "ml-1m"


def find_movielens(downloads_dir: Path) -> Path | None:
    """Return the folder holding the three ``.dat`` files, or None if it is not there."""
    folder = Path(downloads_dir) / "ml-1m"
    needed = ("users.dat", "movies.dat", "ratings.dat")
    return folder if all((folder / n).exists() for n in needed) else None


def read_movielens(folder: Path):
    """Read the three files into DataFrames ``(users, ratings, movies)``.

    The separator is ``::`` (two characters), which needs ``engine="python"``.
    The files have no header row, so we give the column names ourselves.
    ``movies.dat`` contains accented characters, so it is read as ``latin-1``.
    """
    folder = Path(folder)
    users = pd.read_csv(folder / "users.dat", sep="::", header=None, engine="python",
                        names=["user_id", "gender", "age", "occupation", "zip"])
    ratings = pd.read_csv(folder / "ratings.dat", sep="::", header=None, engine="python",
                          names=["user_id", "movie_id", "rating", "timestamp"])
    movies = pd.read_csv(folder / "movies.dat", sep="::", header=None, engine="python",
                         names=["movie_id", "title", "genres"], encoding="latin-1")
    return users, ratings, movies
