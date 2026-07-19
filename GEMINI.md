# PFL Project Instructions

This file contains team-shared architecture, conventions, and workflows for the Personal Financial Ledger (PFL) repository.

## Engineering Standards
All AI contributors MUST adhere to the [AI Engineering Playbook](docs/03-Engineering/).

## UI Development Convention
- **Approach**: Server-side rendered UI using Google Apps Script's `HtmlService`.
- **Structure**: All UI templates reside in `src/ui/`.
- **Layout**: `src/ui/Index.html` is the main entry point (shell).
- **Partials**: Use the `include(filename)` helper function in `WebAppAdapter.gs` to inject partials (e.g., `Header`, `Navigation`) into the main layout.
- **Styling**: Styles are defined in partials (e.g., `src/ui/Styles.html`) and included in the `Index.html` head.
