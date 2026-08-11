---
content_type: project
flavours:
- none
prerequisites:
  hard:
  - sql/shop-project
  soft: []
from_repo: sql/shop-project
submission_type: continue_repo
tags:
- sql
- skill/databases
ready: true
title: Shop Database using sql - part 2
---

In the last part of this project you created a Shop Database and performed some SQL queries, now it is time to add more queries.

## Instructions

Create a new branch and ensure your repository maintains the same structure with additional new queries.

### Querying a database

Save all queries in the query script created in the previous project (Shop Database using sql).

**NB! Be sure to label your answers by placing the question above the corresponding code. Submitting a wall of code without explanations makes it difficult to review.**

18. Using `DISTINCT`, select all unique cities from the `Customers` table.
19. Select all unique countries from the `Customers` table using `DISTINCT`.
20. From the `Customers` table, use a `CASE` statement to classify each customer (Full Name) as "Local" if they are from "South Africa", otherwise classify them as "International". Use "Classification" as an alias for the result.
21. From the `Orders` table, use a `CASE` statement to determine if each order is "Completed" or "Pending" based on its shipping status. Use "OrderStatus" as an alias for the result.
22. From the `Customers` table, concatenate customer first and last names and select their emails using the aliases `FullName` for the concatenated name and `EmailAddress` for the email.
23. From the `Products` table, list all products with their names and prices, using `Product` for the product name and `Price` for the buying price as aliases.
24. Create a query using `INNER JOIN` to display payment details from `Payments` table alongside the full name of each customer from the `Customers` table. Utilize `p` for `Payments` and `c` for `Customers` as table aliases.
25. Use `INNER JOIN` to join `Orders` with `Employees` table and show order details along with the full name of the employee responsible for each order. Use `o` for `Orders` and `e` for `Employees` as table aliases.

- Ensure the learner has adapted the naming conventions to match those specified in {{< contentlink path="topics/clean-code/sql" >}}