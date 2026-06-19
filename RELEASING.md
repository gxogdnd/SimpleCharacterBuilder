# Releasing

This guide explains how to cut a new release of SimpleCharacterBuilder. It's
written to be followed step by step — making a release is itself a good way to
practise the full workflow.

Only maintainers (people with write access) can publish a release, but anyone is
welcome to read along or open the version-bump pull request.

## How we version

We follow [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

- **PATCH** (`0.1.0` → `0.1.1`) — backwards-compatible bug fixes.
- **MINOR** (`0.1.0` → `0.2.0`) — new features that don't break existing usage.
- **MAJOR** (`0.1.0` → `1.0.0`) — changes that break existing usage.

While the project is pre-`1.0.0`, treat it as early days: minor versions may
still change things, and that's expected.

## Where the version lives

The version is recorded in **two** places, and they must match:

1. `pyproject.toml` — the `version = "..."` line under `[project]`.
2. `src/charsheet/__init__.py` — the `__version__ = "..."` line.

(`charsheet --version` reads the second one.)

## Step 1 — Bump the version (via a pull request)

`main` is protected, so the bump goes through a normal PR like any other change.

```bash
git checkout main
git pull origin main
git checkout -b release/v0.2.0      # use your new version
```

Edit both files above to the new version, then:

```bash
# Sanity check: both should print the new version
grep '^version' pyproject.toml
python -c "import charsheet; print(charsheet.__version__)"

# Make sure everything is green
ruff format . && ruff check . && pytest
```

Commit, push, and open a PR titled e.g. `Release v0.2.0`:

```bash
git commit -am "Bump version to 0.2.0"
git push origin release/v0.2.0
gh pr create --fill
```

Wait for CI to pass, then merge the PR (CI must be green — that's enforced).

## Step 2 — Tag and publish the release

After the bump is merged, update your local `main` and create the GitHub release.
Creating the release also creates the matching git tag.

```bash
git checkout main
git pull origin main

gh release create v0.2.0 \
  --target main \
  --title "v0.2.0" \
  --notes "Summary of what changed in this release." \
  --latest
```

Tips for the notes:

- Summarise user-facing changes, grouped if there are many.
- `gh release create v0.2.0 --generate-notes` will draft notes from merged PRs,
  which you can then edit.

## Step 3 — Verify

```bash
gh release view v0.2.0
git fetch --tags && git tag -l
```

Check the release page looks right and is marked **Latest**.

## Release checklist

- [ ] Version bumped in `pyproject.toml` **and** `src/charsheet/__init__.py` (they match)
- [ ] `ruff check .` and `pytest` pass
- [ ] Version-bump PR merged with green CI
- [ ] `git tag` chosen as `vMAJOR.MINOR.PATCH` (note the leading `v`)
- [ ] Release created with clear notes and marked latest
- [ ] Release page verified
