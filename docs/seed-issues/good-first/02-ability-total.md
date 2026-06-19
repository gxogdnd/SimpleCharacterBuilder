**Difficulty:** 🟢 good first issue

## What

At the bottom of the `show` command's output, print the **total** of all six
ability scores, for example:

```
Total ability score points: 78
```

## Why

A small, friendly first change that touches one function and one test, while
being a genuinely handy number for comparing characters.

## Acceptance criteria

- [ ] `charsheet show <file>` prints a line with the sum of the six ability
      scores after the existing list.
- [ ] A test asserts the total line appears with the correct number.

## Where to look

- `src/charsheet/cli.py` — the `_print_character` helper.
- `src/charsheet/rules.py` — `ABILITIES` is the list of the six ability names.
- `tests/test_cli.py` — extend the `show` test.

## Hints

- `sum(getattr(character.abilities, a) for a in rules.ABILITIES)` gives the total.
- Six scores of 10 each total 60, which is an easy case to test.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
