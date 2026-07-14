# Telegram Commands

## Purpose

Define the Telegram interface for the Personal Finance Ledger (PFL) MVP.

---

# Commands

## /expense

Record an expense.

Example

/expense 75000 Food Lunch

---

## /income

Record an income.

Example

/income 5000000 Salary July

---

## /transfer

Transfer money between accounts.

Example

/transfer Cash BCA 250000

---

## /balance

Display current account balances.

Example

/balance

---

## /report

Display monthly financial summary.

Example

/report July

---

## /help

Display all available commands.

Example

/help

---

# Design Principles

- Commands should be simple.
- Every command returns a clear confirmation or error.
- AI interpretation is used only when structured commands cannot be parsed.