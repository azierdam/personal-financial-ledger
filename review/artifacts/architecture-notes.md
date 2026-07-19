Architectural Notes: B2.2
- Implemented reusable ValidationEngine separating validation rules from UI rendering.
- Validation logic is separated for unit testing (ValidationEngine.gs).
- Form uses HTML5 novalidate to manage errors via ValidationEngine.
