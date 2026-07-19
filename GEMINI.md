# PFL Project Instructions

This file contains team-shared architecture, conventions, and workflows for the Personal Financial Ledger (PFL) repository.

## Engineering Standards
All AI contributors MUST adhere to the [AI Engineering Playbook](docs/03-Engineering/).

## UI Development Convention
- **Approach**: Server-side rendered UI using Google Apps Script's `HtmlService`.
- **Structure**: All UI templates reside in `src/ui/`.
- **Layout**: `src/ui/Index.html` is the main entry point (shell).
- **Partials**: Use the `include(filename)` helper function in `WebAppAdapter.gs` to inject partials (e.g., `Header`, `Navigation`) into the main layout.
- **Styling**: Styles are defined in partials (e.g., `src/ui/Styles.html`) and included in the `Index.html` head.

## Repository Artifact Policy

The repository is the only persistent workspace.

Any artifact that is intended for review, reuse, or version control must be written inside the repository.

Do not leave implementation plans, reports, review packages, or documentation in temporary directories, cache folders, or Gemini CLI working folders.

Temporary directories may be used internally during execution but must never become the canonical location of project artifacts.

## Git Automation Policy

When a Technical Lead approval prompt contains a **Git Operations** section, execute those operations automatically.

Do not ask for confirmation before running routine Git commands.

Permitted operations:

- git status
- git checkout -b
- git add
- git commit
- git push

Always report:

- current branch
- latest commit hash
- push status
- working tree status

Never:

- merge into main
- force push
- delete branches
- rewrite history

unless explicitly instructed.

## Planning Policy

All implementation plans intended for review or approval must be created inside the repository.

Do not rely on Gemini CLI temporary planning files as project artifacts.

The Product Owner and Technical Lead must never be required to retrieve files from temporary directories.

Repository planning documents are the authoritative planning artifacts.