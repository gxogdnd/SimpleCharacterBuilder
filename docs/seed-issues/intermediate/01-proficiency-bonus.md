**Difficulty:** 🟡 intermediate

## What

Add a pure function `proficiency_bonus(level)` to `rules.py`. In 5e the
proficiency bonus depends only on character level:

| Levels | Bonus |
| ------ | ----- |
| 1–4    | +2    |
| 5–8    | +3    |
| 9–12   | +4    |
| 13–16  | +5    |
| 17–20  | +6    |

## Why

This is a core rule that several other features (skills, saving throws, hit
chances) build on. It's a clean, well-defined function — perfect for practising
test-driven development.

## Acceptance criteria

- [ ] `rules.proficiency_bonus(level)` returns the correct bonus for levels 1–20.
- [ ] It's a pure function (no printing, no file access).
- [ ] Tests in `tests/test_rules.py` cover each band and the boundaries
      (e.g. 4 → +2, 5 → +3).

## Where to look

- `src/charsheet/rules.py` — add the function next to `ability_modifier`.
- `tests/test_rules.py` — parametrise the test like the existing modifier test.

## Hints

- A tidy formula: `2 + (level - 1) // 4`.
- Consider what should happen for an invalid level (e.g. `0`). Raising
  `ValueError` is reasonable — decide, then test it.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
