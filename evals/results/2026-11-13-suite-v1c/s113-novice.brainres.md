<!-- Q: Explain Git to a complete beginner. -->

Git is a tool that saves snapshots of your project's files, so you can go back to any earlier version and see what changed and when.

Think of it as "undo" for a whole folder, with a note on every save.

**Key terms**

| Term | Meaning |
|---|---|
| Repository (repo) | A project folder that Git is tracking |
| Commit | One saved snapshot, with a short message describing it |
| Branch | A separate line of work, so you can try something without touching the main version |
| Remote | A copy of the repo on a server (such as GitHub), used for backup and sharing |

**Why people use it**

1. You can undo mistakes by returning to an older commit.
2. Several people can work on the same project without overwriting each other.
3. You get a full history of who changed what, and why.

**A first example**

Run these in a terminal, inside a new folder:

```bash
git init                      # start tracking this folder
echo "hello" > notes.txt      # create a file
git add notes.txt             # choose what goes in the next snapshot
git commit -m "Add notes"     # save the snapshot with a message
git log                       # see your history
```

`git add` and `git commit` are separate steps because you may want to save only some of your changes in a given snapshot.

Git works on your own computer and needs no internet. GitHub is a different thing: a website that hosts remote copies of Git repos.

Next step: install Git (`git --version` checks whether you already have it), then run the example above in an empty folder.
