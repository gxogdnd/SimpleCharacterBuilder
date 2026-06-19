# Seed issues

This folder holds a ready-made backlog of starter work. It exists so the
project always has well-described tasks for new contributors to learn on — the
backlog *is* the curriculum.

Each file contains the **body** of one issue. To use them:

- **By hand:** open a file, copy its contents into a new GitHub issue, and use
  the title from the table below.
- **All at once:** run [`create-issues.sh`](create-issues.sh) (see the bottom of
  this page).

Difficulty tiers:

- 🟢 **good first issue** — small and self-contained; ideal for a first PR.
- 🟡 **intermediate** — a bit of logic across one or two files.
- 🔴 **enhancement** — a larger, multi-file feature.

## The backlog

| Title | Tier | Labels | File |
|-------|------|--------|------|
| Add a `--quiet` flag to the `create` command | 🟢 | `good first issue` | [good-first/01-quiet-flag.md](good-first/01-quiet-flag.md) |
| Show the total of all ability scores in `show` | 🟢 | `good first issue` | [good-first/02-ability-total.md](good-first/02-ability-total.md) |
| Add tests for `AbilityScores` validation | 🟢 | `good first issue` | [good-first/03-ability-validation-tests.md](good-first/03-ability-validation-tests.md) |
| Add a README example with a negative modifier | 🟢 | `good first issue`, `documentation` | [good-first/04-readme-negative-modifier.md](good-first/04-readme-negative-modifier.md) |
| Implement `proficiency_bonus(level)` | 🟡 | `intermediate` | [intermediate/01-proficiency-bonus.md](intermediate/01-proficiency-bonus.md) |
| Show the proficiency bonus in `show` | 🟡 | `intermediate` | [intermediate/02-show-proficiency-bonus.md](intermediate/02-show-proficiency-bonus.md) |
| Validate `--race` and `--class` against the SRD | 🟡 | `intermediate` | [intermediate/03-validate-race-class.md](intermediate/03-validate-race-class.md) |
| Calculate level-1 hit points | 🟡 | `intermediate` | [intermediate/04-hit-points.md](intermediate/04-hit-points.md) |
| Add a `level-up` command | 🔴 | `enhancement` | [enhancement/01-level-up.md](enhancement/01-level-up.md) |
| Add an `export` command (Markdown) | 🔴 | `enhancement` | [enhancement/02-export-markdown.md](enhancement/02-export-markdown.md) |
| Add skill proficiencies and bonuses | 🔴 | `enhancement` | [enhancement/03-skill-bonuses.md](enhancement/03-skill-bonuses.md) |
| Add an inventory to characters | 🔴 | `enhancement` | [enhancement/04-inventory.md](enhancement/04-inventory.md) |

## Posting them to GitHub

From the repository root, with `gh` authenticated as the repo owner:

```bash
# Check you're acting as the right account first
gh auth status

# Create the labels and all the issues
bash docs/seed-issues/create-issues.sh
```

The script creates a couple of custom labels (`intermediate`, `documentation`)
if they don't exist, then opens every issue above. Running it more than once
will create duplicate issues, so run it just the once.
