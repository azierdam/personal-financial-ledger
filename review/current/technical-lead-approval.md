# Sprint

**Milestone:** D1 – Core Transaction Management

**Sprint:** D1.6 – Dashboard & Summary

**Feature Branch:**

```text
feature/pfl-d1-6-dashboard-summary
```

---

# Objective

Implement a financial dashboard that provides users with a consolidated summary of their financial data.

This sprint introduces read-only aggregation capabilities built on top of the completed transaction management features. The implementation must reuse the existing architecture, centralize all business calculations within the Service layer, and avoid duplicating logic across the application.

---

# Scope

## Dashboard

Implement a dashboard displaying:

- Current Balance
- Total Income
- Total Expense
- Net Balance
- Transaction Count
- Monthly Summary

---

## Service Layer

Extend `TransactionService` with summary and aggregation methods.

Business calculations must remain exclusively within the Service layer.

---

## Repository

Reuse existing repository retrieval methods.

Only extend the repository when required for performance or maintainability.

Do not place business calculations inside the repository.

---

## WebApp

Expose dashboard endpoints required by the UI.

Maintain the existing architecture:

```text
Dashboard UI
        │
        ▼
WebApp
        │
        ▼
TransactionService
        │
        ▼
GoogleSheetsTransactionRepository
```

---

## UI

Implement the Dashboard page.

The dashboard must automatically refresh after:

- Create Transaction
- Edit Transaction
- Delete Transaction

No manual refresh should be required.

---

# Constraints

- Preserve the existing layered architecture.
- Reuse existing repository methods whenever possible.
- Do not duplicate business logic.
- Do not introduce architectural changes.
- Preserve backward compatibility.
- Keep the implementation simple and maintainable.
- Do not modify unrelated functionality.
- If blocked or ambiguous, stop implementation and report the issue to the Technical Lead.

---

# Acceptance Criteria

- Dashboard displays Current Balance correctly.
- Dashboard displays Total Income correctly.
- Dashboard displays Total Expense correctly.
- Dashboard displays Net Balance correctly.
- Dashboard displays Transaction Count correctly.
- Dashboard displays Monthly Summary correctly.
- Dashboard refreshes automatically after Create, Edit, and Delete operations.
- No business calculations exist in the UI.
- Repository remains responsible only for persistence.
- Existing transaction features continue to work without regression.

---

# Deliverables

## Application

- Dashboard UI
- TransactionService summary methods
- WebApp dashboard endpoints
- Integration with existing repository
- Dashboard refresh workflow

## Engineering

Generate the Engineering Review Package containing:

- technical-lead-approval.md
- implementation-summary.md
- architecture-notes.md
- changed-files.md
- validation.md
- self-review.md
- manifest.json

Implementation must follow the Engineering CLI workflow.

---

# Conventional Commit

Approval Document

```bash
git commit -m "docs(engineering): approve D1.6 dashboard & summary"
```

Implementation

```bash
git commit -m "feat(dashboard): implement financial dashboard and summary"
```

---

# Stop Condition

Stop implementation immediately if:

- The approved scope requires architectural changes.
- New repository interfaces are required beyond the approved scope.
- Business rules are ambiguous.
- Acceptance Criteria cannot be satisfied with the current architecture.
- A regression affecting transaction management is detected.

Do not make architectural decisions independently.

Document:

1. Blocking issue.
2. Affected components.
3. Possible implementation options.
4. Expected impact.

Return control to the Technical Lead.