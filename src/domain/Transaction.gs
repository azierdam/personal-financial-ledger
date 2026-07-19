/**
 * Represents a financial transaction.
 * Immutable.
 */
class Transaction {
  /**
   * @param {string} transactionId
   * @param {Date} date
   * @param {Money} amount
   * @param {string} type - TransactionType
   * @param {Category} category
   * @param {Account} account
   * @param {string} description
   */
  constructor(transactionId, date, amount, type, category, account, description) {
    if (typeof transactionId !== 'string' || transactionId.trim().length === 0) {
      throw new Error('TransactionId must be a non-empty string.');
    }
    if (!(date instanceof Date) || isNaN(date.getTime())) {
      throw new Error('Transaction date must be a valid Date object.');
    }
    if (!(amount instanceof Money)) {
      throw new Error('Transaction amount must be an instance of Money.');
    }
    if (type !== TransactionType.INCOME && type !== TransactionType.EXPENSE) {
      throw new Error('Transaction type must be a valid TransactionType.');
    }
    if (!(category instanceof Category)) {
      throw new Error('Transaction category must be an instance of Category.');
    }
    if (!(account instanceof Account)) {
      throw new Error('Transaction account must be an instance of Account.');
    }
    if (typeof description !== 'string') {
      throw new Error('Transaction description must be a string.');
    }

    this.transactionId = transactionId.trim();
    this.date = date;
    this.amount = amount;
    this.type = type;
    this.category = category;
    this.account = account;
    this.description = description.trim();
    Object.freeze(this);
  }
}
