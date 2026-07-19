Architectural Notes: C1.2
- Standardized repository contract: [EntityName]Repository.
- TransactionRepository immutable (only save, findById, findAll).
- Account/CategoryRepository mutable (save, findById, findAll, update).
