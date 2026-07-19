class SheetsAccountRepository {
  constructor(gateway) {
    this.gateway = gateway;
    this.sheetName = 'Accounts';
  }

  save(account) {
    this.gateway.appendRow(this.sheetName, AccountMapper.toRow(account));
  }

  findById(accountId) {
    const rows = this.gateway.getValues(this.sheetName);
    const row = rows.find(r => r[0] === accountId);
    return row ? AccountMapper.toDomain(row) : null;
  }

  findAll() {
    const rows = this.gateway.getValues(this.sheetName);
    return rows.map(r => AccountMapper.toDomain(r));
  }

  update(account) {
    // Implementation deferred
  }
}
