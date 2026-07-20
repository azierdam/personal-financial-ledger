# Engineering CLI

A lightweight internal developer tool for PFL engineering tasks.

## Engineering Workflow v2.1
The Engineering CLI automates the execution of the finalized Engineering Workflow v2.1.

### Artifact Ownership
| Artifact | Owner | Purpose |
| :--- | :--- | :--- |
| `technical-lead-approval.md` | Technical Lead | Machine Contract (Implementation Spec) |
| `.context.md` | Engineering CLI | Gemini context |
| `.prompt.md` | Engineering CLI | Gemini implementation prompt |

*Note: The CLI does NOT parse or interact with `technical-lead-review.md` (Technical Lead artifact).*

## Command Responsibilities

Each command has a single, distinct responsibility:

| Command | Responsibility |
| :--- | :--- |
| `doctor` | Environment validation. |
| `context` | Generate repository context. |
| `prompt` | Generate implementation prompt from `approval.md`. |
| `prepare` | Orchestrate environment setup (branching, context, prompt). |
| `package` | Package review artifacts. |

## Branch Naming Rules
Branch names are generated deterministically based on the sprint ID to ensure Git compliance:
- Normalized to lowercase ASCII.
- All non-alphanumeric characters replaced with single hyphens.
- Repeated hyphens collapsed to a single hyphen.
- Leading and trailing hyphens removed.
- Example: "Engineering CLI – Sprint 1.0" -> `engineering-cli-sprint-1-0`

## Working Tree Safety
The Engineering CLI automatically validates the working tree before any branch automation (Git checkout/branch creation).
- If uncommitted changes are detected, the process is blocked to prevent destructive Git operations.
- The CLI provides a diagnostic report classifying changes into Generated Artifacts and User Modifications.
- Users must commit or stash changes before running `prepare`.
The parser *strictly requires* these sections to be present and non-empty:
- `# Sprint`
- `# Objective`
- `# Scope`
- `# Constraints`
- `# Acceptance Criteria`
- `# Deliverables`
- `# Conventional Commit`
- `# Stop Condition`

*Optional sections (e.g., `# Branch Strategy`, `# Architecture`) are safely ignored by the Engineering CLI.*