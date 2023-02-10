---
_db_id: 705
content_type: project
flavours:
  - any_language
ready: true
submission_type: repo
tags:
  - loops
  - functions
  - foundations
  - data structures
title: Shopping cart calculations
---

## Set up your environment

### Javascript

Your directory structure should look like this:

```
├── src
    ├── shopping_cart.js
    └── data.json
```

### Python

Your directory structure should look like this:

```
├── data
    └── data.json
└── src
    └── shopping_cart.py
```

A lot of new programmers don't know why understanding is important. They think they can just copy code from people and that's enough to get by. BUT as soon as you get your first job you'll need to solve some serious problems on your own.

The problems you'll be solving in this project are designed to be realistic. As a professional, you'll likely need to do things similar to this. Please make sure you 100% understand!

## Here's the scenario

Imagine you are working for a hot new online shopping startup. You've seen online shopping, right? Go poke around on Takealot or Amazon if you haven't.

On the online shopping site, users (people who want to buy stuff) navigate around and then add items to their shopping baskets. Once they are happy with their baskets, then they "checkout", pay for their goodies, and await their delivery.

## Why data matters

As a techie, data will be a part of your life. You're going to need to learn how to make this stuff dance.

For data scientists and data engineers, it's pretty obvious why this is the case. But seriously, for any kind of developer, it's friggin important.

Generally, developers need to work on programs that talk to other programs. And programs talk to each other by passing data structures back and forth.

Take a look at this to see how you can see Tilde's data structures:

{{% youtube Jx0jq2SiFS4 %}}

Ideally, you will be able to build stuff at least as complicated as that. But we're going to start with some simpler things.

## Get started with the project by adding the data to your repo

First of all, please **download the data in [this file](data.json) and add it to your repo**. All of your functions should take this data structure as an argument.

If you look at the data you'll see that what we have is a list or array of elements. Each element represents a shopping basket.

Each shopping basket has a few different pieces:

1. email: this is the email address of the customer.
2. status: this can have a few different values:
   1. OPEN means that the person is still busy shopping.
   2. PAID means that the person has paid for the basket in full, they are waiting for delivery.
   3. DELIVERED means that the customer has paid for and received their stuff.
3. items: this is a list/array of all the things that a person added to the basket.

Each item in the shopping basket has a few properties of its own:

1. name: dah
2. quantity: how many of these does the person want to buy?
3. price: This is the price of a single item. The prices are in South African Rands.

For example, if there is an item in the shopping cart that looks like this:

```
{"name": "hamster", "quantity": 2, "price": 20}
```

Then it means that the person is buying 2 hamsters at a price of R20 each. So that's R40 in total.

Please note that one person can have multiple baskets. If you look at the data, you'll see that tshepo@umuzi.org has 4 baskets. Two have been delivered, one has been paid for (so he's awaiting delivery) and one is open (so he's setting up his next order).

## Write some functionality

### Important notes for Javascript solutions

**1. Destructuring**

In Javascript it is best practice to use destructuring when passing arguments to a function. You can learn about destructuring here: [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

Please make sure you use destructuring for all your functions.

```
getCustomerBaskets(shoppingBaskets, "sine@umuzi.org"); // DON'T DO THIS
getCustomerBaskets("sine@umuzi.org", customerBaskets); // DON'T DO THIS EITHER

// The problem with the above code is that if you get the order of the parameters wrong, then things will break. Your functions should work like this instead:

function getCustomerBaskets({ shoppingBaskets, email }) {...}

getCustomerBaskets({shoppingBaskets, email}) //DO THIS
```

**2. Exports**

Export all your functions for the bot to be able access and mark your code. You do this by including an export statement like this.

```
module.exports = { YOUR_FIRST_FUNCTION_NAME, YOUR_SECOND_FUNCTION_NAME,... };
```

### get baskets belonging to a single customer

Write a function called `get customer baskets` that takes in the email address and the data array as arguments and returns a list/array of all the shopping baskets that belong to the customer with that email address.

If the customer has no shopping baskets then return an empty list/array.

e.g.

```
getCustomerBaskets({ email, shoppingBaskets }); //javascript
getCustomerBaskets(email, shoppingBaskets); //java
get_customer_baskets(email, shopping_baskets) // python
```

This kind of data should be returned if `someone@umuzi.org` has only one basket.

```
[
  {
    email: 'someone@umuzi.org',
    status: 'PAID',
    items: [{
        "name": "hamster",
        "quantity": 2,
        "price": 20
      }]
  }
]
```

### get a list of all the customer email addresses

Write a function called `get all customers`, the function should take the data array as an argument and should return a list of sorted customer email addresses. The list must have no duplicates.

e.g.

```
getAllCustomers({ shoppingBaskets }); //javascript
getAllCustomers(shoppingBaskets); //java
get_all_customers(shopping_baskets) // python
```

### list all the items that have been paid for but not yet delivered

Write a function called `required stock`, your function should take the data array as an argument and should return all the items that need to be sent out for delivery.
You need to return data in the correct format. Just include the names and quantities of the items.

e.g.

```
requiredStock({ shoppingBaskets }); //javascript
requiredStock(shoppingBaskets); //java
required_stock(shopping_baskets) //python
```

For example, if one customer paid for 2 hamsters and another customer paid for one hamster and a bag of sawdust then your function should return the following data structure:

```
[
    {"name":"hamster", "quantity": 3},
    {"name": "bag of sawdust", "quantity": 1}
]
```

### Get the total amount spent by a customer

Write a function called `total spent` that takes an email address as an argument and the data array.
The function must return the total amount that the customer has spent up until this time.

e.g.

```
totalSpent({ email, shoppingBaskets }); //javascript
totalSpent(email, shoppingBaskets); //java
total_spent(email, shopping_baskets) //python
```

Note that if a basket has been delivered then it has been paid for.

### Top customers

Write a function called `top customers` that takes the data array as an argument and returns a list/array of all the customers. The result should be ordered according to the total amount spent.
The returned data structure should be an array/list of dictionaries/objects showing the email addresses and the total amounts spent per customer.

e.g.

```
topCustomers({ shoppingBaskets }); // javascript
topCustomers(shoppingBaskets); // java
top_customers(shopping_baskets) //python
```

Make sure the returned value matches the following structure:

```
[
    {"email": "tshepo@umuzi.org", "total": 1023.10},
    {"email": "maru@email.com", "total": 950},
    ... etc
]
```

Hint: You have already defined some functions that would be useful in finding this result. Call those functions.

### customers who have OPEN baskets

Write a function called `get customers with open baskets` that takes in the data array as an argument and returns a sorted list/array of email addresses for customers who have baskets that are open.
e.g.

```
getCustomersWithOpenBaskets({ shoppingBaskets }); //javascript
getCustomersWithOpenBaskets(shoppingBaskets); //java
get_customers_with_open_baskets(shopping_baskets) //python
```

## Notes to reviewers

- The code must be DRY.
- There can be some global constants to help prevent typos. eg `const DELIVERED="DELIVERED"`.
- Functions are supposed to return very specific things.
- All the functions stated above should take in at least one argument, the data array, and should work with similar data.
- **For those using Javascript:** Make sure all their functions functions are exported correctly. Otherwise, the marking bot won't be able to access their code
