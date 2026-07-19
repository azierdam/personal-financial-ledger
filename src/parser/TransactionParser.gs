const SupportedCommands = Object.freeze({
  ADD: '/add'
});

/**
 * Parses raw user input into TransactionRequest objects.
 */
class TransactionParser {
  /**
   * Parses a command string.
   * @param {string} input
   * @returns {TransactionRequest}
   */
  static parse(input) {
    if (!input || typeof input !== 'string') {
      throw new Error('Input must be a non-empty string.');
    }

    const parts = input.trim().split(/\s+/);
    const command = parts[0];

    if (command !== SupportedCommands.ADD) {
      throw new Error('Invalid command. Expected ' + SupportedCommands.ADD + '.');
    }

    if (parts.length < 3) {
      throw new Error('Invalid format. Expected: ' + SupportedCommands.ADD + ' [amount] [description]');
    }

    const amountRaw = parts[1];
    const amount = Number(amountRaw);
    if (!Number.isFinite(amount)) {
      throw new Error('Invalid amount.');
    }
    if (amount <= 0) {
      throw new Error('Amount must be positive.');
    }

    const description = parts.slice(2).join(' ');
    
    return new TransactionRequest(command, amount, description, TransactionType.EXPENSE);
  }
}
