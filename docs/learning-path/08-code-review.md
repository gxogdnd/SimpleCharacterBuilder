# 8. Working through review

**You'll learn:** how code review works and how to respond to feedback calmly
and productively.

## Review is normal — and a gift

Almost every PR, from everyone, gets review comments. Feedback is about the
*code*, not about *you*. A reviewer spending time on your change is a good sign:
they're helping it (and you) get better.

## Kinds of comments

- **Required changes** — something must change before merging (a bug, a missing
  test). Often left as a formal "Request changes".
- **Suggestions** — "consider…", "what about…". Worth weighing; you can discuss.
- **Questions** — the reviewer wants to understand your reasoning. Just answer.
- **Nitpicks** — small style points, often labelled "nit:". Quick to apply.

## How to respond

1. **Read it all first** before changing anything.
2. **Reply to each comment.** "Done", "Good catch, fixed in abc123", or "I did
   it this way because…". Don't leave a reviewer wondering.
3. **Make the changes** on the same branch, then commit and push:

   ```bash
   git add -A
   git commit -m "Address review: validate the level argument"
   git push origin feature/short-description
   ```

   The PR updates automatically and CI re-runs.
4. **Re-request review** (there's a button) when you're ready for another look.

## If you disagree

That's fine — say so, kindly, and explain your reasoning. Review is a
conversation, not orders. Often you'll land on a third, better option together.
If you're unsure, ask: "What would you suggest here?"

## When it's approved

Once a reviewer approves and CI is green, a maintainer merges it. 🎉 Your change
is now part of the project. Delete your branch (GitHub offers a button) and pull
`main` to get your merged work locally.

➡️ Next: [Updating documentation](09-updating-docs.md)
