**Difficulty:** 🔴 enhancement

## What

Let a character be **proficient** in some skills, and compute each skill's bonus.
A skill bonus is the governing ability's modifier, plus the proficiency bonus if
the character is proficient in that skill.

```
Stealth (DEX): +5    # DEX modifier +3, proficient, +2 proficiency
Arcana (INT): +1     # INT modifier +1, not proficient
```

## Why

This ties together three things you may have built already — ability modifiers,
the proficiency bonus, and the skills reference data — into a real, visible
feature. It's the natural "capstone" enhancement.

## Acceptance criteria

- [ ] A character can store which skills they're proficient in (and it
      saves/loads).
- [ ] A function computes a skill's bonus from the ability modifier and, if
      proficient, the proficiency bonus.
- [ ] The CLI can display skills with their bonuses (e.g. a `skills` option on
      `show`, or a new command — your choice; document it).
- [ ] Tests cover a proficient and a non-proficient skill.

## Where to look

- `src/charsheet/data/skills.json` and `reference.load_skills()` — skill → ability.
- `src/charsheet/models.py` — add proficiency storage to `Character`
  (remember `to_dict`/`from_dict`).
- `src/charsheet/rules.py` — the bonus calculation (keep it pure).
- `src/charsheet/cli.py` and `tests/`.

## Notes for a bigger change

This touches the data model, so plan the JSON shape first and mention it on the
issue. Adding a field to `Character` means updating `to_dict`/`from_dict` and
their tests. Consider splitting into two PRs: (1) store proficiencies, (2)
compute and display bonuses.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
