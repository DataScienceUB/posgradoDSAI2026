# Lab · Clean the temperature data (pairs, ~25 min)

**Mission:** with your AI assistant, write `clean_readings` in `clean.py` so the tests pass, and check with your own eyes that the data is clean.
You are responsible for every line you hand in.

## Files
| File | What it is |
|---|---|
| `stations_raw.csv` | **Synthetic** daily temperatures of 3 stations, with problems on purpose |
| `clean.py` | Skeleton of the function you must write |
| `test_clean.py` | Tests (one is written, you add the `TODO` ones) |
| `lab.ipynb` | Notebook with step-by-step instructions and the final plot |

## Setup (if you did not do it in class)
1. Create a **private** repository `session02-lab` (GitHub Desktop: *File → New repository…*), outside your `postgrau-env` folder.
2. Inside its folder, in a terminal:
   ```bash
   uv init --python 3.12
   uv add pandas matplotlib
   uv add --dev ipykernel pytest
   ```
3. Copy the four files above into the repository folder, open the folder in VS Code and make your first commit.
([pytest documentation](https://docs.pytest.org/en/stable/getting-started.html) · [uv projects](https://docs.astral.sh/uv/guides/projects/))

## Steps
1. **Look.** Run the first cells of `lab.ipynb`. List the problems you find (at least five) in `AI_LOG.md`.
2. **Ask.** Use Copilot or Claude Code in VS Code to write `clean_readings`. Give context and ask for small steps.
3. **Check.** Read the diff *before* accepting. Run `uv run pytest`, then add the missing tests.
4. **See.** Run the last cells of the notebook: you should see three smooth lines rising from winter to spring, with no drops to −999.
5. **Explain and commit.** Explain the code to your partner. Make **at least 3 commits** and push.

## Deliverable
Your repository on GitHub with: notebook (*Restart and Run All* works), `clean.py`, green tests, ≥ 3 commits, and `AI_LOG.md` with one thing the assistant got wrong (or one risk you detected).
