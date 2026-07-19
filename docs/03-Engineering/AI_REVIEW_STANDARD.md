# AI Review Standard

## Definition
Every task produces a review package to ensure quality and traceability.

## Review Artifacts
- **Review Markdown:** Detailed summary of the changes, design decisions, and reasoning.
- **Self Review:** AI-generated verification against the implementation standards.
- **Architecture/Design Notes:** Documentation of any deviations or clarifications.
- **Changed Files List:** Precise list of affected files.
- **Repository Tree:** Visual representation of changed files.
- **Review Checklist:** Completed checklist confirming all requirements.

## Review Package
- **Location:** `.temp/reviews/`
- **Naming:** `review-[SPRINT_ID/TASK_ID].zip` (e.g., `review-S2-05.zip`)
- **Lifecycle:** The ZIP file is a temporary artifact. It is never committed to Git and MUST be deleted after human approval.
