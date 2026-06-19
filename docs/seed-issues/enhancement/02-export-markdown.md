**Difficulty:** 🔴 enhancement

## What

Add an `export` command that writes a character out as a nicely formatted
**Markdown** file, suitable for sharing or printing:

```console
$ charsheet export bruenor.character.json --output bruenor.md
Exported Bruenor to bruenor.md
```

## Why

It separates *computing* a sheet from *rendering* it in a particular format —
an important design idea. It's also immediately useful for players who want a
readable sheet.

## Acceptance criteria

- [ ] `charsheet export <file> --output <file.md>` writes valid Markdown.
- [ ] The Markdown includes the name, race, class, level, and an ability-score
      table with modifiers.
- [ ] If `--output` is omitted, it defaults to `<name>.md`.
- [ ] A test checks the exported file contains the expected headings/values.

## Where to look

- `src/charsheet/cli.py` — add the `export` command.
- Consider a small `export.py` (or a function) that turns a `Character` into a
  Markdown string, so it can be tested without touching files.
- `tests/`.

## Hints

- Build the Markdown as a string, then write it with `Path.write_text`.
- A Markdown table row looks like `| STR | 16 | +3 |`.
- Reuse `character.abilities.modifier(...)` for the modifiers.

## Notes for a bigger change

Keep the *rendering* (Character → string) separate from the *file writing*. The
string part is easy to unit-test; the command just calls it and saves.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
