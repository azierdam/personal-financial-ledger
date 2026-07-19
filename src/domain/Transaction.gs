/**
 * Represents a financial transaction.
 * Immutable.
 */
class Transaction {
  /**
   * @param {string} id
   * @param {Date} date
   * @param {Money} amount
   * @param {string} type - TransactionType
   * @param {Category} category
   * @param {string} description
   */
  constructor(id, date, amount, type, category, description) {
    if (typeof id !== 'string' || id.trim().length === 0) {
      throw new Error('Transaction id must be a non-empty string.');
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
    if (typeof description !== 'string') {
      throw new Error('Transaction description must be a string.');
    }

    this.id = id;
    this.date = date;
    this.amount = amount;
    this.type = type;
    this.category = category;
    this.description = description;
    Object.freeze(this);
  }
}
