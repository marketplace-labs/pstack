---
name: pstack
description: "Use PStack workflows for coding, debugging, code review, architecture, or verification when the user asks for PStack or poteto mode."
---

# PStack for Codex

This is Marketplace Labs' Codex adaptation of Lauren Tan's PStack. Supporting workflows are bundled under `references/upstream/`; they are reference material, not separately installed skills.

Read [the Codex adapter](references/codex.md) before using any bundled workflow. Apply it to every bundled instruction, including instructions passed to another agent. Host instructions, repository instructions, and the user's scope and review gates take precedence over this package.

## Choose a workflow

Interpret `$pstack <request>` as a request to use PStack for that task. Read only the matching workflow and the supporting files it needs. Paths below are relative to `references/upstream/`.

| Request | Read |
| --- | --- |
| Investigate or explain existing behaviour | `skills/poteto-mode/playbooks/investigation.md` |
| Fix a bug | `skills/poteto-mode/playbooks/bug-fix.md` |
| Build a feature | `skills/poteto-mode/playbooks/feature.md` |
| Refactor | `skills/poteto-mode/playbooks/refactoring.md` |
| Design architecture | `skills/architect/SKILL.md` |
| Review a diff | `skills/interrogate/SKILL.md` |
| Review comments | `skills/no-comments/SKILL.md` and `agents/comment-sicko.md` |
| Create a way to verify the real app | `skills/create-verification-skill/SKILL.md` |
| Another named PStack workflow | Find its file under `skills/`, then read it |

If no workflow fits, use the core approach below. Do not load the entire upstream mode or every principle for a small task.

## Core approach

Establish the requested outcome and inspect the existing code before editing. For bugs, reproduce the failure when feasible. Make the smallest coherent change that addresses the cause. Verify observable behaviour using the actual artifact and relevant checks. Preserve useful comment reasoning under the bundled revised policy. Report the result, evidence, and remaining limitations without claiming checks that did not run.

Do not enable PStack permanently, edit global instructions, configure models, commit, publish, or start unattended work just because this skill was invoked. Follow the user's actual request and existing authorisation.

For `setup`, explain that this package uses the session's selected Codex model and tools and needs no Cursor setup or additional model subscriptions. Do not run upstream `setup-pstack`.
