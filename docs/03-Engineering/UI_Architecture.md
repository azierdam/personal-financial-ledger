# UI Architecture

## Overview
The PFL application uses a server-side rendered UI approach using Google Apps Script's `HtmlService`.

## Structure
- `src/ui/`: Contains all HTML templates and styles.
- `src/app/WebApp.gs`: Application entry point and helper functions.
- `Index.html`: The main entry point shell, integrating partials.

## Partials
- `Header.html`: Application header (`.app-header`).
- `Navigation.html`: Main navigation sidebar (`.app-nav`).
- `Dashboard.html`: Placeholder for the dashboard content (`.app-main`).
- `Styles.html`: Application-wide CSS using component-oriented naming (`.app-container`, etc.).

## Pattern
Templates utilize the `include(filename)` helper function in `src/app/WebApp.gs` to inject partials into the main layout.
