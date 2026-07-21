# Sprint

**Milestone:** D1 – Core Transaction Management

**Sprint:** D1.6 – Dashboard & Summary

**Feature Branch:**

```text
feature/pfl-d1-6-dashboard-summary
```

---

# Objective

Implement the financial dashboard to provide users with a consolidated summary of their financial data.

The dashboard must reuse the existing application architecture and present aggregated information without duplicating business logic.

---

# Scope

## Service Layer

Implement dashboard summary functionality, including:

- Current Balance
- Total Income
- Total Expense
- Transaction Count
- Monthly Summary

All calculations must be performed within the Service layer.

---

## Repository

Reuse the existing repository retrieval methods.

Only extend the repository if required for maintainability or performance.

No business calculations belong in the repository.

---

## WebApp

Expose the endpoints required by the dashboard.

Maintain the existing:

```text
UI
 ↓
WebApp
 ↓
Service
 ↓
Repository
```

architecture.

---

## UI

Implement a Dashboard view displaying:

- Current Balance
- Total Income
- Total Expense
- Transaction Count
- Monthly Summary

The dashboard should automatically refresh after:

- Transaction Creation
- Transaction Editing
- Transaction Deletion

---

# Constraints

- Follow the existing layered architecture.
- Reuse existing services whenever possible.
- Do not duplicate aggregation logic.
- Do not modify unrelated functionality.
- Preserve backward compatibility.
- Keep the implementation simple and maintainable.
- Do not introduce architectural changes.
- If implementation becomes ambiguous, stop and report the issue instead of making architectural decisions.

---

# Acceptance Criteria

- Dashboard displays the current balance correctly.
- Dashboard displays total income correctly.
- Dashboard displays total expenses correctly.
- Dashboard displays transaction count correctly.
- Dashboard displays monthly summary correctly.
- Dashboard refreshes automatically after Create, Edit, and Delete operations.
- No financial calculations exist in the UI.
- Repository remains responsible only for data persistence and retrieval.
- Existing transaction workflows continue to function without regression.

---

# Deliverables

## Application

- `src/service/TransactionService.gs`
- `src/app/WebApp.gs`
- `src/ui/Dashboard.html`
- Integration tests (if applicable)

## Engineering

Generate a complete Engineering Review Package containing:

- `technical-lead-approval.md`
- `implementation-summary.md`
- `architecture-notes.md`
- `changed-files.md`
- `validation.md`
- `self-review.md`
- `manifest.json`

Follow the Engineering CLI workflow:

```bash
git add review/current/technical-lead-approval.md
git commit -m "docs(engineering): approve D1.6 dashboard & summary"

python -m tools.engineering setup
python -m tools.engineering prepare gemini
```

---

# Conventional Commit

Approval Document:

```bash
git commit -m "docs(engineering): approve D1.6 dashboard & summary"
```

Implementation:

```bash
git commit -m "feat(dashboard): implement dashboard and financial summary"
```

---

# Stop Condition

Stop implementation immediately if:

- The approved scope cannot be completed without changing the existing architecture.
- Additional repository interfaces are required beyond the approved scope.
- Business rules are ambiguous or undocumented.
- Acceptance Criteria cannot be satisfied with the current design.
- A potential regression affecting existing transaction management is identified.

Do not make architectural decisions independently.

Instead, document:

1. The blocking issue.
2. The affected components.
3. The proposed options.
4. The implementation impact.

Return control to the Technical Lead for a decision.