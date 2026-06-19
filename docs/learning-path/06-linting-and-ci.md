# 6. Linting, formatting, and CI

**You'll learn:** how to keep your code tidy with ruff, and what the automated
checks on your pull request mean.

## Formatting: stop arguing about style

**Formatting** is about how code *looks* — spaces, line breaks, quotes. We let a
tool handle it so nobody has to think about it. We use
[ruff](https://docs.astral.sh/ruff/):

```bash
ruff format .
```

This rewrites your files into the project's standard style. Run it before you
commit.

## Linting: catch likely mistakes

**Linting** looks for *likely problems* — an unused import, a variable you
defined but never used, a common bug pattern:

```bash
ruff check .
```

If it reports something, read the message: it names the file, the line, and a
rule code. Many issues can be fixed automatically:

```bash
ruff check . --fix
```

## CI: the checks that run on your PR

**CI** (Continuous Integration) is automation that runs *the same checks* on
GitHub every time you push to a pull request. For this project, CI runs `ruff`
and `pytest` on several Python versions (see `.github/workflows/ci.yml`).

On your PR you'll see either:

- ✅ a green check — everything passed, or
- ❌ a red X — something failed.

## When CI is red

Don't panic — this is normal and fixable.

1. Click **Details** next to the failed check to see the log.
2. Find the error (a failing test, or a ruff complaint).
3. Reproduce it locally with `pytest` or `ruff check .`.
4. Fix it, commit, and push again. CI re-runs automatically.

The goal before asking for review: **green CI locally and on the PR**. Run this
trio before you push:

```bash
ruff format .
ruff check .
pytest
```

➡️ Next: [Opening a pull request](07-opening-a-pr.md)
