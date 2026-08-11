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
  - topics/solo-learn/sql-intermediate/3-working-with-data
  - docker/intro-to-docker/
  - topics/clean-code/sql
  soft: []
ready: true
story_points: 3
submission_type: repo
tags:
- sql
- skill/databases
title: Shop Database using sql
---

## Installation

- We are using Postgres with Docker.
- Instead of installing Postgres on your computer, you can launch it with a Docker composition.
- MySQL is nice and lots of people use it in the industry, but it doesn't implement standard SQL; it sort of does its own thing a bit. Postgres is a much more standard DB, and the industry loves it.

**NB! Many learners configure the docker-compose.yaml file to make use of the Adminer image but still instruct reviewers to download and install Postgres on their local machines in the documentation. This indicates a misunderstanding of the relationship between these technologies.**

  To Clarify:
  - Docker allows you to run applications in isolated containers.
  - Docker Compose is a tool for defining and running multi-container Docker applications.
  - Using Docker and Docker Compose, you can set up your entire environment, including Postgres and Adminer, without requiring any local installations on the reviewer’s machine.
  
  Ensure the documentation reflects this setup correctly, so reviewers do not need to install Postgres locally. Refer to the following resources for more information:
  - {{< contentlink path="docker/intro-to-docker/" >}}
  - [How to Set Up Postgres and Adminer with Docker Compose](https://codepruner.com/how-to-run-postgresql-and-adminer-or-pgadmin-with-docker-compose/)  

## Structure

- Your repository should have a **.yml** file.
- Your repository should have **.sql** files. The different SQL commands should be saved in different descriptive script files i.e.
  - When the reviewer is looking for the commands you used for creating the database, they should be able to navigate to a file named **create-database.sql**.
  - Navigate to a file named **create-tables.sql** for the commands used to create the database tables.
  - Navigate to a file that contains the commands used for inserting table records.
  - Navigate to a file that contains commands used for querying the database.
- Your repository should have a new **.md** file for documenting the database.

## Instructions

### IMPORTANT

You should know about clean sql code by now. If you need a refresher please take a look here: {{< contentlink path="topics/clean-code/sql" >}}

The names of the tables and columns described in this project are funky (not in a good way).

While doing this project, please ensure that all names are clear and adhere to clean code standards.

### Part 1: Creating a database

Save all of your instructions in script files - you will submit these files on Github.

1. Create a database called "shop".

2. Create the following tables in the shop database:

   - Customers
   - Employees
   - Orders
   - Payments
   - Products

3. Create a primary key for each table with auto-increment. Ensure you correctly specify the data types (e.g. the ID field should be `int`).

4. Create foreign keys so that every ID in the Orders and Payments tables references an existing ID in the tables referenced (e.g., ProductID, EmployeeID, etc).

5. Insert the records from the tables below into the table created in step 2

6. Document the information stored in your database. Specify what information is kept in each table and identify the keys that link records between tables. Save this document in a `.md` format.

#### Customers Table

| ID (int) | FirstName (varchar50) | LastName (varchar50) | Gender (varchar) | Address (varchar200)  | Phone (varchar 20) | Email (varchar100)     | City (varchar20) | Country (varchar50) |
| -------- | --------------------- | -------------------- | ---------------- | --------------------- | ------------------ | ---------------------- | ---------------- | ------------------- |
| 1        | John                  | Hibert               | Male             | 284 chaucer st        | 084789657          | john@gmail.com         | Johannesburg     | South Africa        |
| 2        | Thando                | Sithole              | Female           | 240 Sect 1            | 0794445584         | thando@gmail.com       | Cape Town        | South Africa        |
| 3        | Leon                  | Glen                 | Male             | 81 Everton Rd,Gillits | 0820832830         | Leon@gmail.com         | Durban           | South Africa        |
| 4        | Charl                 | Muller               | Male             | 290A Dorset Ecke      | +44856872553       | Charl.muller@yahoo.com | Berlin           | Germany             |
| 5        | Julia                 | Stein                | Female           | 2 Wernerring          | +448672445058      | Js234@yahoo.com        | Frankfurt        | Germany             |

#### Employees Table

| ID (int) | FirstName (varchar50) | LastName (varchar50) | Email (varchar100) | JobTitle (varchar20) |
| -------- | --------------------- | -------------------- | ------------------ | -------------------- |
| 1        | Kani                  | Matthew              | mat@gmail.com      | Manager              |
| 2        | Lesly                 | Cronje               | LesC@gmail.com     | Clerk                |
| 3        | Gideon                | Maduku               | m@gmail.com        | Accountant           |

#### Orders Table

| ID (int) | ProductID (int) | PaymentID (int) | FulfilledByEmployeeID (int) | DateRequired (datetime) | DateShipped (datetime) | Status (varchar20) |
| -------- | --------------- | --------------- | --------------------------- | ----------------------- | ---------------------- | ------------------ |
| 1        | 1               | 1               | 2                           | 05-09-2018              |                        | Not shipped        |
| 2        | 1               | 2               | 2                           | 04-09-2018              | 03-09-2018             | Shipped            |
| 3        | 3               | 3               | 3                           | 06-09-2018              |                        | Not shipped        |

Note: When creating tables, each table will have an ID column. When joining data between tables, the foreign key must include the name of the table the data came from, e.g., `ProductID` in the above table.

#### Payments Table

| ID (int) | CustomerID (int) | PaymentDate (datetime) | Amount (decimal) |
| -------- | ---------------- | ---------------------- | ---------------- |
| 1        | 1                | 01-09-2018             | R150.75          |
| 2        | 5                | 03-09-2018             | R150.75          |
| 3        | 4                | 03-09-2018             | R700.60          |

Note: When creating tables, you will note that each table has an ID column. When joining data between tables, the foreign key must include the name of the table the data came from, i.e. `CustomerID` in the above table.

#### Products Table

| ID (int) | ProductName (varchar100) | Description (varchar300)                                                      | BuyPrice (decimal) |
| -------- | ------------------------ | ----------------------------------------------------------------------------- | ------------------ |
| 1        | Harley Davidson Chopper  | This replica features a working kickstand, front suspension, gear-shift lever | R150.75            |
| 2        | Classic Car              | Turnable front wheels, steering function                                      | R550.75            |
| 3        | Sportscar                | Turnable front wheels, steering function                                      | R700.60            |

### Part 2: Querying a database

Save all of your instructions in script files - you will submit these files on Github.

**NB! Be sure to label your answers by placing the question above the corresponding code. Submitting a wall of code without explanations makes it difficult to review.**

1. Select all records from the `Customers` table.

2. Select only the `FirstName` column from the `Customers` table

3. Display the full name of the customer with `CustomerID` **1**.

4. Update the record for `CustomerID` **1** in the `Customers` table to change the name to "Lerato Mabitso".

5. Delete the record for the customer with `CustomerID` **2** from the `Customers` table.

6. Select all unique statuses from the `Orders` table and count the number of orders for each status.

7. Return the maximum payment made in the `Payments` table.

8. Select all customers from the `Customers` table, sorted by the `Country` column.

9. Select all products with a price between R100 and R600.

10. Select all fields from `Customers` where the `Country` is "Germany" AND the `City` is "Berlin".

11. Select all fields from `Customers` where the `City` is either "Cape Town" OR "Durban".

12. Select all records from `Products` where the price is greater than R500.

13. Return the total sum of the amounts in the `Payments` table.

14. Count the number of shipped orders in the `Orders` table.

15. Return the average price of all products, both in Rands and in Dollars (assuming the exchange rate is R12 to the Dollar).

16. Using an `INNER JOIN`, create a query that selects all payments along with the corresponding customer information.

17. Select all products that have turnable front wheels.

## Files to submit & instructions for reviewer

- Please make sure that the learner used Postgres and not MySQL.
- The ID columns of the tables can either be TableName + ID or just ID, either is acceptable due to recent updates.

- The following files should be present:
  - YAML/yml file with container setup.
  - The `src` directory should contain 4 SQL script files: one to create the database, one to create tables, one to populate tables, and one to query the database.
  - A new .md file needs to be present in the repository where the learner has documented what information is in each table, how the tables are related, and which keys link the records between tables. The README.md file should not be edited, as it serves its own purpose.
  
- Ensure the learner has adapted the naming conventions to match those specified in {{< contentlink path="topics/clean-code/sql" >}}