---
_db_id: 229
available_flavours:
- any_language
content_type: project
ready: true
submission_type: repo
title: Bank Accounts
---

As usual: TDD please

## part 1: Bank Account

A Bank Account has a balance, an interest rate and a monthly fee.

For example if a person has an interest rate of 12% (which is totally unrealistic but make the numbers easier) and they have R1000 in their bank account then they will receive (R1000 x 12% / 12) after one month of saving. That means they earned R10 in interest. Now if their monthly fee on that account is R50 then their final balance after 1 month is R1000+R10-R50 = R960.

- Create a class called `BankAccount`. it should be constructed with the necessary parameters described above.
- add a function to your bank account class called `finishMonth`(js) or `finish_month`(python). This function should update the `balance` accordingly
- The `balance` of a bank account can also change if a deposit or withdrawal is made. Create a function called `deposit` and another one called `withdraw`

## part 2: Bank

Create a class called `Bank`. A `Bank` contains many bank accounts. A bank associates each bank account with a 10 digit number known as a bank account number. In OOP, this is called encapsulation.

Create the following functions on your `Bank` class:

JavaScript:

- `withdraw(bankAccountNumber,amount)`
- `deposit(bankAccountNumber,amount)`
- `transfer(fromBankAccountNumber,toBankAccountNumber, amount)`

Python:

- `withdraw(bank_account_number,amount)`
- `deposit(bank_account_number,amount)`
- `transfer(from_bank_account_number,to_bank_account_number, amount)`

## Part 3: Customers

This part is a little bit advanced. Stop and think before you write any code. Have a plan. Maybe even draw a picture of your plan

Create a class called `Customer`. A customer can be associated with multiple bank accounts. Each customer also has a secret password. The customer should be able to update their password through use of a `setPassword`(js) or `set_password`(python) function.

Whenever money is taken out of a bank account then the relevent customer's secret password must be checked. You don't need a special password when depositing money.

Update your `Bank` functions to be like this:

JavaScript:

- `withdraw(bankAccountNumber,amount,secretPassword)`
- `deposit(bankAccountNumber,amount)`
- `transfer(fromBankAccountNumber,toBankAccountNumber,amount,secretPassword)`

Python:

- `withdraw(bank_account_number,amount,secret_password)`
- `deposit(bank_account_number,amount)`
- `transfer(from_bank_account_number,to_bank_account_number,amount,secret_password)`

If a password is required and the wrong one is provided then raise an error that says `wrong password`.

For now just keep it simple. Just store Customer's passwords in plain text in a variable on the appropriate object. Of course in real life, password managment and storage is kinda tricky. [Here](https://blog.mozilla.org/webdev/2012/06/08/lets-talk-about-password-storage/)'s a nice article from Mozilla that will give you some background on how to do it the right way.