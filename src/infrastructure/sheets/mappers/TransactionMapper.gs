class TransactionMapper {
  constructor(accountRepo, categoryRepo) {
    this.accountRepo = accountRepo;
    this.categoryRepo = categoryRepo;
  }

  toDomain(row) {
    // Row: id, date, amount, currency, type, categoryId, accountId, description
    const account = this.accountRepo.findById(row[6]);
    const category = this.categoryRepo.findById(row[5]);
    
    if (!account) throw new EntityNotFoundException(`Account ${row[6]} not found.`);
    if (!category) throw new EntityNotFoundException(`Category ${row[5]} not found.`);
    
    return new Transaction(
      row[0], 
      new Date(row[1]), 
      new Money(row[2], row[3]), 
      row[4], 
      category, 
      account, 
      row[7]
    );
  }

  toRow(transaction) {
    return [
      transaction.transactionId,
      transaction.date.toISOString(),
      transaction.amount.value,
      transaction.amount.currency,
      transaction.type,
      transaction.category.categoryId,
      transaction.account.accountId,
      transaction.description
    ];
  }
}
