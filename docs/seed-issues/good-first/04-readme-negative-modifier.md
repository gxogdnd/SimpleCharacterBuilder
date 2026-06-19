**Difficulty:** 🟢 good first issue

## What

The README's example only shows positive and zero modifiers. Add a short
example (or extend the existing one) that includes a **negative** modifier, so
readers see how low scores look — e.g. a Strength of 7 showing `(-2)`.

## Why

A documentation-only first contribution: no code, no tests, just making the docs
clearer. Great for learning the fork → branch → PR loop without touching Python.

## Acceptance criteria

- [ ] The README shows example output containing a negative modifier.
- [ ] The example matches what the app actually prints (run it and copy the real
      output).

## Where to look

- `README.md` — the "What it does (so far)" section.

## Hints

- Generate real output to copy:
  ```bash
  charsheet create --name "Weakling" --strength 7 -o /tmp/w.json
  charsheet show /tmp/w.json
  ```
- Keep the example short; you don't need to show all six abilities.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
