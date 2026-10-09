# Git and GitHub: organizing your folders, forks and keeping in sync

This guide has three parts: **(1)** the simplest way to organize your work with this course repository, **(2)** an **advanced example** with forks, and **(3)** an alternative way to work with the course repository using a fork.

You need: a GitHub account, and (for part 2) a classmate. Everything in part 2 is done in the browser.

---

## 1 · The simple way: two folders (recommended to start)

Create one folder for the course and, inside it, **two separate folders**:

```
postgrau/
├── posgradoDSAI2026/     ← a CLONE of the course repository (read only: only for getting new material)
└── my-work/              ← YOUR own repository (where you write code, notebooks, exercises)
```

* **`posgradoDSAI2026/`** is a *clone* of the course repository. You **do not edit it**. Before each session, update it to get the new files:
  * Terminal: `git pull` (inside that folder).
  * GitHub Desktop: *Fetch origin* → *Pull origin*.
  * VS Code: *Source Control* → *Sync Changes* (or `...` → *Pull*).
* **`my-work/`** is your own repository. You create it (see the [pre-class guide, Part 4](../pre_class/04_git_exercise.md)), and you copy there the files you need to work on.

**Why two folders?** Because your changes in the clone would clash with the new material the next time you pull. Keeping them apart avoids that.

> At the end of this guide we show **another option** (working inside a fork). This two-folder way is the simplest, so start with it.

---

## 2 · Advanced example: forks

A **fork** is **your own copy, on GitHub, of someone else's repository**. You can change it freely without touching the original, and later you can bring the original's new changes into your copy. ([About forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/about-forks) · [Fork a repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo))

**Work in pairs.** You cannot fork your own repository, so one person (**A**) owns the *original* and the other (**B**) makes the *fork*. Then swap roles if you have time.
*No partner?* Fork GitHub's practice repository [`octocat/Spoon-Knife`](https://github.com/octocat/Spoon-Knife) for steps 4–5 and skip step 7.

### Step 1 · A creates a repository
On <https://github.com/new>: name `fork-practice`, **Public**, tick *Add a README file*, *Create repository*.
(It must be public so your classmate can fork it.)

### Step 2 · A writes a file (with the web editor)
GitHub has a **web version of VS Code**. Open your repository on github.com and **press the `.` key** (a dot): the page changes to an editor that looks like VS Code, in your browser ([docs](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor)).

1. Create a new file, for example `notes_A.md`, and write something in it.
2. Open **Source Control** (third icon in the left bar), write a **commit message** ("Add notes from A") and commit.
3. **Main or branch?** When you commit, the editor may offer to commit to `main` or to create a **branch**. We **do not work with branches** in this course: **always choose `main`**. 
4. In the web editor, a commit **goes straight to GitHub**: there is no separate *push* step. (On your laptop, in VS Code or GitHub Desktop, you do need the push.) Check on the repository page that the file is there.

### Step 3 · B forks the repository
B opens A's repository on github.com and clicks **Fork** (top right) → *Create fork*.
B now has `B-username/fork-practice`.

### Step 4 · Check: same content as the original
Open B's fork: it has **the same files as the original** (README and `notes_A.md`). A fork starts as an exact copy.

### Step 5 · B creates a second file (only in the fork)
In B's fork (press `.` again if you like), create `notes_B.md` with some content and commit it to `main`.
Check both repositories: **`notes_B.md` exists only in B's fork**. A's original has not changed. That is the point of a fork.

### Step 6 · A creates a second file in the original
Now A, in the **original** repository, creates `notes_A2.md` and commits it to `main`.
B's fork **does not have it** yet: forks do not update by themselves.

### Step 7 · B synchronizes the fork
In B's fork, on github.com, a banner says the fork is *behind* the original. Click **Sync fork** → **Update branch** ([docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork)).
Now B's fork has `notes_A2.md` **and** `notes_B.md`: the original's changes arrived, and B's own work is kept.

> If *Sync fork* says there are **conflicts** (the same file changed in both places), stop and ask: that needs a manual decision.

**What you learned:** a fork is an independent copy; changes in the fork do not go to the original; and the original's new changes are brought in with *Sync fork*.

---

## 3 · The other option: work inside a fork of the course repository

Instead of two folders, you can **fork the course repository** and work directly in your fork (if the repository settings allow forking; the instructors will tell you):

1. On the course repository page, click **Fork** → *Create fork*. You now have `your-username/posgradoDSAI2026`.
2. **Clone your fork** to your laptop (this is the only folder you need): GitHub Desktop *File → Clone repository…*, or VS Code *Git: Clone*.
3. Work there: your notebooks and exercises live next to the course material, in one folder.
4. **Before each session, get the new material**: on github.com, open your fork and click **Sync fork → Update branch**; then, on your laptop, **pull** (`git pull`, or *Sync Changes*).
5. When you commit, remember: **no push, no safe**. Push your work to your fork.

**Which one to choose?**

| | Two folders (part 1) | Fork (part 3) |
|---|---|---|
| Folders on your laptop | 2 | 1 |
| Getting new material | `git pull` in the clone | *Sync fork* on GitHub, then `git pull` |
| Your work and the course material | separated | together (may conflict if you edit the same file) |
| Difficulty | simplest | needs the fork concept |

If you are unsure, use the two-folder way.
