# Template: files of a project that uses AI assistants

A small starter you can copy into your own project. Each file is **mostly commented out on purpose**: the `TODO` blocks show what to write; the comments explain what the file is for. The example is a tiny data-science project (cleaning a CSV of temperatures).

```
my-project/
├── AGENTS.md          instructions for the AI assistant (read it first, always)
├── CLAUDE.md          one line that makes Claude read AGENTS.md
├── SPECS.md           WHAT we build (requirements, in plain language)
├── DESIGN.md          HOW it should look / behave (choices, data layout, plots)
├── ARCHITECTURE.md    HOW it is built (folders, modules, data flow)
├── TASKS.md           the to-do list: small steps, one at a time
├── README.md          for people (what the project is, how to run it)
├── pyproject.toml     libraries (uv)    ┐
├── uv.lock            exact versions    ┘ created by uv
├── data/
│   └── .gitkeep       keeps the empty folder in Git
├── notebooks/         exploration
├── src/               reusable code (.py)
└── tests/             tests (pytest)
```

You do **not** need all of them in every project. Start with `AGENTS.md` and `TASKS.md`; add the others when the project grows.
