/**
 * Defines the contract for Transaction storage.
 * Storage-agnostic interface.
 */
interface TransactionRepository {
  /**
   * @param {Transaction} transaction
   */
  save(transaction);
  
  /**
   * @param {string} transactionId
   * @return {Transaction|null}
   */
  findById(transactionId);
  
  /**
   * @return {Transaction[]}
   */
  findAll();
  
  /**
   * @param {Transaction} transaction
   */
  update(transaction);
  
  /**
   * @param {string} transactionId
   */
  delete(transactionId);
}
