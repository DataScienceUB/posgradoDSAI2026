# Postgraduate in Data Science & AI · Course resources

Universitat de Barcelona · Facultat de Matemàtiques i Informàtica. All material is in English.

This repository is the **index of every resource** of the course. Each `Session_NN/` folder contains that session's guides, notebooks, exercises and data. New resources are added here as the course goes on.

## 🚀 Start here: prepare your environment

Before **Session 02**, follow the step-by-step guide (about 45 minutes, no programming experience needed, with screenshots):

👉 **[Session 02 · Pre-class guide: prepare your computer](Session_02/pre_class/README.md)**

You will install VS Code, `uv` and Git, create a project and run a verification notebook. The result is your ticket for the *traffic light* at the beginning of the class.

## Resources index

| Session | Resource | What it is |
|---|---|---|
| 02 | [**Pre-class guide**](Session_02/pre_class/README.md) | Install everything and check it works (**do it before the class**) |
| 02 | [`verify_setup.ipynb`](Session_02/pre_class/verify_setup.ipynb) | Notebook that checks your setup |
| 02 | [AI assistants in VS Code](Session_02/guides/ai_assistants_in_vscode.md) | Quick guide: GitHub Copilot and Claude Code |
| 02 | [Lab: clean the temperature data](Session_02/exercises/lab/README.md) | In-class lab (pairs) |
| 02 | [Notebook: the hidden-state trap](Session_02/notebooks/01_hidden_state.ipynb) | Why you must *Restart and Run All* |
| 02 | [Demos](Session_02/demo/ai_diffs/README.md) | Simulated AI changes and notebooks in Git |

## Quick reference

```bash
uv init --python 3.12 my-project   # new project
cd my-project
uv add pandas matplotlib           # add libraries
uv sync                            # recreate the environment from uv.lock
uv run jupyter lab                 # Plan B if the notebook kernel fails in VS Code
```

Questions about the course: ask in class or contact the instructors.
