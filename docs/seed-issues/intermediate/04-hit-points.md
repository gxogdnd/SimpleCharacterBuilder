**Difficulty:** 🟡 intermediate

## What

Calculate and display a character's **hit points at level 1**. In 5e, a level-1
character's maximum HP is the highest roll of their class's hit die plus their
Constitution modifier:

```
HP = hit_die_max + constitution_modifier
```

For example, a Fighter (d10) with Constitution 14 (+2) has `10 + 2 = 12` HP.

## Why

This is the first feature that combines three parts of the project — a class's
data, an ability modifier, and the character — so it's a great step up from the
single-file changes.

## Acceptance criteria

- [ ] A function computes level-1 max HP from a character's class and
      Constitution.
- [ ] `charsheet show <file>` displays the HP.
- [ ] Tests cover at least two classes with different hit dice and CON values.
- [ ] An unknown class is handled sensibly (decide how, and test it).

## Where to look

- `src/charsheet/reference.py` — `load_classes()` gives each class's `hit_die`.
- `src/charsheet/rules.py` — a good home for the HP calculation (keep it pure).
- `src/charsheet/cli.py` — display it in `_print_character`.
- `tests/` — add tests near the layer you change.

## Hints

- The max of a die `dN` is just `N` (the `hit_die` value in the data).
- The Constitution modifier is `character.abilities.modifier("constitution")`.
- Look the class up by name in `load_classes()`.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
