**Difficulty:** 🟡 intermediate

## What

Display the character's proficiency bonus in the `show` command's output, e.g.:

```
Level 5 Dwarf Fighter
Proficiency bonus: +3
```

**Depends on:** "Implement `proficiency_bonus(level)`" — do that one first (or
coordinate on the issue).

## Why

Turns the `proficiency_bonus` rule into something a user can actually see, and
teaches how the CLI layer uses the rules layer.

## Acceptance criteria

- [ ] `charsheet show <file>` prints the proficiency bonus, with a sign (`+3`).
- [ ] The value matches `rules.proficiency_bonus(character.level)`.
- [ ] A test asserts the line appears for a known level.

## Where to look

- `src/charsheet/cli.py` — the `_print_character` helper.
- `src/charsheet/rules.py` — `proficiency_bonus`.
- `tests/test_cli.py`.

## Hints

- A character's level is `character.level`.
- The `show` code already formats a sign for modifiers — reuse that idea.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
