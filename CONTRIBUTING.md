# Contributing to SimpleCharacterBuilder

Welcome! This project exists to help you **learn the real contribution
workflow** by doing it for real, on a small and friendly codebase. Take your
time, and don't worry about making mistakes — that's what the review step is
for.

This guide is the spine. When you hit a step for the first time, there's a
matching, more detailed walkthrough in [`docs/learning-path/`](docs/learning-path/).

## The big picture

Every change — yours and everyone else's — travels the same loop:

```
issue  →  branch  →  code + tests + docs  →  pull request  →  review  →  merge
```

We follow this loop even for the project's own setup work, so you can read the
history and see it in action.

## One-time setup

1. **Make a GitHub account** if you don't have one, and install
   [git](https://git-scm.com/downloads).
2. **Fork** this repository (the *Fork* button, top-right on GitHub). This gives
   you your own copy to push to.
3. **Clone your fork** and install the project:

   ```bash
   git clone https://github.com/<your-username>/SimpleCharacterBuilder.git
   cd SimpleCharacterBuilder
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   pip install -e ".[dev]"
   ```

4. **Add the original repo as `upstream`** so you can stay in sync:

   ```bash
   git remote add upstream https://github.com/gxogdnd/SimpleCharacterBuilder.git
   ```

## Making a change

1. **Pick an issue.** Browse the [issues](https://github.com/gxogdnd/SimpleCharacterBuilder/issues).
   New here? Filter for the `good first issue` label. Comment on the issue to
   say you're taking it.

2. **Sync and branch.** Start from an up-to-date `main`, then create a branch
   named for your work:

   ```bash
   git checkout main
   git pull upstream main
   git checkout -b feature/short-description   # e.g. feature/add-ability-modifiers
   ```

3. **Write the code.** Keep it small and readable — match the style around you.

4. **Write or update tests.** Anything with logic needs a test. Run them:

   ```bash
   pytest
   ```

5. **Lint and format.** We use [ruff](https://docs.astral.sh/ruff/):

   ```bash
   ruff check .       # find problems
   ruff format .      # fix formatting
   ```

6. **Update the docs** if your change affects how the app is used or built.

7. **Commit** in small, clear steps:

   ```bash
   git add -A
   git commit -m "Add ability score modifiers"
   ```

   Write commit messages in the imperative mood ("Add ...", "Fix ...") and
   explain *why* in the body if it isn't obvious.

8. **Push** to your fork and **open a pull request**:

   ```bash
   git push origin feature/short-description
   ```

   Then open the PR on GitHub. Fill in the template, and use
   `Closes #<issue-number>` so the issue closes automatically on merge.

## After you open the PR

- **CI runs automatically.** Watch the checks at the bottom of the PR. If ruff
  or pytest fail, click in to read why, push fixes to the same branch, and the
  checks re-run.
- **A maintainer reviews it.** They may ask questions or request changes — this
  is normal and how we all learn. Reply, push more commits, and the PR updates.
- **Merge.** Once it's approved and green, it gets merged. 🎉 You've contributed!

## Ground rules

- Be kind and patient — see the [Code of Conduct](CODE_OF_CONDUCT.md).
- One focused change per pull request.
- Ask questions freely. "I don't understand X" is always a welcome comment.

Thank you for contributing, and welcome to open source.
