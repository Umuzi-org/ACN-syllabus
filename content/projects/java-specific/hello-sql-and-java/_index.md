---
_db_id: 204
available_flavours:
- java
content_type: project
prerequisites:
  hard:
  - projects/java-specific/introduction-to-spring-boot/part-4
  - topics/java-specific/jdbc-templates
  soft:
  - projects/sql
submission_type: repo
title: SQL Extended
---

I hope at this point you should have already read up on JDBC templates, JPA and Hibernate from the topic resources. In this project we wil re-visit you SQl project. Instead of only using scripts to create and interact with your database you are doing to do this using java + scripts. You will be using dataSources to configured your connection to your database and query your tables.

## Part1

1. Revise {{% contentlink path="projects/sql/" %}} and make sure all tables are created and populated

2. Use vanilla java **(no Springboot)** connect to your database and perform the queries in part2 but only number [1-7]

3. Use Springboot JDBC templates to connect to your database and perform the queries in part2 but only number [1-9]

**Added Bonus**

4. Lastly I would like you to use Hibernate + JPA to connect to your database and perform the queries in part2 [1-17]

**Don't forget to test your application**

## Part 2: Querying a database (Reminder)

Save all of your instructions in a script file - you will submit this file on Gnomio and github.

1. SELECT ALL records from table Customers.

2. SELECT records only from the name column in the Customers table.

3. Show the name of the Customer whose CustomerID is 1.

4. UPDATE the record for CustomerID = 1 on the Customer table so that the name is “Lerato Mabitso”.

5. DELETE the record from the Customers table for customer 2 (CustomerID = 2).

6. Select all unique statuses from the Orders table and get a count of the number of orders for each unique status.

7. Return the MAXIMUM payment made on the PAYMENTS table.

8. Select all customers from the “Customers” table, sorted by the “Country” column.

9. Select all products with a price BETWEEN R100 and R600.

10. Select all fields from “Customers” where country is “Germany” AND city is “Berlin”.

11. Select all fields from “Customers” where city is “Cape Town” OR “Durban”.

12. Select all records from Products where the Price is GREATER than R500.

13. Return the sum of the Amounts on the Payments table.

14. Count the number of shipped orders in the Orders table.

15. Return the average price of all Products, in Rands and in Dollars (assume the exchange rate is R12 to the Dollar).

16. Using INNER JOIN create a query that selects all Payments with Customer information.

17. Select all products that have turnable front wheels.