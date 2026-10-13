# DESIGN.md

## Data
- Column names in `snake_case`: `date`, `station`, `temperature_c` (the unit goes in the name).
- Station names in Title case: `Gracia`, `Montjuic`, `Raval`.
- Dates are real dates (datetime), not strings.

## Plots
- One line per station, same colours in every plot.
- Axis labels with units (`temperature (°C)`), a title that says what you see.
- Grid with low opacity; a legend.

## Code style
- Functions with a docstring and type hints.
- A notebook cell has at most ~15 lines; reusable code lives in `src/`.
