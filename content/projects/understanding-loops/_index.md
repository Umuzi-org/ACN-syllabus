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

## Language specific notes

### JavaScript

Your directory structure should look like this:

```
└── src
    └──shopping_cart.js
```

#### JavaScript Destructuring

In Javascript it is best practice to use destructuring when passing arguments to a function. You can learn about destructuring here: [destructuring](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment).

Please make sure you use destructuring for all your functions.

Let's say you have a function called getCustomerBaskets that takes an email address and data-structure containing all the shopping baskets as input.

```
// DON'T DEFINE YOUR FUNCTION LIKE THIS
function getCustomerBaskets(allShoppingBaskets, "sine@umuzi.org"){...}

// DON'T CALL YOUR FUNCTION LIKE THIS
getCustomerBaskets("sine@umuzi.org", customerBaskets);

// The problem with the above code is that if you get the order of the parameters wrong, then things will break. Your functions should work like this instead:

// DEFINE YOUR FUNCTION LIKE THIS
function getCustomerBaskets({ email, allShoppingBaskets }) {...}

// YOU CAN CALL IT LIKE THIS
getCustomerBaskets({ email: "sine@umuzi.org", allShoppingBaskets }) //DO THIS
```

#### JavaScript Exports

Make sure you export all your functions using the following format:

```
module.exports = {
    YOUR_FIRST_FUNCTION_NAME,
    YOUR_SECOND_FUNCTION_NAME,...
    };
```

### Java

Your directory structure should look like this:

```
├── build.gradle
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
├── settings.gradle
└── src
    └── main
        └── java
             └── ShoppingCartCalculations.java <------ names are important

```

If the instructions tell you to return a list or array then the correct thing to return is a `List`.

### Python

Your directory structure should look like this:

```
└── shopping_cart
    └── shopping_cart.py
```

## Introduction

A lot of new programmers don't know why understanding is important. They think they can just copy code from people and that's enough to get by. BUT as soon as you get your first job you'll need to solve some serious problems on your own.

The problems you'll be solving in this project are designed to be realistic. As a professional, you'll likely need to do things similar to this. Please make sure you 100% understand!

## Here's the scenario

Imagine you are working for a hot new online shopping startup. You've seen online shopping, right? Go poke around on Takealot or Amazon if you haven't.

On the online shopping site, users (people who want to buy stuff) navigate around and then add items to their shopping baskets. Once they are happy with their baskets, then they "checkout", pay for their goodies, and await their delivery.

## Why data matters

As a techie, data will be a part of your life. You're going to need to learn how to make this stuff dance.

For data scientists and data engineers, it's pretty obvious why this is the case. But seriously, for any kind of developer, it's friggin' important.

Generally, developers need to work on programs that talk to other programs. And programs talk to each other by passing data structures back and forth.

Take a look at this to see how you can see Tilde's data structures:

{{< youtube Jx0jq2SiFS4 >}}

Ideally, you will be able to build stuff at least as complicated as that. But we're going to start with some simpler things.

## Get started with the project by understanding the data format

First of all, please **download the data in [this file](data.json)**. You can use it for testing out your functions.

If you look at the data you'll see that what we have is a list or array of elements. Each element represents a single shopping basket.

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

## Working with JSON files

JSON is a lovely data format because it is easy for humans to read, and machines like it too.

If you are working in **Python** then you can turn the JSON file into a data structure in your code by making use of the [json package](https://docs.python.org/3/library/json.html).

In JavaScript you can simply `require` a JSON file and then it'll get converted into the appropriate data-structure.

In Java you can turn the JSON file into a data structure in your code by making use of [json for java](https://github.com/FasterXML/jackson), [here is a tutorial](https://www.baeldung.com/jackson-object-mapper-tutorial)

## Write some functionality

### Get baskets belonging to a single customer

Write a function called `get customer baskets` that takes in two arguments:

- the email address of a customer
- a list/array of all the shopping baskets

The function must return a list/array of all the shopping baskets that belong to the customer with that email address.

If the customer has no shopping baskets then return an empty list/array.

Different languages have different requirements:

```
getCustomerBaskets({ email, allShoppingBaskets }); // javascript. This should return an array
getCustomerBaskets(email, allShoppingBaskets); // java. This should return a List
get_customer_baskets(email, all_shopping_baskets) // python. This should return a list
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

### Get a list of all the customer email addresses

Write a function called `get all customers`, the function should take the data array as an argument and should return a list of sorted customer email addresses. The list must have no duplicates.

e.g.

```
getAllCustomers({ allShoppingBaskets }); //javascript
getAllCustomers(allShoppingBaskets); //java
get_all_customers(all_shopping_baskets) // python
```

### List all the items that have been paid for but not yet delivered

Write a function called `get required stock`, your function should take the data array as an argument and should return all the items that need to be sent out for delivery.
You need to return data in the correct format. Just include the names and quantities of the items.

e.g.

```
getRequiredStock({ allShoppingBaskets }); //javascript
getRequiredStock(allShoppingBaskets); //java
get_required_stock(all_shopping_baskets) //python
```

For example, if one customer paid for 2 hamsters and another customer paid for one hamster and a bag of sawdust then your function should return the following data structure:

```
[
    {"name": "hamster", "quantity": 3},
    {"name": "bag of sawdust", "quantity": 1}
]
```

### Get the total amount spent by a customer

Write a function called `get total spent` that takes an email address as an argument and the data array.
The function must return the total amount that the customer has spent up until this time.

e.g.

```
getTotalSpent({ email, allShoppingBaskets }); //javascript
getTotalSpent(email, allShoppingBaskets); //java
get_total_spent(email, all_shopping_baskets) //python
```

Note that if a basket has been delivered then it has been paid for.

### Top customers

Write a function called `get top customers` that takes the data array as an argument and returns a list/array of all the customers. The result should be ordered according to the total amount spent.

The returned data structure should be an array/list of dictionaries/objects showing the email addresses and the total amounts spent per customer.

e.g.

```
getTopCustomers({ allShoppingBaskets }); // javascript
getTopCustomers(allShoppingBaskets); // java
get_top_customers(all_shopping_baskets) //python
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

### Get customers who have OPEN baskets

Write a function called `get customers with open baskets` that takes in the data array as an argument and returns a sorted list/array of email addresses for customers who have baskets that are open.
e.g.

```
getCustomersWithOpenBaskets({ allShoppingBaskets }); //javascript
getCustomersWithOpenBaskets(allShoppingBaskets); //java
get_customers_with_open_baskets(all_shopping_baskets) //python
```

## Notes to reviewers

- The code must be DRY.
- There can be some global constants to help prevent typos. eg `const DELIVERED="DELIVERED"`.
- Functions are supposed to return very specific things.
- All the functions stated above should take in at least one argument, the data array, and should work with similar data.
- **For those using Javascript:** Make sure all the functions are exported correctly, otherwise, the marking bot won't be able to access the code.