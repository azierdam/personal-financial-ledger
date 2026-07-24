# Sprint

**Milestone:** D1 – Core Transaction Management

**Sprint:** D1.8 – Import & Export

**Feature Branch:**

```text
feature/pfl-d1-8-import-export
```

---

# Objective

<<<<<<< Updated upstream
Implement transaction search and filtering capabilities to allow users to quickly locate financial records while preserving the existing layered architecture and maintaining a responsive user experience.

This sprint extends the transaction retrieval capability without introducing architectural changes.
=======
Implement transaction import and export capabilities to enable users to back up and restore transaction data while preserving the existing architecture.

The implementation must integrate seamlessly with the current transaction management workflow without introducing architectural changes.
>>>>>>> Stashed changes

---

# Scope

## Service Layer

<<<<<<< Updated upstream
Implement search functionality within `TransactionService`.

Create:

```text
searchTransactions(searchCriteria)
=======
Extend `TransactionService` to support:

```text
exportTransactions()

importTransactions(...)
>>>>>>> Stashed changes
```

Responsibilities:

<<<<<<< Updated upstream
- Retrieve all transactions from the repository.
- Apply business filtering.
- Support filtering by:
  - Description
  - Transaction Type
  - Category
  - Date Range
- Support combined filters.
- Return filtered domain objects.

Filtering logic belongs exclusively in the Service layer.

---

## Search Criteria Model (Recommended)

Introduce a dedicated Search Criteria model instead of passing a generic object.

Example:

```javascript
{
  description: "",
  transactionType: "",
  category: "",
  startDate: null,
  endDate: null
}
```

Purpose:

- Strong API contract
- Easier validation
- Better extensibility
- Consistent with existing domain-oriented architecture

This model should remain lightweight and immutable where practical.
=======
- Retrieve transactions for export.
- Import transaction data.
- Validate imported data.
- Convert imported records into domain objects.
- Persist valid transactions.
- Return import results.

Business validation belongs exclusively in the Service layer.
>>>>>>> Stashed changes

---

## Repository

<<<<<<< Updated upstream
Reuse the existing retrieval methods.
=======
Reuse the existing repository implementation.
>>>>>>> Stashed changes

Repository responsibilities remain:

- Persistence
- Retrieval

<<<<<<< Updated upstream
Repository must **not** implement business filtering.

Do not introduce repository-side optimization during this sprint.
=======
No business logic shall be implemented in the repository.
>>>>>>> Stashed changes

---

## WebApp

<<<<<<< Updated upstream
Expose:

```text
getFilteredTransactions(searchCriteria)
```
=======
Expose endpoints required for:

- Export Transactions
- Import Transactions

WebApp remains a thin adapter between the UI and Service layer.
>>>>>>> Stashed changes

Responsibilities:

- Receive Search Criteria
- Delegate to TransactionService
- Return filtered transactions

Business logic must not be duplicated inside WebApp.

---

## UI

<<<<<<< Updated upstream
Enhance the transaction page with:

- Search textbox
- Transaction Type filter
- Category filter
- Date range selector
- Clear Filters button

Filtering should update the transaction list dynamically using:

```text
google.script.run
```

without requiring a page refresh.
=======
Provide user actions for:

- Export Transactions
- Import Transactions

The UI shall:

- Allow users to select an import file.
- Allow users to export existing transactions.
- Display import results.
- Refresh the transaction list after a successful import.
>>>>>>> Stashed changes

---

# Constraints

<<<<<<< Updated upstream
- Preserve the current layered architecture.
- Keep all business filtering inside TransactionService.
- Repository remains persistence-only.
- Reuse existing repository methods.
- No architectural refactoring.
- No regression to CRUD functionality.
- No regression to Dashboard functionality.
- Keep the implementation simple, maintainable, and deterministic.
- Stop and report if architectural changes become necessary.
=======
- Preserve the existing layered architecture.
- Repository remains persistence-only.
- Business validation remains inside TransactionService.
- Reuse existing domain models where applicable.
- Maintain compatibility with existing CRUD functionality.
- Maintain compatibility with Dashboard.
- Maintain compatibility with Search & Filter.
- Keep the implementation simple and maintainable.
- Stop implementation if architectural changes become necessary.
>>>>>>> Stashed changes

---

# Acceptance Criteria

<<<<<<< Updated upstream
- Search by description works.
- Filter by transaction type works.
- Filter by category works.
- Filter by date range works.
- Multiple filters can be combined.
- Clear Filters restores the complete transaction list.
- Results are accurate.
- CRUD functionality remains unaffected.
- Dashboard functionality remains unaffected.
- Review artifacts correctly describe the D1.7 implementation.
=======
- Users can export transactions.
- Users can import valid transactions.
- Invalid transaction data is handled gracefully.
- Import results are communicated to the user.
- Existing CRUD functionality continues to work.
- Dashboard functionality continues to work.
- Search & Filter functionality continues to work.
- Engineering Review Package accurately reflects the implementation.
>>>>>>> Stashed changes

---

# Deliverables

## Application

<<<<<<< Updated upstream
- `src/service/TransactionService.gs`
- Search Criteria model (if introduced)
- `src/app/WebApp.gs`
- `src/ui/Transactions.html`
- Supporting JavaScript updates
- Integration tests (where applicable)

## Engineering

Regenerate the complete Engineering Review Package:
=======
- TransactionService updates
- WebApp updates
- Import UI
- Export UI
- Supporting JavaScript
- Tests (where applicable)

## Engineering

Generate the complete Engineering Review Package:
>>>>>>> Stashed changes

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
git commit -m "docs(engineering): approve D1.8 import & export"
```

