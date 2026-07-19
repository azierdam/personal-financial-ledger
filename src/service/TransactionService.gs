/**
 * Application service for coordinating transaction workflows.
 */
class TransactionService {
  /**
   * @param {TransactionRepository} transactionRepository
   */
  constructor(transactionRepository) {
    // Note: TransactionRepository is injected.
    this.transactionRepository = transactionRepository;
  }

  /**
   * Adds a new transaction based on a request.
   * @param {TransactionRequest} transactionRequest
   * @param {Account} account
   * @param {Category} category
   * @returns {Transaction}
   */
  addTransaction(transactionRequest, account, category) {
    if (!(transactionRequest instanceof TransactionRequest)) {
      throw new Error('Invalid TransactionRequest.');
    }
    if (!(account instanceof Account)) {
      throw new Error('Valid Account entity is required.');
    }
    if (!(category instanceof Category)) {
      throw new Error('Valid Category entity is required.');
    }

    try {
      const id = 'TX-' + new Date().getTime();
      const date = new Date();
      const money = new Money(transactionRequest.amount, 'IDR'); // Default currency
      
      const transaction = new Transaction(
        id,
        date,
        money,
        transactionRequest.transactionType,
        category,
        account,
        transactionRequest.description
      );

      this.transactionRepository.save(transaction);
      return transaction;
    } catch (e) {
      throw new Error('Failed to process transaction: ' + e.message);
    }
  }
}
