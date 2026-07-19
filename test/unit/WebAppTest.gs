/**
 * Unit tests for WebApp.
 */
function testWebAppDoGet() {
  const output = doGet({});
  
  // Verify return type
  if (!output || typeof output.getTitle !== 'function') {
    throw new Error('doGet did not return a valid HtmlOutput object');
  }
  
  // Verify title
  if (output.getTitle() !== 'Personal Financial Ledger') {
    throw new Error('Incorrect title');
  }
  
  // Verify meta tags (basic check)
  const content = output.getContent();
  if (content.indexOf('viewport') === -1) {
    throw new Error('Missing viewport meta tag');
  }
}
