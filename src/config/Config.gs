const Config = Object.freeze({
  getSpreadsheetId: () => PropertiesService.getScriptProperties().getProperty('SPREADSHEET_ID'),
  getLedgerSheetName: () => PropertiesService.getScriptProperties().getProperty('LEDGER_SHEET_NAME') || 'Ledger',
  getDefaultCurrency: () => PropertiesService.getScriptProperties().getProperty('DEFAULT_CURRENCY') || 'IDR'
});
