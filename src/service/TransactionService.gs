/**
 * Application service for coordinating transaction workflows.
 */
class TransactionService {
  /**
   * @param {TransactionRepository} transactionRepository
   */
  constructor(transactionRepository) {
    // Note: TransactionRepository is injected.
    this.transactionRepository = transactionRepository;
  }

  /**
   * Adds a new transaction based on a request.
   * @param {TransactionRequest} transactionRequest
   * @param {Account} account
   * @param {Category} category
   * @returns {Transaction}
   */
  addTransaction(transactionRequest, account, category) {
    if (!(transactionRequest instanceof TransactionRequest)) {
      throw new Error('Invalid TransactionRequest.');
    }
    if (!(account instanceof Account)) {
      throw new Error('Valid Account entity is required.');
    }
    if (!(category instanceof Category)) {
      throw new Error('Valid Category entity is required.');
    }

    try {
      const id = 'TX-' + new Date().getTime();
      const date = new Date();
      const money = new Money(transactionRequest.amount, 'IDR'); // Default currency
      
      const transaction = new Transaction(
        id,
        date,
        money,
        transactionRequest.transactionType,
        category,
        account,
        transactionRequest.description
      );

      this.transactionRepository.save(transaction);
      return transaction;
    } catch (e) {
      throw new Error('Failed to process transaction: ' + e.message);
    }
  }

  /**
   * Deletes a transaction.
   * @param {string} transactionId
   */
  deleteTransaction(transactionId) {
    if (!transactionId || typeof transactionId !== 'string') {
      throw new Error('Invalid Transaction ID.');
    }
    
    try {
      this.transactionRepository.delete(transactionId);
    } catch (e) {
      throw new Error('Failed to delete transaction: ' + e.message);
    }
  }

  /**
   * Updates an existing transaction.
   * @param {Transaction} transaction
   */
  updateTransaction(transaction) {
    if (!(transaction instanceof Transaction)) {
      throw new Error('Invalid Transaction.');
    }
    
    try {
      this.transactionRepository.update(transaction);
    } catch (e) {
      throw new Error('Failed to update transaction: ' + e.message);
    }
  }

  /**
   * Retrieves a transaction by its ID.
   * @param {string} transactionId
   * @returns {Transaction|null}
   */
  getTransactionById(transactionId) {
    return this.transactionRepository.findById(transactionId);
  }

  /**
   * Retrieves all transactions.
   * @returns {Transaction[]}
   */
  getAllTransactions() {
    return this.transactionRepository.findAll();
  }

  /**
   * Calculates dashboard summary data.
   * @returns {Object}
   */
  getDashboardSummary() {
    const transactions = this.getAllTransactions();
    
    let totalIncome = 0;
    let totalExpense = 0;
    const monthlySummary = {};

    transactions.forEach(t => {
      if (t.type === 'INCOME') {
        totalIncome += t.amount.amount;
      } else if (t.type === 'EXPENSE') {
        totalExpense += t.amount.amount;
      }

      const monthYear = t.date.toLocaleString('default', { month: 'short', year: 'numeric' });
      if (!monthlySummary[monthYear]) {
        monthlySummary[monthYear] = { income: 0, expense: 0 };
      }
      if (t.type === 'INCOME') {
        monthlySummary[monthYear].income += t.amount.amount;
      } else {
        monthlySummary[monthYear].expense += t.amount.amount;
      }
    });

    return {
      currentBalance: totalIncome - totalExpense,
      totalIncome,
      totalExpense,
      netBalance: totalIncome - totalExpense,
      transactionCount: transactions.length,
      monthlySummary
    };
  }

  /**
   * Searches and filters transactions based on criteria.
   * @param {SearchCriteria} criteria
   * @returns {Transaction[]}
   */
  searchTransactions(criteria) {
    let transactions = this.getAllTransactions();

    if (criteria.description) {
      transactions = transactions.filter(t => t.description.toLowerCase().includes(criteria.description.toLowerCase()));
    }
    if (criteria.transactionType) {
      transactions = transactions.filter(t => t.type === criteria.transactionType);
    }
    if (criteria.category) {
      transactions = transactions.filter(t => t.category.name === criteria.category);
    }
    if (criteria.startDate) {
      transactions = transactions.filter(t => t.date >= criteria.startDate);
    }
    if (criteria.endDate) {
      transactions = transactions.filter(t => t.date <= criteria.endDate);
    }

    return transactions;
  }
}
