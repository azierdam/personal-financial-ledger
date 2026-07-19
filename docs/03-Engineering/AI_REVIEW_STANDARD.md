# AI Review Standard

## Definition
Every task produces an **Engineering Handover Package** to ensure quality, traceability, and maintainability.

## Engineering Handover Package Structure
- **Location:** `review/`
  - `artifacts/`: Contains all review documentation (`gemini-handover.md` is mandatory).
  - `snapshots/`: Contains the state of `src/`, `docs/`, `test/` relevant to the review.

## Mandatory Artifacts
- `repository-analysis.md` (when applicable)
- `implementation-plan.md` (when applicable)
- `implementation-summary.md`
- `architecture-notes.md`
- `self-review.md`
- `gemini-handover.md` (Mandatory)
- `validation.md`
- `test-results.md`
- `changed-files.md`
- `commit-message.txt`
- `checklist.md`
- `technical-lead-response.md` (Placeholder for Tech Lead approval)

## Artifact Lifecycle
The `review/` folder is part of the repository. All review artifacts are version-controlled and committed as part of the standard engineering workflow.
