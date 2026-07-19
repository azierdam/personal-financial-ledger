# UI Architecture

## Overview
The PFL application uses a server-side rendered UI approach using Google Apps Script's `HtmlService`.

## Structure
- `src/ui/`: Contains all HTML templates and styles.
- `src/app/WebApp.gs`: Application entry point, routing logic, and helper functions.
- `Index.html`: The main entry point shell, integrating partials.

## Routing
Routing is handled by passing a `page` query parameter to the `doGet` function (e.g., `?page=transactions`).
The `WebApp.gs` validates the requested page against the `PAGES` configuration array and renders the corresponding template partial.

## Pages
- `Dashboard.html`: Default view.
- `Transactions.html`
- `Categories.html`
- `Accounts.html`
- `Reports.html`
- `Settings.html`

## Partials
- `Header.html`: Application header (`.app-header`).
- `Navigation.html`: Main navigation sidebar with dynamic active state handling (`.app-nav`).
- `Styles.html`: Application-wide CSS using component-oriented naming (`.app-container`, etc.).

## Pattern
Templates utilize the `include(filename)` helper function in `src/app/WebApp.gs` to inject partials into the main layout.
Navigation is generated dynamically from the `PAGES` constant in `WebApp.gs`.
