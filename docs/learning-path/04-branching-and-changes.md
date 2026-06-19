# 4. Branching and making a change

**You'll learn:** why we use branches, and how to make your change safely.

## Why a branch?

A **branch** is a private line of work. You can experiment freely without
affecting `main` (the official version) or anyone else. When your work is ready,
you propose merging the branch back in.

## Start fresh from main

Always begin from an up-to-date `main` so you're not building on stale code:

```bash
git checkout main
git pull upstream main      # or: git pull origin main
git checkout -b feature/short-description
```

Name the branch for the work, e.g. `feature/add-proficiency-bonus` or
`fix/show-negative-modifier`.

## Make the change

Edit the files the issue pointed you to. As you go:

- Keep it small and focused on the issue.
- Match the style of the code around you (naming, spacing, comments).
- Run the app to see your change in action:

  ```bash
  charsheet show hero.character.json
  ```

## Commit in small steps

A **commit** is a saved snapshot with a message. Commit each logical step:

```bash
git add -A
git status            # check what you're about to commit
git commit -m "Add proficiency bonus to the character sheet"
```

Write messages in the imperative — "Add…", "Fix…", "Update…" — as if completing
the sentence "This commit will…". Explain *why* in extra lines if it isn't
obvious.

## Check your work as you go

Run the tests often. It's much easier to find what broke right after you broke
it:

```bash
pytest
```

➡️ Next: [Writing tests with pytest](05-writing-tests.md)
