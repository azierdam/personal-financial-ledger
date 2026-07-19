/**
 * Abstract base class for Transaction repositories.
 * Concrete implementations must extend this class and implement its methods.
 */
class TransactionRepository {
  /**
   * Saves a transaction.
   * @param {Transaction} transaction
   */
  save(transaction) {
    throw new Error('Method not implemented.');
  }
}
