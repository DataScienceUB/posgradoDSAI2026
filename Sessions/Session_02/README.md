# Session 02 · Working environment and programming with AI

This session is about **how we work**: a reproducible Python environment (`uv`), notebooks in VS Code, Git and GitHub, and AI assistants (GitHub Copilot and Claude) used in a way you can check. It has two parts.

## A · Preparation (before the class)
A short, step-by-step guide to prepare your laptop: accounts, installation, and a check notebook. It is **not** part of the 2 hours of class; its result is the start of the *traffic light* that opens the session.

👉 **[Start here: Prepare your computer](pre_class/README.md)**

| Part | Content |
|---|---|
| [1 · Accounts](pre_class/01_accounts.md) | GitHub account, free student Copilot, course repository access (the formal part) |
| [2 · Installation](pre_class/02_installation.md) | VS Code, `uv`, Git, GitHub Desktop, extensions |
| [3 · Verification](pre_class/03_verification.md) | Create your project and run the check notebook (**required**) |
| [4 · Your first repository](pre_class/04_git_exercise.md) | Optional: create and clone a repository |
| [5 · Fork the course repository](pre_class/05_fork_course_repo.md) | Your own copy of the course repository, and how to keep it up to date (done in class if not before) |
| [Cheat sheet](pre_class/cheatsheet.md) · [Troubleshooting](pre_class/troubleshooting.md) | Commands and Plan B |

## B · In the class
| Resource | What it is |
|---|---|
| [Lab: clean the temperature data](exercises/lab/README.md) | Pairs, with your AI assistant: write a cleaning function and its tests |
| [AI assistants in VS Code](guides/ai_assistants_in_vscode.md) | Quick guide: Copilot and Claude, good habits, what to watch for |
| [Notebook: the hidden-state trap](notebooks/01_hidden_state.ipynb) | Why you must *Restart and Run All* |
| [Demos: simulated AI changes](demo/ai_diffs/README.md) | Four typical assistant mistakes, as diffs you can read |
| [Demo: notebooks in Git](demo/notebook_git/README.md) | Why notebooks are awkward in Git |
| [Git and GitHub: forks and keeping in sync](guides/git_forks_and_sync.md) | How to organize your folders, and an advanced example with forks |
| [Files of a project that uses AI assistants](guides/ai_project_files.md) · [templates](templates/ai_project/README.md) | `AGENTS.md`, `TASKS.md`, `ARCHITECTURE.md`, `SPECS.md`, `DESIGN.md` explained, with small templates |

## Folder map
```
Session_02/
├── pre_class/   preparation guide (4 parts) and the check notebook
├── exercises/   the lab
├── guides/      short guides
├── notebooks/   class notebooks
├── templates/   starter files (AI project files)
└── demo/        demos used in class
```
