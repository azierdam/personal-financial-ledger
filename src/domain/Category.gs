/**
 * Represents a category for financial transactions.
 * Immutable.
 */
class Category {
  /**
   * @param {string} categoryId
   * @param {string} name
   */
  constructor(categoryId, name) {
    if (typeof categoryId !== 'string' || categoryId.trim().length === 0) {
      throw new Error('CategoryId must be a non-empty string.');
    }
    if (typeof name !== 'string' || name.trim().length === 0) {
      throw new Error('Category name must be a non-empty string.');
    }
    this.categoryId = categoryId.trim();
    this.name = name.trim();
    Object.freeze(this);
  }
}
