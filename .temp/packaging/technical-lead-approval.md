# Sprint

**Milestone:** D1 – Core Transaction Management

**Sprint:** D1.7 – Search & Filter

**Feature Branch:**

```text
feature/pfl-d1-7-search-filter
```

---

# Objective

Implement transaction search and filtering capabilities to help users quickly locate financial records.

The implementation must reuse the existing transaction retrieval flow and preserve the current layered architecture.

---

# Scope

## Service Layer

Extend `TransactionService` with search functionality.

Supported capabilities:

- Search by description
- Filter by transaction type (Income / Expense)
- Filter by category
- Filter by date range
- Combined filters

All filtering logic belongs in the Service layer.

---

## Repository

Reuse existing retrieval methods.

Filtering should operate on retrieved domain objects unless a repository optimization is clearly justified.

Do not introduce repository-side business logic.

---

## WebApp

Expose endpoints supporting transaction search and filtering.

Maintain the existing architecture:

```text
Search UI
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

Enhance the transaction list with:

- Search box
- Transaction Type filter
- Category filter
- Date range filter
- Clear Filters action

Filtering should refresh the transaction list without requiring manual page reloads.

---

# Constraints

- Preserve the existing layered architecture.
- Reuse existing repository methods.
- Keep business logic within the Service layer.
- Repository remains responsible only for persistence and retrieval.
- Do not introduce architectural changes.
- Preserve backward compatibility.
- Keep the implementation simple and maintainable.
- If blocked or ambiguous, stop and report to the Technical Lead.

---

# Acceptance Criteria

- Users can search by description.
- Users can filter by transaction type.
- Users can filter by category.
- Users can filter by date range.
- Multiple filters can be combined.
- Clear Filters restores the complete transaction list.
- Search results are accurate.
- Existing CRUD functionality continues to work without regression.
- Review artifacts accurately reflect the D1.7 implementation.

---

# Deliverables

## Application

- `src/service/TransactionService.gs`
- `src/app/WebApp.gs`
- `src/ui/TransactionList.html`
- Supporting UI updates
- Integration tests (where applicable)

## Engineering

Generate the Engineering Review Package:

- technical-lead-approval.md
- implementation-summary.md
- architecture-notes.md
- changed-files.md
- validation.md
- self-review.md
- checklist.md
- gemini-handover.md
- manifest.json

---

# Conventional Commit

Approval Document

```powershell
git commit -m "docs(engineering): approve D1.7 search & filter"
```

Implementation

```powershell
git commit -m "feat(search): implement transaction search and filtering"
```

---

# Stop Condition

Stop implementation immediately if:

- The approved scope requires architectural changes.
- Repository responsibilities must expand beyond persistence and retrieval.
- Search requirements become ambiguous.
- Acceptance Criteria cannot be satisfied within the current architecture.
- A regression affecting existing transaction management is detected.

Do not make architectural decisions independently.

Instead:

1. Document the blocking issue.
2. Identify the affected components.
3. Describe the available implementation options.
4. Explain the expected impact.

Return control to the Technical Lead.