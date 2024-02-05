---
_db_id: 960
content_type: project
flavours:
  - any_language
from_repo: projects/oop/bank-accounts/part-1
prerequisites:
  hard:
    - projects/oop/bank-accounts/part-1
submission_type: continue_repo
tags:
  - skill/combined_concept_projects
title: Bank accounts - part 2
---

In the last part of this project you created a BankAccount, now it is time to create a Bank.

## Directory structure

### Python

Your directory structure should look like this:

```

├── banking
│   └── bank_account.py
|   └── bank.py
├── setup.py
├── requirements.txt
├── .gitignore
└── tests
  └── ???

```

Please use `pytest` to test your work.

### JavaScript

Your directory structure should look like this:

```
├── spec
|   ├── support
|   |   └── jasmine.json
|   └── ???
├── src
|   └── bank_account.js
|   └── bank.js
└── package.json
```

Please test your work using jasmine.

### Java

Update your directory structure to:

```
...

├── app
|   ├── build.gradle
|   └── src
|       ├── main
|       |   └── java
|       |       └── banking
|       |           ├── BankAccount.java
|       |           └── Bank.java  <---NEW
|       └──test
|          └── java
|               └── banking
|                   ├── ???.java    <-------- names are important
|                   └── ???.java    <-------- names are important
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
└── settings.gradle
...
```

## Instructions

Create a class called `Bank`.

If you have ever opened an account at a bank then you will know that there is a set menu of different types of accounts you can open. You can't just choose your interest rate when you feel like it.

For example, a Bank might allow you to open a current account (with a low interest rate), and a 32-day call account (with a high interest rate).

### Different account types

1. Create a method on your Bank class called `add account type`. This should accept an account type name (string) and an interest rate.

Here is some pseudocode:

```
bank.add_account_type("Saving", 5)
bank.add_account_type("Current",2.5)
bank.add_account_type("Fixed deposit", 8.2)
```

### Opening bank accounts

Now a Bank can manage a lot of bank accounts. It keeps track of all the different bank accounts by associating each account with a unique 10 digit number. This number wont change.

Create a function called `open bank account`. It should have one string parameter, the account type name. The function should return the account number of the new bank account.

The account number should be a string that is 10 characters long. Each character in the string should be a digit.

Here is some pseudocode:

```
savings_account_number = bank.open_bank_account("Saving")
current_account_number = bank.open_bank_account("Current")
```

The bank will need to keep track of which bank account is associated with bank account number.

### Interacting with bank accounts

Create the following functions:

(Please follow the naming conventions for the language you are working in)

- `deposit(bank_account_number, amount)` This will find the BankAccount with the matching bank account number and then deposit the money
- `withdraw(bank_account_number, amount)` This will find the BankAccount with the matching bank account number and then withdraw the money
- `transfer(from_account_number,to_account_number, amount)` This will find the two matching accounts, withdraw some money from one of them, and deposit the money into the other one. Please try to keep your code DRY
- `compound_interest()`: This should compound the interest on all the `Bank Accounts` that the `Bank` controls
- `get_balance(from_account_number)`: This should return the balance of the matching account
- `get_interest_rate(from_account_number)`: This should return the interest rate of the matching account

## Usage Examples

```js
// javascript

const bank = new Bank();
// addAccountType
bank.addAccountType({ accountType: "Savings", interestRate: 5 });
bank.addAccountType({ accountType: "Current", interestRate: 2.5 });

// openBankAccount
const savingsAccountNumber = bank.openBankAccount({ accountType: "Savings" }); // should return a 10 digit account number string
const currentAccountNumber = bank.openBankAccount({ accountType: "Current" }); // - - - 10 digit account number string

// deposit
bank.deposit({ accountNumber: savingsAccountNumber, amount: 1500 });
bank.deposit({ accountNumber: currentAccountNumber, amount: 500 });

// withdraw
bank.withdraw({ accountNumber: savingsAccountNumber, amount: 300 });
bank.withdraw({ accountNumber: currentAccountNumber, amount: 200 });

// transfer
bank.transfer({
  fromAccountNumber: currentAccountNumber,
  toAccountNumber: savingsAccountNumber,
  amount: 200,
});

// getBalance
console.log(bank.getBalance({ accountNumber: savingsAccountNumber })); // should return 1400.00
console.log(bank.getBalance({ accountNumber: currentAccountNumber })); // should return 100.00

// getInterestRate
console.log(bank.getInterestRate({ accountNumber: savingsAccountNumber })); // should return 5
console.log(bank.getInterestRate({ accountNumber: currentAccountNumber })); // should return 2.5

// getCompoundInterest
bank.compoundInterest();
console.log(bank.getBalance({ accountNumber: savingsAccountNumber })); // should return 1405.83
console.log(bank.getBalance({ accountNumber: currentAccountNumber })); // should return 100.21
```

## Tests

Again, please take testing very seriously. Imagine working at an actual bank. How careful would you be if a bug in your code could cost someone their life-savings?
