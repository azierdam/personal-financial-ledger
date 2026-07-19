# Infrastructure Architecture

## Overview
The infrastructure layer is responsible for persistence and external system integration, keeping these concerns isolated from the domain layer.

## Google Sheets Implementation
The persistence implementation resides in `src/infrastructure/sheets/`.

### Key Components
- **SheetsGateway**: Provides a lightweight abstraction over `SpreadsheetApp` to prevent direct coupling in repositories.
- **Mappers**: Transform domain objects to/from Sheet rows (e.g., `TransactionMapper`).
- **Repositories**: Concrete implementations of repository contracts (e.g., `SheetsTransactionRepository`) utilizing the Gateway and Mappers.

## Error Handling
All infrastructure-level errors (I/O, malformed data) are wrapped in custom exceptions defined in `src/infrastructure/sheets/Errors.gs` to maintain domain-agnostic interfaces.
