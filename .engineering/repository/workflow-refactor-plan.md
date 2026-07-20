# Workflow Refactor Plan

## Target Workflow
1. Technical Lead Approval (Contract)
2. Engineering CLI Setup (Automation)
3. Gemini Implementation (Manifest-driven)
4. Technical Lead Review (Contract)
5. Repository Finalization (Automation)

## Migration Steps
1. Introduce canonical Review Package Generator (v2).
2. Archive legacy `archive/planning-artifacts/`.
3. Consolidate `review/artifacts/`.
4. Migrate all packaging logic to use `workflow-contract.json`.

## Risk Assessment
- Low: Workflow documentation update.
- Medium: Consolidating review artifacts.
- High: Modifying package generator (requires deterministic validation).
