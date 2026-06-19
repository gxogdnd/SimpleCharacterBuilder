**Difficulty:** 🔴 enhancement

## What

Give characters an **inventory** — a list of items they carry — with commands to
add, remove, and list items:

```console
$ charsheet item-add bruenor.character.json "Warhammer"
$ charsheet item-add bruenor.character.json "Healing potion"
$ charsheet items bruenor.character.json
- Warhammer
- Healing potion
```

(Exact command names are up to you — pick clear ones and document them.)

## Why

A self-contained feature that exercises the full stack: changing the data model,
saving/loading the new field, and adding more than one command. Good practice at
designing a small feature end to end.

## Acceptance criteria

- [ ] A character stores a list of item names that saves and loads correctly.
- [ ] Items can be added and removed via the CLI.
- [ ] The inventory can be listed (and `show` may include it — your choice).
- [ ] Removing a non-existent item gives a friendly message, not a crash.
- [ ] Tests cover add, remove, and the save/load round-trip.

## Where to look

- `src/charsheet/models.py` — add an `items` field to `Character` (and update
  `to_dict`/`from_dict`).
- `src/charsheet/cli.py` — the new commands.
- `src/charsheet/storage.py` — already handles saving/loading once the model
  knows about items.
- `tests/`.

## Notes for a bigger change

Plan the data shape and the command names on the issue first. Use
`field(default_factory=list)` so existing character files without an `items`
key still load. Keep each command's PR focused; you can land "add/list" first
and "remove" second.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
