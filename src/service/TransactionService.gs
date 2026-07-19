/**
 * Application service for coordinating transaction workflows.
 */
class TransactionService {
  /**
   * @param {TransactionRepository} transactionRepository
   */
  constructor(transactionRepository) {
    if (!(transactionRepository instanceof TransactionRepository)) {
      throw new Error('Valid TransactionRepository dependency is required.');
    }
    this.transactionRepository = transactionRepository;
  }

  /**
   * Adds a new transaction based on a request.
   * @param {TransactionRequest} transactionRequest
   * @returns {Transaction}
   */
  addTransaction(transactionRequest) {
    if (!(transactionRequest instanceof TransactionRequest)) {
      throw new Error('Invalid TransactionRequest.');
    }

    try {
      const id = 'TX-' + new Date().getTime();
      const date = new Date();
      const money = new Money(transactionRequest.amount, Config.getDefaultCurrency()); // Default currency
      const category = new Category('General'); // Default category
      
      const transaction = new Transaction(
        id,
        date,
        money,
        transactionRequest.transactionType,
        category,
        transactionRequest.description
      );

      this.transactionRepository.save(transaction);
      return transaction;
    } catch (e) {
      throw new Error('Failed to process transaction: ' + e.message);
    }
  }
}
