/**
 * Represents a monetary value.
 * Immutable.
 */
class Money {
  /**
   * @param {number} amount
   * @param {string} currency
   */
  constructor(amount, currency) {
    if (typeof amount !== 'number' || !Number.isFinite(amount)) {
      throw new Error('Money amount must be a finite number.');
    }
    if (typeof currency !== 'string' || currency.trim().length === 0) {
      throw new Error('Money currency must be a non-empty string.');
    }

    this.amount = amount;
    this.currency = currency;
    Object.freeze(this);
  }
}
