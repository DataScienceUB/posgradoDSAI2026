# TASKS.md

Work on one task at a time. Tick it when its acceptance criteria are met and the tests pass.

- [x] 1. Create the project with `uv`, the folders and the context files
- [ ] 2. Write `clean_readings()` in `src/clean.py` (see SPECS.md)
- [ ] 3. Add the missing tests in `tests/test_clean.py` (decimal comma, -999, "N/A", duplicates, numeric dtype)
- [ ] 4. Run `notebooks/explore.ipynb` and check that the plot shows three smooth curves
- [ ] 5. Write a few lines in `AI_LOG.md`: what the assistant got wrong, or a risk you detected
- [ ] 6. Commit with a clear message and push

### Suggested prompt for task 2
> Read AGENTS.md and SPECS.md. Work on task 2 only: implement `clean_readings` in `src/clean.py`.
> Do not change the tests. When finished, run `uv run pytest` and show me the diff.
