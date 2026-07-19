/**
 * Google Sheets implementation of TransactionRepository.
 */
class GoogleSheetsTransactionRepository extends TransactionRepository {
  /**
   * Saves a transaction to the Ledger sheet in Google Sheets.
   * @param {Transaction} transaction
   */
  save(transaction) {
    if (!(transaction instanceof Transaction)) {
      throw new Error('Invalid transaction.');
    }

    const spreadsheetId = Config.getSpreadsheetId();
    if (!spreadsheetId) {
      throw new Error('Spreadsheet ID not configured.');
    }

    const ss = SpreadsheetApp.openById(spreadsheetId);
    if (!ss) {
      throw new Error('Could not open spreadsheet with ID: ' + spreadsheetId);
    }

    const sheetName = Config.getLedgerSheetName();
    const sheet = ss.getSheetByName(sheetName);
    if (!sheet) {
      throw new Error('Could not find sheet with name: ' + sheetName);
    }

    try {
      sheet.appendRow([
        transaction.transactionId,
        transaction.date,
        transaction.type,
        transaction.category.name,
        transaction.amount.amount,
        transaction.amount.currency,
        transaction.description
      ]);
    } catch (e) {
      throw new Error('Failed to append transaction to Google Sheets: ' + e.message);
    }
  }

  /**
   * Finds a transaction by its ID.
   * @param {string} transactionId
   * @return {Transaction|null}
   */
  findById(transactionId) {
    const transactions = this.findAll();
    return transactions.find(t => t.transactionId === transactionId) || null;
  }

  /**
   * Retrieves all transactions.
   * @return {Transaction[]}
   */
  findAll() {
    const spreadsheetId = Config.getSpreadsheetId();
    const ss = SpreadsheetApp.openById(spreadsheetId);
    const sheetName = Config.getLedgerSheetName();
    const sheet = ss.getSheetByName(sheetName);
    const data = sheet.getDataRange().getValues();
    
    // Skip header row
    const rows = data.slice(1);
    
    return rows.map(row => {
      // row[0] ID, row[1] Date, row[2] Type, row[3] CategoryName, row[4] Amount, row[5] Currency, row[6] Description
      const category = new Category('CAT-' + row[3], row[3]);
      const account = new Account('ACC-DEFAULT', 'Default Account'); // TODO: Support accounts
      const money = new Money(row[4], row[5]);
      
      return new Transaction(
        row[0],
        new Date(row[1]),
        money,
        row[2],
        category,
        account,
        row[6]
      );
    });
  }
}
