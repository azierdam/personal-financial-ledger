/**
 * Navigation configuration.
 */
const PAGES = [
  { id: 'dashboard', label: 'Dashboard', template: 'Dashboard' },
  { id: 'transactions', label: 'Transactions', template: 'Transactions' },
  { id: 'transactionDetail', label: 'Transaction Details', template: 'TransactionDetail' },
  { id: 'transactionForm', label: 'New Transaction', template: 'TransactionForm' },
  { id: 'categories', label: 'Categories', template: 'Categories' },
  { id: 'accounts', label: 'Accounts', template: 'Accounts' },
  { id: 'reports', label: 'Reports', template: 'Reports' },
  { id: 'settings', label: 'Settings', template: 'Settings' }
];

/**
 * Gets a configured TransactionService.
 */
function getService() {
  const repository = new GoogleSheetsTransactionRepository();
  return new TransactionService(repository);
}

/**
 * Handles transaction form submission.
 */
function processTransactionForm(form) {
  const service = getService();
  const account = new Account('ACC-DEFAULT', 'Default Account');
  const category = new Category('CAT-' + form.category.toUpperCase(), form.category);
  
  if (form.transactionId) {
    // Update
    const transaction = new Transaction(
      form.transactionId,
      new Date(form.date),
      new Money(parseFloat(form.amount), 'IDR'),
      form.type,
      category,
      account,
      form.description
    );
    service.updateTransaction(transaction);
  } else {
    // Create
    const request = new TransactionRequest(
      'manual-entry',
      parseFloat(form.amount),
      form.description,
      form.type
    );
    service.addTransaction(request, account, category);
  }
}

/**
 * Handles transaction deletion.
 */
function deleteTransaction(transactionId) {
  getService().deleteTransaction(transactionId);
}

/**
 * WebApp handles the initial web request and renders the main UI template.
 */
function doGet(e) {
  const pageId = e.parameter.page || 'dashboard';
  
  // Validate page
  const pageConfig = PAGES.find(p => p.id === pageId) || PAGES[0];
  
  const template = HtmlService.createTemplateFromFile('src/ui/Index');
  template.page = pageConfig;
  template.pages = PAGES;
  
  const service = getService();
  
  if (pageId === 'dashboard') {
    template.summary = service.getDashboardSummary();
  } else if (pageId === 'transactions') {
    template.transactions = service.getAllTransactions();
  } else if (pageId === 'transactionDetail') {
    template.transaction = service.getTransactionById(e.parameter.id);
  } else if (pageId === 'transactionForm') {
    if (e.parameter.id) {
      template.transaction = service.getTransactionById(e.parameter.id);
    } else {
      template.transaction = null;
    }
  }
  
  return template
    .evaluate()
    .setTitle('Personal Financial Ledger')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}

/**
 * Include helper for template partials.
 */
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}
