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
  // Test valid routing (explicit template)
  const entryPage = doGet({parameter: {page: 'transactionEntry'}});
  if (!entryPage) {
    throw new Error('Failed to load transaction entry page');
  }
  
  // Test invalid routing (should fallback to default - dashboard)
  const invalidPage = doGet({parameter: {page: 'invalid'}});
  if (!invalidPage) {
    throw new Error('Failed to load dashboard fallback');
  }
}
