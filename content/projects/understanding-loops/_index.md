---
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

TODO: Tilde data demonstration

## Project instructions

### Add the data to your repo

First of all, please download this data in this file and add it to your repo. Generally you would do some clever things to import the data, but for now you can just paste it straight into your code.

If you look at the data you'll see that what we have is a list or array of elements. Each element represents a shopping basket.

Each shopping basket has a few different pieces:
1. email: this is the email address of the customer
2. status: this can have a few differnet values:
   1. OPEN means that the person is still busy shopping
   2. PAID means that the person has paid for the basket in full, they are waiting for delivery
   3. DELIVERED means that the customer has received their stuff
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








