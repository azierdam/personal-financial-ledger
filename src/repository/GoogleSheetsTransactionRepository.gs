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
        transaction.id,
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
}
