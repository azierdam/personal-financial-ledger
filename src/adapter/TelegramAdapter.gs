/**
 * Orchestrates Telegram webhook payloads into the application layer.
 */
class TelegramAdapter {
  /**
   * Handles incoming Telegram webhook payloads.
   * @param {Object} payload - The raw JSON payload from Telegram.
   */
  static handleWebhook(payload) {
    if (!payload || !payload.message || !payload.message.text) {
      return this._createResponse('Invalid payload', 400);
    }

    try {
      const message = payload.message.text;
      const request = TransactionParser.parse(message);
      
      const repository = new GoogleSheetsTransactionRepository();
      const service = new TransactionService(repository);
      
      service.addTransaction(request);
      
      return this._createResponse('Success', 200);
    } catch (e) {
      return this._createResponse('Error: ' + e.message, 500);
    }
  }

  /**
   * Helper to create GAS response.
   * @param {string} message 
   * @param {number} code 
   */
  static _createResponse(message, code) {
    return ContentService.createTextOutput(JSON.stringify({ message: message, code: code }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
