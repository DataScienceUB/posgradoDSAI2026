# Simulated AI changes (for the "the diff is your safety net" demo)

Each folder has `before/` (your working code), `after_ai/` (what an assistant *could* hand you) and `changes.diff`.
The cases are **simulated and reproducible**, so everybody sees the same thing. Open `before/` and `after_ai/` in
VS Code (*Compare Selected*) or open `changes.diff`, and ask yourself: what would I check before accepting this?
Then run the code in `after_ai/` (`uv run <file>.py`, or `uv run pytest` in case 4).
