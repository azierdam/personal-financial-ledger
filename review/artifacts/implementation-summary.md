# Implementation Summary: Separating Approval and Review Workflow

## Changes
- Updated `docs/03-Engineering/ENGINEERING_WORKFLOW.md` to clearly distinguish between the roles of `technical-lead-approval.md` (parsed by Engineering CLI) and `technical-lead-review.md` (authored by Technical Lead for review authorization).
- Updated `tools/engineering/README.md` to explicitly note that the Engineering CLI does not parse or interact with `technical-lead-review.md`.

## Validation
- Workflow documentation now reflects the updated lifecycle.
- Engineering CLI parser remains unchanged and correctly targets only `technical-lead-approval.md`.

## Git Status
- Confirmed modifications to `docs/03-Engineering/ENGINEERING_WORKFLOW.md` and `tools/engineering/README.md`.
