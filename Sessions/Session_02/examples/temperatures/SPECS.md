# SPECS.md

## Goal
Produce a clean table of daily temperatures per station from the raw file, and a plot that shows it.

## Input
`data/stations_raw.csv` with columns `date`, `station`, `temperature_c`. It is synthetic and messy on purpose:
- decimal commas (`"12,5"`), text such as `N/A`, empty cells;
- `-999` used as "no measurement";
- station names in different case or with spaces (`RAVAL`, `  raval`);
- duplicated rows.

## Output
A table (pandas DataFrame) with one row per (`date`, `station`):
- `date`: datetime;
- `station`: `Gracia`, `Montjuic` or `Raval`;
- `temperature_c`: float.
Rows without a usable temperature are removed. Sorted by station and date.

## Acceptance criteria
- [ ] No `temperature_c` value is <= -100 and none is missing.
- [ ] No duplicated (`date`, `station`) pair.
- [ ] Exactly three station names.
- [ ] The plot shows three smooth curves rising from winter to spring, with no sudden drops.
- [ ] `uv run pytest` passes.
