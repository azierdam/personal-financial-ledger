/**
 * Represents an account.
 * Immutable.
 */
class Account {
  /**
   * @param {string} accountId
   * @param {string} name
   */
  constructor(accountId, name) {
    if (typeof accountId !== 'string' || accountId.trim().length === 0) {
      throw new Error('AccountId must be a non-empty string.');
    }
    if (typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('Account name must be a non-empty string.');
    }
    this.accountId = accountId.trim();
    this.name = name.trim();
    Object.freeze(this);
  }
}
