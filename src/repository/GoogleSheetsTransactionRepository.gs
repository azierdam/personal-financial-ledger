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
   * Deletes a transaction from the Ledger sheet.
   * @param {string} transactionId
   */
  delete(transactionId) {
    const spreadsheetId = Config.getSpreadsheetId();
    const sheetName = Config.getLedgerSheetName();
    const ss = SpreadsheetApp.openById(spreadsheetId);
    const sheet = ss.getSheetByName(sheetName);
    const data = sheet.getDataRange().getValues();

    // Find row index (header is row 1)
    let rowIndex = -1;
    for (let i = 1; i < data.length; i++) {
      if (data[i][0] === transactionId) {
        rowIndex = i + 1; // Spreadsheet rows are 1-indexed
        break;
      }
    }

    if (rowIndex === -1) {
      throw new Error('Transaction not found: ' + transactionId);
    }

    try {
      sheet.deleteRow(rowIndex);
    } catch (e) {
      throw new Error('Failed to delete transaction from Google Sheets: ' + e.message);
    }
  }

  /**
   * Updates a transaction in the Ledger sheet.

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
