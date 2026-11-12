<!-- Q: Explain Git to a complete beginner. -->

# Git, explained simply

## The core idea
Git is a **save-point system for your files**. Think of writing an essay: instead of saving `essay_final.docx`, `essay_final_v2.docx`, `essay_REALLY_final.docx`, Git keeps one project and remembers every version you choose to save, along with who changed what and why.

## Why people use it
- **Undo mistakes:** go back to any earlier version.
- **See history:** what changed, when, and who did it.
- **Work in parallel:** try an idea without breaking the working version.
- **Collaborate:** many people can edit the same project and merge their work.

## Key vocabulary

| Term | Plain meaning |
|---|---|
| **Repository (repo)** | A project folder that Git is tracking, including its history |
| **Commit** | A saved snapshot, with a short message describing it |
| **Staging area** | A "loading dock" where you choose which changes go into the next commit |
| **Branch** | A separate line of work, like a parallel copy to experiment in |
| **Merge** | Combining one branch's changes into another |
| **Remote** | A copy of the repo on a server (e.g. GitHub) |
| **Clone** | Download a copy of a remote repo |
| **Push / Pull** | Upload your commits / download others' commits |

## Git vs. GitHub
- **Git** is the tool on your computer.
- **GitHub** (also GitLab, Bitbucket) is a website that hosts Git repos so you can share and collaborate. They're related but not the same thing.

## The basic workflow
```bash
git init                    # start tracking a folder
git add notes.txt           # stage a change
git commit -m "Add notes"   # save a snapshot
git status                  # see what's changed
git log                     # view history
```

Then, with a remote:
```bash
git push    # send your commits up
git pull    # get others' commits
```

## A mental picture
Imagine a timeline of snapshots:

```
A --- B --- C --- D      (main branch)
       \
        E --- F          (your experiment branch)
```

You can work on `E` and `F` without touching `main`, then merge them in if you like the result.

## Tips for beginners
1. **Commit often** with clear messages ("Fix login bug", not "stuff").
2. **Use `git status`** constantly; it tells you what's going on.
3. **Don't panic:** committed work is very hard to lose permanently.

If you'd like, I can walk you through creating your first repo hands-on in a practice folder.
