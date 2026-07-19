/**
 * Gateway for SpreadsheetApp interactions.
 */
class SheetsGateway {
  constructor(spreadsheetId) {
    this.ss = SpreadsheetApp.openById(spreadsheetId);
  }

  getValues(sheetName) {
    try {
      const sheet = this.ss.getSheetByName(sheetName);
      if (!sheet) throw new MissingWorksheetException(`Sheet ${sheetName} not found.`);
      return sheet.getDataRange().getValues();
    } catch (e) {
      if (e instanceof MissingWorksheetException) throw e;
      throw new SpreadsheetIOException(e.message);
    }
  }

  appendRow(sheetName, row) {
    try {
      const sheet = this.ss.getSheetByName(sheetName);
      if (!sheet) throw new MissingWorksheetException(`Sheet ${sheetName} not found.`);
      sheet.appendRow(row);
    } catch (e) {
      if (e instanceof MissingWorksheetException) throw e;
      throw new SpreadsheetIOException(e.message);
    }
  }
}
