# Data Model

## Spreadsheet

PersonalFinance

---

## Sheet: Transactions

| Column | Type | Required |
|--------|------|----------|
| ID | String | Yes |
| Date | Date | Yes |
| Type | Enum | Yes |
| Account | String | Yes |
| Category | String | Yes |
| Amount | Number | Yes |
| Currency | String | Yes |
| Merchant | String | No |
| Notes | String | No |
| CreatedAt | Timestamp | Yes |

---

## Sheet: Accounts

| Column | Type |
|--------|------|
| ID | String |
| Name | String |
| Type | Enum |
| Currency | String |
| Balance | Number |

---

## Design Principles

- Immutable transactions
- One row = one financial event
- IDs are generated automatically
- Never edit historical transactions directly