# SimpleCharacterBuilder

[![CI](https://github.com/gxogdnd/SimpleCharacterBuilder/actions/workflows/ci.yml/badge.svg)](https://github.com/gxogdnd/SimpleCharacterBuilder/actions/workflows/ci.yml)

A small command-line tool for building **Dungeons & Dragons 5e** character
sheets — and, just as importantly, a **hands-on learning project** for people
who are new to Python and to contributing on GitHub.

The app is deliberately simple. The real goal is to give you a safe, friendly
place to practise the whole real-world workflow: pick up an issue, create a
branch, write some Python, add tests, update the docs, open a pull request, go
through review, and get it merged.

> New to all of this? Start with **[CONTRIBUTING.md](CONTRIBUTING.md)** and the
> guided **[learning path](docs/learning-path/)**. You do not need to know D&D —
> read the short **[rules primer](docs/dnd-rules.md)** if a term is unfamiliar.

## What it does (so far)

The friendliest way in is the interactive menu — run `charsheet menu` and pick
an action by number (create, show, browse races/classes/skills); it loops until
you quit.

Or jump straight to the interactive builder, which asks one question at a time
and lets you pick a race and class from the SRD lists:

```console
$ charsheet new
Let's build a character. Press Enter to accept each [default].

Name: Bruenor
Race (Dragonborn, Dwarf, Elf, ...) [Human]: Dwarf
Class (Barbarian, Bard, ...) [Fighter]: Fighter
Level [1]: 1

Ability scores (1-30):
  Strength [10]: 16
  ...
```

Prefer a one-liner? The same thing with flags (handy for scripts):

```console
$ charsheet create --name "Bruenor" --race Dwarf --class Fighter --strength 16 --constitution 15
Created Bruenor and saved to bruenor.character.json

$ charsheet show bruenor.character.json
Bruenor
Level 1 Dwarf Fighter

Ability Scores
--------------
STR  16  (+3)
DEX  10  (+0)
CON  15  (+2)
INT  10  (+0)
WIS  10  (+0)
CHA  10  (+0)
```

Run `charsheet create --help` to see every option.

You can also browse the bundled 5e SRD reference data:

```console
$ charsheet races      # e.g. "Dwarf — CON +2"
$ charsheet classes    # e.g. "Wizard (d6) — saves: INT, WIS"
$ charsheet skills     # e.g. "Stealth (DEX)"
```

More — proficiency bonus, hit points, skill bonuses, validated SRD
races/classes, leveling up, and eventually the full 5e SRD — is built up one
issue at a time. That backlog *is* the curriculum.

## Quickstart

You'll need **Python 3.10+** and **git**.

```bash
# 1. Get the code (after forking, use your own fork's URL)
git clone https://github.com/gxogdnd/SimpleCharacterBuilder.git
cd SimpleCharacterBuilder

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install the app plus the development tools, in editable mode
pip install -e ".[dev]"

# 4. Check it works
charsheet --version
```

## Developing

```bash
pytest                 # run the tests
ruff check .           # lint
ruff format .          # auto-format your code
```

The same checks run automatically on every pull request via GitHub Actions.

Maintainers: see **[RELEASING.md](RELEASING.md)** for how to cut a release.

## License

[MIT](LICENSE) © 2026 MuckGX

## Attribution

This project includes material from the **System Reference Document 5.1**
("SRD 5.1") by Wizards of the Coast LLC, available under the
[Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/legalcode).
The SRD content (the data in `src/charsheet/data/`) is owned by Wizards of the
Coast and used under that licence; it is not covered by this project's MIT
licence. See the [rules primer](docs/dnd-rules.md) for more.
