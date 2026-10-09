# Command cheat sheet

[← Back to the guide](README.md)

Run these **inside the project folder** (the terminal path should end in the project name).

| I want to… | Command |
|---|---|
| Create a new project | `uv init --python 3.12 my-project` |
| Add a library | `uv add <library>` |
| Add a library only for development (e.g. notebooks) | `uv add --dev <library>` |
| Remove a library | `uv remove <library>` |
| Recreate the environment from the lock file (e.g. on another laptop) | `uv sync` |
| Change the Python version of a project | `uv python pin <version>` then `uv sync` |
| Run a Python file | `uv run main.py` |
| Open notebooks in the browser (Plan B) | `uv run jupyter lab` |

> **Why Python 3.12?** In this course we all use **Python 3.12**: it is stable, supported by all the libraries we need and by `uv`, and it makes our environments identical. See the [official Python versions table](https://devguide.python.org/versions/). If you need another version for a project it is easy to change (`uv python pin 3.13` then `uv sync`): [uv: Python versions](https://docs.astral.sh/uv/concepts/python-versions/). For this course, keep 3.12.
