---
_db_id: 276
available_flavours:
- any_language
content_type: project
pre: '<b>MEDIUM: </b>'
ready: true
submission_type: repo
title: Resturaunt menu system
---

Create an OOP program that can be used to represent and manage a resturaunt's menu.

- The menu contains items
- Each item can come in different sizes, the sizes have different prices. Eg you might want to order a small pizza or a large pizza
- Items have names and descriptions
- Items have different categories (eg: pizzas, hamburgers, drinks)
- Item's can have different tags. Eg vegetarian, vegan, chef's choice, new, spicey

Different kinds of people need to interact with the menu in different ways:

- everyone needs to be able to view the menu
- The resturaunt manager needs to be able to add/edit/delete everything on the menu

Can you think of any other people who might want to interact with the menu? And how they might interact?

## Instructions

### 1. Draw the class hierarchy

Before you start writing any code, draw a picture of your classes and how they interact. Are you making use of inheritance? What Objects contain other objects? You will be expected to be able to explain your class hierarchy so please take care.

If you are running linux then there's a simple tool called `dia` that is quite useful for these kinds of diagrams. `sudo apt install dia`.

### 2. Code the class hierarchy

Then code up your class hierarchy. Note that at this point in the process there is no functionality exposed. There is no frontend or user interface. The only functions you have are constructors.

If you are doing this in JS then this program

### 3. Resturaunt Manager functions

Create the functionality that the resturaunt manager would need. This functionality should be developed in a TDD way.

The following functionality should be exposed:

- create/delete/list/edit categories
- create/delete/list/edit tags
- create/delete/list/edit menu items

This functionality will eventually be accessable through a user interface. Take some time to think abou that user interface. How would a manager want to interact with it? How will these functions get called? What information will be required at each point?

### 4. Now for the Customers

- Customers should be able to create orders
- An order is composed of a bunch of menu items (or specific sizes)
- menu items can be added to the order at any point
- menu items can be removed from the order at any point

1. Update your class diagrams to show this new information
2. Code the necessary classes
3. Create the following functions:

```
order_instance.add_item(???)
order_instance.remove_item(???)
order_instance.get_total_price()
```

## Additional Resources

- {{% contentlink path="topics/basic-architecture-concepts" %}}