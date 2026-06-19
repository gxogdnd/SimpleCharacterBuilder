**Difficulty:** 🔴 enhancement

## What

Add a `level-up` command that increases a saved character's level by one and
writes the change back to their file:

```console
$ charsheet level-up bruenor.character.json
Bruenor is now level 2.
```

## Why

It's the first command that **loads, modifies, and re-saves** a character, which
is a very common shape for real features. It also naturally interacts with any
level-based stats (like proficiency bonus or HP) once those exist.

## Acceptance criteria

- [ ] `charsheet level-up <file>` increments the character's level by 1 and saves.
- [ ] The new level is reported to the user.
- [ ] Running it again continues to increment (2 → 3 → ...).
- [ ] There's a sensible cap or behaviour at level 20 (decide and document it).
- [ ] Tests cover a level-up and the save round-trip.

## Where to look

- `src/charsheet/cli.py` — add the command next to `show`.
- `src/charsheet/storage.py` — `load_character` / `save_character`.
- `tests/test_cli.py`.

## Hints

- Load, change `character.level`, then save back to the same path.
- The `Character` model already validates that level is at least 1.

## Notes for a bigger change

Plan it in a comment first (load → modify → save → report). Keep the commits
small. If you also want to recompute derived stats on level-up, consider doing
that as a follow-up issue rather than growing this PR.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
