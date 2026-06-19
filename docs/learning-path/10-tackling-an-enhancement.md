# 10. Tackling an enhancement

**You'll learn:** how to approach a larger change that touches several files —
the kind labelled `enhancement` rather than `good first issue`.

By now you've done the full loop on a small change. An enhancement is the same
loop, just bigger. The skill that matters most is **breaking it down**.

## A worked example

Take a realistic issue: **"Add a proficiency bonus to the character sheet."**
In 5e, the bonus depends on level (+2 at levels 1–4, +3 at 5–8, …).

Here's how you might break it apart, following the project's own separation of
concerns:

1. **The rule** — add `proficiency_bonus(level)` to `rules.py`. Pure function,
   easy to test.
2. **Test the rule** — add cases to `tests/test_rules.py` (level 1 → +2, level 5
   → +3, an edge like level 20).
3. **Use it** — show the bonus in `cli.py`'s `show` output.
4. **Test the display** — extend `tests/test_cli.py` to assert it appears.
5. **Document it** — note it in the README and the rules primer.

Notice each step is itself a small, testable change — much like the
`good first issue`s you've already done, stacked together.

## Tips for bigger changes

- **Make a plan in the issue first.** List the steps (like above) as a comment.
  The reviewer can sanity-check your approach *before* you write code — far
  cheaper than reworking it later.
- **Commit step by step.** Separate commits ("add the rule", "show it in the
  CLI", "update docs") make the change easy to follow and to review.
- **Lean on the existing patterns.** Almost everything you need has a smaller
  example already in the codebase. Find it and follow it.
- **If it's getting huge, split it.** Two focused PRs beat one sprawling one. It
  is fine to propose this on the issue.

## You're contributing for real now

Everything past here is practice and repetition. The loop —
issue → branch → code + tests + docs → PR → review → merge — is the same one
used on projects of every size. You've learned it by doing it.

Welcome to open source. 🎲

⬅️ Back to [the learning path index](README.md)
