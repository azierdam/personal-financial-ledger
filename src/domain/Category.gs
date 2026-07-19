/**
 * Represents a category for financial transactions.
 * Immutable.
 */
class Category {
  /**
   * @param {string} name
   */
  constructor(name) {
    if (typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('Category name must be a non-empty string.');
    }
    this.name = name.trim();
    Object.freeze(this);
  }
}
