# Files of a project that uses AI assistants

An assistant works much better when the project tells it **what we are building, how it is organized and what to do next**. Instead of explaining all that in every prompt, we keep it in a few small text files (Markdown) **inside the project**.

```
my-project/
├── AGENTS.md          instructions for the AI assistant (read it first, always)
├── SPECS.md           WHAT we build
├── DESIGN.md          HOW it should look / behave
├── ARCHITECTURE.md    HOW it is built
├── TASKS.md           the to-do list, in small steps
├── README.md          for people
├── pyproject.toml, uv.lock
├── data/              (.gitkeep keeps the empty folder in Git)
├── notebooks/         exploration
├── src/               reusable code (.py)
└── tests/             tests (pytest)
```

| File | What it is | Example in a data-science project |
|---|---|---|
| `AGENTS.md` | Rules and commands for the assistant. Read at the start of every conversation. Standard format: [agents.md](https://agents.md). | "Use uv. Run tests with `uv run pytest`. Never edit a test to make it pass." |
| `SPECS.md` | **What** we want, in plain language: goal, inputs, outputs, acceptance criteria. | "Produce a clean table of daily temperatures per station; no values ≤ −100." |
| `DESIGN.md` | **How it should look or behave**: naming, output format, plot style. | "Columns in snake_case; one line per station in every plot." |
| `ARCHITECTURE.md` | **How it is built**: folders, modules, data flow. | "Cleaning lives in `src/clean.py`; notebooks only call it." |
| `TASKS.md` | The to-do list, in small steps, one at a time. | "[ ] 2. Write `clean_readings()`" |

**Tips**
* Start with `AGENTS.md` and `TASKS.md`. Add the others when the project grows.
* Keep each file **short**. If it is long, the assistant (and you) will not follow it.
* Ask the assistant to work on **one task** of `TASKS.md`, then **read the diff**.
* These files are for you too: they are how you think the project through before writing code.

**Which assistant reads what?** `AGENTS.md` is read by many tools (GitHub Copilot, among others); Claude Code reads `CLAUDE.md`, so a one-line `CLAUDE.md` containing `@AGENTS.md` points it to the same instructions. Interfaces change quickly: check the docs ([Claude Code memory](https://code.claude.com/docs/en/memory) · [Copilot repository instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)).

👉 A small starter with all of these files, commented and with a tiny example: [`templates/ai_project/`](../templates/ai_project/README.md).
