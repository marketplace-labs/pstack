---
name: no-comments
description: "Review and improve comments, preserving useful reasoning and removing redundant or demonstrably stale text."
disable-model-invocation: true
---

# Review comments

Keep the existing `/no-comments` command for compatibility. Its purpose is useful, accurate comments, not the fewest comments.

## Scope and policy

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree.

Preserve design reasoning, tradeoffs, security assumptions, safety constraints, non-obvious behaviour, external quirks, public API contracts, relevant links, and actionable TODOs. Preserve legal and licence notices. Remove redundant narration and demonstrably obsolete comments. Shorten or correct text only without losing useful context. When uncertain, keep the comment and flag what needs investigation.

## Workflow

1. Request an independent review using `comment-sicko` with the scope and relevant context. Use the caller's available agent mechanism and model configuration. If independent review is unavailable, perform the same review directly and disclose that limitation.
2. Check recommendations against the code and available evidence. Reject unsupported deletions, lost rationale, out-of-scope edits, and any assumption that internal code cannot deserve an explanatory comment.
3. Apply justified comment edits within the user's authorised scope. If the user requested a proposal or review first, present the edits without applying them. Preserve uncertain comments and report the open questions.
4. Treat suppressions, formatter directives, documentation directives, and other functional annotations as configuration. Do not remove or change them as routine prose cleanup. If a change is in scope, establish its effect and run the relevant checks; otherwise report it separately.
5. Suggest names, types, tests, runtime checks, or refactors where they would clarify or enforce an important constraint. Do not expand a comment review into application changes without authorisation. Keep complementary rationale even when a constraint becomes enforced.
6. Inspect the final diff. Confirm useful context and protected notices remain. Run relevant validation when executable examples, tooling directives, or generated documentation were affected. Report changes, retained context, validation, unresolved questions, and separate code proposals. Never use deletion count as a success target.
