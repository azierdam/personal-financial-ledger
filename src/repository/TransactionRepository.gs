/**
 * Defines the contract for Transaction storage.
 * Storage-agnostic interface.
 */
class TransactionRepository {
  /**
   * @param {string} transactionId
   */
  delete(transactionId) { throw new Error('Not implemented'); }
  
  /**
   * @param {Transaction} transaction
   */
  save(transaction) { throw new Error('Not implemented'); }
  
  /**
   * @param {Transaction} transaction
   */
  update(transaction) { throw new Error('Not implemented'); }
  
  /**
   * @param {string} transactionId
   * @return {Transaction|null}
   */
  findById(transactionId) { throw new Error('Not implemented'); }
  
  /**
   * @return {Transaction[]}
   */
  findAll() { throw new Error('Not implemented'); }
}
