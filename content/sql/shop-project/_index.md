---
_db_id: 200
content_type: project
flavours:
- none
learning_outcomes:
- sql_docker_composition
- sql_one_to_one_relationship
- sql_one_to_many_relationship
- sql_many_to_many_relation
- sql_query_data_with_join
- sql_query_data_with_group_by
prerequisites:
  hard:
  - topics/solo-learn/sql/4-challenges
  - docker/intro-to-docker/
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- sql
title: Shop Database using sql
---

## Installation:

- We are using Postgres
- Instead of installing Postgres on your computer, you can launch it with a docker composition
- MySQL is nice and lots of people use it in industry, but it doesn't implement standard SQL, it sort of does its own thing a bit. Postgres is a much more standard DB, and the industry loooooves it

## Structure:

- Your repository should have a **.yml** file
- Your repository should have **.sql** files
- The different SQL commands should be saved in different descriptive script files i.e.
  - when the reviewer is looking for the commands you used for creating the database they should be able to navigate to a file named **create-database.sql**,
  - navigate to a file named **create-tables.sql** for the commands used to create the database tables, and
  - navigate to the files that contain the commands used for inserting table records and querying the database

## Instructions

## Part 1: Creating a database

Save all of your instructions in script files - you will submit these files on Github.

1. Create a database called "shop".

2. Create the following tables in the shop database:

   - Customers
   - Employees
   - Orders
   - Payments
   - Products

3. Create a primary key for each table with auto-increment (make sure you correctly specify the data types, e.g. the ID field should be `int`).

4. Create foreign keys so that every ID in the order and payment tables references an existing ID in the tables referenced (e.g., ProductID, EmployeeID, etc).

5. INSERT the records in the tables below into the table you created in step 2.

6. Document what information is stored in your database. Be sure to say what information is kept in what table, and which keys link the records between tables. This file needs to be in a `.md` format.

### Customers Table

| ID (int) | FirstName (varchar50) | LastName (varchar50) | Gender (varchar) | Address (varchar200)  | Phone (varchar 20) | Email (varchar100)     | City (varchar20) | Country (varchar50) |
| ---------------- | --------------------- | -------------------- | ---------------- | --------------------- | ------------------ | ---------------------- | ---------------- | ------------------- |
| 1                | John                  | Hibert               | Male             | 284 chaucer st        | 084789657          | john@gmail.com         | Johannesburg     | South Africa        |
| 2                | Thando                | Sithole              | Female           | 240 Sect 1            | 0794445584         | thando@gmail.com       | Cape Town        | South Africa        |
| 3                | Leon                  | Glen                 | Male             | 81 Everton Rd,Gillits | 0820832830         | Leon@gmail.com         | Durban           | South Africa        |
| 4                | Charl                 | Muller               | Male             | 290A Dorset Ecke      | +44856872553       | Charl.muller@yahoo.com | Berlin           | Germany             |
| 5                | Julia                 | Stein                | Female           | 2 Wernerring          | +448672445058      | Js234@yahoo.com        | Frankfurt        | Germany             |

### Employees Table

| ID (int) | FirstName (varchar50) | LastName (varchar50) | Email (varchar100) | JobTitle (varchar20) |
| ---------------- | --------------------- | -------------------- | ------------------ | -------------------- |
| 1                | Kani                  | Matthew              | mat@gmail.com      | Manager              |
| 2                | Lesly                 | Cronje               | LesC@gmail.com     | Clerk                |
| 3                | Gideon                | Maduku               | m@gmail.com        | Accountant           |

### Orders Table

| Id (int) | ProductID (int) | PaymentID (int) | FulfilledByEmployeeID (int) | DateRequired (datetime) | DateShipped (datetime) | Status (varchar20) |
| ------------- | --------------- | --------------- | --------------------------- | ----------------------- | ---------------------- | ------------------ |
| 1             | 1               | 1               | 2                           | 05-09-2018              |                        | Not shipped        |
| 2             | 1               | 2               | 2                           | 04-09-2018              | 03-09-2018             | Shipped            |
| 3             | 3               | 3               | 3                           | 06-09-2018              |                        | Not shipped        |

Note: When creating tables you will note that each table has an ID column, when joining data between tables the foreign key must include the name of the table the data came from, i.e. `CustomerID` in the above table.
### Payments Table

| CustomerId (int) | ID (int) | PaymentDate (datetime) | Amount (decimal) |
| ---------------- | --------------- | ---------------------- | ---------------- |
| 1                | 1               | 01-09-2018             | R150.75          |
| 5                | 2               | 03-09-2018             | R150.75          |
| 4                | 3               | 03-09-2018             | R700.60          |

Note: When creating tables you will note that each table has an ID column, when joining data between tables the foreign key must include the name of the table the data came from, i.e. `CustomerID` in the above table.
### Products Table

| Id (int) | ProductName (varchar100) | Description (varchar300)                                                    | BuyPrice (decimal) |
| --------------- | ------------------------ | --------------------------------------------------------------------------- | ------------------ |
| 1               | Harley Davidson Chopper  | This replica features a working kickstand, front suspension, gear-shift lever | R150.75            |
| 2               | Classic Car              | Turnable front wheels, steering function                                    | R550.75            |
| 3               | Sportscar               | Turnable front wheels, steering function                                    | R700.60            |

## Part 2: Querying a database

Save all of your instructions in script files - you will submit these files on Github. 

NB! Be sure to label you answers by putting the question above the code that answers it, submitting a wall of code with no explanations makes it difficult to review.

7. SELECT ALL records from table Customers.

8. SELECT records only from the name column in the Customers table.

9. Show the full name of the Customer whose CustomerID is 1.

10. UPDATE the record for CustomerID = 1 on the Customer table so that the name is "Lerato Mabitso".

11. DELETE the record from the Customers table for customer 2 (CustomerID = 2).

12. Select all unique statuses from the Orders table and get a count of the number of orders for each unique status.

13. Return the MAXIMUM payment made on the PAYMENTS table.

14. Select all customers from the "Customers" table, sorted by the "Country" column.

15. Select all products with a price BETWEEN R100 and R600.

16. Select all fields from "Customers" where the country is "Germany" AND the city is "Berlin".

17. Select all fields from "Customers" where the city is "Cape Town" OR "Durban".

18. Select all records from Products where the Price is GREATER than R500.

19. Return the sum of the Amounts on the Payments table.

20. Count the number of shipped orders in the Orders table.

21. Return the average price of all Products, in Rands and Dollars (assume the exchange rate is R12 to the Dollar).

22. Using INNER JOIN create a query that selects all Payments with Customer information.

23. Select all products that have turnable front wheels.

## Files to submit & instructions for reviewer
- YAML/yml file with container setup.
- `src` directory with 4 SQL script files(a script to create a database, create tables, populate tables and one to query the database).
- A `.md` needs to be present in the repo where the learner has documented what information is in which table and how the tables and which keys link the records between tables.
- The ID columns of the tables can either be TableName + ID or just ID, either is acceptable due to recent updates.
