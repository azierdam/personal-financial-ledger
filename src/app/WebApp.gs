/**
 * Navigation configuration.
 */
const PAGES = [
  { id: 'dashboard', label: 'Dashboard', template: 'Dashboard' },
  { id: 'transactions', label: 'Transactions', template: 'Transactions' },
  { id: 'transactionEntry', label: 'New Transaction', template: 'TransactionEntry' },
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
 * WebApp handles the initial web request and renders the main UI template.
 */
function doGet(e) {
  const pageId = e.parameter.page || 'dashboard';
  
  // Validate page
  const pageConfig = PAGES.find(p => p.id === pageId) || PAGES[0];
  
  const template = HtmlService.createTemplateFromFile('src/ui/Index');
  template.page = pageConfig;
  template.pages = PAGES;
  
  if (pageId === 'transactions') {
    template.transactions = getService().getAllTransactions();
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
