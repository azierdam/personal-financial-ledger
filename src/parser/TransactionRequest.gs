/**
 * This object represents parsed user input.
 * It is an application-layer request object.
 * It is NOT a domain entity.
 * Immutable.
 */
class TransactionRequest {
  /**
   * @param {string} command
   * @param {number} amount
   * @param {string} description
   * @param {string} transactionType - TransactionType
   */
  constructor(command, amount, description, transactionType) {
    if (typeof command !== 'string' || command.trim().length === 0) {
      throw new Error('Command must be a non-empty string.');
    }
    if (typeof amount !== 'number' || !Number.isFinite(amount)) {
      throw new Error('Amount must be a finite number.');
    }
    if (typeof description !== 'string' || description.trim().length === 0) {
      throw new Error('Description must be a non-empty string.');
    }
    if (transactionType !== TransactionType.INCOME && transactionType !== TransactionType.EXPENSE) {
      throw new Error('Invalid transaction type.');
    }

    this.command = command;
    this.amount = amount;
    this.description = description;
    this.transactionType = transactionType;
    Object.freeze(this);
  }
}
