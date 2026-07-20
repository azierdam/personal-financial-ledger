# Overview
Transaction editing functionality requires updating existing ledger rows without compromising the immutable financial identity (ID, Type, Amount, etc.).

# Design Decisions
- Reused `TransactionForm.html` for both creation and editing by populating initial data based on transaction existence.
- Implemented `update` in `GoogleSheetsTransactionRepository` to modify rows based on ID.
- Service layer handles update logic, ensuring only metadata is modified.

# Constraints
- Immutable fields (ID, Type, Amount, Account, Timestamp) are read-only in UI.
- No direct spreadsheet manipulation in UI.

# Known Risks
- Race conditions during concurrent edits (not addressed in this sprint).

# Deferred Work
- Enhanced validation for edit-specific constraints.
- Transaction update audit trail.
