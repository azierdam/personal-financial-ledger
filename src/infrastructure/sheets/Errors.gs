/**
 * Infrastructure-specific exceptions.
 */
class EntityNotFoundException extends Error { constructor(message) { super(message); this.name = 'EntityNotFoundException'; } }
class DuplicateEntityException extends Error { constructor(message) { super(message); this.name = 'DuplicateEntityException'; } }
class MissingWorksheetException extends Error { constructor(message) { super(message); this.name = 'MissingWorksheetException'; } }
class MalformedDataException extends Error { constructor(message) { super(message); this.name = 'MalformedDataException'; } }
class SpreadsheetIOException extends Error { constructor(message) { super(message); this.name = 'SpreadsheetIOException'; } }
