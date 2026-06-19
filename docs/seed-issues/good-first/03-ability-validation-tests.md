**Difficulty:** 🟢 good first issue

## What

The `AbilityScores` class already rejects invalid scores, but a few cases aren't
covered by tests yet. Add tests for them — **no application code needs to
change**.

## Why

Writing tests for code that already works is the safest possible way to learn
pytest. You can't break anything, and you make the project more robust.

## Acceptance criteria

- [ ] A test confirms a score below the minimum (e.g. `0`) raises `ValueError`.
- [ ] A test confirms the boundary values `1` and `30` are accepted.
- [ ] A test confirms a non-integer score (e.g. `"twelve"`) raises `TypeError`.
- [ ] `pytest` passes.

## Where to look

- `src/charsheet/models.py` — see `AbilityScores.__post_init__` for the rules
  you're testing.
- `tests/test_models.py` — add your tests here.

## Hints

- Use `pytest.raises`:
  ```python
  import pytest
  with pytest.raises(ValueError):
      AbilityScores(strength=0)
  ```

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
