# AI Implementation Standard

## Coding Standards
- Adhere to the established Apps Script style and conventions.
- Use explicit types and idiomatic constructs.
- Avoid "hidden" logic or workarounds.

## Architecture Rules
- Strictly maintain domain/repository/service layer boundaries.
- Adhere to the defined domain model (`docs/01-Architecture/Domain_Model.md`).

## Documentation Synchronization
- Any change to the system must be reflected in the relevant documentation (`docs/` folder or pack-specific docs).

## Error Handling
- Use consistent, descriptive error handling.
- Log appropriately, ensuring no sensitive data exposure.

## Maintainability
- Reuse existing services and components before creating new ones.
- Follow the DRY (Don't Repeat Yourself) principle.
- Avoid overengineering; keep solutions simple and focused on the requirements.
