# 2. Understanding the project

**You'll learn:** how the code is organised, so you know where to make a change.

You don't need to understand every line. The goal is a mental map.

## The shape of the repository

```
SimpleCharacterBuilder/
├── src/charsheet/        ← the app's code
│   ├── cli.py            ← the command-line commands (create, show, races, ...)
│   ├── models.py         ← the Character and AbilityScores data classes
│   ├── rules.py          ← pure D&D rules (e.g. ability_modifier)
│   ├── storage.py        ← saving/loading characters as JSON
│   ├── reference.py      ← loads the SRD data files
│   └── data/             ← SRD content as JSON (races, classes, skills)
├── tests/                ← one test file per source file
├── docs/                 ← these guides and the rules primer
└── pyproject.toml        ← project + tool configuration
```

## How a command flows

When you run `charsheet show hero.json`:

1. `cli.py` receives the command and the file path.
2. `storage.py` reads the JSON and builds a `Character` (`models.py`).
3. `cli.py` prints it, asking `rules.py` to turn ability scores into modifiers.

Notice the **separation**: rules don't know about files, files don't know about
the command line. That makes each piece easy to read and to test on its own.

## Run the app to explore

```bash
charsheet create --name "Aria" --race Elf --class Wizard --intelligence 16
charsheet show aria.character.json
charsheet races
charsheet classes
charsheet skills
```

## Read a test

Open `tests/test_rules.py`. See how each test gives a function an input and
checks the output? That's the pattern you'll copy later.

## New to D&D?

Read the short [rules primer](../dnd-rules.md). You only need the basics.

➡️ Next: [Claiming your first issue](03-finding-an-issue.md)
