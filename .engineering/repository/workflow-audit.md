# Workflow Audit

## Current State
- Approval/Review workflows are entangled.
- Engineering Review Package still depends on manual artifacts.
- Milestone-specific artifacts copied into unrelated implementations.
- Legacy sprint concepts exist in `archive/planning-artifacts/`.

## Obsolete Components
- Manual review templates in `review/artifacts/`.
- Project-specific sprint directories.
- Legacy workflow documentation.

## Proposed Changes
- Consolidate all packaging artifacts into a single contract-driven generator.
- Move from directory-driven packaging to contract-driven packaging.
- Automate technical-lead-review input based on approved-findings.
