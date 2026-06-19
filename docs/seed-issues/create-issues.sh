#!/usr/bin/env bash
#
# Create the seed-issue backlog on GitHub.
#
# Usage (from anywhere):
#   bash docs/seed-issues/create-issues.sh
#
# Requires the GitHub CLI (`gh`) authenticated as an account with write access
# to this repository. Check first with: gh auth status
#
# WARNING: running this more than once creates DUPLICATE issues. Run it once.

set -euo pipefail

# Resolve the directory this script lives in, so the body files are found
# regardless of where you run it from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if ! command -v gh >/dev/null 2>&1; then
  echo "error: the GitHub CLI (gh) is not installed. See https://cli.github.com/" >&2
  exit 1
fi

echo "Acting as:"
gh auth status 2>&1 | sed 's/^/  /' || true
echo

# Create custom labels if they don't already exist (the built-in 'good first
# issue', 'enhancement', and 'documentation' labels usually exist by default).
ensure_label() {
  local name="$1" color="$2" description="$3"
  gh label create "$name" --color "$color" --description "$description" 2>/dev/null \
    && echo "created label: $name" \
    || echo "label exists:  $name"
}

ensure_label "intermediate" "fbca04" "A step up from a good first issue"
ensure_label "documentation" "0075ca" "Improvements or additions to documentation"
echo

# Each entry: "Title|labels (comma-separated)|body file relative to SCRIPT_DIR"
issues=(
  "Add a --quiet flag to the create command|good first issue|good-first/01-quiet-flag.md"
  "Show the total of all ability scores in show|good first issue|good-first/02-ability-total.md"
  "Add tests for AbilityScores validation|good first issue|good-first/03-ability-validation-tests.md"
  "Add a README example with a negative modifier|good first issue,documentation|good-first/04-readme-negative-modifier.md"
  "Implement proficiency_bonus(level)|intermediate|intermediate/01-proficiency-bonus.md"
  "Show the proficiency bonus in show|intermediate|intermediate/02-show-proficiency-bonus.md"
  "Validate --race and --class against the SRD|intermediate|intermediate/03-validate-race-class.md"
  "Calculate level-1 hit points|intermediate|intermediate/04-hit-points.md"
  "Add a level-up command|enhancement|enhancement/01-level-up.md"
  "Add an export command (Markdown)|enhancement|enhancement/02-export-markdown.md"
  "Add skill proficiencies and bonuses|enhancement|enhancement/03-skill-bonuses.md"
  "Add an inventory to characters|enhancement|enhancement/04-inventory.md"
)

for entry in "${issues[@]}"; do
  IFS='|' read -r title labels body <<<"$entry"
  echo "Creating: $title"
  gh issue create \
    --title "$title" \
    --label "$labels" \
    --body-file "$SCRIPT_DIR/$body"
done

echo
echo "Done. View them with: gh issue list"
