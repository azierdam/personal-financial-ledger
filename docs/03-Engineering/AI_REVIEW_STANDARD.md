# AI Review Standard

## Definition
Every sprint produces an **Engineering Handover Package** to ensure quality, traceability, and maintainability.

## Engineering Handover Package Structure
- **Location:** `review/current/`
  - `HANDOVER.md`: Canonical entry point for review.
  - `artifacts/`: Contains all required review documentation.
  - `snapshots/`: Contains the state of `src/`, `docs/`, `test/` relevant to the review.

## Mandatory Artifacts (`review/current/artifacts/`)
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
- `technical-lead-response.md` (Must start as placeholder)

## Cleanup Policy
After Git push and Product Owner approval:
1. Remove temporary Gemini planning artifacts.
2. Remove temporary compilation directories.
3. Remove obsolete generated review folders outside `review/current/`.
4. Reset `review/current/` for the next sprint.
