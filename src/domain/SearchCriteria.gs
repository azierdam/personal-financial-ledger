/**
 * Domain model for transaction search criteria.
 */
class SearchCriteria {
  /**
   * @param {string} [description]
   * @param {string} [transactionType]
   * @param {string} [category]
   * @param {Date} [startDate]
   * @param {Date} [endDate]
   */
  constructor(description = '', transactionType = '', category = '', startDate = null, endDate = null) {
    this.description = description;
    this.transactionType = transactionType;
    this.category = category;
    this.startDate = startDate ? new Date(startDate) : null;
    this.endDate = endDate ? new Date(endDate) : null;
  }
}
