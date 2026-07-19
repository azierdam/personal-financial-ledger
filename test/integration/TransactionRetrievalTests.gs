/**
 * Integration tests for Transaction retrieval flow.
 */
function testTransactionRetrievalFlow() {
  // Create test data
  const testTransaction = new Transaction(
    'TX-123',
    new Date(),
    new Money(100, 'IDR'),
    TransactionType.EXPENSE,
    new Category('CAT-Food', 'Food'),
    new Account('ACC-Cash', 'Cash'),
    'Lunch'
  );

  // Mock Repository
  const mockRepo = {
    transactions: [testTransaction],
    save: function(t) { this.transactions.push(t); },
    findById: function(id) { return this.transactions.find(t => t.transactionId === id) || null; },
    findAll: function() { return this.transactions; }
  };
  
  const service = new TransactionService(mockRepo);
  
  // Test findAll
  const all = service.getAllTransactions();
  if (all.length !== 1 || all[0].transactionId !== 'TX-123') {
    throw new Error('getAllTransactions failed');
  }
  
  // Test findById
  const found = service.getTransactionById('TX-123');
  if (!found || found.transactionId !== 'TX-123') {
    throw new Error('getTransactionById failed');
  }
}
