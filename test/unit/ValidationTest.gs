/**
 * Unit tests for ValidationEngine.
 */
function testValidationEngine() {
  // Test valid data
  const validData = {
    date: '2026-07-20',
    amount: '100',
    description: 'Coffee',
    category: 'food',
    account: 'cash'
  };
  const resultValid = ValidationEngine.validate(validData);
  if (!resultValid.isValid) {
    throw new Error('Validation failed for valid data');
  }

  // Test invalid data (missing required)
  const invalidData = {
    date: '',
    amount: '100',
    description: '',
    category: '',
    account: ''
  };
  const resultInvalid = ValidationEngine.validate(invalidData);
  if (resultInvalid.isValid) {
    throw new Error('Validation passed for invalid data');
  }
  
  // Test invalid amount
  const invalidAmount = { ...validData, amount: '-10' };
  const resultAmount = ValidationEngine.validate(invalidAmount);
  if (resultAmount.isValid || !resultAmount.errors.amount) {
    throw new Error('Validation passed for negative amount');
  }
}
