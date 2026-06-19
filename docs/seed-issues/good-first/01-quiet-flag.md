**Difficulty:** 🟢 good first issue

## What

Add a `--quiet` / `-q` flag to the `create` command. When given, `create`
should still save the character file but print nothing on success.

## Why

It's a small, self-contained way to learn how command-line options work in this
project, and quiet mode is genuinely useful when scripting.

## Acceptance criteria

- [ ] `charsheet create --name "Hero" --quiet` creates the file but prints no
      success message.
- [ ] Without `--quiet`, the existing `Created ...` message still prints.
- [ ] A test covers both the quiet and non-quiet cases.

## Where to look

- `src/charsheet/cli.py` — the `create` command and its options.
- `tests/test_cli.py` — copy the shape of the existing `create` tests.

## Hints

- `click.option("--quiet", "-q", is_flag=True)` gives you a boolean flag.
- The `CliRunner` test helper captures `result.output`; assert it's empty in
  quiet mode.

## New here?

Read `CONTRIBUTING.md` and the guides in `docs/learning-path/`. Comment below to
claim this issue before you start.
