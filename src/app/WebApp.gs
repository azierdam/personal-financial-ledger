/**
 * Navigation configuration.
 */
const PAGES = [
  { id: 'dashboard', label: 'Dashboard' },
  { id: 'transactions', label: 'Transactions' },
  { id: 'categories', label: 'Categories' },
  { id: 'accounts', label: 'Accounts' },
  { id: 'reports', label: 'Reports' },
  { id: 'settings', label: 'Settings' }
];

/**
 * WebApp handles the initial web request and renders the main UI template.
 */
function doGet(e) {
  const page = e.parameter.page || 'dashboard';
  
  // Validate page
  const pageConfig = PAGES.find(p => p.id === page) || PAGES[0];
  
  const template = HtmlService.createTemplateFromFile('src/ui/Index');
  template.page = pageConfig.id;
  template.pages = PAGES;
  
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
