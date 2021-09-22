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

A lot of noob programmers don't know why understanding is important. They think they can just copy code from people and that's enough to get by. BUT as soon as you get your first job you'll need to solve some serious problems on your own.

The problems you'll be solving in this project are designed to be realistic. As a professional you'll likely need to do things similar to this. Please make sure you 100% understand!

## Here's the scenario

Imagine you are working for a hot new online shopping startup. You've seen online shopping, right? Go poke around on Takealot or Amazon if you haven't.

On the online shopping site, users (people who want to buy stuff) navigate around and then add items to their shopping baskets. Once they are happy with their baskets then they "checkout", pay for their goodies, and await their delivery.

## Why data matters

As any kind of techie, data will be a part of your life. You're going to need to learn how to make this stuff dance.

For data-scientists and data-engineers it's pretty obvious why this is the case. But seriously, for any kind of developer it's friggin important.

Generally developers need to work on programs that talk to other programs. And programs talk to each other by passing data structures back and forth.

Take a look at this to see how you can see Tilde's data structures:

{{% youtube Jx0jq2SiFS4 %}}

Ideally you will be able to build stuff at least as complicated as that. But we'e going to start with some simpler things.
## Get started with the project by addding the data to your repo

First of all, please download this data in [this file](data.json) and add it to your repo.

Generally you would do some clever things to import the data, but for now you can just paste it straight into your code as a global variable.

Please note: Generally, global variables are considered bad. For this project it's ok because we just want you to focus on getting the fuctionality to work.

If you look at the data you'll see that what we have is a list or array of elements. Each element represents a shopping basket.

Each shopping basket has a few different pieces:
1. email: this is the email address of the customer
2. status: this can have a few differnet values:
   1. OPEN means that the person is still busy shopping
   2. PAID means that the person has paid for the basket in full, they are waiting for delivery
   3. DELIVERED means that the customer has paid for and received their stuff
3. items: this is a list/array of all the things that a person added to the basket

Each item in the shopping basket has a few properties of its own:
1. name: dah
2. quantity: how many of these does the person want to buy?
3. price: This is the price of a single item. The prices are in South African Rands

For example if there is an item in the shopping cart that looks like this:
```
{"name": "hamster", "quantity": 2, "price": 20}
```
Then it means that the person is buying 2 hamsters at a price of R20 each. So that's R40 in total.

## Write some functionality

### get baskets belonging to a single customer

Write a function called `get customer baskets` that has an email address as an argument and returns a list/array of all the shopping baskets that belong to the customer with that email address.

If the customer has no shopping baskets then return an empty list/array.

### get a list of all the customer email addresses

Write a function called `get all customers` that returns a list of customer email addresses. The list must have no duplicates.

### list all the items that have been paid for but not yet delivered

Write a function called `required stock` that gets all the items that need to be sent out to delivery.

You need to return data in the correct format. Just include the names and quantities of the items.

Eg: if one customer paid for 2 hamsters and another customer paid for one hamster and a bag of sawdust then your function should return the following data structure:

```
[
    {"name":"hamster", "quantity": 3},
    {"name": "bag of sawdust", "quantity" 1}
]
```

### Get the total amount spent by a customer

Write a function called `total spent` that takes an email address as an argument.

The function must return the total amount that the customer has spent up until this time.

Note that if a basket has been delivered then it has been paid for.

### Top customers

Write a function called `top customers` that returns a list/array of all the customers. The result should be ordered according to total amount spent.

The returned data structure should be an array/list of dictionaries/objects showing the email addresses and the total amounts spent per customer.

Make sure the returned value matches the following structure:

```
[
    {"email": "tshepo@umuzi.org", "total": 1023.10},
    {"email": "maru@email.com", "total":950},
    ... etc
]
```

Hint: You have already defined some functions that would be useful in finding this result. Call those functions.


### customers who have OPEN baskets

Write a function called `get customers with open baskets` that returns a list/array of email addresses for customers who have baskets that are open.
## Notes to reviewers

- the code must be DRY
- having the main data structure as a global is ok, but there shouldn't be other global variables
- there can be some global constants to help prevent typos. eg `const DELIVERED="DELIVERED"`
- functions are supposed to return very specific things