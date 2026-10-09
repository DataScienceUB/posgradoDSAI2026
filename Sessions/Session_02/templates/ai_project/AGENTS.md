# AGENTS.md

<!--
WHAT IS THIS FILE?
  Instructions for AI assistants (Copilot, Claude, others) working in this project.
  The assistant reads it at the start of every conversation, so you do not repeat the same rules in every prompt.
  Keep it SHORT and concrete: what the project is, how to run things, what to do and not to do.
  Standard format shared by many tools: https://agents.md

INCLUDES
  The lines below that start with "@" import another file into the instructions (this syntax is understood by Claude;
  other tools may need you to simply mention the files, so we also list them in plain text).
  Check the current documentation of your assistant: https://code.claude.com/docs/en/memory
-->

<!-- TODO: uncomment and adapt. -->

<!--
## Project
Clean the raw temperature file of three stations and plot it. Python 3.12, managed with uv.

## Read first (context files)
@SPECS.md
@DESIGN.md
@ARCHITECTURE.md
@TASKS.md
(Plain-text list for tools without includes: SPECS.md, DESIGN.md, ARCHITECTURE.md, TASKS.md)

## Commands
- Install / sync environment:  uv sync
- Run tests:                   uv run pytest
- Run a script:                uv run python src/clean.py

## Rules
- Work on ONE task of TASKS.md at a time; say which one.
- Small changes. Do not touch files you were not asked to touch.
- Never edit a test to make it pass: if a test fails, explain why and ask.
- Use only libraries already in pyproject.toml; ask before adding one (uv add).
- After every merge/join, check row counts and totals.
-->
