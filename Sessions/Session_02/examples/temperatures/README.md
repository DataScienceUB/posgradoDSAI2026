# temperatures

Example of a small data-science project prepared to work with AI assistants (Session 02): the **context files are filled in**; the code is yours to write.
It cleans the raw temperature file of three stations and plots it.

## Run it
```bash
uv sync                 # create the environment
uv run pytest           # run the tests (they fail until task 2 is done)
```
Open `notebooks/explore.ipynb` in VS Code and choose the kernel `.venv`, then *Run All*.

## The context files
| File | Read by |
|---|---|
| `AGENTS.md`, `CLAUDE.md` | the AI assistant (rules and commands) |
| `SPECS.md`, `DESIGN.md`, `ARCHITECTURE.md` | assistant and people (what, how it looks, how it is built) |
| `TASKS.md` | assistant and people (what to do next) |

The cleaning function is **not implemented**: it is the exercise. Start with `TASKS.md`, task 2 (the file includes a suggested prompt).
The in-class lab ([exercises/lab](../../exercises/lab/README.md)) is the same problem.