Implementation

```powershell
git commit -m "feat(import-export): implement transaction import and export"
```

---

# Stop Condition

Stop implementation immediately if:

- Repository responsibilities must expand beyond persistence and retrieval.
<<<<<<< Updated upstream
- Search requires architectural redesign.
- Business filtering cannot remain inside TransactionService.
- Existing CRUD functionality regresses.
- Dashboard functionality regresses.
- Acceptance Criteria cannot be achieved within the approved architecture.
=======
- Business validation cannot remain inside TransactionService.
- Existing transaction functionality regresses.
- Dashboard functionality regresses.
- Search & Filter functionality regresses.
- Architectural changes become necessary.
>>>>>>> Stashed changes

Do not make architectural decisions independently.

Instead:

1. Document the issue.
2. Explain the root cause.
<<<<<<< Updated upstream
3. Describe available implementation options.
4. Assess the impact of each option.
=======
3. Present available implementation options.
4. Assess the impact.
>>>>>>> Stashed changes
5. Return control to the Technical Lead.

---

# Technical Lead Review

## Status

✅ **Approved for Implementation**

<<<<<<< Updated upstream
The proposed implementation plan aligns with the approved architecture and satisfies the objectives of Sprint D1.7.

The current design preserves clear separation of responsibilities:

```text
Transactions UI
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

### Technical Lead Recommendations

The following recommendation is **approved for implementation** as part of this sprint:

- Introduce a lightweight `SearchCriteria` model instead of passing a generic object between the UI, WebApp, and Service layers.
- Keep the model simple and focused on representing filter parameters.
- Centralize validation and filtering logic within `TransactionService`.
- Continue treating the repository as a persistence and retrieval layer only.

This recommendation improves maintainability and extensibility without increasing unnecessary complexity.

### Parking Lot (Post-MVP)

The following is **not** part of Sprint D1.7:

- Repository-side query optimization.
- Indexed searching.
- Server-side filtering against Google Sheets.

The current in-memory filtering approach is appropriate for the expected MVP data volume and best aligns with the project's principles of simplicity, maintainability, and low operating cost.
=======
The implementation plan is approved.

Implementation shall:

- Preserve the current layered architecture.
- Reuse the existing repository.
- Keep business logic inside TransactionService.
- Avoid unnecessary architectural changes.
- Regenerate the complete Engineering Review Package after implementation.

The objective of this sprint is to complete the Import & Export capability while maintaining the project's principles of simplicity, maintainability, and low operating cost.
>>>>>>> Stashed changes
