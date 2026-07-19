# Repository Contract Standard

This document defines the standard contract for all repository interfaces in the PFL repository.

## 1. Naming Convention
- All repositories must be named `[EntityName]Repository`.
- Example: `AccountRepository`, `TransactionRepository`.

## 2. Method Semantics
All repositories must implement:
- `save(entity)`: Persists a new entity.
- `findById(id)`: Retrieves an entity by its stable identifier.
- `findAll()`: Retrieves all entities.

Mutable entities must implement:
- `update(entity)`: Updates an existing entity.

## 3. Immutability Principle
- Entities representing historical facts (e.g., `Transaction`) are immutable. Their repositories MUST NOT expose `update` or `delete` operations.
- Entities representing configuration or state that changes over time (e.g., `Account`, `Category`) are mutable. Their repositories SHOULD expose `update` operations.

## 4. Repository Responsibilities
- Repositories are strictly responsible for persistence and retrieval only.
- Business lifecycle logic (e.g., transaction reversal, state transitions) is strictly forbidden in repository contracts.
- Repositories must not expose storage-specific concepts (e.g., Sheets, Rows).
