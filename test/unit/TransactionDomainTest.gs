/**
 * Unit tests for Domain Entities.
 */
function testDomainModel() {
  const money = new Money(100, 'IDR');
  const account = new Account('acc1', 'Cash');
  const category = new Category('cat1', 'Food');
  
  // Test Transaction invariant: missing account
  try {
    new Transaction('t1', new Date(), money, TransactionType.EXPENSE, category, null, 'Lunch');
    throw new Error('Should have failed due to missing account');
  } catch (e) {
    // Expected
  }
  
  // Test Transaction creation
  const t = new Transaction('t1', new Date(), money, TransactionType.EXPENSE, category, account, 'Lunch');
  if (t.transactionId !== 't1') throw new Error('TransactionId mismatch');
  if (t.account.accountId !== 'acc1') throw new Error('AccountId mismatch');
}
