/**
 * Integration tests for Sheets Persistence (using mocked SheetsGateway).
 */
function testSheetsPersistence() {
  // Mock Gateway
  const mockGateway = {
    data: [],
    getValues: function(sheet) { return this.data; },
    appendRow: function(sheet, row) { this.data.push(row); }
  };
  
  const accountRepo = new SheetsAccountRepository(mockGateway);
  const acc = new Account('acc1', 'Test Acc');
  accountRepo.save(acc);
  
  const fetchedAcc = accountRepo.findById('acc1');
  if (fetchedAcc.name !== 'Test Acc') throw new Error('Account save/find failed');
}
