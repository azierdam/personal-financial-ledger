# Engineering CLI

A lightweight internal developer tool for PFL engineering tasks.

## Technical Lead Approval (Machine Contract)
The Engineering CLI uses a machine-readable contract for `review/current/technical-lead-approval.md`.

*Note: The CLI does NOT parse or interact with `technical-lead-review.md`.*

### Required Sections
The parser *strictly requires* these sections to be present and non-empty:
- `# Sprint`
- `# Objective`
- `# Scope`
- `# Constraints`
- `# Acceptance Criteria`
- `# Deliverables`
- `# Conventional Commit`
- `# Stop Condition`

### Optional Sections
The parser *ignores* any section that is not in the required list above (e.g., `# Branch Strategy`, `# Architecture`, `# Technical Lead Recommendations`). Future templates can safely extend with optional sections without breaking the Engineering CLI.

### Extending the Template
When extending the template:
1. Always keep the required sections above.
2. New sections are optional; they will be safely ignored by the Engineering CLI.

## Workflow Alignment
The Engineering CLI distinguishes between **Working Files** (regenerated every sprint) and **Sprint Artifacts** (immutable deliverables).

### Working Files
These files are part of the active engineering workspace.
- **Files**: `.context.md`, `.prompt.md`, `review/current/technical-lead-approval.md`
- **Characteristics**: Regenerated every sprint, temporary, not implementation deliverables.

### Sprint Artifacts
These files are generated after implementation and are final deliverables.
- **Files**: `review/artifacts/implementation-summary.md`, `review/artifacts/validation.md`, `review/artifacts/commit-message.txt`, `review/artifacts/handover.md`
- **Characteristics**: Final deliverables, reviewed by Technical Lead (`technical-lead-review.md`), immutable after approval.

## Commands
- `python -m tools.engineering doctor`: Validate repository environment.
- `python -m tools.engineering context`: Generate/regenerate `.context.md`.
- `python -m tools.engineering prompt gemini`: Generate/regenerate implementation prompt from `review/current/technical-lead-approval.md` in `.prompt.md`.
- `python -m tools.engineering prepare gemini`: Regenerate working files (`.context.md`, `.prompt.md`) and verify the workspace (`review/current/`).

## Architecture
- `core/`: Generic, reusable modules (repository, filesystem, git, approval parsing, etc.).
- `commands/`: Specific task implementations.
- `templates/`: Templates for artifact generation.

## Machine Contract

The Engineering CLI parses only the required sections of `technical-lead-approval.md`.

### Required Sections

- Sprint
- Objective
- Scope
- Constraints
- Acceptance Criteria
- Deliverables
- Conventional Commit
- Stop Condition

These sections form the **Machine Contract**.

Changes to these sections are considered **breaking changes** to the Engineering CLI and must be reviewed carefully.

### Optional Sections

Any additional sections are ignored by the parser.

Examples include:

- Branch Strategy
- Architecture
- Technical Lead Recommendations
- Engineering CLI Enhancement
- Post-Approval Actions

These sections may evolve without affecting the Engineering CLI.