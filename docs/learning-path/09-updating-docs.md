# 9. Updating documentation

**You'll learn:** when and how to update docs so they stay true to the code.

## Why it matters

Out-of-date docs are worse than no docs — they actively mislead. If your change
affects how someone *uses* or *builds* the project, the docs need to keep up. It
is part of the change, not an afterthought.

## What counts as "the docs" here

- **`README.md`** — the front page: what the app does and how to run it.
- **`docs/dnd-rules.md`** — the rules primer, if you add a new rule or data type.
- **These learning-path guides** — if you change a step in the workflow.
- **Docstrings and comments** — the explanations right next to the code.
- **`--help` text** — for the CLI, the `help=` strings in `cli.py` *are* docs.

## A quick checklist

When you finish a change, ask:

- Did I add or change a **command or option**? → update the README usage and the
  command's `help=` text.
- Did I add a new kind of **data** (a field in `data/*.json`)? → mention it in
  the rules primer.
- Did I change **how to set up or run** the project? → update the README
  quickstart.
- Could a newcomer follow the docs and get the result I just saw? If not, fix the
  docs.

## Keep examples real

If you add an example command to the README, actually run it and paste the real
output. Readers will copy it, so it must work.

## Small is fine

A one-line docs fix is a perfectly good contribution — in fact, fixing a typo or
a confusing sentence is a great first PR.

➡️ Next: [Tackling an enhancement](10-tackling-an-enhancement.md)
