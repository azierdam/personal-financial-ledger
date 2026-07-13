# User Journey - Record Expense

## Goal

Record an expense in less than 30 seconds.

## Trigger

User sends a message to the Telegram bot.

## Example

/expense

or

Lunch 75000

## Flow

User
    ↓
Telegram Bot
    ↓
AI interprets the message
    ↓
Validate data
    ↓
Store transaction
    ↓
Update account balance
    ↓
Return confirmation

## Required Data

- Amount
- Category
- Account
- Date

## Optional Data

- Merchant
- Notes
- Tags
- Receipt

## Success

Expense recorded successfully.

## Failure

Missing amount.

Missing account.

Unknown category.