/**
 * Integration tests for Transaction persistence flow.
 */
function testTransactionPersistenceFlow() {
  // Mock Repository
  const mockRepo = {
    savedTransaction: null,
    save: function(t) { this.savedTransaction = t; },
    findById: function(id) { return null; },
    findAll: function() { return []; }
  };
  
  const service = new TransactionService(mockRepo);
  const request = new TransactionRequest('command', 100, 'Lunch', TransactionType.EXPENSE);
  const account = new Account('acc1', 'Cash');
  const category = new Category('cat1', 'Food');
  
  const transaction = service.addTransaction(request, account, category);
  
  if (mockRepo.savedTransaction !== transaction) {
    throw new Error('Transaction was not saved to repository');
  }
}
