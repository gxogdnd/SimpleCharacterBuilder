# 7. Opening a pull request

**You'll learn:** how to share your branch as a pull request that's easy to
review.

## What is a pull request?

A **pull request** (PR) is a proposal: "please pull my branch's changes into
`main`." It's where review and discussion happen before anything is merged.

## Push your branch

First, send your branch up to your fork:

```bash
git push origin feature/short-description
```

git will print a link you can click to start the PR, or you can open it from the
GitHub website.

## Fill in the template

This project provides a PR template — please fill it in. A good PR description:

- **says what the change does** in a sentence or two,
- **links the issue** with `Closes #123` (GitHub then closes the issue when the
  PR merges),
- **explains how you tested it**,
- **ticks the checklist** (tests, ruff, docs).

## Keep it small and self-contained

One issue → one PR. A small PR gets reviewed faster and merged sooner. If you
notice unrelated things to fix, open separate issues for them.

## After you open it

- CI runs automatically — see [guide 6](06-linting-and-ci.md). Get it green.
- A maintainer will be notified to review.
- You can keep pushing commits to the same branch; the PR updates itself.

## Draft PRs

Not finished but want early feedback? Open it as a **draft** PR (an option in
the green button). It signals "not ready to merge yet, but take a look."

➡️ Next: [Working through review](08-code-review.md)
