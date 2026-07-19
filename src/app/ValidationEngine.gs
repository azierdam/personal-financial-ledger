/**
 * Shared validation logic for both client-side UI and server-side testing.
 */
const ValidationEngine = {
  validate: function(formData) {
    const errors = {};
    
    // Required fields check
    ['date', 'amount', 'description', 'category', 'account'].forEach(field => {
      if (!formData[field]) {
        errors[field] = 'This field is required.';
      }
    });
    
    // Amount check
    if (formData.amount && parseFloat(formData.amount) <= 0) {
      errors.amount = 'Amount must be greater than zero.';
    }
    
    return {
      isValid: Object.keys(errors).length === 0,
      errors: errors
    };
  }
};
