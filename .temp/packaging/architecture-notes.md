# Architecture Notes: D1.7 Search & Filter

## Architectural Integrity
The existing layered architecture is preserved:
- Service layer (`TransactionService`) handles all business filtering logic.
- Repository layer (`GoogleSheetsTransactionRepository`) remains responsible solely for data persistence and retrieval.
- UI layer (`Transactions.html`, `WebApp.gs`) handles presentation and orchestration via AJAX for a responsive experience.

No business calculations were introduced into the UI or repository layers.
