# Apps Script Architecture

## Purpose

Define the Google Apps Script components for the Personal Finance Ledger (PFL).

---

# Architecture

Telegram
    │
    ▼
Webhook (doPost)
    │
    ▼
Router
    │
    ├── Expense Handler
    ├── Income Handler
    ├── Transfer Handler
    ├── Balance Handler
    └── Report Handler
    │
    ▼
Business Services
    │
    ├── TransactionService
    ├── AccountService
    └── ReportService
    │
    ▼
Google Sheets

---

# Project Structure

/src
    webhook.gs
    router.gs
    transaction.gs
    account.gs
    report.gs
    sheet.gs
    telegram.gs
    utils.gs

---

# Design Principles

- One responsibility per file.
- Business logic is separated from Telegram.
- Google Sheets access is centralized.
- Every handler returns a standard response.