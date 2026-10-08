# AI assistants in VS Code: quick guide
> Interfaces change fast. If something looks different, check the official docs.

You installed two extensions in the pre-class guide:

| Assistant | Cost for you | Docs |
|---|---|---|
| **GitHub Copilot** | Free for verified students ([how](https://docs.github.com/en/copilot/how-tos/manage-your-account/getting-free-access-to-copilot-pro-as-a-student-teacher-or-maintainer)) | [Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview) |
| **Claude Code** | Credentials will be given to you later | [Claude Code in VS Code](https://code.claude.com/docs/en/vs-code) |

## Three ways to work
1. **Autocomplete:** suggestions appear while you type; accept with `Tab`.
2. **Chat:** ask questions about your code; you decide what to copy.
3. **Agent:** the assistant reads files, edits them and runs commands. Powerful and risky: **always read the diff**.

## Good habits
* Give **context**: open the relevant files, select the code, say what the project is.
* Ask for **small steps** (one function, one test) and say what you **expect** (an example input and output).
* **Read the diff** (Source Control panel) before accepting. **Run** the code. **Test** it.
* Ask it to **explain** its code, and explain it to someone else. If you cannot explain it, do not commit it.
* Keep an `AI_LOG.md`: what you asked, what failed, what you fixed.

## What to watch for (simulated examples in `Session_02/demo/ai_diffs/`)
1. Invented names (columns, functions).
2. Obsolete functions from old tutorials.
3. Silent errors (a join that duplicates rows).
4. "Fixes" that change the test instead of the code.

## Safety
Never paste passwords, API keys or private data in a chat or a prompt. Keys never go into a repository.
