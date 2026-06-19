# 5. Writing tests with pytest

**You'll learn:** how to prove your change works with an automated test — and
why that matters.

## Why tests?

A test is a small piece of code that checks your code does what you expect. They
let us change things later **without fear**: if something breaks, a test goes
red and tells us exactly what and where. Every change with logic needs a test.

## The shape of a test

We use [pytest](https://docs.pytest.org/). A test is just a function whose name
starts with `test_`, containing an `assert`:

```python
from charsheet import rules


def test_ability_modifier_for_an_average_score():
    assert rules.ability_modifier(10) == 0
```

Run the whole suite from the project root:

```bash
pytest
```

`pytest` finds every `test_*` function under `tests/` automatically.

## Where to put your test

Tests mirror the source: code in `rules.py` is tested in `tests/test_rules.py`,
`models.py` in `tests/test_models.py`, and so on. Add your test to the matching
file (or create it if it's a new module).

## Test the behaviour, not the wiring

Aim a test at *what the code should do*:

- a normal case (a typical input),
- an edge case (zero, negative, empty, the smallest/largest allowed value),
- an error case (does it reject bad input?).

Two patterns already used in this project are worth copying:

- **Parametrising** many inputs at once — see `tests/test_rules.py`.
- **Testing the CLI** with click's `CliRunner` — see `tests/test_cli.py`.

## Watch it fail first

A quick trick: make your test expect the *right* answer before you write the
code, run it, and watch it fail. Then write the code and watch it pass. Now you
know the test actually checks something.

➡️ Next: [Linting, formatting, and CI](06-linting-and-ci.md)
