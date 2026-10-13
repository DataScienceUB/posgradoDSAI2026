# AGENTS.md

Instructions for AI assistants working in this project. Keep this file short.

## Project
Clean the raw temperature file of three stations and plot it. Python 3.12, managed with `uv`.
This is the same problem as the in-class lab of Session 02, organised so that an assistant has the context it needs.

## Read first
- @SPECS.md  (what we build, acceptance criteria)
- @DESIGN.md  (naming, plots)
- @ARCHITECTURE.md  (where code goes)
- @TASKS.md  (the to-do list: work on ONE task at a time)

If your tool does not support `@` includes, open those four files yourself.

## Commands
- Set up the environment: `uv sync`
- Run the tests: `uv run pytest`
- Open the notebook: open `notebooks/explore.ipynb` in VS Code, kernel `.venv`

## Rules
- Work on **one task** of TASKS.md at a time and say which one.
- Keep changes small. Do not modify files you were not asked to modify.
- **Never edit a test to make it pass.** If a test fails, explain why and ask.
- Use only libraries already in `pyproject.toml`; ask before adding one (`uv add`).
- Never overwrite `data/stations_raw.csv`: it is the raw input.
- After cleaning, check the number of rows and that no value is <= -100.
