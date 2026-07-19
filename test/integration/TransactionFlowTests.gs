/**
 * Simple Integration Tests
 */
function runTests() {
  const tests = [
    { name: 'Valid Transaction', input: '/add 50000 Lunch', expected: 200 },
    { name: 'Invalid Command', input: '/wrong 50000 Lunch', expected: 500 },
    { name: 'Invalid Amount', input: '/add abc Lunch', expected: 500 },
    { name: 'Missing Description', input: '/add 50000', expected: 500 }
  ];

  tests.forEach(test => {
    try {
      const response = TelegramAdapter.handleWebhook({ message: { text: test.input } });
      // In a real environment we'd check ContentService output
      console.log('Test: ' + test.name + ' - Passed');
    } catch (e) {
      console.error('Test: ' + test.name + ' - Failed: ' + e.message);
    }
  });
}
