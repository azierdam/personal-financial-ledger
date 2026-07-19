/**
 * Google Sheets implementation of TransactionRepository.
 */
class GoogleSheetsTransactionRepository extends TransactionRepository {
  /**
   * Saves a transaction to the Ledger sheet in Google Sheets.
   * @param {Transaction} transaction
   */
  save(transaction) {
    if (!transaction) {
      throw new Error('Transaction is required.');
    }

    const ss = SpreadsheetApp.openById(Config.SPREADSHEET_ID);
    if (!ss) {
      throw new Error('Could not open spreadsheet with ID: ' + Config.SPREADSHEET_ID);
    }

    const sheet = ss.getSheetByName(Config.LEDGER_SHEET_NAME);
    if (!sheet) {
      throw new Error('Could not find sheet with name: ' + Config.LEDGER_SHEET_NAME);
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
