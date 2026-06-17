# SimpleCharacterBuilder

A small command-line tool for building **Dungeons & Dragons 5e** character
sheets — and, just as importantly, a **hands-on learning project** for people
who are new to Python and to contributing on GitHub.

The app is deliberately simple. The real goal is to give you a safe, friendly
place to practise the whole real-world workflow: pick up an issue, create a
branch, write some Python, add tests, update the docs, open a pull request, go
through review, and get it merged.

> New to all of this? Start with **[CONTRIBUTING.md](CONTRIBUTING.md)** and the
> guided **[learning path](docs/learning-path/)**. You do not need to know D&D —
> a rules primer will live in `docs/dnd-rules.md`.

## What it does (so far)

This is an early scaffold. Today the CLI only reports its version:

```console
$ charsheet --version
charsheet, version 0.1.0
```

Everything else — ability scores, races, classes, skills, saving/loading a
character, and eventually the full 5e SRD — is built up one issue at a time.
That backlog *is* the curriculum.

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

## License

[MIT](LICENSE) © 2026 MuckGX
