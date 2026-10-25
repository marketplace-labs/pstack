# PStack for Codex — Marketplace Labs

A Codex skill adapted from **PStack by Lauren Tan (@poteto)**. Use your existing Codex model and tools. No Cursor installation, Claude account, or extra model subscription is required.

## Install

In Codex, ask the built-in installer:

```text
$skill-installer install https://github.com/marketplace-labs/pstack/tree/main/codex/pstack
```

The package is self-contained. Install only `codex/pstack`, not the individual upstream skills. The installer refuses to overwrite an existing destination. The skill is available on your next turn; if it is not listed, restart Codex.

For an update, first preserve any local customisations and move the existing installed `pstack` folder out of the skills directory, then run the installer again. This repository does not enable automatic updates.

## Use

Open your project in Codex, then write:

```text
$pstack fix this bug: [describe the problem]. Reproduce it, fix the cause, and verify the result.
$pstack review the current diff. Report findings without editing.
$pstack review comments in the current diff. Keep useful reasoning.
$pstack build [feature]. Show the changes for review before committing.
```

The single entry point chooses a bundled workflow. Original commands such as `/poteto-mode` and `/no-comments` are not registered Codex commands. Use `$pstack` with a task instead.

## What is adapted

- Native Codex tools and the session's selected model replace Cursor tool names and model aliases.
- Delegation requires the user's or host's authorisation; serial review is labelled honestly.
- User scope, repository instructions, sandbox permissions, and review-before-commit gates remain in force.
- Comment review retains design rationale, tradeoffs, security assumptions, constraints, and non-obvious behaviour. Uncertain comments stay and are flagged.
- All supporting workflows and the original licence travel with the installed skill.

Read [the adapter](codex/pstack/references/codex.md) for exact translations and limits. This is an instruction-based adaptation, not a runtime emulator. Cursor Automations, cloud agents, Bugbot setup, external model panels, and unattended scheduling are not included. Existing local integration tools may still be used when available and authorised.

Packaging and installation checks do not prove every workflow or model follows the instructions correctly. Review generated changes and verify the actual application.

## Maintain the package

Edit source workflows in `skills/`, reviewer briefs in `agents/`, and the Codex entry point or adapter in `codex/pstack/`. Rebuild before committing changes:

```sh
python3 scripts/build-codex.py
python3 scripts/build-codex.py --check
python3 scripts/test_build_codex.py
git diff --check
```

The generated `codex/pstack/references/upstream/` directory must be committed so GitHub skill installation includes every supporting file.

## Attribution and licence

PStack is by Lauren Tan (@poteto), originally in [cursor/plugins](https://github.com/cursor/plugins/tree/main/pstack). Marketplace Labs maintains this unofficial standalone adaptation and is not endorsed by the original author or Cursor.

The original [MIT licence](LICENSE) and copyright are retained. [UPSTREAM.md](UPSTREAM.md) records provenance and local changes. [The imported README](docs/upstream-readme.md) is historical reference; its installation commands target upstream distributions and do not install this Codex adaptation.
