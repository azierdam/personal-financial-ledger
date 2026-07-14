# Google Sheets Schema

## Purpose

Define the spreadsheet structure for the Personal Finance Ledger (PFL).

---

# Spreadsheet

PersonalFinance

---

# Sheet: Accounts

| Column | Type | Required |
|---------|------|----------|
| AccountID | String | Yes |
| LedgerID | String | Yes |
| Name | String | Yes |
| Type | Enum | Yes |
| Currency | String | Yes |
| Balance | Number | Yes |
| Status | Enum | Yes |

---

# Sheet: Transactions

| Column | Type | Required |
|---------|------|----------|
| TransactionID | String | Yes |
| LedgerID | String | Yes |
| TransactionDate | Date | Yes |
| Type | Enum | Yes |
| AccountID | String | Yes |
| CategoryID | String | Yes |
| Amount | Number | Yes |
| Currency | String | Yes |
| Merchant | String | No |
| Notes | String | No |
| CreatedAt | Timestamp | Yes |
| UpdatedAt | Timestamp | Yes |

---

# Design Principles

- One row represents one financial event.
- Transactions are immutable.
- Relationships use IDs.
- Currency is stored using ISO codes (e.g. IDR, USD).
- LedgerID supports future multi-ledger capability.