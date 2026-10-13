# ARCHITECTURE.md

## Folders
```
temperatures/
├── data/stations_raw.csv      raw input (never edited)
├── notebooks/explore.ipynb    exploration; calls code from src/
├── src/clean.py               clean_readings(df) -> DataFrame
├── src/plots.py               plot_stations(df) -> matplotlib Figure
└── tests/test_clean.py        tests of clean_readings
```

## Data flow
`data/stations_raw.csv` -> `pandas.read_csv` -> `clean_readings()` -> clean DataFrame -> `plot_stations()` -> figure

## Decisions
- Cleaning is a plain function in a `.py` file, so it can be tested (a notebook cannot be tested easily).
- Tests import from `src/` (configured in `pyproject.toml`).
