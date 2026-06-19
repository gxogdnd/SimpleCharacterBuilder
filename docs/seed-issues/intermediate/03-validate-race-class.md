**Difficulty:** 🟡 intermediate

## What

When creating a character, validate that the given `--race` and `--class` exist
in the SRD reference data. If not, fail with a clear, friendly error that lists
the valid options.

## Why

Right now you can create a "Wizardd" or a "Humann" by mistake. Validating against
the real data catches typos early and teaches you how to use the `reference`
module.

## Acceptance criteria

- [ ] Creating a character with an unknown race or class exits with a non-zero
      status and a helpful message naming the bad value.
- [ ] The valid options are sourced from `reference.load_races()` /
      `reference.load_classes()` (not hard-coded).
- [ ] Matching is case-insensitive (`dwarf` == `Dwarf`).
- [ ] Tests cover a valid case and an invalid case.

## Where to look

- `src/charsheet/cli.py` — the `create` command.
- `src/charsheet/reference.py` — loaders for races and classes.
- `tests/test_cli.py`.

## Hints

- Build the set of valid names once: `{r["name"].lower() for r in reference.load_races()}`.
- `raise click.BadParameter("...")` produces a clean CLI error with the right
  exit code.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
