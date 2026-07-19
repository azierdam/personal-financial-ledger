/**
 * Unit tests for WebApp.
 */
function testWebAppDoGet() {
  const output = doGet({});
  
  // Verify return type
  if (!output || typeof output.getTitle !== 'function') {
    throw new Error('doGet did not return a valid HtmlOutput object');
  }
  
  // Verify default title
  if (output.getTitle() !== 'Personal Financial Ledger') {
    throw new Error('Incorrect title');
  }
}

function testWebAppRouting() {
  // Test valid routing
  const transactionsPage = doGet({parameter: {page: 'transactions'}});
  if (!transactionsPage) {
    throw new Error('Failed to load transactions page');
  }
  
  // Test invalid routing (should fallback to default - dashboard)
  const invalidPage = doGet({parameter: {page: 'invalid'}});
  if (!invalidPage) {
    throw new Error('Failed to load dashboard fallback');
  }
}
