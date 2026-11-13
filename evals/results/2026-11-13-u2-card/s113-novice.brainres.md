<!-- Q: Explain Git to a complete beginner. -->

Git is a tool that saves snapshots of your project's files, so you can go back to any earlier version and see exactly what changed and when.

Think of it as "save game" for your folder. Instead of files like `report_final_v2_REAL.docx`, you keep one file and Git remembers every saved version.

**Four terms to know**

- **Repository (repo):** a project folder that Git is tracking.
- **Commit:** one saved snapshot, with a short message describing the change.
- **Branch:** a separate line of work, so you can try something without breaking the main version.
- **Remote:** a copy of the repo on a server (such as GitHub), used for backup and teamwork.

**A worked example**

In a terminal, inside a folder called `my-site`:

```bash
git init                      # start tracking this folder
git add index.html            # choose what goes into the next snapshot
git commit -m "Add homepage"  # save the snapshot with a message
```

Now you edit `index.html` and break it. To see what you changed:

```bash
git diff
```

To throw away the edit and return to the last snapshot:

```bash
git restore index.html
```

To see your history:

```bash
git log --oneline
```

**Why the `add` step exists:** it lets you pick which changes go into a commit, so each snapshot stays small and about one thing.

**Git vs. GitHub:** Git runs on your computer and works offline. GitHub is a website that hosts Git repos so you can share them. They are different things.

Next step: run `git init` in a throwaway folder, create a text file, and make your first commit.
