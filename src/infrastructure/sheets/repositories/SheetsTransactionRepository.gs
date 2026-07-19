class SheetsTransactionRepository {
  constructor(gateway, transactionMapper) {
    this.gateway = gateway;
    this.mapper = transactionMapper;
    this.sheetName = 'Transactions';
  }

  save(transaction) {
    this.gateway.appendRow(this.sheetName, this.mapper.toRow(transaction));
  }

  findById(transactionId) {
    const rows = this.gateway.getValues(this.sheetName);
    const row = rows.find(r => r[0] === transactionId);
    return row ? this.mapper.toDomain(row) : null;
  }

  findAll() {
    const rows = this.gateway.getValues(this.sheetName);
    return rows.map(r => this.mapper.toDomain(r));
  }
}
