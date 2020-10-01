---
_db_id: 200
available_flavours:
- none
content_type: project
prerequisites:
  hard:
  - topics/intro-to-relational-databases
  - topics/intro-to-docker/
  soft: []
ready: true
story_points: 3
submission_type: repo
tags: []
title: SQL
---

## Installation:

- We are using Postgres
- Instead of installing Postgres on your computer, you can launch it with a docker composition
- MySQL is nice and lot's of people use it in industry, but it doesn't actually implement standard SQL, it sort of does it's own thing a bit. Postgres is a much more standard DB, and industry loooooves it

## Instructions

## Part 1: Creating a database

Save all of your instructions in a script file - you will submit this file on Gnomio and github.

1. Create a database called "Umuzi".

2. Create the following tables in the Umuzi database:

   - Customers
   - Employees
   - Orders
   - Payments
   - Products

3. Create a primary key for each table with auto-increment (make sure you correctly specify the data types, e.g. the ID field should be `int`).

4. Create foreign keys so that every ID in the order table references an existing ID in the tables referenced (e.g., ProductID, EmployeeID, etc).

5. INSERT the records in the tables below into the table you created in step 2.

6. Document what information is stored in your database. Be sure to say what information is kept in what table, and which keys link the records between tables.

### Customers Table

| CustomerID (int) | FirstName (varchar50) | LastName (varchar50) | Gender (varchar) | Address (varchar200)  | Phone (int 10) | Email (varchar100)     | City (varchar20) | Country (varchar50) |
| ---------------- | --------------------- | -------------------- | ---------------- | --------------------- | -------------- | ---------------------- | ---------------- | ------------------- |
| 1                | John                  | Hibert               | Male             | 284 chaucer st        | 084789657      | john@gmail.com         | Johannesburg     | South Africa        |
| 2                | Thando                | Sithole              | Female           | 240 Sect 1            | 0794445584     | thando@gmail.com       | Cape Town        | South Africa        |
| 3                | Leon                  | Glen                 | Male             | 81 Everton Rd,Gillits | 0820832830     | Leon@gmail.com         | Durban           | South Africa        |
| 4                | Charl                 | Muller               | Mal              | 290A Dorset Ecke      | +44856872553   | Charl.muller@yahoo.com | Berlin           | Germany             |
| 5                | Julia                 | Stein                | Female           | 2 Wernerring          | +448672445058  | Js234@yahoo.com        | Frankfurt        | Germany             |

### Employees Table

| EmployeeID (int) | FirstName (varchar50) | LastName (varchar50) | Email (varchar100) | JobTitle (varchar20) |
| ---------------- | --------------------- | -------------------- | ------------------ | -------------------- |
| 1                | Kani                  | Matthew              | mat@gmail.com      | Manager              |
| 2                | Lesly                 | Cronje               | LesC@gmail.com     | Clerk                |
| 3                | Gideon                | Maduku               | m@gmail.com        | Accountant           |

### Orders Table

| OrderId (int) | ProductID (int) | PaymentID (int) | FulfilledByEmployeeID (int) | DateRequired (datetime) | DateShipped (datetime) | Status (varchar20) |
| ------------- | --------------- | --------------- | --------------------------- | ----------------------- | ---------------------- | ------------------ |
| 1             | 1               | 1               | 2                           | 05-09-2018              |                        | Not shipped        |
| 2             | 1               | 2               | 2                           | 04-09-2018              | 03-09-2018             | Shipped            |
| 3             | 3               | 3               | 3                           | 06-09-2018              |                        | Not shipped        |

### Payments Table

| CustomerId (int) | PaymentID (int) | PaymentDate (datetime) | Amount (decimal) |
| ---------------- | --------------- | ---------------------- | ---------------- |
| 1                | 1               | 01-09-2018             | R150.75          |
| 5                | 2               | 03-09-2018             | R150.75          |
| 4                | 3               | 03-09-2018             | R700.60          |

### Products Table

| ProductId (int) | ProductName (varchar100) | Description (varchar300)                                                    | BuyPrice (decimal) |
| --------------- | ------------------------ | --------------------------------------------------------------------------- | ------------------ |
| 1               | Harley Davidson Chopper  | This replica features working kickstand, front suspension, gear-shift lever | R150.75            |
| 2               | Classic Car              | Turnable front wheels, steering function                                    | R550.75            |
| 3               | Sports car               | Turnable front wheels, steering function                                    | R700.60            |

## Part 2: Querying a database

Save all of your instructions in a script file - you will submit this file on Gnomio and github.

7. SELECT ALL records from table Customers.

8. SELECT records only from the name column in the Customers table.

9. Show the name of the Customer whose CustomerID is 1.

10. UPDATE the record for CustomerID = 1 on the Customer table so that the name is "Lerato Mabitso".

11. DELETE the record from the Customers table for customer 2 (CustomerID = 2).

12. Select all unique statuses from the Orders table and get a count of the number of orders for each unique status.

13. Return the MAXIMUM payment made on the PAYMENTS table.

14. Select all customers from the "Customers" table, sorted by the "Country" column.

15. Select all products with a price BETWEEN R100 and R600.

16. Select all fields from "Customers" where country is "Germany" AND city is "Berlin".

17. Select all fields from "Customers" where city is "Cape Town" OR "Durban".

18. Select all records from Products where the Price is GREATER than R500.

19. Return the sum of the Amounts on the Payments table.

20. Count the number of shipped orders in the Orders table.

21. Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).

22. Using INNER JOIN create a query that selects all Payments with Customer information.

23. Select all products that have turnable front wheels.