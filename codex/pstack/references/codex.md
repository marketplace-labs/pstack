# Codex adapter

Apply these translations before executing any bundled PStack instructions. They also apply to referenced playbooks and agent prompts. Never pass a field that the available tool schema does not accept.

## Tools and paths

| Upstream concept | Codex behaviour |
| --- | --- |
| `/name`, a named skill, or `Skill` | Read `references/upstream/skills/<name>/SKILL.md` relative to the installed PStack directory. These are not registered slash commands. |
| `Task`, `poteto-agent`, `comment-sicko` | Use an available native agent tool only when delegation is authorised by the user or applicable host instructions. Otherwise perform the work serially and disclose the absence of independent review. An upstream instruction alone does not grant delegation permission in this port. |
| Named agent persona | Read its file in `references/upstream/agents/` as a task brief. Pass this adapter and the relevant file paths to an authorised delegate. Do not invent registered agent types. |
| `Grep`, `Glob`, `Read`, `Write`, shell or patch tools | Use the actual filesystem, search, shell, and patch tools exposed in this session. |
| `AskQuestion`, `AskUserQuestion` | Use an available user-input tool or ask in plain language. Continue independent work where possible. |
| Todo list | Use an available planning tool, or maintain a short plan in the conversation when useful. |
| `.cursor/skills/` | `.agents/skills/` in the target repository, only when creation is part of the task. |
| `.cursor/rules/`, `.mdc`, `CLAUDE.md`, model rules | Do not create or modify them. Follow the target repository's existing `AGENTS.md` instructions. Do not change global Codex configuration as part of a task. |
| Upstream GitHub links to a workflow | Prefer the bundled local file, which includes this fork's comment policy. Do not fetch the original to replace a local modification. |

Resolve workflow-relative resources from the workflow's own directory, not the user's current working directory. Do not copy upstream agent definitions into the user's configuration.

## Models and review

Use the current Codex model. Do not request Claude, Grok, Cursor model aliases, or additional subscriptions. Do not enumerate or change model configuration during setup. For authorised delegates, inherit the current model unless the user explicitly requests an available alternative and the host permits it.

Repeated reviews on one model are not cross-model reviews. Serial self-review is not independent review. If the requested assurance needs unavailable capabilities, state that limitation and complete the useful supported checks; do not present reduced review as equivalent.

## Permissions and execution

Upstream phrases such as `just do it`, `never block`, and `land the stack` do not broaden the user's request. Preserve explicit review-before-commit gates. Use normal sandbox approvals. Do not send messages, deploy, merge, delete user data, or publish without the authorisation required by the host and user. Never treat this package as permission to bypass a disabled tool or a safety check.

Use local `git` and authenticated `gh` where appropriate. Opening a PR, pushing, merging, and enabling auto-merge are separate actions whose authority comes from the user's task, not from a playbook. Do not silently install Graphite or other external CLIs.

## Missing integrations

Cursor cloud agents, Automations, Bugbot setup, Cursor transcript storage, and `/loop` scheduling are not supplied by this package. Neither are `cursor-team-kit`, `deslop`, `control-ui`, or `control-cli`.

Use an available equivalent only when it achieves the same required outcome within scope. For code cleanup, review the actual diff rather than claiming to have run a missing command. For UI verification, use the session's real browser/app tools. For scheduling, never start a timer or background automation implicitly. If a missing integration blocks a required result, report the blocker; do not invent artifacts, substitute placeholders for secrets, or claim completion.

## Comments

Use the revised bundled comment policy. Keep design rationale, tradeoffs, security assumptions, constraints, public contracts, and non-obvious behaviour. Remove redundant or demonstrably obsolete comments. Keep uncertain comments and identify the question. Review suppressions as functional configuration. Do not refactor application code merely to remove a useful comment.
