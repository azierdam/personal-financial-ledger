# Architecture Notes

## Affected Layers
1. **UI Layer (`src/ui/TransactionDetail.html`)**: Triggers `confirmDelete` and calls `google.script.run`.
2. **Controller Layer (`src/app/WebApp.gs`)**: Dispatches the request via `deleteTransaction(id)`.
3. **Service Layer (`src/service/TransactionService.gs`)**: Coordinates business validation and repository delegation.
4. **Repository Layer (`src/repository/GoogleSheetsTransactionRepository.gs`)**: Locates the row matching the ID and deletes the row from Google Sheets.

## Sequence of Calls
```
TransactionDetail.html --(confirmDelete)--> WebApp.gs --(deleteTransaction)--> TransactionService.gs --(delete)--> GoogleSheetsTransactionRepository.gs
```

## Architectural Decisions
- Reused the existing base repository interface by adding the `delete` method.
- Avoided Soft Delete as strictly required by the constraints.
