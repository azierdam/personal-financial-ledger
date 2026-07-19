# Architectural Notes: C1.1
- Implemented storage-agnostic domain entities with stable identifiers.
- Repository interfaces are business-oriented (save, findById, etc.).
- Added basic domain invariants to entity constructors to ensure data integrity.
- Removed `delete` from `TransactionRepository` to enforce transaction immutability.
