# Domain Model

## Objective

Define the core business entities of the Personal Finance Ledger (PFL).

This document is implementation-independent.

---

# Future Aggregate: Ledger
The Ledger is the future root aggregate containing:
- Accounts
- Categories
- Transactions

---

# Core Principles

- Every financial event is recorded as a Transaction.
- Accounts hold balances.
- Categories classify transactions.
- Budgets monitor spending.
- Assets and Liabilities determine net worth.

---

# Entities

## Account

Represents where money is stored.

Examples

- Cash
- Bank Account
- E-Wallet
- Credit Card

---

## Transaction

Represents a financial event.

Examples

- Expense
- Income
- Transfer

---

## Category

Classifies a transaction.

Examples

- Food
- Salary
- Transport
- Investment

---

## Budget

Represents a spending limit for a category or period.

---

## Asset

Represents something owned that has value.

Examples

- Cash
- Savings
- Investments

---

## Liability

Represents money owed.

Examples

- Credit Card
- Loan

---

# Relationships

Account
    ↑
Transaction
    ↓
Category

Budget
    ↓
Category

Asset
    ↑
Account

Liability
    ↑
Account